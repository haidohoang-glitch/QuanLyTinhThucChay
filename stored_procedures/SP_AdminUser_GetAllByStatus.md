# Stored Procedure: `AdminUser_GetAllByStatus`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.690000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.763000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Status` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_GetAllByStatus]
	@Status int
AS
SELECT * FROM AdminUser
WHERE [Status] & @Status = @Status
ORDER BY Username

```
