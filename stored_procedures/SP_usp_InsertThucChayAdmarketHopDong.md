# Stored Procedure: `usp_InsertThucChayAdmarketHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 16:43:43.127000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
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
CREATE PROCEDURE [dbo].[usp_InsertThucChayAdmarketHopDong]
(
    @Contract            NVARCHAR(50),
    @Click               INT,
    @View                INT,
    @Money               FLOAT,
    @BannerId            INT,
    @BannerCampaignId    INT,
    @BannerCampaignName  NVARCHAR(50),
    @BannerUsername      NVARCHAR(50),
    @BannerClick         INT,
    @BannerView          INT,
    @BannerMoney         FLOAT,
    @DmSanPhamREF        INT,
    @TenSanPham          NVARCHAR(50),
    @NgayThucHien        DATETIME
)
AS
BEGIN
	SET NOCOUNT ON
	DECLARE @ThucChayAdmarketHopDongID INT
	SET @ThucChayAdmarketHopDongID = 0
	
	SELECT @ThucChayAdmarketHopDongID = [ThucChayAdmarketHopDongID]
	FROM   [dbo].[ThucChayAdmarketHopDong]
	WHERE  ([NgayThucHien] = @NgayThucHien)
	       AND ([BannerId] = @BannerId)
	       AND ([Contract] = @Contract)
	       AND ([DmSanPhamREF] = @DmSanPhamREF)	 
	
	IF (@ThucChayAdmarketHopDongID = 0)
	BEGIN
	    INSERT INTO [dbo].[ThucChayAdmarketHopDong]
	      (
	        [Contract],
	        [Click],
	        [View],
	        [Money],
	        [BannerId],
	        [BannerCampaignId],
	        [BannerCampaignName],
	        [BannerUsername],
	        [BannerClick],
	        [BannerView],
	        [BannerMoney],
	        [DmSanPhamREF],
	        [TenSanPham],
	        [NgayThucHien]
	      )
	    VALUES
	      (
	        @Contract,
	        @Click,
	        @View,
	        @Money,
	        @BannerId,
	        @BannerCampaignId,
	        @BannerCampaignName,
	        @BannerUsername,
	        @BannerClick,
	        @BannerView,
	        @BannerMoney,
	        @DmSanPhamREF,
	        @TenSanPham,
	        @NgayThucHien
	      )
	END
	ELSE
	BEGIN
	    EXEC [usp_UpdateThucChayAdmarketHopDong] @ThucChayAdmarketHopDongID,
	         @Contract,
	         @Click,
	         @View,
	         @Money,
	         @BannerId,
	         @BannerCampaignId,
	         @BannerCampaignName,
	         @BannerUsername,
	         @BannerClick,
	         @BannerView,
	         @BannerMoney,
	         @DmSanPhamREF,
	         @TenSanPham,
	         @NgayThucHien
	END
END

```
