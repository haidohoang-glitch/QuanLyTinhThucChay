# Function: `ThucChay_GetSoLuongThucChayCPD_Test_V1`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-17 09:35:20.673000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayCPD_Test_V1] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
)
RETURNS INT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @CountDotChayHopdong INT	
	DECLARE @CountDotChayThucTreo INT	
	SET  @CountDotChayHopdong = 
			(				
				SELECT COUNT(*) FROM DotChayHopDongChiTiet dchdct
				INNER JOIN HopDongChiTiet hdct ON dchdct.HopDongChiTietREF = hdct.HopDongChiTietID	
				--INNER JOIN dbo.Booking b ON b.BookingID = dchdct.BookingREF
				WHERE dchdct.HopDongChiTietREF = @HopDongChiTietREF
				--AND dchdct.BookingREF >0
				--AND b.[Status] IN (3,5)
				--AND b.HinhThucSP = 1 
				AND dchdct.DeletedStatus <> 1
				AND CONVERT(DATE,dchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
				AND CONVERT(DATE,dchdct.ThoiGianBatDau) >= CONVERT(DATE,@NgayThucHien)
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
	IF(@CountDotChayHopdong >0)
		SET @SoLuongThucChay = @CountDotChayHopdong
	ELSE
		SET @SoLuongThucChay = @CountDotChayThucTreo				
	-- Return the result of the function
	RETURN @SoLuongThucChay
END

```
