# Stored Procedure: `UpdateHTQC_PR_PRSolution`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-11-12 16:54:56
- **Ngày sửa cuối**: 2015-11-12 17:27:57.673000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC UpdateHTQC_PR_PRSolution '2015-11-11',4800000,75407,141
CREATE PROCEDURE [dbo].[UpdateHTQC_PR_PRSolution]
 @NgayThucHien DATETIME,
 @GiaTriThayDoi FLOAT,	
 @HopDongChiTietREF INT,
 @DmSanPhamREF INT
AS
BEGIN
	INSERT INTO thucchaydatinh		
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
 	'' PheDuyetAt,1,0,0,''	
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
 	 10 AS DmHinhThucQuangCao,-- C.DmLoaiREF
 	 'PR' AS TenHinhThucQuangCao, --C.TenLoai	
 	--Thong tin San pham	
 	@DmSanPhamREF as DmSanPhamREF,	
 	(SELECT TOP 1 dsptc.TenSanPham	
 	   FROM DmSanPhamThucChay dsptc WHERE dsptc.DmSanPhamREF = @DmSanPhamREF AND dsptc.DeletedStatus <> 1)TenSanPham,  	
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
 	'PR_TTR' DotChayHopDong,
 	0 AS SoLuongDotChayHD,	
 	'PS THUC TREO PR' DotChayBooking,	
 	0 AS SoLuongDotChayBooking, 	
 	--Thong tin ve Tien	
 	ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuong, 	
 	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 	
 	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 	
 	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh,	
 	C.ChietKhau, C.GiamGia, C.ThanhTien,	
 	C.TiLeTuVan,  C.ChiPhiTuVan,	
 	C.IsKhuyenMai,  	
 	C.KhuyenMai,	
 	--Thuc chay	
 	0 DmBannerREF,	
 	0 DmChienDichREF,	
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
 		SELECT * FROM HopDongChiTiet WHERE 1=1 
 		AND HopDongChiTietID = @HopDongChiTietREF
 	) C  	
 	INNER JOIN  	
 	 ( 	
 	 	SELECT * FROM HopDong hd 
 	    WHERE hd.TrangThaiHopDong != 3	
 	 ) D on D.HopDongID = C.HopDongFK	
 	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF	
 	) TD
 	
 	-- insert pr solusion
 	INSERT INTO thucchaydatinh		
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
 	'' PheDuyetAt,1,0,0,''	
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
 	 34 AS DmHinhThucQuangCao,-- C.DmLoaiREF
 	 'PR Solution' AS TenHinhThucQuangCao, --C.TenLoai	
 	--Thong tin San pham	
 	@DmSanPhamREF as DmSanPhamREF,	
 	(SELECT TOP 1 dsptc.TenSanPham	
 	   FROM DmSanPhamThucChay dsptc WHERE dsptc.DmSanPhamREF = @DmSanPhamREF AND dsptc.DeletedStatus <> 1)TenSanPham,  	
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
 	'PR_TTR' DotChayHopDong,
 	0 AS SoLuongDotChayHD,	
 	'PS THUC TREO PR' DotChayBooking,	
 	0 AS SoLuongDotChayBooking, 	
 	--Thong tin ve Tien	
 	ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuong, 	
 	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 	
 	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 	
 	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh,	
 	C.ChietKhau, C.GiamGia, C.ThanhTien,	
 	C.TiLeTuVan,  C.ChiPhiTuVan,	
 	C.IsKhuyenMai,  	
 	C.KhuyenMai,	
 	--Thuc chay	
 	0 DmBannerREF,	
 	0 DmChienDichREF,	
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
 		SELECT * FROM HopDongChiTiet WHERE 1=1 
 		AND HopDongChiTietID = @HopDongChiTietREF
 	) C  	
 	INNER JOIN  	
 	 ( 	
 	 	SELECT * FROM HopDong hd 
 	    WHERE hd.TrangThaiHopDong != 3	
 	 ) D on D.HopDongID = C.HopDongFK	
 	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF	
 	) TD
END


```
