# Function: `ThucChayAdmarket_GetAdmarketBalanceUserDaily_UserBalance`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-10 16:07:02.813000
- **Ngày sửa cuối**: 2015-06-10 16:07:02.813000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@UserName` | `nvarchar(400)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-03-20
-- Description:	<Description, ,>
-- =============================================
/*
	PRINT [dbo].[ThucChayAdmarket_GetAdmarketBalanceUserDaily_UserBalance]('','2015-04-01',628)
*/
CREATE FUNCTION [dbo].[ThucChayAdmarket_GetAdmarketBalanceUserDaily_UserBalance]
(
	-- Add the parameters for the function here
	@UserName	NVARCHAR(200),
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @returnValue FLOAT = 0
	SET @returnValue =
	(
		SELECT TOP 1 abud.UserBalance 
		FROM AdmarketBalanceUserDaily abud
		WHERE Convert(date,abud.NgayThucHien) <= @NgayThucHien
		AND abud.UserName = @UserName
		AND abud.DmSanPhamREF = @DmSanPhamREF
		ORDER BY abud.NgayThucHien desc
	)
	SET @returnValue = ISNULL(@returnValue,0)
	-- Return the result of the function
	RETURN @returnValue

END

```
