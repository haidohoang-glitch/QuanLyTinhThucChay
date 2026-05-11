# Stored Procedure: `ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh_BK20250825`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-08-25 14:52:04.420000
- **Ngày sửa cuối**: 2025-08-25 14:52:04.420000

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



CREATE PROCEDURE [dbo].[ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh_BK20250825] 
    @NgayGhiNhan DATE,
	@NgayPhatSinh_Tu DATE,
	@NgayPhatSinh_Den DATE,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

	DECLARE @GhiChu NVARCHAR(MAX)
	SET @GhiChu = N'Tính mới: SP tối ưu [dbo].[ThucChay_CPMDonViGoi_GhiNhanPhatSinh_ThucChayDaTinh]' + IIF(@SoHopDong IS NOT NULL, N' xử lý tay', N'')

	DELETE FROM ABM_Data_ThucChay.dbo.thucchaydatinh
	WHERE	convert(date,NgayThucHien) = @NgayGhiNhan
			AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
			AND DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299, 821, 5133)
			AND DotChayHopDong = N'Tính mới CPM DonViGoi'
		    AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
		    AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)

	--======================================= 1. Xác định dữ liệu cần insert ===============================
	CREATE TABLE #DmThucChay  ( 
			ID INT IDENTITY(1,1),
			DmWebsiteREF INT,
			TenWebsite NVARCHAR(MAX),
			DmBannerREF INT,
		    NgayThucHien DATETIME,
			HopDongChiTietREF INT,
			DonViTinh NVARCHAR(100),
			DonGiaSauCK FLOAT,
			DonGiaKM FLOAT,
			DmSanPhamREF INT,
			DmNhanHangREF NVARCHAR(200),

			ChietKhau FLOAT,

			SoLuongThucChay INT,
			ThanhTienSauCK FLOAT,
			SoLuongKM INT,
			ThanhTienKM FLOAT,

			ThanhTienSauCKPhanBo FLOAT,
			ThanhTienKMPhanBo FLOAT,
			ThanhTien_TCDT_PhanBo_TrcNgayThucHien FLOAT,
			ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien FLOAT,
			ThanhTien_LechTreoHa_PhanBo_TrcNgayThucHien FLOAT,

			SoLuongThucChay_GhiNhan INT,
			SoLuongLechTreoHa INT,
			SoLuongKM_GhiNhan INT,
			ThanhTienTC_GhiNhan FLOAT,
			ThanhTienLechTreoHa FLOAT,
			ThanhTienKM_GhiNhan FLOAT)

	INSERT INTO #DmThucChay( 
			DmWebsiteREF ,
			TenWebsite ,
			DmBannerREF ,
		    NgayThucHien ,
			HopDongChiTietREF ,
			DonViTinh ,
			DmSanPhamREF ,
			DmNhanHangREF,
			SoLuongThucChay ,
			ThanhTienSauCK ,
			SoLuongKM ,
			ThanhTienKM,
			ChietKhau)
	SELECT  tc.SiteID,
			tc.SiteName,
			tc.bannerid,
			@NgayGhiNhan,
			tchdct.HopDongChiTietID,
			tchdct.DmDonvitinhREF,
			tc.DmSanPhamREF,
			tchdct.DanhSachNhanHangREF,
			SoLuongThucChay = ISNULL(IIF(tchdct.ChietKhau <> 100, tc.True_View, 0),0),
			ThanhTienSauCK = ISNULL(IIF(tchdct.ChietKhau <> 100, tc.True_View*tchdct.DonGia*(100-tchdct.ChietKhau)/100, 0),0),
			SoLuongKM = ISNULL(IIF(tchdct.ChietKhau = 100, tc.True_View, 0),0),
			ThanhTienKM = ISNULL(IIF(tchdct.ChietKhau = 100, tc.True_View*tchdct.DonGia, 0),0),
			tchdct.ChietKhau
	FROM ABM_Data_ThucChay.dbo.ThucChayTrueView tc
	INNER JOIN ( SELECT DISTINCT 
						tchdct.DmSanPhamREF, tchdct.DmBannerREF,
	                    hd.NgayDanhSoHopDong,hd.SoHopDong, 
						DmDonvitinhREF = (CASE WHEN tchdct.DmDonViTinhREF =1 THEN N'VIEW'
											   WHEN tchdct.DmDonViTinhREF =2 THEN N'CLICK'
											   WHEN tchdct.DmDonViTinhREF =32 THEN N'TRUE VIEW'
										       ELSE ''
										  END),
					    hdct.ChietKhau,
						hdct.HopDongChiTietID,
						dongia =  IIF( tchdct.DmDonViTinhREF = 1, tchdct.DonGia/1000, tchdct.DonGia),
						hdct.DanhSachNhanHangREF
	             FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
				 INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
				 INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
				 WHERE hd.TrangThaiHopDong != 3 AND 
				       hd.DeletedStatus = 0 AND 
					   hdct.DeletedStatus = 0 AND 
					   tchdct.DeletedStatus = 0 AND 
					   tchdct.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299) AND 
					   tchdct.DmHinhThucQuangCaoREF NOT IN (42,13) AND 
					   tchdct.DmDonViTinhREF IN (1,2,32) AND 
					   tchdct.CreatedAt >= '2021-03-01' AND 
					   hdct.DmSanPhamREF IN (339, 240, 598, 5056, 733, 5299) AND 
					   NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF = 18 ) AND 
					   hdct.DonViTinhREF = 10 AND
					   (@SoHopDong IS NULL OR hd.SoHopDong= @SoHopDong) AND
                       (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
                ) tchdct ON	tc.bannerid = CONVERT(NVARCHAR(50),tchdct.DmBannerREF) 
								AND tc.DmSanPhamREF = tchdct.DmSanPhamREF 
								AND tc.SoHopDong = tchdct.SoHopDong
	WHERE   (@NgayDanhSoGioiHan IS NULL OR tchdct.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
			AND CONVERT(DATE,tc.NgayThucHien) BETWEEN @NgayPhatSinh_Tu AND @NgayPhatSinh_Den
			AND tc.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
			AND tchdct.DmDonvitinhREF = N'TRUE VIEW'
	UNION ALL
	SELECT  tc.DmWebsiteREF,
			tc.TenWebsite,
			tc.DmBannerREF,
			@NgayGhiNhan,
			tchdct.HopDongChiTietID,
			tchdct.DmDonvitinhREF,
			tc.DmSanPhamREF,
			tchdct.DanhSachNhanHangREF,
			SoLuongThucChay = ISNULL(IIF(tchdct.ChietKhau <> 100, 
									     IIF(tchdct.DmDonvitinhREF = N'VIEW',tc.TongViewThucChay, tc.TongClickThucChay), 
										 0),0),
			ThanhTienSauCK = ISNULL(IIF(tchdct.ChietKhau <> 100, 
			                            IIF(tchdct.DmDonvitinhREF = N'VIEW',tc.TongViewThucChay, tc.TongClickThucChay)*tchdct.DonGia*(100-tchdct.ChietKhau)/100, 
										0),0),
			SoLuongKM = ISNULL(IIF(tchdct.ChietKhau = 100, 
			                       IIF(tchdct.DmDonvitinhREF = N'VIEW',tc.TongViewThucChay, tc.TongClickThucChay), 
								   0),0),
			ThanhTienKM = ISNULL(IIF(tchdct.ChietKhau = 100, 
			                         IIF(tchdct.DmDonvitinhREF = N'VIEW',tc.TongViewThucChay, tc.TongClickThucChay)*tchdct.DonGia, 
									 0),0),
			tchdct.ChietKhau
	FROM ABM_Data_ThucChay.dbo.ThucChay tc
	INNER JOIN ( SELECT DISTINCT
						tchdct.DmSanPhamREF, tchdct.DmBannerREF,
	                    hd.NgayDanhSoHopDong,hd.SoHopDong, 
						DmDonvitinhREF = (CASE WHEN tchdct.DmDonViTinhREF =1 THEN N'VIEW'
											   WHEN tchdct.DmDonViTinhREF =2 THEN N'CLICK'
											   WHEN tchdct.DmDonViTinhREF =32 THEN N'TRUE VIEW'
										       ELSE ''
										  END),
					    hdct.ChietKhau,
						hdct.HopDongChiTietID,
						dongia =  IIF( tchdct.DmDonViTinhREF = 1, tchdct.DonGia/1000, tchdct.DonGia),
						hdct.DanhSachNhanHangREF
	             FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
				 
				 INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
				 INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
				 WHERE hd.TrangThaiHopDong != 3 AND 
				       hd.DeletedStatus = 0 AND 
					   hdct.DeletedStatus = 0 AND 
					   tchdct.DeletedStatus = 0 AND 
					   tchdct.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299) AND 
					   tchdct.DmHinhThucQuangCaoREF not IN (42,13) AND 
					   tchdct.DmDonViTinhREF IN (1,2,32) AND 
					   tchdct.CreatedAt >= '2021-03-01' AND 
					   hdct.DmSanPhamREF IN (339, 240, 598, 5056, 733, 5299) AND 
					   NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF = 18 ) AND 
					   hdct.DonViTinhREF = 10 AND
                       (@SoHopDong IS NULL OR hd.SoHopDong= @SoHopDong) AND
                       (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
                ) tchdct ON	tc.DmBannerREF = CONVERT(NVARCHAR(50),tchdct.DmBannerREF) 
								AND tc.DmSanPhamREF = tchdct.DmSanPhamREF 
								AND tc.SoHopDong = tchdct.SoHopDong
	WHERE (@NgayDanhSoGioiHan IS NULL OR tchdct.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
		  AND CONVERT(DATE,tc.NgayThucHien) BETWEEN @NgayPhatSinh_Tu AND @NgayPhatSinh_Den
		  AND tc.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
		  AND tchdct.DmDonvitinhREF IN (N'VIEW', N'CLICK')

	UNION ALL
	SELECT  tc.DmWebsiteID,
	        tc.TenWebsite,
			tc.DmBannerID,
			CONVERT(DATE,tc.NgayThucHien),
			tchdctab.HopDongChiTietREF,
			tc.DonViTinh,
	        tc.DmSanPhamREF,
			-1,
			SoLuongThucChay = SUM(tc.SoLuongThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100 ),
			ThanhTienSauCK = SUM(tc.ThanhTienThucChaySauCK * tchdctab.TiLeThucChayHDCTSoVoiBanner/100 ),
			SoLuongThucChayKM = SUM(tc.SoLuongThucChayKM * tchdctab.TiLeThucChayHDCTSoVoiBanner/100),
			ThanhTienThucChayKM = SUM(tc.ThanhTienThucChayKM * tchdctab.TiLeThucChayHDCTSoVoiBanner/100),

			hdct.ChietKhau
	FROM ABM_Data_ThucChay.dbo.ThucChay_Native_Ads tc
	INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.SoHopDong = tc.SoHopDong
	INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Native_Ads tchdctab ON tchdctab.DmBannerID = CONVERT(NVARCHAR(50),tc.DmBannerID) 
																					  AND tchdctab.DeletedStatus = 0
																					  AND tc.DmSanPhamREF = tchdctab.DmSanPhamID 
																					  AND hd.HopDongID = tchdctab.HopDongREF
																					  AND tchdctab.DaThucHienUpdateTiLe = 1
    INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	WHERE   hd.TrangThaiHopDong != 3
			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
			AND hd.DeletedStatus = 0
			AND NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) 
			AND  hdct.DonViTinhREF = 10
			AND CONVERT(DATE,tc.NgayThucHien) BETWEEN @NgayPhatSinh_Tu AND @NgayPhatSinh_Den
			AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
						   WHERE iv.HopDongChiTietREF = tchdctab.HopDongChiTietREF)
			AND tc.DmWebsiteID <> 0
		    AND (@SoHopDong IS NULL OR hd.SoHopDong= @SoHopDong) 
            AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
	GROUP BY	tc.DmSanPhamREF,
				tc.DmWebsiteID,
				tc.TenWebsite,
				tc.DmBannerID,
				tc.DonViTinh,
				CONVERT(DATE,tc.NgayThucHien),
				tchdctab.HopDongChiTietREF,
				hdct.ChietKhau
	
	--2025-08-22 HAIDH COMMENT: THEM VIEC TINH CHO NHOM NHIEU SAN PHAM CHẠY GOI LÀ KINGSIZE HOAC SPONSORPAGE DONVI BAI 
	UNION ALL
	SELECT 
	BAI.DmWebsiteREF ,
			BAI.TenWebsite ,
			0 DmBannerREF ,
		    CONVERT(DATE,BAI.LastModifiedAt) NgayThucHien ,
			BAI.HopDongChiTietREF ,
			BAI.DmDonvitinhREF ,
			BAI.DmSanPhamREF ,
			BAI.DanhSachNhanHangREF DmNhanHangREF,
			SoLuongThucChay = ISNULL(IIF(BAI.ChietKhau <> 100, 
									     BAI.SoLuongThucChay, 
										 0),0),
			ThanhTienSauCK = ISNULL(IIF(BAI.ChietKhau <> 100, 
			                            BAI.DonGia*(100-BAI.ChietKhau)/100, 
										0),0),
			SoLuongKM = ISNULL(IIF(BAI.ChietKhau = 100, 
			                       BAI.SoLuongThucChay, 
								   0),0),
			ThanhTienKM = ISNULL(IIF(BAI.ChietKhau = 100, 
			                         BAI.DonGia, 
									 0),0),
			BAI.ChietKhau
	FROM (
	SELECT tchdct.ThucChayHopDongChiTietID, tchdct.HopDongChiTietREF, tchdct.DmWebsiteREF, tchdct.TenWebsite,
						tchdct.DmSanPhamREF, tchdct.SoLuongThucChay,
	                    hd.NgayDanhSoHopDong,hd.SoHopDong, 
						DmDonvitinhREF = (CASE WHEN tchdct.DmDonViTinhREF =1 THEN N'VIEW'
											   WHEN tchdct.DmDonViTinhREF =2 THEN N'CLICK'
											   WHEN tchdct.DmDonViTinhREF =32 THEN N'TRUE VIEW'
										       ELSE N'BÀI'
										  END),
					    hdct.ChietKhau,
						hdct.HopDongChiTietID,
						tchdct.DonGia,
						hdct.DanhSachNhanHangREF, tchdct.LastModifiedAt
	             FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
				 INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
				 INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
				 WHERE hd.TrangThaiHopDong != 3 AND 
				       hd.DeletedStatus = 0 AND 
					   hdct.DeletedStatus = 0 AND 
					   tchdct.DeletedStatus = 0 AND 
					   tchdct.DmSanPhamREF IN (735, 598) AND 
					   tchdct.DmHinhThucQuangCaoREF NOT IN (42,13) AND 
					   tchdct.CreatedAt >= '2021-03-01' AND 
					   hdct.DmSanPhamREF IN (733,735, 598) AND 
					   NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF = 18 ) AND 
					   hdct.DonViTinhREF = 10 AND --Donvigoi
					   CONVERT(DATE,tchdct.LastModifiedAt) BETWEEN @NgayPhatSinh_Tu AND @NgayPhatSinh_Den AND
					   (@SoHopDong IS NULL OR hd.SoHopDong= @SoHopDong) AND
                       (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
	)BAI
	WHERE 1=1

	DELETE 
	FROM #DmThucChay
	WHERE ThanhTienSauCK = 0 AND ThanhTienKM = 0

	-- update nhãn hàng cho thực chạy onimage và native ads
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
	WHERE dm.DmNhanHangREF = -1 

	UPDATE dm
	SET dm.DonGiaSauCK = IIF(SoLuongThucChay = 0, 0, ThanhTienSauCK / SoLuongThucChay),
	    dm.DonGiaKM = IIF(SoLuongKM = 0, 0, ThanhTienKM / SoLuongKM)
	FROM #DmThucChay dm 

	UPDATE temp
	SET temp.ThanhTienSauCKPhanBo =hdct.ThanhTien,
		temp.ThanhTienKMPhanBo = IIF(hdct.ChietKhau = 100, hdct.SoLuong*hdct.DonGia, 0), 
		temp.ThanhTien_TCDT_PhanBo_TrcNgayThucHien = ISNULL(tcdt.ThanhTien, 0),
		temp.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien = ISNULL(tcdt.ThanhTienKM, 0),
		temp.ThanhTien_LechTreoHa_PhanBo_TrcNgayThucHien = ISNULL(tcdt.ThanhTien_LechTreoHa, 0)
	FROM #DmThucChay temp
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = temp.HopDongChiTietREF
	OUTER APPLY (SELECT HopDongChiTietREF, 
						SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhTien,
						SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS ThanhTienKM,
						SUM(tcdt.ThanhTienLechTreoHa) AS ThanhTien_LechTreoHa
	             FROM ABM_Data_ThucChay.dbo.thucchaydatinh tcdt
				 WHERE tcdt.NgayThucHien <= @NgayGhiNhan AND
					   tcdt.HopDongChiTietREF = temp.HopDongChiTietREF 
				 GROUP BY tcdt.HopDongChiTietREF ) tcdt


	--=============================================== 2. Xác định lệch treo hạ ==========================
	--;WITH CTE_Base AS (
	--	SELECT 
	--	  ID,
	--	  SoLuongThucChay,
	--	  SoLuongKM,
	--	  ThanhTienSauCKPhanBo,
	--	  ThanhTienKMPhanBo,
	--	  ThanhTien_TCDT_PhanBo_TrcNgayThucHien,
	--	  ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien,
	--	  ThanhTienSauCK,
	--	  ThanhTienKM,
	--	  DonGiaSauCK,
	--	  DonGiaKM,
	--	  HopDongChiTietREF,
	--	  ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ID) AS RowNum
	--	FROM #DmThucChay
	--  ),
	--  CTE_Recursive AS (
	--	SELECT 
	--	  ID,HopDongChiTietREF,
	--	  RowNum,
	--	  DonGiaSauCK,
	--	  DonGiaKM,
	--	  ThanhTienTichLuy_SauCKGhiNhan = IIF (CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienSauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--							               CTE_Base.ThanhTienSauCKPhanBo ,  CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienSauCK ),
	--	  ThanhTienTichLuy_KMGhiNhan = IIF (CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienKM>= CTE_Base.ThanhTienKMPhanBo,
	--							               CTE_Base.ThanhTienKMPhanBo ,  CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienKM ),
	--	  SoLuongThucChay_GhiNhan = IIF(CTE_Base.DonGiaSauCK <> 0, 
	--									IIF (CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienSauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--										 CTE_Base.ThanhTienSauCKPhanBo - CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienSauCK )/DonGiaSauCK,
	--									0),
	--	  SoLuongKM_GhiNhan = IIF(DonGiaKM <> 0,
	--							  IIF (CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienKM>= CTE_Base.ThanhTienKMPhanBo,
	--								   CTE_Base.ThanhTienKMPhanBo - CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienKM )/DonGiaKM,
	--						      0),
	--	  ThanhTien_GhiNhan =	IIF (CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienSauCK>= CTE_Base.ThanhTienSauCKPhanBo,
	--								 CTE_Base.ThanhTienSauCKPhanBo - CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienSauCK ),
	--	  ThanhTienKM_GhiNhan = IIF (CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienKM>= CTE_Base.ThanhTienKMPhanBo,
	--								 CTE_Base.ThanhTienKMPhanBo - CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienKM )
	--	FROM CTE_Base
	--	WHERE RowNum = 1

	--	UNION ALL
	--	-- Tính toán đệ quy
	--	SELECT 
	--	  b.ID,
	--	  b.HopDongChiTietREF,
	--	  b.RowNum,
	--	  b.DonGiaSauCK,
	--	  b.DonGiaKM,
	--	  ThanhTienTichLuy_SauCKGhiNhan = IIF (r.ThanhTienTichLuy_SauCKGhiNhan + b.ThanhTienSauCK>= b.ThanhTienSauCKPhanBo,
	--							               b.ThanhTienSauCKPhanBo ,  r.ThanhTienTichLuy_SauCKGhiNhan + b.ThanhTienSauCK ),
	--	  ThanhTienTichLuy_KMGhiNhan = IIF (r.ThanhTienTichLuy_KMGhiNhan + b.ThanhTienKM>= b.ThanhTienKMPhanBo,
	--							               b.ThanhTienKMPhanBo ,  r.ThanhTienTichLuy_KMGhiNhan + b.ThanhTienKM ),
	--	  SoLuongThucChay_GhiNhan = IIF(b.DonGiaSauCK <> 0, 
	--									IIF (r.ThanhTienTichLuy_SauCKGhiNhan + b.ThanhTienSauCK>= b.ThanhTienSauCKPhanBo,
	--										 b.ThanhTienSauCKPhanBo - r.ThanhTienTichLuy_SauCKGhiNhan ,  b.ThanhTienSauCK )/b.DonGiaSauCK,
	--									0),
	--	  SoLuongKM_GhiNhan = IIF(b.DonGiaKM <> 0,
	--							  IIF (r.ThanhTienTichLuy_KMGhiNhan + b.ThanhTienKM>= b.ThanhTienKMPhanBo,
	--								   b.ThanhTienKMPhanBo - r.ThanhTienTichLuy_KMGhiNhan ,  b.ThanhTienKM )/b.DonGiaKM,
	--						      0),
	--	  ThanhTien_GhiNhan = IIF (r.ThanhTienTichLuy_SauCKGhiNhan + b.ThanhTienSauCK>= b.ThanhTienSauCKPhanBo,
	--							   b.ThanhTienSauCKPhanBo - r.ThanhTienTichLuy_SauCKGhiNhan ,  b.ThanhTienSauCK ),
	--	  ThanhTienKM_GhiNhan = IIF (r.ThanhTienTichLuy_KMGhiNhan + b.ThanhTienKM>= b.ThanhTienKMPhanBo,
	--								 b.ThanhTienKMPhanBo - r.ThanhTienTichLuy_KMGhiNhan ,  b.ThanhTienKM )
	--	FROM CTE_Base b
	--	INNER JOIN CTE_Recursive r
	--			   ON r.HopDongChiTietREF = b.HopDongChiTietREF AND b.RowNum  - 1 = r.RowNum 
			  
	--  )

	--UPDATE temp
 --   SET  temp.SoLuongThucChay_GhiNhan = sl.SoLuongThucChay_GhiNhan,
	--	 temp.SoLuongKM_GhiNhan = sl.SoLuongKM_GhiNhan,
	--	 temp.ThanhTienTC_GhiNhan = sl.ThanhTien_GhiNhan,
	--	 temp.ThanhTienKM_GhiNhan = sl.ThanhTienKM_GhiNhan,
	--	 temp.ThanhTienLechTreoHa = IIF(temp.DonGiaKM <> 0, temp.ThanhTienKM - sl.ThanhTienKM_GhiNhan, temp.ThanhTienSauCK - sl.ThanhTien_GhiNhan),
	--	 temp.SoLuongLechTreoHa = IIF(temp.DonGiaKM <> 0, (temp.ThanhTienKM - sl.ThanhTienKM_GhiNhan)/temp.DonGiaKM, (temp.ThanhTienSauCK - sl.ThanhTien_GhiNhan)/sl.DonGiaSauCK)
	--FROM #DmThucChay temp
	--INNER JOIN CTE_Recursive sl ON sl.ID = temp.ID
	--OPTION (MAXRECURSION 0);



	;WITH CTE_Base AS (
			SELECT  ID,
					TongThucChayTruocDo = IIF(ChietKhau <> 100,
					                          ThanhTien_TCDT_PhanBo_TrcNgayThucHien + ThanhTien_LechTreoHa_PhanBo_TrcNgayThucHien + 
											  COALESCE(	SUM(ThanhTienSauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
														), 0),
											  0),
					TongThucChayDenHT =   IIF(ChietKhau <> 100,
					                          ThanhTien_TCDT_PhanBo_TrcNgayThucHien + ThanhTien_LechTreoHa_PhanBo_TrcNgayThucHien + 
											  COALESCE(	SUM(ThanhTienSauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
											  0),
					TongThucChayKMTruocDo=  IIF(ChietKhau = 100,
					                            ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + ThanhTien_LechTreoHa_PhanBo_TrcNgayThucHien + 
												COALESCE(	SUM(ThanhTienKM) OVER (
															PARTITION BY HopDongChiTietREF 
															ORDER BY ID  
															ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
															), 0),
												0),
					TongThucChaKMDenHT =   IIF(ChietKhau = 100,
					                           ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + ThanhTien_LechTreoHa_PhanBo_TrcNgayThucHien + 
											   COALESCE(SUM(ThanhTienKM) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
											   0)
			FROM #DmThucChay )
  
	UPDATE temp
	SET  	temp.ThanhTienTC_GhiNhan = CASE WHEN sl.TongThucChayTruocDo > ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo
											THEN 0
											WHEN sl.TongThucChayTruocDo > ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT <= ThanhTienSauCKPhanBo
											THEN sl.TongThucChayDenHT - sl.TongThucChayTruocDo
											WHEN sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo
											THEN ThanhTienSauCKPhanBo - sl.TongThucChayTruocDo
											WHEN sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT <= ThanhTienSauCKPhanBo
											THEN temp.ThanhTienSauCK
										END, 
			temp.ThanhTienKM_GhiNhan = CASE	WHEN sl.TongThucChayKMTruocDo > ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo
											THEN 0
											WHEN sl.TongThucChayKMTruocDo > ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT <= ThanhTienKMPhanBo
											THEN sl.TongThucChaKMDenHT - sl.TongThucChayKMTruocDo
											WHEN sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo
											THEN ThanhTienKMPhanBo - sl.TongThucChayKMTruocDo
											WHEN sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT <= ThanhTienKMPhanBo
											THEN temp.ThanhTienKM
									  END 
	FROM #DmThucChay temp
	INNER JOIN CTE_Base sl ON sl.ID = temp.ID

	UPDATE temp
	SET  	SoLuongThucChay_GhiNhan = IIF(DonGiaSauCK <> 0, ThanhTienTC_GhiNhan/DonGiaSauCK, 0),
			SoLuongKM_GhiNhan = IIF(DonGiaKM <> 0, ThanhTienKM_GhiNhan/DonGiaKM, 0),
			SoLuongLechTreoHa = SoLuongKM + SoLuongThucChay -  IIF(DonGiaSauCK <> 0, ThanhTienTC_GhiNhan/DonGiaSauCK, 0) - IIF(DonGiaKM <> 0, ThanhTienKM_GhiNhan/DonGiaKM, 0),
			--ThanhTienLechTreoHa = ThanhTienSauCK + ThanhTienKM - ThanhTienTC_GhiNhan - ThanhTienKM_GhiNhan --muc km ghi rieng dong
			ThanhTienLechTreoHa = ThanhTienSauCK  - ThanhTienTC_GhiNhan
	FROM #DmThucChay temp

	--=========================================== 3. INSERT ThucChayDaTinh
	DECLARE @Thucchay_CPMDonViGoi_DmTinhMoi DataType_Thucchay_CPMDonViGoi_DmTinhMoi

	INSERT INTO @Thucchay_CPMDonViGoi_DmTinhMoi
	(
		DmWebsiteREF ,
		TenWebsite ,
		DmBannerREF ,
		NgayThucHien ,
		HopDongChiTietREF ,
		DonViTinh ,
		DonGiaSauCK ,
		DonGiaKM ,
		DmSanPhamREF ,
		DmNhanHangREF,
		GhiChu,
		SoLuongThucChay_GhiNhan,
		SoLuongKM_GhiNhan ,
		ThanhTienTC_GhiNhan ,
		ThanhTienKM_GhiNhan ,
		SoLuongLechTreoHa ,
		ThanhTienLechTreoHa
	)
	SELECT 		DmWebsiteREF ,
				TenWebsite ,
				DmBannerREF ,
				NgayThucHien ,
				HopDongChiTietREF ,
				DonViTinh ,
				DonGiaSauCK ,
				DonGiaKM ,
				DmSanPhamREF ,
				tcgn.DmNhanHangREF,
				GhiChu = @GhiChu,
				SoLuongThucChay_GhiNhan = SUM(SoLuongThucChay_GhiNhan),
				SoLuongKM_GhiNhan = SUM(SoLuongKM_GhiNhan),
				ThanhTienTC_GhiNhan = SUM(ThanhTienTC_GhiNhan),
				ThanhTienKM_GhiNhan = SUM(ThanhTienKM_GhiNhan),
				SoLuongLechTreoHa = SUM(SoLuongLechTreoHa),
				ThanhTienLechTreoHa = SUM(ThanhTienLechTreoHa)
	FROM #DmThucChay tcgn
	GROUP BY    DmWebsiteREF ,
				TenWebsite ,
				DmBannerREF ,
				NgayThucHien ,
				HopDongChiTietREF ,
				DonViTinh ,
				DonGiaSauCK ,
				DonGiaKM ,
				DmSanPhamREF,
				tcgn.DmNhanHangREF
	HAVING SUM(SoLuongThucChay_GhiNhan) <> 0 OR 
		   SUM(SoLuongKM_GhiNhan) <> 0 OR
		   SUM(SoLuongLechTreoHa) <> 0

	EXEC dbo.ThucChay_CPMDonViGoi_Insert_ThucChayDaTinh @Thucchay_CPMDonViGoi_DmTinhMoi
		
	DROP TABLE #DmThucChay
	
END

```
