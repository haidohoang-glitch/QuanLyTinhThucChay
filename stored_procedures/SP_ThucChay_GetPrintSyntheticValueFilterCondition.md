# Stored Procedure: `ThucChay_GetPrintSyntheticValueFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-25 17:01:12.583000
- **Ngày sửa cuối**: 2014-11-19 12:17:55.113000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(1024)` | No |
| `@DmWebsiteREFList` | `nvarchar(1024)` | No |
| `@SoHopDongList` | `nvarchar(1024)` | No |
| `@DmPhongBanREFList` | `nvarchar(1024)` | No |
| `@DmBoPhanREFList` | `nvarchar(1024)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(1024)` | No |
| `@TenNhanVienList` | `nvarchar(1024)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(510)` | No |
| `@DmBannerREFList` | `nvarchar(510)` | No |
| `@DonViTinhList` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-09-17
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_GetPrintSyntheticValueFilterCondition] 
    -- Add the parameters for the stored procedure here
	@GroupFieldName			NVARCHAR(50),
	@StartDate				DATETIME,
	@EndDate				DATETIME,
	@DmSanPhamREFList		NVARCHAR(512),
	@DmWebsiteREFList		NVARCHAR(512),
	@SoHopDongList			NVARCHAR(512),
	@DmPhongBanREFList		NVARCHAR(512),
	@DmBoPhanREFList		NVARCHAR(512),
	@DmNhomLamViecREFList	NVARCHAR(512),
	@TenNhanVienList		NVARCHAR(512),
	@TenDangNhap			NVARCHAR(50),
	@DmHinhThucQuangCaoList NVARCHAR(255),
	@DmBannerREFList		NVARCHAR(255),
	@DonViTinhList			NVARCHAR(255)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql				NVARCHAR(MAX),
			@SqlAdmarket		NVARCHAR(MAX);
			
    DECLARE @DauNhay			NVARCHAR(50);
    Declare @GroupByFildID		NVARCHAR(255);
	Declare @GroupByFild		NVARCHAR(255);
	Declare @FilterString		NVARCHAR(MAX);
	DECLARE @GroupPermission	INT;
	
	DECLARE @PhongID		INT, 
			@BoPhanID		INT, 
			@NhomLamViecID	INT, 
			@ChucDanhID		INT
			
	DECLARE @TuNgay		DATETIME, 
			@DenNgay	DATETIME	
	DECLARE @MinDate	DATETIME, 
			@MaxDate	DATETIME
	DECLARE @SqlCommand NVARCHAR(MAX);
	DECLARE @Count		int
	
	DECLARE @ToUserName		NVARCHAR(50)
	DECLARE @OrderByField	NVARCHAR(50)
	DECLARE @Function		NVARCHAR(50)
	
	DECLARE @Pamrams	NVARCHAR(MAX);
	SET @Pamrams = N'@GroupFieldNameParam nvarchar(50), 
					@StartDateParam datetime,
					@EndDateParam datetime, 
					@DmSanPhamREFListParam nvarchar(4000), 
					@DmWebsiteREFListParam nvarchar(4000), 
					@SoHopDongListParam nvarchar(4000), 
					@DmPhongBanREFListParam nvarchar(4000), 
					@DmBoPhanREFListParam nvarchar(4000), 
					@DmNhomLamViecREFListParam nvarchar(4000), 
					@TenNhanVienListParam nvarchar(4000),
					@TenDangNhapParam nvarchar(50), 
					@DmHinhThucQuangCaoListParam NVARCHAR(200), 
					@DmBannerREFListParam NVARCHAR(200), 
					@DonViTinhListParam NVARCHAR(200)'
	
	IF UPPER(@GroupFieldName) = 'SOHOPDONG'
	BEGIN
		SET @OrderByField = 'NgayKyHopDong'
		SET @Function = 'MAX'
	END
	ELSE
	BEGIN
		SET @OrderByField = 'ThanhTienThucThu'
		SET @Function = 'SUM'
	END
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName
    
    IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild = 'DmSanPhamREF'
		SET @GroupByFildID = 'DmSanPhamREF AS ID,' 
		
		--IF @DmSanPhamREFList=''
		--	SET @DmSanPhamREFList = dbo.GetListSanPhamByNhanVien(@TenDangNhap)
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENWEBSITE'
	Begin
		SET @GroupByFild = 'DmWebsiteREF'
		SET @GroupByFildID = 'DmWebsiteREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENPHONGBAN'
	Begin
		SET @GroupByFild = 'DmPhongBanREF'
		SET @GroupByFildID = 'DmPhongBanREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENBOPHAN'
	Begin
		SET @GroupByFild = 'DmBoPhanREF'
		SET @GroupByFildID = 'DmBoPhanREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC'
	Begin
		SET @GroupByFild = 'DmNhomLamViecREF'
		SET @GroupByFildID = 'DmNhomLamViecREF AS ID,' 
	END
	ELSE IF UPPER(@GroupFieldName) = 'SOHOPDONG'
	Begin
		SET @GroupByFild = 'SoHopDong'
		SET @GroupByFildID = 'SoHopDong AS ID,' 
	END
	ELSE IF UPPER(@GroupFieldName) = 'TENNHANVIEN'
	Begin
		SET @GroupByFild = 'TenDangNhap'
		SET @GroupByFildID = 'TenDangNhap AS ID,' 
		
	END
	
	DECLARE @TableResult TABLE
			(
				GroupFieldName					NVARCHAR(50),
				GroupFileID						NVARCHAR(50),
				NgayKyHopDong					DATETIME,
				GiaTriThayDoi					FLOAT,
				ThanhTienNoiBo					FLOAT,
				ThanhTienKhuyenMai				FLOAT,
				ThanhTienThucChaySauChietKhau	FLOAT,
				ThanhTienThucThu				FLOAT,
				GiaTriThayDoiNB					FLOAT,
				GiaTriThayDoiTC					FLOAT,
				RowNumber						INT
			)
			
	SET @Sql = '
			SELECT
				T2.'+ @GroupFieldName+' AS GroupFieldName,' + @GroupByFildID + '
				T2.NgayKyHopDong,
				SUM(T2.GiaTriThayDoi) AS GiaTriThayDoi,
				SUM(T2.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
				SUM(T2.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(T2.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
				SUM(T2.ThanhTienThucThu) AS ThanhTienThucThu,
				SUM(T2.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
				SUM(T2.GiaTriThayDoiTC) AS GiaTriThayDoiTC,
				ROW_NUMBER() OVER (ORDER BY '+@Function +'(T2.' + @OrderByField + ')DESC) AS num
			FROM
			('
					+ dbo.ThucChay_GenSQLCommandForSyntheticQuery(@StartDate,
																	@EndDate,
																	@DmSanPhamREFList ,
																	@DmWebsiteREFList ,
																	@SoHopDongList ,
																	@DmPhongBanREFList ,
																	@DmBoPhanREFList ,
																	@DmNhomLamViecREFList ,
																	@TenNhanVienList,
																	@TenDangNhap,
																	@PhongID,
																	@BoPhanID,
																	@NhomLamViecID,
																	@ChucDanhID,
																	@DmHinhThucQuangCaoList,
																	@DmBannerREFList,
																	@DonViTinhList
																	) +
			')T2 
			WHERE 1=1 '
			
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')
		SET @Sql += ' AND T2.DmSanPhamREF NOT IN (144,299,337,585) ';
			
	--IF @GroupFieldName = 'SoHopDong' OR @GroupFieldName = 'TenNhanVien'
	--	SET @Sql += '
	--		WHERE T2.DangSuDung NOT IN (5001,5002,5003) '
		
	SET @Sql += '
			GROUP BY T2.'+ @GroupFieldName+',T2.' + @GroupByFild +', NgayKyHopDong 
			ORDER BY ' + @GroupFieldName + ' ASC'
			
	PRINT @Sql;
	
	INSERT INTO @TableResult
	EXECUTE sp_executesql @Sql, @Pamrams, 
		@GroupFieldNameParam			= @GroupFieldName,
		@StartDateParam					= @StartDate,
		@EndDateParam					= @EndDate,
		@DmSanPhamREFListParam			= @DmSanPhamREFList,
		@DmWebsiteREFListParam			= @DmWebsiteREFList,
		@SoHopDongListParam				= @SoHopDongList,
		@DmPhongBanREFListParam			= @DmPhongBanREFList,
		@DmBoPhanREFListParam			= @DmBoPhanREFList,
		@DmNhomLamViecREFListParam		= @DmNhomLamViecREFList,
		@TenNhanVienListParam			= @TenNhanVienList,
		@TenDangNhapParam				= @TenDangNhap,
		@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
		@DmBannerREFListParam			= @DmBannerREFList,
		@DonViTinhListParam				= @DonViTinhList;
		
	-- select data admarket theo hop dong
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')
	BEGIN
		SET @SqlAdmarket = '
			SELECT
				T2.'+ @GroupFieldName+' AS GroupFieldName,' + @GroupByFildID + '
				T2.NgayKyHopDong,
				SUM(T2.GiaTriThayDoi) AS GiaTriThayDoi,
				SUM(T2.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
				SUM(T2.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
				SUM(T2.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
				SUM(T2.ThanhTienThucThu) AS ThanhTienThucThu,
				SUM(T2.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
				SUM(T2.GiaTriThayDoiTC) AS GiaTriThayDoiTC,
				ROW_NUMBER() OVER (ORDER BY '+@Function +'(T2.' + @OrderByField + ')DESC) AS num
			FROM
			('
					+ dbo.ThucChay_GenSQLCommandAdmarketForSyntheticQuery(@StartDate,
																	@EndDate,
																	@DmSanPhamREFList ,
																	@DmWebsiteREFList ,
																	@SoHopDongList ,
																	@DmPhongBanREFList ,
																	@DmBoPhanREFList ,
																	@DmNhomLamViecREFList ,
																	@TenNhanVienList,
																	@TenDangNhap,
																	@PhongID,
																	@BoPhanID,
																	@NhomLamViecID,
																	@ChucDanhID,
																	@DmHinhThucQuangCaoList,
																	@DmBannerREFList,
																	@DonViTinhList
																	) +
			')T2 
			WHERE 1=1 
			GROUP BY T2.'+ @GroupFieldName+',T2.' + @GroupByFild +', NgayKyHopDong 
			ORDER BY ' + @GroupFieldName + ' ASC';
		
		PRINT @SqlAdmarket;	
		INSERT INTO @TableResult
		EXECUTE sp_executesql @SqlAdmarket, @Pamrams, 
			@GroupFieldNameParam			= @GroupFieldName,
			@StartDateParam					= @StartDate,
			@EndDateParam					= @EndDate,
			@DmSanPhamREFListParam			= @DmSanPhamREFList,
			@DmWebsiteREFListParam			= @DmWebsiteREFList,
			@SoHopDongListParam				= @SoHopDongList,
			@DmPhongBanREFListParam			= @DmPhongBanREFList,
			@DmBoPhanREFListParam			= @DmBoPhanREFList,
			@DmNhomLamViecREFListParam		= @DmNhomLamViecREFList,
			@TenNhanVienListParam			= @TenNhanVienList,
			@TenDangNhapParam				= @TenDangNhap,
			@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
			@DmBannerREFListParam			= @DmBannerREFList,
			@DonViTinhListParam				= @DonViTinhList;
	END
	
	
	-- Cho Log action nguoi dung
	DECLARE @LogTime						DATETIME
			,@TenBaoCao						NVARCHAR(512)
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
			,@IsPheDuyet					INT				= 0
			,@PheDuyetAt					DATETIME
			,@PheDuyetBy					NVARCHAR(50)
			
	SET @TenBaoCao = N'In Tổng hợp Báo cáo Thực chạy tổng hợp theo ' + @GroupFieldName;	
		
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
			@TongTienNoiBo				= SUM(A.ThanhTienNoiBo),
			@TongTienKhuyemMai			= SUM(A.ThanhTienKhuyenMai),
			@TongTienThucChaySauCK		= SUM(A.ThanhTienThucThu),
			@TongGiaTriThayDoi			= SUM(A.GiaTriThayDoi)
	FROM @TableResult A;
	
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
	
	-- End In sert action log
	
	SELECT 
		GroupFieldName, GroupFileID,
		MAX(T1.NgayKyHopDong) AS NgayKyHopDong,
		SUM(T1.GiaTriThayDoi) AS GiaTriThayDoi,
		SUM(T1.ThanhTienNoiBo) AS ThanhTienNoiBo,
		SUM(T1.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
		SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
		SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu,
		SUM(T1.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
		SUM(T1.GiaTriThayDoiTC) AS GiaTriThayDoiTC,
		SUM(T1.ThanhTienNoiBo + T1.GiaTriThayDoiNB) AS ThanhTienThucThuNB,
		SUM(T1.ThanhTienThucThu + T1.GiaTriThayDoiTC) AS ThanhTienThucThuTC,
		ROW_NUMBER() OVER (ORDER BY GroupFieldName) AS num
	FROM @TableResult T1 
	GROUP BY GroupFieldName,GroupFileID

	
END

```
