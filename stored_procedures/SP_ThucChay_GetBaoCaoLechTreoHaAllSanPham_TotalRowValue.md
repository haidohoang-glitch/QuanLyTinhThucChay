# Stored Procedure: `ThucChay_GetBaoCaoLechTreoHaAllSanPham_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-17 08:28:14.113000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.443000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
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
| `@IsShowNoiBo` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-07-11
-- Description:	Bao cao lech treo ha theo san pham level 1
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetBaoCaoLechTreoHaAllSanPham_TotalRowValue]
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
	@DonViTinhList			NVARCHAR(200),
	@IsShowNoiBo			INT -- -1: all, 1: noi bo; 0: ko noi bo
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @SqlCommand		NVARCHAR(MAX),
			@DauNhay		NVARCHAR(50) = '''';
    
    DECLARE @PhongID		INT = 0, 
			@BoPhanID		INT = 0, 
			@NhomLamViecID	INT = 0, 
			@ChucDanhID		INT = 0;
			
	DECLARE @Pamrams NVARCHAR(MAX);
	SET @Pamrams = N'@StartDateParam datetime,
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
					@DonViTinhListParam NVARCHAR(200),
					@IsShowNoiBoParam	int';
			
	IF OBJECT_ID('tempdb..#TempTable') IS NOT NULL
		BEGIN
			DROP TABLE #TempTable
		END

	CREATE TABLE #TempTable
	(
		DmSanPhamREF		INT,	
		TenSanPham			NVARCHAR(50),		
		DonViTinh			NVARCHAR(50),		
		SoLuongHopDong		BIGINT,
		ThanhTienHopDong	FLOAT,
		SoLuongThucChay		BIGINT,
		ThanhTienThucChay	FLOAT,
		SoLuongLechTreoHa	BIGINT,
		ThanhTienLechTreoHa	FLOAT
	)
	
	SET @SqlCommand = '
		SELECT 
			B.DmSanPhamREF, B.TenSanPham, B.DonViTinh,
			SUM(B.SoLuongHopDong) AS SoLuongHopDong,
			SUM(B.ThanhTienHopDong) AS ThanhTienHopDong,
			SUM(SoLuongThucChay) AS SoLuongThucChay,
			SUM(ThanhTienThucChay) AS ThanhTienThucChay ,
			SUM(B.SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa,
			SUM(B.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa 
		FROM
		('
			+ dbo.ThucChay_GenSQLCommandForBaoCaoLechTreoHaAllSanPham(@StartDate,
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
												@DonViTinhList,
												@IsShowNoiBo) +
		')B
		GROUP BY B.DmSanPhamREF, B.TenSanPham, B.DonViTinh ';
		
	PRINT @SqlCommand;
	
	INSERT INTO #TempTable
	EXECUTE sp_executesql @SqlCommand, @Pamrams, 
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
		@DonViTinhListParam				= @DonViTinhList,
		@IsShowNoiBoParam				= @IsShowNoiBo;
		
		
	SELECT 	
		DonViTinh,
		SUM(SoLuongHopDong) AS SoLuongHopDong,
		SUM(ThanhTienHopDong) AS ThanhTienHopDong,
		SUM(SoLuongThucChay) AS SoLuongThucChay,
		SUM(ThanhTienThucChay) AS ThanhTienThucChay,
		SUM(SoLuongLechTreoHa) AS SoLuongLechTreoHa,
		SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
	FROM #TempTable
	GROUP BY
		--DmSanPhamREF, TenSanPham, 
		DonViTinh
	
END

```
