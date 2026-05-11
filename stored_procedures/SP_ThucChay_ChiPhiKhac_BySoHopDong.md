# Stored Procedure: `ThucChay_ChiPhiKhac_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-02-26 11:58:57.490000
- **Ngày sửa cuối**: 2025-06-27 17:01:56.517000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `datetime(8)` | No |
| `@NgayCheckThayDoi` | `datetime(8)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@ThoiGianBDTinh` | `datetime(8)` | No |
| `@NgayDanhSoGioiHan_Tiktok` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChay_ChiPhiKhac_BySoHopDong]
    @NgayGhiNhan DATETIME,
    @NgayCheckThayDoi  DATETIME = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@ThoiGianBDTinh DATETIME = '2010-01-01',
	@NgayDanhSoGioiHan_Tiktok DATETIME = '2022-01-01',
	@SoHopDong NVARCHAR(100) = NULL,
	@HopDongChiTietID INT = NULL
AS
    BEGIN
        DECLARE @xulytay NVARCHAR(50),
		@NgayDanhSoGioiHan_PB_MKT DATETIME = '2025-07-01'

		SET @xulytay = IIF(@SoHopDong IS NOT NULL, N'xử lý tay ', N'')


		CREATE TABLE #DmThayDoi 
		( ThucChayHopDongChiTietID INT,
		  HopDongChiTietID INT,
		  HopDongREF INT ,
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
		  LoaiXuLy INT -- 0: không xử lý, 1: đối trừ, 2: đối từ tính lại, 3: ghi nhận mới
		)


		DELETE
		FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh 
		WHERE   NgayThucHien = @NgayGhiNhan
                AND GhiChu LIKE N'%ThucChay_ChiPhiKhac%'
				AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
				AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)
        --=================================================== 1: Xác định danh mục ID cần đối trừ hoặc ghi nhận thêm ====================================
		/* TH1 phân bổ hoặc hợp đồng xóa, hủy hoặc ID treo hủy: đối trừ toàn bộ các ID treo liên quan đã được ghi nhận thực chạy
		   TH2 phân bổ thay đổi giá trị hoặc ID treo thay đổi giá trị hoặc ID treo thêm mới 
		       Nếu tổng không vượt thì ghi nhận mới hoặc đối trừ tính lại với ID treo đã ghi nhận
			   Nếu tổng vượt thì với mỗi phân bổ sắp xếp ID treo theo thứ tự: RecordStatus 1->0, LastModifiedAt asc, ID treo asc
					=> duyệt từ dưới lên, nếu vượt thì đối trừ, tính lại với ID treo đã tính, nếu chưa vượt thì ghi nhận mới với ID chưa ghi nhận
		
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
					LyDo =	N'hợp đồng xóa, hủy hoặc hủy phân bổ hoặc ID treo hủy hoặc ID treo thay đổi trạng thái duyệt',
					LoaiXuLy = 1
			FROM  ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE  tchdct.RecordStatus = 1 
				   AND ( @NgayCheckThayDoi IS NULL OR 
						((hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1) AND 
						 CONVERT(DATE, ISNULL(hd.LastModifiedAt, hd.CreatedAt))  = @NgayCheckThayDoi) OR
						(hdct.DeletedStatus = 1 AND 
						 CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi) OR
						((tchdct.DeletedStatus = 1 OR tchdct.TrangThaiTreo <> 2) AND 
						 CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi)
					   )
				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND NOT (hdct.DmViTriREF in (100093,100478))
				   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				   --AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – Chi phí marketing
				   AND (EXISTS( SELECT TOP (1) ch.ID 
							    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
								AND ch.DeletedStatus = 0 ORDER BY ch.ID
					   ))
				   AND NOT (hdct.DmSanPhamREF = 5184 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
				   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  (hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok))
				   AND (@ThoiGianBDTinh IS NULL OR CONVERT(DATE, tchdct.ThoiGianBatDau) >= @ThoiGianBDTinh)
				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																		WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																		order by hdv.HopDongChiTietREF)
				   AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
				   AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
			UNION
			SELECT  DISTINCT
					tchdct.ThucChayHopDongChiTietID,
					l.HopDongChiTietREF ,
					hd.HopDongID ,
					NgayThucHien =  @NgayGhiNhan,
					LoaiThayDoi = 6,
					LyDo =	N'ID treo gỡ phân bổ',
					LoaiXuLy = 1
			FROM 
		  ( SELECT * 
			FROM  ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
			WHERE  tchdct.RecordStatus = 1 AND tchdct.HopDongChiTietREF =  0  AND 
				   (@NgayCheckThayDoi IS NULL OR CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi )) tchdct 
			OUTER APPLY (SELECT TOP 1 l.HopDongChiTietREF
			             FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietLog l
						 WHERE l.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND
						       CONVERT(DATE, ISNULL(l.LastModifiedAt, l.CreatedAt)) < CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt))
						 ORDER BY CONVERT(DATE, ISNULL(l.LastModifiedAt, l.CreatedAt)) DESC) l
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON l.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE  NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND NOT (hdct.DmViTriREF in (100093,100478))
				   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				   --AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – Chi phí marketing
				   AND (EXISTS( SELECT TOP (1) ch.ID 
							    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
								AND ch.DeletedStatus = 0 ORDER BY ch.ID
					   ))
				   AND NOT (hdct.DmSanPhamREF = 5184 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
				   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  (hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok))
				   AND (@ThoiGianBDTinh IS NULL OR CONVERT(DATE, tchdct.ThoiGianBatDau) >= @ThoiGianBDTinh)
				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																		WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																		order by hdv.HopDongChiTietREF)
				   AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
				   AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)



			
			INSERT INTO #DmThayDoi
			(   ThucChayHopDongChiTietID ,
				HopDongChiTietID ,
				HopDongREF  ,
				NgayThucHien ,
				RecordStatus ,
				LastModifiedAt ,
				ThanhTienKhuyenMaiTreo ,
				ThanhTienSauCKTreo,
			    ThanhTienKhuyenMaiPhanBo ,
				ThanhTienSauCKPhanBo,
				LoaiThayDoi , 
				LyDo 
			)
			SELECT DISTINCT
					tchdct.ThucChayHopDongChiTietID,
					tchdct.HopDongChiTietREF ,
					tchdct.HopDongREF ,
					NgayThucHien =  @NgayGhiNhan,
					tchdct.RecordStatus,
					tchdct.LastModifiedAt,
					ThanhTienKhuyenMaiTreo = IIF(tchdct.ChietKhau = 100,tchdct.SoLuongThucTreo*tchdct.DonGia, 0),
					ThanhTienSauCKTreo =  tchdct.SoLuongThucTreo*tchdct.DonGia*(1-tchdct.ChietKhau/100),
					ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100,hdct.SoLuong*hdct.DonGia, 0),
					ThanhTienSauCKPhanBo = hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100),
					LoaiThayDoi = CASE WHEN tchdct.RecordStatus = 1 AND (CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi) AND 
								            (CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi)
									   THEN 2
									   WHEN tchdct.RecordStatus = 1 AND (CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi)
									   THEN 3
									   WHEN tchdct.RecordStatus = 1 AND (CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi)
									   THEN 4
									   WHEN tchdct.RecordStatus = 1 AND @SoHopDong IS NOT NULL AND @NgayCheckThayDoi IS NULL
								       THEN 7
									   WHEN tchdct.RecordStatus = 0
									   THEN 5
									   ELSE 0
								  END,
					LyDo = CASE WHEN tchdct.RecordStatus = 1 AND (CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi) AND 
								     (CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi)
								THEN N'phân bổ và thực treo có thay đổi giá trị'
								WHEN tchdct.RecordStatus = 1 AND (CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi)
								THEN N'phân bổ có thay đổi giá trị'
								WHEN tchdct.RecordStatus = 1 AND (CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi)
								THEN N'thực treo có thay đổi giá trị'
								WHEN tchdct.RecordStatus = 1 AND @SoHopDong IS NOT NULL AND @NgayCheckThayDoi IS NULL
								THEN N'chạy lại phân bổ'
								WHEN tchdct.RecordStatus = 0
								THEN N'thực treo ghi nhận mới'
								ELSE ''
							END
			FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE ( @NgayCheckThayDoi IS NULL OR 
			       (CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi) OR
			       (CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi))
                   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND NOT (hdct.DmViTriREF in (100093,100478))
				   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				   --AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – Chi phí marketing
				   AND (EXISTS( SELECT TOP (1) ch.ID 
							    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
								AND ch.DeletedStatus = 0 ORDER BY ch.ID
					   ))
				   AND NOT (hdct.DmSanPhamREF = 5184 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) --NGAYDANHSO CreatorContent 2021-10-01
				   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  (hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Tiktok)) 
				   AND (hd.TrangThaiHopDong <> 3 OR hd.DeletedStatus = 0)
				   AND hdct.DeletedStatus = 0
				   AND (@ThoiGianBDTinh IS NULL OR CONVERT(DATE, tchdct.ThoiGianBatDau) >= @ThoiGianBDTinh)
				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND tchdct.TrangThaiTreo = 2
				   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																		WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																		order by hdv.HopDongChiTietREF)
				   AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
				   AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
			
			UPDATE dm
			SET dm.LoaiThayDoi = IIF(LoaiThayDoi = 4, 0, 3)
			FROM #DmThayDoi dm
			OUTER APPLY (SELECT TOP 1 ThanhTienKhuyenMaiTreo = IIF(tchdct.ChietKhau = 100,tchdct.SoLuongThucTreo*tchdct.DonGia, 0),
									  ThanhTienSauCKTreo =  tchdct.SoLuongThucTreo*tchdct.DonGia*(1-tchdct.ChietKhau/100)
						 FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietLog tchdct
						 WHERE tchdct.ThucChayHopDongChiTietID = dm.ThucChayHopDongChiTietID AND
                               CAST(tchdct.LastModifiedAt AS DATE) < @NgayCheckThayDoi
						 ORDER BY tchdct.LastModifiedAt desc) tchdct 
			WHERE ( @NgayCheckThayDoi IS NULL OR 
			        (ROUND(dm.ThanhTienKhuyenMaiTreo - ISNULL(tchdct.ThanhTienKhuyenMaiTreo, 0), 0) = 0 AND 
				     ROUND(dm.ThanhTienSauCKTreo - ISNULL(tchdct.ThanhTienSauCKTreo, 0), 0) = 0))  	AND
				   LoaiThayDoi IN (2, 4)

			UPDATE dm
			SET dm.LoaiThayDoi = 0
			FROM #DmThayDoi dm
			OUTER APPLY (SELECT TOP 1 ThanhTienKhuyenMaiPhanBo = IIF(hdct.ChietKhau = 100,hdct.SoLuong*hdct.DonGia, 0), 
									  ThanhTienSauCKPhanBo = hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100)
						 FROM ABM_Data_ThucChay.dbo.HopDongChiTietLog hdct
						 WHERE hdct.HopDongChiTietREF = dm.HopDongChiTietID AND
                               CAST(hdct.LastModifiedAt AS DATE) < @NgayCheckThayDoi
						 ORDER BY hdct.LastModifiedAt desc) hdct 
			WHERE  ( @NgayCheckThayDoi IS NULL OR
			         (ROUND(dm.ThanhTienKhuyenMaiPhanBo - ISNULL(hdct.ThanhTienKhuyenMaiPhanBo, 0), 0) = 0 AND 
				      ROUND(dm.ThanhTienSauCKPhanBo - ISNULL(hdct.ThanhTienSauCKPhanBo, 0), 0) = 0 )) 	AND
				   LoaiThayDoi = 3

			DELETE
			FROM #DmThayDoi
			WHERE LoaiThayDoi = 0

			UPDATE dm
			SET dm.ThanhTienKhuyenMaiDaTinh = ISNULL(tchdct.ThanhTienKhuyenMaiDaTinh,0),
			    dm.ThanhTienSauCKDaTinh = ISNULL(tchdct.ThanhTienSauCKDaTinh,0)
			FROM #DmThayDoi dm
			OUTER APPLY (SELECT ThanhTienKhuyenMaiDaTinh = SUM (IIF(tchdct.ChietKhau = 100,tchdct.SoLuongThucTreo*tchdct.DonGia, 0)),
			                    ThanhTienSauCKDaTinh =  SUM(tchdct.SoLuongThucTreo*tchdct.DonGia*(1-tchdct.ChietKhau/100))
						 FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
						 WHERE dm.HopDongChiTietID = tchdct.HopDongChiTietREF AND
						       tchdct.ThucChayHopDongChiTietID NOT IN (SELECT ThucChayHopDongChiTietID FROM #DmThayDoi) AND
							   tchdct.RecordStatus = 1
							   AND TrangThaiTreo=2) tchdct
			WHERE dm.LoaiThayDoi IN (2, 3, 4, 5, 7)

			UPDATE dm
			SET dm.LyDo = @xulytay + dm.LyDo
			FROM #DmThayDoi dm

		END
		--=================================================== 2: Xác định phương thức xử lý cho ID treo thuộc: LoaiThayDoi in (2,3,4) ===========
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
				WHERE LoaiThayDoi IN (2, 3, 4, 5, 7) ),

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
					TichLuyThanhTienKM = IIF (ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo > ThanhTienKhuyenMaiPhanBo,
					                          ThanhTienKhuyenMaiDaTinh, 
											  ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo ), 
					TichLuyThanhTienSauCK = IIF (ThanhTienSauCKDaTinh + ThanhTienSauCKTreo > ThanhTienSauCKPhanBo,
												 ThanhTienSauCKDaTinh, 
												 ThanhTienSauCKDaTinh + ThanhTienSauCKTreo ),
					GhiNhanKM = IIF(ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo > ThanhTienKhuyenMaiPhanBo,
					                0, ThanhTienKhuyenMaiTreo ),
					GhiNhanThanhTienSauCK = IIF (ThanhTienSauCKDaTinh + ThanhTienSauCKTreo > ThanhTienSauCKPhanBo,
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
			SET dm.LoaiXuLy = CASE WHEN ISNULL(cte.GhiNhanKM, 0) = 0  AND ISNULL(cte.GhiNhanThanhTienSauCK, 0) = 0
										AND dm.RecordStatus = 1 
								   THEN 1
								   WHEN ISNULL(cte.GhiNhanKM, 0) = 0  AND ISNULL(cte.GhiNhanThanhTienSauCK, 0) = 0
										AND dm.RecordStatus = 0 
								   THEN 0
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 1 AND LoaiThayDoi IN (2,4,7) 
								   THEN 2
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 1 AND LoaiThayDoi NOT IN (2,4) 
								   THEN 0
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 0 
								   THEN 3
								   ELSE 0
							  END
			FROM #DmThayDoi dm
			INNER JOIN CTE_Recursive cte ON cte.ThucChayHopDongChiTietID = dm.ThucChayHopDongChiTietID
			WHERE dm.LoaiThayDoi IN (2,3,4,5,7)
			OPTION (MAXRECURSION 0);

			END 
		--=================================================== 2: Đối trừ thực chạy =============================================
		BEGIN
			INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
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
					,[DotChayHopDong]
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
					, N'Đối trừ: SP tối ưu [dbo].[ThucChay_ChiPhiKhac] do ' + dm.LyDo
					, dm.NgayThucHien
			FROM ABM_Data_ThucChay.dbo.[ThucChayDaTinh] tcdt
			INNER JOIN #DmThayDoi dm ON CAST(dm.ThucChayHopDongChiTietID AS NVARCHAR) = tcdt.DotChayBooking AND 
										dm.LoaiXuLy IN (1,2) AND
										dm.LoaiThayDoi <> 6 AND
                                        dm.HopDongChiTietID = tcdt.HopDongChiTietREF
            INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
			WHERE		tcdt.NgayThucHien < dm.NgayThucHien 
						AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
						AND NOT (hdct.DmViTriREF in (100093,100478))
						----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
						--AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – Chi phí marketing
						AND (EXISTS( SELECT TOP (1) ch.ID 
									FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
									WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
									AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
									AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
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
					,[DotChayHopDong]
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
					,[DotChayHopDong]
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
					, N'Đối trừ: SP tối ưu [dbo].[ThucChay_ChiPhiKhac] do ' + dm.LyDo
					, dm.NgayThucHien
			FROM ABM_Data_ThucChay.dbo.[ThucChayDaTinh] tcdt
			INNER JOIN #DmThayDoi dm ON CAST(dm.ThucChayHopDongChiTietID AS NVARCHAR) = tcdt.DotChayBooking AND 
										dm.LoaiXuLy IN (1,2) AND
										dm.LoaiThayDoi = 6 
            INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
			WHERE		tcdt.NgayThucHien < dm.NgayThucHien 
						AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
						AND NOT (hdct.DmViTriREF in (100093,100478))
						----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
						--AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND tcdt.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – Chi phí marketing
						AND (EXISTS( SELECT TOP (1) ch.ID 
									FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
									WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
									AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
									AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
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
					,[DotChayHopDong]
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
			FROM  ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
			INNER JOIN #DmThayDoi dm ON dm.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND dm.LoaiXuLy IN (1,2)
		END
		--=================================================== 3: Tính mới hoặc tính lại thực chạy ==============================
		BEGIN
			INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
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
					sp.TenSanPham ,
					hdct.DmNhomWebsiteREF ,
					hdct.TenNhomWebsite , 
					hdct.DmChuyenMucREF ,
					hdct.TenChuyenMuc ,
					hdct.DmLoaiBannerREF ,
					hdct.TenLoaiBanner ,
					hdct.DmViTriREF ,
					hdct.TenViTri ,
					'' DotChayHopDong ,
					0 AS SoLuongDotChayHD ,
					tchdct.ThucChayHopDongChiTietID DotChayBooking ,
					0 AS SoLuongDotChayBooking , 
					tchdct.SoLuongThucTreo AS SoLuong ,
					ISNULL(hdct.DonViTinh, N'đ/v') AS DonViTinh ,
					hdct.DonGia AS DonGia , 
					hdct.DonGia AS DonGiaTheoDonViTinh ,
					tchdct.ChietKhau ChietKhau ,
					hdct.GiamGia ,
					hdct.ThanhTien ,
					hdct.TiLeTuVan ,
					hdct.ChiPhiTuVan ,
					hdct.IsKhuyenMai ,
					hdct.KhuyenMai ,
					0 DmBannerREF ,
					0 DmChienDichREF ,
					CASE WHEN ISNULL(hdct.DmWebsiteREF,265) = 265 
						 THEN dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(ISNULL(tchdct.DmWebsiteREF,265)) 
						 ELSE dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(hdct.DmWebsiteREF)
					END	DmWebsiteREF ,
					CASE WHEN ISNULL(hdct.DmWebsiteREF,265) = 265 
						 THEN dbo.GetWebsiteLinkByDmWebsiteID(ISNULL(tchdct.DmWebsiteREF,265), ISNULL(tchdct.TenWebsite,N'(Blanks)')) 
						 ELSE dbo.GetWebsiteLinkByDmWebsiteID(hdct.DmWebsiteREF, hdct.TenWebsite) 
					END TenWebsite ,
					0 TongViewThucChay ,
					0 TongClickThucChay ,
					0 TongSoBaiViet ,
					SoLuongThucChay = IIF(dm.LoaiXuLy = 2, 0, IIF(hdct.IsKhuyenMai = 0, ISNULL(tchdct.SoLuongThucTreo, 0), 0)),
					@NgayGhiNhan AS NgayThucHien ,
					IIF(dm.LoaiXuLy = 2, ISNULL( tchdct.SoLuongThucTreo, 0) * ISNULL(tchdct.DonGia, 0) * (1 - ISNULL(hdct.ChietKhau, 0) / 100), 0) AS GiaTriThayDoi ,
					IIF(dm.LoaiXuLy = 2, 0, ISNULL( tchdct.SoLuongThucTreo, 0) * ISNULL(tchdct.DonGia, 0)) AS ThanhTienThucChayTruocTrietKhau,
					IIF(dm.LoaiXuLy = 2, 0, ISNULL( tchdct.SoLuongThucTreo, 0) * ISNULL(tchdct.DonGia, 0) * ISNULL(hdct.ChietKhau, 0) / 100) AS GiaTriTrietKhauThucChay ,
					IIF(dm.LoaiXuLy = 2, 0, ISNULL( tchdct.SoLuongThucTreo, 0) * ISNULL(tchdct.DonGia, 0) * (1 - ISNULL(hdct.ChietKhau, 0) / 100)) AS ThanhTienSauTrietKhauThucChay ,
					IIF(dm.LoaiXuLy = 2, 0, ISNULL( tchdct.SoLuongThucTreo, 0) * ISNULL(tchdct.DonGia, 0) * (1 - ISNULL(hdct.ChietKhau, 0) / 100) * ISNULL(hdct.TiLeTuVan, 0)/100) AS GiaTriHoaHongThucChay ,
					IIF(dm.LoaiXuLy = 2, 0, ISNULL( tchdct.SoLuongThucTreo, 0) * ISNULL(tchdct.DonGia, 0) * (1 - ISNULL(hdct.ChietKhau, 0) / 100) * (1 - ISNULL(hdct.TiLeTuVan, 0)/100)) AS ThanhTienThucThu ,
					IIF(dm.LoaiXuLy = 2, 0, IIF( hdct.IsKhuyenMai = 1 OR hdct.ChietKhau = 100 , ISNULL( tchdct.SoLuongThucTreo, 0) * ISNULL(tchdct.DonGia, 0), 0)) AS ThanhTienKM ,
					IIF(dm.LoaiXuLy = 2, 0, IIF( hdct.IsKhuyenMai = 1 OR hdct.ChietKhau = 100 , ISNULL( tchdct.SoLuongThucTreo, 0), 0)) AS SoLuongThucChayKM ,
					0 SoLuongLechTreoHa ,
					0 ThanhTienLechTreoHa ,
					GETDATE() ,
					GETDATE() ,
					0 IsPheDuyet ,
					'' PheDuyetBy ,
					'' PheDuyetAt ,
					IIF(dm.LoaiXuLy = 2, IIF(hdct.IsKhuyenMai = 0, ISNULL(tchdct.SoLuongThucTreo, 0), 0), 0) SoLuongThayDoi ,
					IIF(dm.LoaiXuLy = 2, IIF( hdct.IsKhuyenMai = 1 OR hdct.ChietKhau = 100 , ISNULL( tchdct.SoLuongThucTreo, 0), 0), 0) SoLuongKMThayDoi ,
					IIF(dm.LoaiXuLy = 2, IIF( hdct.IsKhuyenMai = 1 OR hdct.ChietKhau = 100 , ISNULL( tchdct.SoLuongThucTreo, 0) * ISNULL(tchdct.DonGia, 0), 0), 0) GiaTriKMThayDoi ,
					IIF(dm.LoaiXuLy = 2, N'Tính lại: ', N'Tính mới: ') + N'SP tối ưu [dbo].[ThucChay_ChiPhiKhac] do ' + dm.LyDo
			FROM  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
			INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
			INNER JOIN #DmThayDoi dm ON dm.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			INNER JOIN ABM_Data_ThucChay.dbo.DmSanPham sp ON sp.DmSanPhamID = hdct.DmSanPhamREF
			WHERE   dm.LoaiXuLy IN (2,3) AND 
			        tchdct.SoLuongThucTreo*tchdct.DonGia <> 0

                             	
			UPDATE  tchdct
            SET     tchdct.RecordStatus = 1
			FROM  ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
			INNER JOIN #DmThayDoi dm ON dm.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND dm.LoaiXuLy IN (2,3)
		END

		DROP TABLE #DmThayDoi
	END


```
