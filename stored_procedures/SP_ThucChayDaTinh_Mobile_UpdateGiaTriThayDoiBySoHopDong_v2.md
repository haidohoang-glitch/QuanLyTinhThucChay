# Stored Procedure: `ThucChayDaTinh_Mobile_UpdateGiaTriThayDoiBySoHopDong_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-02-16 17:04:21.893000
- **Ngày sửa cuối**: 2016-02-16 17:25:51.330000

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
--EXEC [ThucChayDaTinh_Mobile_UpdateGiaTriThayDoiBySoHopDong_v2]  '2016-01-29', '2016-01-29','QC3181115'
CREATE PROCEDURE [dbo].[ThucChayDaTinh_Mobile_UpdateGiaTriThayDoiBySoHopDong_v2]
	-- Add the parameters for the stored procedure here
	 @StartDate DATETIME,
	 @EndDate DATETIME,
	 @SoHopDong NVARCHAR(50)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME,
			@HopDongID INT, @HopDongChiTietID INT, 
			@count_HDCT INT, @BannerType INT, @ProductUnitName NVARCHAR(50)
			
				
	set @NgayThucHien = @StartDate
	WHILE(Convert(date,@NgayThucHien) <= Convert(date,@EndDate))
	BEGIN
		DECLARE Record_Cursor CURSOR FOR 																				
										SELECT distinct hd.SoHopDong, HopDongID, HopDongChiTietID, tc.BannerType--, tc.ProductUnitName
										FROM ThucChay_MobileTemp tc 
											inner join HopDongChiTiet hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
											INNER JOIN HopDong hd ON hd.SoHopDong = tc.SoHopDong 																					
										WHERE hdct.DmSanPhamREF = 342	
--										AND hdct.DonViTinh IN ('CPC','CPM')
AND hd.SoHopDong = @SoHopDong
										AND tc.NgayThucHien =  @NgayThucHien
										AND hdct.HopDongChiTietID IN (SELECT HopDongChiTietREF
										                                FROM HopDongChiTietLog where CONVERT(Date,thoigianlog) = @NgayThucHien)
										ORDER BY HopDongChiTietID									
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @HopDongID, @HopDongChiTietID, @BannerType--, @ProductUnitName
		WHILE @@FETCH_STATUS = 0
			BEGIN									
			UPDATE ThucChayDaTinhMobile SET GiaTriThayDoi = 0
				WHERE Convert(date,NgayThucHien) = @NgayThucHien
					AND HopDongID = @HopDongID
					AND SoHopDong = @SoHopDong
					AND HopDongChiTietREF = @HopDongChiTietID			
					AND DmSanPhamREF = 342
					
			SET @count_HDCT =
				(
					SELECT COUNT(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct
					WHERE hdct.HopDongChiTietID = @HopDongChiTietID	
					AND hdct.DeletedStatus = 0
				)		
			
			IF @count_HDCT > 0
				BEGIN		
					
					EXEC ThucChay_CheckHopDongCoThayDoi_Mobile @HopDongID,@SoHopDong,342,@HopDongChiTietID,@NgayThucHien, @BannerType--,@ProductUnitName
				END
			ELSE
			BEGIN
					
					EXEC ThucChay_CheckHopDongXoaPhanBo_Mobile	@HopDongID,@SoHopDong,342,@HopDongChiTietID,@NgayThucHien, @BannerType--, @ProductUnitName		
				
				END
				FETCH NEXT FROM Record_Cursor INTO @SoHopDong, @HopDongID, @HopDongChiTietID, @BannerType--,@ProductUnitName
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
		
		    -- Insert statements for procedure here
	--Insert tu bang thucchaydatinh from thucchaydatinhmobile 
	
	END
	
	
END

```
