# Stored Procedure: `AdminMenu_GetById`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.250000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Id` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminMenu_GetById]
(
	@Id int
)
AS
SELECT * FROM AdminMenu WHERE AdminMenuId = @Id

```
