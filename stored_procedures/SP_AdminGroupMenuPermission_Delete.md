# Stored Procedure: `AdminGroupMenuPermission_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.870000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.847000

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
CREATE PROCEDURE [dbo].[AdminGroupMenuPermission_Delete]
	@AdminGroupId int	
AS
BEGIN
	DELETE FROM AdminGroupMenuPermission WHERE AdminGroupId = @AdminGroupId		
END

```
