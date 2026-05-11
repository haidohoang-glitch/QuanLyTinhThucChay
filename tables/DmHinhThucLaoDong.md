# Table: `DmHinhThucLaoDong`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmHinhThucLaoDongID` | `INT` PK |  |
| `TenHinhThucLaoDong` | `NVARCHAR(200)` nullable |  |
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
| `PK_DmHinhThucLaoDong` | `DmHinhThucLaoDongID` | PRIMARY KEY |
