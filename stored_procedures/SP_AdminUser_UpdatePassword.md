# Stored Procedure: `AdminUser_UpdatePassword`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.277000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.723000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminUserId` | `int(4)` | No |
| `@Password` | `nvarchar(500)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_UpdatePassword]
(
	--@AdminUserId int,
	--@OldPassword nvarchar(250),
	--@Password nvarchar (250)
	@AdminUserId int,	
	@Password nvarchar (250)
)
AS
UPDATE AdminUser 
SET	
	[Password] = @Password,
	ModifiedOn = getdate()
WHERE
	AdminUserId = @AdminUserId
	--and [Password] = @OldPassword
	
select @@ROWCOUNT

```
