# SP: ThucChay_CPD_Job (Orchestrator)

## 1. Mô Tả Tổng Quan
Đây là SP điều phối cấp cao nhất cho tiến trình tính CPD. Nhiệm vụ chính là xác định khoảng thời gian tính toán và tuần tự gọi các SP con để xử lý chi tiết.

## 2. Parameter & Biến Số
- **Không có Input Parameters**.
- Các biến tự tính toán bên trong:
  - `@dtStart`, `@dtEnd`, `@NgayThucHien`: Tự động lấy **Ngày hôm qua** (`DATEADD(dd,-1, GETDATE())`).
  - `@NgayDanhSo_GioiHan`: Lấy dữ liệu giới hạn **3 năm quay đầu** từ ngày tính.

## 3. Các Bảng Tương Tác
- SP này **không trực tiếp tương tác** với Table nào (không có lệnh INSERT/UPDATE/DELETE). Nhiệm vụ của nó chỉ là tính toán ngày và truyền tham số cho các SP con.

## 4. Trình Tự Thực Thi (Dependencies)
SP này gọi 6 SP con theo thứ tự:
1. `ThucChay_CPDdotchay_PhatSinhThucChay_ThucChayDaTinh` (Tham số: Start, End, GioiHan)
2. `ThucChay_CPDkhongdotchay_PhatSinhThucChay_ThucChayDaTinh` (Tham số: Start, End, GioiHan)
3. `ThucChay_CPDdonvigoi_PhatSinhThucChay_ThucChayDaTinh` (Tham số: NgayThucHien, GioiHan)
4. `ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh` (Tham số: NgayThucHien, NgayThucHien, GioiHan)
5. `ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh` (Tham số: NgayThucHien, NgayThucHien, GioiHan)
6. `ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh` (Tham số: NgayThucHien, NgayThucHien, GioiHan)
