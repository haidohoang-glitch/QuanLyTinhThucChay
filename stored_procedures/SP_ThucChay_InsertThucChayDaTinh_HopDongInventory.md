# Stored Procedure: `ThucChay_InsertThucChayDaTinh_HopDongInventory`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-13 10:11:57.563000
- **Ngày sửa cuối**: 2021-05-31 17:28:13.657000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChitietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@CreateBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
/*
[dbo].[ThucChay_InsertThucChayDaTinh_HopDongInventory] 
	@NgayThucHien = '2016-10-10',
	@HopDongID INT,
	@HopDongChitietID INT,
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(200),
	@CreateBy NVARCHAR(50)
*/

-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_HopDongInventory] 
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChitietID INT,
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(200),
	@CreateBy NVARCHAR(50)
AS
BEGIN

	DECLARE @NgayGioiHanTinh DATETIME
	--, @isInsertThucChayDaTinh_YN int = 0
	, @isExistHopDongChiTietBanInventory int =0
	SET @NgayGioiHanTinh = '2013-01-01'

	IF(NOT EXISTS(SELECT TOP (1) HopDongChiTietREF FROM dbo.DmThongTinHopDongBanInventory
		WHERE HopDongREF =@HopDongID
		AND ISNULL(HopDongChiTietREF,0) = @HopDongChitietID
		ORDER BY HopDongChiTietREF
		)) 
	BEGIN
		--Neu khong phai la san pham admarket
		print 'No Admarket'
		IF(@DmSanPhamREF NOT IN (585,144,628)) 
		begin
			INSERT INTO dbo.ThucChayDaTinh 
			SELECT  NEWID(), TD.*, 
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
			TD.ThanhTien AS ThanhTienSauTrietKhauThucChay,	
			ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
			(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
				else 0
			  END
			) as ThanhTienKM,
			(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.Soluong
				else 0
			  END
			) as SoLuongThucChayKM,
			0 SoLuongLechTreoHa,
			0 ThanhTienLechTreoHa,
			GETDATE(),
			GETDATE(),
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			0 SoLuongThayDoi,
			0 SoLuongKMThayDoi,
			0 GiaTriKMThayDoi,
			'HDBAN_INVENTORY' GhiChu	
			FROM 
			(
			SELECT 
			--ID Hop Dong
			D.HopDongID,
			--Thong tin ve ma so 
			D.SoHopDong, 
			D.DmMaHopDongREF, 
			D.TenMaHopDong, 
			--Thong tin ve thoi gian
			D.NgayDanhSoHopDong, D.NgayKyHopDong, 
			ISNULL(D.NhanHopDong,'') AS NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
			D.So, D.Thang, D.Nam, 
			--Thong tin ve gia tri
			D.GiaTriHopDong, D.CongNo,
			--Thong tin chi tiet phan bo
			C.HopDongChiTietID,
			--Thong tin ve trang thai
			D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
			--Thong tin ve Nhan vien kinh doanh
			D.DmPhongBanREF, 
			ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
			D.DmBoPhanREF, 
			ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
			D.DmNhomLamViecREF, 
			ISNULL(D.TenNhom, '') AS TenNhom, 
			D.DmDiaDiemLamViecREF, 
			D.TenDiaDiemLamViec, 
			D.SysNhanVienREF, 
			ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
			D.TenNhanVien, 
			--Thong tin ve khach hang
			--D.DmKhachHangREF, 
			D.TenKhachHang, 
			C.DanhSachNhanHangREF, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			c.DmSanPhamREF as DmSanPhamREF,
			c.TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			C.DmViTriREF, 
			C.TenViTri, 
			'' DotChayHopDong,
			0 AS SoLuongDotChayHD,		
			'HDBAN_INVENTORY' DotChayBooking,
			0 AS SoLuongDotChayBooking, 
			--Thong tin ve Tien
			C.SoLuong AS SoLuong,	
			isnull(C.DonViTinh, N'đ/v') as DonViTinh, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
			--A.DmWebsiteREF,
			dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			--C.TenWebsite,
			--A.SoHopDong,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			(CASE when C.IsKhuyenMai=0 then c.SoLuong
				else 0
			  END
			) as SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien AS NgayThucHien,
			0 as GiaTriThayDoi,
			C.SoLuong*C.DonGia as ThanhTienThucChayTruocTrietKhau
			FROM 
			(
				SELECT * FROM HopDongChiTiet 
				WHERE 1=1
				AND HopDongChiTietID = @HopDongChitietID
				AND HopDongFK = @HopDongID
				AND DeletedStatus = 0 
   				AND NOT (DmLoaiREF = 13 or DmLoaiBannerREF = 18)	 --Khong tinh thuc chay cho HTQC Mua Ngoai
				AND SoLuong >0
				
			) C  
			INNER JOIN  
			 ( 
	 			SELECT * FROM HopDong hd 
				WHERE hd.HopDongID = @HopDongID
				AND hd.TrangThaiHopDong <> 3
				AND hd.DeletedStatus = 0
			 ) D on D.HopDongID = C.HopDongFK
			) TD
		end
		ELSE
		BEGIN
			--THUCCHAYDATINHADMARKET
			INSERT INTO dbo.ThucChayDaTinhAdmarket
			SELECT  NEWID(), TD.*, 
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
			TD.ThanhTien AS ThanhTienSauTrietKhauThucChay,	
			ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
			(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
				else 0
			  END
			) as ThanhTienKM,
			(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.Soluong
				else 0
			  END
			) as SoLuongThucChayKM,
			0 SoLuongLechTreoHa,
			0 ThanhTienLechTreoHa,
			GETDATE(),
			GETDATE(),
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			0 SoLuongThayDoi,
			0 SoLuongKMThayDoi,
			0 GiaTriKMThayDoi,
			'HDBAN_INVENTORY' GhiChu	
			FROM 
			(
			SELECT 
			--ID Hop Dong
			D.HopDongID,
			--Thong tin ve ma so 
			D.SoHopDong, 
			D.DmMaHopDongREF, 
			D.TenMaHopDong, 
			--Thong tin ve thoi gian
			D.NgayDanhSoHopDong, D.NgayKyHopDong, 
			ISNULL(D.NhanHopDong,'') AS NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
			D.So, D.Thang, D.Nam, 
			--Thong tin ve gia tri
			D.GiaTriHopDong, D.CongNo,
			--Thong tin chi tiet phan bo
			C.HopDongChiTietID,
			--Thong tin ve trang thai
			D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
			--Thong tin ve Nhan vien kinh doanh
			D.DmPhongBanREF, 
			ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
			D.DmBoPhanREF, 
			ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
			D.DmNhomLamViecREF, 
			ISNULL(D.TenNhom, '') AS TenNhom, 
			D.DmDiaDiemLamViecREF, 
			D.TenDiaDiemLamViec, 
			D.SysNhanVienREF, 
			ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
			D.TenNhanVien, 
			--Thong tin ve khach hang
			--D.DmKhachHangREF, 
			D.TenKhachHang, 
			C.DanhSachNhanHangREF, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			c.DmSanPhamREF as DmSanPhamREF,
			c.TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			C.DmViTriREF, 
			C.TenViTri, 
			'' DotChayHopDong,
			0 AS SoLuongDotChayHD,		
			'HDBAN_INVENTORY' DotChayBooking,
			0 AS SoLuongDotChayBooking, 
			--Thong tin ve Tien
			C.SoLuong AS SoLuong,	
			isnull(C.DonViTinh, N'đ/v') as DonViTinh, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
			--A.DmWebsiteREF,
			dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			--C.TenWebsite,
			--A.SoHopDong,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			(CASE when C.IsKhuyenMai=0 then c.SoLuong
				else 0
			  END
			) as SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien AS NgayThucHien,
			0 as GiaTriThayDoi,
			C.SoLuong*C.DonGia as ThanhTienThucChayTruocTrietKhau
			FROM 
			(
				SELECT * FROM HopDongChiTiet 
				WHERE 1=1
				AND HopDongChiTietID = @HopDongChitietID
				AND HopDongFK = @HopDongID
				AND DeletedStatus = 0 
   				AND NOT (DmLoaiREF = 13 or DmLoaiBannerREF = 18)	 --Khong tinh thuc chay cho HTQC Mua Ngoai
				AND SoLuong >0
				
			) C  
			INNER JOIN  
			 ( 
	 			SELECT * FROM HopDong hd 
				WHERE hd.HopDongID = @HopDongID
				AND hd.TrangThaiHopDong <> 3
				AND hd.DeletedStatus = 0
			 ) D on D.HopDongID = C.HopDongFK
			
			) TD


			--THUCCHAYDATINH
			INSERT INTO dbo.ThucChayDaTinh 
			SELECT  NEWID(), TD.*, 
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
			TD.ThanhTien AS ThanhTienSauTrietKhauThucChay,	
			ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
			ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
			(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
				else 0
			  END
			) as ThanhTienKM,
			(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.Soluong
				else 0
			  END
			) as SoLuongThucChayKM,
			0 SoLuongLechTreoHa,
			0 ThanhTienLechTreoHa,
			GETDATE(),
			GETDATE(),
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			0 SoLuongThayDoi,
			0 SoLuongKMThayDoi,
			0 GiaTriKMThayDoi,
			'HDBAN_INVENTORY' GhiChu	
			FROM 
			(
			SELECT 
			--ID Hop Dong
			D.HopDongID,
			--Thong tin ve ma so 
			D.SoHopDong, 
			D.DmMaHopDongREF, 
			D.TenMaHopDong, 
			--Thong tin ve thoi gian
			D.NgayDanhSoHopDong, D.NgayKyHopDong, 
			ISNULL(D.NhanHopDong,'') AS NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
			D.So, D.Thang, D.Nam, 
			--Thong tin ve gia tri
			D.GiaTriHopDong, D.CongNo,
			--Thong tin chi tiet phan bo
			C.HopDongChiTietID,
			--Thong tin ve trang thai
			D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
			--Thong tin ve Nhan vien kinh doanh
			D.DmPhongBanREF, 
			ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
			D.DmBoPhanREF, 
			ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
			D.DmNhomLamViecREF, 
			ISNULL(D.TenNhom, '') AS TenNhom, 
			D.DmDiaDiemLamViecREF, 
			D.TenDiaDiemLamViec, 
			D.SysNhanVienREF, 
			ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
			D.TenNhanVien, 
			--Thong tin ve khach hang
			--D.DmKhachHangREF, 
			D.TenKhachHang, 
			C.DanhSachNhanHangREF, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			c.DmSanPhamREF as DmSanPhamREF,
			c.TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			C.DmViTriREF, 
			C.TenViTri, 
			'' DotChayHopDong,
			0 AS SoLuongDotChayHD,		
			'HDBAN_INVENTORY' DotChayBooking,
			0 AS SoLuongDotChayBooking, 
			--Thong tin ve Tien
			C.SoLuong AS SoLuong,	
			isnull(C.DonViTinh, N'đ/v') as DonViTinh, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
			--A.DmWebsiteREF,
			dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			--C.TenWebsite,
			--A.SoHopDong,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			(CASE when C.IsKhuyenMai=0 then c.SoLuong
				else 0
			  END
			) as SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien AS NgayThucHien,
			0 as GiaTriThayDoi,
			C.SoLuong*C.DonGia as ThanhTienThucChayTruocTrietKhau
			FROM 
			(
				SELECT * FROM HopDongChiTiet 
				WHERE 1=1
				AND HopDongChiTietID = @HopDongChitietID
				AND HopDongFK = @HopDongID
				AND DeletedStatus = 0 
   				AND NOT (DmLoaiREF = 13 or DmLoaiBannerREF = 18)	 --Khong tinh thuc chay cho HTQC Mua Ngoai
				AND SoLuong >0
				
			) C  
			INNER JOIN  
			 ( 
	 			SELECT * FROM HopDong hd 
				WHERE hd.HopDongID = @HopDongID
				AND hd.TrangThaiHopDong <> 3
				AND hd.DeletedStatus = 0
			 ) D on D.HopDongID = C.HopDongFK
			) TD

			IF(EXISTS(SELECT top (1) tcdt.HopDongChiTietREF FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND NgayThucHien = @NgayThucHien))
			BEGIN
				INSERT INTO ThucChayDaTinh_inventory_check
				SELECT top (1) tcdt.HopDongChiTietREF, NgayThucHien FROM ThucChayDaTinh tcdt WHERE tcdt.HopDongID = @HopDongID AND tcdt.HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien = @NgayThucHien
			END
		END
			

			--CAP NHAT THONG TIN HOPDONGCHITIET VAO DmThongTinHopDongBanInventory
			SET @isExistHopDongChiTietBanInventory = 
			(
				SELECT COUNT(HopDongREF)sl FROM dbo.DmThongTinHopDongBanInventory
				WHERE HopDongREF = @HopDongID
				AND ISNULL(HopDongChiTietREF,0) = 0
			)
			IF(@isExistHopDongChiTietBanInventory <> 0)
			BEGIN
				UPDATE dbo.DmThongTinHopDongBanInventory
				SET HopDongChiTietREF = @HopDongChitietID
				, DmSanPhamREF = @DmSanPhamREF
				, TenSanPham = @TenSanPham
				, GhiChu = N'Tinh gia tri thuc chay cho HD ban inventory'
				, LastModifiedAt = GETDATE()
				, LastModifiedBy = @CreateBy
				WHERE HopDongREF = @HopDongID
				AND ISNULL(HopDongChiTietREF,0) = 0
			END
			ELSE
            BEGIN
            	INSERT INTO dbo.DmThongTinHopDongBanInventory
				SELECT hd.HopDongID, hd.SoHopDong, hd.NgayDanhSoHopDong, hd.SysNhanVienREF, hd.DmKhachHangREF
				, hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham,  N'Tinh gia tri thuc chay cho HD ban inventory'
				, GETDATE(), @CreateBy, GETDATE(), @CreateBy, 0, 0   
				FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				WHERE hd.TrangThaiHopDong <>3
				AND hd.DeletedStatus = 0
				AND hdct.DeletedStatus =0
				AND hd.HopDongID = @HopDongID
				AND hdct.HopDongChiTietID = @HopDongChitietID
				AND NOT (DmLoaiREF = 13 or DmLoaiBannerREF = 18)
            END
	END
	--SELECT '1'
END


```
