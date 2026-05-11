# Stored Procedure: `AdminPermisionUsers_AddNew`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-10 16:52:55.140000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.353000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@UserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ	
-- Create date: 2013-10-10
-- Description:	Add user to AdminPermistionUsers
-- =============================================

-- EXEC AdminPermisionUsers_AddNew 'nhatmq'

CREATE PROCEDURE [dbo].[AdminPermisionUsers_AddNew] 
	-- Add the parameters for the stored procedure here
	@UserName NVARCHAR(50)
AS
BEGIN
	IF NOT EXISTS (SELECT UserName FROM AdminPermistionUsers WHERE UserName = @UserName)
		INSERT INTO AdminPermistionUsers
		(
			UserName,
			[Description],
			CreatedBy,
			CratedAt,
			LastModifiedBy,
			LastModifiedAt
		)
		VALUES
		(
			@UserName,
			'',
			'nhatmq',
			GETDATE(),
			'nhatmq',
			GETDATE()
		)
END

```
