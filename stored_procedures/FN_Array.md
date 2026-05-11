# Function: `Array`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-23 08:52:30.767000
- **Ngày sửa cuối**: 2014-10-14 10:39:38.073000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `xml` | Yes |
| `@StringArray` | `varchar(8000)` | No |
| `@Delimiter` | `varchar(10)` | No |

## Definition (Source Code)

```sql
create FUNCTION [dbo].[Array]
-- =================================================
-- array Function
-- =================================================
-- This function returns an XML version of a list with
-- the sequence number and the value of each element
-- as an XML fragment
-- Parameters
-- array() takes a varchar(max) list with whatever delimiter you wish. The
-- second value is the delimiter
   (
    @StringArray VARCHAR(8000),
    @Delimiter VARCHAR(10) = ','
    
   )
RETURNS XML
AS BEGIN
      DECLARE @results TABLE
         (
           seqno INT IDENTITY(1, 1),-- the sequence is meaningful here
           Item VARCHAR(MAX)
         )
      DECLARE @Next INT
      DECLARE @lenStringArray INT
      DECLARE @lenDelimiter INT
      DECLARE @ii INT
      DECLARE @xml XML

      SELECT   @ii = 0, @lenStringArray = LEN(REPLACE(@StringArray, ' ', '|')),
               @lenDelimiter = LEN(REPLACE(@Delimiter, ' ', '|'))

      WHILE @ii <= @lenStringArray + 1--while there is another list element
         BEGIN
            SELECT   @next = CHARINDEX(@Delimiter, @StringArray + @Delimiter,
                                       @ii)
             INSERT   INTO @Results
                     (Item)
                     SELECT   SUBSTRING(@StringArray, @ii, @Next - @ii)
             SELECT   @ii = @Next + @lenDelimiter
         END    
      SELECT   @xml = ( SELECT seqno,
                             item
                     FROM   @results
                   FOR
                     XML PATH('element'),
                         TYPE,
                         ELEMENTS,
                         ROOT('stringarray')
                   )
      RETURN @xml
   END

```
