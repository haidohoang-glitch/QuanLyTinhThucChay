# Stored Procedure: `BaoCaoThucChay_DoiTac_CPC_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 11:47:11.270000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.357000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@DmWebsiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[BaoCaoThucChay_DoiTac_CPC_TotalRowValue]
	-- Add the parameters for the stored procedure here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(2000),
	@DmWebsiteREFList nvarchar(2000),
	@SoHopDongList nvarchar(2000),
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
	SET @FillterString += ' AND DmWebsiteREF in (134,182,56,137,254,85)'
	
	IF @DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1'
		SET @FillterString += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')'
		
	SET @FillterString += dbo.GetThucChayDoiTacFilterString(@StartDate,@EndDate,@DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,@TenDangNhap)
	
	--IF @IsNoiBo = 1
	--	SET @FillterString =  @FillterString + ' AND UPPER(TenMaHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay
	--ELSE IF @IsNoiBo = 0
	--	SET @FillterString = @FillterString + ' AND UPPER(TenMaHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay
	IF @DmSanPhamREFList = '144'
	BEGIN	
		SET @Sql = '
		SELECT 
			COUNT(T.SoHopDong) AS TotalRow,
			dbo.FormatNumber(SUM(T.TongViewThucChay)) AS SoLuongKhuyenMai,
			dbo.FormatNumber(SUM(T.TongClickThucChay)) AS SoLuongThucChay,
			dbo.FormatNumber(SUM(T.ThanhTienThucChay)) AS ThanhTienThucChay
		FROM
		(
			SELECT
				' + @DauNhay + 'Mua Online' + @DauNhay + ' as SoHopDong,
				0 AS TongViewThucChay,
				SUM(ttClick) AS TongClickThucChay,
				SUM(ttClick*Price/1.1) AS ThanhTienThucChay
			FROM ThucChayAdmarketPublisher A
			WHERE 1 = 1 AND DmSanPhamREF = 144 
		'
	
		SET @Sql += @FillterString
	
		SET @Sql += '		    
		)T
		'
	END	
	ELSE
	BEGIN
		SET @FillterString += ' AND (SoLuongThucChay <> 0 OR ThanhTienSauTrietKhauThucChay <> 0 OR SoLuongThucChayKM <> 0 OR ThanhTienKM <> 0)'
	
		SET @FillterString = @FillterString + ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay + ')'		
		
		SET @Sql = '
			SELECT  
				COUNT(T.SoHopDong) AS TotalRow,
				dbo.FormatNumber(SUM(T.SoLuongThucChay)) AS SoLuongThucChay,
				dbo.FormatNumber(SUM(T.SoLuongKhuyenMai)) AS SoLuongKhuyenMai,
				--dbo.FormatNumber(SUM(T.ThanhTienKhuyenMai)) AS TongThanhTienKhuyenMai,
				dbo.FormatNumber(SUM(T.ThanhTienThucChay)) AS ThanhTienThucChay
			
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
	END
	PRINT @Sql;
	EXEC (@Sql);
END

```
