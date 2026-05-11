# Table: `Web_Log_Common`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `LogId` | `INT` PK IDENTITY |  |
| `ConfigId` | `INT` nullable |  |
| `StepType` | `NVARCHAR(50)` nullable |  |
| `ProductGroup` | `NVARCHAR(100)` nullable |  |
| `Title` | `NVARCHAR(255)` nullable |  |
| `NgayThucHien` | `DATE` nullable |  |
| `NguoiThucHien` | `NVARCHAR(100)` nullable |  |
| `NgayKiemTra` | `DATETIME` DEFAULT getdate nullable |  |
| `LogData` | `NVARCHAR(MAX)` nullable |  |
| `TotalRows` | `INT` nullable |  |
| `Status` | `INT` DEFAULT 1 nullable |  |
| `Message` | `NVARCHAR(MAX)` nullable |  |
| `TotalSource` | `INT` nullable |  |
| `TotalTarget` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `IX_Web_Log_Common_ConfigId` | `ConfigId` | BTREE |
| `IX_Web_Log_Common_NgayThucHien` | `NgayThucHien` | BTREE |
| `PK__Web_Log___5E5486487D8A9B78` | `LogId` | PRIMARY KEY |
