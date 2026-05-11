# Stored Procedure: `ThucChayAdXUsersBrand_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-09 14:53:40.290000
- **Ngày sửa cuối**: 2016-03-09 14:53:40.290000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayAdXUsersBrand_Delete](@NgayThucHien DATETIME)
AS
BEGIN
	
	DELETE 
	FROM  dbo.ThucChayAdmarketUser_NhanHang
	WHERE  
	1=1
	AND CONVERT(DATE,NgayThucHien) = Convert(date,@NgayThucHien)	
END
```
