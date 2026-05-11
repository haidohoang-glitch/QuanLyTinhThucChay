# Function: `ThucChay_GetThanhTienChuanThucChay_CPD_Test`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-02 18:10:03.887000
- **Ngày sửa cuối**: 2014-10-14 10:39:30.037000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_CPD_Test]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	--@NgayKyHopDong DATETIME,
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
	SET @DonGiaTheoDonVi = ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_BK(@SoLuong,@DonViTinh,@DonGia,@NgayThucHien,@HopDongChiTietID),0)	
	SET @SoLuongThucChay = ISNULL(dbo.ThucChay_GetSoLuongThucChayCPD_Test(@NgayThucHien, @HopDongChiTietID),0)

	SET @ThanhTienThucChay = @DonGiaTheoDonVi * @SoLuongThucChay


	RETURN @ThanhTienThucChay

END

```
