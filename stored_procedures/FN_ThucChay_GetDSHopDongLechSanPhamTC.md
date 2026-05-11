# Function: `ThucChay_GetDSHopDongLechSanPhamTC`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-11 16:14:17.380000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetDSHopDongLechSanPhamTC]
(
	-- Add the parameters for the function here
	@StartDate DATETIME,
	@EndDate DATETIME
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DSHopDong NVARCHAR(MAX)
	DECLARE @SoHopDong NVARCHAR(50)
	DECLARE @DmSanPhamREF INT
	DECLARE @Count INT
	SET @Count = 0
	SET @DSHopDong = ''
	DECLARE Record_Cursor CURSOR FOR 
		SELECT DISTINCT TC.SoHopDong, dbo.GetProductIDByTypeProduct(tc.TypeProduct) dmsanpham
		FROM ThucChay tc
		WHERE TC.NgayThucHien BETWEEN @StartDate AND @EndDate
		AND tc.TypeProduct NOT IN (1,2)
		OPEN Record_Cursor
		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--CONTENT CODE
				SET @Count = 
				(
					SELECT COUNT(*)
					FROM HopDong hd 
					INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
					AND hd.SoHopDong = @SoHopDong
					AND hdct.DmSanPhamREF IN (@DmSanPhamREF)
					AND hdct.DmSanPhamREF IN (231,238,339,342,337,240,370)
				)
				IF(@Count <= 0)
					SET @DSHopDong = @DSHopDong + @SoHopDong + '(' + convert(nvarchar(50),@DmSanPhamREF) + '),'
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF
			END
		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
	RETURN @DSHopDong
END


--SELECT  [dbo].[ThucChay_GetDSHopDongLechSanPhamTC]('2013-08-01','2013-09-01')
 

```
