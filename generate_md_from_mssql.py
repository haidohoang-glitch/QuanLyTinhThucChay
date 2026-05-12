"""
generate_md_from_mssql.py
--------------------------
Kết nối vào SQL Server, đọc schema thật lấy thông tin table (bảng, cột, index, FK),
rồi sinh ra bộ file .md theo đúng cấu trúc dự án này:

    output_dir/
    ├── README.md
    ├── relations.md
    └── tables/
        ├── <table1>.md
        ├── <table2>.md
        └── ...

Yêu cầu:
    pip install pyodbc python-dotenv

Config:
    Tạo file .env (xem .env.example) với các biến:
        DB_SERVER, DB_DATABASE, DB_USER, DB_PASSWORD, DB_DRIVER, OUTPUT_DIR

Cách dùng:
    # Dùng .env (khuyến khích)
    python generate_md_from_mssql.py

    # Override tham số qua CLI (ưu tiên hơn .env)
    python generate_md_from_mssql.py --server localhost --database GameBoard

    # Chỉ định thư mục đầu ra
    python generate_md_from_mssql.py --output ./schema
"""

import argparse
import os
import sys
import textwrap
from collections import defaultdict

# ── Kiểm tra dependencies ────────────────────────────────────────────────────
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

# Load .env từ cùng thư mục với script
_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(_env_path)


# ─────────────────────────────────────────────────────────────────────────────
# 1.  Kết nối SQL Server
# ─────────────────────────────────────────────────────────────────────────────

def build_connection_string(
    server: str,
    database: str,
    user: str | None,
    password: str | None,
    driver: str,
) -> str:
    base = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};"
    if user and password:
        return base + f"UID={user};PWD={password};"
    # Windows Authentication
    return base + "Trusted_Connection=yes;"


def get_connection(args) -> pyodbc.Connection:
    # Thử tự động tìm driver nếu không chỉ định
    driver = args.driver
    if not driver:
        available = [d for d in pyodbc.drivers() if "SQL Server" in d]
        if not available:
            print("❌  Không tìm thấy ODBC Driver for SQL Server trên máy này.")
            print("    Tải về: https://aka.ms/downloadmsodbcsql")
            sys.exit(1)
        # Ưu tiên driver mới nhất (số version cao nhất)
        driver = sorted(available)[-1]
        print(f"ℹ️   Dùng driver: {driver}")

    conn_str = build_connection_string(
        server=args.server,
        database=args.database,
        user=args.user,
        password=args.password,
        driver=driver,
    )
    try:
        conn = pyodbc.connect(conn_str, timeout=10)
        print(f"✅  Kết nối thành công → [{args.server}].[{args.database}]")
        return conn
    except pyodbc.Error as e:
        print(f"❌  Kết nối thất bại: {e}")
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# 2.  Truy vấn schema
# ─────────────────────────────────────────────────────────────────────────────

SQL_TABLES = """
SELECT
    t.name          AS table_name,
    ep.value        AS table_description
FROM sys.tables t
LEFT JOIN sys.extended_properties ep
    ON ep.major_id   = t.object_id
    AND ep.minor_id  = 0
    AND ep.name      = 'MS_Description'
WHERE t.is_ms_shipped = 0
ORDER BY t.name;
"""

SQL_COLUMNS = """
SELECT
    t.name                          AS table_name,
    c.column_id                     AS col_order,
    c.name                          AS col_name,
    tp.name                         AS base_type,
    c.max_length,
    c.precision,
    c.scale,
    c.is_nullable,
    c.is_identity,
    dc.definition                   AS default_value,
    ep.value                        AS col_description,
    -- PK check
    CASE WHEN pk.column_id IS NOT NULL THEN 1 ELSE 0 END AS is_pk,
    -- FK check
    fkc.parent_object_id            AS fk_parent_obj,
    ref_t.name                      AS fk_ref_table,
    ref_c.name                      AS fk_ref_col
FROM sys.tables t
JOIN sys.columns c          ON c.object_id  = t.object_id
JOIN sys.types  tp          ON tp.user_type_id = c.user_type_id
LEFT JOIN sys.default_constraints dc
    ON dc.object_id = c.default_object_id
LEFT JOIN sys.extended_properties ep
    ON ep.major_id  = c.object_id
    AND ep.minor_id = c.column_id
    AND ep.name     = 'MS_Description'
-- PK
LEFT JOIN (
    SELECT ic.object_id, ic.column_id
    FROM sys.index_columns ic
    JOIN sys.indexes i ON i.object_id = ic.object_id AND i.index_id = ic.index_id
    WHERE i.is_primary_key = 1
) pk ON pk.object_id = c.object_id AND pk.column_id = c.column_id
-- FK
LEFT JOIN sys.foreign_key_columns fkc
    ON fkc.parent_object_id  = c.object_id
    AND fkc.parent_column_id = c.column_id
LEFT JOIN sys.tables  ref_t ON ref_t.object_id = fkc.referenced_object_id
LEFT JOIN sys.columns ref_c
    ON ref_c.object_id  = fkc.referenced_object_id
    AND ref_c.column_id = fkc.referenced_column_id
WHERE t.is_ms_shipped = 0
ORDER BY t.name, c.column_id;
"""

