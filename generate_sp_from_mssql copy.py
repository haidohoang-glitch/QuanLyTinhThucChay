"""
generate_sp_from_mssql.py
--------------------------
Kết nối vào SQL Server bằng Windows Authentication, đọc tất cả Stored Procedures (SP)
và Functions (FN), sau đó sinh ra các file .md để AI dễ dàng đọc hiểu.

Định dạng file MD:
    stored_procedures/
    ├── SP_ThucChay_CPD_Job.md
    ├── FN_GetDonGia.md
    └── ...

Yêu cầu:
    pip install pyodbc python-dotenv

Config:
    Sử dụng chung file .env với tool gen tables.
"""

import argparse
import os
import sys
import textwrap
from collections import defaultdict

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

try:
    import pyodbc
except ImportError:
    print("❌  Thiếu thư viện pyodbc.")
    print("    Cài đặt: pip install pyodbc")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print("❌  Thiếu thư viện python-dotenv.")
    print("    Cài đặt: pip install python-dotenv")
    sys.exit(1)

# Load .env
_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(_env_path)


# ─────────────────────────────────────────────────────────────────────────────
# 1.  Kết nối SQL Server
# ─────────────────────────────────────────────────────────────────────────────

def build_connection_string(server: str, database: str, user: str | None, password: str | None, driver: str) -> str:
    base = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};"
    if user and password:
        return base + f"UID={user};PWD={password};"
    # Windows Authentication mặc định
    return base + "Trusted_Connection=yes;"

def get_connection(args) -> pyodbc.Connection:
    driver = args.driver
    if not driver:
        available = [d for d in pyodbc.drivers() if "SQL Server" in d]
        if not available:
            print("❌  Không tìm thấy ODBC Driver for SQL Server.")
            sys.exit(1)
        driver = sorted(available)[-1]
        print(f"ℹ️   Dùng driver: {driver}")

    conn_str = build_connection_string(args.server, args.database, args.user, args.password, driver)
    try:
        conn = pyodbc.connect(conn_str, timeout=10)
        print(f"✅  Kết nối thành công → [{args.server}].[{args.database}]")
        return conn
    except pyodbc.Error as e:
        print(f"❌  Kết nối thất bại: {e}")
        sys.exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# 2.  Truy vấn dữ liệu SP/FN
# ─────────────────────────────────────────────────────────────────────────────

SQL_ROUTINES = """
SELECT 
    o.name AS routine_name,
    o.type AS routine_type_code,
    o.type_desc AS routine_type,
    m.definition AS routine_definition,
    o.create_date,
    o.modify_date
FROM sys.objects o
JOIN sys.sql_modules m ON o.object_id = m.object_id
WHERE o.type IN ('P', 'FN', 'IF', 'TF') 
  AND o.is_ms_shipped = 0
  AND o.name IN ({placeholders})
ORDER BY o.name;
"""

SQL_PARAMETERS = """
SELECT 
    o.name AS routine_name,
    p.name AS param_name,
    t.name AS data_type,
    p.max_length,
    p.is_output
FROM sys.parameters p
JOIN sys.objects o ON p.object_id = o.object_id
JOIN sys.types t ON p.user_type_id = t.user_type_id
WHERE o.type IN ('P', 'FN', 'IF', 'TF') 
  AND o.is_ms_shipped = 0
  AND o.name IN ({placeholders})
ORDER BY o.name, p.parameter_id;
"""

def fetch_all(conn: pyodbc.Connection, sql: str, params: list = None) -> list[dict]:
    cur = conn.cursor()
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


# ─────────────────────────────────────────────────────────────────────────────
# 2b.  Đọc danh sách SP từ các file FLOW_*.md
# ─────────────────────────────────────────────────────────────────────────────

import re

