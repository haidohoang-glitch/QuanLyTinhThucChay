# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiCPM_With_DonViTinh_Ngay_Site_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-08 10:33:16.550000
- **Ngày sửa cuối**: 2021-07-08 10:33:16.550000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@TiLeBannerSiteHDCT` | `float(8)` | No |
| `@TongViewThucChayBanner` | `bigint(8)` | No |
| `@TongClickThucChayBanner` | `bigint(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]


CREATE  PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiCPM_With_DonViTinh_Ngay_Site_dev] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@TypeProduct INT,
	@DmWebsiteREF INT, 
	@TenWebsite NVARCHAR(50),
	@DmBannerREF INT,
	@TiLeBannerSiteHDCT FLOAT,
	@TongViewThucChayBanner BIGINT, 
	@TongClickThucChayBanner BIGINT
AS
BEGIN
	
	PRINT N'Thuc hien update gia tri du lieu thuc chay thay doi'
		
	--INSERT INTO dbo.ThucChayDaTinh
	--(
	--	ThucChayDaTinhID,
	--	HopDongID,
	--	SoHopDong,
	--	DmMaHopDongREF,
	--	TenMaHopDong,
	--	NgayDanhSoHopDong,
	--	NgayKyHopDong,
	--	NhanHopDong,
	--	NgayNhanBanFax,
	--	NgayNhanHopDongBanCung,
	--	NgayChuyenHopDongChoKeToan,
	--	So,
	--	Thang,
	--	Nam,
	--	GiaTriHopDong,
	--	CongNo,
	--	HopDongChiTietREF,
	--	DangSuDung,
	--	IsGiayPhep,
	--	TrangThaiHopDong,
	--	IsBanCung,
	--	DmPhongBanREF,
	--	TenPhongBan,
	--	DmBoPhanREF,
	--	TenBoPhan,
	--	DmNhomLamViecREF,
	--	TenNhomLamViec,
	--	DmDiaDiemLamViecREF,
	--	TenDiaDiemLamViec,
	--	SysNhanVienREF,
	--	TenDangNhap,
	--	TenNhanVien,
	--	TenKhachHang,
	--	NhanHang,
	--	DmNhomNganhREF,
	--	TenNhomNganh,
	--	DmHinhThucQuangCao,
	--	TenHinhThucQuangCao,
	--	DmSanPhamREF,
	--	TenSanPham,
	--	DmNhomWebsiteREF,
	--	TenNhomWebsite,
	--	DmChuyenMucREF,
	--	TenChuyenMuc,
	--	DmLoaiBannerREF,
	--	TenLoaiBanner,
	--	DmViTriREF,
	--	TenViTri,
	--	DotChayHopDong,
	--	SoLuongDotChayHD,
	--	DotChayBooking,
	--	SoLuongDotChayBooking,
	--	SoLuong,
	--	DonViTinh,
	--	DonGia,
	--	DonGiaTheoDonVi,
	--	ChietKhau,
	--	GiamGia,
	--	ThanhTien,
	--	TiLeTuVan,
	--	ChiPhiTuVan,
	--	IsKhuyenMai,
	--	KhuyenMai,
	--	DmBannerREF,
	--	DmChienDichREF,
	--	DmWebsiteREF,
	--	TenWebsite,
	--	TongViewThucChay,
	--	TongClickThucChay,
	--	TongSoBaiViet,
	--	SoLuongThucChay,
	--	NgayThucHien,
	--	GiaTriThayDoi,
	--	ThanhTienThucChayTruocTrietKhau,
	--	GiaTriTrietKhauThucChay,
	--	ThanhTienSauTrietKhauThucChay,
	--	GiaTriHoaHongThucChay,
	--	ThanhTienThucThu,
	--	ThanhTienKM,
	--	SoLuongThucChayKM,
	--	SoLuongThucChayLechTreoHa,
	--	ThanhTienLechTreoHa,
	--	CreatedAt,
	--	LastModifiedAt,
	--	IsPheDuyet,
	--	PheDuyetBy,
	--	PheDuyetAt,
	--	SoLuongThayDoi,
	--	SoLuongKMThayDoi,
	--	GiaTriKMThayDoi,
	--	GhiChu
	--)

	SELECT  NEWID() ThuChayDaTinhID, TD.HopDongID,
	--Thong tin ve ma so 
	TD.SoHopDong, 
	TD.DmMaHopDongREF, 
	TD.TenMaHopDong, 
	--Thong tin ve thoi gian
	TD.NgayDanhSoHopDong, TD.NgayKyHopDong, 
	TD.NhanHopDong, TD.NgayNhanBanFax, TD.NgayNhanHopDongBanCung, TD.NgayChuyenHopDongChoKeToan, 
	TD.So, TD.Thang, TD.Nam, 
	--Thong tin ve gia tri
	TD.GiaTriHopDong, TD.CongNo,
	--Thong tin chi tiet phan bo
	TD.HopDongChiTietREF,
	--Thong tin ve trang thai
	TD.DangSuDung, TD.IsGiayPhep, TD.TrangThaiHopDong,TD.IsBanCung, 
	--Thong tin ve Nhan vien kinh doanh
	TD.DmPhongBanREF, 
	TD.TenPhongBan, 
	TD.DmBoPhanREF, 
	TD.TenBoPhan, 
	TD.DmNhomLamViecREF, 
	TD.TenNhom, 
	TD.DmDiaDiemLamViecREF, 
	TD.TenDiaDiemLamViec, 
	TD.SysNhanVienREF, 
	TD.TenDangNhap,  
	TD.TenNhanVien, 
	TD.TenKhachHang, 
	TD.NhanHang,
	TD.DmNhomNganhREF, 
	TD.TenNhomNganh, 
	--Thong tin hinh thuc quang cao
	TD.DmHinhThucQuangCao, TD.TenHinhThucQuangCao, 
	--Thong tin San pham
	TD.DmSanPhamREF,
	TD.TenSanPham,  
	TD.DmNhomWebsiteREF, 
	TD.TenNhomWebsite, 
	TD.DmChuyenMucREF, 
	TD.TenChuyenMuc, 
	TD.DmLoaiBannerREF, 
	TD.TenLoaiBanner, 
	TD.DmBannerREF DmViTriREF, 
	TD.TenViTri, 
	TD.DotChayHopDong, --HAIDH COMMENT THONG TIN PHAN BIET CHAY CPM THEO NGAY
	TD.DonGia AS SoLuongDotChayHD,
	TD.DotChayBooking, --THONG TIN PHAN BIET CHAY CPM THEO NGAY VA CO THONG TIN SITE
	TD.SoLuongDotChayBooking, 
	TD.SoLuong,
	TD.DonViTinh, 
	TD.DonGia,
	TD.DonGiaTheoDonViTinh,
	TD.ChietKhau, TD.GiamGia, TD.ThanhTien,
	TD.TiLeTuVan,  TD.ChiPhiTuVan,
	TD.IsKhuyenMai,  
	TD.KhuyenMai,
	TD.DmBannerREF,--A.DmBannerREF,
	TD.DmChienDichREF,--A.DmChienDichREF,
	TD.DmWebsiteREF,
	TD.TenWebsite,
	TD.TongViewThucChay,
	TD.TongClickThucChay,
	TD.TongSoBaiViet,
	0 SoLuongThucChay,
	TD.NgayThucHien,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) GiaTriThayDoi,
	0 ThanhTienThucChayTruocTrietKhau, 
	0 AS GiaTriTrietKhauThucChay,
	0 AS ThanhTienSauTrietKhauThucChay,
	0 AS GiaTriHoaHongThucChay,
	0 AS ThanhTienThucThu,
	0 as ThanhTienKM,
	0 as SoLuongThucChayKM,
	0 AS SoLuongLechTreoHa,
	0 AS ThanhTienLechTreoHa,
	GETDATE(),
	GETDATE(),
	0 IsPheDuyet,
	'' PheDuyetBy,
	'' PheDuyetAt,
	TD.SoLuongThucChay SoLuongThayDoi,
	(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))) then ISNULL(TD.TongViewThucChay,0)
		else 0
	  END
	) SoLuongKMThayDoi,
	(CASE when TD.IsKhuyenMai=1 then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) GiaTriKMThayDoi,
	N'Thuc hien update gia tri du lieu thuc chay thay doi' GhiChu	
	FROM 
	(	SELECT 
		--ID Hop Dong
		D.HopDongID,
		--Thong tin ve ma so 
		D.SoHopDong, 
		D.DmMaHopDongREF, 
		D.TenMaHopDong, 
		--Thong tin ve thoi gian
		D.NgayDanhSoHopDong, D.NgayKyHopDong, 
		D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
		D.So, D.Thang, D.Nam, 
		--Thong tin ve gia tri
		D.GiaTriHopDong, D.CongNo,
		--Thong tin chi tiet phan bo
		@HopDongChiTietID HopDongChiTietREF,
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
		D.TenKhachHang, 
		(SELECT TOP (1) DmNhanHangREF FROM dbo.ThucChayHopDongChiTiet 
		WHERE HopDongChiTietREF = @HopDongChiTietID AND CONVERT(NVARCHAR(50),DmBannerREF) = @DmBannerREF ORDER BY HopDongChiTietREF ) NhanHang,
		C.DmNhomNganhREF, 
		C.TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		dbo.GetProductIDByTypeProduct(@TypeProduct) AS DmSanPhamREF,
		dbo.GetProductNameByTypeProduct(@TypeProduct) AS TenSanPham,  
		C.DmNhomWebsiteREF, 
		C.TenNhomWebsite, 
		C.DmChuyenMucREF, 
		C.TenChuyenMuc, 
		C.DmLoaiBannerREF, 
		C.TenLoaiBanner, 
		C.DmBannerREF DmViTriREF, 
		C.TenViTri, 
		N'NGAY' DotChayHopDong, --HAIDH COMMENT THONG TIN PHAN BIET CHAY CPM THEO NGAY
		C.DonGia AS SoLuongDotChayHD,
		@TenWebsite DotChayBooking, --THONG TIN PHAN BIET CHAY CPM THEO NGAY VA CO THONG TIN SITE
		@DmWebsiteREF SoLuongDotChayBooking, 
		C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
		N'VIEW' AS DonViTinh, 
		C.DonGia AS DonGia,
		(CASE WHEN @TongViewThucChayBanner <> 0 THEN C.DonGia/@TongViewThucChayBanner 
			ELSE 0
			END	)AS DonGiaTheoDonViTinh,
		C.ChietKhau, C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		@DmBannerREF DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		@DmWebsiteREF DmWebsiteREF,
		@TenWebsite TenWebsite,
		@TongViewThucChayBanner TongViewThucChay,
		@TongClickThucChayBanner TongClickThucChay,
		0 TongSoBaiViet,
		(CASE WHEN C.ChietKhau = 100 THEN 0
			ELSE [dbo].[fn_TinhSoLuongThucChayCPM_With_DonViTinh_Ngay] (
																			@HopDongChiTietID,
																			@NgayThucHien,
																			C.DonGia,
																			@TiLeBannerSiteHDCT,
																			C.ThanhTien,
																			C.ChietKhau ,
																			@TongViewThucChayBanner
																		)
		END 
		) AS SoLuongThucChay,
		@NgayThucHien NgayThucHien,
		0 AS GiaTriThayDoi,
		[dbo].[fn_TinhTienThucChayCPM_With_DonViTinh_Ngay] (
															@HopDongChiTietID,
															@NgayThucHien,
															C.DonGia,
															@TiLeBannerSiteHDCT ,
															C.ThanhTien,
															C.ChietKhau 
		) AS ThanhTienThucChayTruocTrietKhau

		FROM
		(SELECT * FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID) C INNER JOIN  
		(SELECT * FROM dbo.HopDong WHERE SoHopDong = @SoHopDong AND TrangThaiHopDong <> 3) D on D.HopDongID = C.HopDongFK
	 	
	) TD
	
END

```
