# Function: `fnSplitString`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2014-07-30 09:58:43.247000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.410000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@string` | `nvarchar` | No |
| `@delimiter` | `char(1)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fnSplitString] 
( 
    @string NVARCHAR(MAX), 
    @delimiter CHAR(1) 
) 
RETURNS @output TABLE(splitdata NVARCHAR(MAX)) 
BEGIN 
    DECLARE @start INT, @end INT
     
    SELECT @start = 1, @end = CHARINDEX(@delimiter, @string)
     
    WHILE @start < LEN(@string) + 1 
	
	BEGIN 
        IF @end = 0  
            SET @end = LEN(@string) + 1
       
        INSERT INTO @output (splitdata)
        VALUES(SUBSTRING(@string, @start, @end - @start)) 
        
        SET @start = @end + 1
        
        SET @end = CHARINDEX(@delimiter, @string, @start)
        
	END
	 
    RETURN 
END
```
