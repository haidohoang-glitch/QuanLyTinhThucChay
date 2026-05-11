# Table: `AdminMenu`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdminMenuId` | `INT` PK IDENTITY |  |
| `ParentId` | `INT` nullable |  |
| `Priority` | `INT` nullable |  |
| `Status` | `INT` nullable |  |
| `Name` | `NVARCHAR(1024)` nullable |  |
| `CtrlKey` | `NVARCHAR(512)` nullable |  |
| `Description` | `NVARCHAR(2048)` nullable |  |
| `CtrlSource` | `NVARCHAR(2048)` nullable |  |
| `Params` | `NVARCHAR(2048)` nullable |  |
| `IsCheck` | `INT` NN DEFAULT 0 |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdminMenu` | `AdminMenuId` | PRIMARY KEY |
