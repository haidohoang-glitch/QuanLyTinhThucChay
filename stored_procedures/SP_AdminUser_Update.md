# Stored Procedure: `AdminUser_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.320000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.740000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminUserId` | `int(4)` | No |
| `@Email` | `nvarchar(500)` | No |
| `@FullName` | `nvarchar(500)` | No |
| `@Birthday` | `datetime(8)` | No |
| `@Gender` | `bit(1)` | No |
| `@Information` | `ntext(16)` | No |
| `@Status` | `int(4)` | No |
| `@SettingValues` | `nvarchar(256)` | No |
| `@Mobile` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_Update]
(	
	@AdminUserId int,
	@Email nvarchar (250),
	@FullName nvarchar (250),
	@Birthday datetime,
	@Gender bit,
	@Information ntext,
	@Status int,
	@SettingValues nvarchar (128),
	@Mobile NVARCHAR(50)
)
AS
UPDATE AdminUser SET	
	Email			= @Email,
	FullName		= @FullName,
	Birthday		= @Birthday,
	Gender			= @Gender,
	Information		= @Information,
	[Status]		= @Status,
	SettingValues	= @SettingValues,		
	ModifiedOn		= GETDATE(),
	Mobile			= @Mobile	
WHERE
	AdminUserId = @AdminUserId

```
