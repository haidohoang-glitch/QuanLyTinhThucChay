# Stored Procedure: `ThucChayDaTinh_MuaNgoai_InsertThucChayLai_ThanhTien_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-11 16:47:05.317000
- **Ngày sửa cuối**: 2024-11-26 11:03:24.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ADS_Operating_Result_Map_OrderId` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@Operating_Order_Id` | `int(4)` | No |
| `@DonGiaTheoDonViTinh` | `float(8)` | No |
| `@DonViTinh` | `nvarchar(200)` | No |
| `@SoLuongThucChay` | `bigint(8)` | No |
| `@TongTienThucChayBanSCK` | `float(8)` | No |
| `@TongTienThucChayMuaSCK` | `float(8)` | No |
| `@TongTienLaiThucChaySCK` | `float(8)` | No |
| `@TongTienDuToanMuaSauCK` | `float(8)` | No |
| `@ghiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLai_ThanhTien_GGFB]
	@NgayThucHien						DATETIME,
	@ADS_Operating_Result_Map_OrderId  	INT,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@Operating_Order_Id					INT,
	@DonGiaTheoDonViTinh				FLOAT,
	@DonViTinh							NVARCHAR(100),
	@SoLuongThucChay					BIGINT,
	@TongTienThucChayBanSCK				FLOAT,
	@TongTienThucChayMuaSCK				FLOAT,
	@TongTienLaiThucChaySCK				FLOAT,
	@TongTienDuToanMuaSauCK				FLOAT,
	@ghiChu								NVARCHAR(1000)
	
AS
BEGIN
	DECLARE @NgayGioiHanTinh DATETIME  = '2020-01-01',  -- ngày thực hiện tính nhỏ nhất
	@DmChienDichREF INT = @Operating_Order_Id --Chien dich chay cho GGFB va tinh tien thong thuong
	, @DmWebsiteREF INT = 265
	, @Brand_id NVARCHAR(100) = ''

	SELECT TOP 1 @Brand_id = ISNULL(OD.Brand_id,0),@DmWebsiteREF= ISNULL(OD.DmWebsiteREF,265)
				   FROM DBO.ADS_Operating_Order OD 
				   WHERE OD.Contract_Id = @HopDongREF 
				   AND OD.Contract_Detail_Id = @HopDongChiTietREF
				   AND OD.ID = @Operating_Order_Id

	SET @Brand_id = ISNULL((@Brand_id),'')
	SET @DmWebsiteREF = ISNULL((@DmWebsiteREF),265)

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
           --,[LstDmNhanHangREF] = HDCT.DanhSachNhanHangREF  
		   ,[LstDmNhanHangREF] = @Brand_id
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
           ,[ThucChayMuaNgoaiChiTietREF] = @ADS_Operating_Result_Map_OrderId   
		   ,[TongTienDuToanMuaSauCK] = @TongTienDuToanMuaSauCK  
		   ,[TongTienDuToanLaiMuaSauCK] = IIF((HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100), 0, (HDCT.ThanhTien - @TongTienDuToanMuaSauCK))  
           ,[ChietKhauMua] = 0    
           ,[DmBannerREF] = HDCT.DmBannerREF   
           ,[DmChienDichREF] =  @DmChienDichREF
           --,[DmWebsiteREF] = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(HDCT.DmWebsiteREF) 				
		   ,[DmWebsiteREF] = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF) 				
		   ,[TenWebsite] = dbo.GetWebsiteLinkByDmWebsiteID(@DmWebsiteREF,N'') 
           ,[NgayThucHien] = @Ngaythuchien
           ,[NgayBatDau] = NULL --THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
           ,[NgayKetThuc] = NULL---THONG TIN NGAY BAT DAU VA KET THUC CUA CHIEN DICH
           ,[DonViTinhThucChay] = @DonViTinh
           ,[DonGiaTheoDonViTinhTC] = @DonGiaTheoDonViTinh
           ,[TongViewClickThucChay] = 0 
           ,[TongSoBaiVietChiPhiThucChay] = 0 

		   -- check vượt
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
END




```
