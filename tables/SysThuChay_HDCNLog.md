# Table: `SysThuChay_HDCNLog`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `SysThuChay_HDCNLogID` | `INT` PK IDENTITY |  |
| `MaHanhDong` | `INT` nullable |  |
| `IsHanhDong` | `INT` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `ThoiGianChotSoLieu` | `DATETIME` nullable |  |
| `NguoiThucHien` | `NVARCHAR(50)` nullable |  |
| `IsDongBo` | `INT` nullable |  |
| `ThoiGianHoanThanhDongBo` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_SysThuChay_HDCNLog` | `SysThuChay_HDCNLogID` | PRIMARY KEY |
