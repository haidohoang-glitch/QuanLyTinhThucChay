# Stored Procedure: `BaoCaoThucChay_DoiTac_CPM_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:08.167000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.560000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(100)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(100)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-16
-- Description:	BaoCaoThucChay_DoiTac_BallonAsd
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_CPM_TotalRowValue]
	-- Add the parameters for the stored procedure here
	@StartDate Datetime,
	@EndDate Datetime,
	@DmSanPhamREFList nvarchar(50),
	@DmWebsiteREFList nvarchar(2000),
	@SoHopDongList nvarchar(50),
	@TenDangNhap nvarchar(50),
	@IsNoiBo INT,
	@DmHinhThucQuangCaoList	NVARCHAR(50)
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
		SET @FillterString += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')'
		
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	SET @FillterString += ' AND (SoLuongThucChay <> 0 OR ThanhTienSauTrietKhauThucChay <> 0 OR SoLuongThucChayKM <> 0 OR ThanhTienKM <> 0)'
    
    SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'
    
 --   IF @IsNoiBo = 1
	--	SET @FillterString =  @FillterString + ' AND UPPER(SoHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay
	--ELSE IF @IsNoiBo = 0
	--	SET @FillterString = @FillterString + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
		
    SET @Sql = '
		SELECT  
			COUNT(T.SoHopDong) AS TotalRow,
			dbo.FormatNumber(SUM(T.SoLuongThucChay)) AS TongSoLuongThucChay,
			dbo.FormatNumber(SUM(T.SoLuongKhuyenMai)) AS TongSoLuongKhuyenMai,
			--dbo.FormatNumber(SUM(T.ThanhTienKhuyenMai)) AS TongThanhTienKhuyenMai,
			dbo.FormatNumber(SUM(T.ThanhTienThucChay)) AS TongThanhTienThucChay
			
		FROM
		(
			SELECT   
				SoHopDong, 
				SUM(SoLuongThucChay) AS SoLuongThucChay, 
				SUM(SoLuongThucChayKM) AS SoLuongKhuyenMai,
				SUM(dbo.ThucChay_GetThanhTienThucChayKenh(SoHopDong,ThanhTienSauTrietKhauThucChay,'+@DauNhay + @TenDangNhap + @DauNhay +')) AS ThanhTienThucChay,
				SUM(ThanhTienKM) AS ThanhTienKhuyenMai
			FROM ThucChayDaTinh 
			WHERE 1 = 1 '
    
    SET @Sql += @FillterString   
    
    SET @Sql += ' GROUP BY SoHopDong
		)T 
		'
	
	--SET @Sql += ' ORDER BY ' +  @OrderByString + ' ' + @OrderBy
    
    PRINT @Sql
    
    EXEC(@Sql)
    
END

```
