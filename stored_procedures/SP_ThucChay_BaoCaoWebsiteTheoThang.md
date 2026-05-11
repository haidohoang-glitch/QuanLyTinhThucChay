# Stored Procedure: `ThucChay_BaoCaoWebsiteTheoThang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-06 12:17:53.403000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.830000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--exec [ThucChay_BaoCaoWebsiteTheoThang]

CREATE PROCEDURE [dbo].[ThucChay_BaoCaoWebsiteTheoThang] 

AS
BEGIN
DECLARE @SQLCommand nvarchar(4000)

SELECT 
TenWebsite,
MONTH(NgayThucHien) as NgayThucHien,
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

--SUM(ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai(TenWebsite,NgayThucHien,'website'),0)) AS SoLuongThucChayKhuyenMai,
--SUM(ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongNoiBo(TenWebsite,NgayThucHien,'website'),0)) AS SoLuongThucChayNoiBo,
--DonGiaTheoDonVi,
--ISNULL(SUM(SoLuongThucChay),0) AS SoLuongThucChayThucThu,

--DonViTinh, 
--DonGia, 
--SUM(ChietKhau) AS TongChietKhau ,

--SUM(ThanhTienThucChayTruocTrietKhau) AS ThanhTienThucChayTruocTrietKhau,
--SUM(GiaTriTrietKhauThucChay) AS GiaTriTrietKhauThucChay,
--SUM(ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
--SUM(GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay,

--SUM(GiaTriThayDoi) AS GiaTriThayDoi,

--SUM(ISNULL(dbo.ThucChay_TongGiaTriDoiTuongKhuyenMai(TenWebsite,NgayThucHien,'website'),0)) AS ThanhTienKhuyenMai,
--SUM(ISNULL(dbo.ThucChay_TongGiaTriDoiTuongNoiBo(TenWebsite,NgayThucHien,'website'),0)) AS ThanhTienNoiBo,
ISNULL(SUM(ThanhTienThucThu),0) AS ThanhTienThucThu

FROM dbo.ThucChay_ViewBizAll
WHERE UPPER(TenMaHopDong) <> 'NB' AND IsKhuyenMai <> 1

GROUP BY 
TenWebsite,
MONTH(NgayThucHien)
ORDER BY
MONTH(NgayThucHien),
TenWebsite

END

--EXEC [dbo].[ThucChay_BaoCaoWebsiteTheoThang]

```
