# Stored Procedure: `ThucChay_GetSumFilterCondition_Label_TotalRow_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-17 08:28:11.880000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.990000

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
| `@DmHinhThucQuangCaoList` | `nvarchar(1024)` | No |
| `@DmBannerREFList` | `nvarchar(1024)` | No |
| `@TenNhanHangList` | `nvarchar(4000)` | No |
| `@TenKhachHangList` | `nvarchar(4000)` | No |
| `@DonViTinhList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-09-02
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_GetSumFilterCondition_Label_TotalRow_v2] 
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
	@DmHinhThucQuangCaoList NVARCHAR(512),
	@DmBannerREFList		NVARCHAR(512),
	@TenNhanHangList		NVARCHAR(2000),
	@TenKhachHangList		NVARCHAR(2000),
	@DonViTinhList			NVARCHAR(200)	
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
	Declare @FilterString		NVARCHAR(MAX);
	
	DECLARE @GroupPermission	INT;
	DECLARE @PhongID			INT, 
			@BoPhanID			INT, 
			@NhomLamViecID		INT, 
			@ChucDanhID			INT;
			
	DECLARE @TempTable AS TABLE(
		NhanHang	NVARCHAR(1000)	
	)
	
	SET @DauNhay =''''
	
	DECLARE @Pamrams NVARCHAR(MAX);
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
					@TenNhanHangListParam NVARCHAR(2000),
					@TenKhachHangListParam NVARCHAR(2000),
					@DonViTinhListParam		nvarchar(200)'
	
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
												@DonViTinhList)
	PRINT @FilterString;
	
	SET @Sql = '
		SELECT
			GroupFieldName
		FROM
		(
			SELECT 
				hd.NhanHopDong GroupFieldName,
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
			GROUP BY hd.NhanHopDong, tcdt.TenMaHopDong, tcdt.ThanhTienKM
			HAVING (SUM(ThanhTienSauTrietKhauThucChay) > 0 OR SUM(ThanhTienKM) > 0 OR SUM(GiaTriThayDoi) <> 0)
		)A
		GROUP BY GroupFieldName'
	
	PRINT @Sql;
	INSERT INTO @TempTable
	EXECUTE sp_executesql @Sql, 
		@Pamrams, 
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
		@TenNhanHangListParam			= @TenNhanHangList,
		@TenKhachHangListParam			= @TenKhachHangList,
		@DonViTinhListParam				= @DonViTinhList;
		
	SET @SqlAdmarket = '
		SELECT
			GroupFieldName
		FROM
		(
			SELECT 
				hd.NhanHopDong GroupFieldName,
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
			GROUP BY hd.NhanHopDong, tcdt.TenMaHopDong, tcdt.ThanhTienKM
			HAVING (SUM(ThanhTienSauTrietKhauThucChay) > 0 OR SUM(ThanhTienKM) > 0 OR SUM(GiaTriThayDoi) <> 0)
		)A
		GROUP BY GroupFieldName'
	
	PRINT @SqlAdmarket;
	INSERT INTO @TempTable
	EXECUTE sp_executesql @SqlAdmarket, 
		@Pamrams, 
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
		@TenNhanHangListParam			= @TenNhanHangList,
		@TenKhachHangListParam			= @TenKhachHangList,
		@DonViTinhListParam				= @DonViTinhList;
	
	
	SELECT COUNT(NhanHang) AS MaxRecords
	FROM
	(	
		SELECT DISTINCT NhanHang
		FROM @TempTable
	)T
	
END

```
