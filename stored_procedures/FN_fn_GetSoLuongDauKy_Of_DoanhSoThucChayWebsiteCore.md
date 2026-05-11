# Function: `fn_GetSoLuongDauKy_Of_DoanhSoThucChayWebsiteCore`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:43:21.993000
- **Ngày sửa cuối**: 2015-03-27 17:43:21.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsite` | `int(4)` | No |
| `@DmNhanVienREF` | `int(4)` | No |
| `@PhongBanREF` | `int(4)` | No |
| `@BoPhanREF` | `int(4)` | No |
| `@NhomREF` | `int(4)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@DmViTriBannerREF` | `int(4)` | No |
| `@DmKhachHang` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@TenDonViTinh` | `nvarchar(100)` | No |
| `@UserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_GetSoLuongDauKy_Of_DoanhSoThucChayWebsiteCore]
(
	@LoaiDoanhSo INT,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
	@NgayThucHien DATETIME,
	@DmSanPhamREF	INT,
	@DmWebsite INT,
	@DmNhanVienREF int,
	@PhongBanREF INT,
	@BoPhanREF INT,
	@NhomREF INT,
	@DmHinhThucQuangCaoREF INT,
	@DmViTriBannerREF INT,
	@DmKhachHang INT,
	@HopDongID INT ,
	@TenDonViTinh NVARCHAR(50),
	@UserName NVARCHAR(50)
)
RETURNS BIGINT

BEGIN
	DECLARE @out BIGINT
	SET @out = 0
	SET @out =
	(
		SELECT TOP 1
		(
			CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.SoLuongPhatSinhCuoiKy,0)
			     WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.SoLuongKhuyenMaiPhatSinhCuoiKy,0)
			  ELSE isnull(dstchdc.SoLuongNoiBoPhatSinhCuoiKy,0)
			END
		)SoLuongPhatSinh
		FROM DoanhSoThucChayWebsiteCore dstchdc
		WHERE 1 = 1
		AND dstchdc.DmSanPhamREF = @DmSanPhamREF
		AND dstchdc.DmWebsiteREF = @DmWebsite
		AND dstchdc.DmNhanVienREF = @DmNhanVienREF
		AND dstchdc.PhongBanREF = @PhongBanREF
		AND dstchdc.BoPhanREF = @BoPhanREF
		AND dstchdc.NhomREF = @NhomREF
		AND dstchdc.DmHinhThucQuangCaoREF = @DmHinhThucQuangCaoREF
		AND dstchdc.DmKhachHangREF = @DmKhachHang
		AND dstchdc.DmViTriBannerREF = @DmViTriBannerREF
		AND dstchdc.HopDongID = @HopDongID
		AND dstchdc.TenDonViTinh = @TenDonViTinh
		AND dstchdc.UserName = @UserName
		AND CONVERT(date,DATEADD(day,-1, @NgayThucHien)) = dstchdc.NgayThucHien
	)
	SET @out = ISNULL(@out, 0)
	
	RETURN @out;
END

```
