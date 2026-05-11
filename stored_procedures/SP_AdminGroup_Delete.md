# Stored Procedure: `AdminGroup_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.130000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroup_Delete]
	@AdminGroupId int
AS
DELETE FROM AdminGroup
WHERE
	AdminGroupId = @AdminGroupId

```
