# Table: `Admarket_XuLy_HopDong_LienQuan_ThanhLy`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `Id` | `INT` PK IDENTITY |  |
| `hopdongid` | `INT` nullable |  |
| `sohopdong` | `NVARCHAR(50)` nullable |  |
| `phanboid` | `INT` nullable |  |
| `user_id` | `INT` nullable |  |
| `user_name` | `NVARCHAR(50)` nullable |  |
| `dmsanphamref` | `INT` nullable |  |
| `tensanpham` | `NVARCHAR(500)` nullable |  |
| `giatrithucchay` | `MONEY` nullable |  |
| `giatrithucchaysau` | `MONEY` nullable |  |
| `chenhlech` | `MONEY` nullable |  |
| `hopdongid_thanhly` | `INT` nullable |  |
| `ngaythuchien` | `DATETIME` nullable |  |
| `tonggiatrithucchay` | `MONEY` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_Admarket_XuLy_HopDong_LienQuan_ThanhLy` | `Id` | PRIMARY KEY |
