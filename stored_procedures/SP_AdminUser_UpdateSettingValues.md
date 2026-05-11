# Stored Procedure: `AdminUser_UpdateSettingValues`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:51:39.267000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.717000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Username` | `nvarchar(256)` | No |
| `@SettingValues` | `nvarchar(256)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_UpdateSettingValues]
(
	@Username nvarchar(128),	
	@SettingValues nvarchar (128)
)
AS
UPDATE AdminUser 
SET	
	SettingValues = @SettingValues,
	ModifiedOn = getdate()
WHERE
	Username = @Username
	
select @@ROWCOUNT

```
