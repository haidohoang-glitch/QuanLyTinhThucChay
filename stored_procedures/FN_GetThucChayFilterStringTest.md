# Function: `GetThucChayFilterStringTest`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-13 14:54:20.397000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.173000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

-- =============================================
CREATE FUNCTION [dbo].[GetThucChayFilterStringTest]
(
	-- Add the parameters for the function here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@TenDangNhap NVARCHAR(50)
)
RETURNS nvarchar(4000)
AS

BEGIN	
	Declare @DauNhay nvarchar(50)
	Declare @FilterSQLCommand nvarchar(4000)
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT
	DECLARE @ListWebsiteID nvarchar(200), @ListSanPhamID nvarchar(200)
	DECLARE @ToUserName NVARCHAR(50)
	
	set @DauNhay = ''''
	
	SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName 
	
	SET @ChucDanhID = dbo.NhanSuGetChucDanhByNhanVien(@TenDangNhap)
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	SET @ListWebsiteID = dbo.GetListWebsiteByNhanVien(@TenDangNhap)
	SET @ListSanPhamID = dbo.GetListSanPhamByNhanVien(@TenDangNhap) 
	
	IF @GroupPermission <> -1
	BEGIN
		IF @DmSanPhamREFList = '' 
		SET @DmSanPhamREFList = dbo.GetListSanPhamByNhanVien(@TenDangNhap)
		
		IF @DmWebsiteREFList = ''
			SET @DmWebsiteREFList = dbo.GetListWebsiteByNhanVien(@TenDangNhap)
			
		--IF @DmPhongBanREFList = ''
		--	SET @DmPhongBanREFList = dbo.NhanSuGetPhongByNhanVien(@TenDangNhap)
			
		--IF @DmBoPhanREFList = ''
		--	SET @DmBoPhanREFList = dbo.NhanSuGetBoPhanByNhanVien(@TenDangNhap)
			
		--IF @DmNhomLamViecREFList = ''
		--	SET @DmNhomLamViecREFList = dbo.NhanSuGetNhomLamViecByNhanVien(@TenDangNhap)
		
		IF (@TenNhanVienList = '')
		BEGIN
			IF dbo.Fn_NhanSu_GetListNhanVienByChucDanh(@TenDangNhap) IS NULL
				SET	@TenNhanVienList = @TenDangNhap
			ELSE
				SET @TenNhanVienList = dbo.Fn_NhanSu_GetListNhanVienByChucDanh(@TenDangNhap)
		END
	END

	set @FilterSQLCommand = ' and CONVERT(DATE,NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
	if(@DmSanPhamREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmSanPhamREF in (' + @DmSanPhamREFList + ')'
	--if(@DmWebsiteREFList <> '')
	--	set @FilterSQLCommand = @FilterSQLCommand + ' and DmWebsiteREF in (' + @DmWebsiteREFList + ')'
	if(@SoHopDongList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and SoHopDong in (' + @SoHopDongList + ')'
	if(@DmPhongBanREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmPhongBanREF in (' + @DmPhongBanREFList + ')' 
	if(@DmBoPhanREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmBoPhanREF in (' + @DmBoPhanREFList + ')' 
	if(@DmNhomLamViecREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmNhomLamViecREF in (' + @DmNhomLamViecREFList + ')'
		
	--if(@TenNhanVienList <> '' AND @ListWebsiteID = '' AND @ListSanPhamID = '')
	--	set @FilterSQLCommand = @FilterSQLCommand + ' and 1=1 and TenDangNhap in (' + @TenNhanVienList + ')'
	
	--ELSE IF (@TenNhanVienList <> '' AND @ListWebsiteID <> '')
	--	SET @FilterSQLCommand = @FilterSQLCommand + ' and 2=2 AND DmWebsiteREF IN (' +  @DmWebsiteREFList + ')'
		
	--ELSE IF (@TenNhanVienList <> '')
	--	SET @FilterSQLCommand = @FilterSQLCommand + ' and 5=5 AND DmWebsiteREF IN (' +  @DmWebsiteREFList + ')' 
		
	IF @TenNhanVienList <> ''
	BEGIN
		IF @ListWebsiteID = '' AND @ListSanPhamID = ''
			SET @FilterSQLCommand = @FilterSQLCommand + ' and 1=1 and TenDangNhap in (' + @TenNhanVienList + ')'
		ELSE IF (@ListWebsiteID <> '' AND (@ChucDanhID = 1 OR @ChucDanhID = 3 OR @ChucDanhID = 6 OR @ChucDanhID = 7))
			SET @FilterSQLCommand = @FilterSQLCommand + ' and 3=3 AND (DmWebsiteREF IN (' +  @DmWebsiteREFList + ') OR TenDangNhap IN (' + @TenNhanVienList + '))' 
		ELSE IF @ListWebsiteID <> '' AND @ChucDanhID <> 1 AND @ChucDanhID <> 3 AND @ChucDanhID <> 6 AND @ChucDanhID <> 7
			SET @FilterSQLCommand = @FilterSQLCommand + ' and 2=2 AND DmWebsiteREF IN (' +  @DmWebsiteREFList + ')'
		ELSE IF @ListWebsiteID <> ''
			SET @FilterSQLCommand = @FilterSQLCommand + ' and 5=5 AND DmWebsiteREF IN (' +  @DmWebsiteREFList + ')'
	END

	IF(@TenNhanVienList = '')
	BEGIN
		IF (@ListWebsiteID <> '' AND (@ChucDanhID = 1 OR @ChucDanhID = 3 OR @ChucDanhID = 6 OR @ChucDanhID = 7))
		BEGIN
			SET @TenNhanVienList = dbo.Fn_NhanSu_GetListNhanVienByChucDanh(@TenDangNhap)
			SET @FilterSQLCommand = @FilterSQLCommand + ' and 3=3 AND (DmWebsiteREF IN (' +  @DmWebsiteREFList + ') OR TenDangNhap IN (' + @TenNhanVienList + '))' 
		END
		ELSE IF (@ListWebsiteID <> '' AND (@ChucDanhID <> 1 AND @ChucDanhID <> 3 OR @ChucDanhID <> 6 OR @ChucDanhID <> 7))
			SET @FilterSQLCommand = @FilterSQLCommand + ' and 4=4 AND DmWebsiteREF IN (' +  @DmWebsiteREFList + ')' 
	END	
	
	if(@DmWebsiteREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmWebsiteREF in (' + @DmWebsiteREFList + ')'

	-- Return the result of the function
	RETURN @FilterSQLCommand

END

```
