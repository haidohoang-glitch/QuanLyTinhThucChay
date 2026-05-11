# Stored Procedure: `ThucChay_GetSumFilterCondition_Label_TotalRow`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-23 17:53:45.797000
- **Ngày sửa cuối**: 2014-11-19 12:16:54

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
| `@TenNhanHangList` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Modified date: 2013-09-02
-- Description:	ThucChay_GetSumFilterCondition 
-- =============================================

CREATE PROCEDURE [dbo].[ThucChay_GetSumFilterCondition_Label_TotalRow] 
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
	@DmHinhThucQuangCaoList NVARCHAR(200)
	,@DmBannerREFList NVARCHAR(200)
	,@TenNhanHangList NVARCHAR(2000)		
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql NVARCHAR(MAX);
    DECLARE @DauNhay NVARCHAR(50);
    Declare @GroupByFildID nvarchar(4000);
	Declare @GroupByFild nvarchar(4000);
	Declare @FilterString nvarchar(4000);
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT, @ChucDanhID INT
	DECLARE @TuNgay DATETIME, @DenNgay DATETIME	
	DECLARE @MinDate DATETIME, @MaxDate DATETIME
	DECLARE @SqlCommand VARCHAR(MAX);
	DECLARE @Count INT
	
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
					@TenNhanHangListParam NVARCHAR(2000)'
	
	SET @FilterString = dbo.GetThucChayLabelFilterString(@StartDate,
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
												@TenNhanHangList)
	PRINT @FilterString;
	
	SET @Sql = '
SELECT 
	COUNT(NhanHang) MaxRecords
FROM
(
	SELECT 
		hd.NhanHopDong NhanHang
	FROM ThucChayDaTinh tcdt
		INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
	WHERE ' + @FilterString + '
	GROUP BY hd.NhanHopDong
)T'
	
	PRINT @Sql;
	EXECUTE sp_executesql @Sql, 
		@Pamrams, 
		@GroupFieldNameParam = @GroupFieldName,
		@StartDateParam = @StartDate,
		@EndDateParam = @EndDate,
		@DmSanPhamREFListParam = @DmSanPhamREFList,
		@DmWebsiteREFListParam = @DmWebsiteREFList,
		@SoHopDongListParam = @SoHopDongList,
		@DmPhongBanREFListParam = @DmPhongBanREFList,
		@DmBoPhanREFListParam = @DmBoPhanREFList,
		@DmNhomLamViecREFListParam = @DmNhomLamViecREFList,
		@TenNhanVienListParam = @TenNhanVienList,
		@TenDangNhapParam = @TenDangNhap,
		@DmHinhThucQuangCaoListParam = @DmHinhThucQuangCaoList,
		@DmBannerREFListParam = @DmBannerREFList,
		@TenNhanHangListParam = @TenNhanHangList
	
END

```
