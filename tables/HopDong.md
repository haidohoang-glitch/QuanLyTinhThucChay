# Table: `HopDong`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongID` | `INT` PK | ID primary key của table HopDong |
| `DmMaHopDongREF` | `INT` nullable | ID foreign key từ table DmMaHopDong |
| `TenMaHopDong` | `NVARCHAR(50)` nullable | Mã hợp đồng |
| `So` | `NVARCHAR(50)` nullable |  |
| `Thang` | `INT` nullable |  |
| `Nam` | `INT` nullable |  |
| `NgayKyHopDong` | `DATETIME` nullable | Ngày ký hợp đồng |
| `NhanHopDong` | `NVARCHAR(1000)` nullable | Nhãn hợp đồng |
| `GiaTriHopDong` | `FLOAT` nullable | Giá trị hợp đồng |
| `SoHopDong` | `NVARCHAR(50)` nullable | Mã số hợp đồng |
| `NgayChuyenHopDongChoKeToan` | `DATETIME` nullable |  |
| `GhiChu` | `NVARCHAR(300)` nullable |  |
| `NgayNhanHopDongBanCung` | `DATETIME` nullable |  |
| `DmKhachHangREF` | `INT` nullable | ID foreign key từ table Customer |
| `TenKhachHang` | `NVARCHAR(255)` nullable | Tên khách hàng |
| `DmHinhThucKhachHangREF` | `INT` nullable |  |
| `TenHinhThucKhachHang` | `NVARCHAR(100)` nullable |  |
| `DmLoaiKhachHangREF` | `INT` nullable |  |
| `TenLoaiKhachHang` | `NVARCHAR(100)` nullable |  |
| `SysNhanVienREF` | `INT` nullable | ID foreign key từ table Nhansusoyeulylich |
| `TenDangNhap` | `NVARCHAR(25)` nullable | tên đăng nhập của nhân viên sale |
| `TenNhanVien` | `NVARCHAR(100)` nullable | Tên nhân viên sale |
| `NgayDanhSoHopDong` | `DATETIME` nullable | Ngày đánh số hợp đồng |
| `NganhHang` | `NVARCHAR(1000)` nullable | Ngành hàng |
| `DmNhomREF` | `INT` nullable | ID foreign key từ table DmNhom |
| `TrangThaiHopDong` | `INT` nullable | Trạng thái của hợp đồng |
| `IsBanCung` | `INT` nullable |  |
| `CongNo` | `FLOAT` nullable |  |
| `GhiChuHopDong` | `NVARCHAR(4000)` nullable |  |
| `NgayNhanBanFax` | `DATETIME` nullable |  |
| `LyDoHuyHopDong` | `NVARCHAR(4000)` nullable |  |
| `DangSuDung` | `INT` nullable |  |
| `IsGiayPhep` | `INT` nullable |  |
| `DmPhongBanREF` | `INT` nullable |  |
| `TenPhongBan` | `NVARCHAR(100)` nullable |  |
| `DmBoPhanREF` | `INT` nullable |  |
| `TenBoPhan` | `NVARCHAR(100)` nullable |  |
| `DmNhomLamViecREF` | `INT` nullable |  |
| `TenNhom` | `NVARCHAR(100)` nullable |  |
| `DmDiaDiemLamViecREF` | `INT` nullable |  |
| `TenDiaDiemLamViec` | `NVARCHAR(250)` nullable |  |
| `ChuyenTrang` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable | Người tạo bản ghi dữ liệu |
| `CreatedAt` | `DATETIME` nullable | Ngày tào bản ghi dữ liệu |
| `LastModifiedBy` | `NVARCHAR(50)` nullable | Người sửa bản ghi dữ liệu |
| `LastModifiedAt` | `DATETIME` nullable | Ngày sửa bản ghi dữ liệu |
| `DeletedStatus` | `INT` nullable | = 1 là bản ghi bị xóa, = 0 là bản ghi chưa xóa |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable | Trạng thái bản ghi |
| `IsUuDai` | `INT` nullable |  |
| `ThucHienDenNgayThucChay` | `DATETIME` nullable |  |
| `ThanhTienThucChay` | `FLOAT` nullable |  |
| `ThucHienDenNgayHoaDon` | `DATETIME` nullable |  |
| `ThanhTienHoaDon` | `FLOAT` nullable |  |
| `ThucHienDenNgayCongNo` | `DATETIME` nullable |  |
| `ThanhTienCongNo` | `FLOAT` nullable |  |
| `ThanhTienThanhToan` | `BIGINT` nullable |  |
| `NgayHuyHopDong` | `DATETIME` nullable |  |
| `NguoiHuyHopDong` | `NVARCHAR(100)` nullable |  |
| `IsCalcVoucher` | `INT` nullable |  |
| `GiaTriDatCoc` | `BIGINT` nullable |  |
| `NgayDatCoc` | `DATETIME` nullable |  |
| `NgayGiaHanDatCoc` | `DATETIME` nullable |  |
| `TenNhanGoc` | `NVARCHAR(2000)` nullable |  |
| `DmNhanGocREF` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csHopDong` | `HopDongID DESC` | PRIMARY KEY |
| `IndexSoHD` | `SoHopDong, TrangThaiHopDong` | BTREE |
