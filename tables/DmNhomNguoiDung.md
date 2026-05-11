# Table: `DmNhomNguoiDung`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmNhomNguoiDungID` | `INT` PK |  |
| `TenNhomNguoiDung` | `NVARCHAR(200)` nullable |  |
| `MaNhomNguoiDung` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
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
| `PK_DmNhomNguoiDung` | `DmNhomNguoiDungID` | PRIMARY KEY |
