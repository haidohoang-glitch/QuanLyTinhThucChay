# Stored Procedure: `AdminUser_CheckIfUserExisted`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.660000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.777000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Username` | `nvarchar(500)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_CheckIfUserExisted]
	@Username nvarchar(250)
AS
SELECT COUNT(*) FROM AdminUser
WHERE Username = @Username

```
