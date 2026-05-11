"""
generate_context_for_ai.py
---------------------------
Tự động kết nối SQL Server và sinh ra các file MD cung cấp ngữ cảnh
cho AI để AI có thể đọc, hiểu và maintain hệ thống tính thực chạy.

Các file được sinh ra:
    context/
    ├── 00_MASTER_INDEX.md          -- Bức tranh tổng thể toàn hệ thống
    ├── 01_JOBS_AND_STEPS.md        -- Danh sách Jobs và các Steps
    ├── 02_DM_SANPHAM.md            -- Master Data: Giải mã ID sản phẩm
    └── 03_DM_HINHTHUCQUANGCAO.md   -- Master Data: Giải mã loại hình QC

Cách dùng:
    python generate_context_for_ai.py
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
# Kết nối
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


def fetch(conn, sql, params=None):
    cur = conn.cursor()
    if params:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]


# ─────────────────────────────────────────────────────────────────────────────
# Các Query lấy dữ liệu
# ─────────────────────────────────────────────────────────────────────────────

SQL_JOBS_STEPS = """
SELECT
    j.name          AS job_name,
    j.description   AS job_description,
    j.enabled       AS job_enabled,
    s.step_id,
    s.step_name,
    s.command,
    s.on_success_action,
    s.on_fail_action,
    s.database_name
FROM msdb.dbo.sysjobs j
JOIN msdb.dbo.sysjobsteps s ON j.job_id = s.job_id
WHERE j.name LIKE N'%ThucChay%' 
   OR j.name LIKE N'%Get%' 
   OR j.name LIKE N'%Sync%' 
   OR j.name LIKE N'%Import%'
ORDER BY j.name, s.step_id;
"""

# !! THAY TÊN BẢNG/CỘT PHÙ HỢP VỚI HỆ THỐNG CỦA BẠN !!
# Bảng DmSanPham — giải mã ID sản phẩm
# Nếu bảng này nằm ở database khác, thêm tiền tố [DatabaseName].[dbo].[TableName]
SQL_DM_SANPHAM = """
SELECT
    DmSanPhamID     AS id,
    TenSanPham      AS ten_san_pham,
    MaSanPham       AS ma_san_pham
FROM dbo.DmSanPham
ORDER BY DmSanPhamID;
"""

# Bảng DmHinhThucQuangCao — giải mã loại hình QC
SQL_DM_HTQC = """
SELECT
    DmHinhThucQuangCaoID    AS id,
    TenHinhThucQuangCao     AS ten_hinh_thuc
