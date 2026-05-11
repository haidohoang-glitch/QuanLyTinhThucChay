# Stored Procedure: `AdminGroup_GetById`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.097000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.990000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroup_GetById]
	@AdminGroupId int
AS
BEGIN	
	SELECT * FROM AdminGroup
	WHERE AdminGroupId = @AdminGroupId
END

```
