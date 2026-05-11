# Stored Procedure: `AdminMenu_Update_Param_Priority`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-28 10:35:28.783000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminMenuId` | `int(4)` | No |
| `@Params` | `nvarchar(4096)` | No |
| `@Priority` | `int(4)` | No |
| `@IsCheck` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminMenu_Update_Param_Priority]
	@AdminMenuId INT,	
	@Params		 NVARCHAR(2048),
	@Priority	 INT,
	@IsCheck	 INT
AS
BEGIN
	UPDATE AdminMenu 
	SET 			
		Params	 = @Params,
		Priority = @Priority,
		IsCheck  = @IsCheck
	WHERE 
		AdminMenuId = @AdminMenuId
END

```
