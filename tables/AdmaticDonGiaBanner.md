# Table: `AdmaticDonGiaBanner`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdmaticDonGiaBannerID` | `INT` NN IDENTITY |  |
| `AdmaticBannerID` | `INT` nullable | Banner core cua Admatic |
| `AdmaticProductID` | `INT` nullable | TYPEPRODUCT
-- 1: Adx Mobile
-- 2: Admicro AdExchange Adx
-- 3: adx Ecom
-- 4: Adx CTA
-- 5: Admarket CPC
-- 6: CPM kingsize
-- 7: CPM Stick
-- 8: TVC Online
-- 9: Balloon
--10: BrandPage
--11: Mobile |
| `DmBannerID` | `INT` nullable | Banner cua san pham core |
| `DonGiaBanner_VAT` | `FLOAT` nullable | Don gia banner da bao gom VAT |
| `LoaiDonGiaTheoDVT` | `INT` nullable | Loai don gia theo don vi tinh:
--1: CPC
--2: CPM
--3: CPM |
| `BannerDateCreate` | `DATETIME` nullable |  |
| `CreatedAt` | `DATETIME` nullable |  |
| `CreatedBy` | `NVARCHAR(50)` nullable |  |
| `LastModifiedAt` | `DATETIME` DEFAULT getdate nullable |  |
| `LastModifiedBy` | `NVARCHAR(50)` nullable |  |
| `RecordStatus` | `INT` nullable |  |
| `DeletedStatus` | `INT` nullable |  |
| `bannerid` | `NVARCHAR(500)` nullable |  |
| `core_bannerid` | `NVARCHAR(500)` nullable |  |
| `product_id` | `NVARCHAR(500)` nullable |  |
| `price` | `NVARCHAR(500)` nullable |  |
| `bid_type` | `NVARCHAR(500)` nullable |  |
| `NgayThucHien` | `DATETIME` nullable |  |
