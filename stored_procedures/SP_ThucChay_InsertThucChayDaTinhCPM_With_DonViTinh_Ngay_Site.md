# Stored Procedure: `ThucChay_InsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-02-22 11:12:52.280000
- **Ngày sửa cuối**: 2019-09-03 09:58:08.323000

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


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site] 
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
	
	PRINT N'Thuc hien insert du lieu thuc chay'
		
	INSERT INTO dbo.ThucChayDaTinh
	(
		ThucChayDaTinhID,
		HopDongID,
		SoHopDong,
		DmMaHopDongREF,
		TenMaHopDong,
		NgayDanhSoHopDong,
		NgayKyHopDong,
		NhanHopDong,
		NgayNhanBanFax,
		NgayNhanHopDongBanCung,
		NgayChuyenHopDongChoKeToan,
		So,
		Thang,
		Nam,
		GiaTriHopDong,
		CongNo,
		HopDongChiTietREF,
		DangSuDung,
		IsGiayPhep,
		TrangThaiHopDong,
		IsBanCung,
		DmPhongBanREF,
		TenPhongBan,
		DmBoPhanREF,
		TenBoPhan,
		DmNhomLamViecREF,
		TenNhomLamViec,
		DmDiaDiemLamViecREF,
		TenDiaDiemLamViec,
		SysNhanVienREF,
		TenDangNhap,
		TenNhanVien,
		TenKhachHang,
		NhanHang,
		DmNhomNganhREF,
		TenNhomNganh,
		DmHinhThucQuangCao,
		TenHinhThucQuangCao,
		DmSanPhamREF,
		TenSanPham,
		DmNhomWebsiteREF,
		TenNhomWebsite,
		DmChuyenMucREF,
		TenChuyenMuc,
		DmLoaiBannerREF,
		TenLoaiBanner,
		DmViTriREF,
		TenViTri,
		DotChayHopDong,
		SoLuongDotChayHD,
		DotChayBooking,
		SoLuongDotChayBooking,
		SoLuong,
		DonViTinh,
		DonGia,
		DonGiaTheoDonVi,
		ChietKhau,
		GiamGia,
		ThanhTien,
		TiLeTuVan,
		ChiPhiTuVan,
		IsKhuyenMai,
		KhuyenMai,
		DmBannerREF,
		DmChienDichREF,
		DmWebsiteREF,
		TenWebsite,
		TongViewThucChay,
		TongClickThucChay,
		TongSoBaiViet,
		SoLuongThucChay,
		NgayThucHien,
		GiaTriThayDoi,
		ThanhTienThucChayTruocTrietKhau,
		GiaTriTrietKhauThucChay,
		ThanhTienSauTrietKhauThucChay,
		GiaTriHoaHongThucChay,
		ThanhTienThucThu,
		ThanhTienKM,
		SoLuongThucChayKM,
		SoLuongThucChayLechTreoHa,
		ThanhTienLechTreoHa,
		CreatedAt,
		LastModifiedAt,
		IsPheDuyet,
		PheDuyetBy,
		PheDuyetAt,
		SoLuongThayDoi,
		SoLuongKMThayDoi,
		GiaTriKMThayDoi,
		GhiChu
	)

	SELECT  NEWID(), TD.*, 
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
	ISNULL((((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	(CASE when TD.IsKhuyenMai=1 then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) as ThanhTienKM,
	(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))) then ISNULL(TD.TongViewThucChay,0)
		else 0
	  END
	) as SoLuongThucChayKM,
	[dbo].[fn_TinhSoLuongThucChayLechTreoHaCPM_With_DonViTinh_Ngay](TD.HopDongChiTietREF,	@NgayThucHien,TD.SoLuongDotChayHD,@TiLeBannerSiteHDCT,TD.ThanhTien,	TD.ChietKhau , TD.TongViewThucChay)	AS SoLuongLechTreoHa,
	[dbo].[fn_TinhTienThucChayLechTreoHaCPM_With_DonViTinh_Ngay] (TD.HopDongChiTietREF,	@NgayThucHien,TD.SoLuongDotChayHD,@TiLeBannerSiteHDCT,TD.ThanhTien,	TD.ChietKhau ) AS ThanhTienLechTreoHa,
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
		(SELECT TOP (1) DmNhanHangREF FROM dbo.ThucChayHopDongChiTiet WHERE HopDongChiTietREF = @HopDongChiTietID AND CONVERT(NVARCHAR(50),DmBannerREF) = @DmBannerREF ORDER BY HopDongChiTietREF ) NhanHang,
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
		CASE WHEN @TongViewThucChayBanner <> 0 AND C.DonViTinhREF = 3 THEN C.DonGia/@TongViewThucChayBanner 
			WHEN @TongViewThucChayBanner <> 0 AND c.DonViTinhREF = 4 THEN (C.DonGia/7)/@TongViewThucChayBanner
		ELSE 0
		END AS DonGiaTheoDonViTinh,
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
