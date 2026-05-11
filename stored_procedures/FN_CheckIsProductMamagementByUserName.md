# Function: `CheckIsProductMamagementByUserName`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-07-17 12:22:54.567000
- **Ngày sửa cuối**: 2015-07-17 12:22:54.567000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@userName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-23
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[CheckIsProductMamagementByUserName]
(
	-- Add the parameters for the function here
	@userName NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @resultValue INT

	-- Add the T-SQL statements to compute the return value here
	SET @resultValue = 0;
	
	IF EXISTS(
		SELECT A.TenDangNhap
		FROM AdminBoPhanWebsite A
		WHERE 1=1
			AND A.TenDangNhap = @userName
			AND A.DmSanPhamREF > 0
	)
		SET @resultValue = 1;

	-- Return the result of the function
	RETURN @resultValue

END


```
