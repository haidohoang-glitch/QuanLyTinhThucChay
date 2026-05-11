# Stored Procedure: `ThucChay_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-02-06 16:44:38.960000
- **Ngày sửa cuối**: 2025-12-31 14:46:26.323000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |
| `@NgayCheckThayDoi` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql



--EXEC [dbo].[ThucChay_ChiPhiKhac] @NgayGhiNhan = '2025-07-11', @NgayCheckThayDoi = '2025-07-11'

CREATE PROCEDURE [dbo].[ThucChay_ChiPhiKhac]
    @NgayGhiNhan DATE,
    @NgayCheckThayDoi  DATE = NULL,
	@NgayDanhSoGioiHan DATE = NULL,
	@SoHopDong NVARCHAR(100) = NULL,
	@HopDongChiTietID INT = NULL
AS
	DECLARE @NgayDanhSoGioiHan_PB_MKT DATETIME = '2025-07-05',
	@NgayDanhSoGioiHan_Admatic_MKT DATETIME = '2025-10-10'

    BEGIN
		IF @SoHopDong IS NOT NULL 
		BEGIN
			SET @NgayCheckThayDoi = NULL
			SET @NgayDanhSoGioiHan = NULL
		END

		CREATE TABLE #DmPBThayDoi 
		( HopDongChiTietID INT,
		  LoaiThayDoi INT,
		  LyDo NVARCHAR(MAX),
		  LoaiXuLy INT -- 1: đối trừ, 2: đối từ tính lại
		)

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
                AND DotChayHopDong LIKE N'ThucChay_ChiPhi'
				AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
				AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)
        --=================================================== 1: Xác định danh mục ID cần đối trừ hoặc ghi nhận thêm ====================================
		/*
		- 1. phân bổ, hợp đồng hủy: đối trừ phân bổ
		- 2. treo thay đổi giá trị, treo gỡ phân bổ, đổi phân bổ, treo hủy, phân bổ thay đổi giá trị: đối trừ tính lại cho phân bổ
		- 3. treo mới: ghi nhân cho phân bổ mới
		*/
		BEGIN
			INSERT INTO #DmPBThayDoi
			(	  HopDongChiTietID ,
				  LoaiThayDoi,
				  LyDo ,
				  LoaiXuLy 
			)
			SELECT  DISTINCT
					hdct.HopDongChiTietID ,
					LoaiThayDoi = 1,
					LyDo =	N' hợp đồng/ phân bổ xóa, hủy',
					LoaiXuLy = 1
			FROM  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		    WHERE  (
					((hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1) AND 
						CONVERT(DATE, ISNULL(hd.LastModifiedAt, hd.CreatedAt))  = @NgayCheckThayDoi) OR
					(hdct.DeletedStatus = 1 AND 
						CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi) 
					)

				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND NOT (hdct.DmViTriREF in (100093,100478))
				   AND (EXISTS( SELECT TOP (1) ch.ID 
							    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
								AND ch.DeletedStatus = 0 ORDER BY ch.ID
					   ))
			       AND hdct.DmSanPhamREF <> 5184
				   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  hd.NgayDanhSoHopDong >= '2022-01-01')
				   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				   AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
				   ----HAIDH COMMENT 20250917 THEM DIEU KIEN LOAI Admatic - Marketing fee
				   --AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT
							--					AND (hdct.DmLoaiNenTangREF <> 9 OR hdct.DmLoaiNenTangREF IS NULL)) --Marketing fee – Admatic
				   ------HAIDH COMMENT 20251204 LOAI  Admatic - Marketing fee - NEN TANG = 9
				   AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817  --AND hdct.DmLoaiNenTangREF = 9
				   ) --Marketing fee – Admatic - nen tang = 9

				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																		WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																		order by hdv.HopDongChiTietREF)

			INSERT INTO #DmPBThayDoi
			(	  HopDongChiTietID ,
				  LoaiThayDoi,
				  LyDo ,
				  LoaiXuLy 
			)
			SELECT  DISTINCT
					l.HopDongChiTietREF ,   -- phân bổ cũ
					LoaiThayDoi = 2,
					LyDo =	N' phân bổ có ID treo đổi phân bổ',
					LoaiXuLy = 2
			FROM  ( SELECT * 
					FROM  ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
					WHERE  tchdct.RecordStatus = 1 AND --tchdct.HopDongChiTietREF =  0  AND 
						   CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi ) tchdct 
			OUTER APPLY (SELECT TOP 1 l.HopDongChiTietREF
			             FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietLog l
						 WHERE l.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND
						       CONVERT(DATE, ISNULL(l.LastModifiedAt, l.CreatedAt)) < @NgayCheckThayDoi
						 ORDER BY CONVERT(DATE, ISNULL(l.LastModifiedAt, l.CreatedAt)) DESC) l
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON l.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE  tchdct.HopDongChiTietREF <> l.HopDongChiTietREF
				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND NOT (hdct.DmViTriREF in (100093,100478))
				   AND (EXISTS( SELECT TOP (1) ch.ID 
							    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
								AND ch.DeletedStatus = 0 ORDER BY ch.ID
					   ))
				   AND hdct.DmSanPhamREF <> 5184
				   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  hd.NgayDanhSoHopDong >= '2022-01-01')
				   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				   AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
				   ----HAIDH COMMENT 20250917 THEM DIEU KIEN LOAI Admatic - Marketing fee
				   --AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT
							--					AND (hdct.DmLoaiNenTangREF <> 9 OR hdct.DmLoaiNenTangREF IS NULL)) --Marketing fee – Admatic
				   ------HAIDH COMMENT 20251204 LOAI  Admatic - Marketing fee - NEN TANG = 9
				   AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817  --AND hdct.DmLoaiNenTangREF = 9
				   ) --Marketing fee – Admatic - nen tang = 9

				   AND CONVERT(DATE, tchdct.ThoiGianBatDau) >= '2010-01-01'

				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																		WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																		order by hdv.HopDongChiTietREF)
				   AND hdct.DeletedStatus = 0 AND hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN (0,3)

			INSERT INTO #DmPBThayDoi
			(	  HopDongChiTietID ,
				  LoaiThayDoi,
				  LyDo ,
				  LoaiXuLy 
			)
			SELECT  DISTINCT
					tchdct.HopDongChiTietREF ,  -- phân bổ mới
					LoaiThayDoi = 2,
					LyDo =	N' phân bổ có ID treo đổi phân bổ',
					LoaiXuLy = 2
			FROM  ( SELECT * 
					FROM  ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
					WHERE  tchdct.RecordStatus = 1 AND --tchdct.HopDongChiTietREF =  0  AND 
						   CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi ) tchdct 
			OUTER APPLY (SELECT TOP 1 l.HopDongChiTietREF
			             FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietLog l
						 WHERE l.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND
						       CONVERT(DATE, ISNULL(l.LastModifiedAt, l.CreatedAt)) < @NgayCheckThayDoi
						 ORDER BY CONVERT(DATE, ISNULL(l.LastModifiedAt, l.CreatedAt)) DESC) l
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE  tchdct.HopDongChiTietREF <> l.HopDongChiTietREF
				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND NOT (hdct.DmViTriREF in (100093,100478))
				   AND (EXISTS( SELECT TOP (1) ch.ID 
							    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
								AND ch.DeletedStatus = 0 ORDER BY ch.ID
					   ))
				   AND hdct.DmSanPhamREF <> 5184
				   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  hd.NgayDanhSoHopDong >= '2022-01-01')
				   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				   AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
   				--   ----HAIDH COMMENT 20250917 THEM DIEU KIEN LOAI Admatic - Marketing fee
				   --AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT
							--					AND (hdct.DmLoaiNenTangREF <> 9 OR hdct.DmLoaiNenTangREF IS NULL)) --Marketing fee – Admatic
				   ------HAIDH COMMENT 20251204 LOAI  Admatic - Marketing fee - NEN TANG = 9
				   AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817  --AND hdct.DmLoaiNenTangREF = 9
				   ) --Marketing fee – Admatic - nen tang = 9

				   AND CONVERT(DATE, tchdct.ThoiGianBatDau) >= '2010-01-01'

				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																		WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																		order by hdv.HopDongChiTietREF)
				   AND tchdct.HopDongChiTietREF NOT IN (SELECT HopDongChiTietID FROM #DmPBThayDoi)
				   AND hdct.DeletedStatus = 0 AND hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN (0,3)


			INSERT INTO #DmPBThayDoi
			(	  HopDongChiTietID ,
				  LoaiThayDoi,
				  LyDo ,
				  LoaiXuLy 
			)
			SELECT  DISTINCT
					hdct.HopDongChiTietID ,
					LoaiThayDoi = 3,
					LyDo =	N' phân bổ có ID treo hủy hoặc đổi trạng thái duyêt',
					LoaiXuLy = 2
			FROM  ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
			WHERE  tchdct.RecordStatus = 1 
				   AND ((tchdct.DeletedStatus = 1 OR tchdct.TrangThaiTreo <> 2) AND 
						 CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi)
				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND NOT (hdct.DmViTriREF in (100093,100478))
				   AND (EXISTS( SELECT TOP (1) ch.ID 
							    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
								AND ch.DeletedStatus = 0 ORDER BY ch.ID
					   ))
			       AND hdct.DmSanPhamREF <> 5184
				   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  hd.NgayDanhSoHopDong >= '2022-01-01')
				   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				   AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
				   ------HAIDH COMMENT 20250917 THEM DIEU KIEN LOAI Admatic - Marketing fee
				   --AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT
							--					AND (hdct.DmLoaiNenTangREF <> 9 OR hdct.DmLoaiNenTangREF IS NULL)) --Marketing fee – Admatic
					------HAIDH COMMENT 20251204 LOAI  Admatic - Marketing fee - NEN TANG = 9
				   AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817  --AND hdct.DmLoaiNenTangREF = 9
				   ) --Marketing fee – Admatic - nen tang = 9


				   AND CONVERT(DATE, tchdct.ThoiGianBatDau) >= '2010-01-01'

				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																		WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																		order by hdv.HopDongChiTietREF)
				   AND hdct.HopDongChiTietID NOT IN (SELECT HopDongChiTietID FROM #DmPBThayDoi)

			INSERT INTO #DmPBThayDoi
			(	  HopDongChiTietID ,
				  LoaiThayDoi,
				  LyDo ,
				  LoaiXuLy 
			)
			SELECT  DISTINCT
					hdct.HopDongChiTietID ,
					LoaiThayDoi = 4,
					LyDo =	N' phân bổ thay đổi giá trị',
					LoaiXuLy = 2
			FROM  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		    WHERE  CONVERT(DATE, ISNULL(hdct.LastModifiedAt, hdct.CreatedAt)) = @NgayCheckThayDoi 
				   AND hd.TrangThaiHopDong NOT IN (0,3) AND hd.DeletedStatus = 0 AND hdct.DeletedStatus = 0 
				   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				   AND NOT (hdct.DmViTriREF in (100093,100478))
				   AND (EXISTS( SELECT TOP (1) ch.ID 
							    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
								WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
								AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
								AND ch.DeletedStatus = 0 ORDER BY ch.ID
					   ))
			       AND hdct.DmSanPhamREF <> 5184
				   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  hd.NgayDanhSoHopDong >= '2022-01-01')
				   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				   AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
				   ------HAIDH COMMENT 20250917 THEM DIEU KIEN LOAI Admatic - Marketing fee
				   --AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT
							--					AND (hdct.DmLoaiNenTangREF <> 9 OR hdct.DmLoaiNenTangREF IS NULL)) --Marketing fee – Admatic
				   ------HAIDH COMMENT 20251204 LOAI  Admatic - Marketing fee - NEN TANG = 9
				   AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817  --AND hdct.DmLoaiNenTangREF = 9
				   ) --Marketing fee – Admatic - nen tang = 9

				   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																		WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																		order by hdv.HopDongChiTietREF)
				   AND hdct.HopDongChiTietID NOT IN (SELECT HopDongChiTietID FROM #DmPBThayDoi)

			DELETE dm
			FROM #DmPBThayDoi dm
			INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
			OUTER APPLY (SELECT TOP 1 ThanhTienKhuyenMaiPhanBo = IIF(l.ChietKhau = 100,l.SoLuong*l.DonGia, 0), 
									  ThanhTienSauCKPhanBo = l.SoLuong*l.DonGia*(1-l.ChietKhau/100)
						 FROM ABM_Data_ThucChay.dbo.HopDongChiTietLog l
						 WHERE l.HopDongChiTietREF = hdct.HopDongChiTietID AND
                               CAST(l.LastModifiedAt AS DATE) < @NgayCheckThayDoi
						 ORDER BY l.LastModifiedAt desc) l 
			WHERE  ROUND(IIF(hdct.ChietKhau = 100,hdct.SoLuong*hdct.DonGia, 0) - ISNULL(l.ThanhTienKhuyenMaiPhanBo, 0), 0) = 0 AND 
				   ROUND(hdct.SoLuong*hdct.DonGia*(1-hdct.ChietKhau/100) - ISNULL(l.ThanhTienSauCKPhanBo, 0), 0) = 0 	AND
				   LoaiThayDoi = 4

			INSERT INTO #DmPBThayDoi
			(	  HopDongChiTietID ,
				  LoaiThayDoi,
				  LyDo ,
				  LoaiXuLy 
			)
			SELECT DISTINCT
					tchdct.HopDongChiTietREF,
					LoaiThayDoi = 5,
					LyDo = N' thực treo có thay đổi giá trị',
					LoaiXuLy = 2
			FROM (  SELECT tchdct.HopDongChiTietREF, 
						   tchdct.ThucChayHopDongChiTietID,
						   ThanhTienKhuyenMaiTreo = IIF(tchdct.ChietKhau = 100,tchdct.SoLuongThucTreo*tchdct.DonGia, 0),
						   ThanhTienSauCKTreo =  tchdct.SoLuongThucTreo*tchdct.DonGia*(1-tchdct.ChietKhau/100)
					FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
					INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
					INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
					WHERE  CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi
						   AND tchdct.RecordStatus = 1 AND tchdct.TrangThaiTreo = 2
						   AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
						   AND NOT (hdct.DmViTriREF in (100093,100478))
						   AND (EXISTS( SELECT TOP (1) ch.ID 
										FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
										WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
										AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
										AND ch.DeletedStatus = 0 ORDER BY ch.ID
							   ))
						   AND hdct.DmSanPhamREF <> 5184
						   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  hd.NgayDanhSoHopDong >= '2022-01-01')
						   AND hdct.DeletedStatus = 0
						   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																				WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																				order by hdv.HopDongChiTietREF)

						   AND (hd.TrangThaiHopDong <> 3 OR hd.DeletedStatus = 0)
						   AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
						   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
						   AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
						   ----HAIDH COMMENT 20250917 THEM DIEU KIEN LOAI Admatic - Marketing fee
						   --AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT
									--			AND (hdct.DmLoaiNenTangREF <> 9 OR hdct.DmLoaiNenTangREF IS NULL)) --Marketing fee – Admatic
						   AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817  --AND hdct.DmLoaiNenTangREF = 9
							) --Marketing fee – Admatic - nen tang = 9

						   AND CONVERT(DATE, tchdct.ThoiGianBatDau) >= '2010-01-01'
						   AND tchdct.TrangThaiTreo = 2

						   AND hdct.HopDongChiTietID NOT IN (SELECT HopDongChiTietID FROM #DmPBThayDoi)
					) tchdct
			OUTER APPLY (SELECT TOP 1 ThanhTienKhuyenMaiTreo = IIF(l.ChietKhau = 100,l.SoLuongThucTreo*l.DonGia, 0),
									  ThanhTienSauCKTreo =  l.SoLuongThucTreo*l.DonGia*(1-l.ChietKhau/100)
						 FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietLog l
						 WHERE l.ThucChayHopDongChiTietID = tchdct.ThucChayHopDongChiTietID AND
                               CAST(l.LastModifiedAt AS DATE) < @NgayCheckThayDoi
						 ORDER BY l.LastModifiedAt desc) l
			WHERE  ROUND(tchdct.ThanhTienKhuyenMaiTreo - ISNULL(l.ThanhTienKhuyenMaiTreo, 0), 0) <> 0 or 
				   ROUND(tchdct.ThanhTienSauCKTreo - ISNULL(l.ThanhTienSauCKTreo, 0), 0) <> 0  


			--
			IF @SoHopDong IS NOT NULL 
			BEGIN
				INSERT INTO #DmPBThayDoi
				(		HopDongChiTietID ,
						LoaiThayDoi,
						LyDo ,
						LoaiXuLy 
				)				
				SELECT DISTINCT
					    hdct.HopDongChiTietID,
						LoaiThayDoi = 6,
						LyDo = N' xử lý tay phân bổ',
						LoaiXuLy = 2
				FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
				INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
				WHERE  NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
					   AND NOT (hdct.DmViTriREF in (100093,100478))
					   AND (EXISTS( SELECT TOP (1) ch.ID 
									FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
									WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
									AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
									AND ch.DeletedStatus = 0 ORDER BY ch.ID
						   ))
					   AND hdct.DmSanPhamREF <> 5184
					   AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  hd.NgayDanhSoHopDong >= '2022-01-01')
					   AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																			WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																			order by hdv.HopDongChiTietREF)
					   AND hd.SoHopDong = @SoHopDong

					   AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
					   ----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
					   AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
					   ----HAIDH COMMENT 20250917 THEM DIEU KIEN LOAI Admatic - Marketing fee
					   --AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT
								--				AND (hdct.DmLoaiNenTangREF <> 9 OR hdct.DmLoaiNenTangREF IS NULL)) --Marketing fee – Admatic
					   AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817  --AND hdct.DmLoaiNenTangREF = 9
					   ) --Marketing fee – Admatic - nen tang = 9

			END
		END
		--=================================================== 2: Xác định danh mục các treo cần xử lý ===========
		INSERT INTO #DmThayDoi
		(
					ThucChayHopDongChiTietID,
					HopDongChiTietID,
					HopDongREF,
					NgayThucHien,
					RecordStatus,
					LastModifiedAt,
					ThanhTienKhuyenMaiTreo,
					ThanhTienSauCKTreo,
					ThanhTienKhuyenMaiPhanBo,
					ThanhTienSauCKPhanBo,
					LoaiThayDoi,
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
				dm.LoaiThayDoi,
				LyDo = IIF(tchdct.RecordStatus = 0 , N' duyệt lại ID treo chưa được ghi nhận do', N' tính lại ID treo do') + dm.LyDo
		FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
		INNER JOIN  ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietID = tchdct.HopDongChiTietREF
		WHERE   CONVERT(DATE, tchdct.ThoiGianBatDau) >= '2010-01-01'
				AND CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) <= @NgayCheckThayDoi 
				AND tchdct.DeletedStatus = 0 AND tchdct.TrangThaiTreo = 2
				AND dm.LoaiXuLy = 2
		UNION
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
				loaithaydoi = 7,
				LyDo = N' ID treo duyệt mới'
		FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
		INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE   CONVERT(DATE, ISNULL(tchdct.LastModifiedAt, tchdct.CreatedAt)) = @NgayCheckThayDoi
		        AND tchdct.RecordStatus = 0 AND tchdct.DeletedStatus = 0 AND tchdct.TrangThaiTreo = 2

                AND NOT ( hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18 )
				AND NOT (hdct.DmViTriREF in (100093,100478))
				AND (EXISTS( SELECT TOP (1) ch.ID 
							FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay ch 
							WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
							AND ch.NhomTinhDoanhSoThucChay = 1 --Nhom Tinh chi phi
							AND ch.DeletedStatus = 0 ORDER BY ch.ID
					))
				AND hdct.DmSanPhamREF <> 5184
				AND NOT ((hdct.DmSanPhamREF = 5188  OR hdct.DmViTriREF = 100774) AND  hd.NgayDanhSoHopDong >= '2022-01-01')
				AND hdct.DeletedStatus = 0
				AND  NOT EXISTS(SELECT TOP (1) hdv.HopDongChiTietREF FROM ABM_Data_ThucChay.dbo.DmThongTinHopDongBanInventory hdv 
																	WHERE hdv.HopDongChiTietREF = hdct.HopDongChiTietID 
																	order by hdv.HopDongChiTietREF)

				AND (hd.TrangThaiHopDong <> 3 OR hd.DeletedStatus = 0)
				AND (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan)
				----HAIDH COMMENT 20250627 THEM DIEU KIEN LOAI Performance Base - Marketing fee
				AND NOT (hdct.DmLoaiREF = 5038 AND hdct.DmSanPhamREF = 817  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_PB_MKT) --Marketing fee – PB
				----HAIDH COMMENT 20250917 THEM DIEU KIEN LOAI Admatic - Marketing fee
				--AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817 AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_Admatic_MKT
				--								AND (hdct.DmLoaiNenTangREF <> 9 OR hdct.DmLoaiNenTangREF IS NULL)) --Marketing fee – Admatic
				AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmSanPhamREF = 817  --AND hdct.DmLoaiNenTangREF = 9
				   ) --Marketing fee – Admatic - nen tang = 9
				AND CONVERT(DATE, tchdct.ThoiGianBatDau) >= '2010-01-01'

				AND hdct.HopDongChiTietID NOT IN (SELECT HopDongChiTietID FROM #DmPBThayDoi)

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
		WHERE dm.LoaiThayDoi = 7

		UPDATE dm
		SET dm.ThanhTienKhuyenMaiDaTinh = 0,
			dm.ThanhTienSauCKDaTinh = 0
		FROM #DmThayDoi dm
		WHERE dm.LoaiThayDoi <> 7

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
					ROW_NUMBER() OVER (PARTITION BY HopDongChiTietID ORDER BY SIGN(ThanhTienKhuyenMaiTreo+ ThanhTienSauCKTreo) ASC, LastModifiedAt ASC, ThucChayHopDongChiTietID ASC) AS RowNum
				FROM #DmThayDoi
				),

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
					TichLuyThanhTienKM = IIF (ROUND(ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo - ThanhTienKhuyenMaiPhanBo, 0) > 0,
					                          ThanhTienKhuyenMaiDaTinh, 
											  ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo ), 
					TichLuyThanhTienSauCK = IIF (ROUND(ThanhTienSauCKDaTinh + ThanhTienSauCKTreo - ThanhTienSauCKPhanBo, 0) > 0,
												 ThanhTienSauCKDaTinh, 
												 ThanhTienSauCKDaTinh + ThanhTienSauCKTreo ),
					GhiNhanKM = IIF(ROUND(ThanhTienKhuyenMaiDaTinh + ThanhTienKhuyenMaiTreo - ThanhTienKhuyenMaiPhanBo, 0) > 0,
					                0, ThanhTienKhuyenMaiTreo ),
					GhiNhanThanhTienSauCK = IIF (ROUND(ThanhTienSauCKDaTinh + ThanhTienSauCKTreo - ThanhTienSauCKPhanBo, 0) > 0,
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
					TichLuyThanhTienKM = IIF (ROUND(r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo - b.ThanhTienKhuyenMaiPhanBo, 0)>0,
					                          r.TichLuyThanhTienKM, 
											  r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo ), 
					TichLuyThanhTienSauCK = IIF (ROUND(r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo - b.ThanhTienSauCKPhanBo, 0)>0,
												 r.TichLuyThanhTienSauCK, 
												 r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo ),
					GhiNhanKM =	IIF (ROUND(r.TichLuyThanhTienKM + b.ThanhTienKhuyenMaiTreo - b.ThanhTienKhuyenMaiPhanBo, 0) > 0,
									 0, b.ThanhTienKhuyenMaiTreo ),
					GhiNhanThanhTienSauCK = IIF (ROUND(r.TichLuyThanhTienSauCK + b.ThanhTienSauCKTreo - b.ThanhTienSauCKPhanBo, 0) > 0,
												 0, b.ThanhTienSauCKTreo )
				FROM CTE_Base b 
				INNER JOIN CTE_Recursive r  ON r.HopDongChiTietID = b.HopDongChiTietID AND r.RowNum = b.RowNum - 1
			)

			UPDATE dm
			SET dm.LoaiXuLy = CASE WHEN ISNULL(cte.GhiNhanKM, 0) = 0  AND ISNULL(cte.GhiNhanThanhTienSauCK, 0) = 0
										AND dm.RecordStatus = 1 
								   THEN 1  -- đối trừ
								   WHEN ISNULL(cte.GhiNhanKM, 0) = 0  AND ISNULL(cte.GhiNhanThanhTienSauCK, 0) = 0
										AND dm.RecordStatus = 0 
								   THEN 0  -- không xử lý
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 1 
								   THEN 2  -- đối trừ tính lại
								   WHEN(ISNULL(cte.GhiNhanKM, 0) <> 0  OR ISNULL(cte.GhiNhanThanhTienSauCK, 0) <> 0) 
										AND dm.RecordStatus = 0 
								   THEN 3  -- ghi nhận mới
								   ELSE 0
							  END
			FROM #DmThayDoi dm
			INNER JOIN CTE_Recursive cte ON cte.ThucChayHopDongChiTietID = dm.ThucChayHopDongChiTietID
			OPTION (MAXRECURSION 0);

			END 
		--=================================================== 2: Đối trừ thực chạy =============================================
		DECLARE @InsertedIDs TABLE (IDTreo NVARCHAR(100));

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
			OUTPUT INSERTED.DotChayBooking INTO @InsertedIDs
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
					,N'ThucChay_ChiPhi'
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
					, @NgayGhiNhan
			FROM ABM_Data_ThucChay.dbo.[ThucChayDaTinh] tcdt
			INNER JOIN #DmPBThayDoi dm ON dm.HopDongChiTietID = tcdt.HopDongChiTietREF
			WHERE		tcdt.NgayThucHien < @NgayGhiNhan
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
			HAVING SUM(tcdt.[ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) <> 0
				   OR SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) <> 0

			UPDATE  tchdct
            SET     tchdct.RecordStatus = 0
			FROM  ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
			JOIN @InsertedIDs I ON I.IDTreo = CAST(tchdct.ThucChayHopDongChiTietID AS NVARCHAR(100))

			INSERT INTO ABM_Data_ThucChay.dbo.thucchaydatinh_log
			SELECT *
			FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
			WHERE NgayThucHien = @NgayGhiNhan AND
				  DotChayBooking IN (SELECT IDTreo FROM @InsertedIDs) AND 
				  DotChayHopDong = 'ThucChay_ChiPhi'
		END

		DELETE
		FROM @InsertedIDs
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
			OUTPUT INSERTED.DotChayBooking INTO @InsertedIDs
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
					N'ThucChay_ChiPhi' DotChayHopDong ,
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
			INNER JOIN @InsertedIDs I ON I.IDTreo = CAST(tchdct.ThucChayHopDongChiTietID AS NVARCHAR(100))


			INSERT INTO ABM_Data_ThucChay.dbo.thucchaydatinh_log
			SELECT *
			FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
			WHERE NgayThucHien = @NgayGhiNhan AND
				  DotChayBooking IN (SELECT IDTreo FROM @InsertedIDs) AND 
				  DotChayHopDong = 'ThucChay_ChiPhi'

		END

		DROP TABLE #DmThayDoi
	END


```
