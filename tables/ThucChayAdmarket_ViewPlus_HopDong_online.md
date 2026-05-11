# Table: `ThucChayAdmarket_ViewPlus_HopDong_online`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `id` | `INT` PK IDENTITY |  |
| `user_id` | `NVARCHAR(100)` nullable |  |
| `username` | `NVARCHAR(100)` nullable |  |
| `isnoibo` | `NVARCHAR(100)` nullable |  |
| `contract_number` | `NVARCHAR(100)` nullable |  |
| `tt_click` | `NVARCHAR(100)` nullable |  |
| `tt_view` | `NVARCHAR(100)` nullable |  |
| `money` | `NVARCHAR(100)` nullable |  |
| `promotion` | `NVARCHAR(100)` nullable |  |
| `domain_name` | `NVARCHAR(1000)` nullable |  |
| `domain_tt_click` | `NVARCHAR(100)` nullable |  |
| `domain_tt_view` | `NVARCHAR(100)` nullable |  |
| `domain_money` | `NVARCHAR(100)` nullable |  |
| `domain_promotion` | `NVARCHAR(100)` nullable |  |
| `campaign_id` | `NVARCHAR(100)` nullable |  |
| `DmSanPhamREF` | `NVARCHAR(100)` nullable |  |
| `TenSanPham` | `NVARCHAR(100)` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `createdBy` | `NVARCHAR(100)` nullable |  |
| `createdAt` | `DATETIME` nullable |  |
| `contract_number_change` | `NVARCHAR(100)` nullable |  |
| `data_type` | `INT` nullable | =1 du lieu khong co hd, = 2 dl hd da do day van co dl tc tra ve, =3 hop dong chua day nhung dl tr vuot qua gia tri hd, =4 khi chạy thừa và muốn chuyên giá trị thừa sang hợp đồng khác,= 5 TH tra ve vuot khong dang ke confirm du lieu de = du lieu tra ve asd lam |
| `confirm_money` | `NVARCHAR(100)` nullable | th data_type = 2 can confirm so tien chay cua hd den dau (lech do pp tinh cu va moi) |
| `confirm_tt_click` | `INT` nullable |  |
| `confirm_tt_view` | `INT` nullable |  |
| `giatrihopdong` | `MONEY` nullable |  |
| `trangthai` | `INT` nullable | = 0 chưa xử lý, =1 đã xử lý |
| `confirm_date` | `DATETIME` nullable |  |
| `confirm_status` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayAdmarket_ViewPlus_HopDong_online` | `id` | PRIMARY KEY |
