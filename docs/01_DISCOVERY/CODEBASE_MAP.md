# Quan lý tính thuc chay — Codebase Map

> **Mục đích:** Tài liệu tham khảo kỹ thuật mô tả cấu trúc, stack, module và phụ thuộc của codebase.
> **Trạng thái:** 🟢 Complete
> **Ngày cập nhật:** 2026-05-08

---

## 1. Executive Summary

**Dự án này là gì?**
Hệ thống tính toán doanh số thực tế (Actual Revenue) dựa trên SQL Server. Nó thực hiện đồng bộ dữ liệu từ các nguồn sản phẩm (PR, CPD, Admarket, Mobile...) qua SQL Agent Jobs, áp dụng các thuật toán tính toán phức tạp (bao gồm cả đệ quy) và lưu trữ kết quả tập trung tại `ThucChayDaTinh`.

**Hình thái dự án:** Database-centric (Tập trung vào Database/SQL).

**Stack chính:** MSSQL Server (T-SQL), SQL Agent Jobs, Tool RecurringJob (External).

**Chỉ số trưởng thành:**
- Tổng số bảng: 507
- Tổng số hàm (Functions): 671
- Tổng số Stored Procedures: ~140 (trong luồng tính)
- Ngôn ngữ chính: T-SQL (100%)

---

## 2. Tech Stack Inventory

### Data Layer

| Thành phần | Phiên bản | Mục đích |
|-----------|-----------|---------|
| MSSQL Server | Unknown | Primary Database (ABM_Data_ThucChay) |

### Build & Tooling

| Công cụ | Phiên bản | Mục đích |
|------|---------|---------|
| Tool RecurringJob | External | Thu thập dữ liệu thực chạy từ nguồn sản phẩm |
| SQL Agent | Integrated | Điều phối (Orchestration) các Job tính toán hàng ngày |

---

## 3. Cấu trúc Thư mục (Folder Structure)

```
/ (Root)
├── context/              Tài liệu ngữ cảnh và dữ liệu đầu vào (Internal)
├── company-skills/       Bộ quy tắc và kỹ năng chuẩn của công ty
├── docs/                 Tài liệu hệ thống (Phase 0, 1, 2, 3)
│   ├── 00_REQUIREMENTS/  Đặc tả SRS (Phân theo Module M1-M10)
│   ├── 01_DISCOVERY/     Bản đồ codebase, kiến trúc dữ liệu, nợ kỹ thuật
│   └── INDEX.md          Bảng điều hướng tài liệu dự án
└── sql_scripts/          (Giả định) Chứa các script SQL của hệ thống
```

---

## 4. Module Boundaries (Ranh giới Module)

Hệ thống được phân chia theo các nhóm sản phẩm (Product Groups):

| Module | Mục đích | Bảng đích chính | Phụ thuộc |
|--------|---------|---------------|-----------|
| **PR/CPD** | Tính thực chạy bài viết/banner cố định. | ThucChayDaTinh | HopDong, HopDongChiTiet |
| **Admarket** | Tính theo đấu thầu/ngân sách. | ThucChayDaTinhAdmarket | ThucChayAdmarket_PhanBo |
| **Mobile** | Tính theo sản lượng (CTE đệ quy). | ThucChayDaTinh | ThucChayHopDongChiTiet |
| **Orchestrator** | Điều phối thứ tự chạy các Job. | N/A | Toàn bộ SP tính toán |

---

## 5. Entry Points (Điểm bắt đầu)

### Entry: SQL Agent Jobs (Daily)

- **Trigger:** Tự động lúc 08:00 AM hàng ngày.
- **Quy trình thực thi:**
  1. `ThucChay_CPD_Chiphi_PR`
  2. `ThucChay_Admarket_PB_Calculated_BySQLJobs`
  3. `ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs`
  4. `job_Tinhthucchay_PerformanceBase`

---

## 6. Open Questions

| ID | Câu hỏi | Vị trí | Bước tiếp theo |
|----|----------|------------|---------------------|
| OQ-1 | Logic tính thay đổi cho CPV/CPR? | SP CPM_Job | Phỏng vấn Stakeholder |
| OQ-2 | Phiên bản MSSQL cụ thể đang dùng? | Database Server | Kiểm tra thông tin server |

---

## 7. Ghi chú & Caveats

- **Chế độ phân rã:** Mode B (Tôn trọng cấu trúc phân nhóm SP hiện có).
- **Phạm vi khám phá:** Đã quét 11 luồng tính toán chính và hơn 500 bảng dữ liệu.
- **Thời gian thực hiện:** ~4 giờ.
- **Độ tin tưởng:** Cao (High).
