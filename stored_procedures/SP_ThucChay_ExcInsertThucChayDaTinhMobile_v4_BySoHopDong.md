# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhMobile_v4_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-21 11:19:21.267000
- **Ngày sửa cuối**: 2017-03-22 16:45:12.143000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--SELECT DISTINCT NgayThucHien FROM thucchay WHERE SoHopDong LIKE '%QC650115%' AND TypeProduct = 10
--exec [ThucChay_ExcInsertThucChayDaTinhMobile_v4_BySoHopDong] '2017-03-10','2017-03-11','QC1710217'
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhMobile_v4_BySoHopDong]--tinh ca truong hop 1 phan bo nhieu banner
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@SoHopDong NVARCHAR(50)
	
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @HopDongChiTietREF INT
	
	SET @NgayThucHien = @StartDate
	while(@NgayThucHien <= @EndDate)
	BEGIN
		
		--Xoa data truoc khi thuc hien
		DELETE FROM ThucChayDaTinhMobile 
		WHERE DmSanPhamREF = 342 AND NgayThucHien = @NgayThucHien AND SoHopDong = @SoHopDong
		AND NOT (DmHinhThucQuangCao = 13 or DmLoaiBannerREF IN (17,18))
		
		--Insert vao bang temp --danh cho truong hop phanbo
		EXEC ThucChay_InsertToTemp_Mobile_BySoHopDong @NgayThucHien, @SoHopDong
		
		--Insert vao bang HopDongChiTietAndBanner
		EXEC [ThucChay_HopDongChiTietAndBannerByDmSanPhamREF] 342, @NgayThucHien
				
		--Duyet tung phan bo
		DECLARE vendor_cursor CURSOR FOR 
			SELECT distinct A.SoHopDong, A.HopDongChiTietREF			
			FROM ThucChay_MobileTemp A 
			WHERE 1=1 
			and A.NgayThucHien = @NgayThucHien
			AND A.SoHopDong = @SoHopDong
			AND A.HopDongChiTietREF NOT IN (0,1) AND A.HopDongChiTietREF IS NOT NULL
			ORDER BY A.HopDongChiTietREF			

		OPEN vendor_cursor
		
		FETCH NEXT FROM vendor_cursor INTO @SoHopDong,@HopDongChiTietREF

		WHILE @@FETCH_STATUS = 0
		BEGIN
			SELECT @SoHopDong,@HopDongChiTietREF
			--Tinh thuc chay rieng cho phan bo
		    IF dbo.ThucChay_IsHopDongChiTietSingle(@HopDongChiTietREF) = 1				
				EXEC ThucChay_ExcInsertThucChayDaTinhMobileSingle @HopDongChiTietREF, @NgayThucHien
			--Tinh cho truong hop multi	
		    ELSE IF  (dbo.ThucChay_IsHopDongChiTietSingle(@HopDongChiTietREF) = 0 AND 
						(SELECT COUNT(ThucChayDaTinhID) FROM ThucChayDaTinhMobile  
						 WHERE HopDongChiTietREF = @HopDongChiTietREF 
						 AND NgayThucHien = @NgayThucHien) = 0)
				
			EXEC [ThucChay_ExcInsertThucChayDaTinhMobileBanner] @NgayThucHien, @SoHopDong, @HopDongChiTietREF
				
		    ELSE IF dbo.ThucChay_IsHopDongChiTietSingle(@HopDongChiTietREF) = -1
				BEGIN 	
					SELECT 'NOK'			
					--EXEC [UpdateHopDongChiTietREFInThucChayByBannerMobile]  @SoHopDong,@HopDongChiTietREF,@NgayThucHien
				end
			FETCH NEXT FROM vendor_cursor INTO @SoHopDong,@HopDongChiTietREF
		END 
		CLOSE vendor_cursor;
		DEALLOCATE vendor_cursor;

				
	set @NgayThucHien = dateadd(d,1,@NgayThucHien)

		
	end 
END

```
