# Stored Procedure: `ThucChayDaTinh_DoiTru_ThanhTien_CreatorContent_ByKetQuaVanHanhID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-25 16:34:46.770000
- **Ngày sửa cuối**: 2022-01-12 10:35:14.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@AppKetQuaVanHanh_CreatorContent_id` | `int(4)` | No |
| `@ghiChuDoiTru` | `nvarchar(1024)` | No |
| `@ThucChayDaTinhID_op` | `nvarchar(200)` | Yes |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayDaTinh_DoiTru_ThanhTien_CreatorContent_ByKetQuaVanHanhID]
	@NgayGhiNhanThucChay				DATETIME,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@AppKetQuaVanHanh_CreatorContent_id INT,
	@ghiChuDoiTru						NVARCHAR(512),
	@ThucChayDaTinhID_op				NVARCHAR(100) OUTPUT

AS
BEGIN
	DECLARE @NgayGioiHanTinh DATETIME  = '2020-01-01'
	, @NgayGioiHanTinh_HDCT DATETIME = '2020-01-01'
	, @Ghichu_DotChayHopDong NVARCHAR(200) = N'ThanhTien_CreatorContent'

	DECLARE @TABLE_OP TABLE(ThucChayDaTinhID NVARCHAR(100), AppKetQuaVanHanh_CreatorContent_id INT)

	INSERT INTO dbo.ThucChayDaTinh
	(
			ThucChayDaTinhID,										-- id bản ghi
			HopDongID,												-- HĐ
			SoHopDong,		   										-- HĐ
			DmMaHopDongREF,											-- HĐ
			TenMaHopDong,											-- HĐ		
			NgayDanhSoHopDong,										-- HĐ	
			NgayKyHopDong,											-- HĐ	
			NhanHopDong,											-- HĐ	
			NgayNhanBanFax,											-- HĐ	
			NgayNhanHopDongBanCung,									-- HĐ	
			NgayChuyenHopDongChoKeToan,								-- HĐ	
			So,														-- HĐ	
			Thang,													-- HĐ	
			Nam,													-- HĐ	
			GiaTriHopDong,											-- HĐ	
			CongNo,													-- HĐ	
			HopDongChiTietREF,										-- HĐ	
			DangSuDung,												-- HĐ	
			IsGiayPhep,												-- HĐ	
			TrangThaiHopDong,										-- Thay đổi	: 2
			IsBanCung,												-- HĐ	
			DmPhongBanREF,											-- HĐ	
			TenPhongBan,											-- HĐ	
			DmBoPhanREF,											-- HĐ
			TenBoPhan,												-- HĐ
			DmNhomLamViecREF,										-- HĐ
			TenNhomLamViec,											-- HĐ
			DmDiaDiemLamViecREF,									-- HĐ
			TenDiaDiemLamViec,										-- HĐ
			SysNhanVienREF,											-- HĐ
			TenDangNhap,											-- HĐ
			TenNhanVien,											-- HĐ
			TenKhachHang,											-- HĐ
			NhanHang,												-- HĐCT
			DmNhomNganhREF,											-- HĐCT
			TenNhomNganh,											-- HĐCT
			DmHinhThucQuangCao,										-- HĐCT
			TenHinhThucQuangCao,									-- HĐCT
			DmSanPhamREF,											-- HĐCT
			TenSanPham,												-- HĐCT
			DmNhomWebsiteREF,										-- HĐCT
			TenNhomWebsite,											-- HĐCT
			DmChuyenMucREF,											-- HĐCT
			TenChuyenMuc,											-- HĐCT
			DmLoaiBannerREF,										-- HĐCT
			TenLoaiBanner,											-- HĐCT
			DmViTriREF,												-- HĐCT
			TenViTri,												-- HĐCT
			DotChayHopDong,											-- ghi chú
			SoLuongDotChayHD,										-- 0      ??????????????????????
			DotChayBooking,											-- id thực chạy bán
			SoLuongDotChayBooking,									-- id thực chạy bán
			SoLuong,												-- HĐCT
			DonViTinh,												-- TC
			DonGia,													-- HĐCT
			DonGiaTheoDonVi,										-- HĐCT
			ChietKhau,												-- HĐCT
			GiamGia,												-- HĐCT
			ThanhTien,												-- HĐCT
			TiLeTuVan,												-- HĐCT
			ChiPhiTuVan,											-- HĐCT
			IsKhuyenMai,											-- HĐCT <=> chiết khấu = 100
			KhuyenMai,												-- HĐCT
			DmBannerREF,											-- HĐCT
			DmChienDichREF,											-- 0
			DmWebsiteREF,											-- HĐCT
			TenWebsite,											    -- HĐCT
			TongViewThucChay,									    -- 0
			TongClickThucChay,									    -- 0
			TongSoBaiViet,										    -- 0
			SoLuongThucChay,										-- TC:  nếu phân bổ khuyến mại  thì không ghi nhận => 0
			NgayThucHien,											-- @NgayThucHien
			GiaTriThayDoi,											-- 0
			ThanhTienThucChayTruocTrietKhau,						-- nếu phân bổ khuyến mai thì = ?????
			GiaTriTrietKhauThucChay,								-- nếu phân bổ khuyến mại thì = ????
			ThanhTienSauTrietKhauThucChay,							
			GiaTriHoaHongThucChay,									-- 0
			ThanhTienThucThu,										-- TCB Sau CK
			ThanhTienKM,											-- thành tiền TC của HĐKM , nếu phân bổ KM thì tính => TCBSCK              
			SoLuongThucChayKM,										-- SL TC của HĐKM , nếu phân bổ KM thì tính => SLTC 
			SoLuongThucChayLechTreoHa,								-- số lượng TC vượt hợp đồng
			ThanhTienLechTreoHa,									-- thành tiền thực chạy vượt hợp đồng
			CreatedAt,												-- GETDATE()
			LastModifiedAt,											-- GETDATE()
			IsPheDuyet,												-- ''
			PheDuyetBy,												-- ''
			PheDuyetAt,												-- ''
			SoLuongThayDoi,											-- 0
			SoLuongKMThayDoi,										-- 0
			GiaTriKMThayDoi,										-- 0
			GhiChu													-- @ghichu
		)

	
	OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.DotChayBooking INTO @TABLE_OP
	SELECT NEWID() AS ThucChayDaTinhID, 
			tcdt.HopDongID,														
			tcdt.SoHopDong,		   												
			tcdt.DmMaHopDongREF,														
			tcdt.TenMaHopDong,														
			tcdt.NgayDanhSoHopDong,														
			tcdt.NgayKyHopDong,														
			tcdt.NhanHopDong,														
			tcdt.NgayNhanBanFax,														
			tcdt.NgayNhanHopDongBanCung,														
			tcdt.NgayChuyenHopDongChoKeToan,														
			tcdt.So,														
			tcdt.Thang,														
			tcdt.Nam,														
			tcdt.GiaTriHopDong,														
			tcdt.CongNo,														
			tcdt.HopDongChiTietREF,														
			tcdt.DangSuDung,														
			tcdt.IsGiayPhep,														
			tcdt.TrangThaiHopDong,											
			tcdt.IsBanCung,														
			tcdt.DmPhongBanREF,														
			tcdt.TenPhongBan,														
			tcdt.DmBoPhanREF,														
			tcdt.TenBoPhan,														
			tcdt.DmNhomLamViecREF,														
			tcdt.TenNhomLamViec,														
			tcdt.DmDiaDiemLamViecREF,														
			tcdt.TenDiaDiemLamViec,														
			tcdt.SysNhanVienREF,														
			tcdt.TenDangNhap,														
			tcdt.TenNhanVien,														
			tcdt.TenKhachHang,														
			tcdt.NhanHang,														
			tcdt.DmNhomNganhREF,														
			tcdt.TenNhomNganh,														
			tcdt.DmHinhThucQuangCao,														
			tcdt.TenHinhThucQuangCao,														
			tcdt.DmSanPhamREF,														
			tcdt.TenSanPham,														
			tcdt.DmNhomWebsiteREF,														
			tcdt.TenNhomWebsite,														
			tcdt.DmChuyenMucREF,														
			tcdt.TenChuyenMuc,														
			tcdt.DmLoaiBannerREF,														
			tcdt.TenLoaiBanner,														
			tcdt.DmViTriREF,														
			tcdt.TenViTri,														
			tcdt.DotChayHopDong,														
			tcdt.SoLuongDotChayHD,										-- 0      ??????????????????????				
			tcdt.DotChayBooking,														
			tcdt.SoLuongDotChayBooking,														
			tcdt.SoLuong,														
			tcdt.DonViTinh,														
			tcdt.DonGia,														
			tcdt.DonGiaTheoDonVi,														
			tcdt.ChietKhau,														
			tcdt.GiamGia,														
			tcdt.ThanhTien,														
			tcdt.TiLeTuVan,														
			tcdt.ChiPhiTuVan,														
			tcdt.IsKhuyenMai,											-- HĐCT <=> chiết khấu = 100			
			tcdt.KhuyenMai,														
			tcdt.DmBannerREF,														
			tcdt.DmChienDichREF,											
			tcdt.DmWebsiteREF,														
			tcdt.TenWebsite,											    -- HĐCT			
			0 AS TongViewThucChay,									    -- 0					
			0 AS TongClickThucChay,									    -- 0					
			0 AS TongSoBaiViet,										    -- 0				
			0 AS SoLuongThucChay,										-- TC:  nếu phân bổ khuyến mại  thì không ghi nhận => 0				
			@NgayGhiNhanThucChay NgayThucHien,											-- @NgayThucHien			
			SUM(tcdt.GiaTriThayDoi	 + tcdt.ThanhTienSauTrietKhauThucChay)	AS GiaTriThayDoi,										
			0 AS ThanhTienThucChayTruocTrietKhau,						-- nếu phân bổ khuyến mai thì = ?????								
			0 AS GiaTriTrietKhauThucChay,								-- nếu phân bổ khuyến mại thì = ????						
			0 AS ThanhTienSauTrietKhauThucChay,														
			0 AS GiaTriHoaHongThucChay,												
			0 AS ThanhTienThucThu,														
			0 AS ThanhTienKM,											-- thành tiền TC của HĐKM , nếu phân bổ KM thì tính => TCBSCK              			
			0 AS SoLuongThucChayKM,										-- SL TC của HĐKM , nếu phân bổ KM thì tính => SLTC 				
			-SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa,														
			-SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa,														
			GETDATE() AS CreatedAt,														
			GETDATE() AS LastModifiedAt,														
			0 IsPheDuyet,												-- ''		
			'' PheDuyetBy,												-- ''		
			GETDATE() AS PheDuyetAt,												-- ''		
			SUM(tcdt.SoLuongThucChay  + tcdt.SoLuongThayDoi) AS SoLuongThayDoi,														
			SUM(tcdt.SoLuongKMThayDoi + tcdt.SoLuongThucChayKM) AS SoLuongKMThayDoi,													
			SUM(tcdt.GiaTriKMThayDoi + tcdt.ThanhTienKM) AS GiaTriKMThayDoi,													
			@ghiChuDoiTru AS GhiChu												-- @ghichu	
			FROM dbo.ThucChayDaTinh tcdt
			WHERE tcdt.HopDongID = @HopDongREF
			AND tcdt.HopDongChiTietREF = @HopDongChiTietREF
			AND tcdt.DotChayBooking = @AppKetQuaVanHanh_CreatorContent_id
			AND tcdt.NgayThucHien <= @NgayGhiNhanThucChay
			AND tcdt.NgayThucHien >= @NgayGioiHanTinh_HDCT
			AND tcdt.DotChayHopDong = @Ghichu_DotChayHopDong
			GROUP BY
			tcdt.HopDongID,														
			tcdt.SoHopDong,		   												
			tcdt.DmMaHopDongREF,														
			tcdt.TenMaHopDong,														
			tcdt.NgayDanhSoHopDong,														
			tcdt.NgayKyHopDong,														
			tcdt.NhanHopDong,														
			tcdt.NgayNhanBanFax,														
			tcdt.NgayNhanHopDongBanCung,														
			tcdt.NgayChuyenHopDongChoKeToan,														
			tcdt.So,														
			tcdt.Thang,														
			tcdt.Nam,														
			tcdt.GiaTriHopDong,														
			tcdt.CongNo,														
			tcdt.HopDongChiTietREF,														
			tcdt.DangSuDung,														
			tcdt.IsGiayPhep,														
			tcdt.TrangThaiHopDong,											
			tcdt.IsBanCung,														
			tcdt.DmPhongBanREF,														
			tcdt.TenPhongBan,														
			tcdt.DmBoPhanREF,														
			tcdt.TenBoPhan,														
			tcdt.DmNhomLamViecREF,														
			tcdt.TenNhomLamViec,														
			tcdt.DmDiaDiemLamViecREF,														
			tcdt.TenDiaDiemLamViec,														
			tcdt.SysNhanVienREF,														
			tcdt.TenDangNhap,														
			tcdt.TenNhanVien,														
			tcdt.TenKhachHang,														
			tcdt.NhanHang,														
			tcdt.DmNhomNganhREF,														
			tcdt.TenNhomNganh,														
			tcdt.DmHinhThucQuangCao,														
			tcdt.TenHinhThucQuangCao,														
			tcdt.DmSanPhamREF,														
			tcdt.TenSanPham,														
			tcdt.DmNhomWebsiteREF,														
			tcdt.TenNhomWebsite,														
			tcdt.DmChuyenMucREF,														
			tcdt.TenChuyenMuc,														
			tcdt.DmLoaiBannerREF,														
			tcdt.TenLoaiBanner,														
			tcdt.DmViTriREF,														
			tcdt.TenViTri,														
			tcdt.DotChayHopDong,														
			tcdt.SoLuongDotChayHD,										-- 0      ??????????????????????				
			tcdt.DotChayBooking,														
			tcdt.SoLuongDotChayBooking,														
			tcdt.SoLuong,														
			tcdt.DonViTinh,														
			tcdt.DonGia,														
			tcdt.DonGiaTheoDonVi,														
			tcdt.ChietKhau,														
			tcdt.GiamGia,														
			tcdt.ThanhTien,														
			tcdt.TiLeTuVan,														
			tcdt.ChiPhiTuVan,														
			tcdt.IsKhuyenMai,											-- HĐCT <=> chiết khấu = 100			
			tcdt.KhuyenMai,														
			tcdt.DmBannerREF,														
			tcdt.DmChienDichREF,											
			tcdt.DmWebsiteREF,														
			tcdt.TenWebsite

			IF(EXISTS(SELECT TOP (1) ThucChayDaTinhID FROM @TABLE_OP 
						WHERE AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_id 
						ORDER BY ThucChayDaTinhID))
			BEGIN
				--THUC HIEN DOI TRU BEN THUCCHAYDATINH_MUANGOAI
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

			   SELECT tcdtm.[HopDongREF]										-- HD
			   ,tcdtm.[SoHopDong]											-- HD
			   ,tcdtm.[DmMaHopDongREF]									-- HD
			   ,tcdtm.[NgayDanhSoHopDong]								    -- HD
			   ,tcdtm.[TrangThaiHopDong]									-- HD
			   ,tcdtm.[DmNhanVienREF]										-- HD
			   ,tcdtm.[TenDangNhap]										-- HD
			   ,tcdtm.[DmPhongBanREF]										-- HD
			   ,tcdtm.[DmBoPhanREF]										-- HD
			   ,tcdtm.[DmNhomLamViecREF]									-- HD
			   ,tcdtm.[DmDiaDiemLamViecREF]								-- HD
			   ,tcdtm.[DmKhachHangREF]									-- HD
			   ,tcdtm.[HopDongChiTietREF]									-- HDCT
			   ,tcdtm.[LstDmNhanHangREF]									-- HDCT
			   ,tcdtm.[LstDmNhomNganhREF]									-- HDCT
			   ,tcdtm.[DmHinhThucQuangCaoREF]								-- HDCT
			   ,tcdtm.[DmSanPhamREF]										-- HDCT
			   ,tcdtm.[DmChuyenMucREF]									-- HDCT
			   ,tcdtm.[DmLoaiBannerREF]									-- HDCT
			   ,tcdtm.[DmViTriREF]										-- HDCT
			   ,tcdtm.[SoLuong]											-- HDCT
			   ,tcdtm.[DonViTinhREF]										-- HĐCT
			   ,tcdtm.[DonGia]											-- HDCT
			   ,tcdtm.[ChietKhau]											-- HDCT
			   ,tcdtm.[ThanhTien]											-- HDCT
			   ,tcdtm.[IsKhuyenMai]										-- HDCT
			   ,tcdtm.[KhuyenMai]											-- HDCT
			   ,tcdtm.[ThucChayMuaNgoaiChiTietREF]						-- HDCT
			   ,0 AS [TongTienDuToanMuaSauCK]							-- HDCT
			   ,0 AS [TongTienDuToanLaiMuaSauCK]							-- HDCT
			   ,0 AS [ChietKhauMua]										-- 0
			   ,tcdtm.[DmBannerREF]										-- HDCT
			   ,tcdtm.[DmChienDichREF]									-- 0
			   ,tcdtm.[DmWebsiteREF]										-- HDCT
			   ,tcdtm.[TenWebsite]										-- HDCT
			   ,@NgayGhiNhanThucChay as [NgayThucHien]										-- @Ngaythuchien
			   ,tcdtm.[NgayBatDau]										-- THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
			   ,tcdtm.[NgayKetThuc]										
			   ,tcdtm.[DonViTinhThucChay]									-- TC
			   ,0 AS [DonGiaTheoDonViTinhTC]								-- TC
			   ,0 AS [TongViewClickThucChay]								-- 0
			   ,0 AS [TongSoBaiVietChiPhiThucChay]					    -- 0
			   ,0 AS [SoLuongThucChay]									-- TC
			   ,0 AS [TongThanhTienThucChayBanSauCK]						-- TC,tcdtm. CK
			   ,0 AS [TongThanhTienThucChayMuaSauCK]                     -- TC
			   ,0 AS [ThanhTienLaiThucChaySauCK]							-- TC bán - mua
			   ,0 AS [ThanhTienLaiThucChayKM]							-- TC lãi của HDCT khuyến mại
			   ,0 AS [SoLuongThucChayKM]									-- Số lượng TC của HDCT khuyến mại
			   ,0 AS [SoLuongThucChayLechTreoHa]                         -- số lượng vượt phân bổ
			   ,0 AS [ThanhTienLechTreoHa]								-- thành tiền vượt phân bổ
			   ,SUM(ISNULL(tcdtm.[ThanhTienLaiThucChaySauCK],0) + ISNULL(tcdtm.[GiaTriThayDoiLaiSauCK],0)) 	AS [GiaTriThayDoiLaiSauCK]							-- 0
			   ,SUM(ISNULL(tcdtm.[SoLuongThucChay],0) + ISNULL(tcdtm.[SoLuongThayDoi],0)) AS [SoLuongThayDoi]								-- 0	
			   ,SUM(ISNULL(tcdtm.[SoLuongThucChayKM],0) + ISNULL(tcdtm.[SoLuongKMThayDoi],0)) [SoLuongKMThayDoi]									-- 0
			   ,SUM(ISNULL(tcdtm.[ThanhTienLaiThucChayKM],0) + ISNULL(tcdtm.[GiaTriKMLaiThayDoi],0)) AS [GiaTriKMLaiThayDoi]								-- 0
			   ,@ghiChuDoiTru + N', tcdtm' AS [GhiChu]											-- GhiChu
			   ,GETDATE() AS [CreatedAt]											-- GETDATE()
			   ,GETDATE() AS [LastModifiedAt]								-- GETDATE()
			   FROM dbo.ThucChayDaTinhMuaNgoai tcdtm
			   WHERE tcdtm.HopDongREF = @HopDongREF
			   AND tcdtm.HopDongChiTietREF = @HopDongChiTietREF
			   AND tcdtm.[ThucChayMuaNgoaiChiTietREF] = @AppKetQuaVanHanh_CreatorContent_id
			   GROUP BY	   tcdtm.[HopDongREF]										-- HD
			   ,tcdtm.[SoHopDong]											-- HD
			   ,tcdtm.[DmMaHopDongREF]									-- HD
			   ,tcdtm.[NgayDanhSoHopDong]								    -- HD
			   ,tcdtm.[TrangThaiHopDong]									-- HD
			   ,tcdtm.[DmNhanVienREF]										-- HD
			   ,tcdtm.[TenDangNhap]										-- HD
			   ,tcdtm.[DmPhongBanREF]										-- HD
			   ,tcdtm.[DmBoPhanREF]										-- HD
			   ,tcdtm.[DmNhomLamViecREF]									-- HD
			   ,tcdtm.[DmDiaDiemLamViecREF]								-- HD
			   ,tcdtm.[DmKhachHangREF]									-- HD
			   ,tcdtm.[HopDongChiTietREF]									-- HDCT
			   ,tcdtm.[LstDmNhanHangREF]									-- HDCT
			   ,tcdtm.[LstDmNhomNganhREF]									-- HDCT
			   ,tcdtm.[DmHinhThucQuangCaoREF]								-- HDCT
			   ,tcdtm.[DmSanPhamREF]										-- HDCT
			   ,tcdtm.[DmChuyenMucREF]									-- HDCT
			   ,tcdtm.[DmLoaiBannerREF]									-- HDCT
			   ,tcdtm.[DmViTriREF]										-- HDCT
			   ,tcdtm.[SoLuong]											-- HDCT
			   ,tcdtm.[DonViTinhREF]										-- HĐCT
			   ,tcdtm.[DonGia]											-- HDCT
			   ,tcdtm.[ChietKhau]											-- HDCT
			   ,tcdtm.[ThanhTien]											-- HDCT
			   ,tcdtm.[IsKhuyenMai]										-- HDCT
			   ,tcdtm.[KhuyenMai]											-- HDCT
			   ,tcdtm.[ThucChayMuaNgoaiChiTietREF]						-- HDCT
			   ,tcdtm.[DmBannerREF]										-- HDCT
			   ,tcdtm.[DmChienDichREF]									-- 0
			   ,tcdtm.[DmWebsiteREF]										-- HDCT
			   ,tcdtm.[TenWebsite]										-- HDCT
			   ,tcdtm.[NgayBatDau]										-- THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
			   ,tcdtm.[NgayKetThuc]										
			   ,tcdtm.[DonViTinhThucChay]

				UPDATE A
				SET A.RecordStatus = 0
				FROM dbo.AppKetQuaVanHanh_CreatorContent A
				WHERE A.AppKetQuaVanHanh_CreatorContent_id = @AppKetQuaVanHanh_CreatorContent_id
			END
			SET @ThucChayDaTinhID_op = ISNULL((SELECT TOP (1) ThucChayDaTinhID FROM @TABLE_OP),'')
END



```
