# Stored Procedure: `usp_Nhanhang_CheckExistsTenNhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:46.193000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNhanHang` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Nhanhang_CheckExistsTenNhan]
@TenNhanHang NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT COUNT(DmNhanhangID) FROM DmNhanHang n WHERE n.TenNhanHang = @TenNhanHang
		
END

```
