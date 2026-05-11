# Stored Procedure: `ThucChay_TotalSumByFillterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-19 10:00:50.043000
- **Ngày sửa cuối**: 2015-08-05 16:50:42.957000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(510)` | No |
| `@DmWebsiteREFList` | `nvarchar(510)` | No |
| `@SoHopDongList` | `nvarchar(510)` | No |
| `@DmPhongBanREFList` | `nvarchar(510)` | No |
| `@DmBoPhanREFList` | `nvarchar(510)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(510)` | No |
| `@TenNhanVienList` | `nvarchar(510)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(510)` | No |
| `@DmBannerREFList` | `nvarchar(510)` | No |
| `@DonViTinhList` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description: Select total value by fillter condition
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_TotalSumByFillterCondition]
(
	-- Add the parameters for the stored procedure here
	@GroupFieldName			NVARCHAR(50),
	@StartDate				DATETIME,
	@EndDate				DATETIME,
	@DmSanPhamREFList		NVARCHAR(255),
	@DmWebsiteREFList		NVARCHAR(255),
	@SoHopDongList			NVARCHAR(255),
	@DmPhongBanREFList		NVARCHAR(255),
	@DmBoPhanREFList		NVARCHAR(255),
	@DmNhomLamViecREFList   NVARCHAR(255),
	@TenNhanVienList		NVARCHAR(255),
	@TenDangNhap			NVARCHAR(50),
	@DmHinhThucQuangCaoList NVARCHAR(255),
	@DmBannerREFList		NVARCHAR(255),
	@DonViTinhList			NVARCHAR(255)
)
AS
BEGIN
	DECLARE @Sql				NVARCHAR(MAX),
			@SqlAdmarket		NVARCHAR(MAX),
			@FilterString		NVARCHAR(255);
			
    DECLARE @DauNhay			NVARCHAR(50);
    Declare @GroupByFildID		NVARCHAR(255);
	Declare @GroupByFild		NVARCHAR(255);
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
	
	DECLARE @ToUserName NVARCHAR(50)
	
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
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName 
    
    IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild = 'DmSanPhamREF'
		SET @GroupByFildID = 'DmSanPhamREF AS ID,' 
		
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
	
	DECLARE @TempTable TABLE
	(
		GroupFieldName					NVARCHAR(50),
		GroupFileID						NVARCHAR(50),
		DonViTinh						NVARCHAR(50),
		SoHopDong						NVARCHAR(50),
		NgayKyHopDong					DATETIME,
		GiaTriThayDoi					FLOAT,
		SoLuongHopDongNoiBo				FLOAT,
		SoLuongHopDongKhuyenMai			FLOAT,
		SoLuongHopDongThucThu			FLOAT,
		SoLuongThucChayNoiBo			FLOAT,
		SoLuongThucChayKhuyenMai		FLOAT,
		SoLuongThucChayThucThu			FLOAT,
		ThanhTienNoiBo					FLOAT,
		ThanhTienKhuyenMai				FLOAT,
		ThanhTienThucChaySauChietKhau	FLOAT,
		ThanhTienThucThu				FLOAT,
		GiaTriThayDoiNB					FLOAT,
		GiaTriThayDoiTC					FLOAT
	)

	SET @PhongID		= 0;
	SET @BoPhanID		= 0;
	SET @NhomLamViecID	= 0;
	SET @ChucDanhID		= 0;
	
	SET @FilterString = '';
	IF @DonViTinhList <> ''
		SET @FilterString += ' AND T1.DonViTinh IN (' + @DonViTinhList + ')';

	SET @Sql = '		
		SELECT
			T1.'+ @GroupFieldName+','+@GroupByFildID+'
			T1.DonViTinh,SoHopDong AS SHD,
			MAX(T1.NgayKyHopDong) AS NgayKyHopDong,
			SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
			MAX(T1.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
			MAX(T1.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
			MAX(T1.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
			SUM(T1.SoLuongThucChayNoiBo) SoLuongThucChayNoiBo,
			SUM(T1.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
			SUM(T1.SoLuongThucChayThucThu) SoLuongThucChayThucThu,
			SUM(T1.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
			SUM(T1.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
			SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
			SUM(T1.ThanhTienThucChayThucThu) AS ThanhTienThucThu,
			SUM(T1.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
			SUM(T1.GiaTriThayDoiTC) AS GiaTriThayDoiTC
		FROM
		('
			+ dbo.ThucChay_GenSQLCommandForQuery(@StartDate,
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
												@DmBannerREFList) +
		')T1	
		WHERE 1=1 ' + @FilterString;
		
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')	
	BEGIN
		SET @Sql += ' AND DmSanPhamREF NOT IN (' + dbo.ThucChay_GetListProductAdmarket() + ')';
		SET @Sql += ' AND NOT(DmSanPhamREF = 375 AND year(NgayThucHien) = 2013) ';
	END
		
	
		SET @Sql += ' 
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF
		'	
	PRINT @GroupFieldName
	PRINT @Sql;
	
	INSERT INTO @TempTable
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
	
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')
	BEGIN
		SET @SqlAdmarket = '		
		SELECT
			T1.'+ @GroupFieldName+','+@GroupByFildID+'
			T1.DonViTinh,SoHopDong AS SHD,
			MAX(T1.NgayKyHopDong) AS NgayKyHopDong,
			SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
			MAX(T1.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
			MAX(T1.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
			MAX(T1.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
			SUM(T1.SoLuongThucChayNoiBo) SoLuongThucChayNoiBo,
			SUM(T1.SoLuongThucChayKhuyenMai) SoLuongThucChayKhuyenMai,
			SUM(T1.SoLuongThucChayThucThu) SoLuongThucChayThucThu,
			SUM(T1.ThanhTienThucChayNoiBo) AS ThanhTienNoiBo,
			SUM(T1.ThanhTienThucChayKhuyenMai) AS ThanhTienKhuyenMai,
			SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
			SUM(T1.ThanhTienThucChayThucThu) AS ThanhTienThucThu,
			SUM(T1.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
			SUM(T1.GiaTriThayDoiTC) AS GiaTriThayDoiTC
		FROM
		('
			+ dbo.ThucChay_GenSQLCommandAdmarketForQuery(@StartDate,
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
												@DmBannerREFList) +
		')T1	
		WHERE 1=1 ' + @FilterString + '
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF
		'
		
	PRINT '2'
	END	
	PRINT @SqlAdmarket;
	
	INSERT INTO @TempTable
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
			
	SET @TenBaoCao = N'Báo cáo Thực chạy chi tiết theo ' + @GroupFieldName;	
	
	-- Lay So luong theo don vi tinh Click
	SELECT @TongClickThucChayNoiBo		= SUM(A.SoLuongThucChayNoiBo),
			@TongClickThucChayKhuyenMai = SUM(A.SoLuongThucChayKhuyenMai),
			@TongClickThucChay			= SUM(A.SoLuongThucChayThucThu)
	FROM @TempTable A
	WHERE A.DonViTinh = 'CLICK';
	
	-- Lay So luong, Thanh tien theo don vi tinh View
	SELECT  @TongViewThucChayNoiBo		= SUM(A.SoLuongThucChayNoiBo),
			@TongViewThucChayKhuyenMai  = SUM(A.SoLuongThucChayKhuyenMai),
			@TongViewThucChay			= SUM(A.SoLuongThucChayThucThu)
	FROM @TempTable A
	WHERE A.DonViTinh = N'VIEW';
	
	-- Lay So luong theo don vi tinh Ngay
	SELECT  @TongSoNgayChayNoiBo		= SUM(A.SoLuongThucChayNoiBo),
			@TongSoNgayChayKhuyenMai = SUM(A.SoLuongThucChayKhuyenMai),
			@TongSoNgayChay			= SUM(A.SoLuongThucChayThucThu)
	FROM @TempTable A
	WHERE A.DonViTinh = N'NGÀY';
	
	-- Lay So luong theo don vi tinh Bài
	SELECT  @TongSoBaiVietNoiBo		= SUM(A.SoLuongThucChayNoiBo),
			@TongSoBaiVietKhuyenMai = SUM(A.SoLuongThucChayKhuyenMai),
			@TongSoBaiViet			= SUM(A.SoLuongThucChayThucThu)
	FROM @TempTable A
	WHERE A.DonViTinh = N'BÀI';
	
	-- Lay Thanh tien thuc chay
	SELECT  
			@TongTienNoiBo				= SUM(A.ThanhTienNoiBo),
			@TongTienKhuyemMai			= SUM(A.ThanhTienKhuyenMai),
			@TongTienThucChaySauCK		= SUM(A.ThanhTienThucThu),
			@TongGiaTriThayDoi			= SUM(A.GiaTriThayDoi)
	FROM @TempTable A;
	
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
		
	-- En Insert action log
		
	SELECT 
			T1.DonViTinh, 
			SUM(T1.GiaTriThayDoi) AS GiaTriThayDoi,
			SUM(T1.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
			SUM(T1.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
			SUM(T1.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
			SUM(T1.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo,
			SUM(T1.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
			SUM(T1.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
			SUM(T1.ThanhTienNoiBo) AS ThanhTienNoiBo,
			SUM(T1.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
			SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu,
			SUM(T1.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
			SUM(T1.GiaTriThayDoiTC) AS GiaTriThayDoiTC,
			SUM(T1.ThanhTienNoiBo + T1.GiaTriThayDoiNB) AS ThanhTienThucThuNB,
			SUM(T1.ThanhTienThucThu + T1.GiaTriThayDoiTC) AS ThanhTienThucThuTC,
			ROW_NUMBER() OVER (ORDER BY SUM(T1.ThanhTienThucThu) DESC) AS num
	FROM @TempTable T1
	GROUP BY T1.DonViTinh
	ORDER BY T1.DonViTinh
	;
	
END

```
