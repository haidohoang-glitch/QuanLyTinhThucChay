# Function: `fn_GetDoanhSoDauKy_DoanhSoHaiDauNhanHangCore`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-04-22 16:42:52.083000
- **Ngày sửa cuối**: 2015-04-22 16:42:52.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@NhanVienREF` | `int(4)` | No |
| `@BoPhanREF` | `int(4)` | No |
| `@PhongBanREF` | `int(4)` | No |
| `@NhomREF` | `int(4)` | No |
| `@DmKhachHangREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsite` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@DmListNganhHangREF` | `nvarchar(400)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@TenDonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauNhanHangCore]
(
	@LoaiDoanhSo INT,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
	@NgayThucHien DATETIME,
	@HopDongREF INT,
	@NhanVienREF INT,
	@BoPhanREF INT,
	@PhongBanREF INT,
	@NhomREF INT,
	@DmKhachHangREF INT,
	@HopDongChiTietREF INT,
	@DmSanPhamREF	INT,
	@DmWebsite INT,
	@DmNhanHangREF INT,
	@DmListNganhHangREF NVARCHAR(200),
	@TenDangNhap NVARCHAR(50),
	@TenDonViTinh NVARCHAR(50)
)
RETURNS BIGINT

BEGIN
	DECLARE @out BIGINT
	SET @out = 0
	--@LoaiDoanhSo = 1: Soluong thuc thu
	--2: SoLuongKM
	--3: SoLuongNB
	SET @out =
	(
		SELECT TOP 1 
		(
			CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.ThucThuPhatSinhCuoiKy,0)
			     WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.KhuyenMaiPhatSinhCuoiKy,0)
			  ELSE isnull(dstchdc.NoiBoPhatSinhCuoiKy,0)
			END
		)SoLuongCuoiKy
		FROM DoanhSoHaiDauNhanHangCore dstchdc
		WHERE 1 = 1
		AND dstchdc.HopDongID = @HopDongREF
		AND dstchdc.DmKhachHangREF = @DmKhachHangREF
		AND dstchdc.DmNhanVienREF = @NhanVienREF
		AND dstchdc.BoPhanREF = @BoPhanREF
		AND dstchdc.PhongBanREF =@PhongBanREF
		AND dstchdc.NhomREF = @NhomREF
		AND dstchdc.HopDongChiTietREF = @HopDongChiTietREF
		AND dstchdc.DmNhanHangREF = @DmNhanHangREF
		AND dstchdc.DmSanPhamREF = @DmSanPhamREF
		AND dstchdc.DmWebsiteREF = @DmWebsite
		AND dstchdc.DmListNganhHangREF = @DmListNganhHangREF
		AND dstchdc.TenDangNhap = @TenDangNhap
		AND dstchdc.DonViTinh = @TenDonViTinh
		AND  dstchdc.NgayThucHien <= CONVERT(date,DATEADD(day,-1, @NgayThucHien))
		ORDER BY dstchdc.NgayThucHien DESC
	)
	
	SET @out = ISNULL(@out, 0)
	
	RETURN @out;
END

```
