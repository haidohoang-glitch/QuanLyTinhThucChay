# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-21 11:43:01.210000
- **Ngày sửa cuối**: 2015-03-17 18:42:34.040000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@Shd` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-05-20
-- Description:	Insert ThucChayDaTinh doi voi san pham Mobile Ads
-- =============================================
 --EXEC ThucChay_ExcInsertThucChayDaTinhMobile '2015-03-16','2015-03-16','QC960215'
-- EXEC ThucChay_ExcInsertThucChayDaTinhMobile '2014-04-13','2014-04-13','QC220414'
 
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhMobile] 
	@StartDate datetime,
	@EndDate DATETIME,
	@Shd NVARCHAR(50)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong		NVARCHAR(50),  
			@TenWebsite		NVARCHAR(50), 
			@DonViTinh		NVARCHAR(50),
			@BannerType		INT,
			@HopDongChiTietREF INT,
			@DonViTinhHD NVARCHAR(50)
			 	
	set @NgayThucHien = @StartDate
	
	while(@NgayThucHien <= @EndDate)
	BEGIN	
		SELECT @NgayThucHien	
		-- Insert data to ThucChayMobileTemp
		--EXEC ThucChayMobile_InsertToTemp @NgayThucHien, @NgayThucHien,@Shd
		
		-- Delete du lieu truoc khi tinh neu da ton tai
		DELETE FROM ThucChayDaTinhMobileBanner  WHERE DmSanPhamREF = 342 AND 
		NgayThucHien  =@NgayThucHien
		AND SoHopDong = @Shd
		
		-- Thuc chay khong hop dong
		--EXEC dbo.ThucChayDaTinh_InsertThucChayMobileNoContract @NgayThucHien
		
		 -- Thuc chay co so hop dong
		DECLARE Record_Cursor CURSOR FOR 
		
		SELECT distinct tcm.[Contract],tcm.SiteName,'VIEW' UnitName,-- tcm.UnitName, 
		tcm.BannerType
		FROM ThucChayMobileTemp AS tcm
		WHERE tcm.dt = @NgayThucHien 
		AND tcm.[Contract] = @Shd
		--AND tcm.HopDongChiTietRER IN (73488,73489)

		ORDER BY tcm.SiteName, tcm.BannerType
		OPEN Record_Cursor
		 -- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TenWebsite, @DonViTinh, @BannerType
			
		WHILE @@FETCH_STATUS = 0
			BEGIN		
										
				EXEC ThucChayDaTinh_InsertThucChayMobileContractByContractNo_v3 
					@NgayThucHien, 
					@SoHopDong, 
					@TenWebsite, 
					@DonViTinh,
					@BannerType
					
				--EXEC dbo.ThucChayDaTinh_UpdateSoLuongLechTreoHa
				--	@NgayThucHien,
				--	@SoHopDong,
				--	342	
				
				FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @TenWebsite, @DonViTinh, @BannerType
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
						
		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)	
		SELECT @NgayThucHien
	end 
	
	SELECT '1'
	--SELECT * FROM @Table
END


```
