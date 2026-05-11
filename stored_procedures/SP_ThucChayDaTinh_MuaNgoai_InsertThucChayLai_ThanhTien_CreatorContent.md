# Stored Procedure: `ThucChayDaTinh_MuaNgoai_InsertThucChayLai_ThanhTien_CreatorContent`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-25 16:35:39.280000
- **Ngày sửa cuối**: 2021-10-14 16:47:20.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@AppKetQuaVanHanh_CreatorContent_id` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DonGiaTheoDonViTinh` | `float(8)` | No |
| `@DonViTinh` | `nvarchar(200)` | No |
| `@SoLuongThucChay` | `bigint(8)` | No |
| `@TongTienThucChayBanSCK` | `float(8)` | No |
| `@TongTienThucChayMuaSCK` | `float(8)` | No |
| `@TongTienLaiThucChaySCK` | `float(8)` | No |
| `@ghiChu` | `nvarchar(2000)` | No |
| `@ThucChayDaTinh_MuaNgoai_ouput` | `bigint(8)` | Yes |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLai_ThanhTien_CreatorContent]
	@NgayThucHien						DATETIME,
	@AppKetQuaVanHanh_CreatorContent_id	INT,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@DonGiaTheoDonViTinh				FLOAT,
	@DonViTinh							NVARCHAR(100),
	@SoLuongThucChay					BIGINT,
	@TongTienThucChayBanSCK				FLOAT,
	@TongTienThucChayMuaSCK				FLOAT,
	@TongTienLaiThucChaySCK				FLOAT,
	@ghiChu								NVARCHAR(1000),
	@ThucChayDaTinh_MuaNgoai_ouput		BIGINT OUTPUT
	
AS
BEGIN
	DECLARE @NgayGioiHanTinh DATETIME  = '2020-01-01'  -- ngày thực hiện tính nhỏ nhất
	
	DECLARE @Table_out TABLE(ThucChayDaTinh_MuaNgoai_ID INT, HopDongID int, HopDongChiTietID int)

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

	OUTPUT INSERTED.ID, INSERTED.HopDongREF, INSERTED.HopDongChiTietREF INTO @Table_out

    SELECT
			[HopDongREF] = @HopDongREF   
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
           ,[HopDongChiTietREF]  = @HopDongChiTietREF     
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
           ,[ChietKhau]   =  HDCT.[ChietKhau]  
           ,[ThanhTien]  =  HDCT.[ThanhTien]   
           ,[IsKhuyenMai]  =  HDCT.[IsKhuyenMai]    
           ,[KhuyenMai]  =  HDCT.[KhuyenMai]    
           ,[ThucChayMuaNgoaiChiTietREF] = @AppKetQuaVanHanh_CreatorContent_id   
		   ,[TongTienDuToanMuaSauCK] = 0  
		   ,[TongTienDuToanLaiMuaSauCK] = 0 
           ,[ChietKhauMua] = 0    
           ,[DmBannerREF] = HDCT.DmBannerREF   
           ,[DmChienDichREF] =  0
           ,[DmWebsiteREF] = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(HDCT.DmWebsiteREF) 				
		   ,[TenWebsite] = dbo.GetWebsiteLinkByDmWebsiteID(HDCT.DmWebsiteREF,HDCT.TenWebsite) 
           ,[NgayThucHien] = @Ngaythuchien
           ,[NgayBatDau] = NULL --THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
           ,[NgayKetThuc] = NULL---THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
           ,[DonViTinhThucChay] = @DonViTinh
           ,[DonGiaTheoDonViTinhTC] = @DonGiaTheoDonViTinh
           ,[TongViewClickThucChay] = 0 
           ,[TongSoBaiVietChiPhiThucChay] = 0 
           ,[SoLuongThucChay] = IIF ((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100), 0, @SoLuongThucChay)
           ,[TongThanhTienThucChayBanSauCK]  = IIF((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100) , 0, @TongTienThucChayBanSCK)
           ,[TongThanhTienThucChayMuaSauCK] = @TongTienThucChayMuaSCK
           ,[ThanhTienLaiThucChaySauCK] =  IIF((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100) , 0, @TongTienLaiThucChaySCK)
           ,[ThanhTienLaiThucChayKM] = IIF((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100), @TongTienLaiThucChaySCK, 0)  -- thực chạy lãi của TH Khuyến mại 100%
           ,[SoLuongThucChayKM] = IIF((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100), @SoLuongThucChay, 0)
           ,[SoLuongThucChayLechTreoHa] = 0
           ,[ThanhTienLechTreoHa] = 0
           ,[GiaTriThayDoiLaiSauCK] = 0
           ,[SoLuongThayDoi] = 0
           ,[SoLuongKMThayDoi] = 0
           ,[GiaTriKMLaiThayDoi] = 0
           ,[GhiChu] = @GhiChu
           ,[CreatedAt] = GETDATE()
           ,[LastModifiedAt] = GETDATE()
		FROM 
		(	SELECT * 
			FROM dbo.HopDongChiTiet HDCT 
			WHERE  HDCT.HopDongChiTietID = @HopDongChiTietREF
		)hdct 
		INNER JOIN 
		(	SELECT *
			FROM dbo.HopDong HD 
			WHERE HD.HopDongID = @HopDongREF
		)hd ON HD.HopDongID = hdct.HopDongFK

		SET @ThucChayDaTinh_MuaNgoai_ouput = ISNULL((SELECT TOP (1) ThucChayDaTinh_MuaNgoai_ID FROM @Table_out),0)
END





```
