# Stored Procedure: `AdminGroup_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.050000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.797000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |
| `@Name` | `nvarchar(500)` | No |
| `@Description` | `ntext(16)` | No |
| `@Status` | `int(4)` | No |
| `@Priority` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroup_Update]
	@AdminGroupId int,
	@Name nvarchar(250),
	@Description ntext,
	@Status int,
	@Priority int
AS
UPDATE AdminGroup 
SET
	Name = @Name,
	[Description] = @Description,
	[Status] = @Status,
	Priority = @Priority
WHERE
	AdminGroupId = @AdminGroupId

```
