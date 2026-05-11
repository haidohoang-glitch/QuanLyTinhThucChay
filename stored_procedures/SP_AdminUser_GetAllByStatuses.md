# Stored Procedure: `AdminUser_GetAllByStatuses`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.670000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.760000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Statuses` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_GetAllByStatuses]
	@Statuses int
AS
SELECT * FROM AdminUser
WHERE [Status] & @Statuses = [Status]
ORDER BY Username

```
