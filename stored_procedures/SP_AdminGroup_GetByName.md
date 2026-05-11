# Stored Procedure: `AdminGroup_GetByName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-28 10:35:44.600000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.800000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Name` | `nvarchar(256)` | No |

## Definition (Source Code)

```sql
CREATE proc [dbo].[AdminGroup_GetByName]
	@Name NVARCHAR(128)
AS
BEGIN
	SELECT TOP 1 * FROM AdminGroup ag 
	WHERE NAME = @Name
END

```
