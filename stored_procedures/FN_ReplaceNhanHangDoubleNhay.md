# Function: `ReplaceNhanHangDoubleNhay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-03-11 10:40:18.197000
- **Ngày sửa cuối**: 2017-03-11 10:40:18.197000

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
CREATE FUNCTION [dbo].[ReplaceNhanHangDoubleNhay]
(
	-- Add the parameters for the function here
	@TenNhanhang NVARCHAR(500)
)
RETURNS NVARCHAR(500)
as
BEGIN

	SET @TenNhanhang = replace(@TenNhanhang,'''''', '''')

	-- Return the result of the function
	RETURN @TenNhanhang

END


```
