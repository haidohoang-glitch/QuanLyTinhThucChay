# Function: `ThucChayDaTinh_GetDonGiaBaoGiaSanPham`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-12 17:44:30.900000
- **Ngày sửa cuối**: 2014-11-19 12:17:40.430000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChayDaTinh_GetDonGiaBaoGiaSanPham]
(
	@NgayThucHien DATETIME,
	@DmSanPhamREF NVARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DefaultDate DATETIME
	SET @DefaultDate = '3000-12-31' 
	
	-- Add the SELECT statement with parameter references here
	DECLARE @DonGia FLOAT
	set @DonGia  = ISNULL((SELECT TOP 1 DonGia FROM BangGiaSanPham bgsp
	                WHERE bgsp.DmSanPhamREF = @DmSanPhamREF
	                AND @NgayThucHien BETWEEN bgsp.NgayHieuLuc AND ISNULL(bgsp.NgayHetHieuLuc,@DefaultDate)
	                ),0)
	 RETURN @DonGia
END

```
