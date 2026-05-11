# Function: `fn_GetDauKy_Of_Nam_HopDongTheoWebsite`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:43:39.903000
- **Ngày sửa cuối**: 2015-03-27 17:43:39.903000

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
| `@DmWebsiteREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@isSoluong` | `int(4)` | No |
| `@TenDonViTinh` | `nvarchar(100)` | No |
| `@UserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================

CREATE FUNCTION [dbo].[fn_GetDauKy_Of_Nam_HopDongTheoWebsite] 
(
	-- Add the parameters for the function here
   @HopDongID INT,
   @DmNhanVienREF INT,
   @PhongBanREF INT,
   @BoPhanREF INT,
   @NhomREF INT,
   @DmKhachHangREF INT,
   @LoaiKhachHang INT,
   @DmWebsiteREF INT,
   @NgayThucHien DATETIME,
   @LoaiDoanhSo INT,
   @isSoluong INT,
   @TenDonViTinh nvarchar(50),
   @UserName nvarchar(50)
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @out float
    DECLARE @DateCalc DATETIME 
    SET @DateCalc = DATEADD(yyyy,-1,@NgayThucHien)
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
			FROM rptThucChay_HopDong_TheoWebsite_Nam dstchdc
			WHERE 1 = 1
			AND dstchdc.HopDongID = @HopDongID
			AND dstchdc.DmNhanVienREF = @DmNhanVienREF
			AND dstchdc.PhongBanREF = @PhongBanREF
			AND dstchdc.BoPhanREF = @BoPhanREF
			AND dstchdc.NhomREF = @NhomREF
			AND dstchdc.LoaiKhachHang = @LoaiKhachHang
			AND dstchdc.DmKhachHangREF = @DmKhachHangREF
			AND dstchdc.DmWebsiteREF = @DmWebsiteREF 
			AND dstchdc.Nam = YEAR(@DateCalc) 
	        AND dstchdc.TenDonViTinh = @TenDonViTinh
	        AND dstchdc.UserName = @UserName 
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
			FROM rptThucChay_HopDong_TheoWebsite_Nam dstchdc
			WHERE 1 = 1
			AND dstchdc.HopDongID = @HopDongID
			AND dstchdc.DmNhanVienREF = @DmNhanVienREF
			AND dstchdc.PhongBanREF = @PhongBanREF
			AND dstchdc.BoPhanREF = @BoPhanREF
			AND dstchdc.NhomREF = @NhomREF
			AND dstchdc.LoaiKhachHang = @LoaiKhachHang
			AND dstchdc.DmKhachHangREF = @DmKhachHangREF
			AND dstchdc.DmWebsiteREF = @DmWebsiteREF 
		    AND dstchdc.Nam = YEAR(@DateCalc)
		    AND dstchdc.TenDonViTinh = @TenDonViTinh
	        AND dstchdc.UserName = @UserName

		)
		SET @out = ISNULL(@out, 0)
	-- Return the result of the function
	RETURN @out

END

```
