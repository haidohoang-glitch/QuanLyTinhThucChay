# Stored Procedure: `ThucChay_BaoCaoByFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-09 07:28:26.460000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.937000

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


CREATE PROCEDURE [dbo].[ThucChay_BaoCaoByFilterCondition] 
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
					
	set @SQLCommand =  dbo.ThucChay_GetBaoCaoByFilterCondition(
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
	print @SQLCommand
	exec(@SQLCommand)

END

```
