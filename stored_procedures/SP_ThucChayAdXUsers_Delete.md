# Stored Procedure: `ThucChayAdXUsers_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:00.380000
- **Ngày sửa cuối**: 2015-06-25 17:37:44.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayAdXUsers_Delete](@NgayThucHien DATETIME)
AS
BEGIN
	
	DELETE 
	FROM   ThucChayAdXForUsers
	WHERE  
	1=1
	AND CONVERT(DATE,NgayThucHien) = Convert(date,@NgayThucHien)	
END
```
