# Stored Procedure: `usp_Nhanhang_SearchByTennhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:47.807000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.550000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNhanhang` | `nvarchar(2048)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Nhanhang_SearchByTennhan]
	@TenNhanhang NVARCHAR(1024)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT TOP 100 dnh.DmNhanHangID, dnh.TenNhanHang
	FROM   DmNhanHang dnh
	WHERE  dnh.TenNhanHang LIKE '%' + @TenNhanhang + '%'
END

```
