# Table: `Web_Config_Rules`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `Name` | `NVARCHAR(255)` nullable |  |
| `TargetGroup` | `NVARCHAR(100)` nullable |  |
| `Priority` | `INT` DEFAULT 10 nullable |  |
| `ConditionJson` | `NVARCHAR(MAX)` nullable |  |
| `Status` | `BIT` DEFAULT 1 nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__Web_Conf__3214EC070B959B0F` | `Id` | PRIMARY KEY |
