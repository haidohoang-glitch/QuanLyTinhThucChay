# Function: `Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-22 17:42:28.290000
- **Ngày sửa cuối**: 2014-10-14 11:28:39.503000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham]
(
	-- Add the parameters for the function here
	@DmNhanHangREF INT,
	@HopDongREF INT,
	@DmSanPhamREF INT,
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
			SET @Result =
			(
				SELECT SUM(isnull(a.doanhsothucchay,0)) FROM RptNhanHangThucChayFull a
				WHERE a.DmNhanHangREF = @DmNhanHangREF
				AND a.DmSanPhamREF = @DmSanPhamREF
				AND a.HopDongREF = @HopDongREF
				AND CONVERT(date,a.NgayThucHien) BETWEEN @StartDate AND @EndDate
			)
		END
	SET @Result = ISNULL(@Result,0)
	
	RETURN @Result

END

--select [dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham](455,1233,140,'2013-01-01','2013-12-31')

```
