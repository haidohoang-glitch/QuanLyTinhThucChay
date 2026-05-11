# Stored Procedure: `AdminGroupUser_Create`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.810000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.833000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |
| `@AdminUserId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroupUser_Create]
	@AdminGroupId int,
	@AdminUserId int
AS
INSERT INTO AdminGroupUser
(
	AdminGroupId,
	AdminUserId
) VALUES (
	@AdminGroupId,
	@AdminUserId
)

```
