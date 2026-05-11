# Function: `ThucChay_GetSoLuongThucChayCPD_Test_V2`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-12 10:25:46.243000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.373000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayCPD_Test_V2] 
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
				WHERE dchdct.HopDongChiTietREF = @HopDongChiTietREF				
				AND dchdct.DeletedStatus <> 1
				AND hdct.DeletedStatus <> 1
				AND CONVERT(DATE, @NgayThucHien) 
				BETWEEN CONVERT(DATE,dchdct.ThoiGianBatDau) AND CONVERT(DATE,dchdct.ThoiGianKetThuc)
			)	
	SET @CountDotChayThucTreo =
		(
			SELECT COUNT(*) FROM ThucChayHopDongChiTiet tchdct
			INNER JOIN HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID			 
			WHERE tchdct.HopDongChiTietREF = @HopDongChiTietREF
			AND CONVERT(DATE,@NgayThucHien) 
			BETWEEN CONVERT(date, tchdct.ThoiGianBatDau)AND CONVERT(DATE,tchdct.ThoiGianKetThuc)
			AND tchdct.DeletedStatus = 0
			AND hdct.DeletedStatus = 0
		)
	IF(@CountDotChayHopdong >0)
		SET @SoLuongThucChay = @CountDotChayHopdong
	ELSE
		SET @SoLuongThucChay = @CountDotChayThucTreo				
	-- Return the result of the function
	RETURN @SoLuongThucChay
END

```
