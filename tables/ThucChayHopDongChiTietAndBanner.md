# Table: `ThucChayHopDongChiTietAndBanner`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayHopDongChiTietID` | `INT` nullable |  |
| `DmBannerID` | `NVARCHAR(50)` nullable |  |
| `HopDongChiTietREF` | `INT` nullable |  |
| `HopDongREF` | `INT` nullable |  |
| `BookingREF` | `INT` nullable |  |
| `ThoiGianBatDau` | `DATETIME` nullable |  |
| `ThoiGianKetThuc` | `DATETIME` nullable |  |
| `TiLeThucChayHDCTSoVoiBanner` | `FLOAT` nullable |  |
| `DaThucHienUpdateTiLe` | `TINYINT` DEFAULT 0 nullable | = 0 Chua thuc hien update ti le thuc chay cho HopDongChiTietID<br>= 1 Da Thuc hien update ti le thuc chay cho HopDongChiTietID |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `DsNhanHangREF` | `NVARCHAR(200)` nullable |  |
| `LogTime` | `DATETIME` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `Index_HopDong_Banner` | `HopDongREF` | BTREE |
| `ThucChayHDCTAndBanner` | `DmBannerID, HopDongChiTietREF, DaThucHienUpdateTiLe` | BTREE |
