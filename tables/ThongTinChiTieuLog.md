# Table: `ThongTinChiTieuLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThongTinChiTieuLogID` | `INT` PK IDENTITY |  |
| `ChiTieuBoPhan` | `NVARCHAR(50)` nullable |  |
| `DmChiTieuBoPhanREF` | `INT` nullable |  |
| `LevelChiTieu` | `INT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `DoanhSoChiTieu` | `NUMERIC(20,5)` nullable |  |
| `LoaiTien` | `INT` nullable |  |
| `TenLoaiTien` | `NVARCHAR(100)` nullable |  |
| `NguoiDangKy` | `NVARCHAR(100)` nullable |  |
| `NguoiXacNhan` | `NVARCHAR(100)` nullable |  |
| `GhiChu` | `NVARCHAR(MAX)` nullable |  |
| `ThongTinChiTieuREF` | `INT` nullable |  |
| `LoaiLog` | `INT` nullable |  |
| `NguoiLog` | `NVARCHAR(100)` nullable |  |
| `NgayLog` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(100)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeleteStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThongTinChiTieuLog` | `ThongTinChiTieuLogID` | PRIMARY KEY |
