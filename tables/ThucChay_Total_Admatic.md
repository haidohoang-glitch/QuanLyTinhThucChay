# Table: `ThucChay_Total_Admatic`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `id` | `INT` PK IDENTITY |  |
| `tt_click` | `NVARCHAR(500)` nullable |  |
| `tt_view` | `NVARCHAR(500)` nullable |  |
| `money` | `NVARCHAR(500)` nullable |  |
| `contract_number` | `NVARCHAR(500)` nullable |  |
| `domain_tt_click` | `NVARCHAR(500)` nullable |  |
| `domain_tt_view` | `NVARCHAR(500)` nullable |  |
| `domain_tt_money` | `NVARCHAR(500)` nullable |  |
| `domain_tt_promotion` | `NVARCHAR(500)` nullable |  |
| `DmSanPhamREF` | `NVARCHAR(500)` nullable |  |
| `TenSanPham` | `NVARCHAR(500)` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `createdBy` | `NVARCHAR(500)` nullable |  |
| `createdAt` | `DATETIME` nullable |  |
| `promotion` | `NVARCHAR(500)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChay_Total_Admatic` | `id` | PRIMARY KEY |
