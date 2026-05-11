# Function: `ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-04 14:45:13.910000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.133000

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
CREATE FUNCTION [dbo].[ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai]
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

DECLARE @TongSoLuongThucChayDoiTuongKhuyenMai float 

IF(@LoaiDoiTuong =  'TENSANPHAM')
Begin
	SET @TongSoLuongThucChayDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuongThucChay) 
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
	SET @TongSoLuongThucChayDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuongThucChay) 
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
	SET @TongSoLuongThucChayDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuongThucChay) 
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
	SET @TongSoLuongThucChayDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuongThucChay) 
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
	SET @TongSoLuongThucChayDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuongThucChay) 
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
	SET @TongSoLuongThucChayDoiTuongKhuyenMai = 
					(

					SELECT
					SUM(SoLuongThucChay) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE SoHopDong = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND IsKhuyenMai = 1

					GROUP BY 
					NgayThucHien,
					SoHopDong,
					IsKhuyenMai
					)
END

RETURN @TongSoLuongThucChayDoiTuongKhuyenMai

END

```
