# Stored Procedure: `AdminMenu_GetAllByStatusAndUserId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.743000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.887000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Status` | `int(4)` | No |
| `@UserId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminMenu_GetAllByStatusAndUserId] 
	@Status int,
	@UserId int
AS -- [AdminMenu_GetAllByStatusAndUserId]  '3', '2' 
select * from AdminMenu where AdminMenu.AdminMenuId in (
	select AdminGroupMenuPermission.AdminMenuId from AdminGroupMenuPermission 
	where AdminGroupMenuPermission.AdminGroupId in (
		select AdminGroupUser.AdminGroupId from AdminGroupUser 
		where AdminGroupUser.AdminUserId = @UserId
	)
) and AdminMenu.[Status] & @Status = AdminMenu.[Status]
order by AdminMenu.ParentId, AdminMenu.Priority

```
