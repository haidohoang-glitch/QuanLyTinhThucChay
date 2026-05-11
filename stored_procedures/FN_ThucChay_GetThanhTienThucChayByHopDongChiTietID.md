# Function: `ThucChay_GetThanhTienThucChayByHopDongChiTietID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-28 22:47:36.817000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.703000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienThucChayByHopDongChiTietID]
(
	-- Add the parameters for the function here
	@HopDongChiTietID NVARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN

	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT
		
	SET @ThanhTienThucChay = (SELECT SUM(ThanhTienSauTrietKhauThucChay) FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF = @HopDongChiTietID)
	
	SET @ThanhTienThucChay = ISNULL(@ThanhTienThucChay,0)
	
	SET @ThanhTienThucChay = ROUND(@ThanhTienThucChay,0)
	-- Return the result of the function
	RETURN @ThanhTienThucChay

END
```