SQL_INDEXES = """
SELECT
    t.name          AS table_name,
    i.name          AS index_name,
    i.is_unique,
    i.is_primary_key,
    -- STUFF + FOR XML PATH: tương thích mọi version SQL Server (2008+)
    STUFF((
        SELECT ', ' + c2.name + CASE ic2.is_descending_key WHEN 1 THEN ' DESC' ELSE '' END
        FROM sys.index_columns ic2
        JOIN sys.columns c2
            ON c2.object_id  = ic2.object_id
            AND c2.column_id = ic2.column_id
        WHERE ic2.object_id          = i.object_id
          AND ic2.index_id           = i.index_id
          AND ic2.is_included_column = 0
        ORDER BY ic2.key_ordinal
        FOR XML PATH(''), TYPE
    ).value('.', 'NVARCHAR(MAX)'), 1, 2, '') AS columns
FROM sys.tables t
JOIN sys.indexes i ON i.object_id = t.object_id
WHERE t.is_ms_shipped = 0
  AND i.type > 0          -- loại bỏ heap
  AND EXISTS (
      SELECT 1 FROM sys.index_columns ic3
      WHERE ic3.object_id = i.object_id AND ic3.index_id = i.index_id
  )
ORDER BY t.name, i.name;
"""

SQL_FOREIGN_KEYS = """
SELECT
    fk.name                     AS fk_name,
    pt.name                     AS parent_table,
    pc.name                     AS parent_col,
    rt.name                     AS ref_table,
    rc.name                     AS ref_col,
    fk.delete_referential_action_desc,
    fk.update_referential_action_desc
FROM sys.foreign_keys fk
JOIN sys.foreign_key_columns fkc ON fkc.constraint_object_id = fk.object_id
JOIN sys.tables  pt  ON pt.object_id  = fk.parent_object_id
JOIN sys.columns pc  ON pc.object_id  = fk.parent_object_id  AND pc.column_id = fkc.parent_column_id
JOIN sys.tables  rt  ON rt.object_id  = fk.referenced_object_id
JOIN sys.columns rc  ON rc.object_id  = fk.referenced_object_id AND rc.column_id = fkc.referenced_column_id
ORDER BY parent_table, fk_name;
"""


