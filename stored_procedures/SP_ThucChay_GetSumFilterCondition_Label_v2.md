# Stored Procedure: `ThucChay_GetSumFilterCondition_Label_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-10 23:05:04.957000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.937000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
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
CREATE PROCEDURE [dbo].[ThucChay_GetSumFilterCondition_Label_v2]     
    @PageIndex				INT = 1,
	@RecordCount			INT = 10,
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
			@ChucDanhID			INT
	
	SET @DauNhay =''''
	
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
					@TenNhanHangListParam NVARCHAR(2000),
					@TenKhachHangListParam NVARCHAR(2000),
					@DonViTinhListParam		nvarchar(200)'
					
	DECLARE @TempTable AS TABLE (
		GroupFieldName		NVARCHAR(2000), 
		GiaTriThayDoi		FLOAT, 
		ThanhTienNoiBo		FLOAT, 
		ThanhTienKhuyenMai  FLOAT, 
		ThanhTienThucThu	FLOAT,
		ThanhTienThucThuNB	FLOAT, 
		ThanhTienThucThuTC	FLOAT
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
												@DonViTinhList)
												
	PRINT @FilterString;												
	
	SET @Sql = '
		SELECT
			GroupFieldName,
			SUM(GiaTriThayDoi) GiaTriThayDoi,				
			SUM(ThanhTienNoiBo) ThanhTienNoiBo,
			SUM(ThanhTienKhuyenMai) ThanhTienKhuyenMai,
			SUM(ThanhTienThucThu) ThanhTienThucThu,
			SUM(ThanhTienNoiBo + GiaTriThayDoiNB) ThanhTienThucThuNB,
			SUM(ThanhTienThucThu + GiaTriThayDoiTC) ThanhTienThucThuTC
		FROM
		(
			SELECT
				CASE WHEN (hd.NhanHopDong = ' + @DauNhay + '' + @DauNhay + ' OR hd.NhanHopDong IS NULL) THEN ' + @DauNhay + '-' + @DauNhay + '
						ELSE hd.NhanHopDong 
				END AS GroupFieldName,
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
		@TenNhanHangListParam			= @TenNhanHangList,	
		@TenKhachHangListParam			= @TenKhachHangList,
		@DonViTinhListParam				= @DonViTinhList;
		
	-- Admarket data
	SET @SqlAdmarket = '
		SELECT
			GroupFieldName,
			SUM(GiaTriThayDoi) GiaTriThayDoi,				
			SUM(ThanhTienNoiBo) ThanhTienNoiBo,
			SUM(ThanhTienKhuyenMai) ThanhTienKhuyenMai,
			SUM(ThanhTienThucThu) ThanhTienThucThu,
			SUM(ThanhTienNoiBo + GiaTriThayDoiNB) ThanhTienThucThuNB,
			SUM(ThanhTienThucThu + GiaTriThayDoiTC) ThanhTienThucThuTC
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
		@TenNhanHangListParam			= @TenNhanHangList,	
		@TenKhachHangListParam			= @TenKhachHangList,
		@DonViTinhListParam				= @DonViTinhList;
		
		
	SELECT 
		T.GroupFieldName,
		T.GiaTriThayDoi,
		T.ThanhTienNoiBo,
		T.ThanhTienKhuyenMai,
		T.ThanhTienThucThu,
		T.ThanhTienThucThuNB,
		T.ThanhTienThucThuTC
	FROM
	(
		SELECT 
			T1.GroupFieldName, 
			SUM(T1.GiaTriThayDoi)       AS GiaTriThayDoi, 
			SUM(T1.ThanhTienNoiBo)		AS ThanhTienNoiBo, 
			SUM(T1.ThanhTienKhuyenMai)	AS ThanhTienKhuyenMai, 
			SUM(T1.ThanhTienThucThu)	AS ThanhTienThucThu,
			SUM(T1.ThanhTienThucThuNB)	AS ThanhTienThucThuNB, 
			SUM(T1.ThanhTienThucThuTC)	AS ThanhTienThucThuTC,
			ROW_NUMBER() OVER (ORDER BY T1.GroupFieldName ASC) AS num
		FROM @TempTable T1	
		GROUP BY
			T1.GroupFieldName
	)T
	WHERE 
		T.num BETWEEN (@PageIndex-1)*@RecordCount + 1 AND @PageIndex*@RecordCount;
END

```
