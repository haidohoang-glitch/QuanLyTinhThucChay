# Stored Procedure: `AdminMenu_Create`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.397000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.893000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ParentId` | `int(4)` | No |
| `@Name` | `nvarchar(4096)` | No |
| `@CtrlKey` | `nvarchar(4096)` | No |
| `@CtrlSource` | `nvarchar(4096)` | No |
| `@Params` | `nvarchar(4096)` | No |
| `@Priority` | `int(4)` | No |
| `@Status` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminMenu_Create]
	@ParentId int,
	@Name nvarchar(2048),	
	@CtrlKey nvarchar(2048),
	@CtrlSource nvarchar(2048),
	@Params nvarchar(2048),
	@Priority int,
	@Status int							
AS
BEGIN
	INSERT INTO AdminMenu
	(
		ParentId,
		Name,		
		CtrlKey,
		CtrlSource,
		Params,
		Priority,
		[Status]
	)
	VALUES
	(
		@ParentId,
		@Name,	
		@CtrlKey,	
		@CtrlSource, 
		@Params,
		@Priority,
		@Status
	)
END

DECLARE @ID INT SET @ID = SCOPE_IDENTITY();
SELECT @ID

```
