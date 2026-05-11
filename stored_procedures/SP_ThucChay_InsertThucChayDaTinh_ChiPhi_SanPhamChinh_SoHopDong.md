# Stored Procedure: `ThucChay_InsertThucChayDaTinh_ChiPhi_SanPhamChinh_SoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:17.957000
- **Ngày sửa cuối**: 2019-03-21 17:01:42.127000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [ThucChay_InsertThucChayDaTinh_ChiPhi_SanPhamChinh_SoHopDong] '2016-04-20','2016-04-20','',93441
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_ChiPhi_SanPhamChinh_SoHopDong] 
	@StartDate datetime,
	@EndDate DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietREF INT
AS
BEGIN

DECLARE @NgayThucHien DATETIME, @NgayGioiHanTinh DATETIME
set @NgayThucHien = Convert(date,@StartDate)
SET @NgayGioiHanTinh = '2013-01-01'
---------***********DANH SACH CAC SAN PHAM CHINH CO TINH CHI PHI*******-------------
					--Banner CPD 140
					--Banner CPD Chuyên Trang 228
					--BoxApp CPD 549
					--BoxApp Multi	564
					--Box App Self-serving	375
					--CPM Chuyên Trang 231
					--CPM Mass 238
					--CPM Admarket 337
					--CPMulti 531
					--BoxApp CPM	 370
					--Balloon Ads	339
					--Mobile	342
					--Ad page	305
					--Sponsor Post	381
					--TVC 240


WHILE(@NgayThucHien <= @EndDate)
BEGIN	 
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
	--C.NhanHang, 
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
	--C.DmWebsiteREF, 
	--C.TenWebsite, 
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
	--A.DmWebsiteREF,
	dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
	--C.TenWebsite,
	--A.SoHopDong,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	--(CASE when C.IsKhuyenMai=0 then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID),0)
	--	else 0
	--  END
	--) as SoLuongThucChay,
	c.SoLuong AS SoLuongThucChay, 
	--Thanhuc Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	0 as GiaTriThayDoi,
	c.SoLuong * c.DonGia as ThanhTienThucChayTruocTrietKhau
	--ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID),0) * ISNULL(C.DonGia,0) as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT * FROM HopDongChiTiet 
			WHERE DmSanPhamREF in (140,228,549,564,375,231,238,337,531,370,339,342,305,381,240,680,240,821)
			AND HopDongChiTietID = @HopDongChiTietREF
			AND DmLoaiBannerREF = 17 --Loai banner CHI PHI cua sanpham chinh
		
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd 
	    WHERE hd.TrangThaiHopDong <> 3
	    AND hd.SoHopDong = @SoHopDong
	 ) D on D.HopDongID = C.HopDongFK
	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF 	
	AND ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi_SanPhamChinh(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID),0) >0
	AND C.SoLuong >0	 
	) TD
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END 
SELECT '1'
END

```
