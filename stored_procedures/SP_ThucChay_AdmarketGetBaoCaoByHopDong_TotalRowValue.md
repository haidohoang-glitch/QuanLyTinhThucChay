# Stored Procedure: `ThucChay_AdmarketGetBaoCaoByHopDong_TotalRowValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:25.090000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.847000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDongList` | `varchar(2000)` | No |
| `@DmSanPhamREFList` | `varchar(2000)` | No |
| `@TenDangNhap` | `varchar(50)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-16
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_AdmarketGetBaoCaoByHopDong_TotalRowValue]
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@SoHopDongList VARCHAR(2000),
	@DmSanPhamREFList VARCHAR(2000),
	@TenDangNhap VARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @SqlCommandString VARCHAR(MAX),
			@SqlSelectString VARCHAR(MAX),
			@SqlFilterString VARCHAR(MAX),
			@SqlSecurityString VARCHAR(MAX);
	
	DECLARE @DauNhay VARCHAR(10)='''';
	
	
	SET @SqlSelectString = '
		SELECT 
			ISNULL(A.SoHopDong,' + @DauNhay + '-' + @DauNhay + ') AS SoHopDong
			,SUM(A.TongClick) AS TongClick
			,SUM(A.TongView) AS TongView
			,SUM(A.TongTienThucChay) AS TongTienThucChay
			,ROW_NUMBER() OVER (ORDER BY A.SoHopDong) AS num
			--,A.NgayThucHien
		FROM ThucChayDaTinhAdmarketHopDong A
		WHERE 
	'
	SET @SqlSecurityString = '(';
	SET @SqlSecurityString += dbo.GetSecurityDataByTenDangNhap(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap');

	SET @SqlSecurityString = @SqlSecurityString + ' OR (' + dbo.GetSecurityWebsiteProductAdmarket(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap','DmSanPhamREF','DmWebsiteREF') + '))';
	
	SET @SqlFilterString = '';
	IF @SoHopDongList <> ''
		SET @SqlFilterString = @SqlFilterString + ' AND SoHopDong IN (' + @SoHopDongList + ')';
	--IF @DmSanPhamREFList <> ''
	--	SET @SqlFilterString = @SqlFilterString + ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')';
	
	SET @SqlCommandString = @SqlSelectString + @SqlSecurityString + @SqlFilterString;
	
	SET @SqlCommandString += '
		GROUP BY A.SoHopDong
	'

	SET @SqlCommandString = '
		SELECT 
			 COUNT(T.SoHopDong) AS TotalRows,
			 dbo.FormatNumber(SUM(T.TongClick)) TongClick,
			 dbo.FormatNumber(SUM(T.TongView)) TongView,
			 dbo.FormatNumber(SUM(T.TongTienThucChay)) TongTienThucChay
		FROM 
		(' 
			+ @SqlCommandString + 
		') T
		'
		
			
	
	--PRINT @SqlSelectString;
	--PRINT @SqlSecurityString;
	PRINT @SqlCommandString;
	
	EXEC (@SqlCommandString);
END

```
