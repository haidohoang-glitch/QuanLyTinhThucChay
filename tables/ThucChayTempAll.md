# Table: `ThucChayTempAll`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `ThucChayID` | `NVARCHAR(50)` PK |  |
| `SoHopDong` | `NVARCHAR(50)` nullable |  |
| `DanhsachDmBookingREF` | `NVARCHAR(100)` nullable |  |
| `DmSanPhamREF` | `INT` nullable |  |
| `TenSanPham` | `NVARCHAR(255)` nullable |  |
| `DmNhomWebsiteREF` | `INT` nullable |  |
| `TenNhomWebsite` | `NVARCHAR(50)` nullable |  |
| `DmWebsiteREF` | `INT` nullable |  |
| `TenWebsite` | `NVARCHAR(255)` nullable |  |
| `DmChienDichREF` | `INT` nullable |  |
| `TenChienDich` | `NVARCHAR(255)` nullable |  |
| `DmBannerREF` | `INT` nullable |  |
| `TenBanner` | `NVARCHAR(256)` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
| `TongViewThucChay` | `FLOAT` nullable |  |
| `TongClickThucChay` | `FLOAT` nullable |  |
| `CreatedBy` | `NVARCHAR(1)` NN |  |
| `CreatedAt` | `DATETIME` NN |  |
| `LastModifiedBy` | `NVARCHAR(1)` NN |  |
| `LastModifiedAt` | `DATETIME` NN |  |
| `DeletedStatus` | `INT` NN |  |
| `PrintStatus` | `INT` NN |  |
| `RecordStatus` | `INT` NN |  |
| `TongSoBaiViet` | `FLOAT` nullable |  |
| `HopDongChiTietREF` | `NVARCHAR(50)` nullable |  |
| `SoThuTuTheoNgay` | `INT` nullable |  |
| `TypeProduct` | `INT` nullable |  |

---

## Indexes

| Index | Columns | Loại |
|-------|---------|------|
| `csThucChayTempAll` | `ThucChayID` | PRIMARY KEY |
