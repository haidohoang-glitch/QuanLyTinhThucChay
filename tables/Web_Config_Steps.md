# Table: `Web_Config_Steps`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `StepType` | `NVARCHAR(50)` nullable |  |
| `ProductGroup` | `NVARCHAR(100)` nullable |  |
| `SQLFile` | `NVARCHAR(500)` nullable |  |
| `Title` | `NVARCHAR(255)` nullable |  |
| `SpName` | `NVARCHAR(255)` nullable |  |
| `Priority` | `INT` DEFAULT 10 nullable |  |
| `Status` | `BIT` DEFAULT 1 nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |
| `DatabaseName` | `NVARCHAR(255)` DEFAULT 'ABM_Data_ThucChay' nullable |  |
| `IsLogging` | `BIT` DEFAULT 1 nullable |  |
| `LogTable` | `NVARCHAR(255)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__Web_Conf__3214EC076802C2F9` | `Id` | PRIMARY KEY |
