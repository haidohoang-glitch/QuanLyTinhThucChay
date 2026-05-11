# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_SponsorPost`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-30 10:24:29.477000
- **Ngày sửa cuối**: 2015-04-10 11:14:10.553000

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
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_SponsorPost] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE	@HopDongREF INT,@SoHopDong NVARCHAR(50),@HopDongChiTietID INT
	DECLARE @SoLuongDotChayHD INT,@ThanhTienHDCT FLOAT
	DECLARE @NgayThucHien DATETIME
	set @NgayThucHien = @StartDate

	WHILE(Convert(date,@NgayThucHien) <= Convert(date,@EndDate))
	BEGIN
		PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
		DECLARE Record_Cursor CURSOR FOR 
	    
		SELECT a.HopDongID, a.SoHopDong, a.HopDongChiTietREF, a.SoLuong, a.ThanhTien FROM
		(
			SELECT tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF, tcdt.SoLuong, tcdt.ThanhTien
			  FROM ThucChayDaTinh tcdt
			WHERE Convert(date,tcdt.NgayThucHien) = @NgayThucHien
			AND tcdt.DmSanPhamREF IN (381)
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3 --Đơn vị của CPC, CLICK
		UNION

			SELECT DISTINCT hd.HopDongID, hd.SoHopDong,hdct.HopDongChiTietID, hdct.SoLuong, hdct.ThanhTien 
			FROM HopDongThayDoi hdtd
			INNER JOIN HopDong hd ON hdtd.HopDongFK = hd.HopDongID
			INNER JOIN HopDongChiTiet hdct ON hdct.HopDongFK = hdtd.HopDongFK
			WHERE convert(date,hdtd.NgayThayDoi) = @NgayThucHien
			AND hdct.DmSanPhamREF IN (381)
			AND hd.TrangThaiHopDong <> 3
			AND hdct.DeletedStatus <> 1
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh)  = 3 --Đơn vị của CPC, CLICK
		)A
		ORDER BY a.SoHopDong, a.HopDongChiTietREF
	
		
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
				UPDATE ThucChayDaTinh
				SET
					GiaTriThayDoi = 0
				WHERE Convert(date,NgayThucHien) = @NgayThucHien
					AND HopDongID = @HopDongREF 
					AND SoHopDong = @SoHopDong
					AND HopDongChiTietREF = @HopDongChiTietID
					AND DmSanPhamREF IN (381)
				--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK				
				--EXEC ThucChay_CheckHopDongCoThayDoi_SponsorPost @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien
				EXEC ThucChayDaTinh_SponsorPost_UpdateGiaTriThayDoi_ManualByHopDongChiTietID @NgayThucHien,@SoHopDong,@HopDongChiTietID,381
			FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor	
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
	SELECT 2
END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_SponsorPost] '2013-09-01', '2013-09-30'


```
