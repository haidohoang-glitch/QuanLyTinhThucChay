# Function: `GetThucChayFilterString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 05:36:07.610000
- **Ngày sửa cuối**: 2015-07-17 14:40:40.690000

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


CREATE FUNCTION [dbo].[GetThucChayFilterString]
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
	@DmBannerREFList NVARCHAR(200)
)
RETURNS nvarchar(4000)
AS
BEGIN	

	Declare @DauNhay			nvarchar(50)
	Declare @FilterSQLCommand	nvarchar(4000)
	DECLARE @ChucDanhID			INT
	DECLARE @GroupPermission	INT;
	DECLARE @PhongID			INT, 
			@BoPhanID			INT, 
			@NhomLamViecID		INT;
			
	DECLARE @ListWebsiteID		nvarchar(200), 
			@ListSanPhamID		nvarchar(200), 
			@ListTenNhanVien	nvarchar(2000)
	DECLARE @ToUserName			NVARCHAR(50), 
			@ToanTu				nvarchar(50)
			
	DECLARE @IsWebsiteManager	INT;
	DECLARE @CurrentYear		NVARCHAR(50);
	
	DECLARE @StarDateActive		NVARCHAR(50),
			@EndDateActive		NVARCHAR(50);
	
	--SET @CurrentYear = CONVERT(NVARCHAR(50), YEAR(GETDATE()));
	
	set @DauNhay = ''''

	
	set @FilterSQLCommand = 'CONVERT(DATE,NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
	IF(EXISTS(SELECT abpw.DmWebsiteREF
	            FROM AdminBoPhanWebsite AS abpw 
	          WHERE abpw.TenDangNhap = @TenDangNhap AND abpw.DmWebsiteREF > 0) AND 
		NOT EXISTS(SELECT apu.UserName
		             FROM AdminPermistionUsers AS apu WHERE apu.UserName = @TenDangNhap))
		BEGIN
			SET @IsWebsiteManager = 1;	
			SET @CurrentYear = (SELECT NamThucChay FROM ThucChayConfiguration WHERE RecordStatus = 1 AND DeletedStatus = 0);
			SET @FilterSQLCommand = @FilterSQLCommand + ' AND Year(NgayThucHien) >= ' + @CurrentYear + ' '; 
		END
				
	--Set quyen theo dieu kien tim kiem	
	if(@DmSanPhamREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmSanPhamREF in (' + @DmSanPhamREFList + ')'
	if(@DmWebsiteREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmWebsiteREF in (' + @DmWebsiteREFList + ')'				
	if(@SoHopDongList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and SoHopDong in (' + @SoHopDongList + ')'
	if(@DmPhongBanREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmPhongBanREF in (' + @DmPhongBanREFList + ')' 
	if(@DmBoPhanREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmBoPhanREF in (' + @DmBoPhanREFList + ')' 
	if(@DmNhomLamViecREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmNhomLamViecREF in (' + @DmNhomLamViecREFList + ')'
		
	IF @TenNhanVienList <> ''
		SET @FilterSQLCommand += ' AND TenDangNhap IN (' + @TenNhanVienList + ')'
		
	IF	(@DmHinhThucQuangCaoREFList <> '' AND @DmHinhThucQuangCaoREFList <> '-1')
		SET @FilterSQLCommand += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoREFList + ')'
		
	IF (@DmBannerREFList <> '' )
		SET @FilterSQLCommand += ' AND DmViTriREF IN (' + @DmBannerREFList + ')'
		
	
	-- Phan quyen cho nhung account xem du lieu thuc chay trong khoang thooi gian nhat dinh
	
	IF EXISTS(SELECT UserName FROM AdminPermisionUsersByTime A WHERE A.UserName = @TenDangNhap AND A.RecordStatus = 1)
	BEGIN
		SELECT 
			@StarDateActive = CONVERT(NVARCHAR(50),StartDateActive),
			@EndDateActive  = CONVERT(NVARCHAR(50),EndDateActive)
		FROM AdminPermisionUsersByTime
		WHERE 
			UserName			= @TenDangNhap
			AND RecordStatus	= 1
		
		SET @FilterSQLCommand += ' AND NgayThucHien BETWEEN ' + @DauNhay + @StarDateActive + @DauNhay +
													' AND ' + @DauNhay + @EndDateActive + @DauNhay
	END
	
	RETURN @FilterSQLCommand

END
```
