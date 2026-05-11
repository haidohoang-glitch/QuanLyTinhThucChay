# Table: `DmNhomWebsiteTag`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmNhomWebsiteTagID` | `INT` PK |  |
| `TenNhomWebsiteTag` | `NVARCHAR(200)` nullable |  |
| `TypeNhomWebsiteTag` | `INT` nullable |  |
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
| `PK_DmNhomWebsiteTag` | `DmNhomWebsiteTagID` | PRIMARY KEY |
