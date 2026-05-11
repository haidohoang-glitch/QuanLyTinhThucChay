# Table: `NguoiDung`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `Username` | `NVARCHAR(50)` NN |  |
| `Password` | `NVARCHAR(255)` NN |  |
| `FirstName` | `NVARCHAR(100)` nullable |  |
| `LastName` | `NVARCHAR(100)` nullable |  |
| `Roles` | `NVARCHAR(255)` nullable |  |
| `Email` | `NVARCHAR(255)` nullable |  |
| `EmailConfirmed` | `BIT` DEFAULT 0 nullable |  |
| `IsActive` | `BIT` DEFAULT 1 nullable |  |
| `CreatedAt` | `DATETIME` DEFAULT getdate nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK__NguoiDun__3214EC070A37EE22` | `Id` | PRIMARY KEY |
| `UQ__NguoiDun__536C85E438B6FCF9` | `Username` | UNIQUE |
