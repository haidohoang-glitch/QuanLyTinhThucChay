# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhMobile_v4`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-20 15:32:55.717000
- **Ngày sửa cuối**: 2016-12-16 09:35:47.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--ThucChay_ExcInsertThucChayDaTinhMobile_v4_BySoHopDong '2015-07-15','2015-07-15','QC180615'
--exec ThucChay_ExcInsertThucChayDaTinhMobile_v4 '2015-03-24','2015-03-24'
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhMobile_v4]--tinh ca truong hop 1 phan bo nhieu banner
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
	
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @SoHopDong NVARCHAR(50), @HopDongChiTietREF INT
	
	SET @NgayThucHien = @StartDate
	while(@NgayThucHien <= @EndDate)
	BEGIN
		
		--Xoa data truoc khi thuc hien
		DELETE FROM ThucChayDaTinhMobile WHERE DmSanPhamREF = 342 
		AND NgayThucHien = @NgayThucHien
		AND not (DmHinhThucQuangCao in (13,42) or DmLoaiBannerREF  in (17,18))
		--Insert vao bang temp --danh cho truong hop phanbo
		EXEC ThucChay_InsertToTemp_Mobile @NgayThucHien
		
		--Insert vao bang HopDongChiTietAndBanner
		EXEC ThucChay_HopDongChiTietAndBannerByDmSanPhamREF 342,@StartDate
				
		--Duyet tung phan bo
		DECLARE vendor_cursor CURSOR FOR 
			SELECT distinct A.SoHopDong, A.HopDongChiTietREF			
			FROM ThucChay_MobileTemp A 
			WHERE 1=1 
			and A.NgayThucHien = @NgayThucHien
			AND A.HopDongChiTietREF NOT IN (0,1) AND A.HopDongChiTietREF IS NOT NULL
			AND HopDongChiTietREF NOT IN (SELECT HopDongChiTietID 
										FROM dbo.HopDongChiTiet 
										WHERE DmSanPhamREF = 342 AND (DmLoaiBannerREF = 17 OR DmLoaiNenTangREF = 8)
															 AND DeletedStatus <> 1)
			ORDER BY A.HopDongChiTietREF

		OPEN vendor_cursor
		
		FETCH NEXT FROM vendor_cursor INTO @SoHopDong,@HopDongChiTietREF

		WHILE @@FETCH_STATUS = 0
		BEGIN
			--PRINT 'HopDongChiTietID:' +CONVERT(NVARCHAR(50),@HopDongChiTietREF) + ' & SoHopDong: ' + convert(nvarchar(50),+@SoHopDong) 
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
				SELECT 'NOK'
			FETCH NEXT FROM vendor_cursor INTO @SoHopDong,@HopDongChiTietREF
		END 
		CLOSE vendor_cursor;
		DEALLOCATE vendor_cursor;

		
		--Tinh truong hop khong so hop dong
		EXEC [ThucChay_InsertThucChayDaTinh_MobileNoContract] @NgayThucHien 
		
		-- Update Gia tri thay doi thuc chay Mobile
		EXEC dbo.ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi_v2 @NgayThucHien, @NgayThucHien			
		
		
		------************
		--XU LY HD HUY
		EXEC [ThucChay_UpdateGiaTriThayDoi_HDHuy] @NgayThucHien, @NgayThucHien				
		
		
		--Insert du lieu tu ThucChayDaTinhMobile -> ThucChayDaTinh 
		EXEC ThucChay_InsertIntoTCDTFromTCDTMobile @NgayThucHien
		------************
	set @NgayThucHien = dateadd(d,1,@NgayThucHien)

		
	end 
END

```
