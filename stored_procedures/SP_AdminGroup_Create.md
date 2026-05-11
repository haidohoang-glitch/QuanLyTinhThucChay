# Stored Procedure: `AdminGroup_Create`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.150000
- **Ngày sửa cuối**: 2014-11-19 12:16:49.073000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Name` | `nvarchar(500)` | No |
| `@Description` | `ntext(16)` | No |
| `@Status` | `int(4)` | No |
| `@Priority` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminGroup_Create]
(
	@Name nvarchar(250),
	@Description ntext,
	@Status int,
	@Priority int
)
AS
INSERT INTO AdminGroup 
(
	Name,
	[Description],
	[Status],
	Priority
)
VALUES (
	@Name,
	@Description,
	@Status,
	@Priority
)

DECLARE @ID INT SET @ID = SCOPE_IDENTITY();
SELECT @ID

```
