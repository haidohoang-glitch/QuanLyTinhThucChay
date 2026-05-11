# Function: `fn_GetDauKy_Of_Nam_ViTriBanner`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:43:38.290000
- **Ngày sửa cuối**: 2015-03-27 17:43:38.290000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DmNhanVienREF` | `int(4)` | No |
| `@PhongBanREF` | `int(4)` | No |
| `@BoPhanREF` | `int(4)` | No |
| `@NhomREF` | `int(4)` | No |
| `@TenDonViTinh` | `nvarchar(100)` | No |
| `@UserName` | `nvarchar(100)` | No |
| `@DmViTriBannerREF` | `int(4)` | No |
| `@NamThucHien` | `datetime(8)` | No |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@isSoLuong` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================

CREATE FUNCTION [dbo].[fn_GetDauKy_Of_Nam_ViTriBanner] 
(
	-- Add the parameters for the function here
   @DmNhanVienREF INT,
   @PhongBanREF int,
   @BoPhanREF int,
   @NhomREF int,
   @TenDonViTinh nvarchar(50),
   @UserName nvarchar(50),
   @DmViTriBannerREF INT,
   @NamThucHien DATETIME,
   @LoaiDoanhSo INT,
   @isSoLuong INT 
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @out float
    DECLARE @DateCalc DATETIME 
    SET @DateCalc = DATEADD(yyyy,-1,@NamThucHien)
	-- Add the T-SQL statements to compute the return value here
	IF @isSoLuong = 0
	BEGIN
		SET @out =
		(
			SELECT TOP 1
			(
				CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.ThucChayPhatSinhCuoiKy,0)
					 WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.KhuyenMaiPhatSinhCuoiKy,0)
				  ELSE isnull(dstchdc.NoiBoPhatSinhCuoiKy,0)
				END
			)DoanhSoPhatSinh
			FROM rptThucChay_TenViTriBanner_Nam dstchdc
			WHERE 1 = 1
			AND DmNhanVienREF = @DmNhanVienREF
			AND PhongBanREF = @PhongBanREF
			AND BoPhanREF = @BoPhanREF
			And NhomREF = @NhomREF
			AND TenDonViTinh = @TenDonViTinh
			And UserName = @UserName
			AND dstchdc.DMViTriBannerREF = @DmViTriBannerREF
			AND dstchdc.Nam = Year(@DateCalc)
		)
	END
	ELSE
		BEGIN
			SET @out =
		(
			SELECT TOP 1
			(
				CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.SoLuongPhatSinhCuoiKy,0)
					 WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.SoLuongKhuyenMaiPhatSinhCuoiKy,0)
				  ELSE isnull(dstchdc.SoLuongNoiBoPhatSinhCuoiKy,0)
				END
			)DoanhSoPhatSinh
			FROM rptThucChay_TenViTriBanner_Nam dstchdc
			WHERE 1 = 1
			AND DmNhanVienREF = @DmNhanVienREF
			AND PhongBanREF = @PhongBanREF
			AND BoPhanREF = @BoPhanREF
			And NhomREF = @NhomREF
			AND TenDonViTinh = @TenDonViTinh
			And UserName = @UserName
			AND dstchdc.DMViTriBannerREF = @DmViTriBannerREF
			AND dstchdc.Nam = Year(@DateCalc)
		)
		END
		SET @out = ISNULL(@out, 0)
	-- Return the result of the function
	RETURN @out

END

```
