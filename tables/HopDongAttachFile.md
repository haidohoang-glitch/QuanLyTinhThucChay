# Table: `HopDongAttachFile`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `HopDongAttachFileID` | `BIGINT` PK |  |
| `HopDongREF` | `INT` NN |  |
| `fileName` | `NVARCHAR(200)` nullable |  |
| `Url` | `NVARCHAR(2000)` nullable |  |
| `FileTypeREF` | `INT` nullable |  |
| `description` | `NVARCHAR(200)` nullable |  |
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
| `PK_HopDongAttachFile` | `HopDongAttachFileID` | PRIMARY KEY |
