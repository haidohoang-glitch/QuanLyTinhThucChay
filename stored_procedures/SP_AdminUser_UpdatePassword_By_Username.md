# Stored Procedure: `AdminUser_UpdatePassword_By_Username`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-27 09:55:42.280000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.720000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Username` | `nvarchar(500)` | No |
| `@Password` | `nvarchar(500)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <27,05,2014>
-- Description:	<Cập nhật thông tin mật khẩu theo tên đăng nhập>
-- =============================================
CREATE PROCEDURE [dbo].[AdminUser_UpdatePassword_By_Username]
(	
	@Username NVARCHAR(250),	
	@Password NVARCHAR(250)
)
AS
BEGIN
	UPDATE AdminUser 
	SET			
		[Password]	= @Password
	WHERE
		Username = @Username
END

```
