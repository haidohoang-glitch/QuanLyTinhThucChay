# Stored Procedure: `ThucChay_TableTotalPageNumber`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-14 13:08:24.033000
- **Ngày sửa cuối**: 2015-08-05 16:49:42.100000

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
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_TableTotalPageNumber]
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
	DECLARE @Sql				NVARCHAR(MAX),
			@SqlAdmarket		NVARCHAR(MAX);
	Declare @DauNhay			NVARCHAR(50)
	Declare @GroupByFildID		NVARCHAR(50)
	Declare @GroupByFild		NVARCHAR(50)
	Declare @FilterString		NVARCHAR(MAX)
	DECLARE @IsHaveValue		NVARCHAR(MAX)
	DECLARE @GroupPermission	INT;
	DECLARE @PhongID			INT, 
			@BoPhanID			INT, 
			@NhomLamViecID		INT, 
			@ChucDanhID			INT
	DECLARE @TuNgay				DATETIME, 
			@DenNgay			DATETIME	
	DECLARE @MinDate			DATETIME, 
			@MaxDate			DATETIME
	DECLARE @SqlCommand			Nvarchar(MAX)
	DECLARE @Count				INT
	
	DECLARE @Pamrams			NVARCHAR(MAX);
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
		
	DECLARE @ToUserName NVARCHAR(50)
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName

	IF @GroupFieldName = 'TenSanPham'
		Begin
			SET @GroupByFild = 'DmSanPhamREF'
			SET @GroupByFildID = 'DmSanPhamREF AS ID,' 
		End
	ELSE IF @GroupFieldName = 'TenWebsite'
		Begin
			SET @GroupByFild = 'DmWebsiteREF'
			SET @GroupByFildID = 'DmWebsiteREF AS ID,' 
		End
	ELSE IF @GroupFieldName = 'TenPhongBan'
		Begin
			SET @GroupByFild = 'DmPhongBanREF'
			SET @GroupByFildID = 'DmPhongBanREF AS ID,' 
		End
	ELSE IF @GroupFieldName = 'TenBoPhan'
		Begin
			SET @GroupByFild = 'DmBoPhanREF'
			SET @GroupByFildID = 'DmBoPhanREF AS ID,' 
		End
	ELSE IF @GroupFieldName = 'TenNhomLamViec'
		Begin
			SET @GroupByFild = 'DmNhomLamViecREF'
			SET @GroupByFildID = 'DmNhomLamViecREF AS ID,' 
		END
	ELSE IF @GroupFieldName = 'SoHopDong'
		Begin
			SET @GroupByFild = 'SoHopDong'
			SET @GroupByFildID = 'SoHopDong AS ID,' 
		END
	ELSE IF @GroupFieldName = 'TenNhanVien'
		Begin
			SET @GroupByFild = 'TenDangNhap'
			SET @GroupByFildID = 'TenDangNhap AS ID,' 
		End

	IF OBJECT_ID('tempdb..#TempTable') IS NOT NULL
		BEGIN
			DROP TABLE #TempTable
		END

	CREATE TABLE #TempTable
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
			ThanhTienThucThu				FLOAT
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
			SUM(T1.ThanhTienThucChayThucThu) AS ThanhTienThucThu
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
		WHERE 1=1 ' + @FilterString 
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')
	BEGIN
		SET @Sql += ' AND DmSanPhamREF NOT IN (' + dbo.ThucChay_GetListProductAdmarket() + ')';
		SET @Sql += ' AND NOT(DmSanPhamREF = 375 AND year(NgayThucHien) = 2013) ';
	END
		
	
	SET @Sql += '
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF'

	PRINT @Sql;
	
	INSERT INTO #TempTable
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
		
	-- Sect data from thuc chay tinh theo hinh thuc SelfServing, Admarket do du lieu tra tu san pham tra ve theo cac chieu khac nhau.	
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
			SUM(T1.ThanhTienThucChayThucThu) AS ThanhTienThucThu
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
	END
	
	PRINT @SqlAdmarket;
	
	INSERT INTO #TempTable
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
	
	SELECT 
		COUNT(T.GroupFileID) AS MaxRecords		
	FROM
	(
		SELECT 
			 T1.GroupFileID, T1.GroupFieldName,
			 T1.DonViTinh 
			 
		FROM #TempTable T1
		GROUP BY T1.GroupFileID, T1.GroupFieldName, T1.DonViTinh
		HAVING ROUND(SUM(T1.GiaTriThayDoi),0) <> 0 OR ROUND(SUM(T1.ThanhTienNoiBo),0) > 0 OR ROUND(SUM(T1.ThanhTienKhuyenMai),0) > 0 OR ROUND(SUM(T1.ThanhTienThucThu),0) > 0
	)T
	;

END

```
