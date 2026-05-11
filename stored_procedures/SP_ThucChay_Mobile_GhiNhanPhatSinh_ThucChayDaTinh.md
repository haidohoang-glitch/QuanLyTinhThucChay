# Stored Procedure: `ThucChay_Mobile_GhiNhanPhatSinh_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-14 16:59:53.057000
- **Ngày sửa cuối**: 2025-10-27 09:52:20.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_Mobile_GhiNhanPhatSinh_ThucChayDaTinh] 
	@NgayThucHien DATE,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(100) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN

	DECLARE @GhiChu NVARCHAR(MAX)
	DECLARE @xulytay NVARCHAR(50) 
	SET @xulytay = IIF(@SoHopDong IS NOT NULL, N' do xử lý tay ', N'')
	SET @GhiChu = N'Tính mới: SP tối ưu [dbo].[ThucChay_Mobile_GhiNhanPhatSinh_ThucChayDaTinh]' + @xulytay

	DELETE tcdt
	FROM ABM_data_ThucChay.dbo.ThucChayDaTinh tcdt
	LEFT JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE hdct.DmSanPhamREF = 342 AND 
		  ISNULL(hdct.DmLoaiNenTangREF,0) <> 8 AND 
		  NOT (tcdt.DmHinhThucQuangCao IN (13,42) OR tcdt.DmLoaiBannerREF IN (17,18)) AND 
		  tcdt.DotChayHopDong NOT IN ( N'NGAY', N'CPM_DonViGoi',N'Tính mới CPM DonViGoi') AND
		  tcdt.NgayThucHien = @NgayThucHien AND 
		  tcdt.DotChayHopDong = N'Tính mới Mobile' AND 
		 (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID) AND
         (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong) 

	--======================================= 1. Xác định dữ liệu cần insert ===============================
	CREATE TABLE #DmThucChay  ( 
			ThucChayID INT,
			DmNhanHangREF NVARCHAR(MAX), 
			TenWebsite NVARCHAR(255),
			DmBannerREF INT,
			bannerType INT,
			DonViTinhTreo NVARCHAR(50),
		    NgayThucHien DATETIME,
			HopDongChiTietREF INT,
			ChietKhau FLOAT,

			TongViewThucChay INT,
			TongClickThucChay INT,
			SoLuongThucChay INT,
			DonGiaChay FLOAT,

			SoLuongDanhSoPhanBo INT,
			ThanhTienSauCKPhanBo FLOAT,
			ThanhTienKMPhanBo FLOAT,

			SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien INT,
			SoLuongLechTreohaDaTinhPhanBo_TrcNgayThucHien INT,

			ThanhTienGhiNhanDaTinhPhanBo_TrcNgayThucHien FLOAT,
			ThanhTienLechTreohaDaTinhPhanBo_TrcNgayThucHien FLOAT,
			ThanhTienKMDaTinhPhanBo_TrcNgayThucHien FLOAT,

			SoLuongThucChay_GhiNhan INT,
			SoLuongKM_GhiNhan INT,
			ThanhTienThucChay_GhiNhan FLOAT,
			ThanhTienKM_GhiNhan FLOAT,

			SoLuongLechTreoHa INT,
			ThanhTienLechTreoHa FLOAT,
			
			LoaiXuLy INT  --1: Phân bổ ký gói, 2: Pb thường
			)

	INSERT INTO #DmThucChay( 
			ThucChayID, 
			TenWebsite,
			DmBannerREF ,
			bannerType ,
			DonViTinhTreo,
		    NgayThucHien ,
			HopDongChiTietREF ,
			SoLuongDanhSoPhanBo,
			ChietKhau,
			ThanhTienSauCKPhanBo ,
			ThanhTienKMPhanBo ,

			TongViewThucChay ,
			TongClickThucChay ,
			SoLuongThucChay,
			
			LoaiXuLy)
	SELECT  DISTINCT
	        tc.ID,
			tc.TenWebsite,
			tc.DmBannerREF,
			tc.BannerType,
			CASE WHEN tchdct.DmDonViTinhREF = 1 THEN N'CPM'
				 WHEN tchdct.DmDonViTinhREF = 2 THEN N'CPC'
				 ELSE ''
			END,
			CONVERT(DATE,tc.NgayThucHien),
			tchdctab.HopDongChiTietREF,
			hdct.ChietKhau,
			SoLuongDanhSoPhanBo = IIF( hdct.donvitinh = 'CPM', hdct.SoLuong*1000, hdct.SoLuong),
			ThanhTienSauCKPhanBo = hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100),
			ThanhTienKMPhanBo = IIF(hdct.ChietKhau = 100, hdct.SoLuong*hdct.DonGia, 0),

			tc.TongViewThucChay,
			tc.TongClickThucChay,
			SUM(
				CASE WHEN hdct.donvitinh = 'CPC' OR (hdct.DonViTinh = N'Gói' AND tchdct.DmDonViTinhREF = 2)
					 THEN ISNULL(tc.TongClickThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0)
					 WHEN hdct.donvitinh = 'CPM' OR (hdct.DonViTinh = N'Gói' AND tchdct.DmDonViTinhREF = 1)
					 THEN ISNULL(tc.TongViewThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100,0)
					 ELSE 0
				END) ,

			LoaiXuLy = IIF(hdct.DonViTinh = N'Gói', 1, 2)
	FROM ABM_data_thucchay.dbo.thucchay tc
	INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTietAndBanner tchdctab 
																 ON    tchdctab.DmBannerID = CONVERT(NVARCHAR(50),tc.DmBannerREF) 
																	   AND tchdctab.DeletedStatus = 0
	INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct ON tchdct.DmBannerREF = CONVERT(NVARCHAR(50),tc.DmBannerREF) AND 
																	  tchdctab.HopDongChiTietREF = tchdct.HopDongChiTietREF AND
																	  tchdct.DeletedStatus = 0
    INNER JOIN  ABM_data_thucchay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN  ABM_data_thucchay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK
	INNER JOIN ABM_data_thucchay.dbo.ThucChay_Mobile_DmPhanBoChungBanner_Truoc20241212 pbcu ON pbcu.ID = tchdctab.HopDongChiTietREF 
	WHERE   hd.TrangThaiHopDong != 3
			AND hd.DeletedStatus = 0
			AND tc.NgayThucHien = @NgayThucHien
			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
			AND tc.TypeProduct = 10 
			AND tc.DmWebsiteREF <> 0 
			AND hdct.DmSanPhamREF <> 733
			AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID) 
            AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong) 
	GROUP BY 	tc.ID,
				tc.TenWebsite,
				tc.DmBannerREF,
				tc.BannerType,
				tchdct.DmDonViTinhREF ,
				tchdctab.HopDongChiTietREF,
				hdct.ChietKhau,
				hdct.donvitinh, hdct.SoLuong,
				hdct.DonGia, hdct.ChietKhau,
				tc.TongViewThucChay,
				tc.TongClickThucChay,
				hdct.DonViTinh,
				tc.NgayThucHien
	
	UPDATE dm
	SET DonGiaChay = ISNULL(dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau ( 	dm.HopDongChiTietREF, 
																				dbo.ThucChay_Mobile_GetDonViTinh(hdct.DonViTinh, ISNULL(dm.DonViTinhTreo, '')),
																				dm.BannerType,
																				dm.NgayThucHien) , 0)
	FROM #DmThucChay dm
	INNER JOIN  ABM_data_thucchay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietREF


	-- tính theo phương pháp mới
	INSERT INTO #DmThucChay( 
			ThucChayID, 
			TenWebsite,
			DmBannerREF ,
			bannerType ,
			DonViTinhTreo,
		    NgayThucHien ,
			HopDongChiTietREF ,
			ChietKhau,
			SoLuongDanhSoPhanBo ,
			ThanhTienSauCKPhanBo,
			ThanhTienKMPhanBo,

			TongViewThucChay ,
			TongClickThucChay ,
			SoLuongThucChay,
			DonGiaChay,
			
			LoaiXuLy)
	SELECT  DISTINCT   -- tránh TH thucchayhopdongchitiet ra nhiều bản ghi
			tc.ID,
			tc.TenWebsite,
			tc.DmBannerREF,
			tc.BannerType,
			CASE WHEN tchdct.DmDonViTinhREF = 1 THEN N'CPM'
				 WHEN tchdct.DmDonViTinhREF = 2 THEN N'CPC'
				 ELSE ''
			END,
			CONVERT(DATE,tc.NgayThucHien),
			tc.HopDongChiTietREF,
			hdct.ChietKhau,
			SoLuongDanhSoPhanBo = IIF( hdct.donvitinh = 'CPM', hdct.SoLuong*1000, hdct.SoLuong),
			ThanhTienSauCKPhanBo = hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100),
			ThanhTienKMPhanBo = IIF(hdct.ChietKhau = 100, hdct.SoLuong*hdct.DonGia, 0),

			tc.TongViewThucChay,
			tc.TongClickThucChay,
			CASE WHEN (tchdct.DmDonViTinhREF = 1 AND hdct.DonViTinhREF = 10 ) OR hdct.DonViTinhREF = 1
				 THEN tc.TongViewThucChay
				 WHEN (tchdct.DmDonViTinhREF = 2 AND hdct.DonViTinhREF = 10 ) OR hdct.DonViTinhREF = 2
				 THEN tc.TongClickThucChay
				 ELSE 0
			END ,
			CASE WHEN (tchdct.DmDonViTinhREF = 1 AND hdct.DonViTinhREF = 10 ) 
				 THEN tchdct.DonGia/1000
				 WHEN (tchdct.DmDonViTinhREF = 2 AND hdct.DonViTinhREF = 10 )
				 THEN tchdct.DonGia
				 WHEN  hdct.DonViTinhREF = 1
				 THEN  hdct.DonGia/1000
				 WHEN  hdct.DonViTinhREF = 2
				 THEN  hdct.DonGia
				 ELSE 0
			END,

			LoaiXuLy = IIF(hdct.DonViTinh = N'Gói', 1, 2)
	FROM ABM_data_thucchay.dbo.thucchay tc   
	INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct ON tchdct.DmBannerREF = CONVERT(NVARCHAR(50),tc.DmBannerREF) AND tchdct.DeletedStatus = 0
    INNER JOIN  ABM_data_thucchay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tc.HopDongChiTietREF
	INNER JOIN  ABM_data_thucchay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK
	WHERE   hd.TrangThaiHopDong != 3
			AND hd.DeletedStatus = 0
			AND tc.NgayThucHien = @NgayThucHien
			AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
			AND tc.TypeProduct = 10 
			AND tc.DmWebsiteREF <> 0 
			AND NOT EXISTS(SELECT TOP 1 ID FROM ABM_data_thucchay.dbo.ThucChay_Mobile_DmPhanBoChungBanner_Truoc20241212 cu WHERE cu.ID = hdct.HopDongChiTietID )
			AND hdct.DmSanPhamREF <> 733
			AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID) 
            AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong) 
		
	DELETE
	FROM #DmThucChay
	WHERE SoLuongThucChay = 0

	UPDATE temp
	SET temp.SoLuongDanhSoPhanBo = hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh),
		temp.SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien = ISNULL(tcdt.SoluongGhiNhanDaTinh, 0),
		temp.SoLuongLechTreohaDaTinhPhanBo_TrcNgayThucHien = ISNULL(tcdt.SoLuongLechTreoHaDaTinh, 0),

		temp.ThanhTienGhiNhanDaTinhPhanBo_TrcNgayThucHien = ISNULL(ThanhTienSauCKDaTinh, 0),
		temp.ThanhTienLechTreohaDaTinhPhanBo_TrcNgayThucHien = ISNULL(ThanhTienLechTreoHaDaTinh, 0),
		temp.ThanhTienKMDaTinhPhanBo_TrcNgayThucHien = ISNULL(ThanhTienKMDaTinh, 0)
	FROM #DmThucChay temp
	INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = temp.HopDongChiTietREF
	OUTER APPLY (SELECT HopDongChiTietREF, SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi + tcdt.SoLuongKMThayDoi + tcdt.SoLuongThucChayKM) AS SoluongGhiNhanDaTinh,
						SUM(tcdt.SoLuongThucChayLechTreoHa) AS SoLuongLechTreoHaDaTinh,
						SUM(tcdt.ThanhTienLechTreoHa) AS ThanhTienLechTreoHaDaTinh,
						SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS ThanhTienKMDaTinh,
						SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) ThanhTienSauCKDaTinh
	             FROM ABM_data_thucchay.dbo.ThucChayDaTinh tcdt
				 WHERE tcdt.NgayThucHien <= temp.ngaythuchien AND
					   tcdt.HopDongChiTietREF = temp.HopDongChiTietREF
				 GROUP BY tcdt.HopDongChiTietREF ) tcdt

	UPDATE dm
	SET dm.DmNhanHangREF = ISNULL(tchdct.DmNhanHangREF, '')
	FROM #DmThucChay dm
	OUTER APPLY  (SELECT STUFF ((   SELECT DISTINCT  ',' + tchdct.DmNhanHangREF
									FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct
									WHERE DeletedStatus = 0 AND 
										  tchdct.HopDongChiTietREF = dm.HopDongChiTietREF AND 
										  tchdct.DmBannerREF = CONVERT(NVARCHAR(50),dm.DmBannerREF) 
									FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 
									1, 1, '') AS DmNhanHangREF
							) tchdct

	--=============================================== 2. Xác định lệch treo hạ ==========================
	-- Với TH phân bổ đơn vị gói (loại xử lý = 1) thì check vượt thành tiền, còn lại thì check vượt số lượng
	;WITH CTE_Base AS (
			SELECT 
					  ThucChayID,
					  SoLuongThucChay,
					  SoLuongDanhSoPhanBo,
					  SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien,
					  HopDongChiTietREF,
					  ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ThucChayID) AS RowNum
			FROM #DmThucChay
			WHERE LoaiXuLy = 2
	  ),
	  CTE_Recursive AS (
			SELECT 
					  ThucChayID,
					  SoLuongThucChay,
					  SoLuongDanhSoPhanBo,
					  HopDongChiTietREF,
					  RowNum,
					  TichLuyGhiNhan = IIF (SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien + SoLuongThucChay>= SoLuongDanhSoPhanBo,
											SoLuongDanhSoPhanBo ,  SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien + SoLuongThucChay ),
					  ThucChayGhiNhan = IIF (SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien + SoLuongThucChay>= SoLuongDanhSoPhanBo,
											 SoLuongDanhSoPhanBo - SoLuongGhiNhanDaTinhPhanBo_TrcNgayThucHien,  SoLuongThucChay ) 
			FROM CTE_Base
			WHERE RowNum = 1

			UNION ALL
			-- Tính toán đệ quy
			SELECT 
					  b.ThucChayID,
					  b.SoLuongThucChay,
					  b.SoLuongDanhSoPhanBo,
					  b.HopDongChiTietREF,
					  b.RowNum,
					  TichLuyGhiNhan = IIF(  r.TichLuyGhiNhan + b.SoLuongThucChay>=  b.SoLuongDanhSoPhanBo, 
											 b.SoLuongDanhSoPhanBo , r.TichLuyGhiNhan + b.SoLuongThucChay ),
					  ThucChayGhiNhan = IIF (r.TichLuyGhiNhan + b.SoLuongThucChay>= b.SoLuongDanhSoPhanBo,
											 b.SoLuongDanhSoPhanBo - r.TichLuyGhiNhan,  b.SoLuongThucChay )
			FROM CTE_Base b
			INNER JOIN CTE_Recursive r
					   ON r.HopDongChiTietREF = b.HopDongChiTietREF AND b.RowNum  - 1 = r.RowNum 
			  
	  )
  
	UPDATE temp
	SET  SoLuongThucChay_GhiNhan = IIF(temp.ChietKhau = 100, 0, sl.ThucChayGhiNhan),
	     SoLuongKM_GhiNhan = IIF(temp.ChietKhau = 100, sl.ThucChayGhiNhan, 0),
		 SoLuongLechTreoHa =   temp.SoLuongThucChay - sl.ThucChayGhiNhan
	FROM #DmThucChay temp
	INNER JOIN CTE_Recursive sl ON sl.ThucChayID = temp.ThucChayID
	WHERE temp.LoaiXuLy = 2
	OPTION (MAXRECURSION 0);

	UPDATE dm
	SET 	ThanhTienThucChay_GhiNhan = SoLuongThucChay_GhiNhan*DonGiaChay*(1-dm.ChietKhau/100),
			ThanhTienKM_GhiNhan = IIF(ChietKhau = 100, SoLuongKM_GhiNhan*DonGiaChay, 0),
			ThanhTienLechTreoHa = SoLuongLechTreoHa*DonGiaChay
	FROM #DmThucChay dm
	WHERE LoaiXuLy = 2


	;WITH CTE_Base AS (
			SELECT 
					  ThucChayID,
					  ThanhTienSauCK = SoLuongThucChay*DonGiaChay*(1-ChietKhau/100),
					  ThanhTienKM = IIF(ChietKhau = 100, SoLuongThucChay*DonGiaChay, 0),
					  ThanhTienSauCKPhanBo,
					  ThanhTienKMPhanBo,
					  ThanhTienGhiNhanDaTinhPhanBo_TrcNgayThucHien,
					  ThanhTienKMDaTinhPhanBo_TrcNgayThucHien,
					  HopDongChiTietREF,
					  ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ThucChayID) AS RowNum
			FROM #DmThucChay
			WHERE LoaiXuLy = 1
	  ),
	  CTE_Recursive AS (
			SELECT 
					  ThucChayID,
					  ThanhTienSauCK,
					  ThanhTienKM,
					  ThanhTienSauCKPhanBo,
					  ThanhTienKMPhanBo,
					  HopDongChiTietREF,
					  RowNum,
					  TichLuyTTGhiNhan = IIF (ThanhTienGhiNhanDaTinhPhanBo_TrcNgayThucHien + ThanhTienSauCK>= ThanhTienSauCKPhanBo,
											  ThanhTienSauCKPhanBo ,  ThanhTienGhiNhanDaTinhPhanBo_TrcNgayThucHien + ThanhTienSauCK ),
					  ThucChayTTGhiNhan = IIF (ThanhTienGhiNhanDaTinhPhanBo_TrcNgayThucHien + ThanhTienSauCK>= ThanhTienSauCKPhanBo,
											   ThanhTienSauCKPhanBo - ThanhTienGhiNhanDaTinhPhanBo_TrcNgayThucHien,  ThanhTienSauCK ),
					  TichLuyKMGhiNhan = IIF (ThanhTienKMDaTinhPhanBo_TrcNgayThucHien + ThanhTienKM>= ThanhTienKMPhanBo,
											  ThanhTienKMPhanBo ,  ThanhTienKMDaTinhPhanBo_TrcNgayThucHien + ThanhTienKM ),
					  ThucChayKMGhiNhan = IIF (ThanhTienKMDaTinhPhanBo_TrcNgayThucHien + ThanhTienKM>= ThanhTienKMPhanBo,
											   ThanhTienKMPhanBo - ThanhTienKMDaTinhPhanBo_TrcNgayThucHien,  ThanhTienKM )				  

			FROM CTE_Base
			WHERE RowNum = 1

			UNION ALL
			-- Tính toán đệ quy
			SELECT 
					  b.ThucChayID,
					  b.ThanhTienSauCK,
					  b.ThanhTienKM,
					  b.ThanhTienSauCKPhanBo,
					  b.ThanhTienKMPhanBo,
					  b.HopDongChiTietREF,
					  b.RowNum,
					  TichLuyTTGhiNhan = IIF( r.TichLuyTTGhiNhan + b.ThanhTienSauCK>=  b.ThanhTienSauCKPhanBo, 
											  b.ThanhTienSauCKPhanBo , r.TichLuyTTGhiNhan + b.ThanhTienSauCK ),
					  ThucChayTTGhiNhan = IIF (r.TichLuyTTGhiNhan + b.ThanhTienSauCK>=  b.ThanhTienSauCKPhanBo, 
											   b.ThanhTienSauCKPhanBo - r.TichLuyTTGhiNhan,  b.ThanhTienSauCK ),
					  TichLuyKMGhiNhan = IIF( r.TichLuyKMGhiNhan + b.ThanhTienKM>=  b.ThanhTienKMPhanBo, 
											  b.ThanhTienKMPhanBo , r.TichLuyKMGhiNhan + b.ThanhTienKM ),
					  ThucChayKMGhiNhan = IIF (r.TichLuyKMGhiNhan + b.ThanhTienKM>=  b.ThanhTienKMPhanBo, 
											   b.ThanhTienKMPhanBo - r.TichLuyKMGhiNhan,  b.ThanhTienKM )
			FROM CTE_Base b
			INNER JOIN CTE_Recursive r ON r.HopDongChiTietREF = b.HopDongChiTietREF AND b.RowNum  - 1 = r.RowNum 
			  
	  )
  
	UPDATE temp
	SET  temp.ThanhTienThucChay_GhiNhan = sl.ThucChayTTGhiNhan,
		 temp.ThanhTienKM_GhiNhan = sl.ThucChayKMGhiNhan
	FROM #DmThucChay temp
	INNER JOIN CTE_Recursive sl ON sl.ThucChayID = temp.ThucChayID
	WHERE temp.LoaiXuLy = 1
	OPTION (MAXRECURSION 0);

	UPDATE  dm
	SET 	dm.SoLuongThucChay_GhiNhan = IIF(DonGiaChay<> 0 and ChietKhau <> 100, ThanhTienThucChay_GhiNhan/((1-ChietKhau/100)*DonGiaChay), 0),
			dm.SoLuongKM_GhiNhan = IIF(DonGiaChay<> 0 and ChietKhau = 100, ThanhTienKM_GhiNhan/DonGiaChay, 0)
	FROM #DmThucChay dm
	WHERE LoaiXuLy = 1

	UPDATE  dm
	SET 	dm.SoLuongLechTreoHa = SoLuongThucChay - SoLuongKM_GhiNhan - SoLuongThucChay_GhiNhan,
			dm.ThanhTienLechTreoHa = (SoLuongThucChay - SoLuongKM_GhiNhan - SoLuongThucChay_GhiNhan)*DonGiaChay
	FROM #DmThucChay dm
	WHERE LoaiXuLy = 1

	--=========================================== 3. INSERT ThucChayDaTinh
	DECLARE @Thucchay_Mobile_DmTinhMoi DataType_Thucchay_Mobile_DmTinhMoi2


	INSERT INTO @Thucchay_Mobile_DmTinhMoi
	(
	       HopDongChiTietREF,
		   NgayThucHien,
		   DmBannerREF,
		   TenWebsite,
		   DmNhanHangREF,
		   bannerType,
		   DonViTinhTreo,
		   Dongia,

		   TongViewThucChay ,
		   TongClickThucChay ,
		   SoLuongThucChay_GhiNhan,
		   SoLuongKM_GhiNhan ,
		   SoLuongLechTreoHa ,

		   ThanhTienThucChay_GhiNhan,
		   ThanhTienKM_GhiNhan,
		   ThanhTienLechTreoHa,

		   GhiChu 
	)
	SELECT  tcgn.HopDongChiTietREF,
			tcgn.NgayThucHien,
			tcgn.DmBannerREF,
			tcgn.TenWebsite,
			tcgn.DmNhanHangREF,
			tcgn.bannerType,
			tcgn.DonViTinhTreo,
			tcgn.DonGiaChay,

			TongViewThucChay = SUM(ISNULL(tcgn.TongViewThucChay,0)) ,
			TongClickThucChay = SUM(ISNULL(tcgn.TongClickThucChay,0)) ,
			SoLuongThucChay_GhiNhan = SUM(ISNULL(tcgn.SoLuongThucChay_GhiNhan,0)) ,
			SoLuongKM_GhiNhan = SUM(ISNULL(tcgn.SoLuongKM_GhiNhan,0)) ,
			SoLuongLechTreoHa = SUM(ISNULL(tcgn.SoLuongLechTreoHa,0)),

			ThanhTienThucChay_GhiNhan = SUM(ISNULL(ThanhTienThucChay_GhiNhan,0)) ,
			ThanhTienKM_GhiNhan = SUM(ISNULL(ThanhTienKM_GhiNhan,0)) ,
			ThanhTienLechTreoHa = SUM(ISNULL(ThanhTienLechTreoHa,0)) ,

			GhiChu = IIF(pbcu.id IS NOT NULL, N'PP cũ ', N'PP mới ') + @GhiChu 
	FROM #DmThucChay tcgn
	LEFT JOIN ABM_data_thucchay.dbo.ThucChay_Mobile_DmPhanBoChungBanner_Truoc20241212 pbcu ON pbcu.id = tcgn.HopDongChiTietREF
	GROUP BY    tcgn.HopDongChiTietREF,
				tcgn.NgayThucHien,
				tcgn.DmBannerREF,
				tcgn.TenWebsite,
				tcgn.DmNhanHangREF,
				tcgn.bannerType,
				tcgn.DonViTinhTreo,
				pbcu.id,
				tcgn.DonGiaChay
	HAVING  SUM(tcgn.SoLuongThucChay_GhiNhan) <> 0 OR 
			SUM(tcgn.SoLuongLechTreoHa) <> 0  OR
			SUM(SoLuongKM_GhiNhan) <> 0


	EXEC dbo.ThucChay_Mobile_Insert_ThucChayDaTinh @Thucchay_Mobile_DmTinhMoi
		
	DROP TABLE #DmThucChay
	
END

```
