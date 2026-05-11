# Table: `ThongTinChiTieu`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThongTinChiTieuID` | `INT` PK IDENTITY |  |
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
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |
| `LastModifiedBy` | `NVARCHAR(100)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeleteStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__ThongTin__736B2EBB3E0DBAA9` | `ThongTinChiTieuID` | PRIMARY KEY |
