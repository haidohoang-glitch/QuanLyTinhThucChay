# Function: `ThucChay_GenSQLCommandDataSanPhamThucChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-27 23:30:12.850000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.503000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmBookingREF` | `nvarchar(8000)` | No |
| `@DmBannerREF` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandDataSanPhamThucChay] 
(
	-- Add the parameters for the function here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmBookingREF nvarchar(4000),
	@DmBannerREF nvarchar(4000)
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay nvarchar(50)
	DECLARE @FilterSQLCommand nvarchar(4000)
	
	SET @DauNhay = ''''
	
	SET @FilterSQLCommand = ' and CONVERT(DATE,NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
	IF(@DmSanPhamREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and A.DmSanPhamREF in (' + @DmSanPhamREFList + ')'
	if(@DmWebsiteREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and A.DmWebsiteREF in (' + @DmWebsiteREFList + ')'
	if(@SoHopDongList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and A.SoHopDong in (' + @SoHopDongList + ')'
	if(@DmBannerREF <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and A.DmBannerREF in (' + @DmBannerREF + ')'
	if (@DmBookingREF <> '') 
		set @FilterSQLCommand = @FilterSQLCommand + ' and B.DanhsachDmBookingREF IN (' + @DmBookingREF + ')'
	
	if @DmBookingREF = ''
	BEGIN
		SET @Sql = 'SELECT SoHopDong,
					dbo.ThucChay_RepleaceTenSanPham(TenSanPham) AS TenSanPham,
					TenWebsite,
					DanhsachDmBookingREF,
					DmBannerREF,
					NgayThucHien,
					TongViewThucChay,
					TongClickThucChay,
					ROW_NUMBER() OVER (ORDER BY NgayThucHien,TenSanPham,TenWebsite ) AS num
					FROM dbo.ThucChay A
					WHERE DeletedStatus <> 1	
					'+ @FilterSQLCommand 

		-- Return the result of the function
	END
	ELSE
	BEGIN
		SET @SoHopDongList = REPLACE(@SoHopDongList,'N''','');
		SET @SoHopDongList = REPLACE(@SoHopDongList,'''','');
		
		SET @Sql = '

			SELECT 
							SoHopDong, DmSanPhamREF, dbo.ThucChay_RepleaceTenSanPham(TenSanPham) AS TenSanPham, 
							TenWebsite, DanhsachDmBookingREF, DmBannerREF, NgayThucHien,
							TongViewThucChay,TongClickThucChay, DeletedStatus,
							ROW_NUMBER() OVER (ORDER BY NgayThucHien) AS num   
						FROM [dbo].[GetThucChayByFullCondition](' + @DauNhay + CONVERT(nvarchar(50),@StartDate) + @DauNhay + ',' 
																+ @DauNhay + CONVERT(nvarchar(50),@EndDate) + @DauNhay + ',' 
																+ @DauNhay + @DmBookingREF + @DauNhay + ',' 
																+ @DauNhay + @DmBannerREF + @DauNhay + ',' 
																+ @DauNhay + @SoHopDongList + @DauNhay +')'
					
		--SET @Sql = @Sql + @FilterSQLCommand
		
		--SET @Sql = @Sql + '
		--			GROUP BY dbo.ThucChay_RepleaceTenSanPham(A.TenSanPham),DmSanPhamREF'
					
							
	END
	RETURN @Sql
END

```
