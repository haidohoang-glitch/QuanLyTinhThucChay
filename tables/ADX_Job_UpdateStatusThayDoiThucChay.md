# Table: `ADX_Job_UpdateStatusThayDoiThucChay`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `Status` | `INT` nullable | 1: Cần chạy Job, 2: Đã chạy, 3: Chạy lỗi |
| `FromDate` | `DATETIME2` nullable |  |
| `ToDate` | `DATETIME2` nullable |  |
| `IsDeleted` | `BIT` DEFAULT 0 nullable |  |
| `RequestKeyError` | `NVARCHAR(2000)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ADX_Job_UpdateStatusThayDoiThucChay` | `Id` | PRIMARY KEY |
