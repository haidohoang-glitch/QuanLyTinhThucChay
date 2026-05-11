# Function: `GetSoHopDongByID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-23 10:45:25.943000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.683000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION GetSoHopDongByID
(
	-- Add the parameters for the function here
	@HopDongID INT
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoHopDong NVARCHAR(50)

	-- Add the T-SQL statements to compute the return value here
	SET @SoHopDong = (SELECT SoHopDong FROM HopDong WHERE HopDongID = @HopDongID)

	-- Return the result of the function
	RETURN @SoHopDong
	

END

```
