# 00 — MASTER INDEX: Project "Quan ly tinh thuc chay"

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

## 2. Luồng lấy dữ liệu đầu vào (Input Jobs)

> ⚠️ **Cần bổ sung**: Bảng dưới đây liệt kê các Job làm nhiệm vụ đồng bộ/lấy dữ liệu từ các hệ thống khác về trước khi tính toán. Bạn hãy điền tên Job tương ứng vào nhé.

| Tên Job lấy dữ liệu | Nguồn dữ liệu (Source) | Bảng tạm (Staging/Input Tables) |
|---------------------|------------------------|---------------------------------|
| _(VD: Job_Get_Data_PR)_ | Hệ thống PR | _(chưa điền)_ |
| _(chưa điền)_ | _(chưa điền)_ | _(chưa điền)_ |

---

## 3. Luồng tính toán (Calculation Jobs) & Mapping

> ⚠️ **Cần bổ sung**: Bảng dưới đây map từng nhóm sản phẩm với SP Orchestrator để tính toán.
> Để biết SP Orchestrator là gì, chạy: `python generate_sp_flow_mssql.py --root_sp "TênSP"`

| Nhóm Sản phẩm | SP Orchestrator (Level 1) | Bảng đích |
|---------------|--------------------------|-----------|
| PR | ThucChay_PR_Job | ThucChayDaTinh |
| CPD đợt chạy | ThucChay_CPD_Job | ThucChayDaTinh |
| CPD không đợt chạy | ThucChay_CPD_Job | ThucChayDaTinh |
| CPD đơn vị gói | ThucChay_CPD_Job | ThucChayDaTinh |
| Admatic | ThucChay_Admatic_Job | ThucChayDaTinh |
| Chi phí khác | ThucChay_ChiPhi_Job | ThucChayDaTinh |
| Chi phí sản phẩm chính | ThucChay_ChiPhi_Job | ThucChayDaTinh |
| Inventory | ThucChay_job_TinhthucchayInventory | ThucChayDaTinh |
| CPM thuần | ThucChay_CPM_Job | ThucChayDaTinh |
| CPV | ThucChay_CPM_Job | ThucChayDaTinh |
| CPR | ThucChay_CPM_Job | ThucChayDaTinh |
| Trueview | ThucChay_CPM_Job | ThucChayDaTinh |
| Native_Ads/On Image | ThucChay_CPM_Job | ThucChayDaTinh |
| CPM đơn vị bài | ThucChay_CPM_Job | ThucChayDaTinh |
| CPM đơn vị gói | ThucChay_CPM_Job | ThucChayDaTinh |
| CPM đơn vị ngày | ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs | ThucChayDaTinh |
| GGFB - theo thực tế phát sinh | ThucChay_GGFB_Job | ThucChayDaTinh |
| GGFB - theo sản lượng chốt | ThucChay_GGFB_Job | ThucChayDaTinh |
| Admarket | job_prc_asd_calc_admarket_PhanBo | ThucChayDaTinhAdmarket |
| Admarket điều chỉnh giá trị | prc_asd_calc_admarket_UpdateValue_With_HopDong | ThucChayDaTinhAdmarket |
| Mobile | ThucChay_Mobile_Job | ThucChayDaTinh |

---

## 4. Danh mục tài liệu hệ thống

| File | Nội dung |
|------|----------|
| [01_JOBS_AND_STEPS.md](./01_JOBS_AND_STEPS.md) | Toàn bộ Jobs và Steps trên SQL Agent |
| [02_DM_SANPHAM.md](./02_DM_SANPHAM.md) | Master Data: ID sản phẩm và tên |
| [03_DM_HINHTHUCQUANGCAO.md](./03_DM_HINHTHUCQUANGCAO.md) | Master Data: Loại hình quảng cáo |
| [stored_procedures/FLOW_ThucChay_CPD_Job.md](./stored_procedures/FLOW_ThucChay_CPD_Job.md) | Luồng gọi chi tiết nhóm CPD |
| [stored_procedures/](./stored_procedures/) | Source code toàn bộ 548 SP/FN |
| [tables/](./tables/) | Schema chi tiết các bảng dữ liệu |

---

## 5. Hướng dẫn AI khi được hỏi

- **Hỏi tổng quan** → Đọc file này là đủ.
- **Hỏi về Job cụ thể** → Xem `01_JOBS_AND_STEPS.md`.
- **Hỏi tại sao doanh số sai** → Xem `FLOW_{SP}.md` của nhóm đó + `02_DM_SANPHAM.md`.
- **Hỏi sửa bug SP cụ thể** → Xem `stored_procedures/SP_{TênSP}.md`.