FROM dbo.DmHinhThucQuangCao
ORDER BY DmHinhThucQuangCaoID;
"""


# ─────────────────────────────────────────────────────────────────────────────
# Hàm gen từng file
# ─────────────────────────────────────────────────────────────────────────────

def action_map(code: int) -> str:
    return {1: "Quit (Success)", 2: "Quit (Failure)", 3: "Go to next step", 4: "Go to step"}.get(code, str(code))


def gen_jobs_and_steps(conn, out_dir: str):
    print("📋 Đang lấy thông tin Jobs & Steps...")
    rows = fetch(conn, SQL_JOBS_STEPS)
    if not rows:
        print("⚠️ Không tìm thấy Job nào.")
        return

    # Gom theo job
    from collections import defaultdict
    jobs = defaultdict(list)
    job_meta = {}
    for r in rows:
        name = r['job_name']
        jobs[name].append(r)
        job_meta[name] = {'description': r['job_description'], 'enabled': r['job_enabled']}

    # Phân loại
    input_keywords = ['get', 'sync', 'import', 'laydulieu', 'api']
    
    input_jobs = {}
    calc_jobs = {}
    
    for job_name, steps in jobs.items():
        if any(kw in job_name.lower() for kw in input_keywords):
            input_jobs[job_name] = steps
        else:
            calc_jobs[job_name] = steps

    lines = [
        "# 01 — Danh sách Jobs & Steps",
        "",
        f"> Tổng số Jobs liên quan: **{len(jobs)}**",
        "",
        "## PHẦN 1: CÁC JOB LẤY DỮ LIỆU ĐẦU VÀO (INPUT JOBS)",
        "---",
        ""
    ]
    
    if not input_jobs:
        lines.append("*(Không tìm thấy Job nào có từ khóa: get, sync, import...)*\n")
    
    for job_name, steps in sorted(input_jobs.items()):
        meta = job_meta[job_name]
        status = "✅ Đang bật" if meta['enabled'] else "❌ Đã tắt"
        lines += [
            f"### Job: `{job_name}`",
            f"- **Trạng thái**: {status}",
            f"- **Mô tả**: {meta['description'] or '*(chưa có)*'}",
            "",
            "| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |",
            "|------|----------|----------------------|----------|----------------|--------------|",
        ]
        for s in steps:
            cmd = (s['command'] or '').replace('\n', ' ').strip()
            lines.append(
                f"| {s['step_id']} | {s['step_name']} | `{cmd}` | {s['database_name']} "
                f"| {action_map(s['on_success_action'])} | {action_map(s['on_fail_action'])} |"
            )
        lines.append("")

    lines += [
        "## PHẦN 2: CÁC JOB TÍNH TOÁN (CALCULATION JOBS)",
        "---",
        ""
    ]
    
    for job_name, steps in sorted(calc_jobs.items()):
        meta = job_meta[job_name]
        status = "✅ Đang bật" if meta['enabled'] else "❌ Đã tắt"
        lines += [
            f"### Job: `{job_name}`",
            f"- **Trạng thái**: {status}",
            f"- **Mô tả**: {meta['description'] or '*(chưa có)*'}",
            "",
            "| Step | Tên Step | Command (SP được gọi) | Database | Khi thành công | Khi thất bại |",
            "|------|----------|----------------------|----------|----------------|--------------|",
        ]
        for s in steps:
            cmd = (s['command'] or '').replace('\n', ' ').strip()
            lines.append(
                f"| {s['step_id']} | {s['step_name']} | `{cmd}` | {s['database_name']} "
                f"| {action_map(s['on_success_action'])} | {action_map(s['on_fail_action'])} |"
            )
        lines.append("")

    out = os.path.join(out_dir, "01_JOBS_AND_STEPS.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ {out}")


def gen_master_data(conn, out_dir: str, sql: str, filename: str, title: str, col_id: str, col_name: str):
    print(f"📋 Đang lấy {title}...")
    try:
        rows = fetch(conn, sql)
    except Exception as e:
        print(f"⚠️ Không thể lấy {title}: {e}")
        print(f"   → Vui lòng kiểm tra lại tên bảng/cột trong script (SQL ở đầu file).")
        return

    lines = [f"# {title}", "", "| ID | Tên |", "|----|-----|"]
    for r in rows:
        lines.append(f"| `{r[col_id]}` | {r[col_name]} |")
    lines.append("")

    out = os.path.join(out_dir, filename)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ {out}")


def gen_master_index(out_dir: str):
    """Gen file index tổng thể — phần Job mapping cần bạn điền tay."""
    content = """\
# 00 — MASTER INDEX: Hệ thống Tính Thực Chạy

> **Hướng dẫn dùng cho AI**: Đọc file này trước. Từ đây điều hướng sang file chi tiết phù hợp với câu hỏi.

---

## 1. Tổng quan hệ thống

Hệ thống tính **Thực Chạy** chạy theo ngày trên SQL Server Agent.
Kết quả được ghi vào các bảng đích dùng chung:

| Bảng đích | Mục đích |
|-----------|----------|
| `ThucChayDaTinh` | Kết quả tính thực chạy cho hầu hết các nhóm sản phẩm |
| `ThucChayDaTinhAdmarket` | Riêng nhóm Admarket và Admarket điều chỉnh |
| `ThucChayDaTinh_MuaNgoai` | Riêng nhóm mua ngoài (ThucChayMuaNgoaiChiTiet) |

---

## 2. Mapping: Nhóm Sản phẩm → SP Orchestrator → Bảng đích

> ⚠️ **Cần bổ sung**: Bảng dưới đây cần bạn điền tay tên SP Orchestrator cho từng nhóm sản phẩm.
> Để biết SP Orchestrator là gì, chạy: `python generate_sp_flow_mssql.py --root_sp "TênSP"`

| Nhóm Sản phẩm | SP Orchestrator (Level 1) | Bảng đích |
|---------------|--------------------------|-----------|
| PR | _(chưa điền)_ | ThucChayDaTinh |
| CPD đợt chạy | ThucChay_CPD_Job | ThucChayDaTinh |
| CPD không đợt chạy | ThucChay_CPD_Job | ThucChayDaTinh |
| CPD đơn vị gói | ThucChay_CPD_Job | ThucChayDaTinh |
| Admatic | _(chưa điền)_ | ThucChayDaTinh |
| Chi phí khác | _(chưa điền)_ | ThucChayDaTinh |
| Chi phí sản phẩm chính | _(chưa điền)_ | ThucChayDaTinh |
| Inventory | _(chưa điền)_ | ThucChayDaTinh |
| CPM thuần | _(chưa điền)_ | ThucChayDaTinh |
| CPV | _(chưa điền)_ | ThucChayDaTinh |
| CPR | _(chưa điền)_ | ThucChayDaTinh |
| Trueview | _(chưa điền)_ | ThucChayDaTinh |
| Native_Ads/On Image | _(chưa điền)_ | ThucChayDaTinh |
| CPM đơn vị bài | _(chưa điền)_ | ThucChayDaTinh |
| CPM đơn vị gói | _(chưa điền)_ | ThucChayDaTinh |
| CPM đơn vị ngày | _(chưa điền)_ | ThucChayDaTinh |
| GGFB - theo thực tế phát sinh | _(chưa điền)_ | ThucChayDaTinh |
| GGFB - theo sản lượng chốt | _(chưa điền)_ | ThucChayDaTinh |
| ThucChayMuaNgoaiChiTiet | _(chưa điền)_ | ThucChayDaTinh_MuaNgoai |
| Admarket | _(chưa điền)_ | ThucChayDaTinhAdmarket |
| Admarket điều chỉnh giá trị | _(chưa điền)_ | ThucChayDaTinhAdmarket |
| Mobile | _(chưa điền)_ | ThucChayDaTinh |

