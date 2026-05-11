# Table: `Web_Config_Chitiet`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `Title` | `NVARCHAR(255)` nullable |  |
| `ProductGroup` | `NVARCHAR(100)` nullable |  |
| `DisplayGroup` | `NVARCHAR(255)` nullable |  |
| `Priority` | `INT` DEFAULT 10 nullable |  |
| `Status` | `BIT` DEFAULT 1 nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |
| `SpName` | `NVARCHAR(255)` nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `DatabaseName` | `NVARCHAR(255)` DEFAULT 'ABM_Data_ThucChay' nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__Web_Conf__3214EC07E26B9CD0` | `Id` | PRIMARY KEY |
