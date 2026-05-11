# Table: `PR_Nhanhang_Chuanhoa`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ID` | `INT` PK IDENTITY |  |
| `sohopdong` | `NVARCHAR(256)` NN |  |
| `DmNhanhangID` | `INT` NN |  |
| `TenNhanhang` | `NVARCHAR(1024)` NN |  |
| `phanbosite_id` | `INT` NN |  |
| `website` | `NVARCHAR(256)` nullable |  |
| `chuyenmuc` | `NVARCHAR(256)` nullable |  |
| `giatien` | `DECIMAL(18,0)` nullable |  |
| `thoigianbd` | `DATETIME` nullable |  |
| `link` | `NVARCHAR(1024)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_PR_Nhanhang_Chuanhoa` | `ID` | PRIMARY KEY |
