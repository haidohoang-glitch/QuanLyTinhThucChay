# Stored Procedure: `ThucChay_BaoCaoSumByFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-13 01:14:22.127000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.717000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
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
| `@IsOrderBy` | `bit(1)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--exec [ThucChay_BaoCaoSumByFilterCondition]
--'TenSanPham'
--,'2013-05-01'
--,'2013-05-15'
--,''
--,''
--,''
--,''
--,''
--,''
--,''
--,1

CREATE PROCEDURE [dbo].[ThucChay_BaoCaoSumByFilterCondition] 
	-- Add the parameters for the stored procedure here
	@GroupFieldName nvarchar(50),
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@IsOrderBy bit
AS
BEGIN

	Declare @SQLCommand nvarchar(4000)
					
	set @SQLCommand =  dbo.ThucChay_GetBaoCaoSumByFilterCondition(
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
									@IsOrderBy
								)
	--print @SQLCommand
	exec(@SQLCommand)

END

```
