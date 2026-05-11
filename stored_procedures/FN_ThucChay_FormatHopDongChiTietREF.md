# Function: `ThucChay_FormatHopDongChiTietREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-17 16:42:00.140000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.703000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.ThucChay_FormatHopDongChiTietREF
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue NVARCHAR(50);

	IF @HopDongChiTietID <> 0 
		SET @ReturnValue = CONVERT(NVARCHAR(50),@HopDongChiTietID)
	ELSE
		SET @ReturnValue = ''

	-- Return the result of the function
	RETURN @ReturnValue

END

```
