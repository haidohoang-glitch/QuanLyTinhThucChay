# Function: `ThucChay_GetSoNgayCanhBaoThucChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-11 17:14:29.240000
- **Ngày sửa cuối**: 2015-06-11 17:14:29.240000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-03-20
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoNgayCanhBaoThucChay]
(

)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @returnValue INT

	SET @returnValue = 3;

	-- Return the result of the function
	RETURN @returnValue

END

```
