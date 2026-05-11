# Stored Procedure: `MappingUser_GetUserNameToMapping`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:21.970000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.590000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromUserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-28
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[MappingUser_GetUserNameToMapping]
	-- Add the parameters for the stored procedure here
	@FromUserName NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT * 
    FROM MappingUser A
    WHERE A.FromUserName = @FromUserName
END

```
