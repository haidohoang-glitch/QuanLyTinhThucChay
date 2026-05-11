# Function: `f_FIND_IN_STRLIST`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-09 16:22:16.143000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.797000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@str` | `nvarchar` | No |
| `@strlist` | `nvarchar` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[f_FIND_IN_STRLIST] 
(
	@str   NVARCHAR(MAX),
	@strlist NVARCHAR(MAX)
)
RETURNS int

BEGIN
	DECLARE @out INT
	SET @out = 0
	IF(@strlist <> '' AND @str <> '')
	SET @out =
	(
		SELECT COUNT(ITEM)		
		FROM dbo.ArrayToTable(dbo.Array(@strlist,','))
		WHERE dbo.FormatString(item) = @str
	)
	SET @out = ISNULL(@out,0)	
	
	RETURN @out
END
```
