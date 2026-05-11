# Table: `KhachHangThongTinChungLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `KhachHangThongTinChungLogID` | `BIGINT` PK IDENTITY |  |
| `KhachHangThongTinChungREF` | `BIGINT` nullable |  |
| `TenKhachHang` | `NVARCHAR(200)` nullable |  |
| `TenVietTat` | `NVARCHAR(200)` nullable |  |
| `TenTiengAnh` | `NVARCHAR(200)` nullable |  |
| `MaKhachHang` | `BIGINT` nullable |  |
| `TenHinhThucKhachHang` | `NVARCHAR(200)` nullable |  |
| `DmHinhThucKhachHangREF` | `INT` nullable |  |
| `MaHinhThucKhachHang` | `NVARCHAR(200)` nullable |  |
| `MaSoThue` | `NVARCHAR(200)` nullable |  |
| `MaSoDangKyKinhDoanh` | `NVARCHAR(200)` nullable |  |
| `SoCMND` | `NVARCHAR(200)` nullable |  |
| `NgayCap` | `DATETIME` nullable |  |
| `NoiCap` | `NVARCHAR(200)` nullable |  |
| `DiaChiKhachHang` | `NVARCHAR(200)` nullable |  |
| `SoDienThoai` | `NVARCHAR(200)` nullable |  |
| `SoDienThoai2` | `NVARCHAR(200)` nullable |  |
| `SoDienThoai3` | `NVARCHAR(200)` nullable |  |
| `Mobile` | `NVARCHAR(200)` nullable |  |
| `SoFax` | `NVARCHAR(200)` nullable |  |
| `Email` | `NVARCHAR(200)` nullable |  |
| `Email2` | `NVARCHAR(200)` nullable |  |
| `SoTaiKhoan` | `NVARCHAR(200)` nullable |  |
| `MoTaiNganHang` | `NVARCHAR(200)` nullable |  |
| `NgaySinh_NgayThanhLapCty` | `DATETIME` nullable |  |
| `WebsiteCty` | `NVARCHAR(200)` nullable |  |
| `LinhVucKinhDoanh` | `NVARCHAR(200)` nullable |  |
| `KhachHangThongTinChungREF1` | `INT` nullable |  |
| `KhachHangThuocCapThu` | `INT` nullable |  |
| `TenNguoiDaiDien` | `NVARCHAR(200)` nullable |  |
| `GioiTinhNguoiDaiDien` | `NVARCHAR(200)` nullable |  |
| `DmChuVuREF` | `INT` nullable |  |
| `ChucVu` | `NVARCHAR(200)` nullable |  |
| `SoDienThoaiNguoiDaiDien` | `NVARCHAR(200)` nullable |  |
| `ThongTinKhac` | `NVARCHAR(200)` nullable |  |
| `TenFileDiKem` | `NVARCHAR(200)` nullable |  |
| `UrlTaiLieu` | `NVARCHAR(200)` nullable |  |
| `MoTaTaiLieuDiKem` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `ThoiGianLog` | `DATETIME` nullable |  |
| `NguoiLog` | `NVARCHAR(200)` nullable |  |
| `LoaiLog` | `INT` nullable |  |
| `CoMaSoThueYN` | `INT` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_KhachHangThongTinChungLog` | `KhachHangThongTinChungLogID` | PRIMARY KEY |
