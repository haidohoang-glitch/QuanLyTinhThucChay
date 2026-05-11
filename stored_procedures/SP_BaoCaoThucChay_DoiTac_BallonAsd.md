# Stored Procedure: `BaoCaoThucChay_DoiTac_BallonAsd`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:07.737000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.473000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ColumnSort` | `nvarchar(100)` | No |
| `@OrderBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-16
-- Description:	BaoCaoThucChay_DoiTac_BallonAsd
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_BallonAsd]
	-- Add the parameters for the stored procedure here
	@PageIndex int,
	@RecordCount int,
	@StartDate Datetime,
	@EndDate Datetime,
	@DmWebsiteREFList nvarchar(2000),
	@TenDangNhap nvarchar(50),
	@ColumnSort nvarchar(50),
	@OrderBy nvarchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @Sql nvarchar(4000)
    DECLARE @DauNhay nvarchar(50)
    DECLARE @FillterString nvarchar(4000)
    DECLARE @OrderByString nvarchar(2000)
    DECLARE @DmSanPhamREFList nvarchar(50) = ''
    DECLARE @SoHopDongList nvarchar(50) = ''
    
    SET @DauNhay = ''''
		
	SET @FillterString = dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
    
    IF @ColumnSort = 'SoHopDong'
		SET @OrderByString = 'SoHopDong'
	ELSE IF @ColumnSort = 'SoLuong'
		SET @OrderByString = 'SUM(SoLuongThucChay/1000)'
	ELSE IF @ColumnSort = 'ThanhTien'
		SET @OrderByString = 'SUM(ThanhTienSauTrietKhauThucChay)'
    
    SET @Sql = '
		SELECT  TOP ' + CONVERT(NVARCHAR,@RecordCount) + '
			T.SoHopDong,
			dbo.FormatNumber(T.SoLuong) AS SoLuong,
			dbo.FormatNumber(T.ThanhTien) AS ThanhTien,
			T.num As STT  
		FROM
		(
			SELECT   
				SoHopDong, 
				SUM(SoLuongThucChay)/1000 AS SoLuong, 
				SUM(ThanhTienSauTrietKhauThucChay) AS ThanhTien,
				ROW_NUMBER() OVER (ORDER BY ' + @OrderByString + ' ' + @OrderBy + ') AS num
			FROM ThucChayDaTinh 
			WHERE 1=1 AND DmSanPhamREF = 339 AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay + 'NB%' + @DauNhay 
    
    SET @Sql += @FillterString   
    
    SET @Sql += ' GROUP BY SoHopDong
		)T 
		WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount)
	
	--SET @Sql += ' ORDER BY ' +  @OrderByString + ' ' + @OrderBy
    
    PRINT @Sql
    
    EXEC(@Sql)
    
END

```
