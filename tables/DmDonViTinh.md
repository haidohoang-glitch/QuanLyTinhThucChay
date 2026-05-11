# Table: `DmDonViTinh`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmDonViTinhID` | `BIGINT` PK |  |
| `MaDonViTinh` | `NVARCHAR(200)` nullable |  |
| `TenDonViTinh` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `TINYINT` nullable |  |
| `PrintStatus` | `TINYINT` nullable |  |
| `RecordStatus` | `TINYINT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmDonViTinh` | `DmDonViTinhID` | PRIMARY KEY |
