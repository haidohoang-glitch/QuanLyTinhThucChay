# Stored Procedure: `ThucChay_BaoCaoTheoWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-04 15:03:46.887000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.287000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--exec [ThucChay_BaoCaoTheoWebsite]

CREATE PROCEDURE [dbo].[ThucChay_BaoCaoTheoWebsite] 

AS
BEGIN
DECLARE @SQLCommand nvarchar(4000)

SELECT 
TenWebsite,
NgayThucHien,
--SoHopDong,
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
--SUM(SoLuong) AS SoLuongHopDong, 

ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai(TenWebsite,NgayThucHien,'tenwebsite'),0) AS SoLuongThucChayKhuyenMai,
ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongNoiBo(TenWebsite,NgayThucHien,'tenwebsite'),0) AS SoLuongThucChayNoiBo,
--DonGiaTheoDonVi,
ISNULL(SUM(SoLuongThucChay),0) AS SoLuongThucChayThucThu,

--DonViTinh, 
--DonGia, 
--SUM(ChietKhau) AS TongChietKhau ,

--SUM(ThanhTienThucChayTruocTrietKhau) AS ThanhTienThucChayTruocTrietKhau,
--SUM(GiaTriTrietKhauThucChay) AS GiaTriTrietKhauThucChay,
--SUM(ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
--SUM(GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay,

--SUM(GiaTriThayDoi) AS GiaTriThayDoi,

ISNULL(dbo.ThucChay_TongGiaTriDoiTuongKhuyenMai(TenWebsite,NgayThucHien,'tenwebsite'),0) AS ThanhTienKhuyenMai,
ISNULL(dbo.ThucChay_TongGiaTriDoiTuongNoiBo(TenWebsite,NgayThucHien,'tenwebsite'),0) AS ThanhTienNoiBo,
ISNULL(SUM(ThanhTienThucThu),0) AS ThanhTienThucThu

FROM dbo.ThucChay_ViewBizAll
WHERE UPPER(TenMaHopDong) <> 'NB' AND IsKhuyenMai <> 1

GROUP BY 
TenWebsite,
NgayThucHien
ORDER BY
NgayThucHien,
TenWebsite

END

--EXEC [dbo].[ThucChay_BaoCaoTheoSanPham]

```