def extract_sp_names_from_flows(flow_dir: str) -> set[str]:
    """Quét tất cả file FLOW_*.md trong thư mục, trích xuất tên SP/FN xuất hiện trong bảng parameters."""
    sp_names = set()
    
    # Tìm tất cả FLOW_*.md trong thư mục
    flow_files = [
        os.path.join(flow_dir, f)
        for f in os.listdir(flow_dir)
        if f.upper().startswith("FLOW_") and f.endswith(".md")
    ]
    
    if not flow_files:
        print(f"⚠️  Không tìm thấy file FLOW_*.md nào trong: {flow_dir}")
        return sp_names
    
    print(f"📚  Đang quét {len(flow_files)} file FLOW_*.md...")
    
    # Regex: trích xuất tên nằm trong các đoạn `code` của bảng Markdown
    # Ví dụ: | `ThucChay_CPD_Job` | ... |
    pattern = re.compile(r'\|\s*`([^`]+)`\s*\|')
    
    for fpath in flow_files:
        with open(fpath, encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
        matches = pattern.findall(content)
        for m in matches:
            sp_names.add(m.strip())
    
    print(f"✅  Tìm thấy {len(sp_names)} SP/FN nằm trong các luồng.")
    return sp_names


# ─────────────────────────────────────────────────────────────────────────────
# 3.  Sinh file .md cho AI
# ─────────────────────────────────────────────────────────────────────────────

def generate_md_content(routine: dict, parameters: list[dict]) -> str:
    r_type = routine["routine_type_code"].strip()
    type_label = "Stored Procedure" if r_type == "P" else "Function"
    
    lines = [
        f"# {type_label}: `{routine['routine_name']}`",
        "",
        f"- **Loại**: {routine['routine_type']}",
        f"- **Ngày tạo**: {routine['create_date']}",
        f"- **Ngày sửa cuối**: {routine['modify_date']}",
        "",
    ]

    # Render Parameters
    if parameters:
        lines.extend([
            "## Parameters",
            "",
            "| Parameter | Type | Output |",
            "|-----------|------|--------|"
        ])
        for p in parameters:
            p_name = p['param_name'] if p['param_name'] else "(Return Value)"
            p_type = f"{p['data_type']}({p['max_length']})" if p['max_length'] > 0 else p['data_type']
            is_output = "Yes" if p['is_output'] else "No"
            lines.append(f"| `{p_name}` | `{p_type}` | {is_output} |")
        lines.append("")
    else:
        lines.extend(["## Parameters", "", "*(Không có tham số)*", ""])

    # Render Code SQL
    lines.extend([
        "## Definition (Source Code)",
        "",
        "```sql",
        routine["routine_definition"] if routine["routine_definition"] else "-- NO DEFINITION FOUND",
        "```",
        ""
    ])
    
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# 4.  Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    _default_server   = os.getenv("DB_SERVER")   or ""
    _default_database = os.getenv("DB_DATABASE") or ""
    _default_user     = os.getenv("DB_USER")     or None
    _default_password = os.getenv("DB_PASSWORD") or None
    _default_driver   = os.getenv("DB_DRIVER")   or None
    _default_output   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "stored_procedures")

    parser = argparse.ArgumentParser(description="Gen SP/Function SQL Server ra file MD cho AI.")
    parser.add_argument("--server",   "-S", default=_default_server)
    parser.add_argument("--database", "-D", default=_default_database)
    parser.add_argument("--user",     "-U", default=_default_user)
    parser.add_argument("--password", "-P", default=_default_password)
    parser.add_argument("--driver",         default=_default_driver)
    parser.add_argument("--output",   "-o", default=_default_output, help="Thư mục xuất file (mặc định: ./stored_procedures)")
    args = parser.parse_args()

    if not args.server or not args.database:
        print("❌ Thiếu cấu hình --server hoặc --database. Vui lòng kiểm tra file .env")
        sys.exit(1)

    conn = get_connection(args)

    # Bước 1: Đọc danh sách SP từ FLOW_*.md
    out_dir = os.path.abspath(args.output)
    sp_in_flows = extract_sp_names_from_flows(out_dir)
    
    if not sp_in_flows:
        print("❌ Không có tên SP nào được tìm thấy từ các file FLOW_*.md. Hãy chạy generate_sp_flow_mssql.py trước.")
        sys.exit(1)

    # Bước 2: Truy vấn DB chỉ lấy những SP/FN thuộc luồng
    print(f"📋  Đang truy vấn {len(sp_in_flows)} SP/FN từ database...")
    placeholders = ", ".join("?" * len(sp_in_flows))
    sp_list = list(sp_in_flows)
    
    sql_routines = SQL_ROUTINES.replace("{placeholders}", placeholders)
    sql_params   = SQL_PARAMETERS.replace("{placeholders}", placeholders)
    
    routines = fetch_all(conn, sql_routines, sp_list)
    params   = fetch_all(conn, sql_params, sp_list)
    conn.close()

    if not routines:
        print("⚠️   Không tìm thấy SP/FN nào khớp trong database (kiểm tra lại tên trong FLOW_*.md).")
        sys.exit(0)

    print(f"🗂️   Tìm thấy {len(routines)}/{len(sp_in_flows)} SP/FN trong database.")

    # Gom tham số theo routine
    params_by_routine = defaultdict(list)
    for p in params:
        params_by_routine[p["routine_name"]].append(p)

    # Tạo folder nếu chưa có
    out_dir = os.path.abspath(args.output)
    os.makedirs(out_dir, exist_ok=True)
    
    print("✍️   Đang tạo/ghi đè các file MD...")

    # Gen file mới (nếu file đã tồn tại thì sẽ được ghi đè do chế độ "w")
    for r in routines:
        name = r["routine_name"]
        prefix = "SP_" if r["routine_type_code"].strip() == "P" else "FN_"
        safe_name = "".join(c for c in name if c.isalnum() or c in "_-")
        
        file_name = f"{prefix}{safe_name}.md"
        content = generate_md_content(r, params_by_routine.get(name, []))
        
        with open(os.path.join(out_dir, file_name), "w", encoding="utf-8") as f:
            f.write(content)

    print()
    print(f"✅  Hoàn tất! Đã tạo file MD cho AI đọc tại: {out_dir}")

if __name__ == "__main__":
    main()
