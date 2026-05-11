# Function: `ThucChay_GetThanhTienThucChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-29 08:22:48.010000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.737000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
| `@TongSoBaiViet` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienThucChay]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	@NgayKyHopDong DATETIME,
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@TongSoBaiViet FLOAT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT
	DECLARE @DonGiaTheoDonVi FLOAT
	DECLARE @SoLuongThucChay FLOAT
	
	SET @DonViTinh = UPPER(@DonViTinh)
	SET @DonGiaTheoDonVi = dbo.ThucChay_GetDonGiaTheoDonViTinh(@SoLuong,@DonViTinh,@DonGia,@NgayKyHopDong)
	SET @SoLuongThucChay = dbo.ThucChay_GetSoLuongThucChayByDonViTinh(@TongViewThucChay,@TongClickThucChay,@TongSoBaiViet,@DonViTinh)
	
	SET @ThanhTienThucChay = @DonGiaTheoDonVi * @SoLuongThucChay
	

	RETURN @ThanhTienThucChay

END

```
