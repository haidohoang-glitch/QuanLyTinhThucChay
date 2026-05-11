# Stored Procedure: `usp_UpdateThucChayAdmarketHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 16:43:43.170000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.997000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayAdmarketHopDongID` | `int(4)` | No |
| `@Contract` | `nvarchar(100)` | No |
| `@Click` | `int(4)` | No |
| `@View` | `int(4)` | No |
| `@Money` | `float(8)` | No |
| `@BannerId` | `int(4)` | No |
| `@BannerCampaignId` | `int(4)` | No |
| `@BannerCampaignName` | `nvarchar(100)` | No |
| `@BannerUsername` | `nvarchar(100)` | No |
| `@BannerClick` | `int(4)` | No |
| `@BannerView` | `int(4)` | No |
| `@BannerMoney` | `float(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_UpdateThucChayAdmarketHopDong]
(
    @ThucChayAdmarketHopDongID  INT,
    @Contract                   NVARCHAR(50),
    @Click                      INT,
    @View                       INT,
    @Money                      FLOAT,
    @BannerId                   INT,
    @BannerCampaignId           INT,
    @BannerCampaignName         NVARCHAR(50),
    @BannerUsername             NVARCHAR(50),
    @BannerClick                INT,
    @BannerView                 INT,
    @BannerMoney                FLOAT,
    @DmSanPhamREF               INT,
    @TenSanPham                 NVARCHAR(50),
    @NgayThucHien               DATETIME
)
AS
BEGIN
	SET NOCOUNT ON
	
	UPDATE [dbo].[ThucChayAdmarketHopDong]
	SET    [Contract]                   = @Contract,
	       [Click]                      = @Click,
	       [View]                       = @View,
	       [Money]                      = @Money,
	       [BannerId]                   = @BannerId,
	       [BannerCampaignId]           = @BannerCampaignId,
	       [BannerCampaignName]         = @BannerCampaignName,
	       [BannerUsername]             = @BannerUsername,
	       [BannerClick]                = @BannerClick,
	       [BannerView]                 = @BannerView,
	       [BannerMoney]                = @BannerMoney,
	       [DmSanPhamREF]               = @DmSanPhamREF,
	       [TenSanPham]                 = @TenSanPham,
	       [NgayThucHien]               = @NgayThucHien
	WHERE  [ThucChayAdmarketHopDongID]  = @ThucChayAdmarketHopDongID
END

```
