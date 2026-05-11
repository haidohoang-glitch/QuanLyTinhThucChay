# Function: `ThucChay_TongSoLuongHopDongDoiTuongKhuyenMaiV2`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-14 12:56:56.017000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TenDoiTuong` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiDoiTuong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[ThucChay_TongSoLuongHopDongDoiTuongKhuyenMaiV2]
(
	-- Add the parameters for the function here
	@TenDoiTuong NVARCHAR(50),
	@NgayThucHien DATETIME,
	@LoaiDoiTuong NVARCHAR(50) 
	
)
RETURNS float 
AS
BEGIN

SET @LoaiDoiTuong = UPPER(@LoaiDoiTuong)

DECLARE @TongSoLuongDoiTuongKhuyenMai float 

IF(@LoaiDoiTuong =  'TENSANPHAM')
Begin
	SET @TongSoLuongDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuong) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE DmSanPhamREF = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

					GROUP BY 
					NgayThucHien,
					TenSanPham,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'TENWEBSITE')
Begin
	SET @TongSoLuongDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuong) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE DmWebsiteREF = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

					GROUP BY 
					NgayThucHien,
					TenWebsite,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'TENPHONGBAN')
Begin
	SET @TongSoLuongDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuong) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE DmPhongBanREF = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

					GROUP BY 
					NgayThucHien,
					TenPhongBan,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'TENBOPHAN')
Begin
	SET @TongSoLuongDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuong) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE DmBoPhanREF = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

					GROUP BY 
					NgayThucHien,
					TenBoPhan,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'TENNHOM')
Begin
	SET @TongSoLuongDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuong) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE DmNhomLamViecREF = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

					GROUP BY 
					NgayThucHien,
					TenNhomLamViec,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'SOHOPDONG')
Begin
	SET @TongSoLuongDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuong) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE SoHopDong = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

					GROUP BY 
					NgayThucHien,
					SoHopDong,
					IsKhuyenMai
					)
END

RETURN @TongSoLuongDoiTuongKhuyenMai

END
```
