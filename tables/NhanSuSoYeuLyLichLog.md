# Table: `NhanSuSoYeuLyLichLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `NhanSuSoYeuLyLichLogID` | `BIGINT` PK |  |
| `NhanSuSoYeuLyLichID` | `INT` nullable |  |
| `MaNhanSu` | `NVARCHAR(200)` nullable |  |
| `HoVaTen` | `NVARCHAR(200)` nullable |  |
| `BiDanh` | `NVARCHAR(200)` nullable |  |
| `NgaySinh` | `DATETIME` nullable |  |
| `NoiSinh` | `NVARCHAR(200)` nullable |  |
| `GioiTinh` | `INT` nullable |  |
| `SoCMTND` | `NVARCHAR(200)` nullable |  |
| `NoiCap` | `NVARCHAR(200)` nullable |  |
| `NgayCap` | `DATETIME` nullable |  |
| `HoKhauThuongTru` | `NVARCHAR(200)` nullable |  |
| `DiaChiThuongTru` | `NVARCHAR(200)` nullable |  |
| `DiaChiLienHe` | `NVARCHAR(200)` nullable |  |
| `DanToc` | `NVARCHAR(200)` nullable |  |
| `TonGiao` | `NVARCHAR(200)` nullable |  |
| `TrinhDoVanHoa` | `NVARCHAR(200)` nullable |  |
| `TrinhDoNgoaiNgu` | `NVARCHAR(200)` nullable |  |
| `QuaTrinhBanThan` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `Email` | `NVARCHAR(200)` nullable |  |
| `EmailCaNhan` | `NVARCHAR(200)` nullable |  |
| `Mobile` | `NVARCHAR(200)` nullable |  |
| `DienThoai1` | `NVARCHAR(200)` nullable |  |
| `DienThoai2` | `NVARCHAR(200)` nullable |  |
| `Code` | `BIGINT` nullable |  |
| `NgayBatDauLamViec` | `DATETIME` nullable |  |
| `NgayNghiViec` | `DATETIME` nullable |  |
| `ImageFIleName` | `NVARCHAR(200)` nullable |  |
| `ImageFIleNameEncode` | `NVARCHAR(200)` nullable |  |
| `MaSoThue` | `NVARCHAR(200)` nullable |  |
| `IsNhanSuYN` | `INT` nullable |  |
| `BanMem` | `NVARCHAR(200)` nullable |  |
| `ThoiGianLog` | `DATETIME` nullable |  |
| `NguoiLog` | `NVARCHAR(200)` nullable |  |
| `LoaiLog` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_NhanSuSoYeuLyLichLog` | `NhanSuSoYeuLyLichLogID` | PRIMARY KEY |
