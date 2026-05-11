# Stored Procedure: `ThucChay_UpdateThucChayPRID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-21 12:01:02.957000
- **Ngày sửa cuối**: 2014-11-19 12:24:48.523000

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
CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayPRID] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE	@HopDongChiTietID INT, @DmSanPHamREF INT, @Soluongthucchay INT, @thucchayPRID INT
	DECLARE @NgayThucHien DATETIME, @dmThucChayPRID NVARCHAR(50)
	set @NgayThucHien = @StartDate
	

	WHILE(Convert(date,@NgayThucHien) <= Convert(date,@EndDate))
	BEGIN
		PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
		DECLARE Record_Cursor CURSOR FOR 

		SELECT a.HopDongChiTietREF,a.DmSanPhamREF, a.NgayThucHien,a.SoLuongThucChay, tchdctp.ThucChayHopDongChiTietPRID
		  FROM 
		(
			SELECT tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF, tcdt.NgayThucHien, tcdt.SoLuongThucChay 
			,tcdt.DotChayBooking 
			FROM ThucChayDaTinh tcdt
			WHERE tcdt.DmSanPhamREF IN (141,245,250)
			AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
		)a
		INNER JOIN ThucChayHopDongChiTietPR tchdctp
		ON a.HopDongChiTietREF = tchdctp.HopDongChiTietREF
		AND convert(date,a.NgayThucHien) = CONVERT(date, tchdctp.ThoiGianBatDau)
		WHERE  tchdctp.DeletedStatus = 0
		ORDER BY a.HopDongChiTietREF, a.NgayThucHien
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor INTO @HopDongChiTietID , @DmSanPHamREF, @NgayThucHien, @Soluongthucchay, @thucchayPRID
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				SET @dmThucChayPRID =
				(
					SELECT distinct tcdt.DotChayBooking FROM ThucChayDaTinh tcdt
					WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
					AND CONVERT(date,tcdt.NgayThucHien) = @NgayThucHien
					AND tcdt.DmSanPhamREF IN (141,245,250)
				)
				
				IF(@dmThucChayPRID <> '')
					SET @dmThucChayPRID = @dmThucChayPRID + ',' + convert(nvarchar(50),@thucchayPRID)
				ELSE
					SET @dmThucChayPRID = convert(nvarchar(50),@thucchayPRID)
				--UPDATE GIA TRI THAY DOI CUA THUCCHAYDATINH = 0
				UPDATE ThucChayDaTinh
				SET
					DotChayBooking = @dmThucChayPRID
				WHERE HopDongChiTietREF = @HopDongChiTietID
				AND Convert(date,NgayThucHien) = @NgayThucHien
				AND DmSanPhamREF IN (141,245,250)	
				--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
			FETCH NEXT FROM Record_Cursor INTO @HopDongChiTietID , @DmSanPHamREF, @NgayThucHien, @Soluongthucchay, @thucchayPRID
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END
END

--EXEC [ThucChay_UpdateThucChayPRID] '2013-01-01', '2013-10-30'


```
