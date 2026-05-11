# Table: `DmFileType`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `DmFileTypeID` | `BIGINT` PK |  |
| `FileTypeName` | `NVARCHAR(200)` NN |  |
| `Ordering` | `INT` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `LoaiFileCanBanCung` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_DmFileType` | `DmFileTypeID` | PRIMARY KEY |
