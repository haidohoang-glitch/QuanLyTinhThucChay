# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:24.287000
- **Ngày sửa cuối**: 2017-06-07 10:00:07.627000

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
CREATE  PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE	@HopDongREF INT,@SoHopDong NVARCHAR(50),@HopDongChiTietID INT
	DECLARE @SoLuongDotChayHD INT,@ThanhTienHDCT FLOAT, @DmWebsiteREF INT, @DmSanPhamREF INT
	DECLARE @NgayThucHien DATETIME, @count_HDCT INT, @SoLuongThucChayBF INT
	set @NgayThucHien = @StartDate

	WHILE(Convert(date,@NgayThucHien) <= Convert(date,@EndDate))
	BEGIN
		PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
		SET @count_HDCT = 0
		SET @SoLuongThucChayBF = 0
		DECLARE Record_Cursor CURSOR FOR 
	    
		SELECT distinct  hd.HopDongID, hd.SoHopDong,  hdcttd.DmSanPhamREF, hdcttd.HopDongChiTietREF
		FROM HopDong hd
		INNER JOIN HopDongThayDoi hdtd ON hd.HopDongID = hdtd.HopDongFK AND hd.TrangThaiHopDong <> 3
		INNER JOIN HopDongChiTietThayDoi hdcttd ON hdtd.HopDongFK = hdcttd.HopDongFK
		AND hdcttd.DmSanPhamREF IN (231,238,339,240,370,598,613,732,735)
		WHERE 1=1
		AND NOT (hdcttd.DmLoaiREF in (13,42) or DmLoaiBannerREF = 18)--Khong update gia tri thay doi cho HTQC Mua Ngoai 
		AND convert(date,hdtd.NgayThayDoi) = @NgayThucHien
		AND (([dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdcttd.DonViTinh)  = 3)OR(hdcttd.DonViTinh = 'CPV')) --Đơn vị của hình thức CPM
		AND [dbo].[ThucChay_CheckSanPhamBoxAppSelfServing](hdcttd.DmSanPhamREF, isnull(hdcttd.TenViTri,''))  = 0
		ORDER BY hd.SoHopDong	
		
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong,  @DmSanPhamREF, @HopDongChiTietID
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
				PRINT @SoHopDong
				UPDATE ThucChayDaTinh
				SET
					GiaTriThayDoi = 0
				WHERE Convert(date,NgayThucHien) = @NgayThucHien
					AND HopDongID = @HopDongREF 
					AND SoHopDong = @SoHopDong
					AND HopDongChiTietREF = @HopDongChiTietID
					AND DmSanPhamREF IN (231,238,339,240,370,598,613,732,735)
				
				SET @SoLuongThucChayBF =
				(
					SELECT SUM(ThucChayDaTinh.SoLuongThucChay) from ThucChayDaTinh
					WHERE Convert(date,NgayThucHien) < @NgayThucHien
					AND HopDongID = @HopDongREF 
					AND HopDongChiTietREF = @HopDongChiTietID
					AND DmSanPhamREF IN (231,238,339,240,370,598,613,732,735)
				)	
				SET @count_HDCT =
				(
					SELECT COUNT(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct
					WHERE hdct.HopDongChiTietID = @HopDongChiTietID	
					AND hdct.DeletedStatus = 0
				)	
				IF(@SoLuongThucChayBF >0)
				BEGIN
					IF(@count_HDCT >0)
					--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
						EXEC ThucChay_CheckHopDongCoThayDoi_CPM @HopDongREF ,@SoHopDong, @DmSanPhamREF ,@HopDongChiTietID, @NgayThucHien
					ELSE
						EXEC ThucChay_CheckHopDongXoaPhanBo_CPM @HopDongREF ,@SoHopDong, @DmSanPhamREF ,@HopDongChiTietID, @NgayThucHien	
				END
					
			FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @DmSanPhamREF, @HopDongChiTietID
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
	SELECT 2
END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] '2014-04-29', '2014-04-29'

```
