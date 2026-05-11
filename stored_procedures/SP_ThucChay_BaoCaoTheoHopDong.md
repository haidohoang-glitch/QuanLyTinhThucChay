# Stored Procedure: `ThucChay_BaoCaoTheoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-04 16:24:13.490000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.310000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_BaoCaoTheoHopDong] 

AS
BEGIN
DECLARE @SQLCommand nvarchar(4000)

SELECT TOP 100

NgayThucHien,
SoHopDong,
--DmBannerREF,
--TenMaHopDong,
--IsKhuyenMai,

--TenPhongBan,
--TenBoPhan,
--TenNhom,
--TenDiaDiemLamViec,
--TenDangNhap,
--TenNhanVien,

--TenKhachHang,

--NhanHang,
--TenNhomNganh,
--TenHinhThucQuangCao,
--TenSanPham,
--TenWebsite,
--SUM(SoLuong) AS SoLuongHopDong, 
ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai(SoHopDong,NgayThucHien,'sohopdong'),0) AS SoLuongThucChayKhuyenMai,
ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongNoiBo(SoHopDong,NgayThucHien,'sohopdong'),0) AS SoLuongThucChayNoiBo,
--DonGiaTheoDonVi,
SUM(SoLuongThucChay) AS SoLuongThucChayThucThu,

--DonViTinh, 
--DonGia, 
--SUM(ChietKhau) AS TongChietKhau ,

--SUM(ThanhTienThucChayTruocTrietKhau) AS ThanhTienThucChayTruocTrietKhau,
--SUM(GiaTriTrietKhauThucChay) AS GiaTriTrietKhauThucChay,
--SUM(ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
--SUM(GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay,

--SUM(GiaTriThayDoi) AS GiaTriThayDoi,
SUM(ThanhTienThucThu) AS ThanhTienThucThu,
ISNULL(dbo.ThucChay_TongGiaTriDoiTuongKhuyenMai(SoHopDong,NgayThucHien,'sohopdong'),0) AS ThanhTienKhuyenMai,
ISNULL(dbo.ThucChay_TongGiaTriDoiTuongNoiBo(SoHopDong,NgayThucHien,'sohopdong'),0) AS ThanhTienNoiBo


FROM dbo.ThucChay_ViewBizAll
WHERE UPPER(TenMaHopDong) <> 'NB' AND IsKhuyenMai <> 1
AND ThanhTienThucThu != 0
GROUP BY 
SoHopDong,
NgayThucHien
ORDER BY
SoHopDong,
NgayThucHien

END

--EXEC [dbo].[ThucChay_BaoCaoTheoSanPham]

```
