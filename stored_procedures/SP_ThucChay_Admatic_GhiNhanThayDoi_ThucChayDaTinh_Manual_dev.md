# Stored Procedure: `ThucChay_Admatic_GhiNhanThayDoi_ThucChayDaTinh_Manual_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-12-31 14:07:11.303000
- **Ngày sửa cuối**: 2026-04-16 11:55:08.787000

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

/*
exec [dbo].[ThucChay_Admatic_GhiNhanThayDoi_ThucChayDaTinh_Manual_dev]
	@NgayGhiNhan = '2026-04-15',  -- date
    @NgayDanhSoGioiHan = '2023-04-15',  -- date
    @SoHopDong = N'QC0180425',  -- nvarchar
    @HopDongChiTietID = 753869  -- int
*/

CREATE PROCEDURE [dbo].[ThucChay_Admatic_GhiNhanThayDoi_ThucChayDaTinh_Manual_dev]
	@NgayGhiNhan DATE,
    @NgayCheckThayDoi DATE = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN
	DECLARE @NgayDanhSoGioiHan_MKT DATETIME = '2025-10-10'
	, @ghiChu_Tinhlai NVARCHAR(2000) = N'Tính lại: SP tối ưu + MKT-FEE [dbo].[ThucChay_Admatic_GhiNhanThayDoi_ThucChayDaTinh_Manual] do '
	, @ghiChu_DoiTru NVARCHAR(2000) = N'Đối trừ: SP tối ưu + MKT-FEE [dbo].[ThucChay_Admatic_GhiNhanThayDoi_ThucChayDaTinh_Manual] do '

	IF @SoHopDong IS NOT NULL
	BEGIN
		SET @NgayCheckThayDoi = NULL 
		SET @NgayDanhSoGioiHan = NULL
	END

	--DELETE FROM dbo.ThucChayDaTinh
	--WHERE	convert(date,NgayThucHien) = @NgayGhiNhan
	--	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao = 13)
	--	--AND DmSanPhamREF IN (339, 240, 598, 342, 5056, 5299)
	--	AND DotChayHopDong IN ( N'Đối trừ Admatic', N'Tính lại Admatic')
	--	AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
	--	AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)

	--========================================= 1. Xác định phân bổ thay đổi tỉ lệ/banner và pb có thay đổi số lượng, đơn giá, chiết khấu ==============================
    CREATE TABLE #DmPBThayDoi (
					NgayThucHien DATETIME,
					HopDongChiTietREF INT,
					BannerID INT,
					LoaiThayDoi INT,     --1: thay đổi thành tiền phân bổ, 2: phân bổ hủy, 3: treo hủy, 4: phân bổ khác chạy chung banner sau đó hủy treo, 5: phân bổ thay đổi thông tin nhãn
					LyDo NVARCHAR(MAX)
					)
	BEGIN
		--* phân bổ thay đổi thông tin
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
									THEN IIF(@SoHopDong IS NULL, '', N'xử lý tay') + N'hợp đồng hủy'
									WHEN hdct.DeletedStatus = 1
									THEN IIF(@SoHopDong IS NULL, '', N'xử lý tay') + N'phân bổ bị xóa'
									WHEN @SoHopDong IS NULL
									THEN N'phân bổ thay đổi thành tiền hoặc chiết khấu'
									ELSE N'xử lý tay hợp đồng/ phân bổ' 
							   END 
        FROM dbo.HopDongChiTiet hdct
		INNER JOIN dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
		WHERE
			 hdct.DmLoaiREF = 42 AND 
			 --HAIDH COMMENT 16092025 THEM SANPHAM MKT-FEE CHO VIEC TINH THUC CHAY THEO TIEN VE
			 NOT (hd.NgayDanhSoHopDong <@NgayDanhSoGioiHan_MKT and hdct.DmSanPhamREF = 817) AND

			 hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5133,5056,5268,5367,817) AND 
			 NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF IN (17, 18)) AND
			 hdct.DonViTinh <> N'BÀI' AND
			 NOT (EXISTS(SELECT HopDongChiTietREF 
								 FROM dbo.DmThongTinHopDongBanInventory 
								 WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
				  )  AND

			(@NgayCheckThayDoi IS NULL OR CONVERT(DATE, hd.LastModifiedAt) =  @NgayCheckThayDoi OR CONVERT(DATE, hdct.LastModifiedAt) =  @NgayCheckThayDoi)  AND 
			(@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) AND
			(@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong) AND 
			(@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
			 

		-- TH thay đổi thông tin nhãn hàng
		UPDATE dm
		SET dm.LoaiThayDoi = CASE WHEN (hdct.DanhSachNhanHangREF = l.DanhSachNhanHangREF AND  
										IIF(hdct.ChietKhau = 100,  hdct.SoLuong*hdct.dongia, hdct.ThanhTien) = l.ThanhTien AND
										hdct.ChietKhau = l.ChietKhau) OR 
										l.ThanhTien IS NULL  
								  THEN 0
								  WHEN hdct.DanhSachNhanHangREF <> l.DanhSachNhanHangREF AND 
									   IIF(hdct.ChietKhau = 100,  hdct.SoLuong*hdct.dongia, hdct.ThanhTien) = l.ThanhTien AND 
									   hdct.ChietKhau = l.ChietKhau
								  THEN 5
								  ELSE dm.LoaiThayDoi
							 END,
		    dm.LyDo =  CASE WHEN (hdct.DanhSachNhanHangREF = l.DanhSachNhanHangREF AND  
								  IIF(hdct.ChietKhau = 100,  hdct.SoLuong*hdct.dongia, hdct.ThanhTien) = l.ThanhTien AND
								  hdct.ChietKhau = l.ChietKhau) OR 
								  l.ThanhTien IS NULL 
							THEN ''
							WHEN hdct.DanhSachNhanHangREF <> l.DanhSachNhanHangREF AND 
								 IIF(hdct.ChietKhau = 100,  hdct.SoLuong*hdct.dongia, hdct.ThanhTien) = l.ThanhTien AND 
								 hdct.ChietKhau = l.ChietKhau
							THEN N'phân bổ thay đổi thông tin nhãn hàng'
							ELSE dm.LyDo
					   END
		FROM #DmPBThayDoi dm
		INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietREF
		OUTER APPLY (SELECT TOP 1 ThanhTien = IIF(l.ChietKhau = 100,  l.SoLuong*l.dongia, l.ThanhTien), l.ChietKhau, l.DanhSachNhanHangREF
					 FROM dbo.HopDongChiTietLog l 
					 WHERE LastModifiedAt < @NgayCheckThayDoi AND 
						   l.HopDongChiTietREF = dm.HopDongChiTietREF
					 ORDER BY HopDongChiTietLogID desc ) l 
		WHERE dm.LoaiThayDoi = 1 AND 
		      @NgayCheckThayDoi IS NOT NULL 
			  
		--** phân bổ hủy treo 
        INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongChiTietREF,
						--BannerID,
						LoaiThayDoi,
						LyDo
        )
        SELECT DISTINCT @NgayGhiNhan,
                        hdct.HopDongChiTietID,
						--tchdct.DmBannerREF,
						LoaiThayDoi = 3,
						LyDo = N'phân bổ hủy treo'
        FROM dbo.ThucChayHopDongChiTiet tchdct
		INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		INNER JOIN dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
		WHERE	 hd.TrangThaiHopDong NOT IN (0,3) AND
				 hd.DeletedStatus = 0 AND

				 hdct.DonViTinhREF <> 7 AND
				 hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5133,5056,5268, 5367,817) AND 
				 NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) AND 
				 hdct.DeletedStatus = 0  
                 --hdct.HopDongChiTietID  NOT IN (SELECT HopDongChiTietREF FROM #DmPBThayDoi WHERE LoaiThayDoi IN (1,2)) 
				 AND NOT (EXISTS(SELECT HopDongChiTietREF 
								 FROM dbo.DmThongTinHopDongBanInventory 
								 WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
						  )
				 AND hdct.DmLoaiREF = 42 AND

				--HAIDH COMMENT 16092025 THEM SANPHAM MKT-FEE CHO VIEC TINH THUC CHAY THEO TIEN VE
				NOT (hd.NgayDanhSoHopDong <@NgayDanhSoGioiHan_MKT and hdct.DmSanPhamREF = 817) AND

				 tchdct.DmHinhThucQuangCaoREF = 42 AND 
				 tchdct.DmHinhThucQuangCaoREF <> 13 AND 
				 tchdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5133,5056,5268,5367,817) AND
				 tchdct.DeletedStatus = 1 AND 

				 CAST(tchdct.LastModifiedAt AS DATE) = @NgayCheckThayDoi AND
				(@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) 

		--*** các phân bổ chạy chung banner với các phân bổ hủy treo hoặc bị hủy: vì ảnh hưởng đến tỷ lệ hdct so với banner (đã check lại từ anh Hải case này)
		INSERT INTO #DmPBThayDoi
        (				NgayThucHien,
						HopDongChiTietREF,
						LoaiThayDoi,
						LyDo
        )
        SELECT DISTINCT @NgayGhiNhan,
                        hdct.HopDongChiTietID,
						LoaiThayDoi = 4,
						LyDo = N'banner liên quan đến phân bổ khác hủy treo'
        FROM dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic tc
		INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tc.HopDongChiTietREF
		INNER JOIN dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID 
		INNER JOIN (SELECT DISTINCT bn.DmBannerREF
					FROM #DmPBThayDoi dm
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic bn
									ON dm.HopDongChiTietREF = bn.HopDongChiTietREF 
									   AND dm.LoaiThayDoi IN (2, 3) ) bn ON bn.DmBannerREF = tc.DmBannerREF
		WHERE	 hd.TrangThaiHopDong NOT IN (0,3) AND
				 hd.DeletedStatus = 0 AND

				 hdct.DonViTinhREF <> 7 AND
				 hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5133,5056,5268, 5367,817) AND 
				 NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) AND 
				 hdct.DeletedStatus = 0 AND 
                 hdct.HopDongChiTietID  NOT IN (SELECT HopDongChiTietREF FROM #DmPBThayDoi WHERE LoaiThayDoi IN (1,2,3)) 
				 AND NOT (EXISTS(SELECT HopDongChiTietREF 
								 FROM dbo.DmThongTinHopDongBanInventory 
								 WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
						  )
				 AND NOT (EXISTS(SELECT dm.HopDongChiTietREF 
								 FROM #DmPBThayDoi dm 
								 WHERE dm.HopDongChiTietREF = hdct.HopDongChiTietID)
						  )
				 AND hdct.DmLoaiREF = 42
				 AND tc.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5133,5056,5268, 5367,817) 
				 AND tc.[DeletedStatus] = 0

				 --HAIDH COMMENT 16092025 THEM SANPHAM MKT-FEE CHO VIEC TINH THUC CHAY THEO TIEN VE
				 AND NOT (hd.NgayDanhSoHopDong <@NgayDanhSoGioiHan_MKT and hdct.DmSanPhamREF = 817) 

				 AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) 

		select * from #DmPBThayDoi

		-- Loại TH phân bổ không thay đổi thông tin hợp đồng và không phát sinh treo hủy hoặc liên quan đến treo hủy
		DELETE
		FROM #DmPBThayDoi
		WHERE LoaiThayDoi = 0
		-- Với TH phân bổ thay đổi thông tin nhãn hàng nhưng có phát sinh treo hủy hoặc liên quan đến treo hủy
		-- thì sẽ đói trừ và tính lại cả phân bổ thay vì chỉ đối trừ và ghi nhận lại thông tin nhãn
		DELETE dm
		FROM #DmPBThayDoi dm
		INNER JOIN (
					SELECT distinct HopDongChiTietREF
					FROM #DmPBThayDoi
					WHERE LoaiThayDoi IN (3,4)
					) dmcheck ON dmcheck.HopDongChiTietREF = dm.HopDongChiTietREF
		WHERE dm.LoaiThayDoi = 5

		-- Với TH phân bổ thay đổi thông tin chiết khấu nhưng có phát sinh treo hủy 
		-- thì bỏ bản ghi lý do treo hủy
		DELETE dm
		FROM #DmPBThayDoi dm
		INNER JOIN (
					SELECT distinct HopDongChiTietREF
					FROM #DmPBThayDoi
					WHERE LoaiThayDoi = 1
					) dmcheck ON dmcheck.HopDongChiTietREF = dm.HopDongChiTietREF
		WHERE dm.LoaiThayDoi = 3
                    

	END	
     
	--select * from #DmPBThayDoi

	--========================================= 2. Xác định thucchayID của các phân bổ trên ====================================================================================================================
	CREATE TABLE #DmTinhLai 
				(	ID INT IDENTITY(1,1),
					DmWebsiteREF INT,
					TenWebsite NVARCHAR(MAX),
					DmBannerREF INT,
					NgayThucHien DATETIME,
					HopDongChiTietREF INT,
					DonViTinh NVARCHAR(100),
					DonGiaSauCK FLOAT,
					DonGiaKM FLOAT,
					DmSanPhamREF INT,
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
	--INSERT INTO #DmTinhLai
	--(				DmWebsiteREF ,
	--				TenWebsite ,
	--				DmBannerREF ,
	--				NgayThucHien ,
	--				HopDongChiTietREF ,
	--				DonViTinh ,
	--				DmSanPhamREF ,
	--				ChietKhau,

	--				SoLuongThucChay ,
	--				ThanhTienSauCK ,
	--				SoLuongKM ,
	--				ThanhTienKM ,

	--				LyDo)


	SELECT  tc.DmWebsiteID,
			tc.TenWebsite,
			tc.DmBannerID,
			@NgayGhiNhan,
			tchdct.HopDongChiTietREF,
			tc.DonViTinh,
			tc.DmSanPhamREF,
			hdct.ChietKhau,
			tchdct.TiLeThucChayHDCTSoVoiBanner,
			SoLuongThucChay = ISNULL(IIF(hdct.ChietKhau <> 100, tc.SoLuongThucChay*tchdct.TiLeThucChayHDCTSoVoiBanner/100, 0),0),
			ThanhTienSauCK = ISNULL(IIF(hdct.ChietKhau <> 100, tc.ThanhTienThucChaySauCK_ChuaVAT*tchdct.TiLeThucChayHDCTSoVoiBanner/100, 0),0),
			SoLuongKM = ISNULL(IIF(hdct.ChietKhau = 100, tc.SoLuongThucChayKM*tchdct.TiLeThucChayHDCTSoVoiBanner/100, 0),0),
			ThanhTienKM = ISNULL(IIF(hdct.ChietKhau = 100, tc.ThanhTienThucChayKM*tchdct.TiLeThucChayHDCTSoVoiBanner/100, 0),0),
			
			Lydo = dm.LyDo
	FROM (SELECT * FROM dbo.[ThucChay_ThanhTien_Admatic] tc 
			WHERE CAST(tc.NgayThucHien AS DATE) <= @NgayGhiNhan 
			AND tc.DmSanPhamREF <> 817 --khong bao gom MKT - FEE
			AND tc.DonViTinh <> N'BÀI'
			AND tc.DmWebsiteID <> 0
			AND tc.DeletedStatus = 0)tc
	INNER JOIN (SELECT * FROM dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic tchdct 
					WHERE tchdct.DmSanPhamREF <> 817 AND tchdct.DeletedStatus = 0
				)  tchdct ON tc.DmBannerID = tchdct.DmBannerREF AND 
							tc.DmSanPhamREF = tchdct.DmSanPhamREF
	INNER JOIN (SELECT * FROM dbo.HopDongChiTiet hdct 
				WHERE 1=1	
					AND hdct.DmLoaiREF = 42
					AND hdct.DmLoaiNenTangREF <> 9
					AND hdct.DeletedStatus = 0
					AND NOT ( hdct.DmLoaiBannerREF IN (17,18)OR hdct.DmLoaiREF IN (13))
					AND  hdct.DmSanPhamREF <> 817
			) hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
	INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK AND
												   hd.SoHopDong = tc.SoHopDong 
	INNER JOIN (SELECT DISTINCT HopDongChiTietREF , LyDo, LoaiThayDoi
			    FROM #DmPBThayDoi                  ) dm ON dm.HopDongChiTietREF = tchdct.HopDongChiTietREF
	WHERE   1=1
			AND dm.LoaiThayDoi IN (1,3,4)
	------HAIDH COMMENT 16092025 THEM SANPHAM MKT-FEE CHO VIEC TINH THUC CHAY THEO TIEN VE
	UNION ALL
	SELECT  tc.DmWebsiteID,
			tc.TenWebsite,
			tc.DmBannerID,
			@NgayGhiNhan,
			tc.HopDongChiTietREF,
			tc.DonViTinh,
			tc.DmSanPhamREF,
			hdct.ChietKhau,
			0 TiLeThucChayHDCTSoVoiBanner,
			SoLuongThucChay = ISNULL(IIF(hdct.ChietKhau <> 100, tc.SoLuongThucChay, 0),0),
			ThanhTienSauCK = ISNULL(IIF(hdct.ChietKhau <> 100, tc.ThanhTienThucChaySauCK_ChuaVAT, 0),0),
			SoLuongKM = ISNULL(IIF(hdct.ChietKhau = 100, tc.SoLuongThucChayKM, 0),0),
			ThanhTienKM = ISNULL(IIF(hdct.ChietKhau = 100, tc.ThanhTienThucChayKM, 0),0),
			
			Lydo = dm.LyDo
	FROM (SELECT * FROM dbo.[ThucChay_ThanhTien_Admatic] tc 
			WHERE CAST(tc.NgayThucHien AS DATE) <= @NgayGhiNhan 
			AND tc.DmSanPhamREF = 817 --MKT - FEE
			AND tc.HopDongChiTietREF <> 0
			AND tc.DmWebsiteID <> 0
			AND tc.DeletedStatus = 0
			AND tc.SoHopDong NOT IN (N'HD PROG',N'HD_DEMO')
			AND tc.DonViTinh <> N'BÀI'
			)tc
	INNER JOIN (SELECT * FROM dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic tchdct 
					WHERE tchdct.DmSanPhamREF = 817 AND tchdct.DeletedStatus = 0
				)  tchdct ON tc.DmBannerID = tchdct.DmBannerREF AND 
							tc.DmSanPhamREF = tchdct.DmSanPhamREF AND
							tc.HopDongChiTietREF = tchdct.HopDongChiTietREF
	INNER JOIN (SELECT * FROM dbo.HopDongChiTiet hdct 
				WHERE 1=1	
					AND hdct.DmLoaiREF = 42
					AND hdct.DmLoaiNenTangREF <> 9
					AND hdct.DeletedStatus = 0
					AND NOT ( hdct.DmLoaiBannerREF IN (17,18)OR hdct.DmLoaiREF IN (13))
					AND  hdct.DmSanPhamREF IN ( 817,733)
			) hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
	INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK AND
												   hd.SoHopDong = tc.SoHopDong 
	INNER JOIN (SELECT DISTINCT HopDongChiTietREF , LyDo, LoaiThayDoi
			    FROM #DmPBThayDoi                  ) dm ON dm.HopDongChiTietREF = tchdct.HopDongChiTietREF
	WHERE   1=1
			AND dm.LoaiThayDoi IN (1,3,4)	

			--HAIDH COMMENT 16092025 THEM SANPHAM MKT-FEE CHO VIEC TINH THUC CHAY THEO TIEN VE
			AND NOT (hd.NgayDanhSoHopDong <@NgayDanhSoGioiHan_MKT and tc.DmSanPhamREF = 817) 

			

	DELETE
	FROM #DmTinhLai
	WHERE ThanhTienSauCK = 0 AND ThanhTienKM = 0 AND SoLuongKM = 0 AND SoLuongThucChay = 0

	UPDATE dm
	SET dm.DonGiaSauCK = IIF(SoLuongThucChay = 0, 0, ThanhTienSauCK / SoLuongThucChay),
	    dm.DonGiaKM = IIF(SoLuongKM = 0, 0, ThanhTienKM / SoLuongKM)
	FROM #DmTinhLai dm 

	UPDATE temp
	SET temp.ThanhTienSauCKPhanBo =hdct.ThanhTien,
		temp.ThanhTienKMPhanBo = IIF(hdct.ChietKhau = 100, hdct.SoLuong*hdct.DonGia, 0)
	FROM #DmTinhLai temp
	INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = temp.HopDongChiTietREF


	--========================================= 3. Xác định lệch treo hạ và ghi nhận của các thucchayID trên ==========================
	
	;WITH CTE_Base AS (
			SELECT  ID,
					TongThucChayTruocDo =  COALESCE(	SUM(ThanhTienSauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
														), 0),
					TongThucChayDenHT =     COALESCE(	SUM(ThanhTienSauCK) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0),
					TongThucChayKMTruocDo=     COALESCE(	SUM(ThanhTienKM) OVER (
															PARTITION BY HopDongChiTietREF 
															ORDER BY ID  
															ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
															), 0),
					TongThucChaKMDenHT =       COALESCE(SUM(ThanhTienKM) OVER (
														PARTITION BY HopDongChiTietREF 
														ORDER BY ID  
														ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
														), 0)
			FROM #DmTinhLai )
  
	UPDATE temp
	SET  	ThanhTienTC_GhiNhan =  CASE WHEN sl.TongThucChayTruocDo > ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo
										THEN 0
										WHEN sl.TongThucChayTruocDo > ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT <= ThanhTienSauCKPhanBo
										THEN sl.TongThucChayDenHT - sl.TongThucChayTruocDo
										WHEN sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT > ThanhTienSauCKPhanBo
										THEN ThanhTienSauCKPhanBo - sl.TongThucChayTruocDo
										WHEN sl.TongThucChayTruocDo <= ThanhTienSauCKPhanBo AND sl.TongThucChayDenHT <= ThanhTienSauCKPhanBo
										THEN temp.ThanhTienSauCK
									END, 
			ThanhTienKM_GhiNhan = CASE	WHEN sl.TongThucChayKMTruocDo > ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo
										THEN 0
										WHEN sl.TongThucChayKMTruocDo > ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT <= ThanhTienKMPhanBo
										THEN sl.TongThucChaKMDenHT - sl.TongThucChayKMTruocDo
										WHEN sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT > ThanhTienKMPhanBo
										THEN ThanhTienKMPhanBo - sl.TongThucChayKMTruocDo
										WHEN sl.TongThucChayKMTruocDo <= ThanhTienKMPhanBo AND sl.TongThucChaKMDenHT <= ThanhTienKMPhanBo
										THEN temp.ThanhTienKM
									END 
	FROM #DmTinhLai temp
	INNER JOIN CTE_Base sl ON sl.ID = temp.ID

	UPDATE temp
	SET  temp.SoLuongThucChay_GhiNhan = IIF(temp.DonGiaSauCK <>0, ThanhTienTC_GhiNhan/temp.DonGiaSauCK, 0),
		 temp.SoLuongKM_GhiNhan = IIF(temp.DonGiaKM <>0, ThanhTienKM_GhiNhan/temp.DonGiaKM, 0),
		 temp.ThanhTienLechTreoHa =  IIF(temp.DonGiaKM <>0, temp.ThanhTienKM - ThanhTienKM_GhiNhan, (temp.ThanhTienSauCK - ThanhTienTC_GhiNhan)*100/(100-ChietKhau))
	FROM #DmTinhLai temp

	UPDATE temp
	SET temp.SoLuongLechTreoHa = IIF(temp.DonGiaKM <> 0, temp.ThanhTienLechTreoHa/temp.DonGiaKM, temp.ThanhTienLechTreoHa/temp.DonGiaSauCK)
	FROM #DmTinhLai temp

	--========================================= 4. Tiến hành đối trừ ===========================================================
	--INSERT INTO dbo.[ThucChayDaTinh]
	--(
	--	ThucChayDaTinhID,
	--	HopDongID,
	--	SoHopDong,
	--	DmMaHopDongREF,
	--	TenMaHopDong,
	--	NgayDanhSoHopDong,
	--	NgayKyHopDong,
	--	NhanHopDong,
	--	NgayNhanBanFax,
	--	NgayNhanHopDongBanCung,
	--	NgayChuyenHopDongChoKeToan,
	--	So,
	--	Thang,
	--	Nam,
	--	GiaTriHopDong,
	--	CongNo,
	--	HopDongChiTietREF,
	--	DangSuDung,
	--	IsGiayPhep,
	--	TrangThaiHopDong,
	--	IsBanCung,
	--	DmPhongBanREF,
	--	TenPhongBan,
	--	DmBoPhanREF,
	--	TenBoPhan,
	--	DmNhomLamViecREF,
	--	TenNhomLamViec,
	--	DmDiaDiemLamViecREF,
	--	TenDiaDiemLamViec,
	--	SysNhanVienREF,
	--	TenDangNhap,
	--	TenNhanVien,
	--	TenKhachHang,
	--	NhanHang,
	--	DmNhomNganhREF,
	--	TenNhomNganh,
	--	DmHinhThucQuangCao,
	--	TenHinhThucQuangCao,
	--	DmSanPhamREF,
	--	TenSanPham,
	--	DmNhomWebsiteREF,
	--	TenNhomWebsite,
	--	DmChuyenMucREF,
	--	TenChuyenMuc,
	--	DmLoaiBannerREF,
	--	TenLoaiBanner,
	--	DmViTriREF,
	--	TenViTri,
	--	DotChayHopDong,
	--	SoLuongDotChayHD,
	--	DotChayBooking,
	--	SoLuongDotChayBooking,
	--	SoLuong,
	--	DonViTinh,
	--	DonGia,
	--	DonGiaTheoDonVi,
	--	ChietKhau,
	--	GiamGia,
	--	ThanhTien,
	--	TiLeTuVan,
	--	ChiPhiTuVan,
	--	IsKhuyenMai,
	--	KhuyenMai,
	--	DmBannerREF,
	--	DmChienDichREF,
	--	DmWebsiteREF,
	--	TenWebsite,
	--	TongViewThucChay,
	--	TongClickThucChay,
	--	TongSoBaiViet,
	--	SoLuongThucChay,
	--	NgayThucHien,
	--	GiaTriThayDoi,
	--	ThanhTienThucChayTruocTrietKhau,
	--	GiaTriTrietKhauThucChay,
	--	ThanhTienSauTrietKhauThucChay,
	--	GiaTriHoaHongThucChay,
	--	ThanhTienThucThu,
	--	ThanhTienKM,
	--	SoLuongThucChayKM,
	--	SoLuongThucChayLechTreoHa,
	--	ThanhTienLechTreoHa,
	--	CreatedAt,
	--	LastModifiedAt,
	--	IsPheDuyet,
	--	PheDuyetBy,
	--	PheDuyetAt,
	--	SoLuongThayDoi,
	--	SoLuongKMThayDoi,
	--	GiaTriKMThayDoi,
	--	GhiChu
	--)
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
		, N'Đối trừ Admatic' AS DotChayHopDong
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
		, @ghiChu_DoiTru + dm.LyDo AS GhiChu
FROM    dbo.[ThucChayDaTinh] tcdt
INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tcdt.HopDongChiTietREF 
WHERE tcdt.NgayThucHien <= dm.NgayThucHien
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
	HAVING  SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) <> 0 OR 
			SUM(SoLuongThucChayLechTreoHa) <> 0 OR 
			SUM(ThanhTienLechTreoHa) <> 0 OR 
			SUM(SoLuongThucChay + SoLuongThayDoi) <> 0 OR
			SUM(SoLuongThucChayKM + SoLuongKMThayDoi) <> 0 OR
			SUM(ThanhTienKM + GiaTriKMThayDoi) <> 0 

	--========================================= 5. Tiến hành tính lại với phân bổ thay đổi thông tin nhãn hàng
	--INSERT INTO dbo.[ThucChayDaTinh]
	--(
	--	ThucChayDaTinhID,
	--	HopDongID,
	--	SoHopDong,
	--	DmMaHopDongREF,
	--	TenMaHopDong,
	--	NgayDanhSoHopDong,
	--	NgayKyHopDong,
	--	NhanHopDong,
	--	NgayNhanBanFax,
	--	NgayNhanHopDongBanCung,
	--	NgayChuyenHopDongChoKeToan,
	--	So,
	--	Thang,
	--	Nam,
	--	GiaTriHopDong,
	--	CongNo,
	--	HopDongChiTietREF,
	--	DangSuDung,
	--	IsGiayPhep,
	--	TrangThaiHopDong,
	--	IsBanCung,
	--	DmPhongBanREF,
	--	TenPhongBan,
	--	DmBoPhanREF,
	--	TenBoPhan,
	--	DmNhomLamViecREF,
	--	TenNhomLamViec,
	--	DmDiaDiemLamViecREF,
	--	TenDiaDiemLamViec,
	--	SysNhanVienREF,
	--	TenDangNhap,
	--	TenNhanVien,
	--	TenKhachHang,
	--	NhanHang,
	--	DmNhomNganhREF,
	--	TenNhomNganh,
	--	DmHinhThucQuangCao,
	--	TenHinhThucQuangCao,
	--	DmSanPhamREF,
	--	TenSanPham,
	--	DmNhomWebsiteREF,
	--	TenNhomWebsite,
	--	DmChuyenMucREF,
	--	TenChuyenMuc,
	--	DmLoaiBannerREF,
	--	TenLoaiBanner,
	--	DmViTriREF,
	--	TenViTri,
	--	DotChayHopDong,
	--	SoLuongDotChayHD,
	--	DotChayBooking,
	--	SoLuongDotChayBooking,
	--	SoLuong,
	--	DonViTinh,
	--	DonGia,
	--	DonGiaTheoDonVi,
	--	ChietKhau,
	--	GiamGia,
	--	ThanhTien,
	--	TiLeTuVan,
	--	ChiPhiTuVan,
	--	IsKhuyenMai,
	--	KhuyenMai,
	--	DmBannerREF,
	--	DmChienDichREF,
	--	DmWebsiteREF,
	--	TenWebsite,
	--	TongViewThucChay,
	--	TongClickThucChay,
	--	TongSoBaiViet,
	--	SoLuongThucChay,
	--	NgayThucHien,
	--	GiaTriThayDoi,
	--	ThanhTienThucChayTruocTrietKhau,
	--	GiaTriTrietKhauThucChay,
	--	ThanhTienSauTrietKhauThucChay,
	--	GiaTriHoaHongThucChay,
	--	ThanhTienThucThu,
	--	ThanhTienKM,
	--	SoLuongThucChayKM,
	--	SoLuongThucChayLechTreoHa,
	--	ThanhTienLechTreoHa,
	--	CreatedAt,
	--	LastModifiedAt,
	--	IsPheDuyet,
	--	PheDuyetBy,
	--	PheDuyetAt,
	--	SoLuongThayDoi,
	--	SoLuongKMThayDoi,
	--	GiaTriKMThayDoi,
	--	GhiChu
	--)
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
			, N'Tính lại Admatic' AS DotChayHopDong
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
			, dm.NgayThucHien
			, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi
			, 0 AS ThanhTienThucChayTruocTrietKhau
			, 0 AS GiaTriTrietKhauThucChay
			, 0 AS ThanhTienSauTrietKhauThucChay
			, 0 AS GiaTriHoaHongThucChay
			, 0 AS ThanhTienThucThu
			, 0 AS ThanhTienKM
			, 0 AS SoLuongThucChayKM
			, SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa
			, SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
			, GETDATE()
			, GETDATE()
			, 0 AS IsPheDuyet
			, '' AS PheDuyetBy
			, GETDATE() PheDuyetAt
			, SUM(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi
			, SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi
			, SUM(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi
			, @ghiChu_Tinhlai + dm.LyDo AS GhiChu
	FROM    dbo.[ThucChayDaTinh] tcdt
	INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietREF = tcdt.HopDongChiTietREF AND dm.LoaiThayDoi = 5
	WHERE tcdt.NgayThucHien < dm.NgayThucHien
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


	--================================ 6. Tính lại với TH phân bổ thay đổi thành tiền, chiết khấu, hủy treo hoặc liên quan đến banner có treo hủy
	DECLARE @Thucchay_Admatic_DmTinhlai DataType_Thucchay_Admatic_DmTinhlai
	INSERT INTO @Thucchay_Admatic_DmTinhlai
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
				LyDo

	select * from @Thucchay_Admatic_DmTinhlai
	--EXEC [dbo].[ThucChay_Admatic_DoiTruTinhLai_ThucChayDaTinh] @Thucchay_Admatic_DmTinhlai

	DROP TABLE #DmTinhLai
	DROP TABLE #DmPBThayDoi

END

```
