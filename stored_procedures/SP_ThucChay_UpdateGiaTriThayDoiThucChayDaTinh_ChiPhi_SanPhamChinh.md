# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 16:14:28.527000
- **Ngày sửa cuối**: 2020-04-22 15:52:51.303000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh] '2014-08-05','2014-08-05'
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_ChiPhi_SanPhamChinh]
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
	    
		SELECT DISTINCT hd.HopDongID, hd.SoHopDong,hdct.HopDongChiTietID, hdct.SoLuong, hdct.ThanhTien FROM HopDongThayDoi hdtd
			INNER JOIN HopDong hd ON hdtd.HopDongFK = hd.HopDongID
			INNER JOIN HopDongChiTiet hdct ON hdct.HopDongFK = hdtd.HopDongFK
			WHERE convert(date,hdtd.NgayThayDoi) = @NgayThucHien
			AND hdct.DmSanPhamREF IN (140,228,549,564,375,231,238,337,531,370,339,342,381,735)
			AND hdct.DmLoaiBannerREF = 17 --Chi phi san pham chinh
			AND hd.TrangThaiHopDong <> 3
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
					AND DmSanPhamREF IN (140,228,549,564,375,231,238,337,531,370,339,342,381,735)
					AND DmLoaiBannerREF = 17 --Chi phi san pham chinh
				--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
				
				EXEC [ThucChay_CheckHopDongCoThayDoi_ChiPhi_SanPhamChinh] @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien
			FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		EXEC [ThucChay_CheckThucTreoThayDoi_ChiPhiKhac]	@NgayThucHien, '2013-01-01' 
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
	SELECT 2
END

	

--endregion

```
