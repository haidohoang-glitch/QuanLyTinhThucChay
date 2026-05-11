# Function: `fn_getsWhereSecurity`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:42:58.477000
- **Ngày sửa cuối**: 2015-03-27 17:42:58.477000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@Security` | `int(4)` | No |
| `@PhongBanSecurity` | `int(4)` | No |
| `@BoPhanSecurity` | `int(4)` | No |
| `@NhomSecurity` | `int(4)` | No |
| `@ListSanPhamSecurity` | `nvarchar(1024)` | No |
| `@ListWebsiteSecurity` | `nvarchar(1024)` | No |
| `@ListKhachHangSecurity` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-06
-- Description:	<Description, ,>
-- =============================================
-- select [dbo].[fn_getsWhereSecurity]('Nhatmq',-1,0,0,0,'','')
CREATE FUNCTION [dbo].[fn_getsWhereSecurity]
(
	-- Add the parameters for the function here
	@TenDangNhap			nvarchar(50),
	@Security				INT,
	@PhongBanSecurity		INT,
	@BoPhanSecurity			INT,
	@NhomSecurity			INT,
	@ListSanPhamSecurity    NVARCHAR(512), -- anh nhat chuyen vao
	@ListWebsiteSecurity    NVARCHAR(512), -- anh nhat chuyen vao
	@ListKhachHangSecurity  NVARCHAR(512)  -- anh nhat chuyen vao
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue NVARCHAR(4000)
	DECLARE @DauNhay VARCHAR(10) = '''';
	DECLARE @ListWebsiteID VARCHAR(200), @ListSanPhamID VARCHAR(200), @ListKhachHangID VARCHAR(200);
	
			SET @ResultValue = ' 1=1 AND ( UserName = ' + @DauNhay + @TenDangNhap + @DauNhay
			IF @Security = 1 SET @ResultValue += ' OR PhongBanREF = '+@PhongBanSecurity+' )' 
			else IF @Security = 2 SET @ResultValue += ' OR BoPhanREF = '+@BoPhanSecurity+' )'
			else IF @Security = 3 SET @ResultValue += ' OR NhomREF = '+@NhomSecurity+' )'
			ELSE SET @ResultValue += ' OR UserName = ' + @DauNhay + @TenDangNhap + @DauNhay + ')'
	    SET @ListWebsiteID = @ListWebsiteSecurity
		SET @ListSanPhamID = @ListSanPhamSecurity
		SET @ListKhachHangID = @ListKhachHangSecurity
			IF (@ListWebsiteID <> '' AND @ListSanPhamID = '' AND @ListKhachHangID ='')
				SET @ResultValue = @ResultValue + ' AND  DmWebsiteREF  IN (' + @ListWebsiteID + '))'
				
			-- Kiem tra neu co quyen quan ly san pham
			IF (@ListSanPhamID <> '' AND @ListWebsiteID = '' AND @ListKhachHangID ='')
				SET @ResultValue = @ResultValue + ' AND DmSanPhamREF IN (' + @ListSanPhamID + '))'
			
			-- Kiem tra neu dong thoi co ca 2 quyen
			IF (@ListWebsiteID <> '' AND @ListSanPhamID <> '' AND @ListKhachHangID ='')
				SET @ResultValue = @ResultValue + ' AND DmWebsiteREF IN (' + @ListWebsiteID + ') OR DmSanPhamREF IN (' + @ListSanPhamID + '))'
			
				
			IF (@ListWebsiteID = '' AND @ListSanPhamID = '' AND @ListKhachHangID <> '')
				SET @ResultValue = @ResultValue + ' AND  DmKhachHangREF  IN (' + @ListKhachHangID + '))'
				
			-- Kiem tra neu
			IF (@ListSanPhamID <> '' AND @ListWebsiteID = '' AND @ListKhachHangID <> '')
				SET @ResultValue = @ResultValue + ' AND DmKhachHangREF IN (' + @ListKhachHangID + ') OR DmSanPhamREF IN (' + @ListSanPhamID + '))'
			
			-- Kiem tra neu 
			IF (@ListWebsiteID <> '' AND @ListSanPhamID ='' AND @ListKhachHangID <> '')
				SET @ResultValue = @ResultValue + ' AND DmWebsiteREF IN (' + @ListWebsiteID + ') OR DmKhachHangREF IN (' + @ListKhachHangID + '))'
				
			IF (@ListWebsiteID <> '' AND @ListSanPhamID <> '' AND @ListKhachHangID <> '')
				SET @ResultValue = @ResultValue + ' AND DmWebsiteREF IN (' + @ListWebsiteID + ') OR DmKhachHangREF IN (' + @ListKhachHangID + ') OR DmSanPhamREF IN (' + @ListSanPhamID + '))'
				
	RETURN @ResultValue

END

```
