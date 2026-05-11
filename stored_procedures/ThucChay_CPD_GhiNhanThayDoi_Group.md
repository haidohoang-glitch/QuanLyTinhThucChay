# Phân Hệ SP: CPD - Ghi Nhận Thay Đổi (Đối Trừ & Tính Lại)

> **Nhóm này bao gồm 3 SP chịu trách nhiệm phát hiện và xử lý dữ liệu khi hợp đồng/phân bổ trong quá khứ bị sửa đổi/xóa.** Đây là cấu trúc tài liệu rút gọn chuẩn AI để giảm thiểu Token.
1. `ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh`
2. `ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh`
3. `ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh`

---

## 1. Input / Output Tables

### Input (Dữ liệu quét thay đổi)
- Các bảng nguồn tương tự phân hệ Tính mới (`HopDong`, `HopDongChiTiet`, `ThucChayHopDongChiTiet`, `DotChayHopDongChiTiet`).
- Lọc bổ sung điều kiện về thời gian thay đổi: `LastModifiedAt = @NgayCheckThayDoi` hoặc `DeletedStatus = 1`.
- Quét đối chiếu ngược lại bảng đích `ThucChayDaTinh` (tổng số lượng, tổng tiền đã tính trong quá khứ).

### Output (Xử lý chênh lệch)
- Bảng `ThucChayDaTinh`:
  - **INSERT 1 (Ghi Nhận Đối Trừ)**: Tạo một bản ghi mang giá trị **ÂM** (`-SUM(...)`) bằng chính xác lượng chênh lệch (Delta). Cột `GhiChu LIKE N'Đối trừ%'`.
  - **INSERT 2 (Tính Lại Thực Chạy)**: Tạo một bản ghi mang giá trị **DƯƠNG** tính theo cấu trúc dữ liệu và đơn giá mới nhất. Cột `GhiChu LIKE N'Tính lại%'`.
- Bảng `ThucChayHopDongChiTiet` (Chỉ Đơn vị gói):
  - **UPDATE**: Cập nhật `RecordStatus = 0` (khi đối trừ) và `RecordStatus = 1` (khi đã tính lại).

---

## 2. Business Logic Cốt Lõi (4 Bước)

### Bước 1: Clean-up (Cho phép Job chạy lại nhiều lần)
- DELETE ngay các bản ghi `Đối trừ` và `Tính lại` đã được sinh ra trong cùng ngày hôm nay (`@NgayGhiNhan`). Giúp hệ thống không bao giờ bị nhân đôi dữ liệu nếu Job chạy fail và được chạy lại bằng tay.

### Bước 2: Xác định tập dữ liệu thay đổi
Quét hệ thống và dán nhãn (`Loaithaydoi`, `Mathaydoi`) cho các trường hợp:
1. Sửa thông tin hợp đồng / phân bổ (đơn giá, chiết khấu).
2. Sửa thông tin đợt chạy đánh số.
3. Sửa thông tin đợt chạy thực treo.
4. Xóa phân bổ (`DeletedStatus = 1`).
5. Can thiệp chạy tay qua biến `@SoHopDong`.

### Bước 3: Tính toán Delta (Đối Trừ)
- Tính tổng giá trị lý thuyết đến hiện tại dựa trên số liệu vừa sửa.
- Tính tổng giá trị thực tế đã ghi nhận trong bảng `ThucChayDaTinh`.
- Sinh ra dòng dữ liệu với **Thành tiền chênh lệch = (Giá trị lý thuyết HT - Giá trị thực tế đã lưu)**.

### Bước 4: Tính Lại Dữ Liệu
- Apply công thức tính doanh số tương tự như phân hệ Tính Mới, nhưng gán với mác "Tính lại do thay đổi thông tin..." để Audit.
