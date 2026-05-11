# Stored Procedure: `ThucChay_GetContractFilterCondition_Label_TotalRow`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-23 18:46:25.867000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.823000

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
| `@DmHinhThucQuangCaoList` | `nvarchar(4000)` | No |
| `@DmBannerREFList` | `nvarchar(4000)` | No |
| `@TenNhanHangList` | `nvarchar(4000)` | No |
| `@TenKhachHangList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_GetContractFilterCondition_Label_TotalRow] 
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
	@DonViTinh NVARCHAR(50),	
	@TenDangNhap NVARCHAR(50),
	@DmHinhThucQuangCaoList NVARCHAR(2000),
	@DmBannerREFList NVARCHAR(2000),
	@TenNhanHangList NVARCHAR(2000),
	@TenKhachHangList NVARCHAR(200)	
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql NVARCHAR(MAX),
			@SqlAdmarket NVARCHAR(MAX);
    DECLARE @DauNhay NVARCHAR(50);
    Declare @GroupByFildID nvarchar(4000);
	Declare @GroupByFild nvarchar(4000);
	Declare @FilterString nvarchar(4000);
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand VARCHAR(MAX);

	DECLARE @ToUserName NVARCHAR(50)
	
    SET @DauNhay = '''';
    
    DECLARE @Pamrams NVARCHAR(MAX);
	SET @Pamrams = N'
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
					@DonViTinhParam nvarchar(50),
					@TenDangNhapParam nvarchar(50), 
					@DmHinhThucQuangCaoListParam NVARCHAR(200), 
					@DmBannerREFListParam NVARCHAR(200), 
					@TenNhanHangListParam NVARCHAR(2000),
					@TenKhachHangListParam NVARCHAR(200)'
					
	DECLARE @TempTable AS TABLE (
		GroupFieldID		NVARCHAR(2000), 
		SoHopDong			NVARCHAR(2000)
	)
	
	SET @FilterString = dbo.GetThucChayLabelFilterString_v2(@StartDate,
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
												@TenNhanHangList,
												@TenKhachHangList,
												@DonViTinh)
												
	PRINT @FilterString;												
	
	SET @Sql = '
		SELECT
			A.ID, A.SoHopDong
		FROM
		(
			SELECT 
				tcdt.SoHopDong ID,
				tcdt.SoHopDong SoHopDong,
				SUM(tcdt.GiaTriThayDoi) GiaTriThayDoi,					
				CASE WHEN (UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN 
						ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienNoiBo,
				ISNULL(SUM(tcdt.ThanhTienKM),0) AS ThanhTienKhuyenMai,			
				CASE WHEN (UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' AND UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ')  THEN 
						ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienThucThu,
				CASE WHEN (UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN 
						ISNULL(SUM(tcdt.GiaTriThayDoi),0) 
					ELSE 0
				END AS GiaTriThayDoiNB,
				CASE WHEN (UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' AND UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ')  THEN 
						ISNULL(SUM(tcdt.GiaTriThayDoi),0) 
					ELSE 0
				END AS GiaTriThayDoiTC
			FROM ThucChayDaTinh tcdt																	                      
				INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
			WHERE ' + @FilterString + ' 
			GROUP BY tcdt.SoHopDong, tcdt.TenMaHopDong, tcdt.ThanhTienKM
		)A
		GROUP BY 
			A.ID, A.SoHopDong'
	
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
		@DmBannerREFListParam			= @DmBannerREFList,
		@TenNhanHangListParam			= @TenNhanHangList,
		@TenKhachHangListParam			= @TenKhachHangList;
		
		
	-- Select data admarket
	SET @SqlAdmarket = '
		SELECT
			A.ID, A.SoHopDong
		FROM
		(
			SELECT 
				tcdt.SoHopDong ID,
				tcdt.SoHopDong SoHopDong,
				SUM(tcdt.GiaTriThayDoi) GiaTriThayDoi,					
				CASE WHEN (UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN 
						ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienNoiBo,
				ISNULL(SUM(tcdt.ThanhTienKM),0) AS ThanhTienKhuyenMai,			
				CASE WHEN (UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' AND UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ')  THEN 
						ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienThucThu,
				CASE WHEN (UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' OR UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' OR UPPER(tcdt.TenMaHopDong) LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ') THEN 
						ISNULL(SUM(tcdt.GiaTriThayDoi),0) 
					ELSE 0
				END AS GiaTriThayDoiNB,
				CASE WHEN (UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay + ' AND UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + '%SH%' + @DauNhay + ' AND UPPER(tcdt.TenMaHopDong) NOT LIKE ' + @DauNhay + '%SOHA%' + @DauNhay + ')  THEN 
						ISNULL(SUM(tcdt.GiaTriThayDoi),0) 
					ELSE 0
				END AS GiaTriThayDoiTC
			FROM ThucChayDaTinhAdmarket tcdt																	                      
				INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
			WHERE ' + @FilterString + ' 
			GROUP BY tcdt.SoHopDong, tcdt.TenMaHopDong, tcdt.ThanhTienKM
		)A
		GROUP BY 
			A.ID, A.SoHopDong'
	
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
		@DmBannerREFListParam			= @DmBannerREFList,
		@TenNhanHangListParam			= @TenNhanHangList,
		@TenKhachHangListParam			= @TenKhachHangList
	
	SELECT 
		COUNT(T.SoHopDong) AS MaxRecords
	FROM
	(	
		SELECT DISTINCT SoHopDong
		FROM @TempTable
	) T
END

```
