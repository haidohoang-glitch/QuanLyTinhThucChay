# Stored Procedure: `ThucChay_BaoCaoThucChayChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-20 10:56:05.827000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.270000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@DmBookingREF` | `varchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmBannerREF` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_BaoCaoThucChayChiTiet]
-- Add the parameters for the stored procedure here		
	@PageIndex Int,
	@RecordCount Int,
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@DmBookingREF varchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmBannerREF nvarchar(4000)
AS
BEGIN	
	--- Declare Variable --------
	declare @StartIndex Int
	declare @MaxRecords Int
	declare @i Int
	declare @PageCount INT
	declare @ApproximatedNumber float	

	Declare @DauNhay nvarchar(50)
	set @DauNhay = ''''
	Declare @FilterSQLCommand nvarchar(4000)
	DECLARE @SQL NVARCHAR(max)	
	
	SET @FilterSQLCommand = ' and CONVERT(DATE,NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
	IF(@DmSanPhamREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmSanPhamREF in (' + @DmSanPhamREFList + ')'
	if(@DmWebsiteREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmWebsiteREF in (' + @DmWebsiteREFList + ')'
	if(@SoHopDongList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and SoHopDong in (' + @SoHopDongList + ')'	
	
	SET @SQL = '
		SELECT TOP (' + CONVERT(NVARCHAR,@RecordCount) + ') T.* FROM
		(' +
			dbo.ThucChay_GenSQLCommandDataSanPhamThucChay(@StartDate,
														  @EndDate,
														  @DmSanPhamREFList,
														  @DmWebsiteREFList,
														  @SoHopDongList,
														  @DmBookingREF,
														  @DmBannerREF) +
		') AS T
		WHERE num >' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount) + 
		' ORDER BY T.num'
	
	PRINT @SQL;
	EXEC sp_executesql @SQL;
END

```
