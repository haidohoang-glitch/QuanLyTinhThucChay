# Function: `fn_GetDauKy_Of_Ngay_KhachHangTheoLoaiNenTang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-07 12:18:19.540000
- **Ngày sửa cuối**: 2015-03-07 12:18:19.540000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DmKhachHangREF` | `int(4)` | No |
| `@LoaiKhachHang` | `int(4)` | No |
| `@DmLoaiNenTangREF` | `int(4)` | No |
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

CREATE FUNCTION [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoLoaiNenTang] 
(
	-- Add the parameters for the function here
   @DmKhachHangREF INT,
   @LoaiKhachHang INT,
   @DmLoaiNenTangREF INT,
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
			FROM rptThucChay_KhachHang_TheoNenTang_Ngay dstchdc
			WHERE 1 = 1
			AND dstchdc.DmHinhThucKhachHangREF = @LoaiKhachHang
			AND dstchdc.DmKhachHangREF = @DmKhachHangREF
			AND dstchdc.DmLoaiNenTangREF = @DmLoaiNenTangREF 
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
			FROM rptThucChay_KhachHang_TheoNenTang_Ngay dstchdc
			WHERE 1 = 1
			AND dstchdc.DmHinhThucKhachHangREF = @LoaiKhachHang
			AND dstchdc.DmKhachHangREF = @DmKhachHangREF
			AND dstchdc.DmLoaiNenTangREF = @DmLoaiNenTangREF 
			AND dstchdc.NgayThucHien = @DateCalc
		)
		SET @out = ISNULL(@out, 0)
	-- Return the result of the function
	RETURN @out

END

```
