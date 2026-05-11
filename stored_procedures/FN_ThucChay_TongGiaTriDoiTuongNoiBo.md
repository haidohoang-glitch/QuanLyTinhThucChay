# Function: `ThucChay_TongGiaTriDoiTuongNoiBo`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-04 14:07:15.577000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.260000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TenDoiTuong` | `nvarchar(2)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@LoaiDoiTuong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_TongGiaTriDoiTuongNoiBo]
(
	-- Add the parameters for the function here
	@TenDoiTuong NVARCHAR,
	@NgayThucHien DATETIME,
	@LoaiDoiTuong NVARCHAR(50)
)
RETURNS float 
AS
BEGIN

SET @LoaiDoiTuong = UPPER(@LoaiDoiTuong)

DECLARE @TongGiaTriDoiTuongNoiBo float 

IF(@LoaiDoiTuong =  'TENSANPHAM')
Begin
	SET @TongGiaTriDoiTuongNoiBo = 
			(
			SELECT 

			SUM(ThanhTienThucChayTruocTrietKhau) 

			FROM dbo.ThucChay_ViewBizAll
			WHERE TenSanPham = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND TenMaHopDong IN ('NB')

			GROUP BY 
			NgayThucHien,
			TenSanPham,
			TenMaHopDong
			)
END

IF(@LoaiDoiTuong =  'TENWEBSITE')
Begin
	SET @TongGiaTriDoiTuongNoiBo = 
			(
			SELECT 

			SUM(ThanhTienThucChayTruocTrietKhau) 

			FROM dbo.ThucChay_ViewBizAll
			WHERE TenWebsite = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND TenMaHopDong IN ('NB')

			GROUP BY 
			NgayThucHien,
			TenWebsite,
			TenMaHopDong
			)
END

IF(@LoaiDoiTuong =  'TENPHONGBAN')
Begin
	SET @TongGiaTriDoiTuongNoiBo = 
			(
			SELECT 

			SUM(ThanhTienThucChayTruocTrietKhau) 

			FROM dbo.ThucChay_ViewBizAll
			WHERE TenPhongBan = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND TenMaHopDong IN ('NB')

			GROUP BY 
			NgayThucHien,
			TenPhongBan,
			TenMaHopDong
			)
END

IF(@LoaiDoiTuong =  'TENBOPHAN')
Begin
	SET @TongGiaTriDoiTuongNoiBo = 
			(
			SELECT 

			SUM(ThanhTienThucChayTruocTrietKhau) 

			FROM dbo.ThucChay_ViewBizAll
			WHERE TenBoPhan = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND TenMaHopDong IN ('NB')

			GROUP BY 
			NgayThucHien,
			TenBoPhan,
			TenMaHopDong
			)
END

IF(@LoaiDoiTuong =  'TENNHOM')
Begin
	SET @TongGiaTriDoiTuongNoiBo = 
			(
			SELECT 

			SUM(ThanhTienThucChayTruocTrietKhau) 

			FROM dbo.ThucChay_ViewBizAll
			WHERE TenNhomLamViec = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND TenMaHopDong IN ('NB')

			GROUP BY 
			NgayThucHien,
			TenNhomLamViec,
			TenMaHopDong
			)
END

IF(@LoaiDoiTuong =  'SOHOPDONG')
Begin
	SET @TongGiaTriDoiTuongNoiBo = 
			(
			SELECT 

			SUM(ThanhTienThucChayTruocTrietKhau) 

			FROM dbo.ThucChay_ViewBizAll
			WHERE SoHopDong = @TenDoiTuong AND NgayThucHien = @NgayThucHien AND TenMaHopDong IN ('NB')

			GROUP BY 
			NgayThucHien,
			SoHopDong
			)
END

RETURN @TongGiaTriDoiTuongNoiBo
END

```
