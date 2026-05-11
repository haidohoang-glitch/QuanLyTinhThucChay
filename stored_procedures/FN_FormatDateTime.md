# Function: `FormatDateTime`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-09 10:24:11.953000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.353000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@DateTime` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-09
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.FormatDateTime
(
	-- Add the parameters for the function here
	@DateTime DateTime
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue NVARCHAR(50)

	-- Add the T-SQL statements to compute the return value here
	IF 	CONVERT(DATE, @DateTime) = '1900-01-01'
		SET @ResultValue=''
	ELSE
		SET @ResultValue = CONVERT(NVARCHAR(50),@DateTime)

	-- Return the result of the function
	RETURN @ResultValue

END

```
