# Table: `BookingUserFull`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `UserID` | `INT` PK |  |
| `TenVietTat` | `NVARCHAR(50)` nullable |  |
| `NhanSuSoYeuLyLichREF` | `INT` nullable | Lay id cua bang hdcn_nv_soyeulylich o db: hdcn |
| `TenDangNhap` | `NVARCHAR(50)` nullable | lay username o bang ox_users o db: reportingdb |
| `IsAdmin` | `INT` nullable | =0 sales;
=1 admin |
| `Email` | `NVARCHAR(50)` nullable |  |
| `LastLoginTime` | `DATETIME` nullable |  |
| `GhiChu` | `NVARCHAR(200)` nullable |  |
| `IsDeleted` | `BIT` nullable |  |
| `GroupUserID` | `INT` nullable |  |
| `OxUserREF` | `INT` nullable |  |
| `TypeTool` | `INT` nullable | 1=hd.admicro.vn
2=hdcn.admicro.vn(TMDT) |
| `UserIdHDCNTypeTool` | `INT` nullable |  |
| `TypeLook` | `INT` nullable | =0 mac dinh
=1 system lock |
| `Mobile` | `NVARCHAR(50)` nullable |  |
| `GroupsID` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_BookingUserFull` | `UserID` | PRIMARY KEY |
