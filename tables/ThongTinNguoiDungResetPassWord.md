# Table: `ThongTinNguoiDungResetPassWord`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThongTinNguoiDungResetPassWordID` | `INT` PK |  |
| `NhanSuSoYeuLyLichREF` | `BIGINT` nullable |  |
| `TenNhanSu` | `NVARCHAR(200)` nullable |  |
| `UserName` | `NVARCHAR(200)` nullable |  |
| `PassWords` | `NVARCHAR(200)` nullable |  |
| `ActiveYN` | `INT` nullable |  |
| `IsCoHieuLucYN` | `INT` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `CreatedBy` | `NVARCHAR(200)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(200)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `PrintStatus` | `INT` nullable |  |
| `RecordStatus` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThongTinNguoiDungResetPassWord` | `ThongTinNguoiDungResetPassWordID` | PRIMARY KEY |
