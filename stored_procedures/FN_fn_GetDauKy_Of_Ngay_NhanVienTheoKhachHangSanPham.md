# Function: `fn_GetDauKy_Of_Ngay_NhanVienTheoKhachHangSanPham`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-07 12:18:18.523000
- **Ngày sửa cuối**: 2015-03-07 12:18:18.523000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DmNhanVienREF` | `int(4)` | No |
| `@PhongBanREF` | `int(4)` | No |
| `@BoPhanREF` | `int(4)` | No |
| `@NhomREF` | `int(4)` | No |
| `@DmKhachHangREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
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

CREATE FUNCTION [dbo].[fn_GetDauKy_Of_Ngay_NhanVienTheoKhachHangSanPham] 
(
	-- Add the parameters for the function here
   @DmNhanVienREF INT,
   @PhongBanREF INT,
   @BoPhanREF INT,
   @NhomREF INT,
   @DmKhachHangREF INT,
   @DmSanPhamREF INT,
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
			FROM rptThucChay_NhanVien_TheoKhachHang_SanPham_Ngay dstchdc
			WHERE 1 = 1
			AND dstchdc.DmNhanVienREF = @DmNhanVienREF
			AND dstchdc.PhongBanREF = @PhongBanREF
			AND dstchdc.BoPhanREF = @BoPhanREF
			AND dstchdc.NhomREF = @NhomREF
			AND dstchdc.DmKhachHangREF = @DmKhachHangREF
			AND dstchdc.DmSanPhamREF = @DmSanPhamREF
            AND dstchdc.NgayThucHien = @DateCalc 
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
			FROM rptThucChay_NhanVien_TheoKhachHang_SanPham_Ngay dstchdc
			WHERE 1 = 1
			AND dstchdc.DmNhanVienREF = @DmNhanVienREF
			AND dstchdc.PhongBanREF = @PhongBanREF
			AND dstchdc.BoPhanREF = @BoPhanREF
			AND dstchdc.NhomREF = @NhomREF
			AND dstchdc.DmKhachHangREF = @DmKhachHangREF
			AND dstchdc.DmSanPhamREF = @DmSanPhamREF
			AND dstchdc.NgayThucHien = @DateCalc 
		)
		SET @out = ISNULL(@out, 0)
	-- Return the result of the function
	RETURN @out

END

```
