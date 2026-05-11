# Function: `f_ReturnGroupConcatNhansuID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-01-25 17:09:44.407000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.770000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@strInput` | `nvarchar` | No |
| `@delimiter` | `varchar(2)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[f_ReturnGroupConcatNhansuID] 
(
	@strInput   NVARCHAR(MAX),
	@delimiter  VARCHAR(2)
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out NVARCHAR(2000);
	SELECT @out = COALESCE(@out + ',', '') + CAST(T.NhanSuSoYeuLyLichID AS VARCHAR(1000))
	FROM   (
	           SELECT [Original Data] = @strInput,
	                  items,
	                  ns.NhanSuSoYeuLyLichID
	           FROM   dbo.StringSplitter(@strInput, @delimiter) AS c
	                  INNER JOIN NhanSuSoYeuLyLichFull ns
	                       ON  c.items = ns.HoVaTen
	       ) T	       	
	
	RETURN @out;
END
```
