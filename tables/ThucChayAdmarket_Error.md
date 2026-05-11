# Table: `ThucChayAdmarket_Error`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `id` | `BIGINT` PK IDENTITY |  |
| `user_id` | `NVARCHAR(100)` nullable |  |
| `user_name` | `NVARCHAR(100)` nullable |  |
| `contract_number` | `NVARCHAR(100)` nullable |  |
| `domain_name` | `NVARCHAR(100)` nullable |  |
| `domain_tt_click` | `INT` nullable |  |
| `domain_tt_view` | `INT` nullable |  |
| `domain_money` | `MONEY` nullable |  |
| `dm_sanpham_ref` | `NVARCHAR(50)` nullable |  |
| `ten_san_pham` | `NVARCHAR(500)` nullable |  |
| `dm_vitri_ref` | `NVARCHAR(50)` nullable |  |
| `ten_vi_tri` | `NVARCHAR(500)` nullable |  |
| `ngaythuchien` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChayDaTinh_Admarket_Error` | `id` | PRIMARY KEY |
