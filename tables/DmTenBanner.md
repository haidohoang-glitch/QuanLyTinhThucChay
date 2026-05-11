# Table: `DmTenBanner`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmBannerID` | `INT` PK |  |
| `TenBanner` | `NVARCHAR(200)` nullable |  |
| `InTypeTool` | `NVARCHAR(200)` nullable |  |
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
| `PK_DmTenBanner` | `DmBannerID` | PRIMARY KEY |
