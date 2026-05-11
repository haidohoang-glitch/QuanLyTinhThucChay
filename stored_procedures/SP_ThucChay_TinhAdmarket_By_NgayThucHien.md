# Stored Procedure: `ThucChay_TinhAdmarket_By_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-07-13 15:10:11.430000
- **Ngày sửa cuối**: 2017-07-13 15:10:47.753000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChay_TinhAdmarket_By_NgayThucHien] '2017-07-13'
CREATE PROCEDURE [dbo].[ThucChay_TinhAdmarket_By_NgayThucHien] 
	 @NgayThucHien	DATETIME
			
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	-- Tinh thuc chay Admarket
	EXEC [dbo].[Admarket_ThucChayDaTinhAdmarket_NhanHang] @NgayThucHien, @NgayThucHien
	EXEC [ThucChay_UpdateThucChayDaTinhAdmarket_NhanHangChuanHoa] @NgayThucHien,@NgayThucHien,0,@NgayThucHien

END




```
