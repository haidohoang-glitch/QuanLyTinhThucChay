# Stored Procedure: `ThucChay_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-05-12 11:34:42.113000
- **Ngày sửa cuối**: 2016-11-12 09:57:09.470000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- USE [ABM_Data_Release]
-- GO
-- /****** Object:  StoredProcedure [dbo].[ThucChay_InsertThucChayDaTinh_ChiPhi_SanPhamChinh]    Script Date: 05/12/2016 11:16:46 ******/
-- SET ANSI_NULLS ON
-- GO
-- SET QUOTED_IDENTIFIER ON
-- GO
------------------------------------------------------------
 CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_GiaiPhapCongNghe_SanPhamChinh] 
 	@NgayThucHien DATETIME
 AS
 BEGIN
 
 DECLARE @NgayGioiHanTinh DATETIME
 SET @NgayGioiHanTinh = '2013-01-01'
 	---------***********DANH SACH CAC SAN PHAM CHINH CO TINH CHI PHI*******-------------
 					--BoxApp CPM	 370
 					--Balloon Ads	339
 					--Mobile	342
 
 	----- insert data 
 	INSERT INTO dbo.ThucChayDaTinh 
 	SELECT  NEWID(), TD.*, 
 	ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
 	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,	
 	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
 	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
 	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
 		else 0
 	  END
 	) as ThanhTienKM,
 	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh(@NgayThucHien,@NgayGioiHanTinh ,TD.HopDongChiTietID),0)
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
 	[dbo].[f_ReturnListConcatNhanHangREF_v2] 
 	(
 		C.HopDongChiTietID,
 		@NgayThucHien
 	)NhanHang,
 	C.DmNhomNganhREF, 
 	C.TenNhomNganh, 
 	--Thong tin hinh thuc quang cao
 	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
 	--Thong tin San pham
 	c.DmSanPhamREF as DmSanPhamREF,
 	E.TenSanPham,  
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
 	'' DotChayBooking,
 	0 AS SoLuongDotChayBooking, 
 	--Thong tin ve Tien
 	ISNULL(C.SoLuong,0) AS SoLuong,	
 	isnull(C.DonViTinh, N'đ/v') as DonViTinh, 
 	C.DonGia as DonGia, 
 	C.DonGia AS DonGiaTheoDonViTinh,
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
 	c.SoLuong AS SoLuongThucChay, 
 	--Thanhuc Tien Thuc Chay
 	@NgayThucHien AS NgayThucHien,
 	--c.ThanhTien as GiaTriThayDoi,
	0 as GiaTriThayDoi,
 	C.SoLuong*C.DonGia as ThanhTienThucChayTruocTrietKhau
 	FROM 
 	(
 		SELECT * FROM HopDongChiTiet 
 			WHERE DmSanPhamREF in (370,339,342,598)
 			AND DeletedStatus = 0 
 			AND DmLoaiNenTangREF = 8 --Retargeting & Content base
 			AND NOT((HopDongChiTiet.DmLoaiBannerREF IN (18)) OR (HopDongChiTiet.DmLoaiREF = 13))-- --Khong tinh thuc chay cho HTQC Mua Ngoai
 	) C  
 	INNER JOIN  
 	 ( 
 	 	SELECT * FROM HopDong hd 
 	    WHERE hd.TrangThaiHopDong <> 3
 	    AND hd.DeletedStatus = 0
 	 ) D on D.HopDongID = C.HopDongFK
 	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF 	
 	AND ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID),0) >0
 	AND C.SoLuong >0	 
 	) TD	
	
	EXEC [dbo].[ThucChay_UpdateThucChayHopDongChiTiet_GiaiPhapCongNghe_SanPhamChinh] @NgayThucHien 
 	
	SELECT '1'
 END

```
