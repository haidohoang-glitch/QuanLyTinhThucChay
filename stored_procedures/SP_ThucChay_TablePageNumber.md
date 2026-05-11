# Stored Procedure: `ThucChay_TablePageNumber`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-09 15:48:22.210000
- **Ngày sửa cuối**: 2015-06-16 17:53:33.220000

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
| `@DonViTinh` | `nvarchar(1024)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(1024)` | No |
| `@DmBannerREFList` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_TablePageNumber] 
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
	@DonViTinh				NVARCHAR(512),	
	@TenDangNhap			NVARCHAR(50),
	@DmHinhThucQuangCaoList NVARCHAR(512),
	@DmBannerREFList		NVARCHAR(512)
AS
BEGIN	
	-- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql			NVARCHAR(MAX),
			@SqlAdmarket	NVARCHAR(MAX);
    DECLARE @DauNhay		NVARCHAR(50);
    Declare @GroupByFildID	nvarchar(4000);
	Declare @GroupByFild	nvarchar(4000);
	Declare @FilterString	nvarchar(4000);
	DECLARE @GroupPermission INT;
	DECLARE @PhongID		INT, 
			@BoPhanID		INT, 
			@NhomLamViecID	INT, 
			@ChucDanhID		INT
	
	DECLARE @ToUserName NVARCHAR(50);
	
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
				GroupFieldID					NVARCHAR(50),				
				DonViTinh						NVARCHAR(50),
				SoHopDong						NVARCHAR(50),
				HopDongChiTietREF				INT,
				LechBooking						NVARCHAR(50),
				NgayThucHien					datetime,
				IsKhuyenMai						INT,
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
			SoHopDong AS SHD,
			T1.HopDongChiTietREF,
			T1.LechBooking,T1.NgayThucHien,T1.IsKhuyenMai,
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
		WHERE T1.DonViTinh = N' +@DauNhay + @DonViTinh + @DauNhay + ' 
			AND T1.DmSanPhamREF NOT IN (' + dbo.ThucChay_GetListProductAdmarket() + ')
	'	
	SET @Sql += '
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.HopDongChiTietREF,T1.LechBooking,T1.NgayThucHien,T1.IsKhuyenMai
	'		
	
	PRINT @sql;
	
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
			
	SET @SqlAdmarket = '
		SELECT
			T1.'+ @GroupFieldName+','+@GroupByFildID+'
			T1.DonViTinh,
			SoHopDong AS SHD,
			T1.HopDongChiTietREF,
			T1.LechBooking,T1.NgayThucHien,T1.IsKhuyenMai,
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
		WHERE T1.DonViTinh = N' +@DauNhay + @DonViTinh + @DauNhay + ' 
			AND T1.DmSanPhamREF IN (' + dbo.ThucChay_GetListProductAdmarket() + ')
		GROUP BY T1.'+ @GroupFieldName+','+@GroupByFild+',T1.DonViTinh,SoHopDong,T1.HopDongChiTietREF,T1.LechBooking,T1.NgayThucHien,T1.IsKhuyenMai
	'
	
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
		COUNT(T.NgayThucHien) AS MaxRecords
	FROM
	(
		SELECT 
			GroupFieldName, GroupFieldID,DonViTinh,
			SUM(0) AS HopDongChiTietREF,T1.NgayThucHien,T1.IsKhuyenMai,
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
			ROW_NUMBER() OVER (ORDER BY GroupFieldName) AS num
		FROM @TempTable T1 
		GROUP BY T1.GroupFieldName,T1.GroupFieldID,T1.DonViTinh,T1.NgayThucHien,T1.IsKhuyenMai
	)T
			
	
END



--exec [Select_TablePageNumber] '10','phuongld','DmNgonNgu','1'

```
