# Table: `AdmaticDonGiaBanner`

---

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `AdmaticDonGiaBannerID` | `INT` NN IDENTITY |  |
| `AdmaticBannerID` | `INT` nullable | Banner core cua Admatic |
| `AdmaticProductID` | `INT` nullable | TYPEPRODUCT<br>-- 1: Adx Mobile<br>-- 2: Admicro AdExchange Adx<br>-- 3: adx Ecom<br>-- 4: Adx CTA<br>-- 5: Admarket CPC<br>-- 6: CPM kingsize<br>-- 7: CPM Stick<br>-- 8: TVC Online<br>-- 9: Balloon<br>--10: BrandPage<br>--11: Mobile |
| `DmBannerID` | `INT` nullable | Banner cua san pham core |
| `DonGiaBanner_VAT` | `FLOAT` nullable | Don gia banner da bao gom VAT |
| `LoaiDonGiaTheoDVT` | `INT` nullable | Loai don gia theo don vi tinh:<br>--1: CPC<br>--2: CPM<br>--3: CPM |
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
