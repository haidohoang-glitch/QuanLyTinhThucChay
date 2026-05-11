# Table: `DmPhongBan`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmPhongBanID` | `INT` PK |  |
| `MaSoPhongBan` | `NVARCHAR(200)` nullable |  |
| `TenPhongBan` | `NVARCHAR(200)` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `BIGINT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmPhongBan` | `DmPhongBanID` | PRIMARY KEY |
