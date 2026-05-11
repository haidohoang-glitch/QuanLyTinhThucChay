# Table: `AdminPermistionUsers`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdminPermisionUserID` | `INT` PK IDENTITY |  |
| `UserName` | `NVARCHAR(50)` nullable |  |
| `Description` | `NVARCHAR(255)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CratedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdminPermistionUsers` | `AdminPermisionUserID` | PRIMARY KEY |
