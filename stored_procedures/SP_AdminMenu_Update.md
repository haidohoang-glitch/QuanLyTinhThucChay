# Stored Procedure: `AdminMenu_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.203000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.487000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminMenuId` | `int(4)` | No |
| `@ParentId` | `int(4)` | No |
| `@Name` | `nvarchar(4096)` | No |
| `@CtrlKey` | `nvarchar(4096)` | No |
| `@CtrlSource` | `nvarchar(4096)` | No |
| `@Params` | `nvarchar(4096)` | No |
| `@Priority` | `int(4)` | No |
| `@Status` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminMenu_Update]
	@AdminMenuId int,
	@ParentId int,
	@Name nvarchar(2048),	
	@CtrlKey nvarchar(2048),
	@CtrlSource nvarchar(2048),
	@Params nvarchar(2048),
	@Priority int,
	@Status int							
AS
BEGIN
	UPDATE AdminMenu 
	SET 	
		ParentId = @ParentId,
		Name = @Name,		
		CtrlKey = @CtrlKey,
		CtrlSource = @CtrlSource,
		Params = @Params,
		Priority = @Priority,
		[Status] = @Status
	WHERE 
		AdminMenuId = @AdminMenuId
END

```
