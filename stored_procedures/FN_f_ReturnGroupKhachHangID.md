# Function: `f_ReturnGroupKhachHangID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-01-25 17:09:44.117000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.743000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(2000)` | Yes |
| `@strInput` | `nvarchar` | No |
| `@delimiter` | `varchar(2)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[f_ReturnGroupKhachHangID]
(
	@strInput   NVARCHAR(MAX),
	@delimiter  VARCHAR(2)
)
RETURNS VARCHAR(2000)

BEGIN
	DECLARE @out NVARCHAR(2000);
	
	
	SELECT @out = COALESCE(@out + ',', '') + CAST(T.KhachHangID AS VARCHAR(2000))
	FROM   (
	           SELECT [Original Data] = @strInput,
	                  items,
	                  kh.KhachHangID
	           FROM   dbo.StringSplitter(@strInput, @delimiter) AS c
	                  INNER JOIN KhachHangFull kh
	                       ON  c.items = kh.TenKhachHang
	       ) T
	
	
	RETURN @out;
END
```
