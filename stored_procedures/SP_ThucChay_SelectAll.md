# Stored Procedure: `ThucChay_SelectAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 08:23:03.520000
- **Ngày sửa cuối**: 2014-10-14 10:39:52.767000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_SelectAll] 
	-- Add the parameters for the stored procedure here
AS
BEGIN


SELECT TC.*, 
(TC.ThanhTienThucChayTruocTrietKhau * TC.ChietKhau)/100 AS GiaTriTrietKhauThucChay,
(TC.ThanhTienThucChayTruocTrietKhau - (TC.ThanhTienThucChayTruocTrietKhau * TC.ChietKhau)/100) AS ThanhTienSauTrietKhauThucChay,
(TC.ThanhTienThucChayTruocTrietKhau * TC.TiLeTuVan)/100 AS GiaTriHoaHongThucChay,
(TC.ThanhTienThucChayTruocTrietKhau - (TC.ThanhTienThucChayTruocTrietKhau * TC.ChietKhau)/100 - (TC.ThanhTienThucChayTruocTrietKhau * TC.TiLeTuVan)/100) AS ThanhTienThucThu
FROM 
(
SELECT  
--Thong tin ve ma so 
C.SoHopDong, 
C.DmMaHopDongREF, 
C.TenMaHopDong, 
--Thong tin ve thoi gian
C.NgayDanhSoHopDong, C.NgayKyHopDong, 
C.NhanHopDong, C.NgayNhanBanFax, C.NgayNhanHopDongBanCung, C.NgayChuyenHopDongChoKeToan, 
C.So, C.Thang, C.Nam, 
--Thong tin ve gia tri
C.GiaTriHopDong, C.CongNo,
--Thong tin ve trang thai
C.DangSuDung, C.IsGiayPhep, C.TrangThaiHopDong,C.IsBanCung, 
--Thong tin ve Nhan vien kinh doanh
C.DmPhongBanREF, 
C.TenPhongBan, 
C.DmBoPhanREF, 
C.TenBoPhan, 
C.DmNhomLamViecREF, 
C.TenNhom as TenNhomLamViec,
C.DmDiaDiemLamViecREF, 
C.TenDiaDiemLamViec, 
C.SysNhanVienREF, 
C.TenDangNhap, 
C.TenNhanVien, 
--Thong tin ve khach hang
--C.DmKhachHangREF, 
C.TenKhachHang, 
B.NhanHang, 
B.DmNhomNganhREF, 
B.TenNhomNganh, 
--Thong tin hinh thuc quang cao
B.DmLoaiREF AS DmHinhThucQuangCao, B.TenLoai AS TenHinhThucQuangCao, 
--Thong tin San pham
B.DmSanPhamREF, 
B.TenSanPham, 
B.DmNhomWebsiteREF, 
B.TenNhomWebsite, 
--B.DmWebsiteREF, 
--B.TenWebsite, 
B.DmChuyenMucREF, 
B.TenChuyenMuc, 
B.DmLoaiBannerREF, 
B.TenLoaiBanner, 
B.DmViTriREF, 
B.TenViTri, 
--Thong tin ve Tien
B.SoLuong, B.DonViTinh, B.DonGia, 
dbo.ThucChay_GetDonGiaTheoDonViTinh(B.SoLuong,B.DonViTinh,B.DonGia,C.NgayKyHopDong)AS DonGiaTheoDonVi,
B.ChietKhau, B.GiamGia, B.ThanhTien,
B.TiLeTuVan,  B.ChiPhiTuVan,
B.IsKhuyenMai,  
B.KhuyenMai,
--Thuc chay
A.DmBannerREF,
A.DmChienDichREF,
A.DmWebsiteREF,
A.TenWebsite,
--A.SoHopDong,
A.TongViewThucChay,
A.TongClickThucChay,
A.TongSoBaiViet,
dbo.ThucChay_GetSoLuongThucChayByDonViTinh(A.TongViewThucChay,A.TongClickThucChay,A.TongSoBaiViet,B.DonViTinh) AS SoLuongThucChay,
--Thanhuc Tien Thuc Chay
A.NgayThucHien,
dbo.ThucChay_TinhGiaTriThayDoi(B.DonViTinh,A.NgayThucHien,A.HopDongChiTietREF,B.HopDongFK,B.DonGia) AS GiaTriThayDoi,
dbo.ThucChay_GetThanhTienThucChay(B.SoLuong, B.DonViTinh, B.DonGia, C.NgayKyHopDong, A.TongViewThucChay,A.TongClickThucChay,A.TongSoBaiViet) AS ThanhTienThucChayTruocTrietKhau
FROM dbo.ThucChay A

INNER JOIN dbo.GetHopDongChiTietThayDoiAll() B 
ON A.HopDongChiTietREF = B.HopDongChiTietID 
--ON dbo.ThucChay_GetHopDongChiTietID(A.HopDongChiTietREF, A.DanhsachDmBookingREF,A.SoHopDong) = B.HopDongChiTietID 
INNER JOIN dbo.HopDong C ON C.HopDongID = B.HopDongFK

WHERE (UPPER(B.DonViTinh) <> 'CPC' AND UPPER(B.DonViTinh) <> 'GOI')

) TC


END

--EXEC [ThucChay_SelectAll]


```