---

## 3. Danh mục tài liệu hệ thống

| File | Nội dung |
|------|----------|
| [01_JOBS_AND_STEPS.md](./01_JOBS_AND_STEPS.md) | Toàn bộ Jobs và Steps trên SQL Agent |
| [02_DM_SANPHAM.md](./02_DM_SANPHAM.md) | Master Data: ID sản phẩm và tên |
| [03_DM_HINHTHUCQUANGCAO.md](./03_DM_HINHTHUCQUANGCAO.md) | Master Data: Loại hình quảng cáo |
| [stored_procedures/FLOW_ThucChay_CPD_Job.md](./stored_procedures/FLOW_ThucChay_CPD_Job.md) | Luồng gọi chi tiết nhóm CPD |
| [stored_procedures/](./stored_procedures/) | Source code toàn bộ 548 SP/FN |
| [tables/](./tables/) | Schema chi tiết các bảng dữ liệu |

---

## 4. Hướng dẫn AI khi được hỏi

- **Hỏi tổng quan** → Đọc file này là đủ.
- **Hỏi về Job cụ thể** → Xem `01_JOBS_AND_STEPS.md`.
- **Hỏi tại sao doanh số sai** → Xem `FLOW_{SP}.md` của nhóm đó + `02_DM_SANPHAM.md`.
- **Hỏi sửa bug SP cụ thể** → Xem `stored_procedures/SP_{TênSP}.md`.
"""
    out = os.path.join(out_dir, "00_MASTER_INDEX.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ {out}")


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Gen context MD cho AI đọc hệ thống Thực Chạy.")
    parser.add_argument("--server",   "-S", default=os.getenv("DB_SERVER") or "")
    parser.add_argument("--database", "-D", default=os.getenv("DB_DATABASE") or "")
    parser.add_argument("--user",     "-U", default=os.getenv("DB_USER"))
    parser.add_argument("--password", "-P", default=os.getenv("DB_PASSWORD"))
    parser.add_argument("--driver",         default=os.getenv("DB_DRIVER"))
    parser.add_argument("--output",   "-o", default="context")
    args = parser.parse_args()

    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.output)
    os.makedirs(out_dir, exist_ok=True)

    conn = get_connection(args)

    # 1. Jobs & Steps (từ msdb — luôn chạy được)
    gen_jobs_and_steps(conn, out_dir)

    # 2. Master Data Sản phẩm
    # !! SỬA TÊN BẢNG/CỘT NẾU CẦN !!
    gen_master_data(
        conn, out_dir,
        sql=SQL_DM_SANPHAM,
        filename="02_DM_SANPHAM.md",
        title="02 — Master Data: Sản phẩm (DmSanPham)",
        col_id="id",
        col_name="ten_san_pham",
    )

    # 3. Master Data Loại hình QC
    # !! SỬA TÊN BẢNG/CỘT NẾU CẦN !!
    gen_master_data(
        conn, out_dir,
        sql=SQL_DM_HTQC,
        filename="03_DM_HINHTHUCQUANGCAO.md",
        title="03 — Master Data: Hình thức quảng cáo (DmHinhThucQuangCao)",
        col_id="id",
        col_name="ten_hinh_thuc"
    )

    conn.close()

    # 4. Bỏ qua việc gen Master Index để không ghi đè lên file bạn đã điền tay!
    # gen_master_index(out_dir)

    print()
    print(f"🎉 Hoàn tất! Toàn bộ file context đã được cập nhật tại: {out_dir}")
    print()
    print("📌 Đã chia Jobs thành 2 phần: Input Jobs và Calculation Jobs trong 01_JOBS_AND_STEPS.md.")

if __name__ == "__main__":
    main()
