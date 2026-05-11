# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD_bk`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-15 10:48:41.167000
- **Ngày sửa cuối**: 2014-11-19 12:17:00.187000

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
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD_bk] 
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
	    
		SELECT tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF, tcdt.SoLuong, tcdt.ThanhTien
		  FROM ThucChayDaTinh tcdt
		WHERE Convert(date,tcdt.NgayThucHien) = @NgayThucHien
		AND tcdt.DmSanPhamREF IN (140,228,241)
		ORDER BY tcdt.SoHopDong	
		
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
					AND DmSanPhamREF IN (140,228,241)	
				--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
				EXEC ThucChay_CheckHopDongCoThayDoi_CPD @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien ,@SoLuongDotChayHD ,@ThanhTienHDCT
			FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID , @SoLuongDotChayHD, @ThanhTienHDCT
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPD] '2013-09-01', '2013-09-30'

```
