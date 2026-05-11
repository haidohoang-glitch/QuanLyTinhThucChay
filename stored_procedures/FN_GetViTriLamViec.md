# Function: `GetViTriLamViec`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-27 16:38:49.357000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.980000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(300)` | Yes |
| `@TenPhongBan` | `nvarchar(100)` | No |
| `@TenBoPhan` | `nvarchar(100)` | No |
| `@TenNhom` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION GetViTriLamViec
(
	-- Add the parameters for the function here
	@TenPhongBan NVARCHAR(50),
	@TenBoPhan NVARCHAR(50),
	@TenNhom NVARCHAR(50)
)
RETURNS NVARCHAR(150)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result NVARCHAR(150)
	
	SET @Result = ''
	
	IF(@TenPhongBan IS NOT NULL AND @TenPhongBan <> '') SET @Result = @Result + @TenPhongBan + ','
	
	IF(@TenBoPhan IS NOT NULL AND @TenBoPhan <> '') SET @Result = @Result + @TenBoPhan + ','

	IF(@TenNhom IS NOT NULL AND @TenNhom <> '') SET @Result = @Result + @TenNhom + ','
	
	-- Return the result of the function
	RETURN @Result

END

```
