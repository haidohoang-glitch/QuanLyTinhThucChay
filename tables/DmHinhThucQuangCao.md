# Table: `DmHinhThucQuangCao`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmHinhThucQuangCaoID` | `INT` PK |  |
| `MaDmHinhThucQuangCao` | `NVARCHAR(50)` nullable |  |
| `TenHinhThucQuangCao` | `NVARCHAR(50)` nullable |  |
| `GhiChu` | `NVARCHAR(MAX)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmHinhThucQuangCao` | `DmHinhThucQuangCaoID` | PRIMARY KEY |
