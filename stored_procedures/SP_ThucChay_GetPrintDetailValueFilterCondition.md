# Stored Procedure: `ThucChay_GetPrintDetailValueFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-25 17:01:12.793000
- **Ngày sửa cuối**: 2014-11-19 12:17:55.143000

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
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@DonViTinhList` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-09-17
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_GetPrintDetailValueFilterCondition] 
    -- Add the parameters for the stored procedure here
	@GroupFieldName nvarchar(50),
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@TenDangNhap nvarchar(50),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList NVARCHAR(200),
	@DonViTinhList			NVARCHAR(255)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql			NVARCHAR(MAX),
			@SqlAdmarket	NVARCHAR(MAX);
			
    DECLARE @DauNhay			NVARCHAR(50);
    Declare @GroupByFildID		nvarchar(4000);
	Declare @GroupByFild		nvarchar(4000);
	Declare @FilterString		nvarchar(4000);
	DECLARE @GroupPermission	INT;
	
	DECLARE @Level2		NVARCHAR(50), 
			@Level3		NVARCHAR(50)
	DECLARE @PhongID		INT, 
			@BoPhanID		INT, 
			@NhomLamViecID	INT, 
			@ChucDanhID		INT

	DECLARE @ToUserName NVARCHAR(50)
	
	DECLARE @OrderByField NVARCHAR(50)
	DECLARE @Function NVARCHAR(50)
	
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
    
    IF (UPPER(@GroupFieldName) = 'TENSANPHAM' OR UPPER(@GroupFieldName) = 'TENWEBSITE' OR UPPER(@GroupFieldName) = 'TENPHONGBAN' OR UPPER(@GroupFieldName) = 'TENBOPHAN' OR UPPER(@GroupFieldName) = 'TENNHOMLAMVIEC')
	Begin
		SET @Level2 = 'TenNhanVien'
		SET @Level3 = 'SoHopDong' 
	End
	
	ELSE IF (UPPER(@GroupFieldName) = 'SOHOPDONG' OR UPPER(@GroupFieldName) = 'TENNHANVIEN')
	Begin
		SET @Level2 = 'TenSanPham'
		SET @Level3 = 'TenWebsite' 
	END
	
	SET @PhongID = 0;
		SET @BoPhanID = 0;
		SET @NhomLamViecID = 0;
		SET @ChucDanhID = 0;
		
	DECLARE @TableResult TABLE
			(
				GroupFieldName1					NVARCHAR(50),
				GroupFieldName2					NVARCHAR(50),
				GroupFieldName3					NVARCHAR(50),
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
				T2.'+ @GroupFieldName+' AS GroupFieldName1,T2.' + @Level2 + ' AS GroupFieldName2,T2.' + @Level3 +' AS GroupFieldName3,
				MAX(T2.NgayKyHopDong) AS NgayKyHopDong,
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
			WHERE 1 = 1 '
			
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')
		SET @Sql += ' AND T2.DmSanPhamREF NOT IN(144,299,337,585) ';
		
		SET @Sql += ' 
			GROUP BY T2.'+ @GroupFieldName+',T2.' + @Level2 + ', T2.' + @Level3 + '
			ORDER BY ' + @Function + '(T2.' + @OrderByField + ') DESC'
	    
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
		
	-- select du lieu admarket theo hop dong
	IF (@GroupFieldName <> 'TenSanPham' AND @GroupFieldName <> 'TenWebsite')
	BEGIN
		SET @SqlAdmarket = '
		SELECT
			T2.'+ @GroupFieldName+' AS GroupFieldName1,T2.' + @Level2 + ' AS GroupFieldName2,T2.' + @Level3 +' AS GroupFieldName3,
			MAX(T2.NgayKyHopDong) AS NgayKyHopDong,
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
		WHERE 1 = 1 
		GROUP BY T2.'+ @GroupFieldName+',T2.' + @Level2 + ', T2.' + @Level3 + '
			ORDER BY ' + @Function + '(T2.' + @OrderByField + ') DESC';
		
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
	
	SELECT 
		GroupFieldName1,
		GroupFieldName2,
		GroupFieldName3,
		NgayKyHopDong,
		GiaTriThayDoi,
		ThanhTienNoiBo,
		ThanhTienKhuyenMai,
		ThanhTienThucChaySauChietKhau,
		ThanhTienThucThu,
		GiaTriThayDoiNB,
		GiaTriThayDoiTC,
		(ThanhTienNoiBo + GiaTriThayDoiNB) ThanhTienThucThuNB,
		(ThanhTienThucThu + GiaTriThayDoiTC) ThanhTienThucThuTC
	FROM 
	@TableResult
			
	
	
	
END

```
