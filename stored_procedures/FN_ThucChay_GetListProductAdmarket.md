# Function: `ThucChay_GetListProductAdmarket`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-16 16:09:06.813000
- **Ngày sửa cuối**: 2015-06-16 17:47:10.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-06-16
-- Description:	<Description, ,>
-- =============================================
/*
	PRINT dbo.ThucChay_GetListProductAdmarket()
* */
CREATE FUNCTION dbo.ThucChay_GetListProductAdmarket
(
	-- Add the parameters for the function here
	
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @returnValue NVARCHAR(MAX);

	SET @returnValue = '144, 299, 337, 585, 628';

	-- Return the result of the function
	RETURN @returnValue

END

```
