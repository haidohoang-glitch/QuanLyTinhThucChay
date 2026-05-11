# Function: `fn_GetDauKy_Of_Quy_ViTriBanner`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:43:28.250000
- **Ngày sửa cuối**: 2015-03-27 17:43:28.250000

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
| `@QuyThucHien` | `datetime(8)` | No |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@isSoLuong` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================

CREATE FUNCTION [dbo].[fn_GetDauKy_Of_Quy_ViTriBanner] 
(
	-- Add the parameters for the function here
	@DmNhanVienREF INT,
   @PhongBanREF int,
   @BoPhanREF int,
   @NhomREF int,
   @TenDonViTinh nvarchar(50),
   @UserName nvarchar(50),
   @DmViTriBannerREF INT,
   @QuyThucHien DATETIME,
   @LoaiDoanhSo INT,
   @isSoLuong INT 
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @out float
    DECLARE @DateCalc DATETIME 
    SET @DateCalc = DATEADD(QQ,-1,@QuyThucHien)
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
			FROM rptThucChay_TenViTriBanner_Quy dstchdc
			WHERE 1 = 1
			AND DmNhanVienREF = @DmNhanVienREF
			AND PhongBanREF = @PhongBanREF
			AND BoPhanREF = @BoPhanREF
			And NhomREF = @NhomREF
			AND TenDonViTinh = @TenDonViTinh
			And UserName = @UserName
			AND dstchdc.DMViTriBannerREF = @DmViTriBannerREF
		    AND dstchdc.Quy = DATEPART(QQ,@DateCalc)
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
			FROM rptThucChay_TenViTriBanner_Quy dstchdc
			WHERE 1 = 1
			AND DmNhanVienREF = @DmNhanVienREF
			AND PhongBanREF = @PhongBanREF
			AND BoPhanREF = @BoPhanREF
			And NhomREF = @NhomREF
			AND TenDonViTinh = @TenDonViTinh
			And UserName = @UserName
			AND dstchdc.DMViTriBannerREF = @DmViTriBannerREF
		    AND dstchdc.Quy = DATEPART(QQ,@DateCalc)
			AND dstchdc.Nam = Year(@DateCalc)
		)
		END
		SET @out = ISNULL(@out, 0)
	-- Return the result of the function
	RETURN @out

END

```
