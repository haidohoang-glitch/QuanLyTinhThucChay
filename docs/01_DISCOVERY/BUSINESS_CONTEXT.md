# Quan lý tính thuc chay — Business Context

> **Mục đích:** Cung cấp cái nhìn nghiệp vụ về codebase: ai sử dụng, quy tắc quản lý, và các luồng công việc chính.
> **Trạng thái:** 🟢 Complete (Đã cập nhật theo quy trình 5 bước và chuẩn Company-Skill)
> **Ngày cập nhật:** 2026-05-08

---

## 1. Tóm tắt Sản phẩm (Product Summary)

Hệ thống tự động tính toán doanh số quảng cáo thực tế phát sinh (Actual Revenue) cho 21 nhóm sản phẩm dựa trên bằng chứng vận hành (Log treo, View, Click). Hệ thống đóng vai trò quan trọng trong việc chuyển đổi dữ liệu kỹ thuật thành dữ liệu tài chính, hỗ trợ đội Kiểm soát rà soát sai lệch và cung cấp số liệu cho các hệ thống báo cáo (IBiz, BI).

**Lĩnh vực nghiệp vụ:** Quảng cáo trực tuyến (AdTech) / Quản lý doanh thu.

---

## 2. Actors (Tác nhân)

| Tác nhân | Mô tả | Công cụ sử dụng |
|----------|-------|-----------------|
| **Hệ thống RecurringJob** | Tự động lấy dữ liệu từ các nền tảng sản phẩm. | Tool RecurringJob (API/Task) |
| **Hệ thống SQL Agent** | Thực hiện đồng bộ, chuẩn hóa và tính toán tự động. | SQL Agent Jobs (thucchay-ag) |
| **Đội Kiểm soát Thực chạy** | Rà soát dữ liệu, yêu cầu tính bổ sung, báo lỗi và chốt số. | SQL Queries / Management UI |
| **Đội Sản phẩm / Sale** | Cung cấp thông tin PO và yêu cầu xử lý các case đặc thù. | Tool đánh số / CRM |

---

## 3. Use Cases (Trường hợp sử dụng)

- **UC-01:** Hệ thống có thể tự động tính doanh số mới dựa trên thực treo hàng ngày.
- **UC-02:** Hệ thống có thể tự động đối trừ (Offset) khi hợp đồng hoặc phân bổ có thay đổi.
- **UC-03:** Đội Kiểm soát có thể yêu cầu tính lại (Recalculate) cho một hợp đồng cụ thể.
- **UC-04:** Đội Kiểm soát có thể thực hiện "Chốt số" để đẩy dữ liệu sang hệ thống Release.

---

## 4. Domain Entities (Thực thể nghiệp vụ)

| Thực thể | Định nghĩa nghiệp vụ | Thuộc tính quan trọng |
|----------|----------------------|-----------------------|
| **Đánh số (PO)** | Mã hợp đồng được cấp từ tool đánh số (ví dụ: QC0710526). | Mã hợp đồng, Khách hàng, Giá trị tổng. |
| **Phân bổ (HĐCT)** | Chi tiết dòng sản phẩm trong hợp đồng. | Vị trí, Thời gian, Số lượng, Đơn giá. |
| **Thực chạy** | Doanh số/Sản lượng thực tế đã thực hiện. | SoLuongThucChay, ThanhTienThucChay. |
| **Lệch treo hạ** | Trạng thái vượt quá số lượng/giá trị hợp đồng. | LechTreoHa (Quantity/Value overflow). |

---

## 5. Quy tắc Nghiệp vụ (Business Rules)

### 5.1 Quy tắc chung (Global Rules)
- **BR-001 (Hủy/Xóa):** Khi `DeletedStatus = 1`, đối trừ toàn bộ giá trị về 0.
- **BR-002 (Làm tròn):** Thành tiền và Số lượng làm tròn 02 chữ số thập phân.
- **BR-003 (Banner-SP):** 1 banner chỉ gắn với 1 sản phẩm tại một thời điểm.
- **BR-004 (Chốt số):** Sau khi đội Kiểm soát chốt, không được thay đổi dữ liệu trừ khi có phê duyệt từ Lãnh đạo.

### 5.2 Quy tắc tính toán (Calculation Rules)
- **BR-C-01:** Doanh số thực chạy không được vượt quá giá trị phân bổ (trừ trường hợp được cấu hình cho phép).
- **BR-C-02:** Đối trừ (Offset) = Giá trị tính toán mới - Giá trị đã ghi nhận trước đó.

---

## 6. Workflows (Luồng nghiệp vụ)

### 6.1 Chu kỳ vận hành hàng ngày (Daily Cycle)
**Trigger:** Thời gian hệ thống hoặc lịch lịch trình Agent.
**Happy Path:**
1. **B1:** RecurringJob lấy dữ liệu nguồn sản phẩm đưa vào `Data thuc chay`.
2. **B2:** Agent Job đồng bộ HĐ/HĐCT và chuẩn hóa dữ liệu vào bảng `ThucChay`.
3. **B3:** Agent Job tính toán tự động (bắt đầu lúc 08:00 AM).
4. **B4:** Đội Kiểm soát rà soát, yêu cầu viết SP fix/bổ sung (09:00 AM).

### 6.2 Luồng Tính Mới (New Calculation)
**Trigger:** Có dữ liệu thực treo mới chưa được ghi nhận trong `ThucChayDaTinh`.
**Quy trình:**
1. Kiểm tra điều kiện tồn tại của bản ghi.
2. Áp dụng công thức tính toán theo nhóm sản phẩm (M3).
3. Ghi dữ liệu lần đầu vào `ThucChayDaTinh`.

### 6.3 Luồng Tính Lại / Đối trừ (Recalculate / Offset)
**Trigger:** Có sự thay đổi dữ liệu gốc hoặc yêu cầu từ đội Kiểm soát.
**Quy trình:**
1. Xác định các phân bổ bị ảnh hưởng (qua bảng `*ThayDoi` hoặc `CDC`).
2. Xóa dữ liệu cũ hoặc tính toán giá trị mới toàn kỳ.
3. Tính chênh lệch `GiaTriThayDoi`.
4. Ghi nhận bản ghi điều chỉnh vào `ThucChayDaTinh`.

---

## 7. Invariants (Ràng buộc bất biến)

- **INV-01:** Tổng doanh số thực chạy chốt cuối cùng không được âm.
- **INV-02:** Mã hợp đồng trong `ThucChayDaTinh` phải luôn tồn tại trong bảng `HopDong`.

---

## 8. Ghi chú & Caveats (Notes)

- **Chế độ phân rã:** Mode C (Dựa trên cấu trúc 5 bước của người dùng).
- **Phạm vi:** Tài liệu này chỉ tập trung đến hết Bước 4 (Hỗ trợ Kiểm soát).
