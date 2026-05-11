# Function: `GetDaysInYear`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-29 08:21:19.950000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.740000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@NgayKyHopDong` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDaysInYear]
(
	-- Add the parameters for the function here
	@NgayKyHopDong datetime
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DayCount int

	SET  @DayCount = CASE DATEPART(mm, DATEADD(dd, 1, CAST((CAST(YEAR(@NgayKyHopDong) AS VARCHAR(4)) + '0228') AS DATETIME))) 
				WHEN 2 THEN 366 ELSE 365  END 
	RETURN @DayCount

END

```
