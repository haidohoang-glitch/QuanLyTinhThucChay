# Table: `Web_Config_Lookup`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `Title` | `NVARCHAR(255)` NN |  |
| `GroupName` | `NVARCHAR(100)` nullable |  |
| `SpName` | `NVARCHAR(255)` NN |  |
| `DatabaseName` | `NVARCHAR(255)` DEFAULT 'ABM_Data_ThucChay' nullable |  |
| `ParamsJson` | `NVARCHAR(MAX)` nullable |  |
| `Priority` | `INT` DEFAULT 10 nullable |  |
| `Status` | `BIT` DEFAULT 1 nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |
| `CreatedBy` | `NVARCHAR(100)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__Web_Conf__3214EC07E0465978` | `Id` | PRIMARY KEY |
