# Function: `fn_GetSoLuongDauKy_Of_DoanhSoThucChayNganhHangCore`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-07 12:18:05.817000
- **Ngày sửa cuối**: 2015-03-07 12:18:05.817000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmNganhHangREF` | `int(4)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@DmNhanVienREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsite` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_GetSoLuongDauKy_Of_DoanhSoThucChayNganhHangCore]
(
	@LoaiDoanhSo INT,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
	@NgayThucHien DATETIME,
	@DmNganhHangREF INT,
	@HopDongFK INT,
	@DmNhanVienREF INT,
	@HopDongChiTietREF INT,
	@DmSanPhamREF	INT,
	@DmWebsite INT
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
		)DoanhSoPhatSinh
		FROM DoanhSoThucChayNganhHangCore dstchdc
		WHERE 1 = 1
		AND dstchdc.DmNganhHangREF = @DmNganhHangREF
		AND dstchdc.HopDongREF = @HopDongFK
		AND dstchdc.DmNhanVienREF = @DmNhanVienREF
		AND dstchdc.HopDongChiTietREF = @HopDongChiTietREF
		AND dstchdc.DmSanPhamREF = @DmSanPhamREF
		AND dstchdc.DmWebsiteREF = @DmWebsite
		AND CONVERT(date,DATEADD(day,-1, @NgayThucHien)) = dstchdc.NgayThucHien
	)
	SET @out = ISNULL(@out, 0)
	RETURN @out;
END

```
