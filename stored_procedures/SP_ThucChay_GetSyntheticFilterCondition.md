# Stored Procedure: `ThucChay_GetSyntheticFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-25 17:01:11.473000
- **Ngày sửa cuối**: 2016-04-22 09:52:50.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@GroupFieldName` | `nvarchar(1024)` | No |
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
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@DonViTinhList` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
--exec [ThucChay_GetSumFilterCondition]
--@PageIndex = 1,
--	@RecordCount = 10,
--	@GroupFieldName = N'TenSanPham',
--	@StartDate = '2013-01-01',
--	@EndDate = '2013-01-05',
--	@DmSanPhamREFList = N'',
--	@DmWebsiteREFList = N'',
--	@SoHopDongList = N'',
--	@DmPhongBanREFList = N'',
--	@DmBoPhanREFList = N'',
--	@DmNhomLamViecREFList = N'',
--	@TenNhanVienList = N''

-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-09-17
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_GetSyntheticFilterCondition] 
    -- Add the parameters for the stored procedure here
    @PageIndex				INT,
	@RecordCount			INT,
	@GroupFieldName			NVARCHAR(512),
	@StartDate				DATETIME,
	@EndDate				DATETIME,
	@DmSanPhamREFList		NVARCHAR(512),
	@DmWebsiteREFList		NVARCHAR(512),
	@SoHopDongList			NVARCHAR(512),
	@DmPhongBanREFList		NVARCHAR(512),
	@DmBoPhanREFList		NVARCHAR(512),
	@DmNhomLamViecREFList	NVARCHAR(512),
	@TenNhanVienList		NVARCHAR(512),
	@TenDangNhap			nvarchar(50),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList		NVARCHAR(200),
	@DonViTinhList			NVARCHAR(512)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql				NVARCHAR(MAX),
			@SqlAdmarket		NVARCHAR(MAX);
    DECLARE @DauNhay			NVARCHAR(50);
    Declare @GroupByFildID		NVARCHAR(512);
	Declare @GroupByFild		NVARCHAR(512);
	Declare @FilterString		NVARCHAR(512);
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
	
	DECLARE @Pamrams		NVARCHAR(MAX);
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
				GroupFieldName					NVARCHAR(500),
				GroupFileID						NVARCHAR(500),
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
			
	SET @FilterString = '';
	
	IF @DonViTinhList <> ''
		SET @FilterString += ' AND T2.DonViTinh IN (' + @DonViTinhList + ')';
			
	SET @Sql = '
		SELECT
			T2.'+ @GroupFieldName+',' + @GroupByFildID + '
			MAX(T2.NgayKyHopDong) AS NgayKyHopDong,
			SUM(T2.GiaTriThayDoi) GiaTriThayDoi,
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
		WHERE 1 = 1 '
		
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')	
		SET @Sql += ' AND T2.DmSanPhamREF NOT IN (144,299,337,585,628)';
		
		SET @Sql += ' 
		GROUP BY T2.'+ @GroupFieldName+',T2.' + @GroupByFild
	
	PRINT @Sql;
	
	INSERT INTO @TableResult
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
		
	-- select du lieu admarket theo hop dong
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')
	BEGIN
		SET @SqlAdmarket = '
		SELECT
			T2.'+ @GroupFieldName+',' + @GroupByFildID + '
			MAX(T2.NgayKyHopDong) AS NgayKyHopDong,
			SUM(T2.GiaTriThayDoi) GiaTriThayDoi,
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
		WHERE 1 = 1 
		GROUP BY T2.'+ @GroupFieldName+',T2.' + @GroupByFild;
		
		PRINT @SqlAdmarket;
	
		INSERT INTO @TableResult
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
	END
	
	SELECT 
		T.GroupFieldName,T.GroupFileID,
		T.GiaTriThayDoi,
		T.ThanhTienNoiBo,
		T.ThanhTienKhuyenMai,
		T.ThanhTienThucChaySauChietKhau,
		T.ThanhTienThucThu,
		T.GiaTriThayDoiNB,
		T.GiaTriThayDoiTC,
		(T.GiaTriThayDoiNB + T.ThanhTienNoiBo) AS ThanhTienThucThuNB,
		(T.GiaTriThayDoiTC + T.ThanhTienThucThu) AS ThanhTienThucThuTC
	FROM
	(
		SELECT 
			GroupFieldName, GroupFileID,
			MAX(T1.NgayKyHopDong) AS NgayKyHopDong,				
			SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
			SUM(T1.ThanhTienNoiBo) AS ThanhTienNoiBo,
			SUM(T1.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
			SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
			SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu,
			SUM(T1.GiaTriThayDoiNB) AS GiaTriThayDoiNB,
			SUM(T1.GiaTriThayDoiTC) AS GiaTriThayDoiTC,
			ROW_NUMBER() OVER (ORDER BY GroupFieldName) AS num
		FROM @TableResult T1 
		GROUP BY GroupFieldName,GroupFileID
	)T
	WHERE num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount
	ORDER BY 
		T.GroupFieldName

	
END

```
