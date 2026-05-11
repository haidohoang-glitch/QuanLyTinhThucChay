# Stored Procedure: `ThucChay_TablePaging`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-09 15:48:32.853000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_TablePaging]
	-- Add the parameters for the stored procedure here
	@PageIndex Int,
	@RecordCount Int,
	@GroupFieldName nvarchar(50),
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    -- statements for procedure here
	declare @StartIndex Int
	declare @MaxRecords Int
	declare @i Int
	declare @PageCount Int
	declare @ApproximatedNumber float
	declare @SQL nvarchar(4000)
	

	Declare @TableName nvarchar(4000)
	set @TableName =  dbo.ThucChay_GetBaoCaoByFilterCondition(
									@GroupFieldName,
									@StartDate ,
									@EndDate ,
									@DmSanPhamREFList ,
									@DmWebsiteREFList ,
									@SoHopDongList ,
									@DmPhongBanREFList ,
									@DmBoPhanREFList ,
									@DmNhomLamViecREFList ,
									@TenNhanVienList,
									0
									)


	set @ApproximatedNumber=0.49999
	set @i=1
	set @SQL = 'select @MaxRecords=count(*) from ('+ @TableName+ ') T'

	
	EXEC sp_executesql @SQL, N'@MaxRecords int output', @MaxRecords output
	
	set @PageCount = round(convert(float,@MaxRecords)/@RecordCount+@ApproximatedNumber,0)
	SET @StartIndex = (@PageIndex - 1)*@RecordCount + 1
	Set @MaxRecords = @PageIndex*@RecordCount	

	set @TableName =  dbo.ThucChay_GetBaoCaoByFilterCondition(
									@GroupFieldName,
									@StartDate ,
									@EndDate ,
									@DmSanPhamREFList ,
									@DmWebsiteREFList ,
									@SoHopDongList ,
									@DmPhongBanREFList ,
									@DmBoPhanREFList ,
									@DmNhomLamViecREFList ,
									@TenNhanVienList,
									0
									)
	if(@PageCount>=@PageIndex)
		set @SQL = 	'SELECT * FROM 
		(SELECT *, ROW_NUMBER() OVER(ORDER BY NgayThucHien DeSC) AS rownum from ('+@TableName +') T  ) as VitualTable '+
		'WHERE rownum between '+ Convert(nvarchar(50),@StartIndex) + ' and ' + Convert(nvarchar(50),@MaxRecords)
	else
		set @SQL = 'select * from ('+@TableName + ') T'

	PRINT @SQL

	EXEC sp_executesql @SQL
END

```
