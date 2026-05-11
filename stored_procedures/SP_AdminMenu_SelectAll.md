# Stored Procedure: `AdminMenu_SelectAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-05 10:02:30.417000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.490000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE proc [dbo].[AdminMenu_SelectAll]
AS
BEGIN
	SELECT * FROM AdminMenu am
	WHERE IsCheck IN (0, 1)
	ORDER BY am.ParentId, am.Priority	
END

```
