# Stored Procedure: `ThucChay_BaoCaoTheoSanPham_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-04 19:06:21.520000
- **Ngày sửa cuối**: 2014-11-19 12:16:59.297000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_BaoCaoTheoSanPham_test] 

AS
BEGIN
DECLARE @SQLCommand nvarchar(4000)

SELECT 

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
TenSanPham,
--TenWebsite,
SUM(SoLuong) AS SoLuongHopDong, 
dbo.ThucChay_TongSoLuongThucChayDoiTuongKhuyenMai(TenSanPham,NgayThucHien,'SanPham') AS SoLuongThucChayKhuyenMai,
dbo.ThucChay_TongSoLuongThucChayDoiTuongNoiBo(TenSanPham,NgayThucHien,'SanPham') AS SoLuongThucChayNoiBo,
--DonGiaTheoDonVi,
SUM(SoLuongThucChay) AS SoLuongThucChayThucThu,

--DonViTinh, 
--DonGia, 
SUM(ChietKhau) TongChietKhau,

--SUM(ThanhTienThucChayTruocTrietKhau) AS ThanhTienThucChayTruocTrietKhau,
--SUM(GiaTriTrietKhauThucChay) AS GiaTriTrietKhauThucChay,
--SUM(ThanhTienSauTrietKhauThucChay) AS ThanhTienSauTrietKhauThucChay,
--SUM(GiaTriHoaHongThucChay) AS GiaTriHoaHongThucChay,

SUM(GiaTriThayDoi) AS GiaTriThayDoi,
SUM(ThanhTienThucThu) AS ThanhTienThucThu,
dbo.ThucChay_TongGiaTriDoiTuongKhuyenMai(TenSanPham,NgayThucHien,'SanPham') AS ThanhTienKhuyenMai,
dbo.ThucChay_TongGiaTriDoiTuongNoiBo(TenSanPham,NgayThucHien,'SanPham') AS ThanhTienNoiBo


FROM (select top 100 * from dbo.ThucChay_ViewBizAll) A
WHERE UPPER(TenMaHopDong) <> 'NB' AND IsKhuyenMai <> 1

GROUP BY 
NgayThucHien,
TenSanPham,
SoLuong,
DonGia, 
ChietKhau


END

--EXEC [dbo].[ThucChay_BaoCaoTheoSanPham]

```
