# Stored Procedure: `ThucChay_InsertThucTreoThayDoi_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:19.030000
- **Ngày sửa cuối**: 2017-06-07 10:10:23.723000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTiet` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucTreoThayDoi_ChiPhiKhac]


CREATE PROCEDURE [dbo].[ThucChay_InsertThucTreoThayDoi_ChiPhiKhac] 
	@HopDongChiTiet INT,
	@NgaythucHien DATETIME,
	@GiaTriThayDoi FLOAT
AS
BEGIN
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
	--C.NhanHang, 
	[dbo].[f_ReturnListConcatNhanHangREF_v2] 
	(
		C.HopDongChiTietID,
		@NgaythucHien
	)NhanHang,
	C.DmNhomNganhREF, 
	C.TenNhomNganh, 
	--Thong tin hinh thuc quang cao
	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
	--Thong tin San pham
	c.DmSanPhamREF as DmSanPhamREF,
	C.TenSanPham,  
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
	'CPK_TTR' DotChayHopDong,
	0 AS SoLuongDotChayHD,
	'PS THUC TREO CPK' DotChayBooking,
	0 AS SoLuongDotChayBooking, 
	--Thong tin ve Tien
	ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuong, 
	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
	--ISNULL(dbo.ThucChay_GetDonGiaThucTreo_PR(D.NgayKyHopDong, @NgayThucHien, C.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
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
	0 SoLuongThucChay,
	--Thanhuc Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	@GiaTriThayDoi as GiaTriThayDoi,
	0 as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT * FROM HopDongChiTiet WHERE DmSanPhamREF in 
						(--NHOM SP Chi phí--	
							242 -- Luot up	
							,241 -- Tin Vip	
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
							, 635 -- Quản trị fanpage
							, 563  -- Forum Seeding	
							,631 -- facebook seeding
							,651 -- đăng tin fanpage
							,726 --Tư vấn viết đề án truyền thông
							,731 --KOL
							,730 --- Livestream
							,633
							,629
							,729
							,736 -- Chi phí công nghệ
						)
		AND HopDongChiTietID = @HopDongChiTiet
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd 
	    WHERE hd.TrangThaiHopDong != 3
	 ) D on D.HopDongID = C.HopDongFK
--	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
	) TD

END

--EXEC [ThucChay_InsertThucChayDaTinh_ChiPhiKhac] '2013-07-01','2013-07-11'



```
