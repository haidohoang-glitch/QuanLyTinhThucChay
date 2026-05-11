# Function: `ThucChay_GetSoLuongThucChayCPD_Test`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-03-04 09:09:11.870000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.447000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayCPD_Test] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @CountDotChayBooking INT	
	DECLARE @CountDotChayThucTreo INT	
	SET  @CountDotChayBooking = 
			(				
				SELECT COUNT(*) FROM DotChayHopDongChiTiet dchdct
				INNER JOIN dbo.Booking b ON b.BookingID = dchdct.BookingREF
				WHERE dchdct.HopDongChiTietREF = @HopDongChiTietREF
				AND dchdct.BookingREF >0
				--AND b.[Status] IN (3,5)
				AND b.HinhThucSP = 1 
				AND CONVERT(DATE,b.NgayBatDau)  <= CONVERT(DATE,@NgayThucHien)
				AND CONVERT(DATE,b.NgayKetThuc) >= CONVERT(DATE,@NgayThucHien)
			)	
	SET @CountDotChayThucTreo =
		(
			SELECT COUNT(*) FROM ThucChayHopDongChiTiet tchdct
			INNER JOIN HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID			 
			WHERE tchdct.HopDongChiTietREF = @HopDongChiTietREF
			AND CONVERT(date, tchdct.ThoiGianBatDau) <= CONVERT(DATE,@NgayThucHien)
			AND CONVERT(DATE,tchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien)
			AND tchdct.DeletedStatus = 0
		)
	IF(@CountDotChayBooking >0)
		SET @SoLuongThucChay = @CountDotChayBooking
	ELSE
		SET @SoLuongThucChay = @CountDotChayThucTreo				
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
