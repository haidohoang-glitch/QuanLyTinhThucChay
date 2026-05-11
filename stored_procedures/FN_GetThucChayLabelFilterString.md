# Function: `GetThucChayLabelFilterString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-23 17:34:10.437000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.140000

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
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomlamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |
| `@DmHinhThucQuangCaoREFList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@TenNhanHangList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql

-- =============================================
--PRINT [dbo].[GetThucChayFilterString]
--(
-- --@StartDate = 
-- '2013-08-01',
-- --@EndDate = 
-- '2013-09-15',
-- --@DmSanPhamREFList = 
-- N'',
-- --@DmWebsiteREFList =
--  N'',
-- --@SoHopDongList = 
-- N'',
-- --@DmPhongBanREFList = 
-- N'',
-- --@DmBoPhanREFList = 
-- N'',
-- --@DmNhomLamViecREFList = 
-- N'',
-- --@TenNhanVienList = 
-- N'',
-- --@TenDangNhap = 
-- 'doanluan',
-- '3',
-- '',
-- '',
-- '6'
-- )


CREATE FUNCTION [dbo].[GetThucChayLabelFilterString]
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
	@TenDangNhap NVARCHAR(50),
	@DmPhongBanREF int,
	@DmBoPhanREF int,
	@DmNhomlamViecREF int,
	@DmChucDanhREF INT,
	@DmHinhThucQuangCaoREFList NVARCHAR(200),
	@DmBannerREFList NVARCHAR(200),
	@TenNhanHangList NVARCHAR(200)
)
RETURNS nvarchar(4000)
AS
BEGIN	

	Declare @DauNhay nvarchar(50)
	Declare @FilterSQLCommand nvarchar(4000)
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT
	DECLARE @ListWebsiteID nvarchar(200), @ListSanPhamID nvarchar(200), @ListTenNhanVien nvarchar(2000)
	DECLARE @ToUserName NVARCHAR(50), @ToanTu nvarchar(50)
	DECLARE @IsWebsiteManager INT;
	DECLARE @CurrentYear NVARCHAR(50);
	
	SET @CurrentYear = CONVERT(NVARCHAR(50), YEAR(GETDATE()));
	
	set @DauNhay = ''''

	
	set @FilterSQLCommand = 'CONVERT(DATE,tcdt.NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' 
and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
				
	--Set quyen theo dieu kien tim kiem	
	if(@DmSanPhamREFList IS NOT NULL AND @DmSanPhamREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and tcdt.DmSanPhamREF in (' + @DmSanPhamREFList + ')'
		
	if(@DmWebsiteREFList IS NOT NULL AND @DmWebsiteREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and tcdt.DmWebsiteREF in (' + @DmWebsiteREFList + ')'
						
	if(@SoHopDongList IS NOT NULL AND @SoHopDongList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and tcdt.SoHopDong in (' + @SoHopDongList + ')'		
				
	if(@DmPhongBanREFList IS NOT NULL AND @DmPhongBanREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and tcdt.DmPhongBanREF in (' + @DmPhongBanREFList + ')' 
		
	if(@DmBoPhanREFList IS NOT NULL AND @DmBoPhanREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and tcdt.DmBoPhanREF in (' + @DmBoPhanREFList + ')' 
		
	if(@DmNhomLamViecREFList IS NOT NULL AND @DmNhomLamViecREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and tcdt.DmNhomLamViecREF in (' + @DmNhomLamViecREFList + ')'
		
	IF(@TenNhanVienList IS NOT NULL AND @TenNhanVienList <> '')
		SET @FilterSQLCommand += ' AND tcdt.TenDangNhap IN (' + @TenNhanVienList + ')'
		
	IF(@DmHinhThucQuangCaoREFList IS NOT NULL AND @DmHinhThucQuangCaoREFList <> '' AND @DmHinhThucQuangCaoREFList <> '-1')
		SET @FilterSQLCommand += ' AND tcdt.DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoREFList + ')'
		
	IF (@DmBannerREFList IS NOT NULL AND @DmBannerREFList <> '' )
		SET @FilterSQLCommand += ' AND tcdt.DmViTriREF IN (' + @DmBannerREFList + ')'
			
	-- Kiểm tra Admin trong bảng AdminGroup
	-- 2, 34			Admin Thực chạy
	-- 106				thunguyenthi
	-- 103 ,151 ,152	Quản lý nhãn
	DECLARE @IsViewAll INT
	SET @IsViewAll = (SELECT COUNT(au.OxUserREF) 
	                  FROM AdminGroupUser agu JOIN AdminUser au
					  ON agu.AdminUserId = au.AdminUserId
					  WHERE agu.AdminGroupID IN (2, 34, 106, 103 ,151 ,152) AND au.Username = @TenDangNhap)			
		  						
		
	IF (@TenNhanHangList IS NULL OR @TenNhanHangList = '')
		BEGIN			
			IF(@IsViewAll = 0)
				BEGIN
					SET @FilterSQLCommand += ' AND dbo.ReplaceStringEmpty(hd.NhanHopDong) IN 
												(SELECT dbo.ReplaceStringEmpty
(dnh.TenNhanHang) FROM PhanQuyenNhanHang pqnh
													INNER JOIN AdminUser au ON 
pqnh.OxUserREF = au.OxUserREF
													INNER JOIN DmNhanHang dnh ON 
dnh.DmNhanHangID = pqnh.DmNhanHangREF
													WHERE 
													au.Username = ' + @DauNhay + 
@TenDangNhap + @DauNhay + ')'		
				END							
		END
		
	IF (@TenNhanHangList IS NOT NULL AND @TenNhanHangList <> '')
		SET @FilterSQLCommand += ' AND dbo.ReplaceStringEmpty(hd.NhanHopDong) IN (' + @TenNhanHangList + ')'	 	
	
	-- Return the result of the function
			
	-- Fix quyen account cua Nguyen Thi Thu chi duoc xem hop dong noi bo
	--IF @TenDangNhap = 'thunguyenthi'
	--	SET @FilterSQLCommand += ' AND UPPER(TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay
	
	RETURN @FilterSQLCommand
END

```
