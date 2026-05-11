# Function: `Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham_v1`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-22 17:42:28.013000
- **Ngày sửa cuối**: 2014-10-14 11:28:45.270000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmKenh` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham_v1]
(
	-- Add the parameters for the function here
	@DmNhanHangREF INT,
	@HopDongREF INT,
	@DmSanPhamREF INT,
	@DmKenh INT,
	@StartDate DATETIME,
	@EndDate DATETIME
)
RETURNS BIGINT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result BIGINT
	SET @Result = 0
	--Tinh cho Nhan hang theo San pham
	IF(@HopDongREF = 0)
	BEGIN
		SET @Result =
		(
			SELECT SUM(isnull(doanhsothucchay,0)) FROM RptNhanHangThucChayFull
			WHERE DmNhanHangREF = @DmNhanHangREF
			AND DmSanPhamREF = @DmSanPhamREF
			AND CONVERT(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
		)
		 
	END
	ELSE
	BEGIN
		IF(@DmSanPhamREF IN (231,238,339,342,337,240,370))
		BEGIN
			SET @Result =
			(
				SELECT SUM(isnull(a.doanhsothucchay,0)) FROM RptNhanHangThucChayFull a
				left JOIN HopDongChiTiet hdct ON a.HopDongChiTietREF = hdct.HopDongChiTietID 
				WHERE a.DmNhanHangREF = @DmNhanHangREF
				AND hdct.DmNhomWebsiteREF = @DmKenh
				AND a.DmSanPhamREF = @DmSanPhamREF
				AND a.HopDongREF = @HopDongREF
				AND hdct.DeletedStatus = 0
				AND CONVERT(date,a.NgayThucHien) BETWEEN @StartDate AND @EndDate
			)			
		END	--Neu la sp CPM la tag
		ELSE
		BEGIN
			SET @Result =
			(
				SELECT SUM(isnull(a.doanhsothucchay,0)) FROM RptNhanHangThucChayFull a
				left JOIN HopDongChiTiet hdct ON a.HopDongChiTietREF = hdct.HopDongChiTietID
				WHERE a.DmNhanHangREF = @DmNhanHangREF
				AND hdct.DmWebsiteREF = @DmKenh
				AND a.DmSanPhamREF = @DmSanPhamREF
				AND a.HopDongREF = @HopDongREF
				AND hdct.DeletedStatus = 0
				AND CONVERT(date,a.NgayThucHien) BETWEEN @StartDate AND @EndDate
			)	
		END
		
	END
	SET @Result = ISNULL(@Result,0)
	
	RETURN @Result

END

--select [dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham](455,1233,140,'2013-01-01','2013-12-31')

```
