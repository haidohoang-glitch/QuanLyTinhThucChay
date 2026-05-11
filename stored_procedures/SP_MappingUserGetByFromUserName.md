# Stored Procedure: `MappingUserGetByFromUserName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-10 16:52:54.723000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.700000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromUserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-08
-- Description:	Get Mapping UserName
-- =============================================
CREATE PROCEDURE [dbo].[MappingUserGetByFromUserName]
	-- Add the parameters for the stored procedure here
	@FromUserName NVARCHAR(50)
AS
BEGIN
	SELECT A.ToUserName
	FROM MappingUser A
	WHERE A.FromUserName = @FromUserName
END

```
