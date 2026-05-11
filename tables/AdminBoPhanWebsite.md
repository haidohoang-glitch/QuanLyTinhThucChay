# Table: `AdminBoPhanWebsite`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `NhanSuSoYeuLyLichID` | `INT` nullable |  |
| `TenDangNhap` | `NVARCHAR(50)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(50)` nullable |  |
| `DmLoaiDoiTuongREF` | `INT` nullable |  |
| `AdminBoPhanWebsiteID` | `INT` PK IDENTITY |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_AdminBoPhanWebsite` | `AdminBoPhanWebsiteID` | PRIMARY KEY |
