# Table: `AdminPermisionUsersByTime`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdminPermisionUsersByTimeID` | `NVARCHAR(255)` PK |  |
| `UserName` | `NVARCHAR(50)` nullable |  |
| `Note` | `NVARCHAR(512)` nullable |  |
| `StartDateActive` | `DATETIME` nullable |  |
| `EndDateActive` | `DATETIME` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdminPermisionUsersByTime` | `AdminPermisionUsersByTimeID` | PRIMARY KEY |
