# Stored Procedure: `ThucChay_Publish_Data_All`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-05 15:14:24.900000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.767000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `nvarchar(400)` | No |
| `@IsPheDuyet` | `int(4)` | No |
| `@Username` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE proc [dbo].[ThucChay_Publish_Data_All]		
	@DmSanPhamREF		INT,	
	@DmWebsiteREF		NVARCHAR(200),	
	@IsPheDuyet			INT,
	@Username			NVARCHAR(50),
	@StartDate			DATETIME,
	@EndDate			DATETIME,
	@DmHinhThucQuangCaoREF INT,
	@DmBannerREFList		NVARCHAR(200)
AS
BEGIN

	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(10)
	DECLARE @FilterSing NVARCHAR(4000)
	
	DECLARE @Pamrams NVARCHAR(MAX);
		
	SET @Pamrams = N'@DmSanPhamREFParam int,
					@DmWebsiteREFParam nvarchar(4000),
					@IsPheDuyetParam int, 
					@UsernameParam nvarchar(50),
					@StartDateParam datetime, 
					@EndDateParam datetime,
					@DmHinhThucQuangCaoREFParam int, 
					@DmBannerREFListParam nvarchar(4000)'
	
	SET @DauNhay = ''''
	SET @FilterSing = '';
	
	SET @FilterSing += ' NgayThucHien BETWEEN ' + @DauNhay + CONVERT(NVARCHAR(50), @StartDate) + @DauNhay + ' AND ' + @DauNhay + CONVERT(NVARCHAR(50), @EndDate) + @DauNhay;
	
	IF @DmSanPhamREF > 0 
		SET @FilterSing += ' AND DmSanPhamREF = ' + CONVERT(NVARCHAR(50), @DmSanPhamREF)
	IF @DmWebsiteREF <> ''
		SET @FilterSing += ' AND DmWebsiteREF IN (' + @DmWebsiteREF + ')'
		
	IF (@DmHinhThucQuangCaoREF > 0 AND @DmHinhThucQuangCaoREF <> -1 ) 
		SET @FilterSing += ' AND DmHinhThucQuangCao = ' + CONVERT(NVARCHAR(50), @DmHinhThucQuangCaoREF) 
		
	IF @DmBannerREFList <> 0
		SET @FilterSing += ' AND DmViTriREF in (' + @DmBannerREFList + ')'
		
	SET @Sql = '
		UPDATE ThucChayDaTinh
		SET
			IsPheDuyet = ' + CONVERT(NVARCHAR(10),@IsPheDuyet) + ', 
			PheDuyetBy = ' + @DauNhay + @Username + @DauNhay + ',
			PheDuyetAt = ' + @DauNhay + CONVERT(NVARCHAR(30),GETDATE()) +  @DauNhay + '
		WHERE ' + @FilterSing	
		
	
	PRINT @Sql;
	
	EXECUTE sp_executesql @Sql, @Pamrams,
		@DmSanPhamREFParam			= @DmSanPhamREF,
		@DmWebsiteREFParam			=@DmWebsiteREF,	
		@IsPheDuyetParam			= @IsPheDuyet,
		@UsernameParam				= @Username,
		@StartDateParam				= @StartDate,
		@EndDateParam				= @EndDate,
		@DmHinhThucQuangCaoREFParam = @DmHinhThucQuangCaoREF,
		@DmBannerREFListParam		= @DmBannerREFList
		
	-- Cho Log action nguoi dung
	DECLARE @LogTime						DATETIME
			,@TenBaoCao						NVARCHAR(512)
			,@SoHopDong						NVARCHAR(50) = ''
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
			
	SET @TenBaoCao = N'Duyệt dữ liệu theo all hợp đồng'
		
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
		@Username
		,@LogTime
		,@TenBaoCao
		,@StartDate
		,@EndDate
		,@SoHopDong
		,@DmPhongBanREFList
		,@DmBoPhanREFList
		,@DmNhomLamViecREFList
		,@TenNhanVienList
		,@KhachHangREF
		,@NhanHang
		,@DmNhomNganhREF
		,@DmHinhThucQuangCaoREF
		,@DmSanPhamREF
		,@DmBannerREFList
		,@DmWebsiteREF
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
	
	SELECT '0' 			
END

```
