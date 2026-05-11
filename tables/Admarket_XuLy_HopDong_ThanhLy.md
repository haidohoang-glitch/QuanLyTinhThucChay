# Table: `Admarket_XuLy_HopDong_ThanhLy`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `id` | `INT` PK IDENTITY |  |
| `hopdongid` | `INT` nullable |  |
| `sohopdong` | `NVARCHAR(50)` nullable |  |
| `phanboid` | `INT` nullable |  |
| `user_id` | `INT` nullable |  |
| `user_name` | `NVARCHAR(50)` nullable |  |
| `dmsanphamid` | `INT` nullable |  |
| `tensanpham` | `NVARCHAR(500)` nullable |  |
| `giatritinhthucchay` | `MONEY` nullable |  |
| `giatrithucchaymongmuon` | `MONEY` nullable |  |
| `giatrichenhlech` | `MONEY` nullable |  |
| `ngaythuchien` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_Admarket_XuLy_HopDong_ThanhLy` | `id` | PRIMARY KEY |
