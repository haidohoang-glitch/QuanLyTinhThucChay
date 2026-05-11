# Stored Procedure: `AdminGroupMenuPermission_DeleteById`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:57:43.377000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.843000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@MenuIdList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminGroupMenuPermission_DeleteById]
	@MenuIdList NVARCHAR(200)
AS
BEGIN
	DELETE FROM AdminGroupMenuPermission 
	WHERE AdminMenuId in (@MenuIdList);
END

```
