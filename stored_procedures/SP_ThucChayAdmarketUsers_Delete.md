# Stored Procedure: `ThucChayAdmarketUsers_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-02 17:26:30.273000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.760000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayAdmarketUsers_Delete](@NgayThucHien DATETIME)
AS
BEGIN
	SET NOCOUNT ON;
	
	DELETE 
	FROM   ThucChayAdmarketUsers
	WHERE  
	1=1
	--and DmSanPhamREF = @DmSanPhamREF
	       AND NgayThucHien >= Convert(date,@NgayThucHien)
END

```
