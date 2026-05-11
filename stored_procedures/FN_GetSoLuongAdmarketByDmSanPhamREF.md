# Function: `GetSoLuongAdmarketByDmSanPhamREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-27 10:52:03.940000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.653000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[GetSoLuongAdmarketByDmSanPhamREF]
(
	-- Add the parameters for the function here
	@DmSanPhamREF INT,
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoTien FLOAT
	
	SET @SoTien = 0
	
	IF(@DmSanPhamREF = 144 OR @DmSanPhamREF = 299)SET @SoTien = @TongClickThucChay
	ELSE
		IF(@DmSanPhamREF = 337 OR @DmSanPhamREF = 370)SET @SoTien = @TongViewThucChay
	
	-- Return the result of the function
	RETURN @SoTien

END

```
