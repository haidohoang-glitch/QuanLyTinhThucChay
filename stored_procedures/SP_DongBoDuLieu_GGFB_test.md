# Stored Procedure: `DongBoDuLieu_GGFB_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-09 18:10:44.190000
- **Ngày sửa cuối**: 2021-05-25 10:26:52.250000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql


-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [CompareDongBoDuLieu] '2014-01-01','2015-04-09'

--EXEC [DongBoDuLieu_GGFB_test]
CREATE PROCEDURE [dbo].[DongBoDuLieu_GGFB_test]
	-- Add the parameters for the stored procedure here

AS
BEGIN
/*
insert into [ASDAG].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket ([ThucChayDaTinhID]
      ,[HopDongID]
      ,[SoHopDong]
      ,[DmMaHopDongREF]
      ,[TenMaHopDong]
      ,[NgayDanhSoHopDong]
      ,[NgayKyHopDong]
      ,[NhanHopDong]
      ,[NgayNhanBanFax]
      ,[NgayNhanHopDongBanCung]
      ,[NgayChuyenHopDongChoKeToan]
      ,[So]
      ,[Thang]
      ,[Nam]
      ,[GiaTriHopDong]
      ,[CongNo]
      ,[HopDongChiTietREF]
      ,[DangSuDung]
      ,[IsGiayPhep]
      ,[TrangThaiHopDong]
      ,[IsBanCung]
      ,[DmPhongBanREF]
      ,[TenPhongBan]
      ,[DmBoPhanREF]
      ,[TenBoPhan]
      ,[DmNhomLamViecREF]
      ,[TenNhomLamViec]
      ,[DmDiaDiemLamViecREF]
      ,[TenDiaDiemLamViec]
      ,[SysNhanVienREF]
      ,[TenDangNhap]
      ,[TenNhanVien]
      ,[TenKhachHang]
      ,[NhanHang]
      ,[DmNhomNganhREF]
      ,[TenNhomNganh]
      ,[DmHinhThucQuangCao]
      ,[TenHinhThucQuangCao]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmNhomWebsiteREF]
      ,[TenNhomWebsite]
      ,[DmChuyenMucREF]
      ,[TenChuyenMuc]
      ,[DmLoaiBannerREF]
      ,[TenLoaiBanner]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[DotChayHopDong]
      ,[SoLuongDotChayHD]
      ,[DotChayBooking]
      ,[SoLuongDotChayBooking]
      ,[SoLuong]
      ,[DonViTinh]
      ,[DonGia]
      ,[DonGiaTheoDonVi]
      ,[ChietKhau]
      ,[GiamGia]
      ,[ThanhTien]
      ,[TiLeTuVan]
      ,[ChiPhiTuVan]
      ,[IsKhuyenMai]
      ,[KhuyenMai]
      ,[DmBannerREF]
      ,[DmChienDichREF]
      ,[DmWebsiteREF]
      ,[TenWebsite]
      ,[TongViewThucChay]
      ,[TongClickThucChay]
      ,[TongSoBaiViet]
      ,[SoLuongThucChay]
      ,[NgayThucHien]
      ,[GiaTriThayDoi]
      ,[ThanhTienThucChayTruocTrietKhau]
      ,[GiaTriTrietKhauThucChay]
      ,[ThanhTienSauTrietKhauThucChay]
      ,[GiaTriHoaHongThucChay]
      ,[ThanhTienThucThu]
      ,[ThanhTienKM]
      ,[SoLuongThucChayKM]
      ,[SoLuongThucChayLechTreoHa]
      ,[ThanhTienLechTreoHa]
      ,[CreatedAt]
      ,[LastModifiedAt]
      ,[IsPheDuyet]
      ,[PheDuyetBy]
      ,[PheDuyetAt]
      ,[SoLuongThayDoi]
      ,[SoLuongKMThayDoi]
      ,[GiaTriKMThayDoi]
      ,[GhiChu])
select [ThucChayDaTinhID]
      ,[HopDongID]
      ,[SoHopDong]
      ,[DmMaHopDongREF]
      ,[TenMaHopDong]
      ,[NgayDanhSoHopDong]
      ,[NgayKyHopDong]
      ,[NhanHopDong]
      ,[NgayNhanBanFax]
      ,[NgayNhanHopDongBanCung]
      ,[NgayChuyenHopDongChoKeToan]
      ,[So]
      ,[Thang]
      ,[Nam]
      ,[GiaTriHopDong]
      ,[CongNo]
      ,[HopDongChiTietREF]
      ,[DangSuDung]
      ,[IsGiayPhep]
      ,[TrangThaiHopDong]
      ,[IsBanCung]
      ,[DmPhongBanREF]
      ,[TenPhongBan]
      ,[DmBoPhanREF]
      ,[TenBoPhan]
      ,[DmNhomLamViecREF]
      ,[TenNhomLamViec]
      ,[DmDiaDiemLamViecREF]
      ,[TenDiaDiemLamViec]
      ,[SysNhanVienREF]
      ,[TenDangNhap]
      ,[TenNhanVien]
      ,[TenKhachHang]
      ,[NhanHang]
      ,[DmNhomNganhREF]
      ,[TenNhomNganh]
      ,[DmHinhThucQuangCao]
      ,[TenHinhThucQuangCao]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[DmNhomWebsiteREF]
      ,[TenNhomWebsite]
      ,[DmChuyenMucREF]
      ,[TenChuyenMuc]
      ,[DmLoaiBannerREF]
      ,[TenLoaiBanner]
      ,[DmViTriREF]
      ,[TenViTri]
      ,[DotChayHopDong]
      ,[SoLuongDotChayHD]
      ,[DotChayBooking]
      ,[SoLuongDotChayBooking]
      ,[SoLuong]
      ,[DonViTinh]
      ,[DonGia]
      ,[DonGiaTheoDonVi]
      ,[ChietKhau]
      ,[GiamGia]
      ,[ThanhTien]
      ,[TiLeTuVan]
      ,[ChiPhiTuVan]
      ,[IsKhuyenMai]
      ,[KhuyenMai]
      ,[DmBannerREF]
      ,[DmChienDichREF]
      ,[DmWebsiteREF]
      ,[TenWebsite]
      ,[TongViewThucChay]
      ,[TongClickThucChay]
      ,[TongSoBaiViet]
      ,[SoLuongThucChay]
      ,[NgayThucHien]
      ,[GiaTriThayDoi]
      ,[ThanhTienThucChayTruocTrietKhau]
      ,[GiaTriTrietKhauThucChay]
      ,[ThanhTienSauTrietKhauThucChay]
      ,[GiaTriHoaHongThucChay]
      ,[ThanhTienThucThu]
      ,[ThanhTienKM]
      ,[SoLuongThucChayKM]
      ,[SoLuongThucChayLechTreoHa]
      ,[ThanhTienLechTreoHa]
      ,[CreatedAt]
      ,[LastModifiedAt]
      ,[IsPheDuyet]
      ,[PheDuyetBy]
      ,[PheDuyetAt]
      ,[SoLuongThayDoi]
      ,[SoLuongKMThayDoi]
      ,[GiaTriKMThayDoi]
      ,[GhiChu] from ThucChayDaTinhAdmarket  where hopdongchitietref in (616006,616007,616008) and NgayThucHien = '2021-05-13' and CreatedAt >'2021-05-15 10:30' and DmSanPhamREF = 585
	  */

	  --select top 1 * from [ASDAG].ABM_Data_Release.dbo.ThucChayDaTinh where NgayThucHien = '2021-05-23'
	  update  [ASDAG].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket set GhiChu = GhiChu + ' ' where ThucChayDaTinhID = '00073D0C-7887-4AD5-96C5-D0B3557DB365' and NgayThucHien = '2021-05-23'
	  update  [ASDAG].ABM_Data_Release.dbo.ThucChayDaTinh set GhiChu = GhiChu + ' ' where ThucChayDaTinhID = '8ED8A460-81DC-4F85-A76A-6A1800E186C4' and NgayThucHien = '2021-05-23'
END




```
