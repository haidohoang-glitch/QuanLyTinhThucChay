# Stored Procedure: `ThucChay_BaoCaoTongSanPhamAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-06 11:36:08.030000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.190000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_BaoCaoTongSanPhamAll] 

AS
BEGIN
DECLARE @SQLCommand nvarchar(4000)

SELECT 

--NgayThucHien,
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
TenSanPham,
--TenWebsite,
--SUM(SoLuong) AS SoLuongHopDong, 
--SUM(ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai(TenSanPham,NgayThucHien,'SanPham'),0)) AS SoLuongThucChayKhuyenMai,
--SUM(ISNULL(dbo.ThucChay_TongSoLuongThucChayDoiTuongNoiBo(TenSanPham,NgayThucHien,'SanPham'),0)) AS SoLuongThucChayNoiBo,
--DonGiaTheoDonVi,
ISNULL(SUM(SoLuongThucChay),0) AS SoLuongThucChayThucThu,

--DonViTinh, 
--DonGia, 
--SUM(ChietKhau) TongChietKhau,

--SUM(ThanhTienThucChayTruocTrietKhau) AS ThanhTienThucChayTruocTrietKhau,
--SUM(GiaTriTrietKhauThucChay) AS GiaTriTrietKhauThucChay,
--SUM(ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
--SUM(GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay,

--SUM(GiaTriThayDoi) AS GiaTriThayDoi,
--SUM(ISNULL(dbo.ThucChay_TongGiaTriDoiTuongKhuyenMai(TenSanPham,NgayThucHien,'SanPham'),0)) AS ThanhTienKhuyenMai,
--SUM(ISNULL(dbo.ThucChay_TongGiaTriDoiTuongNoiBo(TenSanPham,NgayThucHien,'SanPham'),0)) AS ThanhTienNoiBo,
ISNULL(SUM(ThanhTienThucThu),0) AS ThanhTienThucThu

FROM dbo.ThucChay_ViewBizAll
WHERE UPPER(TenMaHopDong) <> 'NB' AND IsKhuyenMai <> 1

GROUP BY 
TenSanPham
ORDER BY
TenSanPham

END

--EXEC [dbo].[ThucChay_BaoCaoTongSanPhamAll]

```
