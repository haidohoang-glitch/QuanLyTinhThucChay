# Stored Procedure: `ThucChay_InsertGTTDThucChayDaTinhAdmarket_With_HopDong_Admarket_ThangDuGP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-09-07 10:58:53.380000
- **Ngày sửa cuối**: 2026-03-06 17:37:08.300000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChay_PerformanceBase_ThayDoi_ID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Tk` | `nvarchar(100)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@TienThucChay_GhiNhan` | `float(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@ThucChayDaTinhID_output` | `nvarchar(100)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*

*/
CREATE PROCEDURE [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_With_HopDong_Admarket_ThangDuGP]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@ThucChay_PerformanceBase_ThayDoi_ID INT,
	@HopDongID INT,
	@HopDongChiTietID INT, 
	@DmSanPhamREF INT, 
	@Tk NVARCHAR(50),
	@DmViTriREF INT,
	@TenViTri NVARCHAR(100),
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(200),
	@TienThucChay_GhiNhan FLOAT, 
	@GhiChu nvarchar(200),
	@ThucChayDaTinhID_output NVARCHAR(50) OUTPUT
AS
BEGIN
	 DECLARE @SoLuongThayDoi INT = 1, @DonViTinh NVARCHAR(100), @SoLuongThucChay INT = 1, @TenSanPham NVARCHAR(200)=''
	  , @DanhSachNhanHangREF NVARCHAR(200) = ''
	  , @GhiChu_TienThayDoi NVARCHAR(500) = N''
	  , @DmChienDichREF INT = 3 --Thang Du Giai Phap
	  , @V_ChietKhau float = 0
	SET @DonViTinh = 'GÓI'
	SET @TenSanPham =''
	SET @GhiChu_TienThayDoi = N'ThangDuGP, Tk:' +@Tk + ', HDCT: ' + Convert(nvarchar(100),@HopDongChiTietID) + ', ThucChay_ThayDoi_ID: '+ Convert(NVARCHAR(100),@ThucChay_PerformanceBase_ThayDoi_ID)

	DECLARE @Table_thucchaydatinh_id table(
	ThucChayDaTinhID NVARCHAR(50),
	HopDongREF INT
	)

	SELECT TOP 1 @DanhSachNhanHangREF = DanhSachNhanHangREF, @TenSanPham = TenSanPham 
	FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID

	SET @V_ChietKhau = 
	( SELECT A.ChietKhau FROM 
		(
			SELECT 
			hdl.ChietKhau,
			hdl.CreatedAt,
			-- Đánh số thứ tự riêng biệt cho từng SoHopDong
			ROW_NUMBER() OVER (
				PARTITION BY hdl.HopDongChiTietREF
				ORDER BY hdl.CreatedAt desc, HopDongChiTietLogID desc
			) AS OrderHopDongChiTietLog
			FROM dbo.HopDongChiTietLog hdl
			where hdl.HopDongChiTietREF = @HopDongChiTietID
			and hdl.ChietKhau <> 100
		) A WHERE A.OrderHopDongChiTietLog = 1
	)

	SET @V_ChietKhau = ISNULL(@V_ChietKhau,0)

	------TANG GIA TRI THANG DU GIAI PHAP-------
	--1. Ghi nhận vào table ThucchayDatinh_Admarket
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

	OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.HopDongID INTO @Table_thucchaydatinh_id

	SELECT 
		NEWID() thucchaydatinhid,
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
		C.HopDongChiTietID,
		--Thong tin ve trang thai
		D.DangSuDung, D.IsGiayPhep, 2 TrangThaiHopDong,D.IsBanCung, 
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
		C.DanhSachNhanHangREF NhanHang, 
		C.DmNhomNganhREF, 
		C.TenNhomNganh, 
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		c.DmSanPhamREF as DmSanPhamREF,
		C.TenSanPham,  
		C.DmNhomWebsiteREF, 
		C.TenNhomWebsite, 
		C.DmChuyenMucREF, 
		C.TenChuyenMuc,
		C.DmLoaiBannerREF, 
		C.TenLoaiBanner, 
		@DmViTriREF DmViTriREF, 
		@TenViTri TenViTri, 
		@Tk DotChayHopDong,
		0 AS SoLuongDotChayHD,
		@ThucChay_PerformanceBase_ThayDoi_ID DotChayBooking,
		@ThucChay_PerformanceBase_ThayDoi_ID AS SoLuongDotChayBooking, 
		C.SoLuong AS SoLuong, 
		@DonViTinh as DonViTinh, 
		C.DonGia as DonGia, 
		C.DonGia AS DonGiaTheoDonViTinh,
		--C.ChietKhau, 
		@V_ChietKhau AS ChietKhau,
		C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		0 DmBannerREF,
		@DmChienDichREF DmChienDichREF,
		@DmWebsiteREF DmWebsiteREF,
		@TenWebsite TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		@SoLuongThucChay SoLuongThucChay,
		@NgayThucHien AS NgayThucHien,
		0 as GiaTriThayDoi,	 
		0 as ThanhTienThucChayTruocTrietKhau,
		0 AS GiaTriTrietKhauThucChay,
		@TienThucChay_GhiNhan AS ThanhTienSauTrietKhauThucChay,	
		0 AS GiaTriHoaHongThucChay,
		@TienThucChay_GhiNhan AS ThanhTienThucThu,
		0 ThanhTienKM,
		0 as SoLuongThucChayKM,
		0 SoLuongLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() createdat,
		GETDATE() lastmodifiedat,
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		@GhiChu_TienThayDoi GhiChu	
	
		FROM 
		(
			SELECT * FROM dbo.HopDongChiTiet 
				WHERE HopDongChiTietID = @HopDongChiTietID
							AND DmSanPhamREF = @DmSanPhamREF
							--AND TK_AdMarket = @Tk
					AND RecordStatus = 0
		) C  
		INNER JOIN  
		 ( 
	 		SELECT * FROM dbo.HopDong hd 
	 		WHERE 1=1-- hd.TrangThaiHopDong <> 3	    
			   AND hd.HopDongID = @HopDongID
			   AND hd.DeletedStatus = 0
		 ) D on D.HopDongID = C.HopDongFK

	SELECT top (1) @ThucChayDaTinhID_output = ISNULL(ThucChayDaTinhID,'') FROM @Table_thucchaydatinh_id 

	IF(@ThucChayDaTinhID_output <> '')
	 BEGIN
		--2. Ghi nhận vào table ThucChayDaTinh (thông tin ghi nhận giống ThucChayDaTinh_admarket)
		IF(@DmSanPhamREF IN  (144,585,628))
		BEGIN
			INSERT INTO dbo.ThucChayDaTinhAdmarket
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
	

			SELECT 
			NEWID() thucchaydatinhid,
			--ID Hop Dong
			D.HopDongID,
			--Thong tin ve ma so 
			D.SoHopDong, 
			D.DmMaHopDongREF, 
			D.TenMaHopDong, 
			--Thong tin ve thoi gian
			D.NgayDanhSoHopDong, D.NgayKyHopDong, 
			D.DmNhanGocREF AS NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
			D.So, D.Thang, D.Nam, 
			--Thong tin ve gia tri
			D.GiaTriHopDong, D.CongNo,
			--Thong tin chi tiet phan bo
			C.HopDongChiTietID,
			--Thong tin ve trang thai
			D.DangSuDung, D.IsGiayPhep, 2 TrangThaiHopDong,D.IsBanCung, 
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
			C.DanhSachNhanHangREF NhanHang, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			c.DmSanPhamREF as DmSanPhamREF,
			C.TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			@DmViTriREF DmViTriREF, 
			@TenViTri TenViTri, 
			@Tk DotChayHopDong,
			0 AS SoLuongDotChayHD,
			@ThucChay_PerformanceBase_ThayDoi_ID DotChayBooking,
			@ThucChay_PerformanceBase_ThayDoi_ID AS SoLuongDotChayBooking, 
			C.SoLuong AS SoLuong, 
			@DonViTinh as DonViTinh, 
			C.DonGia as DonGia, 
			C.DonGia AS DonGiaTheoDonViTinh,
			--C.ChietKhau,
			@V_ChietKhau AS ChietKhau,
			C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			0 DmBannerREF,
			@DmChienDichREF AS DmChienDichREF,
			@DmWebsiteREF DmWebsiteREF,
			@TenWebsite TenWebsite,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			@SoLuongThucChay SoLuongThucChay,
			@NgayThucHien AS NgayThucHien,
			0 as GiaTriThayDoi,	 
			0 as ThanhTienThucChayTruocTrietKhau,
			0 AS GiaTriTrietKhauThucChay,
			@TienThucChay_GhiNhan AS ThanhTienSauTrietKhauThucChay,	
			0 AS GiaTriHoaHongThucChay,
			@TienThucChay_GhiNhan AS ThanhTienThucThu,
			0 ThanhTienKM,
			0 as SoLuongThucChayKM,
			0 SoLuongLechTreoHa,
			0 ThanhTienLechTreoHa,
			GETDATE() createdat,
			GETDATE() lastmodifiedat,
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			0 SoLuongThayDoi,
			0 SoLuongKMThayDoi,
			0 GiaTriKMThayDoi,
			@GhiChu_TienThayDoi GhiChu	
	
			FROM 
			(
				SELECT * FROM dbo.HopDongChiTiet 
					WHERE HopDongChiTietID = @HopDongChiTietID
								AND DmSanPhamREF = @DmSanPhamREF
								AND TK_AdMarket = @Tk
						AND RecordStatus = 0
			) C  
			INNER JOIN  
			 ( 
	 			SELECT * FROM dbo.HopDong hd 
	 			WHERE 1=1-- hd.TrangThaiHopDong <> 3	    
				   AND hd.HopDongID = @HopDongID
				   AND hd.DeletedStatus = 0
			 ) D on D.HopDongID = C.HopDongFK
		END
		--3. Ghi nhận vào table ThucChayDaTinh_muaNgoai
		INSERT INTO [dbo].[ThucChayDaTinh_MuaNgoai]
           ([HopDongREF]										-- HD
           ,[SoHopDong]											-- HD
           ,[DmMaHopDongREF]									-- HD
           ,[NgayDanhSoHopDong]								    -- HD
           ,[TrangThaiHopDong]									-- HD
           ,[DmNhanVienREF]										-- HD
           ,[TenDangNhap]										-- HD
           ,[DmPhongBanREF]										-- HD
           ,[DmBoPhanREF]										-- HD
           ,[DmNhomLamViecREF]									-- HD
           ,[DmDiaDiemLamViecREF]								-- HD
           ,[DmKhachHangREF]									-- HD
           ,[HopDongChiTietREF]									-- HDCT
           ,[LstDmNhanHangREF]									-- HDCT
           ,[LstDmNhomNganhREF]									-- HDCT
           ,[DmHinhThucQuangCaoREF]								-- HDCT
           ,[DmSanPhamREF]										-- HDCT
           ,[DmChuyenMucREF]									-- HDCT
           ,[DmLoaiBannerREF]									-- HDCT
           ,[DmViTriREF]										-- HDCT
           ,[SoLuong]											-- HDCT
           ,[DonViTinhREF]										-- HĐCT
           ,[DonGia]											-- HDCT
           ,[ChietKhau]											-- HDCT
           ,[ThanhTien]											-- HDCT
           ,[IsKhuyenMai]										-- HDCT
           ,[KhuyenMai]											-- HDCT
           ,[ThucChayMuaNgoaiChiTietREF]						-- HDCT
		   ,[TongTienDuToanMuaSauCK]							-- HDCT
		   ,[TongTienDuToanLaiMuaSauCK]							-- HDCT
           ,[ChietKhauMua]										-- 0
           ,[DmBannerREF]										-- HDCT
           ,[DmChienDichREF]									-- 0
           ,[DmWebsiteREF]										-- HDCT
           ,[TenWebsite]										-- HDCT
           ,[NgayThucHien]										-- @Ngaythuchien
           ,[NgayBatDau]										-- THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
           ,[NgayKetThuc]										
           ,[DonViTinhThucChay]									-- TC
           ,[DonGiaTheoDonViTinhTC]								-- TC
           ,[TongViewClickThucChay]								-- 0
           ,[TongSoBaiVietChiPhiThucChay]					    -- 0
           ,[SoLuongThucChay]									-- TC
           ,[TongThanhTienThucChayBanSauCK]						-- TC, CK
           ,[TongThanhTienThucChayMuaSauCK]                     -- TC
           ,[ThanhTienLaiThucChaySauCK]							-- TC bán - mua
           ,[ThanhTienLaiThucChayKM]							-- TC lãi của HDCT khuyến mại
           ,[SoLuongThucChayKM]									-- Số lượng TC của HDCT khuyến mại
           ,[SoLuongThucChayLechTreoHa]                         -- số lượng vượt phân bổ
           ,[ThanhTienLechTreoHa]								-- thành tiền vượt phân bổ
           ,[GiaTriThayDoiLaiSauCK]								-- 0
           ,[SoLuongThayDoi]									-- 0	
           ,[SoLuongKMThayDoi]									-- 0
           ,[GiaTriKMLaiThayDoi]								-- 0
           ,[GhiChu]											-- GhiChu
           ,[CreatedAt]											-- GETDATE()
           ,[LastModifiedAt])									-- GETDATE()


    SELECT
			[HopDongREF] = @HopDongID   
           ,[SoHopDong] = HD.[SoHopDong]  
           ,[DmMaHopDongREF]  = HD.[DmMaHopDongREF] 
           ,[NgayDanhSoHopDong] = HD.[NgayDanhSoHopDong]    
           ,[TrangThaiHopDong] = 2  
           ,[DmNhanVienREF] = HD.SysNhanVienREF     
           ,[TenDangNhap] = HD.[TenDangNhap]    
           ,[DmPhongBanREF] = HD.[DmPhongBanREF]    
           ,[DmBoPhanREF] = HD.[DmBoPhanREF]   
           ,[DmNhomLamViecREF] = HD.[DmNhomLamViecREF]      
           ,[DmDiaDiemLamViecREF] = HD.[DmDiaDiemLamViecREF]    
           ,[DmKhachHangREF]  = HD.[DmKhachHangREF]    
           ,[HopDongChiTietREF]  = @HopDongChiTietID     
           ,[LstDmNhanHangREF] = HDCT.DanhSachNhanHangREF  
           ,[LstDmNhomNganhREF] = HDCT.DmNhomNganhREF   
           ,[DmHinhThucQuangCaoREF] = HDCT.DmLoaiREF   
           ,[DmSanPhamREF] = HDCT.DmSanPhamREF   
           ,[DmChuyenMucREF] =  HDCT.[DmChuyenMucREF]   
           ,[DmLoaiBannerREF] =  HDCT.[DmLoaiBannerREF]    
           ,[DmViTriREF]  =  HDCT.[DmViTriREF]   
           ,[SoLuong] =  HDCT.[SoLuong]     
           ,[DonViTinhREF]  =  HDCT.[DonViTinhREF]     
           ,[DonGia]  =  HDCT.[DonGia]     
           ,[ChietKhau]   =  @V_ChietKhau -- HDCT.[ChietKhau]  
           ,[ThanhTien]  =  HDCT.[ThanhTien]   
           ,[IsKhuyenMai]  =  HDCT.[IsKhuyenMai]    
           ,[KhuyenMai]  =  HDCT.[KhuyenMai]    
           ,[ThucChayMuaNgoaiChiTietREF] = @ThucChay_PerformanceBase_ThayDoi_ID   
		   ,[TongTienDuToanMuaSauCK] = 0  
		   ,[TongTienDuToanLaiMuaSauCK] = 0 
           ,[ChietKhauMua] = 0    
           ,[DmBannerREF] = HDCT.DmBannerREF   
           ,[DmChienDichREF] =  @DmChienDichREF
           ,[DmWebsiteREF] = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(HDCT.DmWebsiteREF) 				
		   ,[TenWebsite] = dbo.GetWebsiteLinkByDmWebsiteID(HDCT.DmWebsiteREF,HDCT.TenWebsite) 
           ,[NgayThucHien] = @Ngaythuchien
           ,[NgayBatDau] = NULL --THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
           ,[NgayKetThuc] = NULL---THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
           ,[DonViTinhThucChay] = @DonViTinh
           ,[DonGiaTheoDonViTinhTC] = 0
           ,[TongViewClickThucChay] = 0 
           ,[TongSoBaiVietChiPhiThucChay] = 0 
           ,[SoLuongThucChay] = IIF ((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100), 0, @SoLuongThucChay)
           ,[TongThanhTienThucChayBanSauCK]  = 0
           ,[TongThanhTienThucChayMuaSauCK] = 0
           ,[ThanhTienLaiThucChaySauCK] =  IIF((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100) , 0, @TienThucChay_GhiNhan)
           ,[ThanhTienLaiThucChayKM] = IIF((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100), @TienThucChay_GhiNhan, 0)  -- thực chạy lãi của TH Khuyến mại 100%
           ,[SoLuongThucChayKM] = IIF((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100), @SoLuongThucChay, 0)
           ,[SoLuongThucChayLechTreoHa] = 0
           ,[ThanhTienLechTreoHa] = 0
           ,[GiaTriThayDoiLaiSauCK] = 0
           ,[SoLuongThayDoi] = 0
           ,[SoLuongKMThayDoi] = 0
           ,[GiaTriKMLaiThayDoi] = 0
           ,[GhiChu] = @GhiChu_TienThayDoi
           ,[CreatedAt] = GETDATE()
           ,[LastModifiedAt] = GETDATE()
		FROM 
		(	SELECT * 
			FROM dbo.HopDongChiTiet HDCT 
			WHERE  HDCT.HopDongChiTietID = @HopDongChiTietID
		)hdct 
		INNER JOIN 
		(	SELECT *
			FROM dbo.HopDong HD 
			WHERE HD.HopDongID = @HopDongID
		)hd ON HD.HopDongID = hdct.HopDongFK
	 END


END

```
