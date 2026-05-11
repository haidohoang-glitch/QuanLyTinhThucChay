# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-15 11:50:34.060000
- **Ngày sửa cuối**: 2014-11-19 12:17:00.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHIen` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDByHopDongChiTiet '2014-04-20',24147,54504

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDByHopDongChiTiet] 
	-- Add the parameters for the stored procedure here
	@NgayThucHIen DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT
AS
BEGIN
	DECLARE	@HopDongREF INT, @HopDongChiTietID INT , @SoHopDong NVARCHAR(50)
	DECLARE @SoLuongDotChayHD INT, @ThanhTienHDCT FLOAT

	PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
	DECLARE Record_Cursor CURSOR FOR 
		--GET THONG TIN HOPDONGCHITIET
		SELECT hd.HopDongID, hd.SoHopDong, hdct.HopDongChiTietID, hdct.SoLuong, hdct.ThanhTien
		  FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.TrangThaiHopDong <> 3
		AND hd.HopDongID = @HopDongID
		AND hdct.HopDongChiTietID = @HopDongChiTietREF
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 1 --Đơn vị của hình thức CPD 
		ORDER BY hd.SoHopDong	
	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
		
	WHILE @@FETCH_STATUS = 0
		BEGIN
			--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
			--EXEC ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDong @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien ,@SoLuongDotChayHD ,@ThanhTienHDCT
			EXEC ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien ,@SoLuongDotChayHD ,@ThanhTienHDCT
		FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
		END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	SELECT 2
END

--EXEC ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPDByHopDongChiTiet '2014-04-20',24147,54504

```
