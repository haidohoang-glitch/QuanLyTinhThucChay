# Function: `ASD_SPLIT`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2017-01-06 12:47:29.657000
- **Ngày sửa cuối**: 2017-01-06 12:47:29.657000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DELIMITER` | `varchar(5)` | No |
| `@LIST` | `varchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		MinhNH
-- Create date: 07/20/2015
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[ASD_SPLIT] 
   (  @DELIMITER VARCHAR(5), 
      @LIST      VARCHAR(MAX) 
   ) 
   RETURNS @TABLEOFVALUES TABLE 
      (  ROWID   SMALLINT IDENTITY(1,1), 
         [VALUE] VARCHAR(MAX) 
      ) 
AS 
   BEGIN
    
      DECLARE @LENSTRING INT 
 
      WHILE LEN( @LIST ) > 0 
         BEGIN 
         
            SELECT @LENSTRING = 
               (CASE CHARINDEX( @DELIMITER, @LIST ) 
                   WHEN 0 THEN LEN( @LIST ) 
                   ELSE ( CHARINDEX( @DELIMITER, @LIST ) -1 )
                END
               ) 
                                
            INSERT INTO @TABLEOFVALUES 
               SELECT SUBSTRING( @LIST, 1, @LENSTRING )
                
            SELECT @LIST = 
               (CASE ( LEN( @LIST ) - @LENSTRING ) 
                   WHEN 0 THEN '' 
                   ELSE RIGHT( @LIST, LEN( @LIST ) - @LENSTRING - 1 ) 
                END
               ) 
         END
          
      RETURN 
      
   END
```
