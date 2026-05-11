# Stored Procedure: `AdminGroupMenuPermission_GetByAdminGroupIdAdminMenuId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.827000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.097000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |
| `@AdminMenuId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <25.02.2012>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminGroupMenuPermission_GetByAdminGroupIdAdminMenuId]
	@AdminGroupId int,
	@AdminMenuId int	
AS
BEGIN
	SELECT * FROM AdminGroupMenuPermission 
	WHERE AdminGroupId = @AdminGroupId AND AdminMenuId = @AdminMenuId
END

```
