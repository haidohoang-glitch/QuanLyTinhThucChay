# Function: `GetLastCharIndex`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-01-28 13:51:01.023000
- **Ngày sửa cuối**: 2015-01-28 13:51:01.023000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@s` | `varchar` | No |
| `@char` | `varchar(200)` | No |

## Definition (Source Code)

```sql
Create function GetLastCharIndex(@s varchar(max), @char varchar(200)) returns int
as
begin
 
 DECLARE  @lastIndex int
 DECLARE  @nOccurance int
 DECLARE @searchExpression varchar(max)
 SET @nOccurance = len(@s)
 SET @lastIndex = 0
 SET @searchExpression = @s
 
 while @nOccurance > 0
 BEGIN 
	SELECT @nOccurance = charIndex(@char, @searchExpression)
	IF (@nOccurance > 0)
	BEGIN
		SET @lastIndex = @lastIndex + @nOccurance
		SET @searchExpression = substring(@searchExpression, @nOccurance + 1, len(@searchExpression))
	END
 END
 
	
 return @lastIndex
 
end
```
