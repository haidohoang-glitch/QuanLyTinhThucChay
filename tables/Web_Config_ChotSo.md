# Table: `Web_Config_ChotSo`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `ProductGroup` | `NVARCHAR(100)` nullable |  |
| `Title` | `NVARCHAR(255)` nullable |  |
| `SpName` | `NVARCHAR(255)` nullable |  |
| `DatabaseName` | `NVARCHAR(255)` DEFAULT 'ABM_Data_ThucChay' nullable |  |
| `Priority` | `INT` DEFAULT 10 nullable |  |
| `Status` | `BIT` DEFAULT 1 nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |
| `SQLFile` | `NVARCHAR(255)` nullable |  |
| `IsLogging` | `BIT` DEFAULT 1 nullable |  |
| `LogTable` | `NVARCHAR(255)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__Web_Conf__3214EC07642B8308` | `Id` | PRIMARY KEY |
