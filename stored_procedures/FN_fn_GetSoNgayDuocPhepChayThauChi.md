# Function: `fn_GetSoNgayDuocPhepChayThauChi`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-10 16:07:02.353000
- **Ngày sửa cuối**: 2016-08-29 12:07:44.980000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_GetSoNgayDuocPhepChayThauChi]()
RETURNS INT

BEGIN
	DECLARE @out INT
	SET @out = 1000
	SET @out = ISNULL(@out, 0)
	
	RETURN @out;
END

```
