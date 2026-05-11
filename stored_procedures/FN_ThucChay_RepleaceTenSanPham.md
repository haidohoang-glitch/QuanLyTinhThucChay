# Function: `ThucChay_RepleaceTenSanPham`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-29 10:20:04.273000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.547000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(400)` | Yes |
| `@TenSanPham` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_RepleaceTenSanPham]
(
	-- Add the parameters for the function here
	@TenSanPham NVARCHAR(200)
)
RETURNS NVARCHAR(200)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue NVARCHAR(200)

	IF (@TenSanPham = 'CPM ChuyÃªn trang' OR @TenSanPham = 'CPM ChuyÃƒÂªn trang' OR @TenSanPham = 'CPM ChuyÃƒÆ’Ã‚Âªn trang')
		SET @ReturnValue = 'CPM Chuyên trang'
	ELSE 
		SET @ReturnValue = @TenSanPham

	-- Return the result of the function
	RETURN @ReturnValue

END

```
