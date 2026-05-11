# Function: `f_ReturnGroupNghanhHangID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-01-25 17:09:43.737000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.717000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@strInput` | `nvarchar` | No |
| `@delimiter` | `varchar(2)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[f_ReturnGroupNghanhHangID]
(
	@strInput   NVARCHAR(MAX),
	@delimiter  VARCHAR(2)
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out NVARCHAR(2000);
	
	
	
	
	SELECT @out = COALESCE(@out + ',', '') + CAST(T.DmNghanhHangID AS VARCHAR(2000))
	FROM   (
	           SELECT [Original Data] = @strInput,
	                  items,
	                  dnh.DmNghanhHangID
	           FROM   dbo.StringSplitter(@strInput, @delimiter) AS c
	                  INNER JOIN DmNghanhHang dnh
	                       ON  c.items = dnh.TenNghanhHang
	       ) T
	
	
	RETURN @out;
END
```
