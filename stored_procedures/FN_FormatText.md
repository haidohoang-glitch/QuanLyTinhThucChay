# Function: `FormatText`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-09 11:47:05.793000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@InputText` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-06
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.FormatText
(
	-- Add the parameters for the function here
	@InputText NVARCHAR(MAX)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue NVARCHAR(MAX)
	
	IF @InputText <> ''
	BEGIN
		SET @InputText = LOWER(@InputText)
		
		SET @ReturnValue = (SELECT UPPER(LEFT(@InputText,1))+SUBSTRING(@InputText,2,LEN(@InputText)))
	END
	ELSE
		SET @ReturnValue = ''

	-- Return the result of the function
	RETURN @ReturnValue

END

```
