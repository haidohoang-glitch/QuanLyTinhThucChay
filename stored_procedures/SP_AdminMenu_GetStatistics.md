# Stored Procedure: `AdminMenu_GetStatistics`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.220000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.877000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Status` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <01.03.2012>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminMenu_GetStatistics]
	@Status int	
AS
BEGIN	
	SELECT COUNT(AdminMenuId) FROM AdminMenu WHERE [Status] = @Status
END

```
