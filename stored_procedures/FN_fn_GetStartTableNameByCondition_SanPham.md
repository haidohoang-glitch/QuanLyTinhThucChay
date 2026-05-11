# Function: `fn_GetStartTableNameByCondition_SanPham`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-26 11:48:09.003000
- **Ngày sửa cuối**: 2015-03-26 11:48:09.003000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(200)` | Yes |
| `@isWeb` | `int(4)` | No |
| `@isHinhThucQuangCao` | `int(4)` | No |
| `@isBanner` | `int(4)` | No |
| `@isHopDong` | `int(4)` | No |
| `@isKhachHang` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================

CREATE FUNCTION [dbo].[fn_GetStartTableNameByCondition_SanPham]
(
	-- Add the parameters for the function here
	@isWeb INT,
	@isHinhThucQuangCao INT,
	@isBanner INT,
	@isHopDong INT,
	@isKhachHang INT 
)
RETURNS NVARCHAR(100)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @result NVARCHAR(100)
	-- Add the T-SQL statements to compute the return value here
	-- Có 1 diêud kiện
	IF(@isWeb >0 AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isHopDong = 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_SanPham_TheoWebsite'
	IF(@isWeb = 0 AND @isHinhThucQuangCao > 0 AND @isBanner = 0 AND @isHopDong = 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_SanPham_TheoHinhThucQuangCao'
	IF(@isWeb = 0 AND @isHinhThucQuangCao = 0 AND @isBanner > 0 AND @isHopDong = 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_SanPham_TheoBanner'
	IF(@isWeb = 0 AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isHopDong > 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham'
	IF(@isWeb = 0 AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isHopDong = 0 AND @isKhachHang > 0)
		SET @result = 'rptThucChay_KhachHang_TheoSanPham'
	-- Có 2 điều kiện
	-- co website
	IF(@isWeb > 0 AND @isHinhThucQuangCao > 0 AND @isBanner = 0 AND @isHopDong = 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_SanPham_TheoWebsite_HinhThucQuangCao'
	IF(@isWeb > 0 AND @isHinhThucQuangCao = 0 AND @isBanner > 0 AND @isHopDong = 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_SanPham_TheoWebsite_Banner'
	IF(@isWeb > 0 AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isHopDong > 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham_Website'
	IF(@isWeb > 0 AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isHopDong = 0 AND @isKhachHang > 0)
		SET @result = 'rptThucChay_KhachHang_TheoSanPham_Website'
	-- co HinhThucQuangCao
	IF(@isWeb = 0 AND @isHinhThucQuangCao > 0 AND @isBanner > 0 AND @isHopDong = 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_SanPham_TheoHinhThucQuangCao_Banner'
	IF(@isWeb = 0 AND @isHinhThucQuangCao > 0 AND @isBanner = 0 AND @isHopDong > 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham_HinhThucQuangCao'
	IF(@isWeb = 0 AND @isHinhThucQuangCao > 0 AND @isBanner = 0 AND @isHopDong = 0 AND @isKhachHang > 0)
		SET @result = 'rptThucChay_KhachHang_TheoSanPham_HinhThucQuangCao'
	-- Co banner
	IF(@isWeb = 0 AND @isHinhThucQuangCao = 0 AND @isBanner > 0 AND @isHopDong > 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham_Banner'
	IF(@isWeb = 0 AND @isHinhThucQuangCao = 0 AND @isBanner > 0 AND @isHopDong = 0 AND @isKhachHang > 0)
		SET @result = 'rptThucChay_KhachHang_TheoSanPham_Banner'
	IF(@isWeb = 0 AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isHopDong > 0 AND @isKhachHang > 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham'-- do hd co ca khach hang
	-- co 3 dieu kien 
	IF(@isWeb > 0 AND @isHinhThucQuangCao > 0 AND @isBanner > 0 AND @isHopDong = 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_SanPham_TheoWebsite_HinhThucQuangCao_Banner'
	IF(@isWeb > 0 AND @isHinhThucQuangCao = 0 AND @isBanner > 0 AND @isHopDong > 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham_Website_Banner'
	IF(@isWeb > 0 AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isHopDong > 0 AND @isKhachHang > 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham_Website' -- do hop dong co khach hang
		
	IF(@isWeb = 0 AND @isHinhThucQuangCao > 0 AND @isBanner > 0 AND @isHopDong > 0 AND @isKhachHang = 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham_HinhThucQuangCao_Banner' 
	IF(@isWeb = 0 AND @isHinhThucQuangCao > 0 AND @isBanner = 0 AND @isHopDong > 0 AND @isKhachHang > 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham_HinhThucQuangCao' -- do hop dong co khach hang
	IF(@isWeb = 0 AND @isHinhThucQuangCao = 0 AND @isBanner > 0 AND @isHopDong > 0 AND @isKhachHang > 0)
		SET @result = 'rptThucChay_HopDong_TheoSanPham_Banner' -- do hop dong co khach hang
	RETURN @result

END

```
