# Stored Procedure: `ThucChay_GetSumFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-20 14:50:51.620000
- **Ngày sửa cuối**: 2016-04-22 09:52:03.490000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@GroupFieldName` | `nvarchar(100)` | No |
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
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@DonViTinhList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-09-02
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_GetSumFilterCondition] 
    -- Add the parameters for the stored procedure here
    @PageIndex				INT = 1,
	@RecordCount			INT = 10,
	@GroupFieldName			nvarchar(50),
	@StartDate				datetime,
	@EndDate				datetime,
	@DmSanPhamREFList		nvarchar(4000),
	@DmWebsiteREFList		nvarchar(4000),
	@SoHopDongList			nvarchar(4000),
	@DmPhongBanREFList		nvarchar(4000),
	@DmBoPhanREFList		nvarchar(4000),
	@DmNhomLamViecREFList	nvarchar(4000),
	@TenNhanVienList		nvarchar(4000),
	@TenDangNhap			nvarchar(50),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList		NVARCHAR(200),
	@DonViTinhList			NVARCHAR(200)		
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql				NVARCHAR(MAX);
    DECLARE @DauNhay			NVARCHAR(50);
    Declare @GroupByFildID		nvarchar(4000);
	Declare @GroupByFild		nvarchar(4000);
	Declare @FilterString		nvarchar(4000);
	DECLARE @GroupPermission	INT;
	
	DECLARE @PhongID		INT, 
			@BoPhanID		INT, 
			@NhomLamViecID	INT, 
			@ChucDanhID		INT;
			
	DECLARE @SqlAdmarket	NVARCHAR(MAX);
	
	DECLARE @ToUserName NVARCHAR(50)

	
	DECLARE @Pamrams NVARCHAR(MAX);
	SET @Pamrams = N'@PageIndexParam int,
					@RecordCountParam int,
					@GroupFieldNameParam nvarchar(50), 
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
					@DonViTinhListParam NVARCHAR(200)';
	
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
	
	IF OBJECT_ID('tempdb..#TempTable') IS NOT NULL
		BEGIN
			DROP TABLE #TempTable
		END

	CREATE TABLE #TempTable
		(
			GroupFieldName nvarchar(500),
			GroupFieldID nvarchar(500),
			DonViTinh nvarchar(500),
			SoHopDong NVARCHAR(50),
			NgayKyHopDong DATETIME,
			GiaTriThayDoi FLOAT,
			SoLuongHopDongNoiBo float,
			SoLuongHopDongKhuyenMai float,
			SoLuongHopDongThucThu float,
			SoLuongThucChayNoiBo float,
			SoLuongThucChayKhuyenMai float,
			SoLuongThucChayThucThu float,
			ThanhTienNoiBo float,
			ThanhTienKhuyenMai float,
			ThanhTienThucChaySauChietKhau float,
			ThanhTienThucThu FLOAT,
			GiaTriThayDoiNB					FLOAT,
			GiaTriThayDoiTC					FLOAT
		)

	SET @PhongID = 0;
	SET @BoPhanID = 0;
	SET @NhomLamViecID = 0;
	SET @ChucDanhID = 0;
	
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
		SET @Sql += ' AND DmSanPhamREF NOT IN (144, 299, 337, 585) '; 
		SET @Sql += ' AND NOT(DmSanPhamREF = 375 AND year(NgayThucHien) = 2013) ';
	END
		
		
	SET @Sql += '
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF, T1.HopDongChiTietREF
		
	'

	PRINT @Sql;
	
	INSERT INTO #TempTable
	EXECUTE sp_executesql @Sql, @Pamrams, 
		@PageIndexParam					= @PageIndex,
		@RecordCountParam				= @RecordCount,
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
	END
	
	PRINT @SqlAdmarket;
	
	INSERT INTO #TempTable
	EXECUTE sp_executesql @SqlAdmarket, @Pamrams, 
		@PageIndexParam					= @PageIndex,
		@RecordCountParam				= @RecordCount,
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
		T.GroupFieldID AS ID,
		T.GroupFieldID,
		CASE WHEN @GroupFieldName = 'SoHopDong' AND T.GroupFieldName = '-' THEN 'MuaOnline'
			 WHEN @GroupFieldName <> 'SoHopDong' AND (T.GroupFieldName = '-' OR T.GroupFieldName = '') THEN 'Other'		
			 ELSE T.GroupFieldName
		END AS GroupFieldName,
		T.DonViTinh,  
		T.GiaTriThayDoi AS GTTD,
		T.GiaTriThayDoi AS GiaTriThayDoi,
		(T.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo, 
		(T.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai, 
		(T.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
		(T.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo, 
		(T.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai, 
		(T.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
		(T.ThanhTienNoiBo) AS ThanhTienNoiBo, 
		(T.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai, 
		(T.ThanhTienThucThu) AS ThanhTienThucThu,
		T.GiaTriThayDoiNB AS GiaTriThayDoiNB,
		T.GiaTriThayDoiTC AS GiaTriThayDoiTC,
		(T.ThanhTienNoiBo + T.GiaTriThayDoiNB) AS ThanhTienThucThuNB,
		(T.ThanhTienThucThu + T.GiaTriThayDoiTC) AS ThanhTienThucThuTC
		,num AS ItemIndex
	FROM
	(
		SELECT 			 
			 T1.GroupFieldID, T1.GroupFieldName,
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
			 ROW_NUMBER() OVER (ORDER BY (T1.GroupFieldName) ASC) AS num
		FROM #TempTable T1
		GROUP BY T1.GroupFieldID, T1.GroupFieldName, T1.DonViTinh
		HAVING ROUND(SUM(T1.GiaTriThayDoi),0) <> 0 OR ROUND(SUM(T1.ThanhTienNoiBo),0) <> 0 OR ROUND(SUM(T1.ThanhTienKhuyenMai),0) <> 0 OR ROUND(SUM(T1.ThanhTienThucThu),0) <> 0
			--OR T1.SoLuongThucChayNoiBo <> 0 OR T1.SoLuongThucChayKhuyenMai <> 0 OR T1.SoLuongThucChayThucThu <> 0
	)T
	WHERE T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount;
END

```
