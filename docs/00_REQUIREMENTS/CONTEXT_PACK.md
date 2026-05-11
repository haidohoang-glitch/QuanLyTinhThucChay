# CONTEXT_PACK — Hệ thống Tính Thực Chạy

> **Skill:** `project-context-ingestion` | **Trạng thái:** 🟡 Skeleton — cần bổ sung
>
> File này tổng hợp TOÀN BỘ ngữ cảnh dự án từ mọi nguồn, phục vụ làm input cho SRS và các phase sau.

---

## 1. Thông tin Dự án

| Thuộc tính | Giá trị |
|------------|---------|
| **Tên dự án** | Hệ thống Tính Thực Chạy (Sales Calculation System) |
| **Database** | ABM_Data_ThucChay (MSSQL) |
| **Server** | thucchay-ag |
| **Loại dự án** | Legacy — đã vận hành production |
| **Ngôn ngữ chính** | T-SQL (Stored Procedures, Functions) |
| **Scheduling** | SQL Server Agent Jobs |
| **Authentication** | Windows Authentication |

---

## 2. Mục đích Hệ thống

<!-- ⚠️ CẦN USER BỔ SUNG: Mô tả chi tiết hệ thống làm gì -->

Hệ thống tính **doanh số thực chạy** cho 21 nhóm sản phẩm quảng cáo, chạy hằng ngày theo lịch SQL Agent.

Kết quả ghi vào 3 bảng đích:
- `ThucChayDaTinh` — hầu hết các nhóm
- `ThucChayDaTinhAdmarket` — nhóm Admarket
- `ThucChayDaTinh_MuaNgoai` — nhóm Mua ngoài

---

## 3. Stakeholders

<!-- ⚠️ CẦN USER BỔ SUNG -->

| Vai trò | Tên / Team | Trách nhiệm |
|---------|------------|-------------|
| Product Owner | _(chưa điền)_ | _(chưa điền)_ |
| DBA / Vận hành | _(chưa điền)_ | Giám sát Jobs, xử lý sự cố |
| Business Users | _(chưa điền)_ | Sử dụng dữ liệu từ ThucChayDaTinh |

---

## 4. Nguồn Dữ liệu Đã Thu Thập

### 4.1 Tài liệu tự động (auto-generated)

| Nguồn | File | Mô tả |
|-------|------|-------|
| SQL Agent Jobs | `context/01_JOBS_AND_STEPS.md` | 13 Jobs, steps chi tiết |
| Master Data SP | `context/02_DM_SANPHAM.md` | Danh mục sản phẩm |
| Master Data HTQC | `context/03_DM_HINHTHUCQUANGCAO.md` | Danh mục hình thức QC |
| Job Descriptions | `context/04_JOB_DESC.md` | Mô tả ý nghĩa Jobs (từ DB) |
| Table Descriptions | `context/05_TABLE_DESC.md` | Mô tả ý nghĩa Tables (từ DB) |
| Data Architecture | `context/06_DATA_ARCHITECTURE.md` | Virtual Relations từ column desc |
| SP Flows | `stored_procedures/FLOW_*.md` (11 files) | Call graph + parameters |
| SP Details | `stored_procedures/SP_*.md` (140 files) | Source code + docs |
| Table Schema | `tables/*.md` | Column types, indexes |

### 4.2 Tài liệu cần thu thập thủ công

<!-- ⚠️ CẦN USER BỔ SUNG: Tạo các file .md sau -->

| Cần thu thập | Gợi ý file | Trạng thái |
|--------------|-----------|------------|
| Logic tính mới (new calculation) | `context/INPUT_LOGIC_TINH_MOI.md` | ✅ Đã có |
| Logic tính thay đổi (changed value) | `context/INPUT_LOGIC_TINH_THAYDOI.md` | ✅ Đã có |
| Lịch chạy Jobs (schedule) | `context/INPUT_JOB_SCHEDULE.md` | ✅ Đã có |
| Danh sách lỗi thường gặp | `context/INPUT_COMMON_ERRORS.md` | 🔴 Chưa có |
| Quy trình xử lý sự cố hiện tại | `context/INPUT_INCIDENT_PROCESS.md` | 🔴 Chưa có |
| Hệ thống nguồn & hệ thống đích | `context/INPUT_SYSTEMS_MAP.md` | 🔴 Chưa có |

---

## 5. Đặc tả Yêu cầu Hệ thống (SRS)

Toàn bộ các yêu cầu trên được chi tiết hóa trong bộ tài liệu SRS Phase 0:

- [M1 Introduction](./SRS_VI/M1_INTRODUCTION.md)
- [M2 Overview](./SRS_VI/M2_OVERVIEW.md)
- [M3-M8 Functional Requirements](./SRS_VI/M3-M8_FUNCTIONAL_REQUIREMENTS.md)
- [M9 Non-Functional Requirements](./SRS_VI/M9_NFR.md)
- [M10 Traceability Matrix](./SRS_VI/M10_TRACEABILITY.md)

---

## 5. Ràng buộc & Quy ước

- Không sử dụng Foreign Keys cứng → quan hệ mô tả trong column description
- SQL Server Native Client 11.0
- Windows Authentication
- Database đơn: `ABM_Data_ThucChay`
- Job alert: Email qua PowerShell script `D:\script\send_mail.ps1`

---

## _sources/

_(Thư mục chứa raw materials gốc — transcripts, meeting notes, etc.)_
