# Function: `fn_asd_get_giatrihopdong_ggfb`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-09-12 15:57:14.150000
- **Ngày sửa cuối**: 2019-02-20 10:10:10.477000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(1000)` | No |
| `@DmLoaiBanner_REF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[fn_asd_get_giatrihopdong_ggfb] 
(
	-- Add the parameters for the function here
	@HopDongID int,
	@TenSanPham nvarchar(500),
	@DmLoaiBanner_REF int,
	@DonViTinh	nvarchar(100)
)
RETURNS bigint
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultVar bigint

	-- Add the T-SQL statements to compute the return value here
	select @ResultVar = sum(ThanhTien) FROM ABM_Data_ThucChay.dbo.HopDongChiTiet where HopDongFK = @HopDongID 
	and TenSanPham = @TenSanPham 
	and DmLoaiBannerREF = @DmLoaiBanner_REF
	and DonViTinh = @DonViTinh
	AND DeletedStatus <> 1
	-- Return the result of the function
	set @ResultVar = isnull(@ResultVar,0)

	RETURN @ResultVar

END

```
