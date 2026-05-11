# Table: `Web_Config_DauHieu`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `DauHieu` | `NVARCHAR(MAX)` nullable |  |
| `ProductGroup` | `NVARCHAR(100)` nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__Web_Conf__3214EC07365572E7` | `Id` | PRIMARY KEY |
