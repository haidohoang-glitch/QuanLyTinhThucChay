# Function: `ThucChay_TongSoLuongHopDongDoiTuongKhuyenMai`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 14:19:29.760000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.227000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TenDoiTuong` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiDoiTuong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_TongSoLuongHopDongDoiTuongKhuyenMai]
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
					WHERE TenSanPham = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

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
					WHERE TenWebsite = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

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
					WHERE TenPhongBan = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

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
					WHERE TenBoPhan = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

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
					WHERE TenNhomLamViec = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

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
