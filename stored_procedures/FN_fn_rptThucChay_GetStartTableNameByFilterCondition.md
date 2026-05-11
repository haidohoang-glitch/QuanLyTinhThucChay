# Function: `fn_rptThucChay_GetStartTableNameByFilterCondition`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:43:42.833000
- **Ngày sửa cuối**: 2015-03-27 17:43:42.833000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(400)` | Yes |
| `@Type` | `nvarchar(4)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@GroupFieldName` | `nvarchar(1000)` | No |
| `@sHopDong` | `nvarchar(1000)` | No |
| `@sHinhThucQuangCao` | `nvarchar(1000)` | No |
| `@sSanPham` | `nvarchar(1000)` | No |
| `@sWebsite` | `nvarchar(1000)` | No |
| `@sBanner` | `nvarchar(1000)` | No |
| `@ListWebsiteSecurity` | `nvarchar(1000)` | No |
| `@ListSanPhamSecurity` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[fn_rptThucChay_GetStartTableNameByFilterCondition]
(
	-- Add the parameters for the function here
	@Type					NVARCHAR(2),
	@TenDangNhap			NVARCHAR(50),
	@GroupFieldName			NVARCHAR(500),
	@sHopDong				nvarchar(500),
	@sHinhThucQuangCao		nvarchar(500),
	@sSanPham				nvarchar(500),
	@sWebsite				nvarchar(500),
	@sBanner				nvarchar(500),
	@ListWebsiteSecurity    NVARCHAR(500),
	@ListSanPhamSecurity    NVARCHAR(500)
)
RETURNS NVARCHAR(200)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @StartTableName NVARCHAR(200)
	DECLARE @isHopDong INT SET @isHopDong =0
	DECLARE @isHinhThucQuangCao INT SET @isHinhThucQuangCao =0
	DECLARE @isSanPham INT SET @isSanPham =0
	DECLARE @isWebsite INT SET @isWebsite =0
	DECLARE @isBanner INT SET @isBanner =0
	DECLARE @isKhachHang INT SET @isKhachHang =0
	------------------------------------------------
	IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @isSanPham = 1
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENWEBSITE'
	Begin
		SET @isWebsite = 1
	End
	ELSE IF UPPER(@GroupFieldName) = 'SOHOPDONG'
	Begin
		SET @isHopDong = 1
	END
	
	------------------------------------------------
	IF @sHopDong <>'' SET @isHopDong =1
	IF @sHinhThucQuangCao <>'' SET @isHinhThucQuangCao =1
	IF @sSanPham <>'' or @ListSanPhamSecurity <>''  SET @isSanPham =1
	IF @sWebsite <>'' or @ListWebsiteSecurity<>'' SET @isWebsite =1
	IF @sBanner <>'' SET @isBanner =1
	IF (SELECT COUNT(*) FROM rptThucChay_Security WHERE TenDangNhap = @TenDangNhap AND isnull(isKhachHang,0) =1)>0 SET @isKhachHang =1
	-- Add the T-SQL statements to compute the return value here
	IF @Type ='01'-- Bao cao thuc chay tong hop theo san pham
	BEGIN
		IF @isHopDong =0 AND @isHinhThucQuangCao =0 AND @isWebsite = 0 AND @isBanner = 0 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_SanPham'
		ELSE
		IF @isHopDong =1 AND @isHinhThucQuangCao =0 AND @isWebsite = 0 AND @isBanner = 0 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_HopDong_TheoSanPham'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =1 AND @isWebsite = 0 AND @isBanner = 0 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_HinhThucQuangCao_TheoSanPham'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =0 AND @isWebsite = 1 AND @isBanner = 0 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_SanPham_TheoWebsite'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =0 AND @isWebsite = 0 AND @isBanner = 1 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_SanPham_TheoTenViTriBanner'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =0 AND @isWebsite = 0 AND @isBanner = 0 AND @isKhachHang = 1
		   SET @StartTableName = 'rptThucChay_KhachHang_TheoSanPham'
		ELSE
		IF @isHopDong =1 AND @isHinhThucQuangCao =1 AND @isWebsite = 0 AND @isBanner = 0 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_HopDong_TheoHinhThucQuangCao_SanPham'
		ELSE
		IF @isHopDong =1 AND @isHinhThucQuangCao =0 AND @isWebsite = 1 AND @isBanner = 0 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_HopDong_TheoSanPham_Website'
		ELSE
		IF @isHopDong =1 AND @isHinhThucQuangCao =0 AND @isWebsite = 0 AND @isBanner = 1 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_HopDong_TheoSanPham_Banner'
		ELSE
		IF @isHopDong =1 AND @isHinhThucQuangCao =0 AND @isWebsite = 0 AND @isBanner = 0 AND @isKhachHang = 1
		   SET @StartTableName = 'rptThucChay_HopDong_TheoSanPham'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =1 AND @isWebsite = 1 AND @isBanner = 0 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_HinhThucQuangCao_TheoSanPham_Website'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =1 AND @isWebsite = 0 AND @isBanner = 1 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =1 AND @isWebsite = 0 AND @isBanner = 0 AND @isKhachHang = 1
		   SET @StartTableName = 'rptThucChay_KhachHang_TheoHinhThucQuangCao_SanPham'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =0 AND @isWebsite = 1 AND @isBanner = 1 AND @isKhachHang = 0
		   SET @StartTableName = 'rptThucChay_SanPham_TheoWebsite_ViTriBanner'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =0 AND @isWebsite = 1 AND @isBanner = 0 AND @isKhachHang = 1
		   SET @StartTableName = 'rptThucChay_HopDong_TheoSanPham_Website'
		ELSE
		IF @isHopDong =0 AND @isHinhThucQuangCao =0 AND @isWebsite = 0 AND @isBanner = 1 AND @isKhachHang = 1
		   SET @StartTableName = 'rptThucChay_HopDong_TheoSanPham_ViTriBanner'
		ELSE 
			SET  @StartTableName = 'rptThucChay_BaoCaoTongHopTheoWebsite'
	END
	IF @Type ='02' -- Bao cao tong hop thuc chay theo website
	BEGIN
		IF @isHopDong =0 AND @isSanPham = 0 AND @isKhachHang = 0
			SET @StartTableName ='rptThucChay_Website'
		ELSE
		IF @isHopDong = 1 AND @isSanPham = 0 AND @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoWebsite'
		ELSE
		IF @isHopDong =0 AND @isSanPham = 1 AND @isKhachHang = 0
			SET @StartTableName ='rptThucChay_SanPham_TheoWebsite'
		ELSE
		IF @isHopDong =0 AND @isSanPham = 0 AND @isKhachHang = 1
			SET @StartTableName ='rptThucChay_KhachHang_TheoWebsite'
		ELSE
		IF @isHopDong =1 AND @isSanPham = 1 AND @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
		ELSE
		IF @isHopDong =1 AND @isSanPham = 0 AND @isKhachHang = 1
			SET @StartTableName ='rptThucChay_HopDong_TheoWebsite'
		ELSE
		IF @isHopDong =0 AND @isSanPham = 1 AND @isKhachHang = 1
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
		ELSE
		IF @isHopDong =1 AND @isSanPham = 1 AND @isKhachHang = 1
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
		ELSE 
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
	END
	IF @Type ='03' -- bao cao tong hop thuc chay theo hop dong
	BEGIN 
		IF @isHinhThucQuangCao = 0 AND @isSanPham = 0 AND @isWebsite = 0 AND @isbanner = 0
			SET @StartTableName ='rptThucChay_HopDong'
		--ELSE
		--IF @isHinhThucQuangCao = 1 AND @isSanPham = 0 AND @isWebsite = 0 AND @isbanner = 0
		--	SET @StartTableName ='rptThucChay_HopDong_TheoHinhThucQuangCao'
		--ELSE
		--IF @isHinhThucQuangCao = 0 AND @isSanPham = 1 AND @isWebsite = 0 AND @isbanner = 0
		--	SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
		--ELSE
		--IF @isHinhThucQuangCao = 0 AND @isSanPham = 0 AND @isWebsite = 1 AND @isbanner = 0
		--	SET @StartTableName ='rptThucChay_HopDong_TheoWebsite'
		--ELSE
		--IF @isHinhThucQuangCao = 0 AND @isSanPham = 0 AND @isWebsite = 0 AND @isbanner = 1
		--	SET @StartTableName ='rptThucChay_HopDong_TheoViTriBanner'
			
		--ELSE
		--IF @isHinhThucQuangCao = 1 AND @isSanPham = 1 AND @isWebsite = 0 AND @isbanner = 0
		--	SET @StartTableName ='rptThucChay_HopDong_TheoHinhThucQuangCao_SanPham'
		--ELSE
		--IF @isHinhThucQuangCao = 0 AND @isSanPham = 1 AND @isWebsite = 1 AND @isbanner = 0
		--	SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
		--ELSE
		--IF @isHinhThucQuangCao = 0 AND @isSanPham = 1 AND @isWebsite = 0 AND @isbanner = 1
		--	SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_ViTriBanner'
		--ELSE 
			SET @StartTableName ='rptThucChay_BaoCaoTongHopTheoHopDong'
		
	END
	IF @Type ='04' -- bao cao tong hop thuc chay theo phong ban,Bo phan, nhom lam viec
	BEGIN
		if @isHopDong = 0 and @isSanPham = 0 and @isWebsite = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_DoiBan'
		ELSE
		if @isHopDong = 1 and @isSanPham = 0 and @isWebsite = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
		ELSE
		if @isHopDong = 0 and @isSanPham = 1 and @isWebsite = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_SanPham'
		ELSE
		if @isHopDong = 0 and @isSanPham = 0 and @isWebsite = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_Website'
		ELSE
		if @isHopDong = 0 and @isSanPham = 0 and @isWebsite = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_KhachHang'
		ELSE
		if @isHopDong = 1 and @isSanPham = 1 and @isWebsite = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
		ELSE
		if @isHopDong = 1 and @isSanPham = 0 and @isWebsite = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoWebsite'
		ELSE
		if @isHopDong = 1 and @isSanPham = 0 and @isWebsite = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
		ELSE
		if @isHopDong = 0 and @isSanPham = 1 and @isWebsite = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_SanPham_TheoWebsite'
		ELSE
		if @isHopDong = 0 and @isSanPham = 1 and @isWebsite = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_KhachHang_TheoSanPham'
		ELSE
		if @isHopDong = 0 and @isSanPham = 0 and @isWebsite = 1 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_KhachHang_TheoWebsite'
		ELSE
		if @isHopDong = 1 and @isSanPham = 1 and @isWebsite = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
		ELSE
		if @isHopDong = 1 and @isSanPham = 1 and @isWebsite = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
		ELSE
		if @isHopDong = 1 and @isSanPham = 0 and @isWebsite = 1 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_HopDong_TheoWebsite'
		ELSE
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
	END
	IF @Type ='05' -- bao cao tong hop thuc chay theo nhan vien
	BEGIN
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_NhanVien'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 1 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HinhThucQuangCao'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_SanPham'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 1 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_Website'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_TenViTriBanner'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_KhachHang'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 1 and @isSanPham = 1 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HinhThucQuangCao_TheoSanPham'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 1 and @isSanPham = 0 and @isWebsite = 1 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HinhThucQuangCao_TheoSanPham_Website'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 1 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 1 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_KhachHang_TheoHinhThucQuangCao'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 1 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_SanPham_TheoWebsite'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 0 and @isBanner = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_SanPham_TheoTenViTriBanner'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_KhachHang_TheoSanPham'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 1 and @isBanner = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_KhachHang_TheoWebsite'
		ELSE
		if @isHopDong = 0 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 1 and @isBanner = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_SanPham_TheoWebsite_ViTriBanner'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 1 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HoDong_TheohinhThucQuangCao'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDongTheoSanPham'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 1 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoWebsite'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoViTriBanner'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 0 and @isSanPham = 0 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 1 and @isSanPham = 1 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoHinhThucQuangCao_SanPham'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 1 and @isBanner = 0 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 0 and @isBanner = 1 and @isKhachHang = 0
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_ViTriBanner'
		ELSE
		if @isHopDong = 1 and @isHinhThucQuangCao = 0 and @isSanPham = 1 and @isWebsite = 0 and @isBanner = 0 and @isKhachHang = 1
			SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
		ELSE
			SET @StartTableName ='rptThucChay_BaoCaoTongHopTheoWebsite'
	END
    IF @Type = '06'-- bao cao chi tiet theo khach hang
    BEGIN
    	IF @isHopDong = 0  AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isSanPham = 0 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_KhachHang'
    	ELSE
    	IF @isHopDong = 1  AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isSanPham = 0 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong'
    	else
    	IF @isHopDong = 0  AND @isHinhThucQuangCao = 1 AND @isBanner = 0 AND @isSanPham = 0 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_KhachHang_TheoHinhThucQuangCao'
    	else
    	IF @isHopDong = 0  AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isSanPham = 1 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_KhachHang_TheoSanPham'
    	else
    	IF @isHopDong = 0  AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isSanPham = 0 AND @isWebsite =1
    		SET @StartTableName ='rptThucChay_KhachHang_TheoWebsite'
    	else
    	IF @isHopDong = 0  AND @isHinhThucQuangCao = 0 AND @isBanner = 1 AND @isSanPham = 0 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong_TheoViTriBanner'
    	else
    	IF @isHopDong = 1  AND @isHinhThucQuangCao = 1 AND @isBanner = 0 AND @isSanPham = 0 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong_TheoHinhThucQuangCao'
    	else
    	IF @isHopDong = 1 AND @isHinhThucQuangCao = 0 AND @isBanner = 1 AND @isSanPham = 0 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong_TheoViTriBanner'
    	else
    	IF @isHopDong = 1  AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isSanPham = 1 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong_TheoSanPham'
    	else
    	IF @isHopDong = 1  AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isSanPham = 0 AND @isWebsite =1
    		SET @StartTableName ='rptThucChay_HopDong_TheoWebsite'
    	else
    	IF @isHopDong = 0  AND @isHinhThucQuangCao = 1 AND @isBanner = 0 AND @isSanPham = 1 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong_TheoHinhThucQuangCao_SanPham'
    	else
    	IF @isHopDong = 0  AND @isHinhThucQuangCao = 0 AND @isBanner = 1 AND @isSanPham = 1 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_ViTriBanner'
    	else
    	IF @isHopDong = 0  AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isSanPham = 1 AND @isWebsite =1
    		SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
    	else
    	IF @isHopDong = 1  AND @isHinhThucQuangCao = 1 AND @isBanner = 0 AND @isSanPham = 1 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong_TheoHinhThucQuangCao_SanPham'
    	else
    	IF @isHopDong = 1  AND @isHinhThucQuangCao = 0 AND @isBanner = 1 AND @isSanPham = 1 AND @isWebsite =0 
    		SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_ViTriBanner'
    	else
    	IF @isHopDong = 1  AND @isHinhThucQuangCao = 0 AND @isBanner = 0 AND @isSanPham = 1 AND @isWebsite =1
    		SET @StartTableName ='rptThucChay_HopDong_TheoSanPham_Website'
    	ELSE SET @StartTableName ='rptThucChay_BaoCaoTongHopTheoWebsite'
    	
    END
	-- Return the result of the function
	RETURN @StartTableName
END

```
