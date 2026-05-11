# Stored Procedure: `ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-07 17:18:18.827000
- **Ngày sửa cuối**: 2025-12-22 10:56:59.743000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |
| `@NgayPhatSinh_Tu` | `date(3)` | No |
| `@NgayPhatSinh_Den` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh] 
    @NgayGhiNhan DATE,
	@NgayPhatSinh_Tu DATE,
	@NgayPhatSinh_Den DATE,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

	DECLARE @GhiChu NVARCHAR(MAX)
	SET @GhiChu = N'Tính mới: SP tối ưu [dbo].[ThucChay_NativeAds_GhiNhanPhatSinh_ThucChayDaTinh]' 
	
	IF @SoHopDong IS NOT NULL
	BEGIN 
		SET @GhiChu = @GhiChu + N' xử lý tay'
		SET @NgayDanhSoGioiHan = NULL 
	END 

	DELETE tcdt 
	FROM ABM_Data_ThucChay.dbo.thucchaydatinh tcdt
	WHERE	CONVERT(date,NgayThucHien) = @NgayGhiNhan
			AND DmSanPhamREF IN (821, 5133)
			AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
			AND NOT EXISTS(	SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
							WHERE iv.HopDongChiTietREF = tcdt.HopDongChiTietREF
							ORDER BY iv.HopDongChiTietREF)
			AND DotChayHopDong = N'Tính mới NativeAds'
		    AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
		    AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)

	--======================================= 1. Xác định dữ liệu cần insert ===============================
	CREATE TABLE #DmThucChay  (
	        ID INT IDENTITY(1,1),
			DmSanPhamREF INT, 
			TenSanPham NVARCHAR(100),
			DmWebsiteREF INT, 
			TenWebsite NVARCHAR(MAX),
			DmBannerREF INT, 
			DonViTinh NVARCHAR(100),
		    NgayThucHien DATETIME,
			HopDongChiTietREF INT,
			DmNhanHangREF NVARCHAR(200),

			ChietKhau FLOAT,

			SoLuongThucChay INT,
			SoLuongThucChayKM INT,
			ThanhTienThucChaySauCK FLOAT,
			ThanhTienThucChayKM FLOAT,
			DonGiaSauCK FLOAT,
			DonGiaKM FLOAT,

			ThanhTienSauCKPhanBo FLOAT,
			ThanhTienKMPhanBo FLOAT,

			TTDTPhanBo_TrcNgayThucHien FLOAT,
			TTDT_KM_PhanBo_TrcNgayThucHien FLOAT,
			TTDT_LechTreoHa_PhanBo_TrcNgayThucHien FLOAT,

			SLTC_GhiNhan INT,
			SLTC_KM_GhiNhan INT,
			TTTC_GhiNhan FLOAT,
			TTTC_KM_GhiNhan FLOAT,
			SoLuongLechTreoHa INT,
			ThanhTienLechTreoHa FLOAT)

	INSERT INTO #DmThucChay( 
			DmSanPhamREF , 
			TenSanPham,
			DmWebsiteREF , 
			TenWebsite ,
			DmBannerREF , 
			DonViTinh ,
		    NgayThucHien ,
			HopDongChiTietREF ,
			
			ChietKhau,

			SoLuongThucChay ,
			SoLuongThucChayKM ,
			ThanhTienThucChaySauCK ,
			ThanhTienThucChayKM ,
			DonGiaSauCK,
			DonGiaKM,

			ThanhTienSauCKPhanBo ,
			ThanhTienKMPhanBo  )
	SELECT  tc.DmSanPhamREF,
	        tc.TenSanPham,
			tc.DmWebsiteID,
			tc.TenWebsite,
			tc.DmBannerID,
			tc.DonViTinh,
			@NgayGhiNhan,
			tchdctab.HopDongChiTietREF,

			hdct.ChietKhau,

			SoLuongThucChay = SUM(tc.SoLuongThucChay) * tchdctab.TiLeThucChayHDCTSoVoiBanner/100 ,
			SoLuongThucChayKM = SUM(tc.SoLuongThucChayKM) * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,
			ThanhTienThucChaySauCK = SUM(tc.ThanhTienThucChaySauCK) * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,
			ThanhTienThucChayKM = SUM(tc.ThanhTienThucChayKM) * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,
			DonGiaSauCK = IIF(hdct.ChietKhau <> 100 AND ISNULL(SUM(tc.SoLuongThucChay), 0) <> 0, 
							  SUM(tc.ThanhTienThucChaySauCK)/ SUM(tc.SoLuongThucChay), 0),
			DonGiaKM = IIF(hdct.ChietKhau = 100 AND ISNULL(SUM(tc.SoLuongThucChayKM), 0) <> 0, 
						   SUM(tc.ThanhTienThucChayKM)/ SUM(tc.SoLuongThucChayKM), 0),

			ThanhTienSauCKPhanBo = IIF(hdct.ChietKhau = 100, 0, hdct.ThanhTien),
			ThanhTienKMPhanBo = IIF(hdct.ChietKhau = 100, hdct.DonGia*hdct.SoLuong, 0)
	FROM ABM_Data_ThucChay.dbo.ThucChay_Native_Ads tc
	INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.SoHopDong = tc.SoHopDong
	INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Native_Ads tchdctab ON tchdctab.DmBannerID = CONVERT(NVARCHAR(50),tc.DmBannerID) 
																					  AND tchdctab.DeletedStatus = 0
																					  AND tc.DmSanPhamREF = tchdctab.DmSanPhamID 
																					  AND hd.HopDongID = tchdctab.HopDongREF
    INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	WHERE   hd.TrangThaiHopDong != 3
			AND hd.DeletedStatus = 0
			AND NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) 
			AND  hdct.DonViTinhREF NOT IN  (3, 10) 
			AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
						   WHERE iv.HopDongChiTietREF = tchdctab.HopDongChiTietREF)
			AND CONVERT(DATE,tc.NgayThucHien) BETWEEN @NgayPhatSinh_Tu AND @NgayPhatSinh_Den 
			AND CONVERT(DATE,tc.NgayThucHien) <= @NgayGhiNhan
			AND tc.DmWebsiteID <> 0

			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
			AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
			AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
	GROUP BY	tc.DmSanPhamREF,
				tc.DmWebsiteID,
				tc.TenWebsite,
				tc.DmBannerID,
				tc.DonViTinh,
				CONVERT(DATE,tc.NgayThucHien),
				tchdctab.HopDongChiTietREF,
				tchdctab.TiLeThucChayHDCTSoVoiBanner,
				hdct.ChietKhau, hdct.ThanhTien, hdct.DonGia, hdct.SoLuong, tc.TenSanPham

	UPDATE dm
	SET dm.DmNhanHangREF = ISNULL(tchdct.DmNhanHangREF, '')
	FROM #DmThucChay dm
	OUTER APPLY  (SELECT STUFF ((   SELECT DISTINCT  ',' + tchdct.DmNhanHangREF
									FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
									WHERE DeletedStatus = 0 AND 
										  tchdct.HopDongChiTietREF = dm.HopDongChiTietREF AND 
										  tchdct.DmBannerREF = CONVERT(NVARCHAR(50),dm.DmBannerREF) 
									FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 
									1, 1, '') AS DmNhanHangREF
							) tchdct

	UPDATE temp
	SET temp.TTDTPhanBo_TrcNgayThucHien = ISNULL(tcdt.TTDTPhanBo_TrcNgayThucHien, 0),
		temp.TTDT_KM_PhanBo_TrcNgayThucHien = ISNULL(tcdt.TTDT_KM_PhanBo_TrcNgayThucHien, 0),
		temp.TTDT_LechTreoHa_PhanBo_TrcNgayThucHien = ISNULL(tcdt.TTDT_LechTreoHa_PhanBo_TrcNgayThucHien, 0)
	FROM #DmThucChay temp
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = temp.HopDongChiTietREF
	OUTER APPLY (SELECT HopDongChiTietREF, 
						SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS TTDTPhanBo_TrcNgayThucHien,
						SUM(tcdt.ThanhTienLechTreoHa) AS TTDT_LechTreoHa_PhanBo_TrcNgayThucHien,
						SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS TTDT_KM_PhanBo_TrcNgayThucHien
	             FROM ABM_Data_ThucChay.dbo.thucchaydatinh tcdt
				 WHERE tcdt.NgayThucHien <= @NgayGhiNhan AND
					   tcdt.HopDongChiTietREF = temp.HopDongChiTietREF 
				 GROUP BY tcdt.HopDongChiTietREF ) tcdt



	--=============================================== 2. Xác định lệch treo hạ ==========================
	--;WITH CTE_Base AS (
	--	SELECT 
	--		ID,
	--		HopDongChiTietREF,

	--		SoLuongThucChay ,
	--		SoLuongThucChayKM ,
	--		ThanhTienThucChaySauCK ,
	--		ThanhTienThucChayKM ,
	--		DonGiaSauCK ,
	--		DonGiaKM ,

	--		ChietKhau,

	--		ThanhTienSauCKPhanBo ,
	--		ThanhTienKMPhanBo ,

	--		TTDTPhanBo_TrcNgayThucHien ,
	--		TTDT_KM_PhanBo_TrcNgayThucHien ,
	--		TTDT_LechTreoHa_PhanBo_TrcNgayThucHien ,

	--		SLTC_GhiNhan ,[ThucChay_CPD_Chiphi_PR_Admarket_PBdieuchinh_CPMngay_Mobile_Inventory]
	--		SLTC_KM_GhiNhan ,
	--		TTTC_GhiNhan ,
	--		TTTC_KM_GhiNhan ,
	--		SoLuongLechTreoHa ,
	--		ThanhTienLechTreoHa ,

	--		ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ID) AS RowNum
	--	FROM #DmThucChay
	--  ),
	--  CTE_Recursive AS (
	--	SELECT 
	--		ID,
	--		HopDongChiTietREF,
	--		Chietkhau,

	--		SoLuongThucChay ,
	--		SoLuongThucChayKM ,
	--		ThanhTienThucChaySauCK ,
	--		ThanhTienThucChayKM ,
	--		DonGiaSauCK ,
	--		DonGiaKM ,

	--		ThanhTienSauCKPhanBo ,
	--		ThanhTienKMPhanBo ,

	--		TTDTPhanBo_TrcNgayThucHien ,
	--		TTDT_KM_PhanBo_TrcNgayThucHien ,
	--		TTDT_LechTreoHa_PhanBo_TrcNgayThucHien ,

	--		RowNum,

	--		TichLuyThanhTienGhiNhan = IIF(ChietKhau <> 100, IIF (TTDTPhanBo_TrcNgayThucHien + CTE_Base.ThanhTienThucChaySauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--															 CTE_Base.ThanhTienSauCKPhanBo ,  TTDTPhanBo_TrcNgayThucHien + CTE_Base.ThanhTienThucChaySauCK )
	--													  , TTDTPhanBo_TrcNgayThucHien),
	--		SoLuongThucChayGhiNhan = IIF(ChietKhau <> 100 AND CTE_Base.DonGiaSauCK <> 0, IIF (TTDTPhanBo_TrcNgayThucHien + CTE_Base.ThanhTienThucChaySauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--																						  CTE_Base.ThanhTienSauCKPhanBo - TTDTPhanBo_TrcNgayThucHien,  CTE_Base.ThanhTienThucChaySauCK )/ CTE_Base.DonGiaSauCK
	--																				   , 0),
	--		ThanhTienTCGhiNhan =  IIF(Chietkhau <> 100, IIF (TTDTPhanBo_TrcNgayThucHien + CTE_Base.ThanhTienThucChaySauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--														 CTE_Base.ThanhTienSauCKPhanBo - TTDTPhanBo_TrcNgayThucHien,  CTE_Base.ThanhTienThucChaySauCK )
	--											      , 0),
	--		TichLuyKMGhiNhan = IIF(ChietKhau = 100, IIF (CTE_Base.TTDT_KM_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienThucChayKM>= CTE_Base.ThanhTienKMPhanBo,
	--													 CTE_Base.ThanhTienKMPhanBo ,  CTE_Base.TTDT_KM_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienThucChayKM )
	--											  , CTE_Base.TTDT_KM_PhanBo_TrcNgayThucHien),
	--		SoLuongKMGhiNhan = IIF(ChietKhau = 100 AND CTE_Base.DonGiaKM <> 0, IIF (CTE_Base.TTDT_KM_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienThucChayKM>= CTE_Base.ThanhTienKMPhanBo,
	--																				CTE_Base.ThanhTienKMPhanBo - CTE_Base.TTDT_KM_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienThucChayKM  / CTE_Base.DonGiaKM )
	--																		 , 0),
	--		ThanhTienKMGhiNhan = IIF(ChietKhau = 100, IIF (CTE_Base.TTDT_KM_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienThucChayKM>= CTE_Base.ThanhTienKMPhanBo,
	--													   CTE_Base.ThanhTienKMPhanBo - CTE_Base.TTDT_KM_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienThucChayKM )
	--											    , 0)
	--	FROM CTE_Base
	--	WHERE RowNum = 1

	--	UNION ALL
	--	-- Tính toán đệ quy
	--	SELECT 
	--	    b.ID,
	--	    b.HopDongChiTietREF,
	--		b.Chietkhau,

	--		b.SoLuongThucChay ,
	--		b.SoLuongThucChayKM ,
	--		b.ThanhTienThucChaySauCK ,
	--		b.ThanhTienThucChayKM ,
	--		b.DonGiaSauCK ,
	--		b.DonGiaKM ,

	--		b.ThanhTienSauCKPhanBo ,
	--		b.ThanhTienKMPhanBo ,

	--		b.TTDTPhanBo_TrcNgayThucHien ,
	--		b.TTDT_KM_PhanBo_TrcNgayThucHien ,
	--		b.TTDT_LechTreoHa_PhanBo_TrcNgayThucHien ,

	--		b.RowNum,

	--		TichLuyThanhTienGhiNhan = IIF(b.ChietKhau <> 100, IIF (r.TichLuyThanhTienGhiNhan + b.ThanhTienThucChaySauCK>= b.ThanhTienSauCKPhanBo,
	--															 b.ThanhTienSauCKPhanBo ,  r.TichLuyThanhTienGhiNhan + b.ThanhTienThucChaySauCK )
	--													  , r.TichLuyThanhTienGhiNhan),
	--		SoLuongThucChayGhiNhan = IIF(b.ChietKhau <> 100 AND b.DonGiaSauCK <> 0, IIF (r.TichLuyThanhTienGhiNhan + b.ThanhTienThucChaySauCK>= b.ThanhTienSauCKPhanBo,
	--																				   b.ThanhTienSauCKPhanBo - r.TichLuyThanhTienGhiNhan,  b.ThanhTienThucChaySauCK )/ b.DonGiaSauCK
	--																				   , 0),
	--		ThanhTienTCGhiNhan =  IIF(b.Chietkhau <> 100, IIF (r.TichLuyThanhTienGhiNhan + b.ThanhTienThucChaySauCK>= b.ThanhTienSauCKPhanBo,
	--														 b.ThanhTienSauCKPhanBo - r.TichLuyThanhTienGhiNhan,  b.ThanhTienThucChaySauCK )
	--											      , 0),

	--		TichLuyKMGhiNhan = IIF(b.ChietKhau = 100, IIF (r.TichLuyKMGhiNhan + b.ThanhTienThucChayKM>= b.ThanhTienKMPhanBo,
	--													 b.ThanhTienKMPhanBo ,  r.TichLuyKMGhiNhan + b.ThanhTienThucChayKM )
	--											  , r.TichLuyKMGhiNhan),
	--		SoLuongKMGhiNhan = IIF(b.ChietKhau = 100 AND b.DonGiaKM <> 0, IIF (r.TichLuyKMGhiNhan + b.ThanhTienThucChayKM>= b.ThanhTienKMPhanBo,
	--																		 b.ThanhTienKMPhanBo - r.TichLuyKMGhiNhan ,  b.ThanhTienThucChayKM  / b.DonGiaKM)
	--																  , 0),
	--		ThanhTienKMGhiNhan = IIF(b.ChietKhau = 100, IIF (r.TichLuyKMGhiNhan + b.ThanhTienThucChayKM>= b.ThanhTienKMPhanBo,
	--													   b.ThanhTienKMPhanBo - r.TichLuyKMGhiNhan ,  b.ThanhTienThucChayKM )
	--											    , 0)
	--	FROM CTE_Base b
	--	INNER JOIN CTE_Recursive r
	--			   ON r.HopDongChiTietREF = b.HopDongChiTietREF AND b.RowNum  - 1 = r.RowNum 
			  
	--  )
	--UPDATE temp
	--SET  	SLTC_GhiNhan = sl.SoLuongThucChayGhiNhan,
	--		SLTC_KM_GhiNhan = sl.SoLuongKMGhiNhan,
	--		TTTC_GhiNhan = sl.ThanhTienTCGhiNhan,
	--		TTTC_KM_GhiNhan = sl.ThanhTienKMGhiNhan,
	--		SoLuongLechTreoHa = IIF(temp.ChietKhau = 100, temp.SoLuongThucChayKM, temp.SoLuongThucChay) - IIF(temp.ChietKhau = 100, sl.SoLuongKMGhiNhan, sl.SoLuongThucChayGhiNhan),
	--		ThanhTienLechTreoHa = IIF(temp.ChietKhau = 100, temp.ThanhTienThucChayKM, temp.ThanhTienThucChaySauCK) - IIF(temp.ChietKhau = 100, sl.ThanhTienKMGhiNhan, sl.ThanhTienTCGhiNhan)
	--FROM #DmThucChay temp
	--INNER JOIN CTE_Recursive sl ON sl.ID = temp.ID
	--OPTION (MAXRECURSION 0);


	;WITH CTE_Base AS (
			SELECT  ID,
					TongThucChayTruocDo = IIF(ChietKhau <> 100,
											  TTDTPhanBo_TrcNgayThucHien + TTDT_LechTreoHa_PhanBo_TrcNgayThucHien + 
											  COALESCE(	SUM(ThanhTienThucChaySauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
														), 0),
											  0),
					TongThucChayDenHT =   IIF(ChietKhau <> 100,
											  TTDTPhanBo_TrcNgayThucHien + TTDT_LechTreoHa_PhanBo_TrcNgayThucHien + 
											  COALESCE(	SUM(ThanhTienThucChaySauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
											  0),
					TongThucChayKMTruocDo=  IIF(ChietKhau = 100,
												TTDT_KM_PhanBo_TrcNgayThucHien + TTDT_LechTreoHa_PhanBo_TrcNgayThucHien + 
												COALESCE(	SUM(ThanhTienThucChayKM) OVER (
															PARTITION BY HopDongChiTietREF 
															ORDER BY ID  
															ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
															), 0),
												0),
					TongThucChaKMDenHT =   IIF(ChietKhau = 100,
											   TTDT_KM_PhanBo_TrcNgayThucHien + TTDT_LechTreoHa_PhanBo_TrcNgayThucHien + 
											   COALESCE(SUM(ThanhTienThucChayKM) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
											   0)
			FROM #DmThucChay )
  
	UPDATE temp
	SET  	TTTC_GhiNhan = CASE WHEN sl.TongThucChayTruocDo > ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo
								THEN 0
								WHEN sl.TongThucChayTruocDo > ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT <= ThanhTienSauCKPhanBo
								THEN sl.TongThucChayDenHT - sl.TongThucChayTruocDo
								WHEN sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo
								THEN ThanhTienSauCKPhanBo - sl.TongThucChayTruocDo
								WHEN sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT <= ThanhTienSauCKPhanBo
								THEN temp.ThanhTienThucChaySauCK
							END, 
			TTTC_KM_GhiNhan = CASE	WHEN sl.TongThucChayKMTruocDo > ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo
									THEN 0
									WHEN sl.TongThucChayKMTruocDo > ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT <= ThanhTienKMPhanBo
									THEN sl.TongThucChaKMDenHT - sl.TongThucChayKMTruocDo
									WHEN sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo
									THEN ThanhTienKMPhanBo - sl.TongThucChayKMTruocDo
									WHEN sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT <= ThanhTienKMPhanBo
									THEN temp.ThanhTienThucChayKM
							  END 
	FROM #DmThucChay temp
	INNER JOIN CTE_Base sl ON sl.ID = temp.ID

	UPDATE temp
	SET  	SLTC_GhiNhan = IIF(ChietKhau <> 100, TTTC_GhiNhan/DonGiaSauCK, 0),
			SLTC_KM_GhiNhan = IIF(ChietKhau = 100, TTTC_KM_GhiNhan/DonGiaKM, 0),
			SoLuongLechTreoHa = IIF(ChietKhau = 100, SoLuongThucChayKM - TTTC_KM_GhiNhan/DonGiaKM, SoLuongThucChay - TTTC_GhiNhan/DonGiaSauCK) ,
			ThanhTienLechTreoHa = IIF(ChietKhau = 100, ThanhTienThucChayKM - TTTC_KM_GhiNhan, ThanhTienThucChaySauCK - TTTC_GhiNhan)
	FROM #DmThucChay temp


	--=========================================== 3. INSERT ThucChayDaTinh
	DECLARE @Thucchay_NativeAds_DmTinhMoi DataType_Thucchay_NativeAds_DmTinhMoi


	INSERT INTO @Thucchay_NativeAds_DmTinhMoi
	(
	    DmSanPhamREF ,
		TenSanPham, 
		DmWebsiteREF , 
		TenWebsite ,
		DmBannerREF , 
		DonViTinh ,
		NgayThucHien ,
		HopDongChiTietREF ,
		DmNhanHangREF ,
		DonGiaSauCK ,
		DonGiaKM ,

		SoLuongThucChay,
		SLTC_GhiNhan ,
		SLTC_KM_GhiNhan ,
		TTTC_GhiNhan ,
		TTTC_KM_GhiNhan ,
		SoLuongLechTreoHa ,
		ThanhTienLechTreoHa ,
		GhiChu 
	)
	SELECT 
	    DmSanPhamREF ,
		TenSanPham,
		DmWebsiteREF , 
		TenWebsite ,
		DmBannerREF , 
		DonViTinh ,
		NgayThucHien ,
		HopDongChiTietREF ,
		DmNhanHangREF ,
		DonGiaSauCK ,
		DonGiaKM ,

		SoLuongThucChay,
		SLTC_GhiNhan ,
		SLTC_KM_GhiNhan ,
		TTTC_GhiNhan ,
		TTTC_KM_GhiNhan ,
		SoLuongLechTreoHa ,
		ThanhTienLechTreoHa ,
		@GhiChu 
	FROM #DmThucChay tcgn
	WHERE	SLTC_GhiNhan <> 0 OR
			SLTC_KM_GhiNhan <> 0 OR
			TTTC_GhiNhan <> 0 OR
			TTTC_KM_GhiNhan <> 0 OR
			SoLuongLechTreoHa <> 0 OR
			ThanhTienLechTreoHa <> 0 

	EXEC dbo.ThucChay_NativeAds_Insert_ThucChayDaTinh @Thucchay_NativeAds_DmTinhMoi
		
	DROP TABLE #DmThucChay
	
END

```
