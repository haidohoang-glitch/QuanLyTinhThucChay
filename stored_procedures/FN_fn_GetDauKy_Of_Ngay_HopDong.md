# Function: `fn_GetDauKy_Of_Ngay_HopDong`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:43:36.873000
- **Ngày sửa cuối**: 2015-03-27 17:43:36.873000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@DmNhanVienREF` | `int(4)` | No |
| `@PhongBanREF` | `int(4)` | No |
| `@BoPhanREF` | `int(4)` | No |
| `@NhomREF` | `int(4)` | No |
| `@DmKhachHangREF` | `int(4)` | No |
| `@LoaiKhachHang` | `int(4)` | No |
| `@TenDonViTinh` | `nvarchar(100)` | No |
| `@UserName` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@isSoluong` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[fn_GetDauKy_Of_Ngay_HopDong] 
(
	-- Add the parameters for the function here
   @HopDongID INT,
   @DmNhanVienREF INT,
   @PhongBanREF INT,
   @BoPhanREF INT,
   @NhomREF INT,
   @DmKhachHangREF INT,
   @LoaiKhachHang INT,
   @TenDonViTinh NVARCHAR(50),
   @UserName NVARCHAR(50),
   @NgayThucHien DATETIME,
   @LoaiDoanhSo INT,
   @isSoluong INT
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @out float
    DECLARE @DateCalc DATETIME 
    SET @DateCalc = DATEADD(DAY,-1,@NgayThucHien)
	-- Add the T-SQL statements to compute the return value here
	IF @isSoluong = 0
		SET @out =
		(
			SELECT TOP 1
			(
				CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.ThucChayPhatSinhCuoiKy,0)
					 WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.KhuyenMaiPhatSinhCuoiKy,0)
				  ELSE isnull(dstchdc.NoiBoPhatSinhCuoiKy,0)
				END
			)DoanhSoPhatSinh
			FROM rptThucChay_HopDong_Ngay dstchdc
			WHERE 1 = 1
			AND dstchdc.NgayThucHien <= @DateCalc
			AND dstchdc.HopDongID = @HopDongID
			AND dstchdc.DmNhanVienREF = @DmNhanVienREF
			AND dstchdc.PhongBanREF = @PhongBanREF
			AND dstchdc.BoPhanREF = @BoPhanREF
			AND dstchdc.NhomREF = @NhomREF
			AND dstchdc.LoaiKhachHang = @LoaiKhachHang
			AND dstchdc.DmKhachHangREF = @DmKhachHangREF
			AND dstchdc.TenDonViTinh = @TenDonViTinh
			AND dstchdc.UserName = @UserName
			ORDER BY dstchdc.NgayThucHien DESC
		)
	ELSE
		SET @out =
		(
			SELECT TOP 1
			(
				CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.SoLuongPhatSinhCuoiKy,0)
					 WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.SoLuongKhuyenMaiPhatSinhCuoiKy,0)
				  ELSE isnull(dstchdc.SoLuongNoiBoPhatSinhCuoiKy,0)
				END
			)DoanhSoPhatSinh
			FROM rptThucChay_HopDong_Ngay dstchdc
			WHERE 1 = 1
			AND dstchdc.NgayThucHien <= @DateCalc
			AND dstchdc.HopDongID = @HopDongID
			AND dstchdc.DmNhanVienREF = @DmNhanVienREF
			AND dstchdc.PhongBanREF = @PhongBanREF
			AND dstchdc.BoPhanREF = @BoPhanREF
			AND dstchdc.NhomREF = @NhomREF
			AND dstchdc.LoaiKhachHang = @LoaiKhachHang
			AND dstchdc.DmKhachHangREF = @DmKhachHangREF
			AND dstchdc.TenDonViTinh = @TenDonViTinh
			AND dstchdc.UserName = @UserName
			ORDER BY dstchdc.NgayThucHien DESC
		)
		SET @out = ISNULL(@out, 0)
	-- Return the result of the function
	RETURN @out

END

```
