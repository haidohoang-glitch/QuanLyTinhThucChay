# Stored Procedure: `ThucChay_AdmarketGetBaoCaoByHopDong_Print`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:25.530000
- **Ngày sửa cuối**: 2014-11-19 12:17:55.190000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDongList` | `nvarchar(4000)` | No |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-17-09
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_AdmarketGetBaoCaoByHopDong_Print]
	-- Add the parameters for the stored procedure here
	@GroupFieldName NVARCHAR(50),
	@StartDate DATETIME,
	@EndDate DATETIME,
	@SoHopDongList NVARCHAR(2000),
	@DmSanPhamREFList NVARCHAR(2000),
	@TenDangNhap NVARCHAR(50)
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
	DECLARE @GroupByField NVARCHAR(200);
	
	
	SET @SqlSelectString = '
			ROW_NUMBER() OVER (ORDER BY A.SoHopDong) AS num
			,A.SoHopDong AS SoHopDong
			,SUM(A.TongClick) AS TongClick
			,SUM(A.TongView) AS TongView
			,SUM(A.TongTienThucChay) AS ThanhTienThucThu
	'
	
	SET @GroupByField = 'A.SoHopDong';
	
	
	IF @GroupFieldName = 'TenSanPham'
	BEGIN
		SET @SqlSelectString += ', A.DmSanPhamREF
								 , A.TenSanPham ';
		SET @GroupByField += ', A.DmSanPhamREF, A.TenSanPham';							
	END
	
	SET @SqlSecurityString = '(';
	
	SET @SqlSecurityString += dbo.GetSecurityDataByTenDangNhap(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap');

	SET @SqlSecurityString += ' OR (' + dbo.GetSecurityWebsiteProductAdmarket(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap','DmSanPhamREF','DmWebsiteREF') + ')';
	
	SET @SqlSecurityString += ')';
	
	SET @SqlFilterString = '';
	IF @SoHopDongList <> ''
		SET @SqlFilterString = @SqlFilterString + ' AND SoHopDong IN (' + @SoHopDongList + ')';
	--ELSE IF @SoHopDongList = ''
	--	SET @SqlFilterString = @SqlFilterString + ' AND SoHopDong IS NULL';
	IF @DmSanPhamREFList <> ''
		SET @SqlFilterString = @SqlFilterString + ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')';
	
	SET @SqlCommandString = '
		SELECT ' + @SqlSelectString + '
		FROM ThucChayDaTinhAdmarketHopDong A 
		WHERE ' + @SqlSecurityString + @SqlFilterString + '
		GROUP BY ' + @GroupByField + '
		ORDER BY ' + @GroupByField;

	--PRINT @SqlSelectString;
	--PRINT @SqlSecurityString;
	PRINT @SqlCommandString;
	
	EXEC (@SqlCommandString);
END



```
