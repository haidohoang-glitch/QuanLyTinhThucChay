# Stored Procedure: `AdminUser_GetBy_Username_Status`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.373000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.750000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Username` | `nvarchar(500)` | No |
| `@Status` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_GetBy_Username_Status]
	@Username nvarchar(250),
	@Status int
AS
SELECT * FROM AdminUser
WHERE Username = @Username AND [Status] & @Status = [Status]

```
