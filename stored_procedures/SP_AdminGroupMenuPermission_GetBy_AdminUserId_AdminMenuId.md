# Stored Procedure: `AdminGroupMenuPermission_GetBy_AdminUserId_AdminMenuId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.857000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminUserId` | `int(4)` | No |
| `@AdminMenuId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <27.02.2012>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminGroupMenuPermission_GetBy_AdminUserId_AdminMenuId]	
	@AdminUserId int,	
	@AdminMenuId int
AS
BEGIN	
	SELECT * FROM AdminGroupMenuPermission 
	WHERE 
		AdminGroupId IN (select AdminGroupId from AdminGroupUser where AdminUserId = @AdminUserId)
		AND AdminMenuId = @AdminMenuId 
END

```
