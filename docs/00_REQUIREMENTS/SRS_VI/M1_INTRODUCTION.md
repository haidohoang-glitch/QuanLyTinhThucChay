# M1 — Giới thiệu (Introduction)

> **SRS Module 1 trong 10** | Dự án: Quản lý tính thực chạy | Phiên bản: v0.1 (DRAFT) | Ngày: 2026-05-08

---

## 1.1 Mục đích (Purpose)

Tài liệu Đặc tả yêu cầu phần mềm (SRS) này mô tả các yêu cầu cho hệ thống **Quản lý tính thực chạy** (ABM_Data_ThucChay).

**Đối tượng độc giả:**
- Ban quản trị dự án (Project Managers).
- Đội ngũ kỹ thuật (Engineering Lead, Developers).
- Đội ngũ kiểm thử (QA/QC).
- Các bên liên quan (Stakeholders) từ bộ phận kinh doanh và vận hành.

**Mục đích của tài liệu:**
- Định nghĩa phạm vi và ranh giới của hệ thống tính thực chạy.
- Cung cấp các tiêu chí nghiệm thu có thể kiểm thử được cho đội ngũ QA.
- Làm cơ sở để reverse-engineer logic từ mã nguồn SQL hiện có sang tài liệu nghiệp vụ chuẩn hóa.

---

## 1.2 Phạm vi (Scope)

### Tên sản phẩm
Hệ thống Quản lý tính thực chạy (Tên nội bộ: ABM_Data_ThucChay)

### Chức năng chính
Hệ thống thực hiện tính toán doanh số thực tế dựa trên dữ liệu vận hành từ nhiều nguồn khác nhau. Phạm vi cốt lõi của dự án tập trung vào việc tự động hóa tính toán, hỗ trợ đội Kiểm soát rà soát dữ liệu, xử lý các yêu cầu tính toán bổ sung thông qua việc viết mới các Stored Procedure, và điều tra/khắc phục các sự cố dữ liệu (Bug fix) phát sinh trong quá trình vận hành hàng ngày. Dự án kết thúc tại khâu cung cấp dữ liệu đã được kiểm soát và điều chỉnh.

### Các chức năng nằm ngoài phạm vi (Out of scope)
- Hệ thống chốt dữ liệu và đẩy sang môi trường Release/BI (B5).
- Thanh toán và kế toán thực tế (ERP).
- Hệ thống quản lý hợp đồng gốc (CRM/ABM core).

---

## 1.3 Định nghĩa và Thuật ngữ (Definitions, Acronyms)

| Thuật ngữ | Định nghĩa |
|-----------|------------|
| **CPD** | Cost Per Day - Tính phí theo ngày. |
| **PR** | Các loại hình bài viết (Tuyến bài, Giao lưu trực tuyến, Adpage). |
| **CPM** | Cost Per Mile - Tính phí theo 1000 lượt hiển thị. |
| **CPV/CPR** | Cost Per View / Cost Per Reach. |
| **Offset (Đối trừ)** | Cơ chế tính chênh lệch giữa giá trị mới và giá trị đã tính để điều chỉnh doanh số. |
| **Orchestration** | Việc điều phối thứ tự thực thi của các Job để đảm bảo tính toàn vẹn dữ liệu. |
| **MoSCoW** | Phương pháp ưu tiên: Must (Bắt buộc) / Should (Nên có) / Could (Có thể) / Won't (Chưa làm). |
| **FR** | Functional Requirement - Yêu cầu chức năng. |

---

## 1.4 Tài liệu tham khảo (References)

| ID | Tài liệu | Vai trò |
|----|-----------|---------|
| REF-01 | `docs/Logic_nghiepvu_tinh_thucchay.md` | Tài liệu nghiệp vụ gốc |
| REF-02 | `context/INPUT_LOGIC_TINH_MOI.md` | Logic tính mới chi tiết |
| REF-03 | `context/INPUT_LOGIC_TINH_THAYDOI.md` | Logic tính thay đổi chi tiết |
| REF-04 | `context/INPUT_JOB_SCHEDULE.md` | Lịch trình và điều phối Job |

---

## 1.5 Tổng quan cấu trúc (Overview)

Tài liệu SRS này được tổ chức thành các module:

| Module | Nội dung |
|--------|---------|
| M1 | Giới thiệu (Tài liệu này) |
| M2 | Mô tả tổng quan hệ thống |
| M3 | Logic Tính Mới (Functional Domain 1) |
| M4 | Logic Tính Thay Đổi (Functional Domain 2) |
| M5 | Lập lịch & Điều phối Job (Functional Domain 3) |
| M6 | Kiểm soát & Toàn vẹn dữ liệu |
| M7 | Cảnh báo & Xử lý sự cố |
| M8 | Quản lý Dữ liệu Đích |
| M9 | Các yêu cầu phi chức năng (NFR) |
| M10 | Ma trận truy xuất (RTM) & Các vấn đề tồn đọng |
