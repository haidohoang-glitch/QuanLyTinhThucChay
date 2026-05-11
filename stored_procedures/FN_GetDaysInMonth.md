# Function: `GetDaysInMonth`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-29 08:21:02.040000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.773000

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
CREATE FUNCTION [dbo].[GetDaysInMonth]
(
	-- Add the parameters for the function here
	@NgayKyHopDong datetime
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DayCount int
	SET @DayCount = DAY(DATEADD(mm, DATEDIFF(mm, -1, @NgayKyHopDong), -1)) 

	-- Return the result of the function
	RETURN @DayCount

END

```
