# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhMobileBanner_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-20 12:21:05.620000
- **Ngày sửa cuối**: 2017-05-20 12:21:27.527000

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
--EXEC [ThucChay_ExcInsertThucChayDaTinhMobileBanner] '2015-01-21','QC3291214',70731
-- EXEC ThucChay_ExcInsertThucChayDaTinhMobile '2014-04-13','2014-04-13','QC220414'
 
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhMobileBanner_test]
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT
AS
BEGIN
	DECLARE @TenWebsite   NVARCHAR(50),
	        @DonViTinh    NVARCHAR(50),
	        @BannerType   INT,
	        @DonViTinhHD  NVARCHAR(50), @HTQC NVARCHAR(50), @tc INT, @tv INT
	
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
	    	SET @HTQC = (
	        SELECT TOP 1 hdct.TenLoai
	        FROM   HopDongChiTiet hdct
	        WHERE  hdct.HopDongChiTietID = @HopDongChiTietID
	    )
		SET @HTQC = (
	        SELECT CASE 
	                    WHEN @HTQC = 'CPM' THEN 'VIEW'
	                    WHEN @HTQC = 'CPC' THEN 'CLICK'
	                    ELSE @HTQC
	               END
	    ) 
	-- Insert data to ThucChayMobileTemp
	EXEC ThucChayMobile_InsertToTemp @NgayThucHien,
	     @NgayThucHien,
	     @SoHopDong
	
	-- Delete du lieu truoc khi tinh neu da ton tai
	DELETE 
	FROM   ThucChayDaTinhMobile
	WHERE  DmSanPhamREF = 342
	       AND NgayThucHien = @NgayThucHien
	       AND SoHopDong = @SoHopDong
	       AND NOT (DmHinhThucQuangCao = 13 or DmLoaiBannerREF IN (17,18))
	       AND HopDongChiTietREF IN (SELECT HopDongChiTietID
	                                 FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	
	DECLARE Record_Cursor CURSOR  
	FOR
	    SELECT tcm.[Contract],
	           tcm.SiteName,
	           (case when @DonViTinhHD = 'VIEW' THEN 'VIEW'
	            WHEN @DonViTinhHD = 'CLICK' THEN 'CLICK'
	            ELSE  @HTQC
	           END)UnitName,
	           tcm.BannerType, SUM(TotalClick) tc, SUM(TotalView) tv
	    FROM   ThucChayMobileTemp AS tcm
	    WHERE  tcm.dt = @NgayThucHien
	           AND tcm.[Contract] = @SoHopDong
	           AND tcm.HopDongChiTietRER IN (SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	    GROUP BY tcm.[Contract],
	           tcm.SiteName,tcm.BannerType
	    ORDER BY
	           tcm.SiteName,
	           tcm.BannerType
	
	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TenWebsite, @DonViTinh, @BannerType, @tc, @tv
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    --EXEC ThucChayDaTinh_InsertThucChayMobileContractByContractNo_Banner
	   SELECT
	         @NgayThucHien,
	         @SoHopDong,
	         @TenWebsite,
	         @DonViTinh,
	         @BannerType,
	         @HopDongChiTietID
	          
	    
	    FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TenWebsite, @DonViTinh, 
	    @BannerType, @tc, @tv
	END
	
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	
	SELECT '1'
END
--ThucChayDaTinh_InsertThucChayMobileContractByContractNo_Banner '2015-01-21','QC3291214','afamily.vn','CLICK',4,70731
```
