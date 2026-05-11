# Table: `CauHinhHeThong`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `GroupName` | `NVARCHAR(255)` nullable |  |
| `BigBlock` | `NVARCHAR(255)` nullable |  |
| `TableName` | `NVARCHAR(255)` nullable |  |
| `SQLFile` | `NVARCHAR(500)` nullable |  |
| `OrderIndex` | `INT` DEFAULT 0 nullable |  |
| `Status` | `BIT` DEFAULT 1 nullable |  |
| `Prioritize` | `BIT` DEFAULT 0 nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__CauHinhH__3214EC0741EFE28A` | `Id` | PRIMARY KEY |
