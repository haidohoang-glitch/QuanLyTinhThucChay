# Stored Procedure: `AdminGroupUser_GetGroupsByUserId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.773000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.823000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminUserId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroupUser_GetGroupsByUserId]
	@AdminUserId int
AS
SELECT * FROM AdminGroupUser
WHERE AdminUserId = @AdminUserId

```
