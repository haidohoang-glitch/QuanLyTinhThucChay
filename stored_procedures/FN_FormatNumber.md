# Function: `FormatNumber`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-11 18:17:36.900000
- **Ngày sửa cuối**: 2015-06-11 18:17:36.900000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(100)` | Yes |
| `@Number` | `float(8)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[FormatNumber]
(
   @Number FLOAT
)
 RETURNS VARCHAR(100)
  AS
 BEGIN
   DECLARE @val VARCHAR(100),@unFormattedNumber VARCHAR(100)
   
   SET @unFormattedNumber = Convert(VARCHAR(100),CONVERT(BIGINT,ROUND(@Number,0)))
   
   SET @val = convert(VARCHAR(50), cast(@unFormattedNumber AS MONEY), 1)

   RETURN (SELECT left(@val, len(@val) - 3))
 END

```
