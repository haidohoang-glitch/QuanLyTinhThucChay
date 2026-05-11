# Function: `fn_GetDauKy_Of_Thang_ChuyenMuc`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:43:27.763000
- **Ngày sửa cuối**: 2015-03-27 17:43:27.763000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DmNhanVienREF` | `int(4)` | No |
| `@PhongBanREF` | `int(4)` | No |
| `@BoPhanREF` | `int(4)` | No |
| `@NhomREF` | `int(4)` | No |
| `@TenDonViTinh` | `nvarchar(100)` | No |
| `@Username` | `nvarchar(100)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@IsSoLuong` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================

CREATE FUNCTION [dbo].[fn_GetDauKy_Of_Thang_ChuyenMuc] 
(
	-- Add the parameters for the function here
   @DmNhanVienREF INT,
   @PhongBanREF INT,
   @BoPhanREF INT,
   @NhomREF INT,
   @TenDonViTinh NVARCHAR(50),
   @Username NVARCHAR(50),
   @DmChuyenMucREF INT,
   @NgayThucHien DATETIME,
   @LoaiDoanhSo INT,
   @IsSoLuong int
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @out float
    DECLARE @DateCalc DATETIME 
    SET @DateCalc = DATEADD(MONTH,-1,@NgayThucHien)
	-- Add the T-SQL statements to compute the return value here
	IF @IsSoLuong =0
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
			FROM rptThucChay_ChuyenMuc_Thang dstchdc
			WHERE 1 = 1
				AND dstchdc.DmNhanVienREF = @DmNhanVienREF
			AND dstchdc.PhongBanREF = @PhongBanREF
			AND dstchdc.BoPhanREF = @BoPhanREF
			AND dstchdc.NhomREF = @NhomREF
			AND dstchdc.TenDonViTinh = @TenDonViTinh
			AND dstchdc.UserName = @Username
			AND dstchdc.DmChuyenMucREF = @DmChuyenMucREF
			AND dstchdc.Nam = YEAR(@DateCalc) 
			AND dstchdc.Thang <= MONTH(@DateCalc)
			ORDER BY dstchdc.Thang DESC
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
			FROM rptThucChay_ChuyenMuc_Thang dstchdc
			WHERE 1 = 1
				AND dstchdc.DmNhanVienREF = @DmNhanVienREF
			AND dstchdc.PhongBanREF = @PhongBanREF
			AND dstchdc.BoPhanREF = @BoPhanREF
			AND dstchdc.NhomREF = @NhomREF
			AND dstchdc.TenDonViTinh = @TenDonViTinh
			AND dstchdc.UserName = @Username
			AND dstchdc.DmChuyenMucREF = @DmChuyenMucREF
			AND dstchdc.Nam = YEAR(@DateCalc) 
			AND dstchdc.Thang <= MONTH(@DateCalc)
			ORDER BY dstchdc.Thang DESC
		)		
		END
		SET @out = ISNULL(@out, 0)
	-- Return the result of the function
	RETURN @out

END

```
