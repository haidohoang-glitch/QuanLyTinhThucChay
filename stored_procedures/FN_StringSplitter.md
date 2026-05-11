# Function: `StringSplitter`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2014-01-25 17:09:43.397000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.177000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@str` | `nvarchar` | No |
| `@delimiter` | `char(1)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[StringSplitter]
(
	@str        NVARCHAR(MAX),
	@delimiter  CHAR(1)
)
RETURNS TABLE
AS
	RETURN 
	
	SELECT ItemNumber = ROW_NUMBER() OVER(
	           ORDER BY(
	               SELECT 1
	           )
	       ),
	       Items = SPLIT.a.value('.', 'NVARCHAR(max)')
	FROM   (
	           SELECT CAST(
	                      '<X>' + REPLACE(@str, @delimiter, '</X><X>') + '</X>' 
	                      AS XML
	                  ) AS Splitdata
	       ) X
	       CROSS APPLY Splitdata.nodes('/X') SPLIT(a)   
```
