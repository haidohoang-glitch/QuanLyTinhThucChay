# Table: `QuyenChucNangNhomQuyenLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `QuyenChucNangNhomQuyenLogID` | `INT` PK |  |
| `DmNhomNguoiDungREF` | `INT` nullable |  |
| `TenNhomNguoiDung` | `NVARCHAR(200)` nullable |  |
| `DmChucNangREF` | `INT` nullable |  |
| `TenChucNang` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
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
| `PK_QuyenChucNangNhomQuyenLog` | `QuyenChucNangNhomQuyenLogID` | PRIMARY KEY |
