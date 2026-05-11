# Function: `ThucChay_GetThanhTienChuanThucChay_TinVip`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-04 16:44:24.783000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.863000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_TinVip]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	@NgayKyHopDong DATETIME,
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT
	DECLARE @DonGiaTheoDonVi FLOAT
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @intHopDongChiTietID INT
	set @intHopDongChiTietID = CONVERT(INT, @HopDongChiTietID) 
	
	SET @DonViTinh = UPPER(@DonViTinh)
	SET @DonGiaTheoDonVi = ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_TinVIP(@SoLuong,@DonViTinh,@DonGia,@NgayKyHopDong,@NgayThucHien,@HopDongChiTietID),0)
	SET @SoLuongThucChay = ISNULL(dbo.ThucChay_GetSoLuongThucChayTinVip(@NgayThucHien, @HopDongChiTietID),0)
	
	SET @ThanhTienThucChay = @DonGiaTheoDonVi * @SoLuongThucChay
	

	RETURN @ThanhTienThucChay

END

```
