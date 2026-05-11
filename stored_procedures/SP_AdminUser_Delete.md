# Stored Procedure: `AdminUser_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.707000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.767000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminUserId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <30.10.2012>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[AdminUser_Delete] 
	@AdminUserId INT
AS
BEGIN
	DELETE FROM AdminGroupUser WHERE AdminUserId = @AdminUserId			
	
	DELETE FROM AdminUser WHERE AdminUserId = @AdminUserId	
END

```
