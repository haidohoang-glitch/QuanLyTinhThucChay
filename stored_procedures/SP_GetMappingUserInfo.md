# Stored Procedure: `GetMappingUserInfo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-26 15:33:24.693000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.380000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-24
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetMappingUserInfo] 
	-- Add the parameters for the stored procedure here
	@TenDangNhap NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @ToUserName NVARCHAR(50);
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
    
    IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName;
		
	SELECT * FROM AdminUser A WHERE A.Username = @TenDangNhap;
END

```
