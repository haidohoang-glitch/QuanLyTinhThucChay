# Table: `DmBoPhan`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmBoPhanID` | `INT` PK |  |
| `TenBoPhan` | `NVARCHAR(200)` nullable |  |
| `DmPhongBanFK` | `INT` nullable |  |
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
| `PK_DmBoPhan` | `DmBoPhanID` | PRIMARY KEY |
