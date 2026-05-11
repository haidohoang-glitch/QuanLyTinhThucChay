# Stored Procedure: `GetDistinctDataByFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-09 05:56:25.057000
- **Ngày sửa cuối**: 2014-10-14 10:39:59.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |
| `@TenChiTiet` | `nvarchar(100)` | No |
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
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


create PROCEDURE [dbo].[GetDistinctDataByFilterCondition] 
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50),
	@TenChiTiet nvarchar(50),
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
	Declare @DauNhay nvarchar(50)
	Declare @SQLCommand nvarchar(4000)
	set @DauNhay = ''''
	

	if(@TenChiTiet = 'TenNhanVien' or @TenChiTiet = 'SoHopDong')
		set @SQLCommand = 'Select distinct '+ dbo.FormatString(@TenChiTiet)  + ' from '+@TableName +' Where 1=1 ' 
	else
		set @SQLCommand = 'Select distinct '+ dbo.FormatString(@TenChiTiet) + ',' + dbo.GetIDFieldNameByFieldName(@TenChiTiet) + ' from '+@TableName +' Where 1 = 1 '+' and ' + dbo.GetIDFieldNameByFieldName(@TenChiTiet) + '>0'
	
	set @SQLCommand =  @SQLCommand + dbo.GetThucChayFilterString(
														@StartDate ,
														@EndDate ,
														@DmSanPhamREFList ,
														@DmWebsiteREFList ,
														@SoHopDongList ,
														@DmPhongBanREFList ,
														@DmBoPhanREFList ,
														@DmNhomLamViecREFList ,
														@TenNhanVienList 
													)

	set @SQLCommand = @SQLCommand + ' Order By '+ @TenChiTiet
	exec(@SQLCommand)
	--print @SQLCommand
END


--exec [GetAllTableForComboBox] 'DmNgonNgu','','TenNgonNgu'





```
