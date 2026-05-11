# Stored Procedure: `usp_DeleteThucChayAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-13 14:21:17.790000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.243000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_DeleteThucChayAll]
	@NgayThucHien DATETIME
AS
BEGIN
	DELETE [dbo].[ThucChay]
	WHERE  CONVERT(date, NgayThucHien) >= CONVERT(date, @NgayThucHien)
	
	SELECT '1'
END

```
