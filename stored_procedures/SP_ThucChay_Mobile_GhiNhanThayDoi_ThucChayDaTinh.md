# Stored Procedure: `ThucChay_Mobile_GhiNhanThayDoi_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-14 16:59:24.550000
- **Ngày sửa cuối**: 2025-10-27 09:52:22.057000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `datetime(8)` | No |
| `@NgayCheckThayDoi` | `datetime(8)` | No |
| `@NgayDanhSoGioiHan` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql



CREATE PROCEDURE [dbo].[ThucChay_Mobile_GhiNhanThayDoi_ThucChayDaTinh]
    @NgayGhiNhan DATETIME,  -- ngày cần ghi nhân số liệu thucchaydatinh
	@NgayCheckThayDoi DATETIME = NULL, -- dữ liệu phải có thay đổi vào ngày này
	@NgayDanhSoGioiHan DATETIME = NULL, -- giới  hạn tính những hợp đồng có ngày đánh số >= ngày này
	@SoHopDong NVARCHAR(100) = NULL,
	@HopDongChiTietID INT = NULL 
AS
BEGIN
	DECLARE @xulytay NVARCHAR(50) 
	SET @xulytay = IIF(@SoHopDong IS NOT NULL, N'xử lý tay ', N'')

	DELETE tcdt
	FROM ABM_data_ThucChay.dbo.ThucChayDaTinh tcdt
	LEFT JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE hdct.DmSanPhamREF = 342 AND 
		  NOT (tcdt.DmHinhThucQuangCao IN (13,42) OR tcdt.DmLoaiBannerREF IN (17,18)) AND 
		  tcdt.DotChayHopDong NOT IN ( N'NGAY', N'CPM_DonViGoi',N'Tính mới CPM DonViGoi') AND
		  tcdt.NgayThucHien = @NgayGhiNhan AND 
		  tcdt.DotChayHopDong IN (N'Đối trừ Mobile',  N'Tính lại Mobile') AND
         (@HopDongChiTietID IS NULL OR tcdt.HopDongChiTietREF = @HopDongChiTietID) AND
         (@SoHopDong IS NULL OR tcdt.SoHopDong = @SoHopDong) 

	--========================================= 1. Xác định phân bổ thay đổi tỉ lệ/banner và pb có thay đổi số lượng, đơn giá, chiết khấu ==============================
    CREATE TABLE #DmPBThayDoi (
					NgayThucHien DATETIME,
					HopDongID INT,
					HopDongChiTietREF INT,
					LoaiThayDoi INT,     --1: thay đổi thông tin hợp đồng, 2: phân bổ hủy, 3: pb thay đổi tỷ lệ / banner
					LyDo NVARCHAR(MAX),
					PBcothaydoiSL INT
					)
	BEGIN
		-- phân bổ thay đổi thông tin
        INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongID,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo
        )
        SELECT DISTINCT @NgayGhiNhan,
                        hd.HopDongID ,
                        hdct.HopDongChiTietID,
						LoaiThayDoi = IIF(hdct.DeletedStatus = 1 OR  hd.TrangThaiHopDong = 3, 2, 1),
						LyDo = CASE WHEN hd.TrangThaiHopDong = 3
									THEN @xulytay + N'hợp đồng hủy'
									WHEN hdct.DeletedStatus = 1
									THEN @xulytay + N'phân bổ bị xóa'
									ELSE @xulytay + N'phân bổ thay đổi số lượng hoặc đơn giá hoặc chiết khấu hoặc đơn vị tính'
							   END 
        FROM ABM_data_thucchay.dbo.HopDongChiTiet hdct
		INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
		WHERE(@NgayCheckThayDoi IS NULL OR (CONVERT(DATE, hd.LastModifiedAt) =  @NgayCheckThayDoi OR CONVERT(DATE, hdct.LastModifiedAt) =  @NgayCheckThayDoi))  AND 
			 (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) AND
			 hdct.DmSanPhamREF = 342 AND 
		     NOT (hdct.DmLoaiREF IN (13,42) OR hdct.DmLoaiBannerREF IN (17,18)) AND 
			 (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID) AND
             (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong) 

		-- loại TH phân bổ có thay đổi thông tin nhưng không thay đổi số lượng đánh số hoặc dongia
		UPDATE dm
		SET dm.LoaiThayDoi = 0
		FROM #DmPBThayDoi dm
		INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietREF
		OUTER APPLY (SELECT TOP 1 SoLuong , l.DonGia, l.ChietKhau, l.DonViTinh
					 FROM ABM_data_thucchay.dbo.HopDongChiTietLog l 
					 WHERE LastModifiedAt < @NgayGhiNhan AND 
						   l.HopDongChiTietREF = dm.HopDongChiTietREF
					 ORDER BY HopDongChiTietLogID desc ) l 
		WHERE @NgayCheckThayDoi IS NOT NULL AND 
			  dm.LoaiThayDoi = 1 AND 
		      hdct.DonGia = ISNULL(l.dongia, hdct.dongia) AND
			  hdct.ChietKhau = ISNULL(l.ChietKhau, hdct.ChietKhau) AND 
			  hdct.SoLuong = ISNULL(l.SoLuong, hdct.SoLuong) AND
			  hdct.DonViTinh = ISNULL(l.DonViTinh, hdct.DonViTinh)  -- thay đổi đơn vị tính thì sẽ thay đổi cách tính số lượng ký của phân bổ

		DELETE
		FROM #DmPBThayDoi
		WHERE LoaiThayDoi = 0

		-- phân bổ bị ảnh hưởng tỉ lệ hopdongchitiet/banner do phân bổ phía trên thay đổi
		INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongID,
						--DmSanPhamREF,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo )
		SELECT DISTINCT
			   @NgayGhiNhan,
		       tchdctab.HopDongREF,
			   tchdctab.HopDongChiTietREF,
			   LoaiThayDoi = 3,
			   LyDo = N'tỉ lệ phân bổ trên banner thay đổi'
		FROM ( SELECT tchdctab.DmBannerID
			   FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTietAndBanner tchdctab
			   WHERE EXISTS (SELECT HopDongChiTietREF 
							 FROM #DmPBThayDoi dm 
							 WHERE dm.HopDongChiTietREF = tchdctab.HopDongChiTietREF ) 
					 AND DaThucHienUpdateTiLe = 1 ) b
		INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTietAndBanner tchdctab ON b.DmBannerID = tchdctab.DmBannerID 
		INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = tchdctab.HopDongREF
		INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
		INNER JOIN ABM_data_thucchay.dbo.ThucChay_Mobile_DmPhanBoChungBanner_Truoc20241212 pbcu ON pbcu.ID = tchdctab.HopDongChiTietREF
		WHERE tchdctab.HopDongChiTietREF NOT IN (SELECT HopDongChiTietREF 
												 FROM #DmPBThayDoi dm )
		      AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan 
			  AND hdct.KhuyenMai = 1


		-- Phân bổ thay đổi đơn giá treo
		INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongID,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo
        )
		SELECT  DISTINCT 
		        @NgayGhiNhan,
		        hd.HopDongID,
				hdct.HopDongChiTietID,
				LoaiThayDoi = 4,
				LyDo = N'phân bổ ký gói thay đổi đơn giá treo'
		FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct 
		INNER JOIN  ABM_data_thucchay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		INNER JOIN  ABM_data_thucchay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK
		OUTER APPLY (SELECT TOP 1 l.DonGia
					 FROM ThucChayHopDongChiTiet l
		             WHERE l.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND 
					       CAST(l.LastModifiedAt AS DATE) < @NgayCheckThayDoi
					 ORDER BY l.LastModifiedAt desc) l
		WHERE   hd.TrangThaiHopDong != 3
				AND hd.DeletedStatus = 0
				AND hdct.DeletedStatus = 0
				AND CAST(tchdct.LastModifiedAt AS DATE) = @NgayCheckThayDoi
				AND hdct.DmSanPhamREF = 342 and hdct.DonViTinhREF = 10
				AND NOT (hdct.DmLoaiREF IN (13,42) OR hdct.DmLoaiBannerREF IN (17,18)) 
				
				AND ISNULL(l.DonGia, 0) <> ISNULL(tchdct.DonGia, 0) 

				AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				AND NOT EXISTS(SELECT TOP 1 ID FROM ABM_data_thucchay.dbo.ThucChay_Mobile_DmPhanBoChungBanner_Truoc20241212 cu WHERE cu.ID = hdct.HopDongChiTietID )
				AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID) 
				AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)

				AND tchdct.HopDongChiTietREF NOT IN (SELECT HopDongChiTietREF 
												       FROM #DmPBThayDoi dm )


	END	
     
	--========================================= 2. Xác định thucchayID của các phân bổ trên ====================================================================================================================
	CREATE TABLE #DmTinhLai 
				(	ThucChayID INT,
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

					SoLuongThucChay_GhiNhan FLOAT,
					SoLuongKM_GhiNhan INT,
					ThanhTienThucChay_GhiNhan FLOAT,
					ThanhTienKM_GhiNhan FLOAT,

					SoLuongLechTreoHa INT,
					ThanhTienLechTreoHa FLOAT,
			
					LoaiXuLy INT,  --1: Phân bổ ký gói, 2: Pb thường
					LyDo NVARCHAR(MAX))
	INSERT INTO #DmTinhLai
	(		ThucChayID, 
			TenWebsite,
			DmBannerREF ,
			bannerType ,
			DonViTinhTreo,
		    NgayThucHien ,
			HopDongChiTietREF ,
			ChietKhau,
			SoLuongDanhSoPhanBo,
			ThanhTienSauCKPhanBo ,
			ThanhTienKMPhanBo ,

			TongViewThucChay ,
			TongClickThucChay ,
			SoLuongThucChay,

			LoaiXuLy,

			LyDo)
	SELECT  tc.ID,
			tc.TenWebsite,
			tc.DmBannerREF,
			tc.BannerType,
			CASE WHEN tchdct.DmDonViTinhREF = 1 THEN N'CPM'
				 WHEN tchdct.DmDonViTinhREF = 2 THEN N'CPC'
				 ELSE ''
			END,
			@NgayGhiNhan,
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

			LoaiXuLy = IIF(hdct.DonViTinh = N'Gói', 1, 2),

			dm.LyDo 
	FROM ABM_data_thucchay.dbo.thucchay tc
	INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTietAndBanner tchdctab 
																 ON    tchdctab.DmBannerID = CONVERT(NVARCHAR(50),tc.DmBannerREF) 
																	   AND tchdctab.DeletedStatus = 0
	INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct ON tchdct.DmBannerREF = CONVERT(NVARCHAR(50),tc.DmBannerREF) AND 
																	  tchdctab.HopDongChiTietREF = tchdct.HopDongChiTietREF 
																	  AND tchdct.DeletedStatus = 0
	INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tchdctab.HopDongChiTietREF 
	INNER JOIN  ABM_data_thucchay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN  ABM_data_thucchay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK
	INNER JOIN ABM_data_thucchay.dbo.ThucChay_Mobile_DmPhanBoChungBanner_Truoc20241212 pbcu ON pbcu.ID = tchdctab.HopDongChiTietREF 
	WHERE   hd.TrangThaiHopDong <> 3
			AND hd.DeletedStatus = 0 
			AND CONVERT(DATE,tc.NgayThucHien) < dm.NgayThucHien  -- thucchay tại ngaythuchien sẽ được tính mới ở SP ghi nhận phát sinh 
			AND tc.TypeProduct = 10 
			AND tc.DmWebsiteREF <> 0
			AND dm.LoaiThayDoi IN (1,3)
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
				dm.LyDo 

	UPDATE dm
	SET DonGiaChay = ISNULL(dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau ( 	dm.HopDongChiTietREF, 
																				dbo.ThucChay_Mobile_GetDonViTinh(hdct.DonViTinh, ISNULL(dm.DonViTinhTreo, '')),
																				dm.BannerType,
																				dm.NgayThucHien) , 0)
	FROM #DmTinhLai dm
	INNER JOIN  ABM_data_thucchay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietREF

	-- tính theo phương pháp mới
	INSERT INTO #DmTinhLai( 
			ThucChayID, 
			TenWebsite,
			DmBannerREF ,
			bannerType ,
			DonViTinhTreo,
		    NgayThucHien ,
			HopDongChiTietREF ,
			ChietKhau,
			SoLuongDanhSoPhanBo,
			ThanhTienSauCKPhanBo,
			ThanhTienKMPhanBo,

			TongViewThucChay ,
			TongClickThucChay ,
			SoLuongThucChay,
			DonGiaChay,
			
			LoaiXuLy,
			
			LyDo)
	SELECT  DISTINCT
	        tc.ID,
			tc.TenWebsite,
			tc.DmBannerREF ,
			tc.BannerType,
			CASE WHEN tchdct.DmDonViTinhREF = 1 THEN N'CPM'
				 WHEN tchdct.DmDonViTinhREF = 2 THEN N'CPC'
				 ELSE ''
			END,
			@NgayGhiNhan,
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

			LoaiXuLy = IIF(hdct.DonViTinh = N'Gói', 1, 2),

			dm.LyDo 
	FROM ABM_data_thucchay.dbo.thucchay tc
	INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct ON tchdct.DmBannerREF = CONVERT(NVARCHAR(50),tc.DmBannerREF) AND tchdct.DeletedStatus = 0
	INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tchdct.HopDongChiTietREF 
	INNER JOIN  ABM_data_thucchay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tc.HopDongChiTietREF 
	INNER JOIN  ABM_data_thucchay.dbo.HopDong hd on hd.HopDongID = hdct.HopDongFK
	WHERE   hd.TrangThaiHopDong <> 3
			AND hd.DeletedStatus = 0 
			AND CONVERT(DATE,tc.NgayThucHien) < dm.NgayThucHien  -- thucchay tại ngaythuchien sẽ được tính mới ở SP ghi nhận phát sinh 
			AND tc.TypeProduct = 10 
			AND tc.DmWebsiteREF <> 0
			AND dm.LoaiThayDoi IN (1,3,4)
			AND NOT EXISTS (SELECT TOP 1 ID FROM  ABM_data_thucchay.dbo.ThucChay_Mobile_DmPhanBoChungBanner_Truoc20241212 pbcu WHERE pbcu.ID = tc.HopDongChiTietREF   )

	DELETE
	FROM #DmTinhLai
	WHERE SoLuongThucChay = 0

	UPDATE dm
	SET dm.DmNhanHangREF = ISNULL(tchdct.DmNhanHangREF, '')
	FROM #DmTinhLai dm
	OUTER APPLY  (SELECT STUFF ((   SELECT DISTINCT  ',' + tchdct.DmNhanHangREF
									FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTiet  tchdct
									WHERE DeletedStatus = 0 AND 
										  tchdct.HopDongChiTietREF = dm.HopDongChiTietREF AND 
										  tchdct.DmBannerREF = CONVERT(NVARCHAR(50),dm.DmBannerREF) 
									FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 
									1, 1, '') AS DmNhanHangREF
							) tchdct 

	--========================================= 3. Xác định lệch treo hạ và ghi nhận của các thucchayID trên ==========================
	-- Với TH phân bổ đơn vị gói (loại xử lý = 1) thì check vượt thành tiền, còn lại thì check vượt số lượng
	;WITH CTE_Base AS (
		SELECT 
		  ThucChayID,
		  SoLuongThucChay,
		  SoLuongDanhSoPhanBo,
		  HopDongChiTietREF,
		  ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ThucChayID) AS RowNum
		FROM #DmTinhLai
		WHERE LoaiXuLy = 2
	  ),
	  CTE_Recursive AS (
		SELECT 
		  ThucChayID,
		  SoLuongThucChay,
		  SoLuongDanhSoPhanBo,
		  HopDongChiTietREF,
		  RowNum,
		  TichLuyGhiNhan = IIF (SoLuongThucChay>= SoLuongDanhSoPhanBo,
								SoLuongDanhSoPhanBo ,  SoLuongThucChay ),
		  ThucChayGhiNhan = IIF (SoLuongThucChay>= SoLuongDanhSoPhanBo,
								SoLuongDanhSoPhanBo ,  SoLuongThucChay )
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
	FROM #DmTinhLai temp
	INNER JOIN CTE_Recursive sl ON sl.ThucChayID = temp.ThucChayID
	WHERE temp.LoaiXuLy = 2
	OPTION (MAXRECURSION 0);

	UPDATE dm
	SET 	ThanhTienThucChay_GhiNhan = SoLuongThucChay_GhiNhan*DonGiaChay*(1-dm.ChietKhau/100),
			ThanhTienKM_GhiNhan = IIF(ChietKhau = 100, SoLuongKM_GhiNhan*DonGiaChay, 0),
			ThanhTienLechTreoHa = SoLuongLechTreoHa*DonGiaChay
	FROM #DmTinhLai dm
	WHERE LoaiXuLy = 2


	;WITH CTE_Base AS (
			SELECT 
					  ThucChayID,
					  ThanhTienSauCK = SoLuongThucChay*DonGiaChay*(1-ChietKhau/100),
					  ThanhTienKM = IIF(ChietKhau = 100, SoLuongThucChay*DonGiaChay, 0),
					  ThanhTienSauCKPhanBo,
					  ThanhTienKMPhanBo,
					  HopDongChiTietREF,
					  ROW_NUMBER() OVER (PARTITION BY HopDongChiTietREF ORDER BY ThucChayID) AS RowNum
			FROM #DmTinhLai
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
					  TichLuyTTGhiNhan = IIF (ThanhTienSauCK>= ThanhTienSauCKPhanBo,
											  ThanhTienSauCKPhanBo ,  ThanhTienSauCK ),
					  ThucChayTTGhiNhan = IIF (ThanhTienSauCK>= ThanhTienSauCKPhanBo,
											   ThanhTienSauCKPhanBo,  ThanhTienSauCK ),
					  TichLuyKMGhiNhan = IIF (ThanhTienKM>= ThanhTienKMPhanBo,
											  ThanhTienKMPhanBo ,  ThanhTienKM ),
					  ThucChayKMGhiNhan = IIF (ThanhTienKM>= ThanhTienKMPhanBo,
											   ThanhTienKMPhanBo,  ThanhTienKM )				  

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
	FROM #DmTinhLai temp
	INNER JOIN CTE_Recursive sl ON sl.ThucChayID = temp.ThucChayID
	WHERE temp.LoaiXuLy = 1
	OPTION (MAXRECURSION 0);

	UPDATE  dm
	SET 	dm.SoLuongThucChay_GhiNhan = IIF(DonGiaChay<> 0 and ChietKhau <> 100, ThanhTienThucChay_GhiNhan/((1-ChietKhau/100)*DonGiaChay), 0),
			dm.SoLuongKM_GhiNhan = IIF(DonGiaChay<> 0 and ChietKhau = 100, ThanhTienKM_GhiNhan/DonGiaChay, 0)
	FROM #DmTinhLai dm
	WHERE LoaiXuLy = 1

	UPDATE  dm
	SET 	dm.SoLuongLechTreoHa = SoLuongThucChay - SoLuongKM_GhiNhan - SoLuongThucChay_GhiNhan,
			dm.ThanhTienLechTreoHa = (SoLuongThucChay - SoLuongKM_GhiNhan - SoLuongThucChay_GhiNhan)*DonGiaChay
	FROM #DmTinhLai dm
	WHERE LoaiXuLy = 1

	--========================================= 4. Tiến hành đối trừ  ===========================================================
	INSERT INTO ABM_data_ThucChay.dbo.[ThucChayDaTinh]
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
		, N'Đối trừ Mobile' AS DotChayHopDong
		, SoLuongDotChayHD
		, DotChayBooking
		, SoLuongDotChayBooking
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
		, dm.NgayThucHien
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
		, IIF(pbcu.id IS NOT NULL, N'PP cũ ', N'PP mới ') + N'Đối trừ: SP tối ưu [dbo].[ThucChay_mobile_GhiNhanThayDoi_ThucChayDaTinh] do ' + dm.LyDo AS GhiChu
FROM    ABM_data_thucchay.dbo.[ThucChayDaTinh] tcdt
INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tcdt.HopDongChiTietREF 
LEFT JOIN ABM_data_thucchay.dbo.ThucChay_Mobile_DmPhanBoChungBanner_Truoc20241212 pbcu ON pbcu.id = dm.HopDongChiTietREF
WHERE     tcdt.DmSanPhamREF = 342 AND 
		  NOT (tcdt.DmHinhThucQuangCao IN (13,42) OR tcdt.DmLoaiBannerREF IN (17,18)) AND 
		 -- tcdt.DotChayHopDong NOT IN ( N'NGAY', N'CPM_DonViGoi') and
		  tcdt.NgayThucHien < dm.NgayThucHien
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
		, pbcu.id
		, SoLuongDotChayHD
		, DotChayBooking
		, SoLuongDotChayBooking
	HAVING SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) <> 0 OR
		   SUM(SoLuongThucChayLechTreoHa) <> 0 OR
		   SUM(ThanhTienLechTreoHa) <> 0 OR
		   SUM(SoLuongThucChay + SoLuongThayDoi) <> 0 OR
	       SUM(SoLuongThucChayKM + SoLuongKMThayDoi) <> 0 OR
		   SUM(ThanhTienKM + GiaTriKMThayDoi) <> 0
	--========================================= 5. Tiến hành tính lại
	DECLARE @DmTinhLaiTongHop DataType_Thucchay_Mobile_DmTinhLaiTongHop2
	INSERT INTO @DmTinhLaiTongHop
	(
		   HopDongChiTietREF,
		   NgayThucHien,
		   DmBannerREF,
		   TenWebsite,
		   DmNhanHangREF,
		   bannerType,
		   DonViTinhTreo,

		   Dongia,

		   SoLuongThucChay_GhiNhan,
		   SoLuongKM_GhiNhan ,
		   SoLuongLechTreoHa ,

		   ThanhTienThucChay_GhiNhan,
		   ThanhTienKM_GhiNhan,
		   ThanhTienLechTreoHa,
		   LyDo
	)
	SELECT				tcgn.HopDongChiTietREF,
						tcgn.NgayThucHien,
						tcgn.DmBannerREF,
						tcgn.TenWebsite,
						tcgn.DmNhanHangREF,
						tcgn.bannerType,
						DonvitinhTreo,

						tcgn.DonGiaChay,

						SoLuongThucChay_GhiNhan = SUM(ISNULL(tcgn.SoLuongThucChay_GhiNhan,0)) ,
						SoLuongKM_GhiNhan = SUM(ISNULL(tcgn.SoLuongKM_GhiNhan,0)) ,
						SoLuongLechTreoHa = SUM(ISNULL(tcgn.SoLuongLechTreoHa,0)),

						ThanhTienThucChay_GhiNhan = SUM(ISNULL(ThanhTienThucChay_GhiNhan,0)) ,
						ThanhTienKM_GhiNhan = SUM(ISNULL(ThanhTienKM_GhiNhan,0)) ,
						ThanhTienLechTreoHa = SUM(ISNULL(ThanhTienLechTreoHa,0)) ,
						tcgn.LyDo 
	FROM #DmTinhLai tcgn
	INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcgn.HopDongChiTietREF 
	GROUP BY	tcgn.HopDongChiTietREF,
				tcgn.NgayThucHien,
				tcgn.DmBannerREF,
				tcgn.TenWebsite,
				tcgn.DmNhanHangREF,
				tcgn.bannerType,
				tcgn.DonvitinhTreo,
				tcgn.DonGiaChay,
				tcgn.LyDo 
	HAVING SUM(tcgn.SoLuongThucChay_GhiNhan) <> 0 OR 
			SUM(tcgn.SoLuongLechTreoHa) <> 0  OR
			SUM(SoLuongKM_GhiNhan) <> 0

	EXEC [dbo].[ThucChay_Mobile_DoiTruTinhLai_ThucChayDaTinh] @DmTinhLaiTongHop

	DROP TABLE #DmTinhLai
	DROP TABLE #DmPBThayDoi

END

```
