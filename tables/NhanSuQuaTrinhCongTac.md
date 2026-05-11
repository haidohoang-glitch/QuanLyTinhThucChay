# Table: `NhanSuQuaTrinhCongTac`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `NhanSuQuaTrinhCongTacID` | `INT` PK |  |
| `SoHopDongLaoDong` | `NVARCHAR(50)` nullable |  |
| `NhanSuSoYeuLyLichREF` | `INT` NN |  |
| `HinhThucLaoDong` | `INT` nullable |  |
| `DmPhongBanREF` | `INT` nullable |  |
| `DmBoPhanREF` | `INT` nullable |  |
| `DmNhomLamViecREF` | `INT` nullable |  |
| `DmDiaDiemLamViecREF` | `INT` nullable |  |
| `DmChucDanhREF` | `INT` nullable |  |
| `NgayBatDauLamViec` | `DATETIME` nullable |  |
| `NgayNghiViec` | `DATETIME` nullable |  |
| `GhiChu` | `NVARCHAR(4000)` nullable |  |
| `Active` | `INT` NN |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `TenNhanSu` | `NVARCHAR(200)` nullable |  |
| `MaNhanSu` | `NVARCHAR(200)` nullable |  |
| `HinhThucLaoDongREF` | `INT` nullable |  |
| `DmNhomREF` | `INT` nullable |  |
| `NgayKetThucLamViec` | `DATETIME` nullable |  |
| `NgayDiLam` | `DATETIME` nullable |  |
| `NhanSuSoYeuLyLichThayTheREF` | `INT` nullable |  |
| `HinhThucTuyenDungID` | `INT` nullable |  |
| `HinhThucTuyenDung` | `NVARCHAR(200)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csNhanSuQuaTrinhCongTac` | `NhanSuQuaTrinhCongTacID` | PRIMARY KEY |
