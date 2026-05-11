# Stored Procedure: `ThucChay_BaoCaoTheoDoiBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-04 16:13:46.763000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.313000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_BaoCaoTheoDoiBan] 

AS
BEGIN
DECLARE @SQLCommand nvarchar(4000)

SELECT 

NgayThucHien,
--SoHopDong,
--DmBannerREF,
--TenMaHopDong,
--IsKhuyenMai,

TenPhongBan,
TenBoPhan,
TenNhomLamViec,
--TenDiaDiemLamViec,
--TenDangNhap,
--TenNhanVien,

--TenKhachHang,

--NhanHang,
--TenNhomNganh,
--TenHinhThucQuangCao,
--TenSanPham,
--TenWebsite,
SUM(SoLuong) AS SoLuongHopDong, 
dbo.ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai(TenNhomLamViec,NgayThucHien,'tennhom') AS SoLuongThucChayKhuyenMai,
dbo.ThucChay_TongSoLuongThucChayDoiTuongNoiBo(TenNhomLamViec,NgayThucHien,'tennhom') AS SoLuongThucChayNoiBo,
--DonGiaTheoDonVi,
SUM(SoLuongThucChay) AS SoLuongThucChayThucThu,

--DonViTinh, 
--DonGia, 
SUM(ChietKhau) AS TongChietKhau ,

--SUM(ThanhTienThucChayTruocTrietKhau) AS ThanhTienThucChayTruocTrietKhau,
--SUM(GiaTriTrietKhauThucChay) AS GiaTriTrietKhauThucChay,
--SUM(ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
--SUM(GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay,

SUM(GiaTriThayDoi) AS GiaTriThayDoi,
SUM(ThanhTienThucThu) AS ThanhTienThucThu,
dbo.ThucChay_TongGiaTriDoiTuongKhuyenMai(TenNhomLamViec,NgayThucHien,'tennhom') AS ThanhTienKhuyenMai,
dbo.ThucChay_TongGiaTriDoiTuongNoiBo(TenNhomLamViec,NgayThucHien,'tennhom') AS ThanhTienNoiBo


FROM dbo.ThucChay_ViewBizAll
WHERE UPPER(TenMaHopDong) <> 'NB' AND IsKhuyenMai <> 1

GROUP BY 
NgayThucHien,
TenNhomLamViec,
TenBoPhan,
TenPhongBan
ORDER BY
TenPhongBan,
TenBoPhan,
TenNhomLamViec,
NgayThucHien

END

--EXEC [dbo].[ThucChay_BaoCaoTheoSanPham]

```
