# Stored Procedure: `MappingUserUpdate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-15 21:42:44.043000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.697000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromUserName` | `nvarchar(100)` | No |
| `@ToUserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ	
-- Create date: <Create Date,,>
-- Create date: 2013-09-15
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[MappingUserUpdate] 
	-- Add the parameters for the stored procedure here
	@FromUserName NVARCHAR(50),
	@ToUserName NVARCHAR(50)
AS
BEGIN
	IF EXISTS (SELECT A.FromUserName FROM MappingUser A WHERE A.FromUserName = @FromUserName)
		UPDATE MappingUser
		SET
			ToUserName = @ToUserName
		WHERE 
			FromUserName = @FromUserName
	ELSE
		INSERT INTO MappingUser
		(
			FromUserName,
			ToUserName
		)
		VALUES
		(
			@FromUserName,
			@ToUserName
		)
END

```
