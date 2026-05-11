# Stored Procedure: `AdminMenu_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.760000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.890000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminMenuId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <27.02.2012>
-- Edited date:	<01.03.2012>
-- =============================================
CREATE PROCEDURE [dbo].[AdminMenu_Delete]
	@AdminMenuId int
AS
BEGIN
	DELETE FROM AdminGroupMenuPermission WHERE AdminMenuId = @AdminMenuId	

	DELETE FROM AdminMenu WHERE AdminMenuId = @AdminMenuId	
END

```
