# Stored Procedure: `ThucChay_GGFB_GhiNhanPhatSinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-24 17:42:32.887000
- **Ngày sửa cuối**: 2025-06-23 16:56:16.680000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

--EXEC [dbo].[ThucChay_GGFB_GhiNhanPhatSinh] @NgayThucHien = '2025-05-07', @NgayDanhSoGioiHan = '2022-05-07'

CREATE PROCEDURE [dbo].[ThucChay_GGFB_GhiNhanPhatSinh]
	@NgayThucHien DATE,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(100) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

	--================================= TH chạy lại SP từ lần thứ 2 trong cùng @NgayThucHien
	CREATE TABLE #dmIDdatinh (ID INT, type INT)

	INSERT INTO #dmIDdatinh
	SELECT tcdt.DotChayBooking, 
		   IIF(tcdt.DotChayHopDong = N'Tính mới GGFB result_map_order', 1, 2)
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
	LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE tcdt.NgayThucHien = @NgayThucHien AND 
		  tcdt.DotChayHopDong IN (N'Tính mới GGFB result_map_order', N'Tính mới GGFB result_quantity') AND 
		 (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID) AND
         (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong) 

	DELETE tcdt
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
	LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE tcdt.NgayThucHien = @NgayThucHien AND 
		  tcdt.DotChayHopDong IN (N'Tính mới GGFB result_map_order', N'Tính mới GGFB result_quantity') AND 
		 (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID) AND
         (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong) 

	DELETE tcdt
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh_MuaNgoai tcdt
	LEFT JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE tcdt.NgayThucHien = @NgayThucHien AND 
		  tcdt.ghichu IN ( N'Tính mới: SP tối ưu [dbo].[ThucChay_GGFB_GhiNhanPhatSinh]',
		                   N'Tính mới: SP tối ưu xử lý tay [dbo].[ThucChay_GGFB_GhiNhanPhatSinh]') AND 
		 (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID) AND
         (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong) 

	UPDATE TC
	SET IsCaculatedActual = 0
	FROM dbo.[ADS_Operating_Result_Map_Order] TC
	INNER JOIN #dmIDdatinh dm ON dm.type = 1 AND TC.Id = dm.ID
	WHERE CAST(TC.LastModificationTime AS DATE) = @NgayThucHien 
		  AND TC.IsDeleted = 0
		  AND ISNULL(TC.Sell_Money_VND,0) <> 0

	UPDATE TC
	SET [IsCalc_Result_Quantity] = 0
	FROM dbo.[ADS_Operating_Result_Quantity] TC
	INNER JOIN #dmIDdatinh dm ON dm.type = 2 AND TC.Id = dm.ID
	WHERE isnull(TC.IsDeleted,0) = 0
		  AND ISNULL(TC.TotalMoney,0) <> 0 
		  AND CONVERT(DATE,TC.LastModificationTime) = @NgayThucHien


	--============================================Xác định danh mục treo cần tính mới
	-- chú ý: dữ liệu đầu vào của các bảng vận hành phải đảm bảo LastmodifiedTime < cast(getdate as date)
    CREATE TABLE #DmTinhMoi_TheoOrder 
	(		 ID INT 
			,HopDongID INT				
			,HopDongChiTietID INT	
			,Order_Id INT
			,DonViTinh NVARCHAR(100)
			,DmNhanHang INT
			,DmWebsiteID INT
			,ChietKhau FLOAT

			,ThanhTienChay FLOAT
			,SoLuongChay FLOAT
			,DonGiaChay FLOAT
			,DuToanMuaSauCK FLOAT 
			,ThanhTienMua FLOAT

			,ThanhTien_DaTinh_Order FLOAT
			,ThanhTien_DaTinh_HDCT FLOAT

			,NganSachOrder FLOAT
			,ThanhTien_HDCT FLOAT
			
			,ThanhTien_GhiNhan_Order FLOAT

			,ThanhTien_GhiNhan FLOAT
			,SoLuong_GhiNhan FLOAT
			,ThanhTienLai FLOAT

			,Type INT -- 1: result_map_order, 2: result_quantity
	)

	INSERT INTO #DmTinhMoi_TheoOrder 
	(		 ID
			,HopDongID 
			,HopDongChiTietID 
			,Order_Id 
			,DonViTinh 
			,DmNhanHang
			,DmWebsiteID
			,ChietKhau 

			,ThanhTienChay
			,SoLuongChay 
			,DuToanMuaSauCK  
			,ThanhTienMua

			,NganSachOrder 
			,ThanhTien_HDCT

			,Type
	)
	SELECT  tc.Id,
			HopDongID = hdct.HopDongFK, 
			HopDongChiTietID = OD.Contract_Detail_Id,
			Order_Id = TC.Operating_Order_Id,
			DonViTinh = IIF(OD.UNITS = '', N'GÓI', OD.UNITS), 
			DmNhanHang = OD.Brand_id,
			DmWebsiteID = OD.DmWebsiteREF,
			hdct.ChietKhau,
					
			ThanhTienChay = ISNULL(TC.Sell_Money_VND,0),
			SoLuongChay = IIF(ISNULL(TC.Result,0) = 0, 1, TC.Result) ,
			0,
			ThanhTienMua = ISNULL(RS.Total_Money_VND, 0),

			NganSachOrder = OD.Money_Turnover ,
			ThanhTien_HDCT = IIF(hdct.KhuyenMai = 100, hdct.SoLuong*hdct.DonGia, hdct.ThanhTien),

			type = 1
	FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result_Map_Order TC
	INNER JOIN ABM_Data_ThucChay.DBO.ADS_Operating_Order OD ON TC.Operating_Order_Id = OD.Id
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK 
	LEFT JOIN ABM_Data_ThucChay.dbo.ADS_Operating_Result RS ON RS.Id = TC.operating_Result_Id
	WHERE isnull(TC.IsCaculatedActual, 0) = 0
			AND TC.IsDeleted = 0
			AND ISNULL(TC.Sell_Money_VND,0) <> 0
			--AND CONVERT(DATE,TC.CreationTime) = @NgayThucHien
			AND CONVERT(DATE,TC.LastModificationTime) = @NgayThucHien
			AND ISNULL(OD.IsDeleted,0) =0

			AND HDCT.DeletedStatus = 0
			AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
			AND hd.TrangThaiHopDong <> 3
			AND hd.DeletedStatus = 0
			AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
			AND ISNULL(TC.Sell_Money_VND,0) > 0 
	UNION
	SELECT  tc.Id,
			HopDongID = hdct.HopDongFK, 
			HopDongChiTietID = OD.Contract_Detail_Id,
			Order_Id = TC.Operating_Order_Id,	
			DonViTinh = IIF(OD.UNITS = '', N'GÓI', OD.UNITS), 
			DmNhanHang = OD.Brand_id,
			DmWebsiteID = OD.DmWebsiteREF,
			hdct.ChietKhau,

			ThanhTienChay = ISNULL(TC.TotalMoney,0),
			SoLuongChay = IIF(ISNULL(TC.Quantity,0) = 0, 1, TC.Quantity) ,
			0,
			ThanhTienMua = ISNULL(RS.ThanhTienMua, 0),

			NganSachOrder = OD.Money_Turnover ,
			ThanhTien_HDCT = IIF(hdct.KhuyenMai = 100, hdct.SoLuong*hdct.DonGia, hdct.ThanhTien),

			type = 2
	FROM ABM_Data_ThucChay.dbo.[ADS_Operating_Result_Quantity] TC
	INNER JOIN ABM_Data_ThucChay.DBO.ADS_Operating_Order OD ON TC.Operating_Order_Id = OD.Id
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON OD.Contract_Detail_Id = hdct.HopDongChiTietID
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK 
	OUTER APPLY (	SELECT ThanhTienMua = SUM(ISNULL(RS.Total_Money_VND, 0))
					FROM ABM_Data_ThucChay.dbo.ADS_Operating_Result RS 
					WHERE RS.Operating_Order_Id = TC.Operating_Order_Id AND 
							RS.Date_result BETWEEN TC.fromdate AND TC.toDate AND 
							RS.IsDeleted = 0) RS
	WHERE TC.Status = 2 
			AND TC.IsCalc_Result_Quantity = 0 
			AND isnull(TC.IsDeleted,0) = 0
			AND ISNULL(TC.TotalMoney,0) <> 0 
			--AND CONVERT(DATE,TC.CreationTime) = @NgayThucHien
			AND CONVERT(DATE,TC.LastModificationTime) = @NgayThucHien
			AND ISNULL(OD.IsDeleted,0) =0 
		  
			AND HDCT.DeletedStatus = 0
			AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
			AND hd.TrangThaiHopDong <> 3
			AND hd.DeletedStatus = 0
			AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)

			AND ISNULL(TC.TotalMoney,0) > 0 



	UPDATE dm
	SET dm.ThanhTien_DaTinh_Order = ISNULL(tcdt.ThanhTien_DaTinh_Order, 0)
	FROM #DmTinhMoi_TheoOrder dm
	OUTER APPLY (SELECT ThanhTien_DaTinh_Order = SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi + tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
	             FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
				 WHERE tcdt.HopDongChiTietREF = dm.hopdongchitietID AND
				       tcdt.DmChienDichREF = dm.Order_Id AND 
					   CAST(tcdt.NgayThucHien AS DATE) <= @NgayThucHien 
				) tcdt

	UPDATE dm
	SET dm.ThanhTien_DaTinh_HDCT = ISNULL(tcdt.ThanhTien_DaTinh_HDCT, 0)
	FROM #DmTinhMoi_TheoOrder dm
	OUTER APPLY (SELECT ThanhTien_DaTinh_HDCT = SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi + tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
	             FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
				 WHERE tcdt.HopDongChiTietREF = dm.hopdongchitietID AND
					   CAST(tcdt.NgayThucHien AS DATE) <= @NgayThucHien 
				) tcdt
	

	UPDATE dm
	SET dm.DonGiaChay = dm.ThanhTienChay/dm.SoLuongChay
	FROM #DmTinhMoi_TheoOrder dm


	--============================================== Xác định thực chạy được ghi nhận và lệch treo hạ
	-- chặn vượt ngân sách
	;WITH CTE_Base AS (
			SELECT  ID,
					TongThucChayTruocDo_Order =  ThanhTien_DaTinh_Order +  
												 COALESCE(	SUM(ThanhTienChay) OVER (
																PARTITION BY Order_Id  
																ORDER BY ID, Type  
																ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
																), 0) ,
					TongThucChayDenHT_Order =   ThanhTien_DaTinh_Order + 
												COALESCE(	SUM(ThanhTienChay) OVER (
															PARTITION BY Order_Id
															ORDER BY ID, Type 
															ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
															), 0)
			FROM #DmTinhMoi_TheoOrder )
  
	UPDATE temp
	SET ThanhTien_GhiNhan_Order =   CASE	WHEN sl.TongThucChayDenHT_Order <= temp.NganSachOrder
											THEN temp.ThanhTienChay
											WHEN sl.TongThucChayDenHT_Order > temp.NganSachOrder AND 
													sl.TongThucChayTruocDo_Order <= temp.NganSachOrder
											THEN temp.NganSachOrder - sl.TongThucChayTruocDo_Order
											WHEN sl.TongThucChayDenHT_Order > temp.NganSachOrder AND 
													sl.TongThucChayTruocDo_Order > temp.NganSachOrder
											THEN 0
									END
	FROM #DmTinhMoi_TheoOrder temp
	INNER JOIN CTE_Base sl ON sl.ID = temp.ID

	-- chặn vượt phân bổ
	;WITH CTE_Base_2 AS (
			SELECT  ID,
					TongThucChayTruocDo_HDCT =  ThanhTien_DaTinh_HDCT + 
												COALESCE(	SUM(ThanhTien_GhiNhan_Order) OVER (
															PARTITION BY HopDongChiTietID  
															ORDER BY Order_Id, ID, Type  
															ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
															), 0) ,
					TongThucChayDenHT_HDCT =    ThanhTien_DaTinh_HDCT + 
												COALESCE(	SUM(ThanhTien_GhiNhan_Order) OVER (
															PARTITION BY HopDongChiTietID  
															ORDER BY Order_Id, ID, Type 
															ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
															), 0)
			FROM #DmTinhMoi_TheoOrder 
			)

	UPDATE temp
	SET ThanhTien_GhiNhan   =       CASE    WHEN sl.TongThucChayDenHT_HDCT <= temp.ThanhTien_HDCT
											THEN temp.ThanhTien_GhiNhan_Order
											WHEN sl.TongThucChayDenHT_HDCT > temp.ThanhTien_HDCT AND 
													sl.TongThucChayTruocDo_HDCT <= temp.ThanhTien_HDCT
											THEN temp.ThanhTien_HDCT - sl.TongThucChayTruocDo_HDCT
											WHEN sl.TongThucChayDenHT_HDCT > temp.ThanhTien_HDCT AND 
													sl.TongThucChayTruocDo_HDCT > temp.ThanhTien_HDCT
											THEN 0
									END
	FROM #DmTinhMoi_TheoOrder temp
	INNER JOIN CTE_Base_2 sl ON sl.ID = temp.ID



	UPDATE dm
	SET dm.SoLuong_GhiNhan = ThanhTien_GhiNhan / DonGiaChay
	FROM #DmTinhMoi_TheoOrder dm

	UPDATE dm
	SET dm.ThanhTienLai = IIF(ChietKhau = 100, ThanhTienChay - ThanhTienMua, ThanhTien_GhiNhan - ThanhTienMua)
	FROM #DmTinhMoi_TheoOrder dm
	
	--===================================================== INSERT Thucchaydatinh và thucchaydatinh_muangoai ==================================

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
	SELECT		ThucChayDaTinhID = NEWID(),
				HopDongID = hd.HopDongID,
				SoHopDong = hd.SoHopDong,
				DmMaHopDongREF = hd.DmMaHopDongREF,
				TenMaHopDong = hd.TenMaHopDong,
				NgayDanhSoHopDong = hd.NgayDanhSoHopDong,
				NgayKyHopDong = hd.NgayKyHopDong,
				NhanHopDong = hd.NhanHopDong,
				NgayNhanBanFax = hd.NgayNhanBanFax,
				NgayNhanHopDongBanCung = hd.NgayNhanHopDongBanCung,
				NgayChuyenHopDongChoKeToan = hd.NgayChuyenHopDongChoKeToan,
				So = hd.So,
				Thang = hd.Thang,
				Nam = hd.Nam,
				GiaTriHopDong = hd.GiaTriHopDong,
				CongNo = hd.CongNo,
				HopDongChiTietREF = hdct.HopDongChiTietID,
				DangSuDung = hd.DangSuDung,
				IsGiayPhep = hd.IsGiayPhep,
				TrangThaiHopDong = 2,
				IsBanCung = hd.IsBanCung,
				DmPhongBanREF = ISNULL(hd.DmPhongBanREF,0),		
				TenPhongBan = ISNULL(HD.TenPhongBan,''),					
				DmBoPhanREF = ISNULL(HD.DmBoPhanREF,0),				
				TenBoPhan = ISNULL(HD.TenBoPhan,'')	,			
				DmNhomLamViecREF = ISNULL(HD.DmNhomLamViecREF,0),				
				TenNhomLamViec = ISNULL(HD.TenNhom,''),				
				DmDiaDiemLamViecREF = HD.DmDiaDiemLamViecREF, 				
				TenDiaDiemLamViec = ISNULL(HD.TenDiaDiemLamViec,''),				
				SysNhanVienREF = HD.SysNhanVienREF,				
				TenDangNhap = HD.TenDangNhap,				
				TenNhanVien = HD.TenNhanVien,				
				TenKhachHang = HD.TenKhachHang,		
				NhanHang = dm.DmNhanHang,
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
				DotChayHopDong = N'Tính mới GGFB' + IIF(dm.Type = 1, N' result_map_order', ' result_quantity'),
				SoLuongDotChayHD = 0,
				DotChayBooking = dm.ID,
				SoLuongDotChayBooking = 0,
				SoLuong = hdct.SoLuong,
				DonViTinh = [dbo].[FormatDonViTinh_ThanhTien_GGFB](dm.DonViTinh),
				DonGia = hdct.DonGia,
				DonGiaTheoDonVi = dm.DonGiaChay,
				ChietKhau = hdct.ChietKhau,
				GiamGia  = HDCT.GiamGia,					
				ThanhTien  = HDCT.ThanhTien,						
				TiLeTuVan   = HDCT.TiLeTuVan,                
				ChiPhiTuVan = HDCT.ChiPhiTuVan,                       
				IsKhuyenMai = HDCT.IsKhuyenMai,                 
				KhuyenMai   = HDCT.KhuyenMai,                     
				DmBannerREF = HDCT.DmBannerREF ,
				DmChienDichREF = dm.Order_Id,
				DmWebsiteREF = w.DmWebsiteReportingdbID,   
				TenWebsite = ISNULL(w.WebsiteLink, N''),  
				TongViewThucChay = 0,
				TongClickThucChay = 0,
				TongSoBaiViet = 0,
				SoLuongThucChay = ROUND(IIF(hdct.ChietKhau = 100, 0, dm.SoLuong_GhiNhan), 0),
				NgayThucHien = @NgayThucHien,
				GiaTriThayDoi = 0,
				ThanhTienThucChayTruocTrietKhau = IIF(hdct.ChietKhau = 100, dm.ThanhTien_GhiNhan, dm.ThanhTien_GhiNhan/(1-hdct.ChietKhau/100)),
				GiaTriTrietKhauThucChay = IIF(hdct.ChietKhau = 100, 0, dm.ThanhTien_GhiNhan*hdct.ChietKhau/(100-hdct.ChietKhau)),
				ThanhTienSauTrietKhauThucChay = IIF(hdct.ChietKhau = 100, 0, dm.ThanhTien_GhiNhan),
				GiaTriHoaHongThucChay = IIF(hdct.ChietKhau = 100, 0, dm.ThanhTien_GhiNhan*hdct.TiLeTuVan/100),
				ThanhTienThucThu = IIF(hdct.ChietKhau = 100, 0, dm.ThanhTien_GhiNhan - dm.ThanhTien_GhiNhan*hdct.TiLeTuVan/100),
				ThanhTienKM = IIF(hdct.ChietKhau = 100, dm.ThanhTien_GhiNhan, 0),
				SoLuongThucChayKM = ROUND(IIF(hdct.ChietKhau = 100, SoLuong_GhiNhan, 0), 0),
				SoLuongThucChayLechTreoHa = ROUND(SoLuongChay - SoLuong_GhiNhan, 0),
				ThanhTienLechTreoHa = IIF(hdct.ChietKhau = 100, ThanhTienChay - ThanhTien_GhiNhan, (ThanhTienChay - ThanhTien_GhiNhan)/(1-hdct.ChietKhau/100)),
				CreatedAt = GETDATE(),
				LastModifiedAt = GETDATE(),
				IsPheDuyet = '',
				PheDuyetBy = '',
				PheDuyetAt = '',
				SoLuongThayDoi = 0,
				SoLuongKMThayDoi = 0,
				GiaTriKMThayDoi = 0,
				GhiChu = IIF(@SoHopDong IS NULL, 
				             N'Tính mới: SP tối ưu [dbo].[ThucChay_GGFB_GhiNhanPhatSinh]', 
				             N'Tính mới: SP tối ưu xử lý tay [dbo].[ThucChay_GGFB_GhiNhanPhatSinh]' )
	FROM #DmTinhMoi_TheoOrder dm
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
	INNER JOIN ABM_Data_ThucChay.dbo.hopDong hd ON hd.HopDongID = hdct.HopDongFK
	OUTER APPLY (SELECT TOP 1 DmWebsiteReportingdbID, WebsiteLink
				 FROM ABM_Data_ThucChay.dbo.WebsiteMapping_HDCN_Reporting w 
				 WHERE w.DmWebsiteID = dm.DmWebsiteID ) w

	INSERT INTO ABM_Data_ThucChay.[dbo].ThucChayDaTinh_MuaNgoai
	(
	    HopDongREF,
	    SoHopDong,
	    DmMaHopDongREF,
	    NgayDanhSoHopDong,
	    TrangThaiHopDong,
	    DmNhanVienREF,
	    TenDangNhap,
	    DmPhongBanREF,
	    DmBoPhanREF,
	    DmNhomLamViecREF,
	    DmDiaDiemLamViecREF,
	    DmKhachHangREF,
	    HopDongChiTietREF,
	    LstDmNhanHangREF,
	    LstDmNhomNganhREF,
	    DmHinhThucQuangCaoREF,
	    DmSanPhamREF,
	    DmChuyenMucREF,
	    DmLoaiBannerREF,
	    DmViTriREF,
	    SoLuong,
	    DonViTinhREF,
	    DonGia,
	    ChietKhau,
	    ThanhTien,
	    IsKhuyenMai,
	    KhuyenMai,
	    ThucChayMuaNgoaiChiTietREF,
	    TongTienDuToanMuaSauCK,
	    TongTienDuToanLaiMuaSauCK,
	    ChietKhauMua,
	    DmBannerREF,
	    DmChienDichREF,
	    DmWebsiteREF,
	    TenWebsite,
	    NgayThucHien,
	    NgayBatDau,
	    NgayKetThuc,
	    DonViTinhThucChay,
	    DonGiaTheoDonViTinhTC,
	    TongViewClickThucChay,
	    TongSoBaiVietChiPhiThucChay,
	    SoLuongThucChay,
	    TongThanhTienThucChayBanSauCK,
	    TongThanhTienThucChayMuaSauCK,
	    ThanhTienLaiThucChaySauCK,
	    ThanhTienLaiThucChayKM,
	    SoLuongThucChayKM,
	    SoLuongThucChayLechTreoHa,
	    ThanhTienLechTreoHa,
	    GiaTriThayDoiLaiSauCK,
	    SoLuongThayDoi,
	    SoLuongKMThayDoi,
	    GiaTriKMLaiThayDoi,
	    GhiChu,
	    CreatedAt,
	    LastModifiedAt
	)
	SELECT  	    HopDongREF = hdct.HopDongFK
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
				   ,[HopDongChiTietREF] = hdct.HopDongChiTietID
				   ,LstDmNhanHangREF = dm.DmNhanHang
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
				   ,ThucChayMuaNgoaiChiTietREF = 0
				   ,TongTienDuToanMuaSauCK = 0
				   ,TongTienDuToanLaiMuaSauCK = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100, 0, HDCT.ThanhTien )  
				   ,ChietKhauMua = 0
				   ,DmBannerREF = hdct.DmBannerREF
				   ,DmChienDichREF = dm.Order_Id
				   ,DmWebsiteREF = w.DmWebsiteReportingdbID  
				   ,TenWebsite = ISNULL(w.WebsiteLink, N'')
				   ,NgayThucHien = @NgayThucHien
				   ,NgayBatDau = NULL
				   ,NgayKetThuc = NULL
				   ,DonViTinhThucChay = [dbo].[FormatDonViTinh_ThanhTien_GGFB](dm.DonViTinh)
				   ,DonGiaTheoDonViTinhTC = dm.DonGiaChay
				   ,TongViewClickThucChay = 0
				   ,TongSoBaiVietChiPhiThucChay = 0
				   ,SoLuongThucChay = IIF (HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100 , 0, ROUND(dm.SoLuong_GhiNhan, 0))
				   ,[TongThanhTienThucChayBanSauCK]  = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100 , 0, dm.ThanhTien_GhiNhan)
				   ,[TongThanhTienThucChayMuaSauCK] = dm.ThanhTienMua
				   ,[ThanhTienLaiThucChaySauCK] =  IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100 , 0, dm.ThanhTienLai)
				   ,ThanhTienLaiThucChayKM = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100, dm.ThanhTienLai, 0)
				   ,SoLuongThucChayKM = IIF(HDCT.IsKhuyenMai = 1 OR HDCT.ChietKhau = 100, ROUND(dm.SoLuong_GhiNhan, 0), 0)
				   ,SoLuongThucChayLechTreoHa = 0
				   ,ThanhTienLechTreoHa =  0					
				   ,[GiaTriThayDoiLaiSauCK] = 0
				   ,[SoLuongThayDoi] = 0
				   ,[SoLuongKMThayDoi] = 0
				   ,[GiaTriKMLaiThayDoi] = 0
				   ,[GhiChu] = 	 IIF(@SoHopDong IS NULL, 
									 N'Tính mới: SP tối ưu [dbo].[ThucChay_GGFB_GhiNhanPhatSinh]', 
									 N'Tính mới: SP tối ưu xử lý tay [dbo].[ThucChay_GGFB_GhiNhanPhatSinh]' )
				   ,[CreatedAt] = GETDATE()
				   ,[LastModifiedAt] = GETDATE()
	FROM #DmTinhMoi_TheoOrder dm
	INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
	OUTER APPLY (SELECT TOP 1 DmWebsiteReportingdbID, WebsiteLink
				 FROM ABM_Data_ThucChay.dbo.WebsiteMapping_HDCN_Reporting w 
				 WHERE w.DmWebsiteID = ISNULL(dm.DmWebsiteID, 265) ) w

	UPDATE TC
	SET IsCaculatedActual = 1
	FROM dbo.[ADS_Operating_Result_Map_Order] TC
	INNER JOIN #DmTinhMoi_TheoOrder dm ON dm.type = 1 AND TC.Id = dm.ID


	UPDATE TC
	SET [IsCalc_Result_Quantity] = 1
	FROM dbo.[ADS_Operating_Result_Quantity] TC
	INNER JOIN #DmTinhMoi_TheoOrder dm ON dm.type = 2 AND TC.Id = dm.ID

	DROP TABLE #DmTinhMoi_TheoOrder
	DROP TABLE #dmIDdatinh

END


```
