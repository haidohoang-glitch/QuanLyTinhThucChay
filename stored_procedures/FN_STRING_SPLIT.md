# Function: `STRING_SPLIT`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2018-07-30 15:00:20.293000
- **Ngày sửa cuối**: 2018-07-30 15:00:20.293000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@stringToSplit` | `varchar` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[STRING_SPLIT]( @stringToSplit VARCHAR(MAX) )
RETURNS
 @returnList TABLE ([Name] [nvarchar] (500))
AS
BEGIN

 DECLARE @name NVARCHAR(255)
 DECLARE @pos INT

 WHILE CHARINDEX(',', @stringToSplit) > 0
 BEGIN
  SELECT @pos  = CHARINDEX(',', @stringToSplit)  
  SELECT @name = SUBSTRING(@stringToSplit, 1, @pos-1)

  INSERT INTO @returnList 
  SELECT @name

  SELECT @stringToSplit = SUBSTRING(@stringToSplit, @pos+1, LEN(@stringToSplit)-@pos)
 END

 INSERT INTO @returnList
 SELECT @stringToSplit

 RETURN
END
```
