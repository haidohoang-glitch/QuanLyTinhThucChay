# Function: `ThucChay_GetSoLuong_BookingDetailCPM`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-26 11:04:48.700000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.843000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@BookingREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuong_BookingDetailCPM]
(
	-- Add the parameters for the function here
	@FromDate DATETIME, 
	@ToDate DATETIME,
	@BookingREF INT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoluongCPM BIGINT
	SET @SoluongCPM = 0
	
	SET @SoluongCPM =
	(
		SELECT SUM(ISNULL(bd.CPMBook,0)) 
		FROM BookingDetail bd
		WHERE bd.BookingREF = @BookingREF
		AND convert(date,bd.DateRun) BETWEEN @FromDate AND @ToDate
	)
	RETURN @SoluongCPM

END

```
