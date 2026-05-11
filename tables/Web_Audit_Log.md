# Table: `Web_Audit_Log`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AuditId` | `INT` PK IDENTITY |  |
| `Username` | `NVARCHAR(100)` nullable |  |
| `Action` | `NVARCHAR(255)` nullable |  |
| `Description` | `NVARCHAR(MAX)` nullable |  |
| `TargetType` | `NVARCHAR(100)` nullable |  |
| `TargetId` | `NVARCHAR(100)` nullable |  |
| `NgayThucHien` | `DATETIME` DEFAULT getdate nullable |  |
| `IPAddress` | `NVARCHAR(50)` nullable |  |
| `Browser` | `NVARCHAR(MAX)` nullable |  |
| `Status` | `INT` DEFAULT 1 nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `IX_Web_Audit_Log_NgayThucHien` | `NgayThucHien` | BTREE |
| `IX_Web_Audit_Log_Username` | `Username` | BTREE |
| `PK__Web_Audi__A17F2398AA59CCAE` | `AuditId` | PRIMARY KEY |
