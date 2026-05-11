# Stored Procedure: `ThucChayDaTinh_InsertThucChay_ThanhTien_GGFB_BK_20210107`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-01-07 10:18:08.540000
- **Ngày sửa cuối**: 2021-01-07 10:18:08.540000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ADS_Operating_Result_Map_OrderId` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@Operating_Order_Id` | `int(4)` | No |
| `@MaxTienThucChayBanOrder` | `float(8)` | No |
| `@TongTienThucChaySauChietKhauOder` | `float(8)` | No |
| `@ghiChu` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChay_ThanhTien_GGFB_BK_20210107]
	@NgayThucHien						DATETIME,
	@ADS_Operating_Result_Map_OrderId	INT,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@Operating_Order_Id					INT,
	@MaxTienThucChayBanOrder			FLOAT,
	@TongTienThucChaySauChietKhauOder	FLOAT,
	@ghiChu								NVARCHAR(512)
AS
BEGIN
	DECLARE @NgayGioiHanTinh DATETIME  = '2020-01-01',
	@DmChienDichREF int = @Operating_Order_Id --Chien dich cho GGFB va dc tinh theo thong thuong

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
																	-- check vượt hợp đồng ?????????
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
	SELECT NEWID() AS ThucChayDaTinhID, TD.HopDongID, TD.SoHopDong, TD.DmMaHopDongREF, TD.TenMaHopDong, TD.NgayDanhSoHopDong, TD.NgayKyHopDong, 
		TD.NhanHopDong, TD.NgayNhanBanFax, TD.NgayNhanHopDongBanCung, TD.NgayChuyenHopDongChoKeToan, TD.So, TD.Thang, TD.Nam, 
		TD.GiaTriHopDong, TD.CongNo, TD.HopDongChiTietREF, TD.DangSuDung, TD.IsGiayPhep, TD.TrangThaiHopDon,TD.IsBanCung, 
		TD.DmPhongBanREF, TD.TenPhongBan, TD.DmBoPhanREF, TD.TenBoPhan, TD.DmNhomLamViecREF, TD.TenNhomLamViec, TD.DmDiaDiemLamViecREF, TD.TenDiaDiemLamViec, 
		TD.SysNhanVienREF, TD.TenDangNhap, TD.TenNhanVien, TD.TenKhachHang, TD.NhanHang,
		TD.DmNhomNganhREF, TD.TenNhomNganh, TD.DmHinhThucQuangCao, TD.TenHinhThucQuangCao, 
		TD.DmSanPhamREF, TD.TenSanPham, TD.DmNhomWebsiteREF, 
		TD.TenNhomWebsite, TD.DmChuyenMucREF, TD.TenChuyenMuc, 
		TD.DmLoaiBannerREF, TD.TenLoaiBanner, TD.DmViTriREF, TD.TenViTri, 
		TD.DotChayHopDong, TD.SoLuongDotChayHD,
		TD.DotChayBooking, TD.SoLuongDotChayBooking, 
		TD.SoLuong, TD.DonViTinh, TD.DonGia, 
		TD.DonGiaTheoDonVi,--cho nay xem lai viec xac dinh don gia Native ads
		TD.ChietKhau, TD.GiamGia, TD.ThanhTien,
		TD.TiLeTuVan,  TD.ChiPhiTuVan,
		TD.IsKhuyenMai,  
		TD.KhuyenMai,
		TD.DmBannerREF,
		TD.DmChienDichREF,
		TD.DmWebsiteREF,
		TD.TenWebsite,
		TD.TongViewThucChay,
		TD.TongClickThucChay,
		TD.TongSoBaiViet,
		TD.SoLuongThucChay,
		TD.NgayThucHien,
		TD.GiaTriThayDoi,
		----------
		(CASE WHEN TD.ChietKhau = 100 THEN TD.ThanhTienKM
		ELSE (TD.ThanhTienSauTrietKhauThucChay*(100+TD.ChietKhau))/100
		END) AS ThanhTienThucChayTruocTrietKhau ,

		ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
		TD.ThanhTienSauTrietKhauThucChay,
		ISNULL(((TD.ThanhTienSauTrietKhauThucChay * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
		TD.ThanhTienSauTrietKhauThucChay AS ThanhTienThucThu,
		TD.ThanhTienKM,
		TD.SoLuongThucChayKM,
		(CASE WHEN TD.ChietKhau = 100 THEN (TD.SoLuongTC - TD.SoLuongThucChayKM)
				ELSE (TD.SoLuongTC - TD.SoLuongThucChay)
			END
		)AS SoLuongLechTreoHa,
		(CASE WHEN TD.ChietKhau = 100 THEN (TD.Sell_Money_VND- TD.ThanhTienKM)
				ELSE ((TD.Sell_Money_VND - TD.ThanhTienSauTrietKhauThucChay)/(100-TD.ChietKhau))*100
			END
		)AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		TD.GhiChu
		---------
		 FROM
	(
	SELECT HopDongID    = HD.HopDongID,         
			SoHopDong   = HD.SoHopDong,		   
			DmMaHopDongREF = HD.DmMaHopDongREF,    
			TenMaHopDong = HD.TenMaHopDong,	   		
			NgayDanhSoHopDong = HD.NgayDanhSoHopDong,			
			NgayKyHopDong= HD.NgayKyHopDong,				
			NhanHopDong = HD.NhanHopDong,				
			NgayNhanBanFax = HD.NgayNhanBanFax,				
			NgayNhanHopDongBanCung  = HD.NgayNhanHopDongBanCung,			
			NgayChuyenHopDongChoKeToan = HD.NgayChuyenHopDongChoKeToan,			
			So = HD.So,								
			Thang = HD.Thang,							
			Nam = HD.Nam,							
			GiaTriHopDong = HD.GiaTriHopDong,					
			CongNo = HD.CongNo,							
			HopDongChiTietREF = HDCT.HopDongChiTietID,				
			DangSuDung = HD.DangSuDung,						
			IsGiayPhep = HD.IsGiayPhep,						
			TrangThaiHopDon = 2,			
			IsBanCung = HD.IsBanCung,						
			DmPhongBanREF = HD.DmPhongBanREF,					
			TenPhongBan = HD.TenPhongBan,					
			DmBoPhanREF = HD.DmBoPhanREF,				
			TenBoPhan = ISNULL(HD.TenBoPhan,'')	,			
			DmNhomLamViecREF = HD.DmNhomLamViecREF,				
			TenNhomLamViec = ISNULL(HD.TenNhom,''),				
			DmDiaDiemLamViecREF = HD.DmDiaDiemLamViecREF, 				
			TenDiaDiemLamViec = ISNULL(HD.TenDiaDiemLamViec,''),				
			SysNhanVienREF = HD.SysNhanVienREF,				
			TenDangNhap = HD.TenDangNhap,				
			TenNhanVien = HD.TenNhanVien,				
			TenKhachHang = HD.TenKhachHang,				
			NhanHang = HDCT.DanhSachNhanHangREF,				
			DmNhomNganhREF = HDCT.DmNhomNganhREF,				
			TenNhomNganh = ISNULL(HDCT.TenNhomNganh,''),				
			DmHinhThucQuangCao = HDCT.DmLoaiREF,				
			TenHinhThucQuangCao = HDCT.TenLoai,				
			DmSanPhamREF = HDCT.DmSanPhamREF,				
			TenSanPham = HDCT.TenSanPham,				
			DmNhomWebsiteREF = HDCT.DmNhomWebsiteREF,				
			TenNhomWebsite = HDCT.TenNhomWebsite,				
			DmChuyenMucREF= HDCT.DmChuyenMucREF,			
			TenChuyenMuc = HDCT.TenChuyenMuc,			
			DmLoaiBannerREF= HDCT.DmLoaiBannerREF,				
			TenLoaiBanner = HDCT.TenLoaiBanner,					
			DmViTriREF = HDCT.DmViTriREF,						
			TenViTri  = HDCT.TenViTri,					
			DotChayHopDong = @ghiChu	,		
			SoLuongDotChayHD = 0	,		
			DotChayBooking = @ADS_Operating_Result_Map_OrderId	,			
			SoLuongDotChayBooking = @ADS_Operating_Result_Map_OrderId ,   
			SoLuong = HDCT.SoLuong       ,             
			DonViTinh = [dbo].[FormatDonViTinh_ThanhTien_GGFB](TC.DonViTinhTC),				
			DonGia = HDCT.DonGia,						
			DonGiaTheoDonVi = IIF(TC.SoLuongTC = 0,0,TC.Sell_Money_VND/TC.SoLuongTC) ,            
			ChietKhau = HDCT.ChietKhau,					
			GiamGia  = HDCT.GiamGia,					
			ThanhTien  = HDCT.ThanhTien,						
			TiLeTuVan   = HDCT.TiLeTuVan,                
			ChiPhiTuVan = HDCT.ChiPhiTuVan,                       
			IsKhuyenMai = HDCT.IsKhuyenMai,                 
			KhuyenMai   = HDCT.KhuyenMai,                     
			DmBannerREF = HDCT.DmBannerREF ,				
			DmChienDichREF = @DmChienDichREF,				
			DmWebsiteREF = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(HDCT.DmWebsiteREF) ,				
			TenWebsite = dbo.GetWebsiteLinkByDmWebsiteID(HDCT.DmWebsiteREF,HDCT.TenWebsite) ,				
			TongViewThucChay = 0,		
			TongClickThucChay = 0	,			
			TongSoBaiViet = 0	,	
			SoLuongThucChay = (CASE WHEN (HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100) THEN 0
								ELSE [dbo].[ThucChay_GetSoLuongThucChay_ThanhTien_GGFB] ( TC.SoLuongTC, TC.Sell_Money_VND,
																						 TC.SoLuongTC, TC.Sell_Money_VND,
																						 @NgayThucHien, HDCT.HopDongChiTietID,
																						 HDCT.SoLuong, HDCT.DonGia,
																						 HDCT.ThanhTien, HDCT.ChietKhau, @MaxTienThucChayBanOrder	,
																										@TongTienThucChaySauChietKhauOder )
							END),
			NgayThucHien = @NgayThucHien,				
			GiaTriThayDoi = 0,			
			ThanhTienThucChayTruocTrietKhau  = 0,  			      
			GiaTriTrietKhauThucChay = 0,           
			ThanhTienSauTrietKhauThucChay = (CASE WHEN (HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100)  THEN 0
												ELSE [dbo].[ThucChay_ThanhTienThucChay_ThanhTien_GGFB] ( TC.Sell_Money_VND, TC.Sell_Money_VND,
																										@NgayThucHien , HDCT.HopDongChiTietID, 
																										HDCT.SoLuong, HDCT.DonGia,
																										HDCT.ThanhTien, HDCT.ChietKhau, @MaxTienThucChayBanOrder	,
																										@TongTienThucChaySauChietKhauOder)
											END),      
			GiaTriHoaHongThucChay = 0,         
			ThanhTienThucThu = 0,               
			ThanhTienKM = (CASE WHEN (HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100)  THEN [dbo].[ThucChay_ThanhTienThucChay_ThanhTien_GGFB] ( TC.Sell_Money_VND, TC.Sell_Money_VND,
																										@NgayThucHien , HDCT.HopDongChiTietID, 
																										HDCT.SoLuong, HDCT.DonGia,
																										HDCT.ThanhTien, HDCT.ChietKhau, @MaxTienThucChayBanOrder	,
																										@TongTienThucChaySauChietKhauOder )
												ELSE 0
											END),                            
			SoLuongThucChayKM = (CASE WHEN (HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100) THEN [dbo].[ThucChay_GetSoLuongThucChay_ThanhTien_GGFB] ( TC.SoLuongTC, TC.Sell_Money_VND,
																						 TC.SoLuongTC, TC.Sell_Money_VND,
																						 @NgayThucHien, HDCT.HopDongChiTietID,
																						 HDCT.SoLuong, HDCT.DonGia,
																						 HDCT.ThanhTien, HDCT.ChietKhau, @MaxTienThucChayBanOrder	,
																										@TongTienThucChaySauChietKhauOder )
								ELSE 0
								END),        
			SoLuongThucChayLechTreoHa = 0   ,
			ThanhTienLechTreoHa =0,
			CreatedAt  = GETDATE(),
			LastModifiedAt = GETDATE(),
			IsPheDuyet = '',  
			PheDuyetBy = '',    
			PheDuyetAt = GETDATE(),   
			SoLuongThayDoi = 0,   
			SoLuongKMThayDoi = 0,   
			GiaTriKMThayDoi = 0,  
			GhiChu = @ghiChu  ,
			TC.SoLuongTC,
			TC.Sell_Money_VND  
	 FROM 
		(	  SELECT OD.Contract_Number, OD.Contract_Id, OD.Contract_Detail_Id
			  , IIF(OD.UNITS = '',N'GÓI',OD.UNITS ) AS DonViTinhTC--DONVITINH
			  , OD.Product_Id --SAN PHAM
			  , OD.Brand_id --NHAN HANG
			  , TC.Id --THONG TIN CHI TIET THUC CHAY ID
			  , TC.operating_Result_Id --THONG TIN KET QUA THUC CHAY ID CHUA MAPPING
			  , IIF(TC.Result=0,1,TC.Result) AS SoLuongTC --SOLUONG
			  , ISNULL(TC.Sell_Money_VND,0) AS Sell_Money_VND --THANH TIEN THUC CHAY BAN
			  FROM 
			  (SELECT TC.id, TC.Operating_Order_Id, TC.operating_Result_Id, ISNULL(TC.Result,0) Result, TC.Sell_Money_VND 
					FROM [dbo].[ADS_Operating_Result_Map_Order] TC 
					WHERE TC.ID = @ADS_Operating_Result_Map_OrderId 
					AND ISNULL(TC.Sell_Money_VND,0) <> 0
					AND  CONVERT(DATE,TC.[LastModificationTime]) = @NgayThucHien
				) TC
			  INNER JOIN 
			  (SELECT OD.Contract_Number, OD.Contract_Id, OD.Contract_Detail_Id, OD.Id  , ISNULL(OD.UNITS,'') UNITS , OD.Product_Id , OD.Brand_id
				   FROM DBO.ADS_Operating_Order OD 
				   WHERE OD.Contract_Id = @HopDongREF 
				   AND OD.Contract_Detail_Id = @HopDongChiTietREF
			   )OD ON TC.Operating_Order_Id = OD.Id
		) TC
		INNER JOIN 
		(	SELECT * 
			FROM dbo.HopDongChiTiet HDCT 
			WHERE  HDCT.HopDongChiTietID = @HopDongChiTietREF
		)hdct ON hdct.HopDongFK = TC.Contract_Id AND hdct.HopDongChiTietID = TC.Contract_Detail_Id
		INNER JOIN 
		(	SELECT *
			FROM dbo.HopDong HD 
			WHERE HD.HopDongID = @HopDongREF
		)hd ON HD.HopDongID = TC.Contract_Id
	)TD
END



```
