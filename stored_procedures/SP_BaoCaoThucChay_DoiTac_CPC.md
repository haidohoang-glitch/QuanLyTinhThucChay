# Stored Procedure: `BaoCaoThucChay_DoiTac_CPC`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:10.910000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.380000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ColumnSort` | `nvarchar(100)` | No |
| `@OrderBy` | `nvarchar(100)` | No |
| `@IsNoiBo` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_CPC]
	-- Add the parameters for the stored procedure here
	@PageIndex int,
	@RecordCount int,
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(2000),
	@DmWebsiteREFList nvarchar(2000),
	@SoHopDongList nvarchar(2000),
	@TenDangNhap nvarchar(50),
	@ColumnSort nvarchar(50),
	@OrderBy nvarchar(50),
	@IsNoiBo INT
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
	SET @FillterString += ' AND DmWebsiteREF in (134,182,56,137,254,85)'
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	
	--IF @IsNoiBo = 1
	--	SET @FillterString =  @FillterString + ' AND UPPER(TenMaHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay
	--ELSE IF @IsNoiBo = 0
	--	SET @FillterString = @FillterString + ' AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
		
	IF @ColumnSort = 'TongViewThucChay'
		SET @OrderByString = 'SUM(TongViewThucChay)'
	ELSE IF @ColumnSort = 'TongClickThucChay'
		SET @OrderByString = 'SUM(TongClickThucChay)'
	ELSE IF @ColumnSort = 'ThanhTienThucChay'
		SET @OrderByString = 'SUM(ThanhTienSauTrietKhauThucChay)'
	ELSE IF @ColumnSort = 'NgayThucHien'
		SET @OrderByString = 'NgayThucHien'
		
	SET @OrderByString = 'NgayThucHien'
	
	IF @DmSanPhamREFList = '144'
	BEGIN
		SET @Sql = '
		SELECT TOP ' + CONVERT(NVARCHAR,@RecordCount) + @DauNhay +
			'Mua Online' + @DauNhay + ' AS SoHopDong,
			0 AS SoLuongKhuyenMai,
			dbo.FormatNumber(T.TongClickThucChay) AS SoLuongThucChay,
			dbo.FormatNumber(T.ThanhTienThucChay) AS ThanhTienThucChay
		FROM
		(
			SELECT
				SUM(ttView) AS TongViewThucChay,
				SUM(ttClick) AS TongClickThucChay,
				SUM(ttClick*Price/1.1) AS ThanhTienThucChay,
				ROW_NUMBER() OVER (ORDER BY SUM(ttClick) DESC) num
			FROM ThucChayAdmarketPublisher A
			WHERE 1 = 1 AND DmSanPhamREF = 144 
		'   		
	
		SET @Sql += @FillterString
	
		SET @Sql += '		
			 
		)T
		WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount)
	END
	ELSE
	BEGIN
		SET @FillterString += ' AND (SoLuongThucChay <> 0 OR ThanhTienSauTrietKhauThucChay <> 0 OR SoLuongThucChayKM <> 0 OR ThanhTienKM <> 0)'
	
		SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'		
		
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
					ROW_NUMBER() OVER (ORDER BY SoHopDong) AS num
				FROM ThucChayDaTinh 
				WHERE 1=1 ' + @FillterString + '
				GROUP BY SoHopDong
			)T
			WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount)
   
	END
		
	PRINT @Sql;
	EXEC (@Sql);
END

```
