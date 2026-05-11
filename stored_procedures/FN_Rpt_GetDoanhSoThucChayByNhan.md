# Function: `Rpt_GetDoanhSoThucChayByNhan`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-04-22 17:42:29.027000
- **Ngày sửa cuối**: 2014-10-14 11:28:38.943000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[Rpt_GetDoanhSoThucChayByNhan]
(
	-- Add the parameters for the function here
	@DmNhanHangREF INT,
	@StartDate DATETIME,
	@EndDate DATETIME
)
RETURNS BIGINT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result BIGINT
	SET @Result = 0
	SET @Result =
	(
		SELECT SUM(isnull(doanhsothucchay,0)) FROM RptNhanHangThucChayFull
		WHERE DmNhanHangREF = @DmNhanHangREF
		AND CONVERT(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
	)
	SET @Result = ISNULL(@Result,0)
	RETURN @Result

END

```
