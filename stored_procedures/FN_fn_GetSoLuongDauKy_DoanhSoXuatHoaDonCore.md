# Function: `fn_GetSoLuongDauKy_DoanhSoXuatHoaDonCore`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-12 10:46:56.517000
- **Ngày sửa cuối**: 2015-06-12 10:46:56.517000

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
| `@DmHinhThucQCREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsite` | `int(4)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@DmViTriBannerREF` | `int(4)` | No |
| `@DmLoaiNenTangREF` | `int(4)` | No |
| `@TenDonViTinh` | `nvarchar(100)` | No |
| `@ThongTinHoaDonID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_GetSoLuongDauKy_DoanhSoXuatHoaDonCore]
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
	@DmHinhThucQCREF INT,
	@DmSanPhamREF	INT,
	@DmWebsite INT,
	@DmChuyenMucREF INT,
	@DmViTriBannerREF INT,
	@DmLoaiNenTangREF INT,
	@TenDonViTinh NVARCHAR(50),
	@ThongTinHoaDonID int
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
			     WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.SoLuongKMPhatSinhCuoiKy,0)
			  ELSE isnull(dstchdc.SoLuongNoiBoPhatSinhCuoiKy,0)
			END
		)SoLuongCuoiKy
		FROM DoanhSoXuatHoaDonCore dstchdc
		WHERE 1 = 1
		AND dstchdc.HopDongID = @HopDongREF
		AND dstchdc.DmKhachHangREF = @DmKhachHangREF
		AND dstchdc.DmNhanVienREF = @NhanVienREF
		AND dstchdc.BoPhanREF = @BoPhanREF
		AND dstchdc.PhongBanREF =@PhongBanREF
		AND dstchdc.NhomREF = @NhomREF
		AND dstchdc.HopDongChiTietREF = @HopDongChiTietREF
		AND dstchdc.DmHinhThucQuangCaoREF = @DmHinhThucQCREF
		AND dstchdc.DmSanPhamREF = @DmSanPhamREF
		AND dstchdc.DmWebsiteREF = @DmWebsite
		AND dstchdc.DmChuyenMucREF = @DmChuyenMucREF
		AND dstchdc.VitriBannerREF = @DmViTriBannerREF
		AND dstchdc.DonViTinh = @TenDonViTinh
		AND dstchdc.ThongTinHoaDonREF = @ThongTinHoaDonID
		AND isnull(dstchdc.DmLoaiNenTangREF,0) = isnull(@DmLoaiNenTangREF,0)
		AND dstchdc.NgayThucHien <=  CONVERT(date,DATEADD(day,-1, @NgayThucHien))
		ORDER BY dstchdc.NgayThucHien,dstchdc.DoanhSoXuatHoaDonCoreID DESC
	)
	
	SET @out = ISNULL(@out, 0)
	
	RETURN @out;
END

```
