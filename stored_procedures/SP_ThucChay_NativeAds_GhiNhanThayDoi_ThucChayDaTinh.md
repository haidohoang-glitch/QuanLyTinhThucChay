# Stored Procedure: `ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-07 17:17:36.207000
- **Ngày sửa cuối**: 2025-10-24 09:30:24.760000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |
| `@NgayCheckThayDoi` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql


--DECLARE @DmInterger TABLE (ID INT)
CREATE  PROCEDURE [dbo].[ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh]
    @NgayGhiNhan DATE,
    @NgayCheckThayDoi DATE = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

    IF @SoHopDong IS NOT NULL
	BEGIN
		SET @NgayCheckThayDoi = NULL
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
			AND DotChayHopDong IN ( N'Đối trừ NativeAds', N'Tính lại Native Ads')
		    AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
		    AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)

	--========================================= 1. Xác định phân bổ thay đổi tỉ lệ/banner và pb có thay đổi số lượng, đơn giá, chiết khấu ==============================
    CREATE TABLE #DmPBThayDoi (
					NgayThucHien DATETIME,
					HopDongChiTietREF INT,
					LoaiThayDoi INT,     --1: thay đổi thông tin hợp đồng, 2: phân bổ hủy, 3: pb thay đổi tỷ lệ / banner
					LyDo NVARCHAR(MAX),
					PBcothaydoiThanhTien INT      -- xác định là phân bổ có thay đổi thành tiền sau chiết khấu hoặc thành tiền khuyến mại
					)
	BEGIN
		-- phân bổ thay đổi thông tin
        INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo
        )
        SELECT DISTINCT @NgayGhiNhan,
                        hdct.HopDongChiTietID,
						LoaiThayDoi = IIF(hdct.DeletedStatus = 1 OR  hd.TrangThaiHopDong = 3, 2, 1),
						LyDo = CASE WHEN hd.TrangThaiHopDong = 3
									THEN N'hợp đồng hủy'
									WHEN hdct.DeletedStatus = 1
									THEN N'phân bổ bị xóa'
									ELSE N'phân bổ thay đổi thành tiền sau CK hoặc thành tiền khuyến mại'
							   END 
        FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
		WHERE    hdct.DmSanPhamREF IN (821, 5133) AND
				 NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) AND
				 NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
							WHERE iv.HopDongChiTietREF = hdct.HopDongChiTietID ) AND 
				 NOT EXISTS (SELECT top (1) tl.HopDongChiTietID FROM ABM_Data_ThucChay.dbo.GhiNhanThanhLy tl 
							 WHERE tl.HopDongChiTietID = hdct.HopDongChiTietID )
				 AND hdct.DonViTinhREF NOT IN (3,10) 
				 AND (CONVERT(DATE, hd.LastModifiedAt) =  @NgayCheckThayDoi OR CONVERT(DATE, hdct.LastModifiedAt) =  @NgayCheckThayDoi)   
			     AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
			 

		-- loại TH phân bổ có thay đổi thông tin nhưng không thay đổi thành tiền đánh số
		DELETE dm
		FROM #DmPBThayDoi dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietREF
		OUTER APPLY (SELECT TOP 1 l.SoLuong , l.DonGia, l.ChietKhau
					 FROM ABM_Data_ThucChay.dbo.HopDongChiTietLog l 
					 WHERE LastModifiedAt < @NgayCheckThayDoi AND 
						   l.HopDongChiTietREF = dm.HopDongChiTietREF
					 ORDER BY HopDongChiTietLogID desc ) l 
		WHERE hdct.soluong*hdct.DonGia = ISNULL(l.SoLuong, hdct.SoLuong)*ISNULL(l.DonGia, hdct.DonGia) AND 
		      dm.LoaiThayDoi = 1 AND
			  hdct.ChietKhau = ISNULL(l.ChietKhau, hdct.ChietKhau)


		-- phân bổ bị ảnh hưởng tỉ lệ hopdongchitiet/banner do phân bổ phía trên thay đổi
		INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo )
		SELECT DISTINCT
			   @NgayGhiNhan,
			   tchdctab.HopDongChiTietREF,
			   LoaiThayDoi = 3,
			   LyDo = N'tỉ lệ phân bổ trên banner thay đổi'
		FROM ( SELECT tchdctab.DmBannerID
			   FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Native_Ads tchdctab
			   WHERE EXISTS (SELECT HopDongChiTietREF 
							 FROM #DmPBThayDoi dm 
							 WHERE dm.HopDongChiTietREF = tchdctab.HopDongChiTietREF ) 
					 AND DaThucHienUpdateTiLe = 1 ) b
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Native_Ads tchdctab ON b.DmBannerID = tchdctab.DmBannerID 
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = tchdctab.HopDongREF
		WHERE tchdctab.HopDongChiTietREF NOT IN (SELECT HopDongChiTietREF FROM #DmPBThayDoi dm )
		     AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
			 AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
						    WHERE iv.HopDongChiTietREF = tchdctab.HopDongChiTietREF )  
			 AND NOT EXISTS (SELECT top (1) tl.HopDongChiTietID FROM ABM_Data_ThucChay.dbo.GhiNhanThanhLy tl 
						     WHERE tl.HopDongChiTietID = tchdctab.HopDongChiTietREF )

		IF @SoHopDong IS NOT NULL
		BEGIN
			INSERT INTO #DmPBThayDoi
			(				NgayThucHien,
							HopDongChiTietREF,
							LoaiThayDoi,
							LyDo )
			SELECT DISTINCT @NgayGhiNhan,
							hdct.HopDongChiTietID,
							LoaiThayDoi = IIF(hdct.DeletedStatus = 1 OR  hd.TrangThaiHopDong = 3, 2, 1),
							LyDo = CASE WHEN hd.TrangThaiHopDong = 3
										THEN N'xử lý tay hợp đồng hủy'
										WHEN hdct.DeletedStatus = 1
										THEN N'xử lý tay phân bổ bị xóa'
										ELSE N'xử lý tay phân bổ'
							END 
			FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
			WHERE   hdct.DmSanPhamREF IN (821, 5133) AND
					NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) AND
					NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
							WHERE iv.HopDongChiTietREF = hdct.HopDongChiTietID ) AND 
					NOT EXISTS (SELECT top (1) tl.HopDongChiTietID FROM ABM_Data_ThucChay.dbo.GhiNhanThanhLy tl 
								WHERE tl.HopDongChiTietID = hdct.HopDongChiTietID )
					AND hdct.DonViTinhREF NOT IN (3,10) --HAIDH COMMENT BO DONVITINH GOI RA KHOI DIEU KIEN
					AND hd.SoHopDong = @SoHopDong
					AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
		END

	END	
     
	--========================================= 2. Xác định thucchayID của các phân bổ trên ====================================================================================================================
	CREATE TABLE #DmTinhLai 
				(	ID INT IDENTITY(1,1),

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

					SLTC_GhiNhan INT,
					SLTC_KM_GhiNhan INT,
					TTTC_GhiNhan FLOAT,
					TTTC_KM_GhiNhan FLOAT,
					SoLuongLechTreoHa INT,
					ThanhTienLechTreoHa FLOAT,

					LyDo NVARCHAR(MAX))
	INSERT INTO #DmTinhLai
			(		DmSanPhamREF , 
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
	SELECT			tc.DmSanPhamREF,
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
	INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tchdctab.HopDongChiTietREF
	WHERE   hd.TrangThaiHopDong != 3
			AND hd.DeletedStatus = 0
			AND NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) 
			AND  hdct.DonViTinhREF <> 3
			AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
						   WHERE iv.HopDongChiTietREF = tchdctab.HopDongChiTietREF)
		    AND dm.LoaiThayDoi IN (1,3)
			AND CONVERT(DATE,tc.NgayThucHien) < @NgayGhiNhan 
			AND tc.DmWebsiteID <> 0
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
	FROM #DmTinhLai dm
	OUTER APPLY  (SELECT STUFF ((   SELECT DISTINCT  ',' + tchdct.DmNhanHangREF
									FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
									WHERE DeletedStatus = 0 AND 
										  tchdct.HopDongChiTietREF = dm.HopDongChiTietREF AND 
										  tchdct.DmBannerREF = CONVERT(NVARCHAR(50),dm.DmBannerREF) 
									FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 
									1, 1, '') AS DmNhanHangREF
							) tchdct



	--========================================= 3. Xác định lệch treo hạ và ghi nhận của các thucchayID trên ==========================
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

	--		SLTC_GhiNhan ,
	--		SLTC_KM_GhiNhan ,
	--		TTTC_GhiNhan ,
	--		TTTC_KM_GhiNhan ,
	--		SoLuongLechTreoHa ,
	--		ThanhTienLechTreoHa ,

	--		ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ID) AS RowNum
	--	FROM #DmTinhLai
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

	--		RowNum,

	--		TichLuyThanhTienGhiNhan = IIF(ChietKhau <> 100, IIF (CTE_Base.ThanhTienThucChaySauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--															 CTE_Base.ThanhTienSauCKPhanBo ,  CTE_Base.ThanhTienThucChaySauCK )
	--													  , 0),
	--		SoLuongThucChayGhiNhan = IIF(ChietKhau <> 100 AND CTE_Base.DonGiaSauCK <> 0, IIF (CTE_Base.ThanhTienThucChaySauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--																						  CTE_Base.ThanhTienSauCKPhanBo,  CTE_Base.ThanhTienThucChaySauCK )/ CTE_Base.DonGiaSauCK
	--																				   , 0),
	--		ThanhTienTCGhiNhan =  IIF(Chietkhau <> 100, IIF (CTE_Base.ThanhTienThucChaySauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--														 CTE_Base.ThanhTienSauCKPhanBo,  CTE_Base.ThanhTienThucChaySauCK )
	--											      , 0),
	--		TichLuyKMGhiNhan = IIF(ChietKhau = 100, IIF (CTE_Base.ThanhTienThucChayKM>= CTE_Base.ThanhTienKMPhanBo,
	--													 CTE_Base.ThanhTienKMPhanBo ,  CTE_Base.ThanhTienThucChayKM )
	--											  , 0),
	--		SoLuongKMGhiNhan = IIF(ChietKhau = 100 AND CTE_Base.DonGiaKM <> 0, IIF (CTE_Base.ThanhTienThucChayKM>= CTE_Base.ThanhTienKMPhanBo,
	--																				CTE_Base.ThanhTienKMPhanBo,  CTE_Base.ThanhTienThucChayKM  / CTE_Base.DonGiaKM )
	--																		 , 0),
	--		ThanhTienKMGhiNhan = IIF(ChietKhau = 100, IIF (CTE_Base.ThanhTienThucChayKM>= CTE_Base.ThanhTienKMPhanBo,
	--													   CTE_Base.ThanhTienKMPhanBo ,  CTE_Base.ThanhTienThucChayKM )
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
	--FROM #DmTinhLai temp
	--INNER JOIN CTE_Recursive sl ON sl.ID = temp.ID
	--OPTION (MAXRECURSION 0);


	;WITH CTE_Base AS (
			SELECT  ID,
					TongThucChayTruocDo = IIF(ChietKhau <> 100,
											  COALESCE(	SUM(ThanhTienThucChaySauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
														), 0),
											  0),
					TongThucChayDenHT =   IIF(ChietKhau <> 100,
											  COALESCE(	SUM(ThanhTienThucChaySauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
											  0),
					TongThucChayKMTruocDo=  IIF(ChietKhau = 100,
												COALESCE(	SUM(ThanhTienThucChayKM) OVER (
															PARTITION BY HopDongChiTietREF 
															ORDER BY ID  
															ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
															), 0),
												0),
					TongThucChaKMDenHT =   IIF(ChietKhau = 100,
											   COALESCE(SUM(ThanhTienThucChayKM) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
											   0)
			FROM #DmTinhLai )
  
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
	FROM #DmTinhLai temp
	INNER JOIN CTE_Base sl ON sl.ID = temp.ID

	UPDATE temp
	SET  	SLTC_GhiNhan = IIF(ChietKhau <> 100, TTTC_GhiNhan/DonGiaSauCK, 0),
			SLTC_KM_GhiNhan = IIF(ChietKhau = 100, TTTC_KM_GhiNhan/DonGiaKM, 0),
			SoLuongLechTreoHa = IIF(ChietKhau = 100, SoLuongThucChayKM - TTTC_KM_GhiNhan/DonGiaKM, SoLuongThucChay - TTTC_GhiNhan/DonGiaSauCK) ,
			ThanhTienLechTreoHa = IIF(ChietKhau = 100, ThanhTienThucChayKM - TTTC_KM_GhiNhan, ThanhTienThucChaySauCK - TTTC_GhiNhan)
	FROM #DmTinhLai temp

	--========================================= 4. Tiến hành đối trừ phân bổ xóa, hủy ===========================================================
	INSERT INTO ABM_Data_ThucChay.dbo.thucchaydatinh
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
SELECT	  NEWID()
		, tcdt.HopDongID
		, SoHopDong
		, DmMaHopDongREF
		, TenMaHopDong
		, NgayDanhSoHopDong
		, NgayKyHopDong
		, NhanHopDong
		, NgayNhanBanFax
		, NgayNhanHopDongBanCung
		, NgayChuyenHopDongChoKeToan
		, So
		, Thang
		, Nam
		, GiaTriHopDong
		, CongNo
		, tcdt.HopDongChiTietREF
		, DangSuDung
		, IsGiayPhep
		, TrangThaiHopDong
		, IsBanCung
		, DmPhongBanREF
		, TenPhongBan
		, DmBoPhanREF
		, TenBoPhan
		, DmNhomLamViecREF
		, TenNhomLamViec
		, DmDiaDiemLamViecREF
		, TenDiaDiemLamViec
		, SysNhanVienREF
		, TenDangNhap
		, TenNhanVien
		, TenKhachHang
		, NhanHang
		, DmNhomNganhREF
		, TenNhomNganh
		, DmHinhThucQuangCao
		, TenHinhThucQuangCao
		, DmSanPhamREF
		, TenSanPham
		, DmNhomWebsiteREF
		, TenNhomWebsite
		, DmChuyenMucREF
		, TenChuyenMuc
		, DmLoaiBannerREF
		, TenLoaiBanner
		, DmViTriREF
		, TenViTri
		, N'Đối trừ NativeAds' AS DotChayHopDong
		, 0 AS SoLuongDotChayHD
		, '' AS DotChayBooking
		, 0 AS SoLuongDotChayBooking
		, SoLuong
		, DonViTinh
		, DonGia
		, DonGiaTheoDonVi
		, ChietKhau
		, GiamGia
		, ThanhTien
		, TiLeTuVan
		, ChiPhiTuVan
		, IsKhuyenMai
		, KhuyenMai
		, DmBannerREF
		, DmChienDichREF
		, DmWebsiteREF
		, TenWebsite
		, 0 TongViewThucChay
		, 0 TongClickThucChay
		, 0 TongSoBaiViet
		, 0 AS SoLuongThucChay
		, @NgayGhiNhan
		, -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi
		, 0 AS ThanhTienThucChayTruocTrietKhau
		, 0 AS GiaTriTrietKhauThucChay
		, 0 AS ThanhTienSauTrietKhauThucChay
		, 0 AS GiaTriHoaHongThucChay
		, 0 AS ThanhTienThucThu
		, 0 AS ThanhTienKM
		, 0 AS SoLuongThucChayKM
		, -SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa
		, -SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
		, GETDATE()
		, GETDATE()
		, 0 AS IsPheDuyet
		, '' AS PheDuyetBy
		, GETDATE() PheDuyetAt
		, -SUM(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi
		, -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi
		, -SUM(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi
		, N'Đối trừ: SP tối ưu [dbo].[ThucChay_NativeAds_GhiNhanThayDoi_ThucChayDaTinh] do ' + dm.LyDo AS GhiChu
FROM    ABM_Data_ThucChay.dbo.thucchaydatinh tcdt
INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tcdt.HopDongChiTietREF 
WHERE   DmSanPhamREF IN (821, 5133)
		AND NOT ( DmLoaiBannerREF IN ( 17, 18 ) OR DmHinhThucQuangCao IN ( 13, 42 ))
		AND tcdt.NgayThucHien < @NgayGhiNhan
GROUP BY  tcdt.HopDongID
		, SoHopDong
		, DmMaHopDongREF
		, TenMaHopDong
		, NgayDanhSoHopDong
		, NgayKyHopDong
		, NhanHopDong
		, NgayNhanBanFax
		, NgayNhanHopDongBanCung
		, NgayChuyenHopDongChoKeToan
		, So
		, Thang
		, Nam
		, GiaTriHopDong
		, CongNo
		, tcdt.HopDongChiTietREF
		, DangSuDung
		, IsGiayPhep
		, TrangThaiHopDong
		, IsBanCung
		, DmPhongBanREF
		, TenPhongBan
		, DmBoPhanREF
		, TenBoPhan
		, DmNhomLamViecREF
		, TenNhomLamViec
		, DmDiaDiemLamViecREF
		, TenDiaDiemLamViec
		, SysNhanVienREF
		, TenDangNhap
		, TenNhanVien
		, TenKhachHang
		, NhanHang
		, DmNhomNganhREF
		, TenNhomNganh
		, DmHinhThucQuangCao
		, TenHinhThucQuangCao
		, DmSanPhamREF
		, TenSanPham
		, DmNhomWebsiteREF
		, TenNhomWebsite
		, DmChuyenMucREF
		, TenChuyenMuc
		, DmLoaiBannerREF
		, TenLoaiBanner
		, DmViTriREF
		, TenViTri
		, SoLuong
		, DonViTinh
		, DonGia
		, DonGiaTheoDonVi
		, ChietKhau
		, GiamGia
		, ThanhTien
		, TiLeTuVan
		, ChiPhiTuVan
		, IsKhuyenMai
		, KhuyenMai
		, DmBannerREF
		, DmChienDichREF
		, DmWebsiteREF
		, TenWebsite
		, dm.NgayThucHien
		, dm.LyDo

	--========================================= 5. Tiến hành tính thay đổi
	DECLARE @Thucchay_NativeAds_DmTinhlai DataType_Thucchay_NativeAds_DmTinhlai
	INSERT INTO @Thucchay_NativeAds_DmTinhlai
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

		SLTC_GhiNhan ,
		SLTC_KM_GhiNhan ,
		TTTC_GhiNhan ,
		TTTC_KM_GhiNhan ,
		SoLuongLechTreoHa ,
		ThanhTienLechTreoHa ,

		LyDo
	)
	SELECT		tcgn.DmSanPhamREF ,
				tcgn.TenSanPham,
				tcgn.DmWebsiteREF , 
				tcgn.TenWebsite ,
				tcgn.DmBannerREF , 
				tcgn.DonViTinh ,
				tcgn.NgayThucHien ,
				tcgn.HopDongChiTietREF ,
				tcgn.DmNhanHangREF ,
				tcgn.DonGiaSauCK ,
				tcgn.DonGiaKM ,

				SLTC_GhiNhan = SUM(SLTC_GhiNhan),
				SLTC_KM_GhiNhan = SUM(SLTC_KM_GhiNhan) ,
				TTTC_GhiNhan = SUM(TTTC_GhiNhan) ,
				TTTC_KM_GhiNhan = SUM(TTTC_KM_GhiNhan) ,
				SoLuongLechTreoHa = SUM(SoLuongLechTreoHa) ,
				ThanhTienLechTreoHa = SUM(ThanhTienLechTreoHa) ,
				tcgn.LyDo
	FROM #DmTinhLai tcgn
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcgn.HopDongChiTietREF
	GROUP BY	tcgn.DmSanPhamREF ,
				tcgn.TenSanPham,
				tcgn.DmWebsiteREF , 
				tcgn.TenWebsite ,
				tcgn.DmBannerREF , 
				tcgn.DonViTinh ,
				tcgn.NgayThucHien ,
				tcgn.HopDongChiTietREF ,
				tcgn.DmNhanHangREF ,
				tcgn.DonGiaSauCK ,
				tcgn.DonGiaKM ,
				tcgn.LyDo

	EXEC [dbo].[ThucChay_NativeAds_DoiTruTinhLai_ThucChayDaTinh] @Thucchay_NativeAds_DmTinhlai

	DROP TABLE #DmTinhLai
	DROP TABLE #DmPBThayDoi

END

```
