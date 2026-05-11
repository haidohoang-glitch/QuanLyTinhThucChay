# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhSponsorBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-01 15:51:04.247000
- **Ngày sửa cuối**: 2015-04-01 15:53:50.807000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-05-20
-- Description:	Insert ThucChayDaTinh doi voi san pham Mobile Ads
-- =============================================
--EXEC ThucChay_ExcInsertThucChayDaTinhMobile '2015-03-16','2015-03-16','QC960215'
-- EXEC ThucChay_ExcInsertThucChayDaTinhMobile '2014-04-13','2014-04-13','QC220414'
 
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhSponsorBanner]
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT
AS
BEGIN
	DECLARE @TenWebsite   NVARCHAR(50),
	        @DonViTinh    NVARCHAR(50),
	        @BannerType   INT,
	        @DonViTinhHD  NVARCHAR(50)
	
	SET @DonViTinhHD = (
	        SELECT TOP 1 hdct.DonViTinh
	        FROM   HopDongChiTiet hdct
	        WHERE  hdct.HopDongChiTietID = @HopDongChiTietID
	    )
	
	SET @DonViTinhHD = (
	        SELECT CASE 
	                    WHEN @DonViTinhHD = 'CPM' THEN 'VIEW'
	                    WHEN @DonViTinhHD = 'CPC' THEN 'CLICK'
	                    ELSE @DonViTinhHD
	               END
	    ) 
	
	-- Insert data to ThucChayMobileTemp
	EXEC ThucChaySponsor_InsertToTemp @NgayThucHien,
	     @NgayThucHien,
	     @SoHopDong
	
	-- Delete du lieu truoc khi tinh neu da ton tai
	DELETE 
	FROM   ThucChayDaTinhSponsorBanner
	WHERE  DmSanPhamREF = 381
	       AND NgayThucHien = @NgayThucHien
	       AND SoHopDong = @SoHopDong
	       AND HopDongChiTietREF IN (SELECT HopDongChiTietID
	                                 FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	
	
	DECLARE Record_Cursor CURSOR  
	FOR
	    SELECT DISTINCT tcm.[Contract],
	           tcm.SiteName,
	           @DonViTinhHD UnitName,
	           tcm.BannerType
	    FROM   ThucChaySponsorTemp AS tcm
	    WHERE  tcm.dt = @NgayThucHien
	           AND tcm.[Contract] = @SoHopDong
	           AND tcm.HopDongChiTietRER IN (SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	    ORDER BY
	           tcm.SiteName,
	           tcm.BannerType
	
	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TenWebsite, @DonViTinh, @BannerType
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    EXEC ThucChayDaTinh_InsertThucChaySponsorContractByContractNo_Banner
	         @NgayThucHien,
	         @SoHopDong,
	         @TenWebsite,
	         @DonViTinh,
	         @BannerType,
	         @HopDongChiTietID
	          
	    
	    FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TenWebsite, @DonViTinh, 
	    @BannerType
	END
	
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	
	SELECT '1'
END


```
