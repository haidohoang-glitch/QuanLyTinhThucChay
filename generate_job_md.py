import argparse
import os
import sys
import re
from collections import defaultdict
from dotenv import load_dotenv

try:
    import pyodbc
except ImportError:
    print("❌ Thiếu thư viện pyodbc. Cài đặt: pip install pyodbc")
    sys.exit(1)

if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass

# Load .env
_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
load_dotenv(_env_path)

# ─────────────────────────────────────────────────────────────────────────────
# Connection Logic
# ─────────────────────────────────────────────────────────────────────────────

def get_connection(args) -> pyodbc.Connection:
    driver = args.driver
    if not driver:
        available = [d for d in pyodbc.drivers() if "SQL Server" in d]
        if not available:
            print("[ERROR] Không tìm thấy ODBC Driver for SQL Server.")
            sys.exit(1)
        driver = sorted(available)[-1]
    base = f"DRIVER={{{driver}}};SERVER={args.server};DATABASE={args.database};"
    conn_str = base + (f"UID={args.user};PWD={args.password};" if args.user and args.password else "Trusted_Connection=yes;")
    try:
        return pyodbc.connect(conn_str, timeout=10)
    except pyodbc.Error as e:
        print(f"[ERROR] Kết nối thất bại: {e}")
        sys.exit(1)

def fetch(conn, sql, params=None):
    cur = conn.cursor()
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]

# ─────────────────────────────────────────────────────────────────────────────
# SQL Queries
# ─────────────────────────────────────────────────────────────────────────────

SQL_JOBS = """
SELECT
    j.job_id,
    j.name          AS job_name,
    j.description   AS job_description,
    j.enabled       AS job_enabled
FROM msdb.dbo.sysjobs j
WHERE j.name LIKE N'%ThucChay%' 
   OR j.name LIKE N'%Get%' 
   OR j.name LIKE N'%Sync%' 
   OR j.name LIKE N'%Import%'
ORDER BY j.name;
"""

SQL_STEPS = """
SELECT
    s.step_id,
    s.step_name,
    s.command,
    s.database_name
FROM msdb.dbo.sysjobsteps s
WHERE s.job_id = ?
ORDER BY s.step_id;
"""

SQL_DEPENDENCIES = """
SELECT 
    referenced_entity_name AS entity_name,
    referenced_class_desc AS entity_type
FROM sys.sql_expression_dependencies
WHERE referencing_id = OBJECT_ID(?)
"""

# ─────────────────────────────────────────────────────────────────────────────
# Helper Functions
# ─────────────────────────────────────────────────────────────────────────────

def extract_sp_name(command):
    """Try to extract SP name from EXEC statement."""
    if not command:
        return None
    # Match EXEC [schema].[name] or EXEC name
    match = re.search(r'EXEC\s+(?:\[?(\w+)\]?\.)?\[?(\w+)\]?', command, re.IGNORECASE)
    if match:
        schema = match.group(1) or 'dbo'
        name = match.group(2)
        return f"{schema}.{name}"
    return None

def get_mermaid_flow(conn, job_name, steps):
    lines = ["graph TD"]
    job_node = f"Job_{job_name.replace(' ', '_')}"
    lines.append(f"    {job_node}[Job: {job_name}]")
    
    seen_entities = set()
    
    for s in steps:
        sp_name = extract_sp_name(s['command'])
        if sp_name:
            sp_node = f"SP_{sp_name.replace('.', '_')}"
            lines.append(f"    {job_node} --> {sp_node}(SP: {sp_name})")
            
            # Get dependencies for this SP
            try:
                deps = fetch(conn, SQL_DEPENDENCIES, (sp_name,))
                for d in deps:
                    entity = d['entity_name']
                    etype = d['entity_type']
                    entity_node = f"Ent_{entity.replace(' ', '_')}"
                    
                    if etype == 'OBJECT_OR_COLUMN': # Likely a table
                        lines.append(f"    {sp_node} --> {entity_node}[(Table: {entity})]")
                    else: # Likely another SP or function
                        lines.append(f"    {sp_node} --> {entity_node}({entity})")
            except:
                pass # SP might not exist or be in a different DB
    
    return "\n".join(lines)

# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Gen Job MD files.")
    parser.add_argument("--server",   "-S", default=os.getenv("DB_SERVER") or "")
    parser.add_argument("--database", "-D", default=os.getenv("DB_DATABASE") or "")
    parser.add_argument("--user",     "-U", default=os.getenv("DB_USER"))
    parser.add_argument("--password", "-P", default=os.getenv("DB_PASSWORD"))
    parser.add_argument("--driver",         default=os.getenv("DB_DRIVER"))
    parser.add_argument("--output",   "-o", default="jobs")
    args = parser.parse_args()

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.output)
    os.makedirs(out_dir, exist_ok=True)

    conn = get_connection(args)

    print("Đang lấy danh sách Jobs...")
    jobs = fetch(conn, SQL_JOBS)
    
    for j in jobs:
        job_name = j['job_name']
        print(f"Processing Job: {job_name}")
        
        steps = fetch(conn, SQL_STEPS, (j['job_id'],))
        
        lines = [
            f"# Job: {job_name}",
            "",
            "## Thông Tin Cơ Bản",
            "| Thuộc tính | Giá trị |",
            "|---|---|",
            f"| Job Name | {job_name} |",
            f"| Database | {steps[0]['database_name'] if steps else 'msdb'} |",
            "| Hệ thống | Tính toán thực chạy |",
            "",
            "## Các Bước (Steps)",
            "| Step ID | Step Name | Command | Tác dụng |",
            "|---|---|---|---|",
        ]
        
        for s in steps:
            cmd = s['command'].replace('\n', ' ').strip()
            # Try to describe action based on SP name or step name
            action = "Gọi SP" if "EXEC" in cmd.upper() else "Chạy Script"
            lines.append(f"| {s['step_id']} | {s['step_name']} | `{cmd}` | {action} |")
        
        lines.append("")
        lines.append("## Data Flow (Luồng Dữ Liệu)")
        lines.append("```mermaid")
        lines.append(get_mermaid_flow(conn, job_name, steps))
        lines.append("```")
        lines.append("")
        
        out_file = os.path.join(out_dir, f"{job_name}.md")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

    conn.close()
    print(f"Hoàn tất! Đã tạo các file job tại: {out_dir}")

if __name__ == "__main__":
    main()
