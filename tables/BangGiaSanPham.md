# Table: `BangGiaSanPham`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `BangGiaSanPhamID` | `INT` PK IDENTITY |  |
| `DmHinhThucQuangCao` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(50)` nullable |  |
| `DmDonViTinhREF` | `INT` nullable | 1: CPC; 2: CPM |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `TenBanner` | `NVARCHAR(50)` nullable |  |
| `DonGia` | `INT` nullable |  |
| `NgayHieuLuc` | `DATETIME` nullable |  |
| `NgayHetHieuLuc` | `DATETIME` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_BangGiaSanPham` | `BangGiaSanPhamID` | PRIMARY KEY |
