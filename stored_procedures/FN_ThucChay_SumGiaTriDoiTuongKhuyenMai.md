# Function: `ThucChay_SumGiaTriDoiTuongKhuyenMai`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-13 01:21:53.397000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TenDoiTuong` | `nvarchar(2)` | No |
| `@LoaiDoiTuong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
create FUNCTION [dbo].[ThucChay_SumGiaTriDoiTuongKhuyenMai]
(
	-- Add the parameters for the function here
	@TenDoiTuong NVARCHAR,
	@LoaiDoiTuong NVARCHAR(50)
	
)
RETURNS float 
AS
BEGIN

SET @LoaiDoiTuong = UPPER(@LoaiDoiTuong)

DECLARE @TongGiaTriDoiTuongKhuyenMai float 

IF(@LoaiDoiTuong =  'TENSANPHAM')
Begin
	SET @TongGiaTriDoiTuongKhuyenMai = (
					SELECT 
					SUM(ThanhTienThucChayTruocTrietKhau) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE TenSanPham = @TenDoiTuong AND IsKhuyenMai = 1

					GROUP BY 
					TenSanPham,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'TENWEBSITE')
Begin
	SET @TongGiaTriDoiTuongKhuyenMai = (
					SELECT 
					SUM(ThanhTienThucChayTruocTrietKhau) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE TenWebsite = @TenDoiTuong AND IsKhuyenMai = 1

					GROUP BY 
					TenWebsite,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'TENPHONGBAN')
Begin
	SET @TongGiaTriDoiTuongKhuyenMai = (
					SELECT 
					SUM(ThanhTienThucChayTruocTrietKhau) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE TenPhongBan = @TenDoiTuong AND IsKhuyenMai = 1

					GROUP BY 
					TenPhongBan,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'TENBOPHAN')
Begin
	SET @TongGiaTriDoiTuongKhuyenMai = (
					SELECT 
					SUM(ThanhTienThucChayTruocTrietKhau) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE TenBoPhan = @TenDoiTuong  AND IsKhuyenMai = 1

					GROUP BY 
					TenBoPhan,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'TENNHOM')
Begin
	SET @TongGiaTriDoiTuongKhuyenMai = (
					SELECT 
					SUM(ThanhTienThucChayTruocTrietKhau) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE TenNhomLamViec = @TenDoiTuong  AND IsKhuyenMai = 1

					GROUP BY 
					TenNhomLamViec,
					IsKhuyenMai
					)
END

IF(@LoaiDoiTuong =  'SOHOPDONG')
Begin
	SET @TongGiaTriDoiTuongKhuyenMai = (
					SELECT 
					SUM(ThanhTienThucChayTruocTrietKhau) 
					FROM dbo.ThucChay_ViewBizAll
					WHERE SoHopDong = @TenDoiTuong AND IsKhuyenMai = 1

					GROUP BY 
					SoHopDong,
					IsKhuyenMai
					)
END


RETURN @TongGiaTriDoiTuongKhuyenMai
END

```
