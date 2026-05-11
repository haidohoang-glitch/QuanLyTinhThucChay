# Stored Procedure: `DuyetDuLieuTheoSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-07 08:23:56.440000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.150000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `int(4)` | No |
| `@IsPheDuyet` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DonViTinhList` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@DmWebsiteREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-03
-- Description:	Duyet du lieu theo san pham
-- =============================================
-- exec dbo.DuyetDuLieuTheoSanPham 
-- @StartDate = '2013-10-01',
-- @EndDate = '2013-10-15'
-- @DmSanPhamREFList = '339',
-- @TenDangNhap = 'thunguyenthi',
-- @IsNoiBo = 1

CREATE PROCEDURE [dbo].[DuyetDuLieuTheoSanPham] 
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList INT,
	@IsPheDuyet INT,
	@TenDangNhap nvarchar(50),
	@IsNoiBo INT,
	@DonViTinhList NVARCHAR(50),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList NVARCHAR(200),
	@DmWebsiteREFList	NVARCHAR(200)	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Sql NVARCHAR(MAX);
    DECLARE @DauNhay NVARCHAR(50);
    Declare @GroupByFildID nvarchar(4000);
	Declare @GroupByFild nvarchar(4000);
	Declare @FilterString nvarchar(4000) = '';
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand varchar(MAX)
	DECLARE @Count int
	DECLARE @QuaTrinhCongTacTemp TABLE
	(
	  NhanSuID int, 
	  PhongBanREF INT,
	  BoPhanREF INT,
	  NhomLamViecREF INT,
	  ChucDanhREF INT,
	  TuNgay DATETIME,
	  DenNgay DATETIME
	)
	DECLARE @ToUserName NVARCHAR(50)
	
	DECLARE @OrderByField NVARCHAR(50)
	DECLARE @Function NVARCHAR(50)
	
	DECLARE @Pamrams NVARCHAR(MAX);
		
	SET @Pamrams = N'@StartDateParam				datetime,
					@EndDateParam					datetime,
					@DmSanPhamREFListParam			INT,
					@IsPheDuyetParam				INT,
					@TenDangNhapParam				nvarchar(50),
					@IsNoiBoParam					INT,
					@DonViTinhListParam				NVARCHAR(50),
					@DmHinhThucQuangCaoListParam	NVARCHAR(200),
					@DmBannerREFListParam			NVARCHAR(200),
					@DmWebsiteREFListParam			NVARCHAR(200)'
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName
		
	IF @IsNoiBo = 1
		SET @FilterString += '' 
	ELSE IF (@IsNoiBo = 0 AND @DmSanPhamREFList <> 144)
		SET @FilterString += ' AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
		
	SET @FilterString = @FilterString + ' AND CONVERT(DATE,NgayThucHien) BETWEEN ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
	SET @FilterString += ' AND DmSanPhamREF = ' + CONVERT(NVARCHAR(50),@DmSanPhamREFList) + ''
	
	IF (@DmSanPhamREFList <> 144 AND @DonViTinhList <> '')
		SET @FilterString += ' AND dbo.FormatDonViTinh(DonViTinh) IN (' + UPPER(@DonViTinhList) + ')'
	
	IF (@DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1')
		SET @FilterString += ' AND DmHinhThucQuangCao IN (' + @DauNhay + @DmHinhThucQuangCaoList + @DauNhay + ')';
		
	IF @DmBannerREFList <> '' 
		SET @FilterString += ' AND DmViTriREF IN (' + @DauNhay + @DmBannerREFList + @DauNhay + ')'
		
	IF @DmWebsiteREFList <> ''
		SET @FilterString += ' AND DmWebsiteREF IN (' + @DmWebsiteREFList + ')'
	
	IF @DmSanPhamREFList <> 144
		SET @Sql = '
			UPDATE ThucChayDaTinh
			SET 
				IsPheDuyet = ' + CONVERT(varchar(10),@IsPheDuyet) + ',
				PheDuyetBy = ' + @DauNhay + @TenDangNhap + @DauNhay + ',
				PheDuyetAt = GETDATE()	
			WHERE 1=1 ' + @FilterString
	ELSE -- For CPC Admarket
		SET @Sql = '
			UPDATE ThucChayAdmarketPublisher
			SET 
				IsPheDuyet = ' + CONVERT(varchar(10),@IsPheDuyet) + ',
				PheDuyetBy = ' + @DauNhay + @TenDangNhap + @DauNhay + ',
				PheDuyetAt = GETDATE()	
			WHERE 1=1 ' + @FilterString
	
	PRINT @FilterString;	
	PRINT @Sql;
	
	EXECUTE sp_executesql @Sql, @Pamrams,
		@StartDateParam					= @StartDate,
		@EndDateParam					= @EndDate,
		@DmSanPhamREFListParam			= @DmSanPhamREFList,
		@IsPheDuyetParam				= @IsPheDuyet,
		@TenDangNhapParam				= @TenDangNhap,
		@IsNoiBoParam					= @IsNoiBo,
		@DonViTinhListParam				= @DonViTinhList,
		@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
		@DmBannerREFListParam			= @DmBannerREFList,
		@DmWebsiteREFListParam			= @DmWebsiteREFList
	
	-- Cho Log action nguoi dung
	DECLARE @LogTime						DATETIME
			,@TenBaoCao						NVARCHAR(512)
			,@SoHopDongList					NVARCHAR(2000) = ''
			,@DmPhongBanREFList				NVARCHAR(2000) = ''
			,@DmBoPhanREFList				NVARCHAR(2000) = ''
			,@DmNhomLamViecREFList			NVARCHAR(2000) = ''
			,@TenNhanVienList				NVARCHAR(2000) = ''
			,@KhachHangREF					NVARCHAR(512)  = ''
			,@NhanHang						NVARCHAR(4000) = ''
			,@DmNhomNganhREF				NVARCHAR(2000) = ''
			,@TongViewThucChayNoiBo			BIGINT
			,@TongClickThucChayNoiBo		BIGINT
			,@TongSoBaiVietNoiBo			BIGINT
			,@TongSoNgayChayNoiBo			BIGINT
			,@TongViewThucChayKhuyenMai		BIGINT
			,@TongClickThucChayKhuyenMai	BIGINT
			,@TongSoBaiVietKhuyenMai		BIGINT
			,@TongSoNgayChayKhuyenMai		BIGINT
			,@TongViewThucChay				BIGINT
			,@TongClickThucChay				BIGINT
			,@TongSoBaiViet					BIGINT
			,@TongSoNgayChay				BIGINT
			,@TongTienKhuyemMai				FLOAT
			,@TongTienNoiBo					FLOAT
			,@TongTienThucChaySauCK			FLOAT
			,@TongGiaTriThayDoi				FLOAT
			--,@IsPheDuyet					INT				= 0
			,@PheDuyetAt					DATETIME
			,@PheDuyetBy					NVARCHAR(50)
			
	SET @TenBaoCao = N'Duyệt dữ liệu theo sản phẩm'
		
	-- Lay So luong theo don vi tinh Click
	SELECT  @TongClickThucChayNoiBo		= 0,
			@TongClickThucChayKhuyenMai = 0,
			@TongClickThucChay			= 0,
			
			@TongViewThucChayNoiBo		= 0,
			@TongViewThucChayKhuyenMai  = 0,
			@TongViewThucChay			= 0,
			
			@TongSoNgayChayNoiBo		= 0,
			@TongSoNgayChayKhuyenMai	= 0,
			@TongSoNgayChay				= 0,
			
			@TongSoBaiVietNoiBo		= 0,
			@TongSoBaiVietKhuyenMai = 0,
			@TongSoBaiViet			= 0
	
	-- Lay Thanh tien thuc chay
	SELECT  
			@TongTienNoiBo				= 0,
			@TongTienKhuyemMai			= 0,
			@TongTienThucChaySauCK		= 0,
			@TongGiaTriThayDoi			= 0
	
	
	SET @LogTime = GETDATE();
	
	-- Insert action log
	EXEC dbo.LogUserActionFromThucChay_InsertActionLog
		@TenDangNhap
		,@LogTime
		,@TenBaoCao
		,@StartDate
		,@EndDate
		,@SoHopDongList
		,@DmPhongBanREFList
		,@DmBoPhanREFList
		,@DmNhomLamViecREFList
		,@TenNhanVienList
		,@KhachHangREF
		,@NhanHang
		,@DmNhomNganhREF
		,@DmHinhThucQuangCaoList
		,@DmSanPhamREFList
		,@DmBannerREFList
		,@DmWebsiteREFList
		,@TongViewThucChayNoiBo
		,@TongClickThucChayNoiBo
		,@TongSoBaiVietNoiBo
		,@TongSoNgayChayNoiBo
		,@TongViewThucChayKhuyenMai
		,@TongClickThucChayKhuyenMai
		,@TongSoBaiVietKhuyenMai
		,@TongSoNgayChayKhuyenMai
		,@TongViewThucChay
		,@TongClickThucChay
		,@TongSoBaiViet
		,@TongSoNgayChay
		,@TongTienKhuyemMai
		,@TongTienNoiBo
		,@TongTienThucChaySauCK
		,@TongGiaTriThayDoi
		,@IsPheDuyet
		,@PheDuyetAt
		,@PheDuyetBy
		
	-- End Insert action log
	
	--IF(@DmSanPhamREFList <> 144)
	--BEGIN
	--SET @Sql = '
	--	UPDATE ThucChayDaTinh
	--	SET 
	--		IsPheDuyet = ' + CONVERT(varchar(10),@IsPheDuyet) + ',
	--		PheDuyetBy = ' + @DauNhay + @TenDangNhap + @DauNhay + ',
	--		PheDuyetAt = GETDATE()	
	--	WHERE 1=1 ' + @FilterString
	
	--PRINT @FilterString;	
	--PRINT @Sql;
	
	--EXEC(@Sql);
	--END
	--ELSE
	--BEGIN
	--		UPDATE ThucChayAdmarketPublisher 
	--			SET IsPheDuyet = @IsPheDuyet,
	--			PheDuyetBy = @TenDangNhap,
	--			PheDuyetAt = GETDATE()
	--		WHERE
	--			NgayThucHien BETWEEN @StartDate AND @EndDate AND DmSanPhamREF = 144
	--	END
				
	SELECT '0'
END

```
