# Function: `ThucChay_SumSoLuongThucChayDoiTuongNoiBo`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-13 07:59:49.563000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.353000

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
create FUNCTION [dbo].[ThucChay_SumSoLuongThucChayDoiTuongNoiBo]
(
	-- Add the parameters for the function here
	@TenDoiTuong NVARCHAR,
	@LoaiDoiTuong NVARCHAR(50)  
	
)
RETURNS float 
AS
BEGIN

SET @LoaiDoiTuong = UPPER(@LoaiDoiTuong)
DECLARE @TongSoLuongThucChayDoiTuongNoiBo float 

SET @LoaiDoiTuong = UPPER(@LoaiDoiTuong)

DECLARE @TongSoLuongThucChayThucChayDoiTuongKhuyenMai float 

IF(@LoaiDoiTuong =  'TENSANPHAM')
	Begin
		SET @TongSoLuongThucChayDoiTuongNoiBo = 
							(

							SELECT SUM(SoLuongThucChay) 
							FROM dbo.ThucChay_ViewBizAll
							WHERE TenSanPham = @TenDoiTuong  AND TenMaHopDong IN ('NB')

							GROUP BY 

							TenSanPham,
							TenMaHopDong
							)
	END

IF(@LoaiDoiTuong =  'TENWEBSITE')
	Begin
		SET @TongSoLuongThucChayDoiTuongNoiBo = 
							(

							SELECT SUM(SoLuongThucChay) 
							FROM dbo.ThucChay_ViewBizAll
							WHERE TenWebsite = @TenDoiTuong  AND TenMaHopDong IN ('NB')

							GROUP BY 

							TenWebsite,
							TenMaHopDong
							)
	END

IF(@LoaiDoiTuong =  'TENPHONGBAN')
	Begin
		SET @TongSoLuongThucChayDoiTuongNoiBo = 
							(

							SELECT SUM(SoLuongThucChay) 
							FROM dbo.ThucChay_ViewBizAll
							WHERE TenPhongBan = @TenDoiTuong  AND TenMaHopDong IN ('NB')

							GROUP BY 

							TenPhongBan,
							TenMaHopDong
							)
	END

IF(@LoaiDoiTuong =  'TENBOPHAN')
	Begin
		SET @TongSoLuongThucChayDoiTuongNoiBo = 
							(

							SELECT SUM(SoLuongThucChay) 
							FROM dbo.ThucChay_ViewBizAll
							WHERE TenBoPhan = @TenDoiTuong  AND TenMaHopDong IN ('NB')

							GROUP BY 

							TenBoPhan,
							TenMaHopDong
							)
	END

IF(@LoaiDoiTuong =  'TENNHOM')
	Begin
		SET @TongSoLuongThucChayDoiTuongNoiBo = 
							(

							SELECT SUM(SoLuongThucChay) 
							FROM dbo.ThucChay_ViewBizAll
							WHERE TenNhomLamViec = @TenDoiTuong  AND TenMaHopDong IN ('NB')

							GROUP BY 

							TenNhomLamViec,
							TenMaHopDong
							)
	END

IF(@LoaiDoiTuong =  'SOHOPDONG')
	Begin
		SET @TongSoLuongThucChayDoiTuongNoiBo = 
							(

							SELECT SUM(SoLuongThucChay) 
							FROM dbo.ThucChay_ViewBizAll
							WHERE SoHopDong = @TenDoiTuong  AND TenMaHopDong IN ('NB')

							GROUP BY 

							SoHopDong
							)
	END

RETURN @TongSoLuongThucChayDoiTuongNoiBo

END

```
