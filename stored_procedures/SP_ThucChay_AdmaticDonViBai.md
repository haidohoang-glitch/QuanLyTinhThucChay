# Stored Procedure: `ThucChay_AdmaticDonViBai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-10 17:07:14.343000
- **Ngày sửa cuối**: 2025-10-27 15:20:17.280000

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






CREATE PROCEDURE [dbo].[ThucChay_AdmaticDonViBai]
    @NgayGhiNhan DATE,
    @NgayCheckThayDoi  DATE = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
    BEGIN
		DECLARE @XuLyTay NVARCHAR(100) = N'xử lý tay '
		IF @SoHopDong IS NOT NULL
		BEGIN
			SET @NgayCheckThayDoi = NULL
			SET @NgayDanhSoGioiHan = NULL
		END

		CREATE TABLE #DmThayDoi 
		(	  ThucChayHopDongChiTietID INT,
			  HopDongChiTietID INT,
			  HopDongREF INT ,
			  DonGiaHDCT_BF FLOAT,
			  ChietKhauHDCT_BF FLOAT,
			  NgayThucHien DATETIME,
			  RecordStatus INT,
			  LastModifiedAt DATETIME2,
			  ThanhTienKhuyenMaiTreo FLOAT,
			  ThanhTienSauCKTreo FLOAT,
			  ThanhTienKhuyenMaiPhanBo FLOAT,
			  ThanhTienSauCKPhanBo FLOAT,
			  ThanhTienKhuyenMaiDaTinh FLOAT,
			  ThanhTienSauCKDaTinh FLOAT,
			  LoaiThayDoi INT,  
			  LyDo NVARCHAR(MAX),
			  LoaiXuLy INT -- 0: không xử lý, 1: đối trừ, 2: đối trừ tính lại, 3: ghi nhận mới
		)

		DELETE
		FROM ABM_data_thucchay.dbo.ThucChayDaTinh
		WHERE   NgayThucHien = @NgayGhiNhan
		        AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13))
				AND ((DmSanPhamREF  in (305,5312) ) OR	(DmSanPhamREF  = 598 AND DmVitriREF in (9198,100292)))
				AND DmHinhThucQuangCao = 42
				--AND DmVitriREF = 9198
				AND DonViTinh IN ( N'BÀI', N'URL')
                AND DotChayHopDong IN (N'Tính mới Admatic donvibai', N'Tính lại Admatic donvibai', N'Đối trừ Admatic donvibai')
				AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
				AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)

        --=================================================== 1: Xác định danh mục ID cần đối trừ hoặc ghi nhận thêm ====================================
		/* TH1 phân bổ hoặc hợp đồng xóa, hủy: đối trừ toàn bộ các ID treo liên quan đã được ghi nhận thực chạy
		   TH2 phân bổ thay đổi giá trị: sắp xếp ID treo theo thứ tự: RecordStatus 1->0, LastModifiedAt asc, ID treo asc
			   Nếu tổng không vượt thì ghi nhận mới với ID treo chưa tính hoặc đối trừ tính lại với ID treo đã tính (Th phân bổ thay đổi đơn giá)
			   Nếu tổng vượt thì đối trừ với ID treo đã tính
		   TH3 ID treo mới: Nếu chưa vượt thì ghi nhận mới
		*/
		BEGIN
			INSERT INTO #DmThayDoi
			(   ThucChayHopDongChiTietID,
				HopDongChiTietID,
				HopDongREF,
				NgayThucHien,
				LoaiThayDoi,
				LyDo,
				LoaiXuLy
			)
			SELECT  DISTINCT
					tchdct.ThucChayHopDongChiTietID,
					hdct.HopDongChiTietID ,
					hd.HopDongID ,
					NgayThucHien =  @NgayGhiNhan,
					LoaiThayDoi = 1,
					LyDo =	CASE WHEN hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1 OR hdct.DeletedStatus = 1
					             THEN N'hợp đồng hoặc phân bổ xóa, hủy'
								 WHEN tchdct.DeletedStatus = 1
								 THEN N'treo hủy'
							END,
					LoaiXuLy = 1
			FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct
			INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE     (
						((hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1) AND 
						 CONVERT(DATE, ISNULL(hd.LastModifiedAt, hd.CreatedAt))  = @NgayCheckThayDoi) OR
						(hdct.DeletedStatus = 1 AND 
						 CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi) OR
						(tchdct.DeletedStatus = 1 AND 
						 CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi)
					   )
                   AND ((hdct.DmSanPhamREF in (305,5312)) OR (hdct.DmSanPhamREF = 598 AND hdct.DmVitriREF in (9198,100292)))
				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND hdct.DmLoaiREF = 42
				   AND hdct.DeletedStatus = 0
				   AND hdct.DonViTinhREF IN (7,84)


				   AND tchdct.DmSanPhamREF IN (305, 598,5312)
				   AND tchdct.DmHinhThucQuangCaoREF = 42
				   AND tchdct.RecordStatus = 1

				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND hd.TrangThaiHopDong IN (1,2,4) AND  hd.DeletedStatus = 0

			
			INSERT INTO #DmThayDoi
			(	  ThucChayHopDongChiTietID ,
				  HopDongChiTietID ,
				  HopDongREF  ,
				  NgayThucHien ,
				  RecordStatus ,
				  LastModifiedAt ,
				  ThanhTienKhuyenMaiTreo ,
				  ThanhTienSauCKTreo ,
				  ThanhTienKhuyenMaiPhanBo ,
				  ThanhTienSauCKPhanBo ,
				  LoaiThayDoi ,  
				  LyDo,
				  LoaiXuLy
			)
			SELECT DISTINCT
					tchdct.ThucChayHopDongChiTietID,
					tchdct.HopDongChiTietREF ,
					tchdct.HopDongREF ,
					NgayThucHien =  @NgayGhiNhan,
					tchdct.RecordStatus,
					tchdct.LastModifiedAt,
					ThanhTienKhuyenMaiTreo = IIF(hdct.ChietKhau = 100,hdct.DonGia, 0),
					ThanhTienSauCKTreo =  hdct.DonGia*(1-hdct.ChietKhau/100),
					ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100,hdct.SoLuong*hdct.DonGia, 0),
					ThanhTienSauCKPhanBo = hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100),
					LoaiThayDoi = 2,
					LyDo       = N'phân bổ thay đổi thông tin',
					LoaiXuLy = NULL
			FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct
			INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE  CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi
                   AND ((hdct.DmSanPhamREF in (305,5312)) OR (hdct.DmSanPhamREF = 598 AND hdct.DmVitriREF in (9198,100292)))
				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND hdct.DmLoaiREF = 42
				   AND hdct.DeletedStatus = 0
				   AND hdct.DonViTinhREF IN (7,84)


				   AND tchdct.DmSanPhamREF IN (305, 598,5312)
				   AND tchdct.DmHinhThucQuangCaoREF = 42
				   AND tchdct.DeletedStatus = 0

				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
				   AND hd.TrangThaiHopDong IN (1,2,4) AND  hd.DeletedStatus = 0
				   
				   AND tchdct.ThucChayHopDongChiTietID NOT IN (SELECT ThucChayHopDongChiTietID FROM #DmThayDoi)

			
			DELETE dm
			FROM #DmThayDoi dm
			OUTER APPLY (SELECT TOP 1 ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100,hdct.SoLuong*hdct.DonGia, 0), 
									  ThanhTienSauCKPhanBo = hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100),
									  ThanhTienKhuyenMaiTreo_1bai = IIF(hdct.ChietKhau = 100,hdct.DonGia, 0),
									  ThanhTienSauCKTreo_1bai = hdct.DonGia*(1-hdct.ChietKhau/100)
						 FROM ABM_data_thucchay.dbo.HopDongChiTietLog hdct
						 WHERE hdct.HopDongChiTietREF = dm.HopDongChiTietID AND
                               CAST(hdct.LastModifiedAt AS DATE) < @NgayCheckThayDoi
						 ORDER BY hdct.LastModifiedAt desc) hdct 
			WHERE  ROUND(dm.ThanhTienKhuyenMaiPhanBo - ISNULL(hdct.ThanhTienKhuyenMaiPhanBo, 0), 0) = 0 AND 
				   ROUND(dm.ThanhTienSauCKPhanBo - ISNULL(hdct.ThanhTienSauCKPhanBo, 0), 0) = 0 AND
				   ROUND(dm.ThanhTienSauCKTreo - ISNULL(hdct.ThanhTienSauCKTreo_1bai, 0), 0) = 0 AND 
				   ROUND(dm.ThanhTienKhuyenMaiTreo - ISNULL(hdct.ThanhTienKhuyenMaiTreo_1bai, 0), 0) = 0 AND 
				   LoaiThayDoi = 2


			INSERT INTO #DmThayDoi
			(	  ThucChayHopDongChiTietID ,
				  HopDongChiTietID ,
				  HopDongREF  ,
				  NgayThucHien ,
				  RecordStatus ,
				  LastModifiedAt ,
				  ThanhTienKhuyenMaiTreo ,
				  ThanhTienSauCKTreo ,
				  ThanhTienKhuyenMaiPhanBo ,
				  ThanhTienSauCKPhanBo ,
				  LoaiThayDoi ,  
				  LyDo,
				  LoaiXuLy
			)
			SELECT DISTINCT
					tchdct.ThucChayHopDongChiTietID,
					tchdct.HopDongChiTietREF ,
					tchdct.HopDongREF ,
					NgayThucHien =  @NgayGhiNhan,
					tchdct.RecordStatus,
					tchdct.LastModifiedAt,
					ThanhTienKhuyenMaiTreo = IIF(hdct.ChietKhau = 100,hdct.DonGia, 0),
					ThanhTienSauCKTreo =  hdct.DonGia*(1-hdct.ChietKhau/100),
					ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100,hdct.SoLuong*hdct.DonGia, 0),
					ThanhTienSauCKPhanBo = hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100),
					LoaiThayDoi = CASE WHEN tchdct.RecordStatus = 0  
									   THEN 3
									   WHEN tchdct.RecordStatus = 1 
									   THEN 4
									   ELSE 0
								  END,
					LyDo       = CASE  WHEN tchdct.RecordStatus = 0 
									   THEN N'ghi nhận phát sinh treo mới'
									   WHEN tchdct.RecordStatus = 1 
									   THEN N'thay đổi thông tin nhãn treo'
									   ELSE N''
								 END,
					LoaiXuLy = IIF(tchdct.DeletedStatus = 1, 1, NULL)
			FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct
			INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE  CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi
                   AND ((hdct.DmSanPhamREF in (305,5312)) OR (hdct.DmSanPhamREF = 598 AND hdct.DmVitriREF in (9198,100292)))
				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND hdct.DmLoaiREF = 42
				   AND hdct.DeletedStatus = 0
				   AND hdct.DonViTinhREF IN (7,84)


				   AND tchdct.DmSanPhamREF IN (305, 598,5312)
				   AND tchdct.DmHinhThucQuangCaoREF = 42
				   AND tchdct.DeletedStatus = 0

				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
				   AND hd.TrangThaiHopDong IN (1,2,4) AND  hd.DeletedStatus = 0

				   AND tchdct.ThucChayHopDongChiTietID NOT IN (SELECT ThucChayHopDongChiTietID FROM #DmThayDoi)


			DELETE dm
			FROM #DmThayDoi dm
			INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct ON tchdct.ThucChayHopDongChiTietID = dm.ThucChayHopDongChiTietID
			OUTER APPLY (SELECT TOP 1 DmNhanHangREF
			             FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTietLog l
						 WHERE l.ThucChayHopDongChiTietID = dm.ThucChayHopDongChiTietID AND
                               CAST(l.LastModifiedAt AS DATE) < @NgayCheckThayDoi
						 ORDER BY l.ThucChayHopDongChiTietLogID DESC ) l
			WHERE LoaiThayDoi = 4 AND
                  ISNULL(l.DmNhanHangREF, tchdct.DmNhanHangREF) = tchdct.DmNhanHangREF

			UPDATE dm
			SET dm.DonGiaHDCT_BF = ISNULL(l.DonGia, hdct.DonGia),
			    dm.ChietKhauHDCT_BF = ISNULL(l.ChietKhau, hdct.ChietKhau)
			FROM #DmThayDoi dm
			INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
			OUTER APPLY (SELECT TOP 1 hdct.DonGia, l.ChietKhau
						 FROM ABM_data_thucchay.dbo.HopDongChiTietLog l
						 WHERE l.HopDongChiTietREF = dm.HopDongChiTietID AND
                               CAST(l.LastModifiedAt AS DATE) < @NgayCheckThayDoi
						 ORDER BY hdct.LastModifiedAt desc) l 
			WHERE LoaiThayDoi = 3


			IF @SoHopDong IS NOT NULL 
			BEGIN
				INSERT INTO #DmThayDoi
				(	  ThucChayHopDongChiTietID ,
					  HopDongChiTietID ,
					  HopDongREF  ,
					  NgayThucHien ,
					  RecordStatus ,
					  LastModifiedAt ,
					  ThanhTienKhuyenMaiTreo ,
					  ThanhTienSauCKTreo ,
					  ThanhTienKhuyenMaiPhanBo ,
					  ThanhTienSauCKPhanBo ,
					  LoaiThayDoi ,  
					  LyDo,
					  LoaiXuLy
				)
				SELECT DISTINCT
						tchdct.ThucChayHopDongChiTietID,
						tchdct.HopDongChiTietREF ,
						tchdct.HopDongREF ,
						NgayThucHien =  @NgayGhiNhan,
						tchdct.RecordStatus,
						tchdct.LastModifiedAt,
						ThanhTienKhuyenMaiTreo = IIF(hdct.ChietKhau = 100,hdct.DonGia, 0),
						ThanhTienSauCKTreo =  hdct.DonGia*(1-hdct.ChietKhau/100),
						ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100,hdct.SoLuong*hdct.DonGia, 0),
						ThanhTienSauCKPhanBo = hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100),
						LoaiThayDoi = CASE WHEN hdct.DeletedStatus = 1 OR hd.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3 OR tchdct.DeletedStatus = 1
										   THEN 1
										   ELSE 2
									  END,
						LyDo       = CASE  WHEN hdct.DeletedStatus = 1 OR hd.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3 OR tchdct.DeletedStatus = 1
										   THEN N'xử lý tay treo hủy hoặc hợp đồng/hdct hủy'
										   WHEN tchdct.RecordStatus = 1 
										   THEN N'xử lý tay lại treo đã ghi nhận'
										   WHEN tchdct.RecordStatus = 0 
										   THEN N'xử lý tay treo ghi nhận mới'
										   ELSE N''
									 END,
						LoaiXuLy = IIF(hdct.DeletedStatus = 1 OR hd.DeletedStatus = 1 OR hd.TrangThaiHopDong = 3 OR tchdct.DeletedStatus = 1, 1, NULL)
				FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct
				INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
				INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
				WHERE  ((hdct.DmSanPhamREF in (305,5312)) OR (hdct.DmSanPhamREF = 598 AND hdct.DmVitriREF in (9198,100292)))
					   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
					   AND hdct.DmLoaiREF = 42
					   AND hdct.DonViTinhREF IN (7,84)
					   AND (@HopDongChiTietID is NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)


					   AND tchdct.DmSanPhamREF IN (305, 598,5312)
					   AND tchdct.DmHinhThucQuangCaoREF = 42

					   AND hd.SoHopDong = @SoHopDong

					   AND tchdct.ThucChayHopDongChiTietID NOT IN (SELECT ThucChayHopDongChiTietID FROM #DmThayDoi)
			END 

			UPDATE dm
			SET dm.ThanhTienKhuyenMaiDaTinh = ISNULL(IIF(dm.ChietKhauHDCT_BF = 100,dm.dongiaHDCT_BF, 0)*tchdct.SoLuongBai,0),
			    dm.ThanhTienSauCKDaTinh = ISNULL(dm.dongiaHDCT_BF*(1-dm.ChietKhauHDCT_BF/100)*tchdct.SoLuongBai,0)
			FROM #DmThayDoi dm
			OUTER APPLY (SELECT --ThanhTienKhuyenMaiDaTinh = SUM (IIF(dm.ChietKhauHDCT_BF = 100,dm.dongiaHDCT_BF, 0)),
			                    --ThanhTienSauCKDaTinh =  SUM(dm.dongiaHDCT_BF*(1-dm.ChietKhauHDCT_BF/100))
								SoLuongBai = COUNT(DISTINCT tchdct.ThucChayHopDongChiTietID)
						 FROM ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct
						 WHERE dm.HopDongChiTietID = tchdct.HopDongChiTietREF AND
						       tchdct.ThucChayHopDongChiTietID NOT IN (SELECT ThucChayHopDongChiTietID 
																	   FROM #DmThayDoi 
																	   WHERE LoaiThayDoi = 3) AND
							   tchdct.RecordStatus = 1
							   AND CAST(LastModifiedAt AS DATE) <= @NgayGhiNhan ) tchdct
			WHERE dm.LoaiThayDoi = 3


		END
		--=================================================== 2: Xác định phương thức xử lý cho ID treo thuộc: LoaiThayDoi in (2,3) ===========
		-- 0: không xử lý, 1: đối trừ, 2: đối trừ tính lại, 3: ghi nhận mới
		BEGIN 
			;WITH CTE_Base AS (
				SELECT 
					ThucChayHopDongChiTietID,
					RecordStatus,
					ThanhTienKhuyenMaiTreo,
					ThanhTienSauCKTreo,
					ThanhTienKhuyenMaiDaTinh,
					ThanhTienSauCKDaTinh,
					ThanhTienKhuyenMaiPhanBo,
					ThanhTienSauCKPhanBo,
					HopDongChiTietID,
					ROW_NUMBER() OVER (PARTITION BY HopDongChiTietID ORDER BY RecordStatus DESC, LastModifiedAt ASC, ThucChayHopDongChiTietID ASC) AS RowNum
				FROM #DmThayDoi
				WHERE LoaiThayDoi IN (2, 3) ),

			 CTE_Recursive AS (
				SELECT 
					ThucChayHopDongChiTietID,
					RecordStatus,
					ThanhTienKhuyenMaiTreo,
					ThanhTienSauCKTreo,
					ThanhTienKhuyenMaiDaTinh,
					ThanhTienSauCKDaTinh,
					ThanhTienKhuyenMaiPhanBo,
					ThanhTienSauCKPhanBo,
					HopDongChiTietID,
					RowNum,
					TichLuyThanhTienKM = IIF (ISNULL(ThanhTienKhuyenMaiDaTinh, 0) + ThanhTienKhuyenMaiTreo > ThanhTienKhuyenMaiPhanBo,
					                          ISNULL(ThanhTienKhuyenMaiDaTinh, 0), 
											  ISNULL(ThanhTienKhuyenMaiDaTinh, 0) + ThanhTienKhuyenMaiTreo ), 
					TichLuyThanhTienSauCK = IIF (ISNULL(ThanhTienSauCKDaTinh, 0) + ThanhTienSauCKTreo > ThanhTienSauCKPhanBo,
												 ISNULL(ThanhTienSauCKDaTinh, 0), 
												 ISNULL(ThanhTienSauCKDaTinh, 0) + ThanhTienSauCKTreo ),
					GhiNhanKM = IIF(ISNULL(ThanhTienKhuyenMaiDaTinh, 0) + ThanhTienKhuyenMaiTreo > ThanhTienKhuyenMaiPhanBo,
					                0, ThanhTienKhuyenMaiTreo ),
					GhiNhanThanhTienSauCK = IIF (ISNULL(ThanhTienSauCKDaTinh, 0) + ThanhTienSauCKTreo > ThanhTienSauCKPhanBo,
												 0, ThanhTienSauCKTreo )
				FROM CTE_Base
				WHERE RowNum = 1

				UNION ALL
				-- Tính toán đệ quy
				SELECT 
					b.ThucChayHopDongChiTietID,
					b.RecordStatus,
					b.ThanhTienKhuyenMaiTreo,
					b.ThanhTienSauCKTreo,
					b.ThanhTienKhuyenMaiDaTinh,
					b.ThanhTienSauCKDaTinh,
					b.ThanhTienKhuyenMaiPhanBo,
					b.ThanhTienSauCKPhanBo,
					b.HopDongChiTietID,
					b.RowNum,
					TichLuyThanhTienKM = IIF (r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo > b.ThanhTienKhuyenMaiPhanBo,
					                          r.TichLuyThanhTienKM, 
											  r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo ), 
					TichLuyThanhTienSauCK = IIF (r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo > b.ThanhTienSauCKPhanBo,
												 r.TichLuyThanhTienSauCK, 
												 r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo ),
					GhiNhanKM =	IIF (r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo > b.ThanhTienKhuyenMaiPhanBo,
									 0, b.ThanhTienKhuyenMaiTreo ),
					GhiNhanThanhTienSauCK = IIF (r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo > b.ThanhTienSauCKPhanBo,
												 0, b.ThanhTienSauCKTreo )
				FROM CTE_Base b 
				INNER JOIN CTE_Recursive r  ON r.HopDongChiTietID = b.HopDongChiTietID AND r.RowNum = b.RowNum - 1
			)

			UPDATE dm
			SET dm.LoaiXuLy = CASE WHEN LoaiThayDoi = 4
								   THEN 2
								   WHEN ISNULL(cte.GhiNhanKM, 0) = 0  AND ISNULL(cte.GhiNhanThanhTienSauCK, 0) = 0
										AND dm.RecordStatus = 1 
								   THEN 1
								   WHEN ISNULL(cte.GhiNhanKM, 0) = 0  AND ISNULL(cte.GhiNhanThanhTienSauCK, 0) = 0
										AND dm.RecordStatus = 0 
								   THEN 0
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 1 
								   THEN 2
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 0 
								   THEN 3
								   ELSE 0
							  END
			FROM #DmThayDoi dm
			INNER JOIN CTE_Recursive cte ON cte.ThucChayHopDongChiTietID = dm.ThucChayHopDongChiTietID
			WHERE dm.LoaiThayDoi IN (2,3,4)
			OPTION (MAXRECURSION 0);

			DELETE
			FROM #DmThayDoi
			WHERE LoaiXuLy = 0

			END 
		--=================================================== 2: Đối trừ thực chạy =============================================
		BEGIN
			INSERT INTO ABM_data_thucchay.dbo.ThucChayDaTinh
				   ([ThucChayDaTinhID]
				   ,[HopDongID]
				   ,[SoHopDong]
				   ,[DmMaHopDongREF]
				   ,[TenMaHopDong]
				   ,[NgayDanhSoHopDong]
				   ,[NgayKyHopDong]
				   ,[NhanHopDong]
				   ,[NgayNhanBanFax]
				   ,[NgayNhanHopDongBanCung]
				   ,[NgayChuyenHopDongChoKeToan]
				   ,[So]
				   ,[Thang]
				   ,[Nam]
				   ,[GiaTriHopDong]
				   ,[CongNo]
				   ,[HopDongChiTietREF]
				   ,[DangSuDung]
				   ,[IsGiayPhep]
				   ,[TrangThaiHopDong]
				   ,[IsBanCung]
				   ,[DmPhongBanREF]
				   ,[TenPhongBan]
				   ,[DmBoPhanREF]
				   ,[TenBoPhan]
				   ,[DmNhomLamViecREF]
				   ,[TenNhomLamViec]
				   ,[DmDiaDiemLamViecREF]
				   ,[TenDiaDiemLamViec]
				   ,[SysNhanVienREF]
				   ,[TenDangNhap]
				   ,[TenNhanVien]
				   ,[TenKhachHang]
				   ,[NhanHang]
				   ,[DmNhomNganhREF]
				   ,[TenNhomNganh]
				   ,[DmHinhThucQuangCao]
				   ,[TenHinhThucQuangCao]
				   ,[DmSanPhamREF]
				   ,[TenSanPham]
				   ,[DmNhomWebsiteREF]
				   ,[TenNhomWebsite]
				   ,[DmChuyenMucREF]
				   ,[TenChuyenMuc]
				   ,[DmLoaiBannerREF]
				   ,[TenLoaiBanner]
				   ,[DmViTriREF]
				   ,[TenViTri]
				   ,[DotChayHopDong]
				   ,[SoLuongDotChayHD]
				   ,[DotChayBooking]
				   ,[SoLuongDotChayBooking]
				   ,[SoLuong]
				   ,[DonViTinh]
				   ,[DonGia]
				   ,[DonGiaTheoDonVi]
				   ,[ChietKhau]
				   ,[GiamGia]
				   ,[ThanhTien]
				   ,[TiLeTuVan]
				   ,[ChiPhiTuVan]
				   ,[IsKhuyenMai]
				   ,[KhuyenMai]
				   ,[DmBannerREF]
				   ,[DmChienDichREF]
				   ,[DmWebsiteREF]
				   ,[TenWebsite]
				   ,[TongViewThucChay]
				   ,[TongClickThucChay]
				   ,[TongSoBaiViet]
				   ,[SoLuongThucChay]
				   ,[GiaTriThayDoi]
				   ,[ThanhTienThucChayTruocTrietKhau]
				   ,[GiaTriTrietKhauThucChay]
				   ,[ThanhTienSauTrietKhauThucChay]
				   ,[GiaTriHoaHongThucChay]
				   ,[ThanhTienThucThu]
				   ,[ThanhTienKM]
				   ,[SoLuongThucChayKM]
				   ,[SoLuongThucChayLechTreoHa]
				   ,[ThanhTienLechTreoHa]
				   ,[CreatedAt]
				   ,[LastModifiedAt]
				   ,[IsPheDuyet]
				   ,[PheDuyetBy]
				   ,[PheDuyetAt]
				   ,[SoLuongThayDoi]
				   ,[SoLuongKMThayDoi]
				   ,[GiaTriKMThayDoi]
				   ,[GhiChu]
				   ,[NgayThucHien])
			SELECT   NEWID() 
					,[HopDongID]
					,[SoHopDong]
					,[DmMaHopDongREF]
					,[TenMaHopDong]
					,[NgayDanhSoHopDong]
					,[NgayKyHopDong]
					,[NhanHopDong]
					,[NgayNhanBanFax]
					,[NgayNhanHopDongBanCung]
					,[NgayChuyenHopDongChoKeToan]
					,[So]
					,[Thang]
					,[Nam]
					,[GiaTriHopDong]
					,[CongNo]
					,[HopDongChiTietREF]
					,[DangSuDung]
					,[IsGiayPhep]
					,[TrangThaiHopDong]
					,[IsBanCung]
					,[DmPhongBanREF]
					,[TenPhongBan]
					,[DmBoPhanREF]
					,[TenBoPhan]
					,[DmNhomLamViecREF]
					,[TenNhomLamViec]
					,[DmDiaDiemLamViecREF]
					,[TenDiaDiemLamViec]
					,[SysNhanVienREF]
					,[TenDangNhap]
					,[TenNhanVien]
					,[TenKhachHang]
					,tcdt.[NhanHang]
					,tcdt.[DmNhomNganhREF]
					,tcdt.[TenNhomNganh]
					,[DmHinhThucQuangCao]
					,[TenHinhThucQuangCao]
					,tcdt.[DmSanPhamREF]
					,tcdt.[TenSanPham]
					,tcdt.[DmNhomWebsiteREF]
					,tcdt.[TenNhomWebsite]
					,tcdt.[DmChuyenMucREF]
					,tcdt.[TenChuyenMuc]
					,tcdt.[DmLoaiBannerREF]
					,tcdt.[TenLoaiBanner]
					,tcdt.[DmViTriREF]
					,tcdt.[TenViTri]
					,[DotChayHopDong] = N'Đối trừ Admatic donvibai'
					,[SoLuongDotChayHD]
					,[DotChayBooking]
					,[SoLuongDotChayBooking]
					,tcdt.[SoLuong]
					,tcdt.[DonViTinh]
					,tcdt.[DonGia]
					,[DonGiaTheoDonVi]
					,tcdt.[ChietKhau]
					,tcdt.[GiamGia]
					,tcdt.[ThanhTien]
					,tcdt.[TiLeTuVan]
					,tcdt.[ChiPhiTuVan]
					,tcdt.[IsKhuyenMai]
					,tcdt.[KhuyenMai]
					,tcdt.[DmBannerREF]
					,[DmChienDichREF]
					,tcdt.[DmWebsiteREF]
					,tcdt.[TenWebsite]
					,[TongViewThucChay]
					,[TongClickThucChay]
					,[TongSoBaiViet]
					,0 AS [SoLuongThucChay]
					,-SUM([ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) AS [GiaTriThayDoi]
					,-SUM([ThanhTienThucChayTruocTrietKhau]) AS [ThanhTienThucChayTruocTrietKhau]
					,-SUM([GiaTriTrietKhauThucChay]) AS [GiaTriTrietKhauThucChay]
					,0 AS [ThanhTienSauTrietKhauThucChay]
					,0 AS [GiaTriHoaHongThucChay]
					,0 AS [ThanhTienThucThu]
					,0 AS [ThanhTienKM]
					,0 AS [SoLuongThucChayKM]
					,0 AS [SoLuongThucChayLechTreoHa]
					,0 AS [ThanhTienLechTreoHa]
					,GETDATE() AS [CreatedAt]
					,GETDATE() AS [LastModifiedAt]
					,0 AS [IsPheDuyet]
					,'' AS [PheDuyetBy]
					,'' AS [PheDuyetAt]
					,-SUM(tcdt.[SoLuongThucChay] + tcdt.[SoLuongThayDoi]) AS [SoLuongThayDoi]
					,-SUM(tcdt.[SoLuongThucChayKM] + tcdt.[SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
					,-SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) AS [GiaTriKMThayDoi]
					, N'Đối trừ: SP tối ưu [dbo].[ThucChay_Admatic_DonViBai] do ' + dm.LyDo
					, dm.NgayThucHien
			FROM ABM_data_thucchay.dbo.[ThucChayDaTinh] tcdt
			INNER JOIN #DmThayDoi dm ON CAST(dm.ThucChayHopDongChiTietID AS NVARCHAR) = tcdt.DotChayBooking AND 
										dm.LoaiXuLy IN (1,2) AND 
                                        dm.HopDongChiTietID = tcdt.HopDongChiTietREF
            INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
			WHERE		tcdt.NgayThucHien < dm.NgayThucHien 
						AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
						AND ((tcdt.DmSanPhamREF  in (305,5312) ) OR	(tcdt.DmSanPhamREF  = 598 AND tcdt.DmVitriREF in (9198,100292)))
						AND tcdt.DmHinhThucQuangCao = 42
						--AND tcdt.DmVitriREF = 9198
						AND tcdt.DonViTinh IN ( N'BÀI', N'URL')
			GROUP BY [HopDongID]
					,[SoHopDong]
					,[DmMaHopDongREF]
					,[TenMaHopDong]
					,[NgayDanhSoHopDong]
					,[NgayKyHopDong]
					,[NhanHopDong]
					,[NgayNhanBanFax]
					,[NgayNhanHopDongBanCung]
					,[NgayChuyenHopDongChoKeToan]
					,[So]
					,[Thang]
					,[Nam]
					,[GiaTriHopDong]
					,[CongNo]
					,[HopDongChiTietREF]
					,[DangSuDung]
					,[IsGiayPhep]
					,[TrangThaiHopDong]
					,[IsBanCung]
					,[DmPhongBanREF]
					,[TenPhongBan]
					,[DmBoPhanREF]
					,[TenBoPhan]
					,[DmNhomLamViecREF]
					,[TenNhomLamViec]
					,[DmDiaDiemLamViecREF]
					,[TenDiaDiemLamViec]
					,[SysNhanVienREF]
					,[TenDangNhap]
					,[TenNhanVien]
					,[TenKhachHang]
					,tcdt.[NhanHang]
					,tcdt.[DmNhomNganhREF]
					,tcdt.[TenNhomNganh]
					,[DmHinhThucQuangCao]
					,[TenHinhThucQuangCao]
					,tcdt.[DmSanPhamREF]
					,tcdt.[TenSanPham]
					,tcdt.[DmNhomWebsiteREF]
					,tcdt.[TenNhomWebsite]
					,tcdt.[DmChuyenMucREF]
					,tcdt.[TenChuyenMuc]
					,tcdt.[DmLoaiBannerREF]
					,tcdt.[TenLoaiBanner]
					,tcdt.[DmViTriREF]
					,tcdt.[TenViTri]
					,[SoLuongDotChayHD]
					,[DotChayBooking]
					,[SoLuongDotChayBooking]
					,tcdt.[SoLuong]
					,tcdt.[DonViTinh]
					,tcdt.[DonGia]
					,[DonGiaTheoDonVi]
					,tcdt.[ChietKhau]
					,tcdt.[GiamGia]
					,tcdt.[ThanhTien]
					,tcdt.[TiLeTuVan]
					,tcdt.[ChiPhiTuVan]
					,tcdt.[IsKhuyenMai]
					,tcdt.[KhuyenMai]
					,tcdt.[DmBannerREF]
					,tcdt.[DmChienDichREF]
					,tcdt.[DmWebsiteREF]
					,tcdt.[TenWebsite]
					,[TongViewThucChay]
					,[TongClickThucChay]
					,[TongSoBaiViet]
					,dm.LyDo
					,dm.NgayThucHien
			HAVING SUM(tcdt.[ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) <> 0
				   OR SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) <> 0


			UPDATE  tchdct
            SET     tchdct.RecordStatus = 0
			FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct 
			INNER JOIN #DmThayDoi dm ON dm.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND dm.LoaiXuLy IN (1,2)
		END
		--=================================================== 3: Tính mới hoặc tính lại thực chạy ==============================
		BEGIN
			INSERT INTO ABM_data_thucchay.dbo.ThucChayDaTinh
			(       ThucChayDaTinhID,
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
					GhiChu)
			SELECT  NEWID(),
					hd.HopDongID ,
					hd.SoHopDong ,
					hd.DmMaHopDongREF ,
					hd.TenMaHopDong,
					hd.NgayDanhSoHopDong ,
					hd.NgayKyHopDong ,
					ISNULL(hd.NhanHopDong, '') AS NhanHopDong ,
					hd.NgayNhanBanFax ,
					hd.NgayNhanHopDongBanCung ,
					hd.NgayChuyenHopDongChoKeToan ,
					hd.So ,
					hd.Thang ,
					hd.Nam , 
					hd.GiaTriHopDong ,
					hd.CongNo ,
					hdct.HopDongChiTietID ,
					hd.DangSuDung ,
					hd.IsGiayPhep ,
					hd.TrangThaiHopDong ,
					hd.IsBanCung , 
					hd.DmPhongBanREF ,
					ISNULL(hd.TenPhongBan, '') AS TenPhongBan ,
					hd.DmBoPhanREF ,
					ISNULL(hd.TenBoPhan, '') AS TenBoPhan ,
					hd.DmNhomLamViecREF ,
					ISNULL(hd.TenNhom, '') AS TenNhom ,
					hd.DmDiaDiemLamViecREF ,
					hd.TenDiaDiemLamViec ,
					hd.SysNhanVienREF ,
					ISNULL(hd.TenDangNhap, '') AS TenDangNhap ,
					hd.TenNhanVien , 
					hd.TenKhachHang , 
					ISNULL(tchdct.DmNhanHangREF,'') NhanHang ,    
					hdct.DmNhomNganhREF ,
					hdct.TenNhomNganh , 
					hdct.DmLoaiREF AS DmHinhThucQuangCao ,
					hdct.TenLoai AS TenHinhThucQuangCao , 
					hdct.DmSanPhamREF AS DmSanPhamREF ,
					hdct.TenSanPham ,
					hdct.DmNhomWebsiteREF ,
					hdct.TenNhomWebsite , 
					hdct.DmChuyenMucREF ,
					hdct.TenChuyenMuc ,
					hdct.DmLoaiBannerREF ,
					hdct.TenLoaiBanner ,
					hdct.DmViTriREF ,
					hdct.TenViTri ,
					DotChayHopDong = IIF(dm.LoaiXuLy = 2, N'Tính lại Admatic DonViBai', N'Tính mới Admatic DonVibai'),   
					0 AS SoLuongDotChayHD ,
					tchdct.ThucChayHopDongChiTietID DotChayBooking ,
					0 AS SoLuongDotChayBooking , 
					hdct.SoLuong AS SoLuong ,
					UPPER(ISNULL(hdct.DonViTinh, N'đ/v')) AS DonViTinh ,
					hdct.DonGia AS DonGia , 
					hdct.DonGia AS DonGiaTheoDonViTinh ,
					hdct.ChietKhau ChietKhau ,
					hdct.GiamGia ,
					hdct.ThanhTien ,
					hdct.TiLeTuVan ,
					hdct.ChiPhiTuVan ,
					hdct.IsKhuyenMai ,
					hdct.KhuyenMai ,
					0 DmBannerREF ,
					0 DmChienDichREF ,
					dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(hdct.DmWebsiteREF) DmWebsiteREF ,
					dbo.GetWebsiteLinkByDmWebsiteID(hdct.DmWebsiteREF, hdct.TenWebsite) TenWebsite ,
					0 TongViewThucChay ,
					0 TongClickThucChay ,
					0 TongSoBaiViet ,
					SoLuongThucChay = IIF(dm.LoaiXuLy = 2 OR hdct.IsKhuyenMai = 1, 0, 1),
					@NgayGhiNhan AS NgayThucHien ,
					IIF(dm.LoaiXuLy = 2, dm.ThanhTienSauCKTreo, 0) AS GiaTriThayDoi ,
					IIF(dm.LoaiXuLy = 2 OR hdct.ChietKhau = 100, 0, dm.ThanhTienSauCKTreo/(1-ISNULL(hdct.ChietKhau, 0)/100)) AS ThanhTienThucChayTruocTrietKhau,
					IIF(dm.LoaiXuLy = 2, 0, (dm.ThanhTienSauCKTreo/(1-ISNULL(hdct.ChietKhau, 0)/100)) * ISNULL(hdct.ChietKhau, 0) / 100) AS GiaTriTrietKhauThucChay ,
					IIF(dm.LoaiXuLy = 2, 0, dm.ThanhTienSauCKTreo) AS ThanhTienSauTrietKhauThucChay ,
					IIF(dm.LoaiXuLy = 2, 0, dm.ThanhTienSauCKTreo * ISNULL(hdct.TiLeTuVan, 0)/100) AS GiaTriHoaHongThucChay ,
					IIF(dm.LoaiXuLy = 2, 0, dm.ThanhTienSauCKTreo * (1 - ISNULL(hdct.TiLeTuVan, 0)/100)) AS ThanhTienThucThu ,
					IIF(dm.LoaiXuLy = 2, 0, dm.ThanhTienKhuyenMaiTreo) AS ThanhTienKM ,
					IIF(dm.LoaiXuLy = 2 OR hdct.IsKhuyenMai = 0, 0, 1) AS SoLuongThucChayKM ,
					0 SoLuongLechTreoHa ,
					0 ThanhTienLechTreoHa ,
					GETDATE() ,
					GETDATE() ,
					0 IsPheDuyet ,
					'' PheDuyetBy ,
					'' PheDuyetAt ,
					IIF(dm.LoaiXuLy = 2 AND hdct.IsKhuyenMai = 0, 1, 0) SoLuongThayDoi ,
					IIF(dm.LoaiXuLy = 2 AND hdct.IsKhuyenMai = 1, 1, 0) SoLuongKMThayDoi ,
					IIF(dm.LoaiXuLy = 2 AND hdct.IsKhuyenMai = 1, dm.ThanhTienKhuyenMaiTreo, 0) GiaTriKMThayDoi ,
					IIF(dm.LoaiXuLy = 2, N'Tính lại: ', N'Tính mới: ') + N'SP tối ưu [dbo].[ThucChay_Admatic_DonViBai] do ' + dm.LyDo
			FROM  ABM_data_thucchay.dbo.HopDongChiTiet hdct
			INNER JOIN ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
			INNER JOIN #DmThayDoi dm ON dm.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID
			INNER JOIN ABM_data_thucchay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE   dm.LoaiXuLy IN (2,3) AND dm.LoaiThayDoi <> 4
			UNION
			SELECT   NEWID() 
					,[HopDongID]
					,[SoHopDong]
					,[DmMaHopDongREF]
					,[TenMaHopDong]
					,[NgayDanhSoHopDong]
					,[NgayKyHopDong]
					,[NhanHopDong]
					,[NgayNhanBanFax]
					,[NgayNhanHopDongBanCung]
					,[NgayChuyenHopDongChoKeToan]
					,[So]
					,[Thang]
					,[Nam]
					,[GiaTriHopDong]
					,[CongNo]
					,[HopDongChiTietREF]
					,[DangSuDung]
					,[IsGiayPhep]
					,[TrangThaiHopDong]
					,[IsBanCung]
					,[DmPhongBanREF]
					,[TenPhongBan]
					,[DmBoPhanREF]
					,[TenBoPhan]
					,[DmNhomLamViecREF]
					,[TenNhomLamViec]
					,[DmDiaDiemLamViecREF]
					,[TenDiaDiemLamViec]
					,[SysNhanVienREF]
					,[TenDangNhap]
					,[TenNhanVien]
					,[TenKhachHang]
					,tcdt.[NhanHang]
					,tcdt.[DmNhomNganhREF]
					,tcdt.[TenNhomNganh]
					,[DmHinhThucQuangCao]
					,[TenHinhThucQuangCao]
					,tcdt.[DmSanPhamREF]
					,tcdt.[TenSanPham]
					,tcdt.[DmNhomWebsiteREF]
					,tcdt.[TenNhomWebsite]
					,tcdt.[DmChuyenMucREF]
					,tcdt.[TenChuyenMuc]
					,tcdt.[DmLoaiBannerREF]
					,tcdt.[TenLoaiBanner]
					,tcdt.[DmViTriREF]
					,tcdt.[TenViTri]
					,[DotChayHopDong] = N'Tính lại Admatic donvibai'
					,[SoLuongDotChayHD]
					,[DotChayBooking]
					,[SoLuongDotChayBooking]
					,tcdt.[SoLuong]
					,tcdt.[DonViTinh]
					,tcdt.[DonGia]
					,[DonGiaTheoDonVi]
					,tcdt.[ChietKhau]
					,tcdt.[GiamGia]
					,tcdt.[ThanhTien]
					,tcdt.[TiLeTuVan]
					,tcdt.[ChiPhiTuVan]
					,tcdt.[IsKhuyenMai]
					,tcdt.[KhuyenMai]
					,tcdt.[DmBannerREF]
					,[DmChienDichREF]
					,tcdt.[DmWebsiteREF]
					,tcdt.[TenWebsite]
					,[TongViewThucChay]
					,[TongClickThucChay]
					,[TongSoBaiViet]
					,0 AS [SoLuongThucChay]
					,dm.NgayThucHien
					,SUM([ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) AS [GiaTriThayDoi]
					,SUM([ThanhTienThucChayTruocTrietKhau]) AS [ThanhTienThucChayTruocTrietKhau]
					,SUM([GiaTriTrietKhauThucChay]) AS [GiaTriTrietKhauThucChay]
					,0 AS [ThanhTienSauTrietKhauThucChay]
					,0 AS [GiaTriHoaHongThucChay]
					,0 AS [ThanhTienThucThu]
					,0 AS [ThanhTienKM]
					,0 AS [SoLuongThucChayKM]
					,0 AS [SoLuongThucChayLechTreoHa]
					,0 AS [ThanhTienLechTreoHa]
					,GETDATE() AS [CreatedAt]
					,GETDATE() AS [LastModifiedAt]
					,0 AS [IsPheDuyet]
					,'' AS [PheDuyetBy]
					,'' AS [PheDuyetAt]
					,SUM(tcdt.[SoLuongThucChay] + tcdt.[SoLuongThayDoi]) AS [SoLuongThayDoi]
					,SUM(tcdt.[SoLuongThucChayKM] + tcdt.[SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
					,SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) AS [GiaTriKMThayDoi]
					, N'Tính lại: SP tối ưu [dbo].[ThucChay_Admatic_DonViBai] do ' + dm.LyDo
			FROM ABM_data_thucchay.dbo.[ThucChayDaTinh] tcdt
			INNER JOIN #DmThayDoi dm ON CAST(dm.ThucChayHopDongChiTietID AS NVARCHAR) = tcdt.DotChayBooking AND 
										dm.LoaiXuLy = 2 AND 
                                        dm.HopDongChiTietID = tcdt.HopDongChiTietREF AND
                                        dm.LoaiThayDoi = 4
            INNER JOIN ABM_data_thucchay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
			WHERE		tcdt.NgayThucHien < dm.NgayThucHien 
						AND NOT ( tcdt.DmLoaiBannerREF IN (17,18)OR tcdt.DmHinhThucQuangCao IN (13))
						AND ((tcdt.DmSanPhamREF  in (305,5312) ) OR	(tcdt.DmSanPhamREF  = 598 AND tcdt.DmVitriREF in (9198,100292)))
						AND tcdt.DmHinhThucQuangCao = 42
						--AND tcdt.DmVitriREF = 9198
						AND tcdt.DonViTinh IN ( N'BÀI', N'URL')
			GROUP BY [HopDongID]
					,[SoHopDong]
					,[DmMaHopDongREF]
					,[TenMaHopDong]
					,[NgayDanhSoHopDong]
					,[NgayKyHopDong]
					,[NhanHopDong]
					,[NgayNhanBanFax]
					,[NgayNhanHopDongBanCung]
					,[NgayChuyenHopDongChoKeToan]
					,[So]
					,[Thang]
					,[Nam]
					,[GiaTriHopDong]
					,[CongNo]
					,[HopDongChiTietREF]
					,[DangSuDung]
					,[IsGiayPhep]
					,[TrangThaiHopDong]
					,[IsBanCung]
					,[DmPhongBanREF]
					,[TenPhongBan]
					,[DmBoPhanREF]
					,[TenBoPhan]
					,[DmNhomLamViecREF]
					,[TenNhomLamViec]
					,[DmDiaDiemLamViecREF]
					,[TenDiaDiemLamViec]
					,[SysNhanVienREF]
					,[TenDangNhap]
					,[TenNhanVien]
					,[TenKhachHang]
					,tcdt.[NhanHang]
					,tcdt.[DmNhomNganhREF]
					,tcdt.[TenNhomNganh]
					,[DmHinhThucQuangCao]
					,[TenHinhThucQuangCao]
					,tcdt.[DmSanPhamREF]
					,tcdt.[TenSanPham]
					,tcdt.[DmNhomWebsiteREF]
					,tcdt.[TenNhomWebsite]
					,tcdt.[DmChuyenMucREF]
					,tcdt.[TenChuyenMuc]
					,tcdt.[DmLoaiBannerREF]
					,tcdt.[TenLoaiBanner]
					,tcdt.[DmViTriREF]
					,tcdt.[TenViTri]
					,[SoLuongDotChayHD]
					,[DotChayBooking]
					,[SoLuongDotChayBooking]
					,tcdt.[SoLuong]
					,tcdt.[DonViTinh]
					,tcdt.[DonGia]
					,[DonGiaTheoDonVi]
					,tcdt.[ChietKhau]
					,tcdt.[GiamGia]
					,tcdt.[ThanhTien]
					,tcdt.[TiLeTuVan]
					,tcdt.[ChiPhiTuVan]
					,tcdt.[IsKhuyenMai]
					,tcdt.[KhuyenMai]
					,tcdt.[DmBannerREF]
					,tcdt.[DmChienDichREF]
					,tcdt.[DmWebsiteREF]
					,tcdt.[TenWebsite]
					,[TongViewThucChay]
					,[TongClickThucChay]
					,[TongSoBaiViet]
					,dm.LyDo
					,dm.NgayThucHien
			HAVING SUM(tcdt.[ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) <> 0
				   OR SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) <> 0
                             	
			UPDATE  tchdct
            SET     tchdct.RecordStatus = 1
			FROM  ABM_data_thucchay.dbo.ThucChayHopDongChiTiet tchdct 
			INNER JOIN #DmThayDoi dm ON dm.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND dm.LoaiXuLy IN (2,3)
		END

		DROP TABLE #DmThayDoi
	END


```
