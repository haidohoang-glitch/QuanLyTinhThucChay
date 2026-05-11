# Table: `ThucChay_Native_Ads_FixBug`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChay_Native_Ads_FixBugID` | `INT` PK IDENTITY |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `SoHopDong_old` | `NVARCHAR(50)` nullable |  |
| `TypeProduct` | `INT` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(200)` nullable |  |
| `TenNhanHang` | `NVARCHAR(300)` nullable |  |
| `DmNhanHangREF` | `INT` nullable |  |
| `DmBannerID` | `INT` nullable |  |
| `DmWebsiteID` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(500)` nullable |  |
| `DmViTriBannerSanPhamID` | `INT` nullable |  |
| `TenViTriBannerSanPham` | `NVARCHAR(500)` nullable |  |
| `SoLuongThucChay` | `BIGINT` nullable |  |
| `SoLuongThucChayKM` | `BIGINT` nullable |  |
| `DonViTinh` | `NVARCHAR(50)` nullable |  |
| `ThanhTienThucChaySauCK` | `FLOAT` nullable |  |
| `ThanhTienThucChayKM` | `FLOAT` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `DeletedStatus` | `SMALLINT` nullable |  |
| `LyDoLoi` | `NVARCHAR(1000)` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `PK_ThucChay_Native_Ads_FixBug` | `ThucChay_Native_Ads_FixBugID` | PRIMARY KEY |
