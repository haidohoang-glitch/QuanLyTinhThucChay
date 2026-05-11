# Stored Procedure: `AdminPermisionUsers_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-10 16:52:55.350000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.350000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@UserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-10
-- Description:	Delete user
-- =============================================
CREATE PROCEDURE [dbo].[AdminPermisionUsers_Delete]
	-- Add the parameters for the stored procedure here
	@UserName Nvarchar(50)
AS
BEGIN
	DELETE FROM AdminPermistionUsers WHERE UserName = @UserName
END

```
