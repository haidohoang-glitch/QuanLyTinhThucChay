# Function: `ReplaceNhanHang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-05-03 10:57:01.073000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.593000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(1000)` | Yes |
| `@TenNhanhang` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ReplaceNhanHang]
(
	-- Add the parameters for the function here
	@TenNhanhang NVARCHAR(500)
)
RETURNS NVARCHAR(500)
as
BEGIN

	SET @TenNhanhang = replace(@TenNhanhang,'''', '''''')

	-- Return the result of the function
	RETURN @TenNhanhang

END


```
