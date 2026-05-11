# Function: `MD5`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-01-15 14:39:40.093000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(32)` | Yes |
| `@value` | `varchar(4000)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION MD5

(

  @value varchar(4000)

)

RETURNS varchar(32)

AS

BEGIN

  RETURN SUBSTRING(sys.fn_sqlvarbasetostr(HASHBYTES('MD5', @value)),3,32);

END

```
