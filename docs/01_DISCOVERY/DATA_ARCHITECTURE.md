# Quan lý tính thuc chay — Data Architecture Audit

> **Mục đích:** Tài liệu hóa cách hệ thống lưu trữ, di chuyển và quản trị dữ liệu. Xác định rủi ro về tính nhất quán.
> **Trạng thái:** 🟢 Complete
> **Ngày cập nhật:** 2026-05-08

---

## 1. Executive Summary

Hệ thống dựa trên mô hình Single Database (ABM_Data_ThucChay), sử dụng các bảng Staging để nhận dữ liệu từ RecurringJob và xử lý kết quả tập trung tại lớp Output (`ThucChayDaTinh*`). Rủi ro lớn nhất là việc thiếu ràng buộc khóa ngoại (Foreign Keys) cứng, dẫn đến nguy cơ mất toàn vẹn dữ liệu nếu logic Stored Procedure bị lỗi.

**Các rủi ro hàng đầu:**
1. **Thiếu FK cứng** — Toàn vẹn dữ liệu phụ thuộc 100% vào mã nguồn SQL. (Severity: P1)
2. **Logic đối trừ phức tạp** — Nguy cơ vượt phân bổ nếu Jobs chạy không đúng thứ tự. (Severity: P1)

---

## 2. Storage Layer Map (Bản đồ Lớp lưu trữ)

| Lớp | Tên bảng (Ví dụ) | Mục đích | Công nghệ |
|-------|-------|---------|------|
| **L1: Staging** | `Data thuc chay (Raw)` | Chứa dữ liệu thô từ RecurringJob | MSSQL |
| **L2: Normalization** | `ThucChay`, `ThucChayHopDongChiTiet` | Dữ liệu đã được chuẩn hóa, sẵn sàng tính toán | MSSQL |
| **L3: Output** | `ThucChayDaTinh`, `ThucChayDaTinhAdmarket` | Kết quả doanh số cuối cùng | MSSQL |
| **L4: Release** | `ABM_Data_Release` (Server asdag2) | Dữ liệu phục vụ IBiz và BI (Ngoài phạm vi trực tiếp) | MSSQL |

---

## 3. Mối Quan hệ Ảo (Virtual Relations)

Hệ thống sử dụng quy ước đặt tên cột (`REF`, `ID`, `FK`) để thiết lập liên kết logic:

| Thực thể Gốc | Thực thể Tham chiếu | Khóa liên kết | Vai trò |
|--------------|---------------------|---------------|---------|
| `HopDong` | `HopDongChiTiet` | `HopDongFK` | 1-N: Phân bổ chi tiết |
| `HopDong` | `HopDongThayDoi` | `HopDongFK` | 1-N: Lịch sử thay đổi HĐ |
| `HopDongChiTiet` | `ThucChayDaTinh` | `HopDongChiTietREF`| 1-N: Doanh số hàng ngày |
| `HopDongChiTiet` | `ThucChayHopDongChiTiet`| `HopDongChiTietREF`| 1-N: Log vận hành chi tiết |

---

## 4. Data Flow (Luồng dữ liệu)

### Luồng Doanh số (Actual Revenue)

**Write path:**
`RecurringJob` → `Staging Tables` → `Standardization SPs` → `ThucChay*` → `Calculation SPs` → `ThucChayDaTinh`

**Sync mechanisms:** SQL Agent Jobs (Daily Sync).
**Transaction boundary:** Từng Stored Procedure (T-SQL Transactions).

---

## 5. Governance Audit (Quản trị dữ liệu)

| Mối quan tâm | Trạng thái | Khoảng cách (Gap) |
|---------|--------|-----|
| Audit trail | ⚠️ Một phần | Chỉ có Log thay đổi HĐ/HĐCT, thiếu Log chi tiết cho từng lần chạy Job. |
| Access control | ✅ Đã thiết lập | Phân quyền theo User Database. |
| Backup & DR | ✅ Đã thiết lập | Theo chính sách chung của server asdag2. |

---

## 6. Risk Findings (Phát hiện rủi ro)

| ID | Rủi ro | Mức độ | Lớp | Khuyến nghị |
|----|------|----------|-------|----------------------|
| R-01 | Orphan Records | P1 | L3 | Xây dựng SP kiểm tra tính toàn vẹn (Data Integrity Check). |
| R-02 | Race Condition | P2 | L2 | Đảm bảo thứ tự chạy Job qua Job Step dependencies. |

---

## 7. Ghi chú & Caveats

- **Chế độ phân rã:** Mode A (Mô hình phân lớp chuẩn).
- **Độ tin tưởng:** Trung bình (Medium) — Do chưa được truy cập trực tiếp vào server cấu hình.
