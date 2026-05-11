# Function: `ThucChay_GetThanhTienChuaChayByHopDongChiTietID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-28 22:51:35.847000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.143000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuaChayByHopDongChiTietID]
(
	-- Add the parameters for the function here
	@HopDongChiTietID NVARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN

	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT, @ThanhTien FLOAT, @ThanhTienChuaChay FLOAT
		
	SET @ThanhTienThucChay = dbo.ThucChay_GetThanhTienThucChayByHopDongChiTietID(@HopDongChiTietID)
	
	SET @ThanhTien = (SELECT ThanhTien FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID)
	
	SET @ThanhTienChuaChay = @ThanhTien - @ThanhTienThucChay
	-- Return the result of the function
	RETURN @ThanhTienChuaChay 

END
```
