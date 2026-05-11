# Table: `KhachHangThongTinChung`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `KhachHangThongTinChungID` | `BIGINT` PK |  |
| `TenKhachHang` | `NVARCHAR(500)` nullable |  |
| `TenVietTat` | `NVARCHAR(200)` nullable |  |
| `TenTiengAnh` | `NVARCHAR(200)` nullable |  |
| `MaKhachHang` | `BIGINT` nullable |  |
| `TenHinhThucKhachHang` | `NVARCHAR(200)` nullable |  |
| `DmHinhThucKhachHangREF` | `INT` nullable | 1: NB, 2: Ca nhan, 3: DaiLy, 4: Doanh Nghiep |
| `MaHinhThucKhachHang` | `NVARCHAR(200)` nullable |  |
| `DmLoaiKhachHang` | `SMALLINT` nullable |  |
| `TenLoaiKhachHang` | `NVARCHAR(100)` nullable |  |
| `MaSoThue` | `NVARCHAR(200)` nullable |  |
| `MaSoDangKyKinhDoanh` | `NVARCHAR(200)` nullable |  |
| `SoCMND` | `NVARCHAR(200)` nullable |  |
| `NgayCap` | `DATETIME` nullable |  |
| `NoiCap` | `NVARCHAR(200)` nullable |  |
| `DiaChiKhachHang` | `NVARCHAR(500)` nullable |  |
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
| `KhachHangThongTinChungREF` | `INT` nullable |  |
| `KhachHangThuocCapThu` | `INT` nullable |  |
| `TenNguoiDaiDien` | `NVARCHAR(200)` nullable |  |
| `GioiTinhNguoiDaiDien` | `NVARCHAR(200)` nullable |  |
| `DmChuVuREF` | `INT` nullable |  |
| `ChucVu` | `NVARCHAR(200)` nullable |  |
| `SoDienThoaiNguoiDaiDien` | `NVARCHAR(200)` nullable |  |
| `ThongTinKhac` | `NVARCHAR(200)` nullable |  |
| `TenFileDiKem` | `NVARCHAR(500)` nullable |  |
| `UrlTaiLieu` | `NVARCHAR(500)` nullable |  |
| `MoTaTaiLieuDiKem` | `NVARCHAR(500)` nullable |  |
| `GhiChu` | `NVARCHAR(500)` nullable |  |
| `CoMaSoThueYN` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(200)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `quanhuyen` | `INT` nullable |  |
| `tinh_thanhpho` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_KhachHangThongTinChung` | `KhachHangThongTinChungID` | PRIMARY KEY |
