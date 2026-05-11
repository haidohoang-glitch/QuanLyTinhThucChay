# Function: `GetIDFieldNameByFieldName`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 03:40:57.993000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.160000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@FieldName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION GetIDFieldNameByFieldName
(
	-- Add the parameters for the function here
	@FieldName nvarchar(50)
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(50)

	-- Add the T-SQL statements to compute the return value here
	set @Result = 'Dm'+ Replace(@FieldName,'Ten','')+'REF'

	-- Return the result of the function
	RETURN @Result

END

```
