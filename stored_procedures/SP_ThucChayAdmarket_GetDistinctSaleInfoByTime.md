# Stored Procedure: `ThucChayAdmarket_GetDistinctSaleInfoByTime`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-25 17:19:26.453000
- **Ngày sửa cuối**: 2014-10-14 10:39:50.927000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GroupFieldName` | `varchar(50)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@UserName` | `varchar(50)` | No |
| `@DmPhongBanREFList` | `varchar(2000)` | No |
| `@DmBoPhanREFList` | `varchar(2000)` | No |
| `@DmNhomLamViecREFList` | `varchar(2000)` | No |
| `@DmTenNhanVienREFList` | `varchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ	
-- Create date: 2013-12-09
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayAdmarket_GetDistinctSaleInfoByTime]
	-- Add the parameters for the stored procedure here
	@GroupFieldName varchar(50),
	@StartDate DATETIME,
	@EndDate DATETIME,
	@UserName VARCHAR(50),
	@DmPhongBanREFList VARCHAR(2000),
	@DmBoPhanREFList VARCHAR(2000),
	@DmNhomLamViecREFList VARCHAR(2000),
	@DmTenNhanVienREFList varchar(2000)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @SqlCommandString NVARCHAR(MAX),
			@SqlFilterString NVARCHAR(MAX),
			@SqlSecurityString NVARCHAR(MAX);

	declare @Params nvarchar(2000)
	SET @Params = N'
					@PramGroupFieldName varchar(50),
					@PramStartDate DATETIME,
					@PramEndDate DATETIME,
					@PramUserName VARCHAR(50),
					@PramDmPhongBanREFList VARCHAR(2000),
					@PramDmBoPhanREFList VARCHAR(2000),
					@PramDmNhomLamViecREFList VARCHAR(2000),
					@PramDmTenNhanVienREFList varchar(2000)
	'
	
	DECLARE @DauNhay VARCHAR(10)='''';
	DECLARE @ID varchar(50);

	IF @GroupFieldName = 'TenPhongBan'
		SET @ID = 'DmPhongBanREF';
	ELSE IF @GroupFieldName = 'TenNhanVien'
		SET @ID = 'TenDangNhap';
	
	SET @SqlCommandString = '
		SELECT DISTINCT 
			' + @ID + ' AS ID, '
			+ @GroupFieldName + ' AS Name
		FROM
			ThucChayDaTinhAdmarketSale
		WHERE 
	';
	
	SET @SqlSecurityString = '(';

	SET @SqlSecurityString += dbo.GetSecurityDataByTenDangNhap(@StartDate,@EndDate,@UserName,'NgayThucHien','TenDangNhap');
	
	SET @SqlSecurityString = @SqlSecurityString + ' OR (' + dbo.GetSecurityWebsiteProductAdmarket(@StartDate,@EndDate,@UserName,'NgayThucHien','TenDangNhap','DmSanPhamREF','DmWebsiteREF') + ')';
	SET @SqlSecurityString += ')';

	SET @SqlFilterString = '';

	SET @SqlFilterString = @SqlFilterString + dbo.ThucChayAdmarket_GetCommandFilterString(@DmPhongBanREFList,@DmBoPhanREFList,@DmNhomLamViecREFList,@DmTenNhanVienREFList)
	--IF @DmPhongBanREFList <> '' 
	--	SET @SqlFilterString = ' AND DmPhongBanREF IN (' + @DmPhongBanREFList + ')';
	--IF @DmBoPhanREFList <> '' 
	--	SET @SqlFilterString = ' AND DmBoPhanREF IN (' + @DmBoPhanREFList + ')';

	--IF @DmNhomLamViecREFList <> '' 
	--	SET @SqlFilterString = ' AND DmBoPhanREF IN (' + @DmNhomLamViecREFList + ')';

	--IF @DmTenNhanVienREFList <> '' 
	--	SET @SqlFilterString = ' AND TenDangNhap IN (' + @DmTenNhanVienREFList + ')';
		
	SET @SqlCommandString = @SqlCommandString + @SqlSecurityString + @SqlFilterString;
	
	SET @SqlCommandString += '
		ORDER BY ' + @GroupFieldName
	
	
	PRINT @SqlCommandString;
	
	--EXEC (@SqlCommandString); 
	EXECUTE sp_executesql @SqlCommandString ,@Params, 
	@PramGroupFieldName = @GroupFieldName,
	@PramStartDate = @StartDate,
	@PramEndDate = @EndDate,
	@PramUserName = @UserName,
	@PramDmPhongBanREFList = @DmPhongBanREFList,
	@PramDmBoPhanREFList = @DmBoPhanREFList,
	@PramDmNhomLamViecREFList = @DmNhomLamViecREFList,
	@PramDmTenNhanVienREFList = @DmTenNhanVienREFList
	
END

```
