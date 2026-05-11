# Stored Procedure: `AdminUser_UpdateMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-10 16:52:55.047000
- **Ngày sửa cuối**: 2014-11-19 12:24:54.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminUserId` | `int(4)` | No |
| `@Mobile` | `nvarchar(500)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_UpdateMobile]
(	
	@AdminUserId int,	
	@Mobile nvarchar (250)
)
AS
UPDATE AdminUser 
SET	
	Mobile = @Mobile,
	ModifiedOn = getdate()
WHERE
	AdminUserId = @AdminUserId		
select @@ROWCOUNT

```
