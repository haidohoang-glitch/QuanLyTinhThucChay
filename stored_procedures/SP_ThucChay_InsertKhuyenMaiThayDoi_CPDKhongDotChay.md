# Stored Procedure: `ThucChay_InsertKhuyenMaiThayDoi_CPDKhongDotChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-08-21 16:10:26.620000
- **Ngày sửa cuối**: 2024-08-21 16:10:26.620000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@TongGiaTriThucChayDaTinhHT` | `float(8)` | No |
| `@SoLuongThucChayHT` | `float(8)` | No |
| `@GiatriKMHT` | `float(8)` | No |
| `@SoluongKMHT` | `float(8)` | No |

## Definition (Source Code)

```sql


CREATE  PROCEDURE [dbo].[ThucChay_InsertKhuyenMaiThayDoi_CPDKhongDotChay]   
	@HopDongChiTietID INT,@NgaythucHien DATETIME, 
	@TongGiaTriThucChayDaTinhHT FLOAT,
	@SoLuongThucChayHT FLOAT,
	@GiatriKMHT FLOAT, 
	@SoluongKMHT FLOAT
	
	
AS
BEGIN
	--1. Đối trừ
	INSERT INTO [dbo].[ThucChayDaTinh]
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
	SELECT NEWID() AS [ThucChayDaTinhID]
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
		  ,0 AS [SoLuongThucChay]
		  ,@NgayThucHien AS [NgayThucHien]
		  ,-SUM([ThanhTienSauTrietKhauThucChay] + [GiaTriThayDoi]) AS [GiaTriThayDoi]
		  ,-SUM([ThanhTienThucChayTruocTrietKhau]) AS [ThanhTienThucChayTruocTrietKhau]
		  ,-SUM([GiaTriTrietKhauThucChay]) AS [GiaTriTrietKhauThucChay]
		  ,0 AS [ThanhTienSauTrietKhauThucChay]
		  ,0 AS [GiaTriHoaHongThucChay]
		  ,0 AS [ThanhTienThucThu]
		  ,0 AS [ThanhTienKM]
		  ,0 AS [SoLuongThucChayKM]
		  ,0 AS [SoLuongThucChayLechTreoHa]
		  ,0 AS [ThanhTienLechTreoHa]
		  ,GETDATE() AS [CreatedAt]
		  ,GETDATE() AS [LastModifiedAt]
		  ,0 AS [IsPheDuyet]
		  ,'' AS [PheDuyetBy]
		  ,'' AS [PheDuyetAt]
		  ,-SUM([SoLuongThucChay] + [SoLuongThayDoi]) AS [SoLuongThayDoi]
		  ,-SUM([SoLuongThucChayKM] + [SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
		  ,-SUM([ThanhTienKM] + [GiaTriKMThayDoi]) AS [GiaTriKMThayDoi]
		  , N'Đối trừ do thay đổi khuyến mại SP:ThucChay_InsertKhuyenMaiThayDoi_CPDKhongDotChay' GhiChu	
	 FROM [dbo].[ThucChayDaTinh] tcdt
	 WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
				AND tcdt.NgayThucHien <= @NgayThucHien
	 GROUP BY
		   [HopDongID]
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
	  HAVING SUM([ThanhTienSauTrietKhauThucChay] + [GiaTriThayDoi]) <> 0
	  OR SUM([ThanhTienKM] + [GiaTriKMThayDoi]) <> 0

	--2. Tính lại
	IF ROUND(@TongGiaTriThucChayDaTinhHT, 0) != 0 OR @SoLuongThucChayHT != 0 OR 
	   ROUND(@GiatriKMHT, 0) != 0 OR  @SoluongKMHT != 0 
	BEGIN
		INSERT INTO dbo.ThucChayDaTinh 
		SELECT  NEWID(), TD.*, 
				ThanhTienThucChayTruocTrietKhau - ThanhTienThucChayTruocTrietKhau*TD.ChietKhau/100 as GiaTriTrietKhauThucChay,
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
				@SoLuongThucChayHT  SoLuongThayDoi,
				@SoluongKMHT	 SoLuongKMThayDoi,
				@GiatriKMHT  GiaTriKMThayDoi,
				 N'Tính lại do thay đổi chiết khấu SP:ThucChay_InsertKhuyenMaiThayDoi_CPDKhongDotChay' GhiChu	
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
			[dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID, @NgaythucHien)NhanHang,
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
			'CPD_KhongDotChay' DotChayHopDong,
			0 AS SoLuongDotChayHD,
			dbo.GetDotChayThucTreoByHopDongChiTiet(C.HopDongChiTietID,'Y') DotChayBooking,
			ISNULL([dbo].[GetSoLuongDotChayThucTreoByHopDongChiTiet](C.HopDongChiTietID),0) SoLuongDotChayBooking,
			--Thong tin ve Tien
			C.SoLuong AS SoLuong, 
			dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
			ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_CPDKhongDotChay(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			--dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
			dbo.[GetDmWebsiteReportingdbIDByDmWebsiteID_CPD](C.DmWebsiteREF) DmWebsiteREF,
			--dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			dbo.[GetWebsiteLinkByDmWebsiteID_CPD](C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			0 SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien AS NgayThucHien,
			@TongGiaTriThucChayDaTinhHT as GiaTriThayDoi,
			Case when C.ChietKhau = 100 
					then @GiatriKMHT 
					when isnull(C.ChietKhau, 0) <> 100 
					then @TongGiaTriThucChayDaTinhHT/(1-isnull(C.ChietKhau, 0)/100)
			end as ThanhTienThucChayTruocTrietKhau
		FROM 
		(
			SELECT * FROM HopDongChiTiet WHERE DmSanPhamREF in (140,228,564,549)
			AND HopDongChiTietID = @HopDongChiTietID
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

END




--EXEC [ThucChay_InsertThucTreoThayDoi_CPD] '2013-07-01','2013-07-11'

```
