# Function: `CompareSoLuong`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-10-18 20:06:03.537000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.847000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@SoLuong1` | `float(8)` | No |
| `@SoLuong2` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION CompareSoLuong 
(
	-- Add the parameters for the function here
	@SoLuong1 FLOAT,
	@SoLuong2 Float
)
RETURNS int
AS
BEGIN
	
	DECLARE @KetQua int 
	
	SET @KetQua = 0
	IF(@SoLuong1 = @SoLuong2) SET @KetQua = 1
	
	-- Return the result of the function
	RETURN @KetQua

END

```
