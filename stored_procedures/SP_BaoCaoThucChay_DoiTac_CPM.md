# Stored Procedure: `BaoCaoThucChay_DoiTac_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:07.950000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(100)` | No |
| `@DmWebsiteREFList` | `nvarchar(100)` | No |
| `@SoHopDongList` | `nvarchar(100)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ColumnSort` | `nvarchar(100)` | No |
| `@OrderBy` | `nvarchar(100)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-16
-- Description:	BaoCaoThucChay_DoiTac_BallonAsd
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_CPM]
	-- Add the parameters for the stored procedure here
	@PageIndex int,
	@RecordCount int,
	@StartDate Datetime,
	@EndDate Datetime,
	@DmSanPhamREFList nvarchar(50),
	@DmWebsiteREFList nvarchar(50),
	@SoHopDongList nvarchar(50),	
	@TenDangNhap nvarchar(50),
	@ColumnSort nvarchar(50),
	@OrderBy nvarchar(50),
	@IsNoiBo INT,
	@DmHinhThucQuangCaoList NVARCHAR(200)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Sql nvarchar(4000)
    DECLARE @DauNhay nvarchar(50)
    DECLARE @FillterString nvarchar(4000)
    DECLARE @OrderByString nvarchar(2000)
    
    SET @DauNhay = ''''
	
	SET @FillterString = ' AND IsPheDuyet = 1'	
	
	IF @DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1'
		SET @FillterString += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')';
	
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	SET @FillterString += ' AND (SoLuongThucChay <> 0 OR ThanhTienSauTrietKhauThucChay <> 0 OR SoLuongThucChayKM <> 0 OR ThanhTienKM <> 0)'
	
	SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'
	--IF @IsNoiBo = 1
	--	SET @FillterString =  @FillterString + ' AND (UPPER(SoHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay + ' OR UPPER(SoHopDong) LIKE ' + @DauNhay +'%SH%' + @DauNhay + ')'
	--ELSE IF @IsNoiBo = 0
	--	SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ')'
    
    IF @ColumnSort = 'SoHopDong'
		SET @OrderByString = 'SoHopDong'
	ELSE IF @ColumnSort = 'SoLuongThucChay'
		SET @OrderByString = 'SUM(SoLuongThucChay)'
	ELSE IF @ColumnSort = 'ThanhTienThucChay'
		SET @OrderByString = 'SUM(ThanhTienSauTrietKhauThucChay)'
	ELSE IF @ColumnSort = 'SoLuongKhuyenMai'
		SET @OrderByString = 'SUM(SoLuongThucChayKM)'
	ELSE IF @ColumnSort = 'ThanhTienKhuyenMai'
		SET @OrderByString = 'SUM(ThanhTienKM)'
    
    SET @Sql = '
		SELECT  TOP ' + CONVERT(NVARCHAR,@RecordCount) + '
			T.SoHopDong,
			dbo.FormatNumber(T.SoLuongKhuyenMai) AS SoLuongKhuyenMai,
			dbo.FormatNumber(T.SoLuongThucChay) AS SoLuongThucChay,		
			--dbo.FormatNumber(T.ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
			dbo.FormatNumber(T.ThanhTienThucChay) AS ThanhTienThucChay
		FROM
		(
			SELECT   
				SoHopDong, 
				SUM(SoLuongThucChay) AS SoLuongThucChay, 
				SUM(SoLuongThucChayKM) AS SoLuongKhuyenMai,
				SUM(dbo.ThucChay_GetThanhTienThucChayKenh(SoHopDong,ThanhTienSauTrietKhauThucChay,'+@DauNhay + @TenDangNhap + @DauNhay +')) AS ThanhTienThucChay,
				SUM(ThanhTienKM) AS ThanhTienKhuyenMai,
				ROW_NUMBER() OVER (ORDER BY ' + @OrderByString + ' ' + @OrderBy + ') AS num
			FROM ThucChayDaTinh 
			WHERE 1=1 '
    
    SET @Sql += @FillterString   
    
    SET @Sql += ' GROUP BY SoHopDong
		)T 
		WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount)
	
	--SET @Sql += ' ORDER BY ' +  @OrderByString + ' ' + @OrderBy
    
    PRINT @Sql
    
    EXEC(@Sql)
    
END

```
