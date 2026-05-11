# Function: `STRING_SPLIT_QLTC`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2023-07-05 15:56:56.147000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.147000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@stringToSplit` | `varchar` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[STRING_SPLIT_QLTC]( @stringToSplit VARCHAR(MAX) )
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

  SELECT @stringToSplit = LTRIM(RTRIM(Lower(SUBSTRING(@stringToSplit, @pos+1, LEN(@stringToSplit)-@pos))))
 END

 INSERT INTO @returnList
 SELECT @stringToSplit

 RETURN
END

```
