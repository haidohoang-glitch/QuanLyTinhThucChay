# Function: `ThucChay_GetTongThanhTienThucChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-26 16:29:33.093000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.643000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetTongThanhTienThucChay] 
(
	-- Add the parameters for the function here
	@SoHopDong NVARCHAR(50),
	@NgayThucHien DATETIME
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue FLOAT

	SET @ResultValue = (SELECT ISNULL(SUM(tcdt.ThanhTienSauTrietKhauThucChay),0)
						FROM ThucChayDaTinh tcdt
						WHERE 
							tcdt.SoHopDong = @SoHopDong
							AND CONVERT(Date,tcdt.NgayThucHien) <= @NgayThucHien
						)
	-- Return the result of the function
	RETURN @ResultValue

END

```
