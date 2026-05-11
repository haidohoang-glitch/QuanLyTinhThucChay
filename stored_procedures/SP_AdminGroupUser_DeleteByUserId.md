# Stored Procedure: `AdminGroupUser_DeleteByUserId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.793000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.827000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminUserId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroupUser_DeleteByUserId]
	@AdminUserId int
AS
DELETE FROM AdminGroupUser
WHERE AdminUserId = @AdminUserId

```
