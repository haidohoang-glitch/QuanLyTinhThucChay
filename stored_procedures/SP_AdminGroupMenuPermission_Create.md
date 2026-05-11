# Stored Procedure: `AdminGroupMenuPermission_Create`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.890000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.850000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminGroupId` | `int(4)` | No |
| `@AdminMenuId` | `int(4)` | No |
| `@Status` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <25.02.2012>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminGroupMenuPermission_Create]
	@AdminGroupId int,
	@AdminMenuId int,
	@Status int
AS
BEGIN
	INSERT INTO AdminGroupMenuPermission
	(
		AdminGroupId,
		AdminMenuId,
		[Status]
	) 	   
	VALUES
	(
		@AdminGroupId,
		@AdminMenuId,
		@Status
	)	
END

SELECT SCOPE_IDENTITY()

```
