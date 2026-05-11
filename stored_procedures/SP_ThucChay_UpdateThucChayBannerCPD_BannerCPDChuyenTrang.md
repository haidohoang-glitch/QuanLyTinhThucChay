# Stored Procedure: `ThucChay_UpdateThucChayBannerCPD_BannerCPDChuyenTrang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:59.270000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.780000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgaythucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_UpdateThucChayBannerCPD_BannerCPDChuyenTrang] '2014-09-17'


CREATE PROCEDURE [dbo].[ThucChay_UpdateThucChayBannerCPD_BannerCPDChuyenTrang] 
	
	@NgaythucHien DATETIME
	
	
AS
BEGIN
	DECLARE @HopDongChiTiet INT,@GiaTriThayDoi FLOAT, @SoHopDong NVARCHAR(50)
	
	DECLARE Record_cusor CURSOR FOR
		SELECT a.SoHopDong, a.HopDongChiTietID FROM dbo.BannerCPDChuyenTrang a
	OPEN Record_cusor
	FETCH NEXT FROM Record_cusor INTO @SoHopDong, @HopDongChiTiet
	WHILE @@FETCH_STATUS = 0
	BEGIN
		SET @GiaTriThayDoi =
		(
			SELECT SUM(isnull(TCDT.ThanhTienSauTrietKhauThucChay,0) + isnull(TCDT.GiaTriThayDoi,0)) ThanhTienThucChay
			  FROM ThucChayDaTinh tcdt
			WHERE TCDT.HopDongChiTietREF = @HopDongChiTiet
			AND tcdt.DmSanPhamREF = 140
		)
		IF(@GiaTriThayDoi <>0)
		BEGIN
			--1. UPDATE GIA TRI THAY DOI CHO BANNER CPD
			PRINT @HopDongChiTiet
			INSERT INTO dbo.ThucChayDaTinh 
			SELECT  NEWID(), TD.*, 
			0 GiaTriTrietKhauThucChay,
			0 AS ThanhTienSauTrietKhauThucChay,
			0 AS GiaTriHoaHongThucChay,
			0 AS ThanhTienThucThu,
			0 as ThanhTienKM,
			0 as SoLuongThucChayKM,
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
			'' GhiChu	
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
			C.NhanHang, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			140 as DmSanPhamREF,
			N'Banner CPD' TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			--C.DmWebsiteREF, 
			--C.TenWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			C.DmViTriREF, 
			C.TenViTri, 
			'CPD_TTR' DotChayHopDong,
			ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuongDotChayHD,
			'PS THUC TREO CPD' DotChayBooking,
			0 AS SoLuongDotChayBooking, 
			--Thong tin ve Tien
			C.SoLuong AS SoLuong, 
			dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
			ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
			dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			0 SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien AS NgayThucHien,
			-@GiaTriThayDoi as GiaTriThayDoi,
			0 as ThanhTienThucChayTruocTrietKhau
			FROM 
			(
				SELECT * FROM HopDongChiTiet WHERE DmSanPhamREF in (140,228,241,564,549)
				AND HopDongChiTietID = @HopDongChiTiet
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 1 --Đơn vị của hình thức CPD 
			) C  
			INNER JOIN  
			 ( 
	 			SELECT * FROM HopDong hd 
				WHERE hd.TrangThaiHopDong != 3
			 ) D on D.HopDongID = C.HopDongFK
			INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
			) TD
			
			--2. UPDATE GIA TRI THAY DOI CHO BANNER CPD CHUYEN TRANG
			PRINT @HopDongChiTiet
			INSERT INTO dbo.ThucChayDaTinh 
			SELECT  NEWID(), TD.*, 
			0 GiaTriTrietKhauThucChay,
			0 AS ThanhTienSauTrietKhauThucChay,
			0 AS GiaTriHoaHongThucChay,
			0 AS ThanhTienThucThu,
			0 as ThanhTienKM,
			0 as SoLuongThucChayKM,
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
			'' GhiChu	
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
			C.NhanHang, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			c.DmSanPhamREF as DmSanPhamREF,
			E.TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			--C.DmWebsiteREF, 
			--C.TenWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			C.DmViTriREF, 
			C.TenViTri, 
			'CPD_TTR' DotChayHopDong,
			ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuongDotChayHD,
			'PS THUC TREO CPD' DotChayBooking,
			0 AS SoLuongDotChayBooking, 
			--Thong tin ve Tien
			C.SoLuong AS SoLuong, 
			dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
			ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
			dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			0 SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien AS NgayThucHien,
			@GiaTriThayDoi as GiaTriThayDoi,
			0 as ThanhTienThucChayTruocTrietKhau
			FROM 
			(
				SELECT * FROM HopDongChiTiet WHERE DmSanPhamREF in (140,228,241,564,549)
				AND HopDongChiTietID = @HopDongChiTiet
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 1 --Đơn vị của hình thức CPD 
			) C  
			INNER JOIN  
			 ( 
	 			SELECT * FROM HopDong hd 
				WHERE hd.TrangThaiHopDong != 3
			 ) D on D.HopDongID = C.HopDongFK
			INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
			) TD
		END
		

		FETCH NEXT FROM Record_cusor INTO @SoHopDong, @HopDongChiTiet
	END
	CLOSE Record_cusor
	DEALLOCATE  Record_cusor
	
	
END

```
