# Table: `OtpSetting`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `OtpSettingId` | `INT` PK IDENTITY |  |
| `NhanSuSoYeuLyLichID` | `INT` nullable |  |
| `FullName` | `NVARCHAR(200)` nullable |  |
| `Email` | `NVARCHAR(200)` nullable |  |
| `Mobile` | `NVARCHAR(50)` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_OtpManipulate` | `OtpSettingId` | PRIMARY KEY |
