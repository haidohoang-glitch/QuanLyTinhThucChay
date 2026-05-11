# Function: `fn_GetDoanhSoDauKy`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:43:22.443000
- **Ngày sửa cuối**: 2015-03-27 17:43:22.443000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@LoaiDoanhSo` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@NhanVienREF` | `int(4)` | No |
| `@BoPhanREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmHinhThucQCREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmNhomWebsite_Tag` | `nvarchar(100)` | No |
| `@DmWebsite` | `int(4)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@DmViTriBannerREF` | `int(4)` | No |
| `@DmLoaiNenTangREF` | `int(4)` | No |
| `@TenDonViTinh` | `nvarchar(100)` | No |
| `@UserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_GetDoanhSoDauKy]
(
	@LoaiDoanhSo INT,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
	@NgayThucHien DATETIME,
	@HopDongREF INT,
	@NhanVienREF INT,
	@BoPhanREF INT,
	@HopDongChiTietREF INT,
	@DmHinhThucQCREF INT,
	@DmSanPhamREF	INT,
	@DmNhomWebsite_Tag NVARCHAR(50),
	@DmWebsite INT,
	@DmChuyenMucREF INT,
	@DmViTriBannerREF INT,
	@DmLoaiNenTangREF INT,
	@TenDonViTinh NVARCHAR(50),
	@UserName NVARCHAR(50)
)
RETURNS FLOAT

BEGIN
	DECLARE @out FLOAT
	SET @out = 0
	
	SET @out =
	(
		SELECT TOP 1 
		(
			CASE WHEN @LoaiDoanhSo = 1 THEN  isnull(dstchdc.ThucChayPhatSinhCuoiKy,0)
			     WHEN @LoaiDoanhSo = 2 THEN  isnull(dstchdc.KhuyenMaiPhatSinhCuoiKy,0)
			  ELSE isnull(dstchdc.NoiBoPhatSinhCuoiKy,0)
			END
		)DoanhSoPhatSinh
		FROM DoanhSoThucChayHopDongCore dstchdc
		WHERE 1 = 1
		AND dstchdc.HopDongID = @HopDongREF
		AND dstchdc.DmNhanVienREF = @NhanVienREF
		AND dstchdc.BoPhanREF = @BoPhanREF
		AND dstchdc.HopDongChiTietREF = @HopDongChiTietREF
		AND dstchdc.DmHinhThucQuangCaoREF = @DmHinhThucQCREF
		AND dstchdc.DmSanPhamREF = @DmSanPhamREF
		AND dstchdc.NhomWebsite_TagREF = @DmNhomWebsite_Tag
		AND dstchdc.DmWebsiteREF = @DmWebsite
		AND dstchdc.DmChuyenMucREF = @DmChuyenMucREF
		AND dstchdc.VitriBannerREF = @DmViTriBannerREF
		AND dstchdc.TenDonViTinh = @TenDonViTinh
		AND dstchdc.UserName = @UserName
		AND isnull(dstchdc.DmLoaiNenTangREF,0) = isnull(@DmLoaiNenTangREF,0)
		AND CONVERT(date,DATEADD(day,-1, @NgayThucHien)) >=  dstchdc.NgayThucHien
		ORDER BY dstchdc.NgayThucHien DESC
	)
	
	
	SET @out = ISNULL(@out, 0)
	
	RETURN @out;
END

```
