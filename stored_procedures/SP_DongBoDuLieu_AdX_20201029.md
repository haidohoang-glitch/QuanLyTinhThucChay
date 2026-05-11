# Stored Procedure: `DongBoDuLieu_AdX_20201029`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-10-30 10:47:15.800000
- **Ngày sửa cuối**: 2020-10-30 10:48:29.940000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql



-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [CompareDongBoDuLieu] '2014-01-01','2015-04-09'

--EXEC [DongBoDuLieu] '2015-03-15','2015-03-15'
CREATE PROCEDURE [dbo].[DongBoDuLieu_AdX_20201029]
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME, 
	@EndDate DATETIME
AS
BEGIN
	--BEGIN TRY
	--BEGIN TRANSACTION
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
		
		
		--I. Insert vào [ASDAG].ABM_Data_Release
		--1. Table ThucChayDaTinh
		--Xoa du lieu truoc insert
		DELETE FROM [ASDAG].ABM_Data_Release.dbo.ThucChayDaTinh WHERE 1=1
		AND NgayThucHien between @StartDate and @EndDate
		AND DmSanPhamREF = 585 
		AND HopDongID = 0 
		AND DmHinhThucQuangCao <> 42
		----Insert du lieu
		INSERT INTO [ASDAG].ABM_Data_Release.dbo.ThucChayDaTinh
		 ([ThucChayDaTinhID]
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
		SELECT [ThucChayDaTinhID]
		   , [HopDongID]
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
           ,[GhiChu] 
		FROM ThucChayDaTinh tcdt
		WHERE 1=1--tcdt.NgayThucHien = @NgayThucHien
		AND  tcdt.NgayThucHien between @StartDate and @EndDate
		AND  tcdt.DmSanPhamREF = 585 
		AND  tcdt.HopDongID = 0 
		AND  tcdt.DmHinhThucQuangCao <> 42
		
		

	

		--II.Insert vào [192.168.5.38].ABM_Data_Partner
		--ThucChayDaTinh
		DELETE FROM ABM_Data_Partner.dbo.ThucChayDaTinh
			WHERE NgayThucHien between @StartDate and @EndDate	
		----Insert du lieu
		INSERT INTO  ABM_Data_Partner.dbo.ThucChayDaTinh
			SELECT * FROM ThucChayDaTinh tcdt
			WHERE NgayThucHien between @StartDate and @EndDate	
			
			AND (tcdt.DmSanPhamREF NOT IN (144)
				OR ((tcdt.DmSanPhamREF IN (144)) 
					AND (tcdt.DmWebsiteREF IN (265,14907,102139,240233,240252,240313,240263,240397,240240,138535  -- vtv.vn, m.vtv.vn, english.vtv.vn, ims.vtv.vn, imsnews.vtv.vn,lienhoantruyenhinh.vtv.vn,local2.vtv.vn, mobile.vtv.vn, thethao.vtv.vn, m.thethao.vtv.vn
						,1490,138573,155197,171621,240230,240258,240315,140507,240317,240232,240321,240287)-- tuoitre.vn, thethao.tuoitre.vn,nhipsongso.tuoitre.vn, dulich.tuoitre.vn,congnghe.tuoitre.vn,nhadat.tuoitre.vn,mekongxanh.tuoitre.vn,m.mekongxanh.tuoitre.vn,tuoitre.com,beta8.tuoitre.vn,ims.tuoitre.vn,b1.tuoitre.vn,b2.tuoitre.vn
											))
			)
			AND tcdt.DmWebsiteREF IN (85,3144,--giadinh.net.vn , m.giadinh.net.vn
										134,3134--nld.com.vn
										,97219 --subdomain.nld.com.vn
										,102026 -- auto.nld.com.vn
										,102022 -- congnghe.nld.com.vn
										,102018 -- dulich.nld.com.vn
										,102023 -- vnmoney.nld.com.vn
										,102020 -- phunu.nld.com.vn
										,102019 -- suckhoedinhduong.nld.com.vn
										,101552 -- thitruong.nld.com.vn
										,102027 -- vieclam.nld.com.vn
										,101795 --tv.nld.com.vn
										, 102028 -- m.tv.nld.com.vn
										,102021 --tuyensinh.nld.com.vn	
										,161372 --dulichbien.nld.com.vn	
										--182,3136,--suckhoedoisong.vn - a Ngoc cf bỏ
										,254,3139--vneconomy.vn
										,191,3006,81650, 130898,142809,143503,152443,159719--thanhnien.com.vn, www.thanhnien.com.vn,thanhnien.vn, m.thanhnien.vn,thethao.thanhnien.vn,video.thanhnien.vn,game.thanhnien.vn,xe.thanhnien.vn
										,158626,163814,240385 -- ihay.thanhnien.vn, tinnong.thanhnien.vn, media.thanhnien.vn
										,265,14907,102139,240233,240252,240313,240263,240397,240240,138535  -- vtv.vn, m.vtv.vn, english.vtv.vn, ims.vtv.vn, imsnews.vtv.vn,lienhoantruyenhinh.vtv.vn,local2.vtv.vn, mobile.vtv.vn, thethao.vtv.vn, m.thethao.vtv.vn
										,1490,138573,155197,171621,240230,240258,240315,140507,240317,240232,240321,240287-- tuoitre.vn, thethao.tuoitre.vn,nhipsongso.tuoitre.vn, dulich.tuoitre.vn,congnghe.tuoitre.vn,nhadat.tuoitre.vn,mekongxanh.tuoitre.vn,m.mekongxanh.tuoitre.vn,tuoitre.com,beta8.tuoitre.vn,ims.tuoitre.vn,b1.tuoitre.vn,b2.tuoitre.vn
								)
		





END

```
