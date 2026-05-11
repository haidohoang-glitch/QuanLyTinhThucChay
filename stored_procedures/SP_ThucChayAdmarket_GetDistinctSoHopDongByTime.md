# Stored Procedure: `ThucChayAdmarket_GetDistinctSoHopDongByTime`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:25.980000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@UserName` | `varchar(50)` | No |
| `@SoHopDongList` | `varchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ	
-- Create date: 2013-12-09
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayAdmarket_GetDistinctSoHopDongByTime]
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@UserName VARCHAR(50),
	@SoHopDongList VARCHAR(2000)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @SqlCommandString VARCHAR(MAX),
			@SqlFilterString VARCHAR(MAX),
			@SqlSecurityString VARCHAR(MAX);
	
	DECLARE @DauNhay VARCHAR(10)='''';
	
	SET @SqlCommandString = '
		SELECT DISTINCT 
			SoHopDong AS ID,
			SoHopDong AS Name
		FROM
			ThucChayDaTinhAdmarketHopDong
		WHERE 
	';
	
	SET @SqlSecurityString = dbo.GetSecurityDataByTenDangNhap(@StartDate,@EndDate,@UserName,'NgayThucHien','TenDangNhap');
	--SET @SqlSecurityString = @SqlSecurityString + ')';
	SET @SqlSecurityString = @SqlSecurityString + ' OR (' + dbo.GetSecurityWebsiteProductAdmarket(@StartDate,@EndDate,@UserName,'NgayThucHien','TenDangNhap','DmSanPhamREF','DmWebsiteREF') + ')';

	SET @SqlFilterString = '';
	IF @SoHopDongList <> '' 
		SET @SqlFilterString = ' AND SoHopDong IN (' + @SoHopDongList + ')';
		
	SET @SqlCommandString = @SqlCommandString + @SqlFilterString + @SqlSecurityString;
	
	SET @SqlCommandString += '
		ORDER BY SoHopDong
	'
	
	PRINT @SqlCommandString;
	
	EXEC (@SqlCommandString); 
	
END

```
