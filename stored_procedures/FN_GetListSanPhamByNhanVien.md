# Function: `GetListSanPhamByNhanVien`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-03 01:39:29.327000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.097000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-02
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetListSanPhamByNhanVien] 
(
	-- Add the parameters for the function here
	@TenDangNhap nvarchar(50)
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max)
	
	SET @ReturnValue = ''
	
	SET @ReturnValue = ISNULL((SELECT
    STUFF(
    (
    SELECT ',' + CONVERT(NVARCHAR(50),A.DmSanPhamREF)
    FROM AdminBoPhanWebsite A
    WHERE A.TenDangNhap = @TenDangNhap AND A.DmSanPhamREF > 0
    ORDER BY A.DmSanPhamREF
    FOR XML PATH('') 
    ), 1, 1, '') AS DmSanPhamREF
    ),'')

	-- Return the result of the function
	RETURN @ReturnValue

END

--SELECT dbo.GetListSanPhamByNhanVien('admin')

```
