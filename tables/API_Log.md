# Table: `API_Log`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `CallFrom` | `NVARCHAR(500)` nullable |  |
| `CreatedTime` | `DATETIME` nullable |  |
| `API` | `NVARCHAR(2000)` nullable |  |
| `Params` | `NVARCHAR(MAX)` nullable |  |
| `IsDeleted` | `BIT` DEFAULT 0 nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_API_Log` | `Id` | PRIMARY KEY |
