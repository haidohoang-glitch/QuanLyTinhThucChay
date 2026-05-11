# Stored Procedure: `usp_NhanHang_GetListKhachHangById`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:41.117000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.363000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@LstCustomer` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <15.01.2014>
-- Description:	<Description,,>
-- =============================================
--[usp_NhanHang_GetListKhachHangById] '193, 194, 195'
CREATE PROCEDURE [dbo].[usp_NhanHang_GetListKhachHangById]	
	@LstCustomer NVARCHAR(512)		
AS
BEGIN
	DECLARE @Sql NVARCHAR(4000)
	SET @Sql = 'SELECT KhachHangID AS Id, TenKhachHang AS Name FROM KhachHangFull WHERE KhachHangID IN (' + @LstCustomer + ')'
	
	PRINT @Sql
	EXEC (@Sql)					
END

```
