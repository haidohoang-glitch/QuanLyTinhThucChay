# Stored Procedure: `AdminUser_GetByUsername`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.333000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.743000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Username` | `varchar(128)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_GetByUsername]
	@Username varchar(128)
AS
SELECT * FROM AdminUser
WHERE Username = @Username

```
