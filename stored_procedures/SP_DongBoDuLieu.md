# Stored Procedure: `DongBoDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-28 16:59:15.393000
- **Ngày sửa cuối**: 2020-09-17 09:41:09.527000

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
CREATE PROCEDURE [dbo].[DongBoDuLieu]
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
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate
	WHILE (@NgayThucHien <= @EndDate)
		BEGIN
		UPDATE dbo.ThucChayDaTinh SET IsPheDuyet = 0 WHERE NgayThucHien = @NgayThucHien AND IsPheDuyet IS NULL
		--I. Insert vào [192.168.23.217].ABM_Data_Release
		--1. Table ThucChayDaTinh
		--Xoa du lieu truoc insert
		DELETE FROM [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinh 
		WHERE NgayThucHien = @NgayThucHien
		AND DmChienDichREF = 0 --chi lay mua ngoai
		----Insert du lieu
		INSERT INTO [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinh
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
		WHERE tcdt.NgayThucHien = @NgayThucHien
		AND DmChienDichREF = 0 --chi lay mua ngoai
		
		--2. Table ThucChayDaTinhAdmarket
		--Xoa du lieu truoc insert
		DELETE FROM [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket 
		WHERE NgayThucHien = @NgayThucHien
		----Insert du lieu
		INSERT INTO [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket
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
           ,[GhiChu] 
		FROM ThucChayDaTinhAdmarket tcdt
		WHERE tcdt.NgayThucHien = @NgayThucHien		
			
		--2. Table ThucChay_LogNNTinhGiaTriThayDoi
		--Xoa du lieu truoc insert
		DELETE FROM [192.168.23.217].ABM_Data_Release.dbo.ThucChay_LogNNTinhGiaTriThayDoi 
		WHERE NgayThucHien = @NgayThucHien
		--Insert du lieu
		INSERT INTO [192.168.23.217].ABM_Data_Release.dbo.ThucChay_LogNNTinhGiaTriThayDoi
		SELECT * FROM ThucChay_LogNNTinhGiaTriThayDoi tcdt
		WHERE tcdt.NgayThucHien = @NgayThucHien		

		--3. ThucChayDaTinh_MuaNgoai
		DELETE FROM [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinh_MuaNgoai 
		WHERE NgayThucHien = @NgayThucHien
		AND DmChienDichREF = 0 --chi lay mua ngoai
		--Insert du lieu
		INSERT INTO [192.168.23.217].ABM_Data_Release.dbo.ThucChayDaTinh_MuaNgoai
		SELECT * FROM ThucChayDaTinh_MuaNgoai tcdt
		WHERE tcdt.NgayThucHien = @NgayThucHien	
		AND tcdt.DmChienDichREF = 0 --chi lay mua ngoai
	

		--II.Insert vào [192.168.5.38].ABM_Data_Partner
		--ThucChayDaTinh
		DELETE FROM ABM_Data_Partner.dbo.ThucChayDaTinh
			WHERE NgayThucHien = @NgayThucHien		
		----Insert du lieu
		INSERT INTO  ABM_Data_Partner.dbo.ThucChayDaTinh
			SELECT * FROM ThucChayDaTinh tcdt
			WHERE NgayThucHien = @NgayThucHien
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
		--ThucChayAdmarketPublisher	
		DELETE FROM ABM_Data_Partner.dbo.ThucChayAdmarketPublisher
			WHERE NgayThucHien = @NgayThucHien

		INSERT INTO ABM_Data_Partner.dbo.ThucChayAdmarketPublisher
			select * from dbo.ThucChayAdmarketPublisher tcap
			WHERE NgayThucHien = @NgayThucHien	
	
		--II.Insert vào [192.168.23.217].ABM_Data_Partner
		--ThucChayDaTinh
		DELETE FROM [192.168.23.217].ABM_Data_Partner.dbo.ThucChayDaTinh
			WHERE NgayThucHien = @NgayThucHien		
		----Insert du lieu
		INSERT INTO  [192.168.23.217].ABM_Data_Partner.dbo.ThucChayDaTinh
			SELECT * FROM ABM_Data_Partner.dbo.ThucChayDaTinh tcdt
			WHERE NgayThucHien = @NgayThucHien
		--ThucChayAdmarketPublisher	
		DELETE FROM [192.168.23.217].ABM_Data_Partner.dbo.ThucChayAdmarketPublisher
			WHERE NgayThucHien = @NgayThucHien

		INSERT INTO [192.168.23.217].ABM_Data_Partner.dbo.ThucChayAdmarketPublisher
			select * from ABM_Data_Partner.dbo.ThucChayAdmarketPublisher tcap
			WHERE NgayThucHien = @NgayThucHien

		--III. Dong bo bang [DmWebsiteReportingdb]
		DELETE FROM [192.168.23.217].ABM_Data_Release.dbo.DmWebsiteReportingdb
		WHERE CONVERT(date,CreatedAt) = @NgayThucHien
		
		INSERT INTO [192.168.23.217].ABM_Data_Release.dbo.DmWebsiteReportingdb
	
		SELECT  * FROM DmWebsiteReportingdb dwr 
		WHERE dwr.TenWebsite IS NOT NULL 
		AND CONVERT(date,dwr.CreatedAt) = @NgayThucHien		



		--IV.	Insert into Log [ABM_Data_Release]
		
		--Cung Server
		INSERT INTO [ABM_Data_ThucChay].dbo.SysThuChay_HDCNLog 
		(MaHanhDong,IsHanhDong,NgayThucHien,ThoiGianChotSoLieu,NguoiThucHien,IsDongBo,ThoiGianHoanThanhDongBo)
		SELECT 
		 1 as MaHanhDong
		,1 as IsHanhDong
		,@NgayThucHien as NgayThucHien
		,getdate() as ThoiGianChotSoLieu
		,'phuonglt' as NguoiThucHien
		,0 as IsDongBo
		,null as ThoiGianHoanThanhDongBo
		
		--Insert into Log [192.168.23.217].[ABM_Data_Release]
		INSERT INTO [192.168.23.217].[ABM_Data_Release].dbo.SysThuChay_HDCNLog
		(MaHanhDong,IsHanhDong,NgayThucHien,ThoiGianChotSoLieu,NguoiThucHien,IsDongBo,ThoiGianHoanThanhDongBo)		 
		SELECT 
		 1 as MaHanhDong
		,1 as IsHanhDong
		,@NgayThucHien as NgayThucHien
		,getdate() as ThoiGianChotSoLieu
		,'phuonglt' as NguoiThucHien
		,0 as IsDongBo
		,null as ThoiGianHoanThanhDongBo
				
		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		
		END
		
	--COMMIT TRANSACTION
	--END TRY
	--BEGIN CATCH
	--IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION
	---- Error Message
	--DECLARE @Err nvarchar(1000)
	--SET @Err = ERROR_MESSAGE()
	--RAISERROR (@Err,16,1)
	--END CATCH
END

```
