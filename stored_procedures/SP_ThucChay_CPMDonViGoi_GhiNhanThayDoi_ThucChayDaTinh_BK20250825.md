# Stored Procedure: `ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh_BK20250825`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-08-25 15:47:25.980000
- **Ngày sửa cuối**: 2025-08-25 15:47:25.980000

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
CREATE PROCEDURE [dbo].[ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh_BK20250825]
    @NgayGhiNhan DATE,
    @NgayCheckThayDoi DATE = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL ,
	@HopDongChiTietID INT = NULL
AS
BEGIN

    IF @SoHopDong IS NOT NULL 
	BEGIN 
		SET @NgayDanhSoGioiHan = NULL
		SET @NgayCheckThayDoi = NULL
	END

	DELETE FROM ABM_Data_ThucChay.dbo.thucchaydatinh
	WHERE	convert(date,NgayThucHien) = @NgayGhiNhan
			AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
			AND DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299, 821, 5133)
			AND DotChayHopDong IN ( N'Đối trừ CPM donvigoi', N'Tính lại CPMdonvigoi')
		  AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
		  AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)

	--========================================= 1. Xác định phân bổ thay đổi tỉ lệ/banner và pb có thay đổi số lượng, đơn giá, chiết khấu ==============================
    CREATE TABLE #DmPBThayDoi (
					NgayThucHien DATETIME,
					HopDongChiTietREF INT,
					LoaiThayDoi INT,     --1: thay đổi thành tiền phân bổ, 2: phân bổ hủy, 3: thay đổi đơn giá trên treo, 4: hủy treo
					LyDo NVARCHAR(MAX)
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
									ELSE N'phân bổ thay đổi thành tiền KM hoặc sau CK'
							   END 
        FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
		WHERE(CONVERT(DATE, hd.LastModifiedAt) =  @NgayCheckThayDoi OR CONVERT(DATE, hdct.LastModifiedAt) =  @NgayCheckThayDoi)  AND 
			 (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) AND
			 hdct.DonViTinhREF =10 AND
			 hdct.DmSanPhamREF IN (339, 240, 598, 5056, 733, 5299, 821, 5133) AND 
			 NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) 

		-- loại TH phân bổ có thay đổi thông tin nhưng không thay đổi thành tiền
		DELETE dm
		FROM #DmPBThayDoi dm
		INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietREF
		OUTER APPLY (SELECT TOP 1 ThanhTienKM = IIF(l.ChietKhau = 100,  l.SoLuong*l.dongia, 0),
		                          ThanhTienSauCK = IIF(l.ChietKhau <> 100,  l.SoLuong*l.dongia*(100-l.ChietKhau/100), 0)
					 FROM dbo.HopDongChiTietLog l 
					 WHERE LastModifiedAt < @NgayCheckThayDoi AND 
						   l.HopDongChiTietREF = dm.HopDongChiTietREF
					 ORDER BY HopDongChiTietLogID desc ) l 
		WHERE   ((IIF(hdct.ChietKhau = 100,  hdct.SoLuong*hdct.dongia, 0) = l.ThanhTienKM AND 
				  IIF(hdct.ChietKhau <> 100,  hdct.SoLuong*hdct.dongia*(100-hdct.ChietKhau/100), 0) = l.ThanhTienSauCK ) OR
				  l.ThanhTienSauCK IS NULL ) AND 
				  dm.LoaiThayDoi = 1 

		IF @SoHopDong IS NOT NULL
		BEGIN 
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
										THEN N'xử lý tay hợp đồng hủy'
										WHEN hdct.DeletedStatus = 1
										THEN N'xử lý tay phân bổ bị xóa'
										ELSE N'xử lý tay phân bổ'
								   END 
			FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
			WHERE hdct.DonViTinhREF =10 AND
				 hdct.DmSanPhamREF IN (339, 240, 598, 5056, 733, 5299, 821, 5133) AND 
				 NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) AND 
				 hd.SoHopDong = @SoHopDong AND 
				 (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID )
		END

		-- phân bổ có data thực chạy trên thucchaytrueview, thucchay  thay đổi thông tin treo hoặc hủy treo, nativeads và onimage không bắt thay đổi này
        INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo
        )
        SELECT DISTINCT @NgayGhiNhan,
                        hdct.HopDongChiTietID,
						LoaiThayDoi = IIF(tchdct.DeletedStatus = 1, 4, 3),
						LyDo = CASE WHEN tchdct.DeletedStatus = 1
									THEN N'phân bổ hủy treo'
									ELSE N'phân bổ thay đổi đơn giá treo'
							   END
        FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
		WHERE	 (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) AND
				 hdct.DonViTinhREF =10 AND
				 hdct.DmSanPhamREF IN (339, 240, 598, 5056, 733,735, 5299) AND 
				 NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) AND
				 hd.TrangThaiHopDong != 3 AND
				 hd.DeletedStatus = 0 AND 
				 hdct.DeletedStatus = 0 AND 
				 tchdct.DmSanPhamREF NOT IN (5133, 821,735, 598) AND  -- không bắt thay đổi đơn giá treo và hủy treo của onimage và nativeads  
				 CAST(tchdct.LastModifiedAt AS DATE) = @NgayCheckThayDoi AND
                 hdct.HopDongChiTietID  NOT IN (SELECT HopDongChiTietREF FROM #DmPBThayDoi)

		-- loại TH thay đổi thông tin treo nhưng không thay đổi đơn giá treo hoặc hủy treo nhưng trước đó không có log treo  
		DELETE dm
		FROM #DmPBThayDoi dm
		OUTER APPLY (SELECT TOP 1 dongia = IIF( tchdct.DmDonViTinhREF = 1, tchdct.DonGia/1000, tchdct.DonGia), tchdct.DmSanPhamREF
					 FROM dbo.ThucChayHopDongChiTiet tchdct 
					 WHERE tchdct.LastModifiedAt = @NgayCheckThayDoi AND 
						   tchdct.HopDongChiTietREF = dm.HopDongChiTietREF AND
                           tchdct.DeletedStatus = 0 AND 
						   tchdct.DmSanPhamREF IN (339, 240, 342, 598,735, 5056, 5299) AND 
						   tchdct.DmHinhThucQuangCaoREF NOT IN (42,13) AND 
						   --tchdct.DmDonViTinhREF IN (1,2,32) AND --haidh comment cho nay xem lai do du lieu lien quan den ca donvi bai chua dc chuan hoa
						   tchdct.CreatedAt >= '2021-03-01'  
					 ORDER BY tchdct.ThucChayHopDongChiTietID desc ) tchdct 
		OUTER APPLY (SELECT TOP 1 dongia = IIF( l.DmDonViTinhREF = 1, l.DonGia/1000, l.DonGia), l.DmSanPhamREF
					 FROM dbo.ThucChayHopDongChiTietLog l 
					 WHERE l.LastModifiedAt < @NgayCheckThayDoi AND 
						   l.HopDongChiTietREF = dm.HopDongChiTietREF AND
                           l.DeletedStatus = 0 AND 
						   l.DmSanPhamREF IN (339, 240, 342, 598,735, 5056, 5299) AND 
						   l.DmHinhThucQuangCaoREF NOT IN (42,13) AND 
						   --l.DmDonViTinhREF IN (1,2,32) AND --haidh comment cho nay xem lai do du lieu lien quan den ca donvi bai chua dc chuan hoa
						   l.CreatedAt >= '2021-03-01'  
					 ORDER BY l.ThucChayHopDongChiTietLogID desc ) l 
		WHERE l.dongia IS NOT NULL AND
		      l.DmSanPhamREF = tchdct.DmSanPhamREF AND 
		      ISNULL(tchdct.dongia, 0) = l.dongia AND 
			  dm.LoaiThayDoi IN (3, 4)

		INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo )
		SELECT DISTINCT
			   @NgayGhiNhan,
			   tchdctab.HopDongChiTietREF,
			   LoaiThayDoi = 5,
			   LyDo = N'phân bổ chạy nativeads/onimage có tỉ lệ phân bổ trên banner thay đổi'
		FROM ( SELECT tchdctab.DmBannerID
			   FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Native_Ads tchdctab
			   WHERE EXISTS (SELECT HopDongChiTietREF 
							 FROM #DmPBThayDoi dm 
							 WHERE dm.HopDongChiTietREF = tchdctab.HopDongChiTietREF AND
							       dm.LoaiThayDoi in (1,2)) 
					 AND DaThucHienUpdateTiLe = 1 
					 AND tchdctab.DeletedStatus = 0) b
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Native_Ads tchdctab ON b.DmBannerID = tchdctab.DmBannerID 
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = tchdctab.HopDongREF
		WHERE tchdctab.HopDongChiTietREF NOT IN (SELECT HopDongChiTietREF FROM #DmPBThayDoi dm )
		     AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
			 AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
						    WHERE iv.HopDongChiTietREF = tchdctab.HopDongChiTietREF )  
			 AND NOT EXISTS (SELECT top (1) tl.HopDongChiTietID FROM ABM_Data_ThucChay.dbo.GhiNhanThanhLy tl 
						     WHERE tl.HopDongChiTietID = tchdctab.HopDongChiTietREF )
			 AND tchdctab.DaThucHienUpdateTiLe = 1
			 AND tchdctab.DeletedStatus = 0


	END	
     
	--========================================= 2. Xác định thucchayID của các phân bổ trên ====================================================================================================================
	CREATE TABLE #DmTinhLai 
				(	ThucChayID INT IDENTITY(1,1),
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

					SoLuongThucChay_GhiNhan INT,
					SoLuongLechTreoHa INT,
					SoLuongKM_GhiNhan INT,
					ThanhTienTC_GhiNhan FLOAT,
					ThanhTienLechTreoHa FLOAT,
					ThanhTienKM_GhiNhan FLOAT,

					LyDo NVARCHAR(MAX))
	INSERT INTO #DmTinhLai
	(				DmWebsiteREF ,
					TenWebsite ,
					DmBannerREF ,
					NgayThucHien ,
					HopDongChiTietREF ,
					DonViTinh ,
					DmSanPhamREF ,
					DmNhanHangREF,
					ChietKhau,
					SoLuongThucChay ,
					ThanhTienSauCK ,
					SoLuongKM ,
					ThanhTienKM ,

					LyDo)
	SELECT  tc.SiteID,
			tc.SiteName,
			tc.bannerid,
			@NgayGhiNhan,
			tchdct.HopDongChiTietID,
			tchdct.DmDonvitinhREF,
			tc.DmSanPhamREF,
			DmNhanHangREF = tchdct.DanhSachNhanHangREF,
			ChietKhau = tchdct.ChietKhau,
			SoLuongThucChay = ISNULL(IIF(tchdct.ChietKhau <> 100, tc.True_View, 0),0),
			ThanhTienSauCK = ISNULL(IIF(tchdct.ChietKhau <> 100, tc.True_View*tchdct.DonGia*(100-tchdct.ChietKhau)/100, 0),0),
			SoLuongKM = ISNULL(IIF(tchdct.ChietKhau = 100, tc.True_View, 0),0),
			ThanhTienKM = ISNULL(IIF(tchdct.ChietKhau = 100, tc.True_View*tchdct.DonGia, 0),0),
			tchdct.Lydo
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
						Lydo = dm.LyDo,
						hdct.DanhSachNhanHangREF
	             FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
				 INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
				 INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = hdct.HopDongChiTietID
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
					   dm.LoaiThayDoi IN (1,3,4,5)
                ) tchdct ON	tc.bannerid = CONVERT(NVARCHAR(50),tchdct.DmBannerREF) 
								AND tc.DmSanPhamREF = tchdct.DmSanPhamREF 
								AND tc.SoHopDong = tchdct.SoHopDong
	WHERE   tc.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
			AND tchdct.DmDonvitinhREF = N'TRUE VIEW'
			AND CONVERT(DATE,tc.NgayThucHien) < @NgayGhiNhan
	UNION ALL
	SELECT  tc.DmWebsiteREF,
			tc.TenWebsite,
			tc.DmBannerREF,
			@NgayGhiNhan,
			tchdct.HopDongChiTietID,
			tchdct.DmDonvitinhREF,
			tc.DmSanPhamREF,
			DmNhanHangREF = tchdct.DanhSachNhanHangREF,
			ChietKhau = tchdct.ChietKhau,
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
			tchdct.LyDo
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
						dm.LyDo,
						hdct.DanhSachNhanHangREF
	             FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
				 INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
				 INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = hdct.HopDongChiTietID
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
                       dm.LoaiThayDoi IN (1,3,4,5)
                ) tchdct ON	tc.DmBannerREF = CONVERT(NVARCHAR(50),tchdct.DmBannerREF) 
								AND tc.DmSanPhamREF = tchdct.DmSanPhamREF 
								AND tc.SoHopDong = tchdct.SoHopDong
	WHERE tc.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
		  AND tchdct.DmDonvitinhREF IN (N'VIEW', N'CLICK')
		  AND CONVERT(DATE,tc.NgayThucHien) < @NgayGhiNhan

	UNION ALL
	SELECT  tc.DmWebsiteID,
	        tc.TenWebsite,
			tc.DmBannerID,
			@NgayGhiNhan,
			tchdctab.HopDongChiTietREF,
			tc.DonViTinh,
	        tc.DmSanPhamREF,
			-1,
			hdct.ChietKhau,
			SoLuongThucChay = SUM(tc.SoLuongThucChay * tchdctab.TiLeThucChayHDCTSoVoiBanner/100 ),
			ThanhTienSauCK = SUM(tc.ThanhTienThucChaySauCK * tchdctab.TiLeThucChayHDCTSoVoiBanner/100 ),
			SoLuongThucChayKM = SUM(tc.SoLuongThucChayKM * tchdctab.TiLeThucChayHDCTSoVoiBanner/100),
			ThanhTienThucChayKM = SUM(tc.ThanhTienThucChayKM * tchdctab.TiLeThucChayHDCTSoVoiBanner/100),
			dm.LyDo
	FROM ABM_Data_ThucChay.dbo.ThucChay_Native_Ads tc
	INNER JOIN  ABM_Data_ThucChay.dbo.HopDong hd on hd.SoHopDong = tc.SoHopDong
	INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Native_Ads tchdctab ON tchdctab.DmBannerID = CONVERT(NVARCHAR(50),tc.DmBannerID) 
																					  AND tchdctab.DeletedStatus = 0
																					  AND tc.DmSanPhamREF = tchdctab.DmSanPhamID 
																					  AND hd.HopDongID = tchdctab.HopDongREF
																					  AND tchdctab.DaThucHienUpdateTiLe = 1
    INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct on hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN  #DmPBThayDoi dm ON dm.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE   hd.TrangThaiHopDong != 3
			AND hd.DeletedStatus = 0
			AND NOT ( hdct.DmLoaiREF IN ( 13, 42 ) OR hdct.DmLoaiBannerREF IN (17, 18)) 
			AND  hdct.DonViTinhREF = 10
			AND CONVERT(DATE,tc.NgayThucHien) < @NgayGhiNhan
			AND tc.DmWebsiteID <> 0
			AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory iv 
						   WHERE iv.HopDongChiTietREF = tchdctab.HopDongChiTietREF)
			AND dm.LoaiThayDoi IN (1,3,4,5)
	GROUP BY	tc.DmSanPhamREF,
				tc.DmWebsiteID,
				tc.TenWebsite,
				tc.DmBannerID,
				tc.DonViTinh,
				CONVERT(DATE,tc.NgayThucHien),
				tchdctab.HopDongChiTietREF,
				hdct.ChietKhau,
				dm.LyDo

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
					   CONVERT(DATE,tchdct.LastModifiedAt) < @NgayGhiNhan AND
					   (@SoHopDong IS NULL OR hd.SoHopDong= @SoHopDong) AND
                       (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
	)BAI
	WHERE 1=1

	DELETE 
	FROM #DmTinhLai
	WHERE ThanhTienSauCK = 0 AND ThanhTienKM = 0

	-- update nhãn hàng cho thực chạy onimage và native ads
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
	WHERE dm.DmNhanHangREF = -1 

	UPDATE dm
	SET dm.DonGiaSauCK = IIF(SoLuongThucChay = 0, 0, ThanhTienSauCK / SoLuongThucChay),
	    dm.DonGiaKM = IIF(SoLuongKM = 0, 0, ThanhTienKM / SoLuongKM)
	FROM #DmTinhLai dm 

	UPDATE temp
	SET temp.ThanhTienSauCKPhanBo =hdct.ThanhTien,
		temp.ThanhTienKMPhanBo = IIF(hdct.ChietKhau = 100, hdct.SoLuong*hdct.DonGia, 0)
	FROM #DmTinhLai temp
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = temp.HopDongChiTietREF


	--========================================= 3. Xác định lệch treo hạ và ghi nhận của các thucchayID trên ==========================
	
	;WITH CTE_Base AS (
			SELECT  ThucChayID,
					TongThucChayTruocDo = IIF(ChietKhau <> 100,
											  COALESCE(	SUM(ThanhTienSauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ThucChayID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
														), 0),
											  0),
					TongThucChayDenHT =   IIF(ChietKhau <> 100,
											  COALESCE(	SUM(ThanhTienSauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ThucChayID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
											  0),
					TongThucChayKMTruocDo=  IIF(ChietKhau = 100,
												COALESCE(	SUM(ThanhTienKM) OVER (
															PARTITION BY HopDongChiTietREF 
															ORDER BY ThucChayID  
															ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
															), 0),
												0),
					TongThucChaKMDenHT =   IIF(ChietKhau = 100,
											   COALESCE(SUM(ThanhTienKM) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ThucChayID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
											   0)
			FROM #DmTinhLai )

	UPDATE temp
	SET  	temp.ThanhTienTC_GhiNhan = CASE WHEN sl.TongThucChayTruocDo > ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo THEN 0
											WHEN sl.TongThucChayTruocDo > ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT <= ThanhTienSauCKPhanBo THEN sl.TongThucChayDenHT - sl.TongThucChayTruocDo
											--WHEN sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo THEN ThanhTienSauCKPhanBo - sl.TongThucChayTruocDo
											WHEN (sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo) AND (DonViTinh <> N'BÀI') THEN ThanhTienSauCKPhanBo - sl.TongThucChayTruocDo
											WHEN (sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo) AND (DonViTinh = N'BÀI') THEN 0
											WHEN sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT <= ThanhTienSauCKPhanBo THEN temp.ThanhTienSauCK
										END, 
			temp.ThanhTienKM_GhiNhan = CASE	WHEN sl.TongThucChayKMTruocDo > ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo THEN 0
											WHEN sl.TongThucChayKMTruocDo > ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT <= ThanhTienKMPhanBo THEN sl.TongThucChaKMDenHT - sl.TongThucChayKMTruocDo
											--WHEN sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo THEN ThanhTienKMPhanBo - sl.TongThucChayKMTruocDo
											WHEN (sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo) AND (DonViTinh <> N'BÀI') THEN ThanhTienKMPhanBo - sl.TongThucChayKMTruocDo
											WHEN (sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo) AND (DonViTinh = N'BÀI') THEN 0
											WHEN sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT <= ThanhTienKMPhanBo THEN temp.ThanhTienKM
									  END 
	FROM #DmTinhLai temp
	INNER JOIN CTE_Base sl ON sl.ThucChayID = temp.ThucChayID

	UPDATE temp
	SET  	SoLuongThucChay_GhiNhan = IIF(ChietKhau <> 100, ThanhTienTC_GhiNhan/DonGiaSauCK, 0),
			SoLuongKM_GhiNhan = IIF(ChietKhau = 100, ThanhTienKM_GhiNhan/DonGiaKM, 0),
			SoLuongLechTreoHa = IIF(ChietKhau = 100, SoLuongKM - ThanhTienKM_GhiNhan/DonGiaKM, SoLuongThucChay - ThanhTienTC_GhiNhan/DonGiaSauCK) ,
			--ThanhTienLechTreoHa = IIF(ChietKhau = 100, ThanhTienKM - ThanhTienKM_GhiNhan, ThanhTienSauCK - ThanhTienTC_GhiNhan)
			ThanhTienLechTreoHa = IIF(ChietKhau = 100, ThanhTienKM - ThanhTienKM_GhiNhan, (ThanhTienSauCK/(100-ChietKhau))*100 - (ThanhTienTC_GhiNhan/(100-ChietKhau))*100)
	FROM #DmTinhLai temp

	--========================================= 4. Tiến hành đối trừ  ===========================================================
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
		, N'Đối trừ CPM donvigoi' AS DotChayHopDong
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
		, N'Đối trừ: SP tối ưu [dbo].[ThucChay_CPMDonViGoi_GhiNhanThayDoi_ThucChayDaTinh] do ' + dm.LyDo AS GhiChu
FROM    ABM_Data_ThucChay.dbo.thucchaydatinh tcdt
INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tcdt.HopDongChiTietREF 
WHERE       --NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13,42))
			--AND tcdt.DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299, 821, 5133)
			--AND 
			tcdt.NgayThucHien < @NgayGhiNhan
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
	DECLARE @Thucchay_CPMDonViGoi_DmTinhlai DataType_Thucchay_CPMDonViGoi_DmTinhlai
	INSERT INTO @Thucchay_CPMDonViGoi_DmTinhlai
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
		SoLuongThucChay_GhiNhan ,
		SoLuongLechTreoHa ,
		SoLuongKM_GhiNhan ,
		ThanhTienTC_GhiNhan ,
		ThanhTienLechTreoHa ,
		ThanhTienKM_GhiNhan ,

		LyDo 
	)
	SELECT						
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

		SoLuongThucChay_GhiNhan = SUM(ISNULL(SoLuongThucChay_GhiNhan, 0)),
		SoLuongLechTreoHa = SUM(ISNULL(SoLuongLechTreoHa, 0)),
		SoLuongKM_GhiNhan = SUM(ISNULL(SoLuongKM_GhiNhan, 0)),
		ThanhTienTC_GhiNhan = SUM(ISNULL(ThanhTienTC_GhiNhan, 0)),
		ThanhTienLechTreoHa = SUM(ISNULL(ThanhTienLechTreoHa, 0)),
		ThanhTienKM_GhiNhan = SUM(ISNULL(ThanhTienKM_GhiNhan, 0)),

		LyDo 
	FROM #DmTinhLai tcgn
	GROUP BY	DmWebsiteREF ,
				TenWebsite ,
				DmBannerREF ,
				NgayThucHien ,
				HopDongChiTietREF ,
				DonViTinh ,
				DonGiaSauCK ,
				DonGiaKM ,
				DmSanPhamREF,
				DmNhanHangREF,
				LyDo

	EXEC [dbo].[ThucChay_CPMDonViGoi_DoiTruTinhLai_ThucChayDaTinh] @Thucchay_CPMDonViGoi_DmTinhlai

	DROP TABLE #DmTinhLai
	DROP TABLE #DmPBThayDoi

END

```