def fetch_all(conn: pyodbc.Connection, sql: str) -> list[dict]:
    cur = conn.cursor()
    cur.execute(sql)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def format_type(row: dict) -> str:
    t = row["base_type"].upper()
    ml = row["max_length"]
    p, s = row["precision"], row["scale"]

    if t in ("NVARCHAR", "VARCHAR", "CHAR", "NCHAR"):
        length = "MAX" if ml == -1 else (str(ml // 2) if t.startswith("N") else str(ml))
        return f"{t}({length})"
    if t in ("DECIMAL", "NUMERIC"):
        return f"{t}({p},{s})"
    if t in ("UNIQUEIDENTIFIER",):
        return "UUID"
    return t


def col_flags(row: dict) -> list[str]:
    flags = []
    if row["is_pk"]:
        flags.append("PK")
    if row["fk_ref_table"]:
        nullable_note = " nullable" if row["is_nullable"] else ""
        flags.append(f"FK → {row['fk_ref_table']}.{row['fk_ref_col']}{nullable_note}")
    if not row["is_nullable"] and not row["is_pk"]:
        flags.append("NN")
    if row["is_identity"]:
        flags.append("IDENTITY")
    if row["default_value"]:
        flags.append(f"DEFAULT {row['default_value'].strip('()')}")
    if row["is_nullable"] and not row["fk_ref_table"]:
        flags.append("nullable")
    return flags


# ─────────────────────────────────────────────────────────────────────────────
# 3.  Sinh file .md
# ─────────────────────────────────────────────────────────────────────────────

def md_table_file(table_name: str, columns: list[dict], indexes: list[dict]) -> str:
    lines = [f"# Table: `{table_name}`", "", "---", "", "## Columns", ""]

    # Header
    lines.append("| Column | Type | Description |")
    lines.append("|--------|------|-------------|")

    for col in columns:
        type_str = format_type(col)
        flags = col_flags(col)
        flag_str = " ".join(flags)
        col_type = f"`{type_str}` {flag_str}".strip()
        desc = str(col["col_description"] or "").replace('\n', '<br>').strip()
        lines.append(f"| `{col['col_name']}` | {col_type} | {desc} |")

    # Indexes
    tbl_indexes = [i for i in indexes if i["table_name"] == table_name]
    if tbl_indexes:
        lines += ["", "---", "", "## Indexes", ""]
        lines.append("| Index | Columns | Loại |")
        lines.append("|-------|---------|------|")
        for idx in tbl_indexes:
            kind = "PRIMARY KEY" if idx["is_primary_key"] else ("UNIQUE" if idx["is_unique"] else "BTREE")
            lines.append(f"| `{idx['index_name']}` | `{idx['columns']}` | {kind} |")

    lines.append("")
    return "\n".join(lines)


def md_relations(fk_rows: list[dict], columns_rows: list[dict] = None) -> str:
    lines = [
        "# Database Relations",
        "",
        "> File này được sinh tự động từ SQL Server. "
        "Bạn có thể chỉnh sửa thủ công mà không lo bị ghi đè khi gen lại bảng.",
        "",
    ]

    # Nhóm FK theo parent_table
    by_table: dict[str, list[dict]] = defaultdict(list)
    for fk in fk_rows:
        by_table[fk["parent_table"]].append(fk)

    if not fk_rows:
        lines.append("*(Không có khóa ngoại (Foreign Keys) cứng nào được định nghĩa trên Database)*\n")

    for table, fks in sorted(by_table.items()):
        lines.append(f"### `{table}`")
        lines.append("")
        lines.append("```")
        for fk in fks:
            lines.append(
                f"{fk['parent_table']}.{fk['parent_col']} "
                f"──→ {fk['ref_table']}.{fk['ref_col']}    (N:1)"
            )
        lines.append("```")
        lines.append("")

    # Thêm phần Virtual Relations dựa trên mô tả cột
    lines += [
        "---",
        "",
        "## Virtual Relations (Liên kết logic dựa trên mô tả)",
        "",
        "> Hệ thống không dùng FK cứng. Các liên kết được mô tả qua Property `MS_Description` của từng cột.",
        "",
        "| Bảng | Cột | Ý nghĩa / Liên kết |",
        "|------|-----|--------------------|",
    ]
    
    has_virtual = False
    if columns_rows:
        for col in columns_rows:
            desc = str(col["col_description"] or "").strip()
            if desc: # Nếu cột có mô tả
                desc_clean = desc.replace('\n', '<br>')
                lines.append(f"| `{col['table_name']}` | `{col['col_name']}` | {desc_clean} |")
                has_virtual = True
                
    if not has_virtual:
        lines.append("| *(Trống)* | *(Trống)* | *(Chưa có mô tả nào cho các cột)* |")

    return "\n".join(lines)


def md_readme(table_names: list[str], db_name: str) -> str:
    lines = [
        f"# Database Schema — {db_name}",
        "",
        "> Sinh tự động từ SQL Server bằng `generate_md_from_mssql.py`.",
        "",
        "## Quick Reference",
        "",
        "| Table | File |",
        "|-------|------|",
    ]
    for t in table_names:
        lines.append(f"| `{t}` | [tables/{t}.md](tables/{t}.md) |")

    lines += [
        "",
        "---",
        "",
        "## Database Relations",
        "",
        "> Xem chi tiết các mối quan hệ (Foreign Keys) tại [relations.md](relations.md).",
        "",
        "---",
        "",
        "## Folder Structure",
        "",
        "```",
        "schema/",
        "├── README.md",
        "├── relations.md",
        "└── tables/",
    ]
    for t in table_names:
        lines.append(f"    ├── {t}.md")
    lines += ["```", "", "---", "", "## Conventions", ""]
    lines += [
        "| Ký hiệu | Nghĩa |",
        "|---------|-------|",
        "| `PK` | Primary Key |",
        "| `FK` | Foreign Key |",
        "| `NN` | NOT NULL |",
        "| `UQ` | UNIQUE |",
        "| `DEFAULT x` | Giá trị mặc định |",
        "| `nullable` | Có thể NULL |",
        "| `IDENTITY` | Auto-increment |",
        "",
    ]
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# 4.  Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    # Đọc giá trị mặc định từ .env
    _default_server   = os.getenv("DB_SERVER")   or ""
    _default_database = os.getenv("DB_DATABASE") or ""
    _default_user     = os.getenv("DB_USER")     or None
    _default_password = os.getenv("DB_PASSWORD") or None
    _default_driver   = os.getenv("DB_DRIVER")   or None
    _default_output   = os.getenv("OUTPUT_DIR")  or os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser(
        description="Kết nối SQL Server → sinh file .md schema theo chuẩn dự án",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""\
            Config ưu tiên: CLI args > .env > mặc định

            Ví dụ:
              # Chỉ dùng .env (khuyến khích)
              python generate_md_from_mssql.py

              # Override một phần
              python generate_md_from_mssql.py -D OtherDatabase

              # Chỉ định thư mục output
              python generate_md_from_mssql.py -o ./docs/schema
        """),
    )
    parser.add_argument("--server",   "-S", default=_default_server,   help=f"SQL Server host [env: DB_SERVER] (hiện tại: '{_default_server}')")
    parser.add_argument("--database", "-D", default=_default_database, help=f"Tên database [env: DB_DATABASE] (hiện tại: '{_default_database}')")
    parser.add_argument("--user",     "-U", default=_default_user,     help="SQL Server username [env: DB_USER] (bỏ trống → Windows Auth)")
    parser.add_argument("--password", "-P", default=_default_password, help="SQL Server password [env: DB_PASSWORD]")
    parser.add_argument("--driver",         default=_default_driver,   help="ODBC driver name [env: DB_DRIVER] (tự động detect nếu bỏ trống)")
    parser.add_argument(
        "--output", "-o",
        default=_default_output,
        help=f"Thư mục đầu ra [env: OUTPUT_DIR] (hiện tại: '{_default_output}')",
    )
    parser.add_argument(
        "--schema", default="dbo",
        help="SQL Server schema filter (mặc định: dbo)",
    )

    args = parser.parse_args()

    # Validate bắt buộc
    if not args.server:
        parser.error("Thiếu --server. Hãy set DB_SERVER trong .env hoặc truyền --server")
    if not args.database:
        parser.error("Thiếu --database. Hãy set DB_DATABASE trong .env hoặc truyền --database")

    # Kết nối
    conn = get_connection(args)

    print("📋  Đang đọc schema...")

    tables_rows = fetch_all(conn, SQL_TABLES)
    columns_rows = fetch_all(conn, SQL_COLUMNS)
    indexes_rows = fetch_all(conn, SQL_INDEXES)
    fk_rows      = fetch_all(conn, SQL_FOREIGN_KEYS)

    conn.close()

    table_names = [r["table_name"] for r in tables_rows]
    if not table_names:
        print("⚠️   Không tìm thấy bảng nào trong database (hoặc không có quyền truy cập).")
        sys.exit(0)

    print(f"🗂️   Tìm thấy {len(table_names)} bảng: {', '.join(table_names)}")

    # Tạo thư mục output
    out_dir = os.path.abspath(args.output)
    tables_dir = os.path.join(out_dir, "tables")
    os.makedirs(tables_dir, exist_ok=True)

    # Xóa các file .md cũ trong tables/ trước khi gen mới
    existing_md = [f for f in os.listdir(tables_dir) if f.endswith(".md")]
    if existing_md:
        print(f"🗑️   Xóa {len(existing_md)} file .md cũ trong tables/...")
        for fname in existing_md:
            os.remove(os.path.join(tables_dir, fname))
            print(f"  ✗  tables/{fname}")

    # Nhóm columns theo table
    cols_by_table: dict[str, list[dict]] = defaultdict(list)
    for col in columns_rows:
        cols_by_table[col["table_name"]].append(col)

    # Sinh tables/*.md
    for tbl in table_names:
        content = md_table_file(tbl, cols_by_table.get(tbl, []), indexes_rows)
        path = os.path.join(tables_dir, f"{tbl}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  📄  tables/{tbl}.md")

    # Sinh relations.md
    relations_path = os.path.join(out_dir, "relations.md")
    with open(relations_path, "w", encoding="utf-8") as f:
        f.write(md_relations(fk_rows, columns_rows))
    print("  📄  relations.md")

    # Sinh README.md
    readme_path = os.path.join(out_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(md_readme(table_names, args.database))
    print("  📄  README.md")

    print()
    print(f"✅  Hoàn tất! Tất cả file được lưu tại: {out_dir}")


if __name__ == "__main__":
    main()
