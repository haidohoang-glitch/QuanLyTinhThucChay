# Table: `NhanSuQuaTrinhCongTacLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `NhanSuQuaTrinhCongTacLogID` | `INT` PK |  |
| `NhanSuQuaTrinhCongTacREF` | `INT` nullable |  |
| `TenNhanSu` | `NVARCHAR(200)` nullable |  |
| `MaNhanSu` | `NVARCHAR(200)` nullable |  |
| `NhanSuSoYeuLyLichREF` | `INT` nullable |  |
| `SoHopDongLaoDong` | `NVARCHAR(200)` nullable |  |
| `HinhThucLaoDongREF` | `INT` nullable |  |
| `DmPhongBanREF` | `BIGINT` nullable |  |
| `DmBoPhanREF` | `BIGINT` nullable |  |
| `DmNhomREF` | `INT` nullable |  |
| `DmDiaDiemLamViecREF` | `BIGINT` nullable |  |
| `DmChucDanhREF` | `INT` nullable |  |
| `NgayBatDauLamViec` | `DATETIME` nullable |  |
| `NgayKetThucLamViec` | `DATETIME` nullable |  |
| `NgayDiLam` | `DATETIME` nullable |  |
| `NgayNghiViec` | `DATETIME` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `Active` | `INT` nullable |  |
| `NhanSuSoYeuLyLichThayTheREF` | `INT` nullable |  |
| `HinhThucTuyenDungID` | `INT` nullable |  |
| `HinhThucTuyenDung` | `NVARCHAR(200)` nullable |  |
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
| `PK_NhanSuQuaTrinhCongTacLog` | `NhanSuQuaTrinhCongTacLogID` | PRIMARY KEY |
