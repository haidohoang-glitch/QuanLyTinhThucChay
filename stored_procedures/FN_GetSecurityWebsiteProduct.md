# Function: `GetSecurityWebsiteProduct`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-05 09:32:07.860000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.747000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar` | Yes |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ThoiGianColumn` | `varchar(50)` | No |
| `@TenDangNhapColumn` | `varchar(50)` | No |
| `@SanPhamColumn` | `varchar(50)` | No |
| `@WebsiteColumn` | `varchar(50)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-04
-- Description:	<Description, ,>
-- =============================================
-- PRINT dbo.GetSecurityWebsiteProduct('2013-10-01','2013-10-30','trangphamthithu','NgayThucHien','TenDangNhap','DmSanPhamREF','DmWebsiteREF')
CREATE FUNCTION [dbo].[GetSecurityWebsiteProduct]
(
	-- Add the parameters for the function here
	 @ThoiGianBatDau DATETIME
	,@ThoiGianKetThuc DATETIME
	,@TenDangNhap nvarchar(50)
	,@ThoiGianColumn VARCHAR(50)
	,@TenDangNhapColumn VARCHAR(50)
	,@SanPhamColumn VARCHAR(50)
	,@WebsiteColumn VARCHAR(50)
)
RETURNS VARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @FilterSecurity varchar(8000);
	DECLARE @GroupPermision INT;
	DECLARE @DauNhay VARCHAR(10) = '''';
	DECLARE @ListWebsiteID VARCHAR(200), @ListSanPhamID VARCHAR(200);
	
	IF (EXISTS(SELECT username FROM AdminUser A WHERE A.Username = @TenDangNhap))
	BEGIN
		SET @ListWebsiteID = dbo.GetListWebsiteByNhanVien(@TenDangNhap)
		SET @ListSanPhamID = dbo.GetListSanPhamByNhanVien(@TenDangNhap)
		
		SET @GroupPermision = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap);

		SET @FilterSecurity = ' 1=1 '
		
		SET @FilterSecurity += ' AND (CONVERT(DATE,' + @ThoiGianColumn + ') BETWEEN ' + @DauNhay + CONVERT(VARCHAR(50),@ThoiGianBatDau) + @DauNhay + ' AND ' +  + @DauNhay + CONVERT(VARCHAR(50),@ThoiGianKetThuc) + @DauNhay + ') '
	
		-- Neu ko co quyen xem full du lieu
		IF @GroupPermision <> -1		
		BEGIN
			-- Kiem tra neu co quyen quan ly Website
			IF (@ListWebsiteID <> '' AND @ListSanPhamID = '')
				SET @FilterSecurity = @FilterSecurity + ' AND ( ' + @WebsiteColumn + ' IN (' + @ListWebsiteID + '))'
				
			-- Kiem tra neu co quyen quan ly san pham
			IF (@ListSanPhamID <> '' AND @ListWebsiteID = '')
				SET @FilterSecurity = @FilterSecurity + ' AND (' + @SanPhamColumn + ' IN (' + @ListSanPhamID + '))'
			
			-- Kiem tra neu dong thoi co ca 2 quyen
			IF (@ListWebsiteID <> '' AND @ListSanPhamID <> '')
				SET @FilterSecurity = @FilterSecurity + ' AND ( ' + @WebsiteColumn + ' IN (' + @ListWebsiteID + ') OR ' + @SanPhamColumn + ' IN (' + @ListSanPhamID + '))'
				
			IF (@ListWebsiteID = '' AND @ListSanPhamID = '')
				SET @FilterSecurity = @FilterSecurity + ' AND 1<>1 ' 	
		END
	END
	ELSE
		SET @FilterSecurity = '1<>1'
	
	-- Return the result of the function
	RETURN @FilterSecurity

END

```
