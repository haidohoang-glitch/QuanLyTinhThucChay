# Function: `ThucChay_GenSQLCommandDataSummaryFromThucChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-27 23:21:04.087000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.437000

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
-- Author:		NhatMQ
-- Create date: 2013-08-05
-- Description:	Tao cau lenh generate string lay du lieu thuc chay do ve duoc group theo san pham.
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandDataSummaryFromThucChay] 
(
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
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @FilterSQLCommand NVARCHAR(4000)
	
	SET @DauNhay = ''''
	SET @FilterSQLCommand = ' and CONVERT(DATE,A.NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
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
		SET @Sql = 'SELECT 
						0 AS SoHopDong,
						A.DmSanPhamREF,
						dbo.ThucChay_RepleaceTenSanPham(A.TenSanPham) AS TenSanPham,
						0 AS TenWebsite,
						0 AS DanhsachDmBookingREF,
						0 AS DmBannerREF,
						0 AS NgayThucHien,
						SUM(A.TongViewThucChay) AS TongViewThucChay,
						SUM(A.TongClickThucChay) AS TongClickThucChay,
						ROW_NUMBER() OVER (ORDER BY dbo.ThucChay_RepleaceTenSanPham(A.TenSanPham)) AS num
					FROM dbo.ThucChay A
						WHERE DeletedStatus <> 1 '
		SET @Sql = @Sql + @FilterSQLCommand
		
		SET @Sql = @Sql + '
					GROUP BY dbo.ThucChay_RepleaceTenSanPham(A.TenSanPham),DmSanPhamREF'
	END
	ELSE
	BEGIN
		SET @SoHopDongList = REPLACE(@SoHopDongList,'N''','');
		SET @SoHopDongList = REPLACE(@SoHopDongList,'''','');
		
		SET @DmBookingREF = REPLACE(@DmBookingREF,'N''','');
		SET @DmBookingREF = REPLACE(@DmBookingREF,'''','');
		--PRINT @SoHopDongList;
		
		SET @Sql = 'SELECT 
						0 AS SoHopDong,
						A.DmSanPhamREF,
						dbo.ThucChay_RepleaceTenSanPham(A.TenSanPham) AS TenSanPham,
						0 AS TenWebsite,
						0 AS DanhsachDmBookingREF,
						0 AS DmBannerREF,
						0 AS NgayThucHien,
						SUM(A.TongViewThucChay) AS TongViewThucChay,
						SUM(A.TongClickThucChay) AS TongClickThucChay,
						ROW_NUMBER() OVER (ORDER BY dbo.ThucChay_RepleaceTenSanPham(A.TenSanPham)) AS num
					FROM 
					(
						SELECT 
							SoHopDong, DmSanPhamREF, TenSanPham, TenWebsite, DanhsachDmBookingREF, DmBannerREF, NgayThucHien,
							TongViewThucChay,TongClickThucChay, DeletedStatus  
						FROM [dbo].[GetThucChayByFullCondition](' + @DauNhay + CONVERT(nvarchar(50),@StartDate) + @DauNhay + ',' 
																+ @DauNhay + CONVERT(nvarchar(50),@EndDate) + @DauNhay + ',' 
																+ @DauNhay + @DmBookingREF + @DauNhay + ',' 
																+ @DauNhay + @DmBannerREF + @DauNhay + ',' 
																+ @DauNhay + @SoHopDongList + @DauNhay +')
						
					)A
					WHERE A.DeletedStatus <> 1 '
					
		--SET @Sql = @Sql + @FilterSQLCommand
		
		SET @Sql = @Sql + '
					GROUP BY dbo.ThucChay_RepleaceTenSanPham(A.TenSanPham),DmSanPhamREF'
					
							
	END
	
	RETURN @Sql

END

```
