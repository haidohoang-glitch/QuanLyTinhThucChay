# Table: `AdminUser`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdminUserId` | `INT` PK IDENTITY |  |
| `StoreId` | `INT` nullable |  |
| `Username` | `NVARCHAR(128)` nullable |  |
| `Password` | `NVARCHAR(128)` nullable |  |
| `Email` | `NVARCHAR(128)` nullable |  |
| `FullName` | `NVARCHAR(128)` nullable |  |
| `Birthday` | `DATETIME` nullable |  |
| `Gender` | `BIT` nullable |  |
| `Information` | `NTEXT` nullable |  |
| `Status` | `INT` nullable |  |
| `SettingValues` | `NVARCHAR(128)` nullable |  |
| `CreatedOn` | `DATETIME` nullable |  |
| `ModifiedOn` | `DATETIME` nullable |  |
| `LastLoggedOn` | `DATETIME` nullable |  |
| `NhanSuSoYeuLyLichREF` | `INT` nullable |  |
| `OxUserREF` | `INT` nullable |  |
| `Mobile` | `NVARCHAR(50)` nullable |  |
| `ShortName` | `NVARCHAR(50)` nullable |  |
| `OTPStatus` | `INT` DEFAULT 0 nullable |  |
| `PartnerValue` | `INT` DEFAULT 1 nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdminUser` | `AdminUserId` | PRIMARY KEY |
