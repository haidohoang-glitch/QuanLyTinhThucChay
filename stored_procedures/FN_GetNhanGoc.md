# Function: `GetNhanGoc`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-10-05 10:16:47.530000
- **Ngày sửa cuối**: 2016-10-05 10:16:47.530000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@IDNhan` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION GetNhanGoc
(
	-- Add the parameters for the function here
	@IDNhan NVARCHAR(50)
)
RETURNS INT 
AS
BEGIN
	-- Declare the return variable here
	DECLARE @NhanGoc1 int = 0

	-- Add the T-SQL statements to compute the return value here
	SET @NhanGoc1 = (SELECT CONVERT(NVARCHAR(50),DmNhanHangGocREF) FROM ABM_Tuyetnta.dbo.DmCaseNhanHang WHERE DmNhanHangID = @IDNhan)

	-- Return the result of the function
	RETURN @NhanGoc1

END

```
