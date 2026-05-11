# Stored Procedure: `AdminGroupUser_DeleteByGroupId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-28 10:35:47.537000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.830000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroupUser_DeleteByGroupId]
	@AdminGroupId int
AS
DELETE FROM AdminGroupUser
WHERE AdminGroupId = @AdminGroupId

```
