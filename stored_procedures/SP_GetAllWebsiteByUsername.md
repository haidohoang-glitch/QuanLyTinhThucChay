# Stored Procedure: `GetAllWebsiteByUsername`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:10.340000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.690000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@UserName` | `nvarchar(50)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetAllWebsiteByUsername]
	@UserName NVARCHAR(25)
AS
BEGIN
	SELECT abpw.DmWebsiteREF, abpw.TenWebsite FROM AdminBoPhanWebsite abpw
	WHERE abpw.TenDangNhap = @UserName	
END
-- EXEC [GetAllWebsiteByUsername] 'admin'

```
