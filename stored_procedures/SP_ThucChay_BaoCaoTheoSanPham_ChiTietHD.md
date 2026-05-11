# Stored Procedure: `ThucChay_BaoCaoTheoSanPham_ChiTietHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-31 16:47:12.273000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.180000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_BaoCaoTheoSanPham_ChiTietHD] 
	-- Add the parameters for the stored procedure here
AS
BEGIN
	DECLARE @SQLCommand nvarchar(4000)

SELECT 

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
TenSanPham,
--TenWebsite,
--SUM(SoLuong) AS SoLuongHopDong, 
dbo.ThucChay_TongSoLuongThucChayHopDongKhuyenMai(SoHopDong,NgayThucHien) AS SoLuongThucChayKhuyenMai,
dbo.ThucChay_TongSoLuongThucChayHopDongNoiBo(SoHopDong,NgayThucHien) AS SoLuongThucChayNoiBo,
--DonGiaTheoDonVi,
SUM(SoLuongThucChay) AS SoLuongThucChayThucThu,

--DonViTinh, 
DonGia, 
ChietKhau,

--SUM(ThanhTienThucChayTruocTrietKhau) AS ThanhTienThucChayTruocTrietKhau,
--SUM(GiaTriTrietKhauThucChay) AS GiaTriTrietKhauThucChay,
--SUM(ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
--SUM(GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay,
SUM(ThanhTienThucThu) AS ThanhTienThucThu,
dbo.ThucChay_TongGiaTriHopDongKhuyenMai(SoHopDong,NgayThucHien) AS ThanhTienKhuyenMai,
dbo.ThucChay_TongSoLuongThucChayHopDongNoiBo(SoHopDong,NgayThucHien) AS ThanhTienNoiBo


FROM dbo.ThucChay_ViewBizAll
WHERE UPPER(TenMaHopDong) <> 'NB' AND IsKhuyenMai <> 1

GROUP BY 
NgayThucHien,
SoHopDong,
TenSanPham,
SoLuong,
DonGia, 
ChietKhau

END

```
