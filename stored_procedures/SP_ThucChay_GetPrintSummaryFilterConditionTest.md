# Stored Procedure: `ThucChay_GetPrintSummaryFilterConditionTest`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-28 15:11:04.487000
- **Ngày sửa cuối**: 2014-10-14 10:39:54.447000

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

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChay_GetPrintSummaryFilterConditionTest] 
    -- Add the parameters for the stored procedure here
    --@PageIndex INT = 1,
	--@RecordCount INT = 10,
	@GroupFieldName nvarchar(50),
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;
    --Select
    
    DECLARE @Sql NVARCHAR(4000);
    DECLARE @DauNhay NVARCHAR(50);
    Declare @GroupByFildID nvarchar(4000);
	Declare @GroupByFild nvarchar(4000);
	Declare @FilterString nvarchar(4000);
	DECLARE @Test NVARCHAR(4000);
	
    SET @DauNhay = '''';
    
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
		SET @GroupByFild = 'TenNhanVien'
		SET @GroupByFildID = 'TenNhanVien AS ID,' 
	END
	
	SET @FilterString =  dbo.GetThucChayFilterString(
														@StartDate ,
														@EndDate ,
														@DmSanPhamREFList ,
														@DmWebsiteREFList ,
														@SoHopDongList ,
														@DmPhongBanREFList ,
														@DmBoPhanREFList ,
														@DmNhomLamViecREFList ,
														@TenNhanVienList 
													)

    
    SET @Sql = '
			SELECT T.' + @GroupFieldName + ',T.ID,T.DonViTinh,
				SUM(GiaTriThayDoi) AS GiaTriThayDoi,
				SUM(SoLuongHopDongNoiBo) AS SoLuongHopDongNoiBo,
				SUM(SoLuongHopDongKhuyenMai) AS SoLuongHopDongKhuyenMai,
				SUM(SoLuongHopDongThucThu) AS SoLuongHopDongThucThu,
				SUM(SoLuongThucChayNoiBo) AS SoLuongThucChayNoiBo,
				SUM(SoLuongThucChayKhuyenMai) AS SoLuongThucChayKhuyenMai,
				SUM(SoLuongThucChayThucThu) AS SoLuongThucChayThucThu,
				ROUND(SUM(ThanhTienThucChayNoiBo),0) AS ThanhTienThucChayNoiBo,
				ROUND(SUM(ThanhTienThucChayKhuyenMai),0) AS ThanhTienThucChayKhuyenMai,
				ROUND(SUM(ThanhTienThucThu),0) AS ThanhTienThucThu,
				ROW_NUMBER() OVER (ORDER BY ID) AS num
			FROM 
			( 
			' 
				+ dbo.ThucChay_GenSQLCommandDataSummaryByFillterCondition(@GroupFieldName,
																			@GroupByFildID,
																			@GroupByFild,
																			@StartDate ,
																			@EndDate ,
																			@DmSanPhamREFList ,
																			@DmWebsiteREFList ,
																			@SoHopDongList ,
																			@DmPhongBanREFList ,
																			@DmBoPhanREFList ,
																			@DmNhomLamViecREFList ,
																			@TenNhanVienList) + 
			') T
			GROUP BY T.ID,T.DonViTinh,' + @GroupFieldName
    
    PRINT @Sql;
    EXEC (@Sql);
END


```
