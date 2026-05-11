# Function: `FormatDate`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-09 11:47:05.353000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.380000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@InputDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	Format Date
-- =============================================
CREATE FUNCTION [dbo].[FormatDate]
(
	-- Add the parameters for the function here
	@InputDate datetime
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue NVARCHAR(50)
	IF (@InputDate IS NOT NULL AND CONVERT(DATE,@InputDate) <> '01/01/1900')
		SET @ReturnValue = (SELECT CONVERT(VARCHAR, @InputDate, 103))
	ELSE
		SET @ReturnValue = ''

	-- Return the result of the function
	RETURN @ReturnValue

END

```
