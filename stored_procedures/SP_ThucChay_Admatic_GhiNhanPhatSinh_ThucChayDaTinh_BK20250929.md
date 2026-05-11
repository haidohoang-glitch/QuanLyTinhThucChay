# Stored Procedure: `ThucChay_Admatic_GhiNhanPhatSinh_ThucChayDaTinh_BK20250929`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-09-29 14:49:45.910000
- **Ngày sửa cuối**: 2025-09-29 14:49:45.910000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql





CREATE PROCEDURE [dbo].[ThucChay_Admatic_GhiNhanPhatSinh_ThucChayDaTinh_BK20250929] 
	@StartDate DATE,
	@EndDate DATE,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN
	DECLARE @NgayDanhSoGioiHan_MKT DATETIME = '2025-10-10'
	IF @SoHopDong IS NOT NULL
    BEGIN
		SET @NgayDanhSoGioiHan = NULL
	END 

	DECLARE @GhiChu NVARCHAR(MAX)
	SET @GhiChu = N'Tính mới: SP tối ưu [dbo].[ThucChay_Admatic_GhiNhanPhatSinh_ThucChayDaTinh]'

	DELETE FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
	WHERE	convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
			AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao = 13)
			AND DotChayHopDong = N'Tính mới Admatic'
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
			DonGiaKM FLOAT,
			DmSanPhamREF INT,
			DonViTinh NVARCHAR(100),
			DonGiaSauCK FLOAT,
			ChietKhau FLOAT,

			SoLuongThucChay INT,
			ThanhTienSauCK FLOAT,
			SoLuongKM INT,
			ThanhTienKM FLOAT,

			ThanhTienSauCKPhanBo FLOAT,
			ThanhTienKMPhanBo FLOAT,
			ThanhTien_TCDT_PhanBo_TrcNgayThucHien FLOAT,
			ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien FLOAT,

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
			ChietKhau,
			DmSanPhamREF ,
			SoLuongThucChay ,
			ThanhTienSauCK ,
			SoLuongKM ,
			ThanhTienKM )
	SELECT  tc.DmWebsiteID,
			tc.TenWebsite,
			tc.DmBannerID,
			CONVERT(DATE,tc.NgayThucHien),
			tchdct.HopDongChiTietREF,
			tc.DonViTinh,
			hdct.ChietKhau,
			tc.DmSanPhamREF,
			SoLuongThucChay = ISNULL(IIF(hdct.ChietKhau <> 100, tc.SoLuongThucChay*tchdct.TiLeThucChayHDCTSoVoiBanner/100, 0),0),
			ThanhTienSauCK = ISNULL(IIF(hdct.ChietKhau <> 100, tc.ThanhTienThucChaySauCK_ChuaVAT*tchdct.TiLeThucChayHDCTSoVoiBanner/100, 0),0),
			SoLuongKM = ISNULL(IIF(hdct.ChietKhau = 100, tc.SoLuongThucChayKM*tchdct.TiLeThucChayHDCTSoVoiBanner/100, 0),0),
			ThanhTienKM = ISNULL(IIF(hdct.ChietKhau = 100, tc.ThanhTienThucChayKM*tchdct.TiLeThucChayHDCTSoVoiBanner/100, 0),0)
	FROM ABM_Data_ThucChay.dbo.[ThucChay_ThanhTien_Admatic] tc
	INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic tchdct ON tc.DmBannerID = tchdct.DmBannerREF AND 
																						   tc.DmSanPhamREF = tchdct.DmSanPhamREF AND 
																						   tchdct.DeletedStatus = 0
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF AND
                                                     (hdct.DmSanPhamREF = tc.DmSanPhamREF OR hdct.DmSanPhamREF = 733 )
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK AND 
												   hd.SoHopDong = tc.SoHopDong
	WHERE   CONVERT(DATE,tc.NgayThucHien) BETWEEN @StartDate AND @EndDate
			AND tc.DonViTinh <> N'BÀI'
			AND tc.DmWebsiteID <> 0
			AND tc.DeletedStatus = 0

			AND hdct.DmLoaiREF = 42
			AND hdct.DmLoaiNenTangREF <> 9
			AND hdct.DeletedStatus = 0
			AND NOT ( hdct.DmLoaiBannerREF IN (17,18)OR hdct.DmLoaiREF IN (13))

			--HAIDH COMMENT 16092025 THEM SAN PHAM MKT-FEE CHO VIEC TINH THUC CHAY
			AND NOT (hd.NgayDanhSoHopDong <@NgayDanhSoGioiHan_MKT and hdct.DmSanPhamREF = 817)

			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
			AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
			AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)

	DELETE
    FROM #DmThucChay
	WHERE SoLuongThucChay = 0 AND SoLuongKM = 0

	UPDATE dm
	SET dm.DonGiaSauCK = IIF(SoLuongThucChay = 0, 0, ThanhTienSauCK / SoLuongThucChay),
	    dm.DonGiaKM = IIF(SoLuongKM = 0, 0, ThanhTienKM / SoLuongKM)
	FROM #DmThucChay dm 

	UPDATE temp
	SET temp.ThanhTienSauCKPhanBo =hdct.ThanhTien,
		temp.ThanhTienKMPhanBo = IIF(hdct.ChietKhau = 100, hdct.SoLuong*hdct.DonGia, 0), 
		temp.ThanhTien_TCDT_PhanBo_TrcNgayThucHien = ISNULL(tcdt.ThanhTien, 0),
		temp.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien = ISNULL(tcdt.ThanhTienKM, 0)
	FROM #DmThucChay temp
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = temp.HopDongChiTietREF
	OUTER APPLY (SELECT HopDongChiTietREF, 
						SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhTien,
						SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS ThanhTienKM
	             FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt
				 WHERE tcdt.NgayThucHien <= @EndDate AND
					   tcdt.HopDongChiTietREF = temp.HopDongChiTietREF 
				 GROUP BY tcdt.HopDongChiTietREF ) tcdt



	--=============================================== 2. Xác định lệch treo hạ ==========================
	;WITH CTE_Base AS (
		SELECT 
		  ID,
		  SoLuongThucChay,
		  SoLuongKM,
		  ThanhTienSauCKPhanBo,
		  ThanhTienKMPhanBo,
		  ThanhTien_TCDT_PhanBo_TrcNgayThucHien,
		  ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien,
		  ThanhTienSauCK,
		  ThanhTienKM,
		  DonGiaSauCK,
		  DonGiaKM,
		  HopDongChiTietREF,
		  ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ID) AS RowNum
		FROM #DmThucChay
	  ),
	  CTE_Recursive AS (
		SELECT 
		  ID, HopDongChiTietREF,
		  RowNum,
		  DonGiaSauCK,
		  DonGiaKM,
		  ThanhTienTichLuy_SauCKGhiNhan = IIF (CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienSauCK>= CTE_Base.ThanhTienSauCKPhanBo,
								               CTE_Base.ThanhTienSauCKPhanBo ,  CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienSauCK ),
		  ThanhTienTichLuy_KMGhiNhan = IIF (CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienKM>= CTE_Base.ThanhTienKMPhanBo,
								               CTE_Base.ThanhTienKMPhanBo ,  CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienKM ),
		  SoLuongThucChay_GhiNhan = IIF(CTE_Base.DonGiaSauCK <> 0, 
										IIF (CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienSauCK>= CTE_Base.ThanhTienSauCKPhanBo,
											 CTE_Base.ThanhTienSauCKPhanBo - CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienSauCK )/DonGiaSauCK,
										0),
		  SoLuongKM_GhiNhan = IIF(DonGiaKM <> 0,
								  IIF (CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienKM>= CTE_Base.ThanhTienKMPhanBo,
									   CTE_Base.ThanhTienKMPhanBo - CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienKM )/DonGiaKM,
							      0),
		  ThanhTien_GhiNhan =	IIF (CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienSauCK>= CTE_Base.ThanhTienSauCKPhanBo,
									 CTE_Base.ThanhTienSauCKPhanBo - CTE_Base.ThanhTien_TCDT_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienSauCK ),
		  ThanhTienKM_GhiNhan = IIF (CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien + CTE_Base.ThanhTienKM>= CTE_Base.ThanhTienKMPhanBo,
									 CTE_Base.ThanhTienKMPhanBo - CTE_Base.ThanhTienKM_TCDT_PhanBo_TrcNgayThucHien ,  CTE_Base.ThanhTienKM )
		FROM CTE_Base
		WHERE RowNum = 1

		UNION ALL
		-- Tính toán đệ quy
		SELECT 
		  b.ID,
		  b.HopDongChiTietREF,
		  b.RowNum,
		  b.DonGiaSauCK,
		  b.DonGiaKM,
		  ThanhTienTichLuy_SauCKGhiNhan = IIF (r.ThanhTienTichLuy_SauCKGhiNhan + b.ThanhTienSauCK>= b.ThanhTienSauCKPhanBo,
								               b.ThanhTienSauCKPhanBo ,  r.ThanhTienTichLuy_SauCKGhiNhan + b.ThanhTienSauCK ),
		  ThanhTienTichLuy_KMGhiNhan = IIF (r.ThanhTienTichLuy_KMGhiNhan + b.ThanhTienKM>= b.ThanhTienKMPhanBo,
								               b.ThanhTienKMPhanBo ,  r.ThanhTienTichLuy_KMGhiNhan + b.ThanhTienKM ),
		  SoLuongThucChay_GhiNhan = IIF(b.DonGiaSauCK <> 0, 
										IIF (r.ThanhTienTichLuy_SauCKGhiNhan + b.ThanhTienSauCK>= b.ThanhTienSauCKPhanBo,
											 b.ThanhTienSauCKPhanBo - r.ThanhTienTichLuy_SauCKGhiNhan ,  b.ThanhTienSauCK )/b.DonGiaSauCK,
										0),
		  SoLuongKM_GhiNhan = IIF(b.DonGiaKM <> 0,
								  IIF (r.ThanhTienTichLuy_KMGhiNhan + b.ThanhTienKM>= b.ThanhTienKMPhanBo,
									   b.ThanhTienKMPhanBo - r.ThanhTienTichLuy_KMGhiNhan ,  b.ThanhTienKM )/b.DonGiaKM,
							      0),
		  ThanhTien_GhiNhan = IIF (r.ThanhTienTichLuy_SauCKGhiNhan + b.ThanhTienSauCK>= b.ThanhTienSauCKPhanBo,
								   b.ThanhTienSauCKPhanBo - r.ThanhTienTichLuy_SauCKGhiNhan ,  b.ThanhTienSauCK ),
		  ThanhTienKM_GhiNhan = IIF (r.ThanhTienTichLuy_KMGhiNhan + b.ThanhTienKM>= b.ThanhTienKMPhanBo,
									 b.ThanhTienKMPhanBo - r.ThanhTienTichLuy_KMGhiNhan ,  b.ThanhTienKM )
		FROM CTE_Base b
		INNER JOIN CTE_Recursive r
				   ON r.HopDongChiTietREF = b.HopDongChiTietREF AND b.RowNum  - 1 = r.RowNum 
			  
	  )
  
	UPDATE temp
	SET  temp.SoLuongThucChay_GhiNhan = sl.SoLuongThucChay_GhiNhan,
		 temp.SoLuongKM_GhiNhan = sl.SoLuongKM_GhiNhan,
		 temp.ThanhTienTC_GhiNhan = sl.ThanhTien_GhiNhan,
		 temp.ThanhTienKM_GhiNhan = sl.ThanhTienKM_GhiNhan,
		 temp.ThanhTienLechTreoHa = IIF(temp.DonGiaKM <> 0, temp.ThanhTienKM - sl.ThanhTienKM_GhiNhan, (temp.ThanhTienSauCK - sl.ThanhTien_GhiNhan)*100/(100-temp.ChietKhau)),
		 temp.SoLuongLechTreoHa = IIF(temp.DonGiaKM <> 0, (temp.ThanhTienKM - sl.ThanhTienKM_GhiNhan)/temp.DonGiaKM, (temp.ThanhTienSauCK - sl.ThanhTien_GhiNhan)/sl.DonGiaSauCK)
	FROM #DmThucChay temp
	INNER JOIN CTE_Recursive sl ON sl.ID = temp.ID
	OPTION (MAXRECURSION 0);

	--=========================================== 3. INSERT ThucChayDaTinh
	DECLARE @Thucchay_Admatic_DmTinhMoi DataType_Thucchay_Admatic_DmTinhMoi


	INSERT INTO @Thucchay_Admatic_DmTinhMoi
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
				DmSanPhamREF 
	HAVING SUM(SoLuongThucChay_GhiNhan) <> 0 OR 
		   SUM(SoLuongKM_GhiNhan) <> 0 OR
		   SUM(SoLuongLechTreoHa) <> 0

	EXEC dbo.ThucChay_Admatic_Insert_ThucChayDaTinh @Thucchay_Admatic_DmTinhMoi
		
	DROP TABLE #DmThucChay
	
END

```
