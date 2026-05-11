# Stored Procedure: `AddUser_AdminBoPhanWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-04 16:04:59.187000
- **Ngày sửa cuối**: 2014-10-14 10:40:05.173000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AccountName` | `nvarchar(100)` | No |
| `@AccountNameReplate` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE AddUser_AdminBoPhanWebsite
	-- Add the parameters for the stored procedure here
	@AccountName NVARCHAR(50),
	@AccountNameReplate NVARCHAR(50)
AS
BEGIN
	DELETE FROM AdminBoPhanWebsite WHERE TenDangNhap = @AccountNameReplate
	
	INSERT INTO AdminBoPhanWebsite
	SELECT 
	  [NhanSuSoYeuLyLichID]
      ,@AccountNameReplate
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmWebsiteREF]
      ,[TenWebsite]
    FROM AdminBoPhanWebsite
    WHERE TenDangNhap = @AccountName
END

```
