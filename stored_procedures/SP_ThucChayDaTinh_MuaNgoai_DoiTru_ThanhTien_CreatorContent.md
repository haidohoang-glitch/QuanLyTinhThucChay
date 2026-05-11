# Stored Procedure: `ThucChayDaTinh_MuaNgoai_DoiTru_ThanhTien_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-25 16:30:57.380000
- **Ngày sửa cuối**: 2021-06-25 16:30:57.380000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@ghiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_DoiTru_ThanhTien_CreatorContent]
	@NgayGhiNhanThucChay				DATETIME,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@ghiChu								NVARCHAR(1000)
	
AS
BEGIN
	DECLARE @NgayGioiHanTinh DATETIME  = '2020-01-01'  -- ngày thực hiện tính nhỏ nhất

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
           ,-SUM([SoLuongThucChayLechTreoHa]) AS [SoLuongThucChayLechTreoHa]                         -- số lượng vượt phân bổ
           ,-SUM([ThanhTienLechTreoHa]) AS [ThanhTienLechTreoHa]								-- thành tiền vượt phân bổ
           ,-SUM(tcdtm.[ThanhTienLaiThucChaySauCK] + tcdtm.[GiaTriThayDoiLaiSauCK]) 	AS [GiaTriThayDoiLaiSauCK]							-- 0
           ,-SUM(tcdtm.[SoLuongThucChay] +tcdtm.[SoLuongThayDoi]) AS [SoLuongThayDoi]								-- 0	
           ,-SUM(tcdtm.[SoLuongThucChayKM] + tcdtm.[SoLuongKMThayDoi]) [SoLuongKMThayDoi]									-- 0
           ,-SUM(tcdtm.[ThanhTienLaiThucChayKM] + tcdtm.[GiaTriKMLaiThayDoi]) AS [GiaTriKMLaiThayDoi]								-- 0
           ,@ghiChu AS [GhiChu]											-- GhiChu
           ,GETDATE() AS [CreatedAt]											-- GETDATE()
           ,GETDATE() AS [LastModifiedAt]								-- GETDATE()
		   FROM dbo.ThucChayDaTinh_MuaNgoai tcdtm
		   WHERE tcdtm.HopDongREF = @HopDongREF
		   AND tcdtm.HopDongChiTietREF = @HopDongChiTietREF
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
		   HAVING (SUM([ThanhTienLechTreoHa]) <> 0
		   OR SUM(tcdtm.[ThanhTienLaiThucChaySauCK] + tcdtm.[GiaTriThayDoiLaiSauCK]) <> 0
		   OR SUM(tcdtm.[ThanhTienLaiThucChayKM] + tcdtm.[GiaTriKMLaiThayDoi]) <> 0
		   )

END





```
