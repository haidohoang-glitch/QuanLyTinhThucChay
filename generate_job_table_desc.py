"""
generate_job_table_desc.py
--------------------------
Kết nối SQL Server để lấy dữ liệu từ 2 bảng do người dùng tự định nghĩa:
1. Job_desc   : Chứa thông tin phân loại (0=Sync, 1=Tính toán) và mô tả chi tiết của Job.
2. Table_desc : Chứa thông tin nhóm sản phẩm dùng bảng nào và ý nghĩa của bảng.

Đầu ra:
    context/04_JOB_DESC.md
    context/05_TABLE_DESC.md
"""

import argparse
import os
import sys
from dotenv import load_dotenv

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

try:
    import pyodbc
except ImportError:
    print("❌ Thiếu thư viện pyodbc. Cài đặt: pip install pyodbc")
    sys.exit(1)

_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(_env_path)


# ─────────────────────────────────────────────────────────────────────────────
# KẾT NỐI DB
# ─────────────────────────────────────────────────────────────────────────────
def get_connection(args) -> pyodbc.Connection:
    driver = args.driver
    if not driver:
        available = [d for d in pyodbc.drivers() if "SQL Server" in d]
        if not available:
            print("❌ Không tìm thấy ODBC Driver for SQL Server.")
            sys.exit(1)
        driver = sorted(available)[-1]
    
    base = f"DRIVER={{{driver}}};SERVER={args.server};DATABASE={args.database};"
    conn_str = base + (f"UID={args.user};PWD={args.password};" if args.user and args.password else "Trusted_Connection=yes;")
    
    try:
        return pyodbc.connect(conn_str, timeout=10)
    except pyodbc.Error as e:
        print(f"❌ Kết nối thất bại: {e}")
        sys.exit(1)


def fetch_all(conn, sql):
    cur = conn.cursor()
    cur.execute(sql)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


# ─────────────────────────────────────────────────────────────────────────────
# TRUY VẤN
# ─────────────────────────────────────────────────────────────────────────────

# !! NẾU TÊN CỘT TRONG BẢNG CỦA BẠN KHÁC, HÃY SỬA LẠI Ở ĐÂY !!

SQL_JOB_DESC = """
SELECT 
    JOB_NAMES, 
    JOB_TYPE_NAME, 
    JOB_DESC 
FROM dbo.Job_desc
ORDER BY JOB_TYPE_NAME, JOB_NAMES;
"""

SQL_TABLE_DESC = """
SELECT 
    NhomSanPhamLevel1, 
    TenBang, 
    YNghiaCuaBang 
FROM dbo.Table_desc
ORDER BY NhomSanPhamLevel1, TenBang;
"""


# ─────────────────────────────────────────────────────────────────────────────
# MAIN LOGIC
# ─────────────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--server", "-S", default=os.getenv("DB_SERVER") or "")
    parser.add_argument("--database", "-D", default=os.getenv("DB_DATABASE") or "")
    parser.add_argument("--user", "-U", default=os.getenv("DB_USER"))
    parser.add_argument("--password", "-P", default=os.getenv("DB_PASSWORD"))
    parser.add_argument("--driver", default=os.getenv("DB_DRIVER"))
    parser.add_argument("--output", "-o", default="context")
    args = parser.parse_args()

    out_dir = os.path.abspath(args.output)
    os.makedirs(out_dir, exist_ok=True)

    print("🔌 Đang kết nối Database...")
    conn = get_connection(args)

    # ---------------------------------------------------------
    # 1. Gen bảng Job_desc
    # ---------------------------------------------------------
    print("📋 Đang lấy dữ liệu từ bảng Job_desc...")
    try:
        jobs = fetch_all(conn, SQL_JOB_DESC)
        
        lines_job = [
            "# 04 — Danh mục Job (Job_desc)",
            "",
            "> **Ghi chú**: `job_type_name = 0` (Job lấy dữ liệu / Sync), `job_type_name = 1` (Job tính toán thực chạy)",
            "",
            "| Tên Job | Loại Job | Ý nghĩa / Mô tả chi tiết |",
            "|---------|----------|--------------------------|"
        ]
        
        for j in jobs:
            j_name = j.get('JOB_NAMES', '')
            j_type = "0 (Sync Data)" if str(j.get('JOB_TYPE_NAME', '')) == '0' else "1 (Calc Data)"
            j_desc = str(j.get('JOB_DESC', '')).replace('\n', ' ')
            lines_job.append(f"| `{j_name}` | {j_type} | {j_desc} |")
            
        out_job = os.path.join(out_dir, "04_JOB_DESC.md")
        with open(out_job, "w", encoding="utf-8") as f:
            f.write("\n".join(lines_job))
        print(f"✅ Đã tạo {out_job}")

    except Exception as e:
        print(f"⚠️ Lỗi khi truy vấn Job_desc (Có thể tên cột/bảng không đúng): {e}")

    # ---------------------------------------------------------
    # 2. Gen bảng Table_desc
    # ---------------------------------------------------------
    print("📋 Đang lấy dữ liệu từ bảng Table_desc...")
    try:
        tables = fetch_all(conn, SQL_TABLE_DESC)
        
        lines_tbl = [
            "# 05 — Danh mục Bảng Dữ liệu (Table_desc)",
            "",
            "> Cấu hình Bảng đích & Bảng nguồn dùng cho từng nhóm sản phẩm.",
            "",
            "| Nhóm Sản Phẩm | Tên Bảng (Table) | Ý nghĩa / Mục đích sử dụng |",
            "|---------------|------------------|----------------------------|"
        ]
        
        for t in tables:
            t_nhom = t.get('NhomSanPhamLevel1', '')
            t_name = t.get('TenBang', '')
            t_desc = str(t.get('YNghiaCuaBang', '')).replace('\n', ' ')
            lines_tbl.append(f"| {t_nhom} | `{t_name}` | {t_desc} |")
            
        out_tbl = os.path.join(out_dir, "05_TABLE_DESC.md")
        with open(out_tbl, "w", encoding="utf-8") as f:
            f.write("\n".join(lines_tbl))
        print(f"✅ Đã tạo {out_tbl}")

    except Exception as e:
        print(f"⚠️ Lỗi khi truy vấn Table_desc (Có thể tên cột/bảng không đúng): {e}")

    conn.close()
    print("\n🎉 Xong! Hãy kiểm tra thư mục context/ nhé.")

if __name__ == "__main__":
    main()
