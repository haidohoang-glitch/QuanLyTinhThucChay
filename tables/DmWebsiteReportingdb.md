# Table: `DmWebsiteReportingdb`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmWebsiteReportingdbID` | `INT` PK IDENTITY |  |
| `TenWebsite` | `NVARCHAR(1000)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `ID` | `NVARCHAR(50)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csDmWebsiteReportingdb` | `DmWebsiteReportingdbID` | PRIMARY KEY |
| `NonClusteredIndex-20140305-145608` | `TenWebsite` | BTREE |
