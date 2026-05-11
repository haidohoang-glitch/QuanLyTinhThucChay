# Stored Procedure: `AdminMenu_GetByParentId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.233000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ParentId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminMenu_GetByParentId]	
	@ParentId int
AS
BEGIN
	SELECT * FROM AdminMenu 
	WHERE ParentId = @ParentId
	ORDER BY Priority 
END

```
