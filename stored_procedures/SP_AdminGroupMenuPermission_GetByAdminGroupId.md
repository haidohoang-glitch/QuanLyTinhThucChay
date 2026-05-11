# Stored Procedure: `AdminGroupMenuPermission_GetByAdminGroupId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.843000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.837000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <25.02.2012>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminGroupMenuPermission_GetByAdminGroupId]
	@AdminGroupId int	
AS
BEGIN
	SELECT * FROM AdminGroupMenuPermission WHERE AdminGroupId = @AdminGroupId		
END

```
