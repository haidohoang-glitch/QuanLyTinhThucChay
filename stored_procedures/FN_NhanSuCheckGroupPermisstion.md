# Function: `NhanSuCheckGroupPermisstion`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-07 00:04:48.863000
- **Ngày sửa cuối**: 2014-10-14 10:39:34.787000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-06
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[NhanSuCheckGroupPermisstion]
(
	-- Add the parameters for the function here
	@TenDangNhap NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue INT -- -1 VIEW ALL, 
	
	IF EXISTS (SELECT UserName FROM AdminPermistionUsers WHERE UserName = @TenDangNhap)
		SET @ResultValue = -1
	ELSE
		SET @ResultValue = 0
	--IF (@TenDangNhap = 'ngocnd' OR @TenDangNhap = 'tramyphandang' OR @TenDangNhap = 'asd' OR @TenDangNhap = 'thuydothu' OR @TenDangNhap = 'kiennguyentrung' OR @TenDangNhap = 'thangnguyentoan' OR @TenDangNhap = 'hangngole' OR @TenDangNhap = 'thucchay')
	--	SET @ResultValue = -1
	--ELSE
	--	SET @ResultValue = 0

	-- Return the result of the function
	RETURN @ResultValue

END

```
