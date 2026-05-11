# Stored Procedure: `ThucChay_AdmarketGetBaoCaoByHopDong_Detail`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:25.313000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.887000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDongList` | `varchar(2000)` | No |
| `@DmSanPhamREFList` | `varchar(2000)` | No |
| `@TenDangNhap` | `varchar(50)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-17-09
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_AdmarketGetBaoCaoByHopDong_Detail]
	-- Add the parameters for the stored procedure here
	@PageIndex INT,
	@PageSize INT,
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
			A.SoHopDong AS SoHopDong
			,A.DmSanPhamREF
			,A.TenSanPham
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
	
	PRINT @SoHopDongList;
	SET @SqlFilterString = '';
	IF @SoHopDongList <> ''
		SET @SqlFilterString = @SqlFilterString + ' AND SoHopDong IN (' + @SoHopDongList + ')';
	ELSE IF @SoHopDongList = ''
		SET @SqlFilterString = @SqlFilterString + ' AND SoHopDong IS NULL';
	IF @DmSanPhamREFList <> ''
		SET @SqlFilterString = @SqlFilterString + ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')';
	
	SET @SqlCommandString = @SqlSelectString + @SqlSecurityString + @SqlFilterString;
	
	SET @SqlCommandString += '
		GROUP BY A.SoHopDong, A.DmSanPhamREF, A.TenSanPham
		
	'

	SET @SqlCommandString = '
		SELECT 
			 T.SoHopDong,
			 T.DmSanPhamREF,T.TenSanPham,
			 dbo.FormatNumber(SUM(T.TongClick)) TongClick,
			 dbo.FormatNumber(SUM(T.TongView)) TongView,
			 dbo.FormatNumber(SUM(T.TongTienThucChay)) TongTienThucChay
			 --T.num STT
		FROM 
		(' 
			+ @SqlCommandString + 
		') T
		WHERE T.num BETWEEN ' + CONVERT(varchar(50),(@PageIndex-1)*@PageSize + 1) + ' AND ' + CONVERT(varchar(50),@PageIndex*@PageSize) + '
		GROUP BY T.SoHopDong, T.DmSanPhamREF,T.TenSanPham
		'
		
			
	
	--PRINT @SqlSelectString;
	--PRINT @SqlSecurityString;
	PRINT @SqlCommandString;
	
	EXEC (@SqlCommandString);
END

```
