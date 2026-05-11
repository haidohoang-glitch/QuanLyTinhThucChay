# Phân Hệ SP: CPD - Tính Mới (Phát Sinh Thực Chạy)

> **Nhóm này bao gồm 3 SP chịu trách nhiệm tính dữ liệu thực chạy mới (INSERT) cho ngày hôm qua.** Để tối ưu hóa cho AI (tiết kiệm token), các SP có logic tương đồng được gộp chung tài liệu.
1. `ThucChay_CPDdotchay_PhatSinhThucchay_ThucChayDaTinh` (CPD Hình thức có đợt chạy)
2. `ThucChay_CPDkhongdotchay_PhatSinhThucchay_ThucChayDaTinh` (CPD Hình thức không đợt chạy)
3. `ThucChay_CPDdonvigoi_PhatSinhThucchay_ThucChayDaTinh` (CPD Hình thức gói)

---

## 1. Input / Output Tables

### Input (Dữ liệu nguồn được SELECT)
- `HopDong`, `HopDongChiTiet`: Lấy thông tin hợp đồng, phân bổ, đơn giá, chiết khấu.
- `DotChayHopDongChiTiet`: Lấy thông tin đợt chạy đánh số.
- `ThucChayHopDongChiTiet`: Lấy thông tin thực treo, số lượng thực chạy (tùy theo loại hình CPD).
- `DmSanPham`: Thông tin tham chiếu danh mục sản phẩm.

### Output (Dữ liệu đích)
- Bảng `ThucChayDaTinh`: 
  - **DELETE**: Xóa các bản ghi cũ của ngày đang chạy (`NgayThucHien = @NgayThucHien`) để đảm bảo tính Idempotent (chạy lại job bao nhiêu lần trong ngày cũng không bị nhân đôi dữ liệu).
  - **INSERT**: Thêm các bản ghi tính toán mới với cột `GhiChu LIKE N'Tính mới%'`.
- Bảng `ThucChayHopDongChiTiet` (Chỉ áp dụng với loại Đơn vị gói):
  - **UPDATE**: Cập nhật `RecordStatus = 1` (đánh dấu đã tính thực chạy).

---

## 2. Business Logic Cốt Lõi

### Điều kiện lọc dữ liệu (Filters)
- **Sản phẩm CPD**: Lọc theo `DmSanPhamREF IN (140, 228, 564, 549, 5082)` (có chênh lệch nhỏ tùy SP, có SP dùng ID 241).
- **Loại hình**: Không phải loại hình Mua ngoài (`DmLoaiREF <> 13`).
- **Trạng thái hợp đồng**: Hợp đồng không bị hủy/xóa (`TrangThaiHopDong <> 3`).
- **Loại Banner**: Bỏ qua banner loại 17, 18.
- Hàm kiểm tra loại CPD: Sử dụng `[dbo].[CheckDonViTinhHinhThucCPDAndNotCPD]` để phân loại (1: Có/Không đợt chạy, 5: Đơn vị gói).

### Công thức tính toán
- **Đơn giá chuẩn**: Tùy loại hình, hệ thống sẽ chia đơn giá theo số ngày đợt chạy đánh số hoặc số ngày thực treo để ra đơn giá theo ngày.
- **Thành tiền**:
  - `ThanhTienThucChayTruocTrietKhau = dongiatheodonvitinh * (soluongthucchay + soluongKM)`
- **Các loại chi phí khác**:
  - `GiaTriTrietKhauThucChay`: Dựa trên % Chiết Khấu.
  - `GiaTriHoaHongThucChay`: Dựa trên % Tỷ Lệ Tư Vấn (đại lý).
  - Khuyến mãi: Xử lý gán toàn bộ thành tiền vào `ThanhTienKM` nếu `IsKhuyenMai = 1` hoặc `ChietKhau = 100`.
