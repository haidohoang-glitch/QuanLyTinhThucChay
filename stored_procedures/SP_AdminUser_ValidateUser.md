# Stored Procedure: `AdminUser_ValidateUser`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.260000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.713000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Username` | `nvarchar(500)` | No |
| `@Password` | `nvarchar(500)` | No |
| `@Statuses` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_ValidateUser]
	@Username nvarchar(250),
	@Password nvarchar(250),
	@Statuses int
AS
	SELECT COUNT(AdminUserId) 
	FROM AdminUser
	WHERE Username = @Username AND [Password] = @Password AND [Status] & @Statuses = [Status]

```
