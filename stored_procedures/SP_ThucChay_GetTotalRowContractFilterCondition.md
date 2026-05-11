# Stored Procedure: `ThucChay_GetTotalRowContractFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-01 12:09:57.660000
- **Ngày sửa cuối**: 2015-06-16 17:52:09.893000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
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
| `@DonViTinh` | `nvarchar(100)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_GetTotalRowContractFilterCondition] 
    -- Add the parameters for the stored procedure here
	@GroupFieldName			NVARCHAR(50),
	@StartDate				DATETIME,
	@EndDate				DATETIME,
	@DmSanPhamREFList		NVARCHAR(4000),
	@DmWebsiteREFList		NVARCHAR(4000),
	@SoHopDongList			NVARCHAR(4000),
	@DmPhongBanREFList		NVARCHAR(4000),
	@DmBoPhanREFList		NVARCHAR(4000),
	@DmNhomLamViecREFList	NVARCHAR(4000),
	@TenNhanVienList		NVARCHAR(4000),
	@DonViTinh				NVARCHAR(50),
	@TenDangNhap			NVARCHAR(50),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList		NVARCHAR(200)	
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
	DECLARE @IsHaveValue		NVARCHAR(4000);
	DECLARE @GroupPermission	INT;
	
	DECLARE @PhongID		INT, 
			@BoPhanID		INT, 
			@NhomLamViecID	INT, 
			@ChucDanhID		INT
			
	DECLARE @ToUserName		NVARCHAR(50);
	
	DECLARE @Pamrams NVARCHAR(MAX);
	SET @Pamrams = N'@GroupFieldNameParam			NVARCHAR(50), 
					@StartDateParam					DATETIME,
					@EndDateParam					DATETIME, 
					@DmSanPhamREFListParam			NVARCHAR(512), 
					@DmWebsiteREFListParam			NVARCHAR(512), 
					@SoHopDongListParam				NVARCHAR(512), 
					@DmPhongBanREFListParam			NVARCHAR(512), 
					@DmBoPhanREFListParam			NVARCHAR(512), 
					@DmNhomLamViecREFListParam		NVARCHAR(512), 
					@TenNhanVienListParam			NVARCHAR(512),
					@DonViTinhParam					NVARCHAR(512),
					@TenDangNhapParam				NVARCHAR(50), 
					@DmHinhThucQuangCaoListParam	NVARCHAR(512), 
					@DmBannerREFListParam			NVARCHAR(512)';
	
    SET @DauNhay = '''';
    SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
    
    SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName
    
    IF UPPER(@GroupFieldName) = 'TENSANPHAM'
	Begin
		SET @GroupByFild	= 'DmSanPhamREF'
		SET @GroupByFildID	= 'DmSanPhamREF AS ID,' 
		
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENWEBSITE'
	Begin
		SET @GroupByFild	= 'DmWebsiteREF'
		SET @GroupByFildID	= 'DmWebsiteREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENPHONGBAN'
	Begin
		SET @GroupByFild	= 'DmPhongBanREF'
		SET @GroupByFildID	= 'DmPhongBanREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENBOPHAN'
	Begin
		SET @GroupByFild	= 'DmBoPhanREF'
		SET @GroupByFildID	= 'DmBoPhanREF AS ID,' 
	End
	ELSE IF UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC'
	Begin
		SET @GroupByFild	= 'DmNhomLamViecREF'
		SET @GroupByFildID	= 'DmNhomLamViecREF AS ID,' 
		
	END
	ELSE IF UPPER(@GroupFieldName) = 'SOHOPDONG'
	Begin
		SET @GroupByFild	= 'SoHopDong'
		SET @GroupByFildID	= 'SoHopDong AS ID,' 
	END
	ELSE IF UPPER(@GroupFieldName) = 'TENNHANVIEN'
	Begin
		SET @GroupByFild	= 'TenDangNhap'
		SET @GroupByFildID	= 'TenDangNhap AS ID,' 
	END
	
	DECLARE @TempTable TABLE
	(
		GroupFieldName					NVARCHAR(50),
		GroupFieldID					NVARCHAR(50),
		DonViTinh						NVARCHAR(50),
		SoHopDong						NVARCHAR(50),
		NgayKyHopDong					DATETIME,
		GiaTriThayDoi					FLOAT,
		SoLuongHopDongNoiBo				BIGINT,
		SoLuongHopDongKhuyenMai			BIGINT,
		SoLuongHopDongThucThu			BIGINT,
		SoLuongThucChayNoiBo			BIGINT,
		SoLuongThucChayKhuyenMai		BIGINT,
		SoLuongThucChayThucThu			BIGINT,
		ThanhTienNoiBo					FLOAT,
		ThanhTienKhuyenMai				FLOAT,
		ThanhTienThucChaySauChietKhau	FLOAT,
		ThanhTienThucThu				FLOAT
	)
			
	SET @Sql = '
		SELECT
			T1.'+ @GroupFieldName+','+@GroupByFildID+'
			T1.DonViTinh,
			T1.SoHopDong AS SHD,
			MAX(T1.NgayKyHopDong) NgayKyHopDong,
			SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
			SUM(T1.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
			SUM(T1.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
			SUM(T1.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
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
		WHERE T1.DonViTinh = N'+@DauNhay + @DonViTinh +@DauNhay + ' 
			AND T1.DmSanPhamREF NOT IN (' + dbo.ThucChay_GetListProductAdmarket() + ')
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF
	'
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
			@DonViTinhParam					= @DonViTinh,
			@TenDangNhapParam				= @TenDangNhap,
			@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
			@DmBannerREFListParam			= @DmBannerREFList;
	
	DECLARE @SqlAdmarket	NVARCHAR(MAX);
	SET @SqlAdmarket = '
		SELECT
			T1.'+ @GroupFieldName+','+@GroupByFildID+'
			T1.DonViTinh,
			T1.SoHopDong AS SHD,
			MAX(T1.NgayKyHopDong) NgayKyHopDong,
			SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
			SUM(T1.SoLuongHopDongNoiBo) SoLuongHopDongNoiBo,
			SUM(T1.SoLuongHopDongKhuyenMai) SoLuongHopDongKhuyenMai,
			SUM(T1.SoLuongHopDongThucThu) SoLuongHopDongThucThu,
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
		WHERE T1.DonViTinh = N' + @DauNhay + @DonViTinh + @DauNhay + '
			AND T1.DmSanPhamREF IN (' + dbo.ThucChay_GetListProductAdmarket() + ')
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.DmSanPhamREF'
	
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
			@DonViTinhParam					= @DonViTinh,
			@TenDangNhapParam				= @TenDangNhap,
			@DmHinhThucQuangCaoListParam	= @DmHinhThucQuangCaoList,
			@DmBannerREFListParam			= @DmBannerREFList;

	SELECT 
		COUNT(T.SoHopDong) AS MaxRecords
	FROM
	(
		SELECT 
			GroupFieldName, GroupFieldID,DonViTinh,SoHopDong,
			SUM(T1.GiaTriThayDoi) GiaTriThayDoi,
			SUM(T1.SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
			SUM(T1.SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
			SUM(T1.SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
			SUM(T1.SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo,
			SUM(T1.SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
			SUM(T1.SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
			SUM(T1.ThanhTienNoiBo) AS ThanhTienNoiBo,
			SUM(T1.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
			SUM(T1.ThanhTienThucChaySauChietKhau) AS ThanhTienThucChaySauChietKhau,
			SUM(T1.ThanhTienThucThu) AS ThanhTienThucThu,
			ROW_NUMBER() OVER (ORDER BY SUM(T1.ThanhTienThucThu) DESC) AS num
		FROM @TempTable T1 
		GROUP BY GroupFieldName,GroupFieldID,DonViTinh, SoHopDong
	)T
	
END

```
