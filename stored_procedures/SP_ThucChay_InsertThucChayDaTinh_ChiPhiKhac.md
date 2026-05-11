# Stored Procedure: `ThucChay_InsertThucChayDaTinh_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:20.037000
- **Ngày sửa cuối**: 2019-01-29 15:33:26.787000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [ThucChay_InsertThucChayDaTinh_ChiPhiKhac] '2014-06-11 00:00:00.000','2014-06-11 15:42:55.690'
-------------------------------------------------------------
CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_ChiPhiKhac] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN

DECLARE @NgayThucHien DATETIME, @NgayGioiHanTinh DATETIME
set @NgayThucHien = Convert(date,@StartDate)
SET @NgayGioiHanTinh = '2013-01-01'



WHILE(@NgayThucHien <= @EndDate)
BEGIN	 
	DELETE FROM dbo.ThucChayDaTinh WHERE NgayThucHien = @NgayThucHien
	AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF IN (18))
	AND DmSanPhamREF IN (--- NHOM SP TMDT --------------
							  242 -- Luot up	
							  ,241 -- Tin vip											
						--NHOM SP Chi phí--
							, 251 --Thiết kế, quản lý
							, 252 --Hosting
							, 253 --Chi phi khac									
							, 535 --Chi phí quản lý campaign
							, 537 --Chi phí viết bài
							, 538 --Chi phí thiết kế
							, 539 --Chi phí dựng clip
							, 540 --Chi phí sáng tạo
							, 541 --Chi phí giải thưởng cuộc thi/ Contest
							, 542 --Chi phí xây dưng microsite/ tab
							, 555 --Chi phí trài trợ
							, 556 --Hiệu đính
							, 557 --Chèn Clip
							, 558 --Chi phí viết bài
							, 559 --Chi phí quay clip
							, 560 --Chi phí sản xuất										
							, 561 -- Chi phí khảo sát thị trường online
							--bo sung
							, 635 -- Quản trị fanpage
							, 563  -- Forum Seeding
							,631 -- Facebook Seeding
							, 651 -- Đăng tin fanpage
							,630 -- Chi phí tư vấn
							,726 --Tư vấn viết đề án truyền thông
							,731 --KOL
							,730 --Livestream
							,629 --Chi phí tổ chức
							,729 --Visual Content
							,633 --Mở fanpage
							,736 -- Chi phí công nghệ
							,734
							, 771, 772 ,775,792 , 805 , 806 , 817,5012
						) 	
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
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi(@NgayThucHien,@NgayGioiHanTinh ,TD.HopDongChiTietID),0)
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
	dbo.ThucChay_GetListThucTreoIDByHopDongChiTietREF
		(@NgayThucHien,@NgayGioiHanTinh,c.HopDongChiTietID) DotChayBooking,
	0 AS SoLuongDotChayBooking, 
	--Thong tin ve Tien
	isnull(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID),0) AS SoLuong,	
	isnull(C.DonViTinh, N'đ/v') as DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
	--ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
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
	(CASE when C.IsKhuyenMai=0 then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID),0)
		else 0
	  END
	) as SoLuongThucChay,
	--Thanhuc Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	0 as GiaTriThayDoi,
	ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID),0) * ISNULL(C.DonGia,0) as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT * FROM HopDongChiTiet 
			WHERE DmSanPhamREF in 
							(--- NHOM SP TMDT --------------
							  242 -- Luot up	
							  ,241 -- Tin vip											
							 --- NHOM SP Chi phí--
							, 251 --Thiết kế, quản lý
							, 252 --Hosting
							, 253 --Chi phi khac									
							, 535 --Chi phí quản lý campaign
							, 537 --Chi phí viết bài
							, 538 --Chi phí thiết kế
							, 539 --Chi phí dựng clip
							, 540 --Chi phí sáng tạo
							, 541 --Chi phí giải thưởng cuộc thi/ Contest
							, 542 --Chi phí xây dưng microsite/ tab
							, 555 --Chi phí trài trợ
							, 556 --Hiệu đính
							, 557 --Chèn Clip
							, 558 --Chi phí viết bài
							, 559 --Chi phí quay clip
							, 560 --Chi phí sản xuất										
							, 561 -- Chi phí khảo sát thị trường online
							--bo sung
							, 635 -- Quản trị fanpage
							, 563  -- Forum Seeding
							,631 -- Facebook Seeding
							, 651 -- Đăng tin fanpage
							,630 -- chi phí tư vấn
							,726 --Tư vấn viết đề án truyền thông
							,731 --KOL
							,730 --livestream
							,629 --Chi phí tổ chức
							,729 --Visual Content
							,633 --Mở fanpage
							,736 -- Chi phí công nghệ
						)
			AND DeletedStatus = 0 
			 AND NOT (DmLoaiREF = 13 or DmLoaiBannerREF = 18)	 --Khong tinh thuc chay cho HTQC Mua Ngoai
		
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd 
	    WHERE hd.TrangThaiHopDong <> 3
	    AND hd.DeletedStatus = 0
	      -- AND hd.SOHOPDONG IN ('QC2941013')
	 ) D on D.HopDongID = C.HopDongFK
	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF 	
	AND ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_ChiPhi(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID),0) >0
	AND C.SoLuong >0	 
	AND C.DmWebsiteREF NOT IN (307,285) -- loai tru website Google, Facebook
	) TD	
	EXEC [ThucChay_UpdateThucChayHopDongChiTiet_ChiPhiKhac] @NgayThucHien
	
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)
	END 
SELECT '1'
END


```
