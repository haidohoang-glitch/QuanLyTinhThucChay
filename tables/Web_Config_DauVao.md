# Table: `Web_Config_DauVao`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `ProductGroup` | `NVARCHAR(100)` nullable |  |
| `SQLFile` | `NVARCHAR(500)` nullable |  |
| `Title` | `NVARCHAR(255)` nullable |  |
| `Priority` | `INT` DEFAULT 10 nullable |  |
| `Status` | `BIT` DEFAULT 1 nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |
| `DatabaseName` | `NVARCHAR(255)` DEFAULT 'ABM_Data_ThucChay' nullable |  |
| `SpName` | `NVARCHAR(255)` nullable |  |
| `IsLogging` | `BIT` DEFAULT 1 nullable |  |
| `LogTable` | `NVARCHAR(500)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__Web_Conf__3214EC071BCF1EE7` | `Id` | PRIMARY KEY |
