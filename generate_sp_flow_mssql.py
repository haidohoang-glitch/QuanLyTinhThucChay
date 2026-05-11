"""
generate_sp_flow_mssql.py
--------------------------
Phân tích luồng gọi (Dependency Flow) bắt đầu từ 1 SP gốc (Level 1).
Sinh ra file Markdown bao gồm:
1. Sơ đồ Mermaid mô tả Call Graph.
2. Danh sách các SP trong luồng và các tham số đầu vào.

Cách dùng:
    python generate_sp_flow_mssql.py --root_sp "ThucChay_CPD_Job"
"""

import argparse
import os
import sys
import pyodbc
from dotenv import load_dotenv
from collections import defaultdict

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# Load .env
_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(_env_path)

def build_connection_string(server: str, database: str, user: str | None, password: str | None, driver: str) -> str:
    base = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};"
    if user and password:
        return base + f"UID={user};PWD={password};"
    return base + "Trusted_Connection=yes;"

def get_connection(args) -> pyodbc.Connection:
    driver = args.driver
    if not driver:
        available = [d for d in pyodbc.drivers() if "SQL Server" in d]
        if not available:
            print("❌ Không tìm thấy ODBC Driver for SQL Server.")
            sys.exit(1)
        driver = sorted(available)[-1]
    
    conn_str = build_connection_string(args.server, args.database, args.user, args.password, driver)
    try:
        conn = pyodbc.connect(conn_str, timeout=10)
        return conn
    except pyodbc.Error as e:
        print(f"❌ Kết nối thất bại: {e}")
        sys.exit(1)

SQL_DEPENDENCIES = """
WITH DependencyTree AS (
    -- Root Level 1
    SELECT 
        referencing_id,
        OBJECT_NAME(referencing_id) AS caller_name,
        referenced_id,
        referenced_entity_name AS called_name,
        1 AS Level
    FROM sys.sql_expression_dependencies
    WHERE OBJECT_NAME(referencing_id) = ?

    UNION ALL

    -- Recursive Level > 1
    SELECT 
        d.referencing_id,
        OBJECT_NAME(d.referencing_id) AS caller_name,
        d.referenced_id,
        d.referenced_entity_name AS called_name,
        t.Level + 1
    FROM sys.sql_expression_dependencies d
    INNER JOIN DependencyTree t ON d.referencing_id = t.referenced_id
    -- Tránh lặp vòng lặp vô hạn nếu có (dù SP ít khi bị)
    WHERE t.Level < 10
)
SELECT DISTINCT caller_name, called_name, Level
FROM DependencyTree
WHERE called_name IS NOT NULL
ORDER BY Level, caller_name, called_name;
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
WHERE o.name IN ({})
ORDER BY o.name, p.parameter_id;
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", "-S", default=os.getenv("DB_SERVER") or "")
    parser.add_argument("--database", "-D", default=os.getenv("DB_DATABASE") or "")
    parser.add_argument("--user", "-U", default=os.getenv("DB_USER"))
    parser.add_argument("--password", "-P", default=os.getenv("DB_PASSWORD"))
    parser.add_argument("--driver", default=os.getenv("DB_DRIVER"))
    parser.add_argument("--root_sp", required=True, help="Tên SP gốc (Level 1)")
    parser.add_argument("--output_dir", default="stored_procedures", help="Thư mục xuất file")
    args = parser.parse_args()

    if not args.server or not args.database:
        print("❌ Thiếu cấu hình DB.")
        sys.exit(1)

    conn = get_connection(args)
    cur = conn.cursor()

    # 1. Truy vấn Dependencies
    root_sp = args.root_sp
    print(f"🔍 Đang phân tích luồng gọi từ SP: {root_sp}...")
    
    cur.execute(SQL_DEPENDENCIES, (root_sp,))
    flows = []
    involved_sps = set([root_sp])
    
    for row in cur.fetchall():
        caller = row[0]
        called = row[1]
        level = row[2]
        flows.append({"caller": caller, "called": called, "level": level})
        involved_sps.add(caller)
        involved_sps.add(called)

    if not flows:
        print(f"⚠️ Không tìm thấy lời gọi SP con nào từ {root_sp} hoặc SP không tồn tại.")
    else:
        print(f"🔗 Tìm thấy {len(flows)} liên kết gọi hàm.")

    # 2. Truy vấn Parameters cho các SP liên quan
    params_by_sp = defaultdict(list)
    if involved_sps:
        placeholders = ",".join("?" * len(involved_sps))
        sql_params = SQL_PARAMETERS.format(placeholders)
        cur.execute(sql_params, list(involved_sps))
        for row in cur.fetchall():
            params_by_sp[row[0]].append({
                "param_name": row[1],
                "data_type": row[2],
                "max_length": row[3],
                "is_output": row[4]
            })

    conn.close()

    # 3. Tạo file Markdown
    os.makedirs(args.output_dir, exist_ok=True)
    out_file = os.path.join(args.output_dir, f"FLOW_{root_sp}.md")
    
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f"# Phân tích Luồng nghiệp vụ: `{root_sp}`\n\n")
        
        # Mermaid Sơ đồ
        f.write("## 1. Sơ đồ Call Graph (Mermaid)\n\n")
        f.write("```mermaid\n")
        f.write("graph TD\n")
        
        # Thêm node gốc
        f.write(f"    {root_sp}[{root_sp}]:::rootNode\n")
        
        for flow in flows:
            caller = flow['caller']
            called = flow['called']
            f.write(f"    {caller} -->|Level {flow['level']}| {called}\n")
            
        f.write("\n    classDef rootNode fill:#f9f,stroke:#333,stroke-width:4px;\n")
        f.write("```\n\n")

        # Chi tiết biến
        f.write("## 2. Chi tiết Biến Đầu Vào (Parameters)\n\n")
        
        # Sắp xếp các SP có liên quan
        for sp in sorted(involved_sps):
            f.write(f"### `{sp}`\n")
            p_list = params_by_sp.get(sp, [])
            if p_list:
                f.write("| Tên tham số | Kiểu dữ liệu | Output |\n")
                f.write("|-------------|--------------|--------|\n")
                for p in p_list:
                    p_name = p['param_name'] or "(Return)"
                    p_type = f"{p['data_type']}({p['max_length']})" if p['max_length'] > 0 else p['data_type']
                    is_out = "Có" if p['is_output'] else "Không"
                    f.write(f"| `{p_name}` | `{p_type}` | {is_out} |\n")
                f.write("\n")
            else:
                f.write("*(Không có tham số)*\n\n")

    print(f"✅ Hoàn tất! Đã xuất file tài liệu tại: {out_file}")

if __name__ == "__main__":
    main()
