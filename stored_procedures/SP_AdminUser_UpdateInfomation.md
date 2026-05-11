# Stored Procedure: `AdminUser_UpdateInfomation`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.300000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminUserId` | `int(4)` | No |
| `@Email` | `nvarchar(500)` | No |
| `@FullName` | `nvarchar(500)` | No |
| `@Birthday` | `datetime(8)` | No |
| `@Gender` | `bit(1)` | No |
| `@Information` | `ntext(16)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_UpdateInfomation]
(
	@AdminUserId int,
	@Email nvarchar (250),
	@FullName nvarchar (250),
	@Birthday datetime,
	@Gender bit,
	@Information ntext	
)
AS
UPDATE AdminUser SET
	Email = @Email,
	FullName = @FullName,
	Birthday = @Birthday,
	Gender = @Gender,
	Information = @Information,	
	ModifiedOn = GETDATE()	
WHERE
	AdminUserId = @AdminUserId

```
