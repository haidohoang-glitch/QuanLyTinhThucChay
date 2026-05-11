# Function: `ThucChay_GetSoLuongThucChayBoxGiaVang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-03-01 10:36:55.590000
- **Ngày sửa cuối**: 2019-04-04 15:00:19.433000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayBoxGiaVang] 
(
	-- Add the parameters for the function here	
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @Count INT	
	
	SET  @Count = 
			(
				
				SELECT COUNT(*) FROM dbo.ThucChayHopDongChiTiet dchdct
				INNER JOIN dbo.HopDongChiTiet hdct 
					ON (
							dchdct.HopDongChiTietREF = hdct.HopDongChiTietID
							AND hdct.DmSanPhamREF in  (385,5005 ,5006,5007,5082 ) 
						)
				WHERE dchdct.HopDongChiTietREF = @HopDongChiTietREF				
				AND CONVERT(DATE, dchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
				AND CONVERT(DATE,dchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien)				
			)	
			IF(@Count >0)
				SET @SoLuongThucChay = 1
			ELSE
				SET @SoLuongThucChay = 0
				
	-- Return the result of the function
	RETURN @SoLuongThucChay

END
```
