# Stored Procedure: `AdminUser_GetAllByStatusesByAdminGroupId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.723000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.757000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |
| `@Statuses` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_GetAllByStatusesByAdminGroupId]
	@AdminGroupId int,
	@Statuses int
AS
SELECT * FROM AdminUser au 
INNER JOIN AdminGroupUser agu
ON au.AdminUserId = agu.AdminUserId
WHERE au.[Status] & @Statuses = au.[Status] AND agu.AdminGroupId = @AdminGroupId
ORDER BY au.Username

```
