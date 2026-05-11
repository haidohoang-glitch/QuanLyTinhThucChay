# Stored Procedure: `ThucChay_CPM_Update_HopDongChiTietAndBanner_bk_07032025`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-07 17:04:29.093000
- **Ngày sửa cuối**: 2025-03-07 17:04:29.093000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@EndDate` | `datetime(8)` | No |
| `@NgayDanhSoGioiHan` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--CREATE TYPE DmInterger AS TABLE  ( ID INT)
create PROCEDURE [dbo].[ThucChay_CPM_Update_HopDongChiTietAndBanner_bk_07032025]
	@EndDate DATETIME,
	@NgayDanhSoGioiHan DATETIME
AS
BEGIN

	CREATE TABLE #ThucChayHopDongChitietTemp
	(	 ThucChayHopDongChiTietID int, 
		 BookingREF int,
		 DmBannerREF int,
		 HopDongREF int,
		 HopDongChiTietREF int, 
		 DmNhanHangREF int,
		 ThoiGianBatDau DATETIME,
		 ThoiGianKetThuc DATETIME, 
		 CreatedBy NVARCHAR(50), 
		 CreatedAt DATETIME, 
		 LastModifiedBy NVARCHAR(50), 
		 LastModifiedAt DATETIME, 
		 DeletedStatus int
	)

	CREATE TABLE #PhanBoThayDoiSoLuong
	(   HopDongChiTietID INT)

	--===================================== 1. Xác định bản ghi thucchayhopdongchitiet thay đổi =====================================================================
	INSERT INTO #ThucChayHopDongChitietTemp
	SELECT  ThucChayHopDongChiTietID , BookingREF,
			tc.DmBannerREF,HopDongREF,HopDongChiTietREF, tc.DmNhanHangREF,tc.ThoiGianBatDau,tc.ThoiGianKetThuc, 
			tc.CreatedBy, tc.CreatedAt, tc.LastModifiedBy, tc.LastModifiedAt, tc.DeletedStatus 
	FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tc
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = tc.HopDongREF
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tc.HopDongChiTietREF
	WHERE HopDongChiTietREF >0 
		  AND HopDongREF > 0
		  AND tc.DmBannerREF is not null 
		  AND tc.DmBannerREF <> ''
		  AND HopDongChiTietREF NOT IN (SELECT HopDongChiTietID FROM ABM_Data_ThucChay.dbo.HopDongChiTiet 
										WHERE (TenLoaiNenTang LIKE '%Retargeting%' OR DmLoaiBannerREF = 17 OR DmLoaiNenTangREF = 8 )
											  AND DeletedStatus <> 1)
		  AND ( CASE WHEN tc.LastModifiedAt >= tc.CreatedAt THEN Convert(date,tc.LastModifiedAt)
						ELSE Convert(date,tc.CreatedAt)
						END
				  )  >= convert(date, @EndDate)
		  AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan
		  AND hd.TrangThaiHopDong <> 3
		  AND hdct.DeletedStatus = 0
			
		

	--==================================== 2. Thực hiện merge data thucchayhopdongchitiet thêm mới hoặc thay đổi ===================================================================
	MERGE INTO ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner AS target
	USING #ThucChayHopDongChitietTemp AS source
	ON  target.HopDongREF = source.HopDongREF
		AND target.HopDongChiTietREF = source.HopDongChiTietREF
		AND target.DmBannerID = source.DmBannerREF
		AND target.ThucChayHopDongChiTietID = source.ThucChayHopDongChiTietID
	WHEN MATCHED THEN 
	UPDATE SET	    target.ThoiGianBatDau = source.ThoiGianBatDau,
					target.ThoiGianKetThuc = source.ThoiGianKetThuc,
					target.CreatedBy = source.CreatedBy,
					target.CreatedAt = source.CreatedAt,
					target.LastModifiedBy = source.LastModifiedBy,
					target.LastModifiedAt = source.LastModifiedAt,
					target.DeletedStatus = source.DeletedStatus,
					target.DsNhanHangREF = source.DmNhanHangREF,
					target.TiLeThucChayHDCTSoVoiBanner = IIF(source.DeletedStatus = 1, 0, target.TiLeThucChayHDCTSoVoiBanner),
					target.DaThucHienUpdateTiLe = IIF(source.DeletedStatus = 1, 1, target.DaThucHienUpdateTiLe)
	WHEN NOT MATCHED BY TARGET THEN 
	INSERT (        ThucChayHopDongChiTietID ,
					DmBannerID ,
					HopDongChiTietREF ,
					HopDongREF ,
					BookingREF ,
					ThoiGianBatDau ,
					ThoiGianKetThuc ,
					TiLeThucChayHDCTSoVoiBanner ,
					DaThucHienUpdateTiLe ,
					CreatedBy ,
					CreatedAt ,
					LastModifiedBy ,
					LastModifiedAt ,
					DeletedStatus ,
					DsNhanHangREF,
					LogTime) 
		VALUES (    source.ThucChayHopDongChiTietID,
					source.DmBannerREF,
					source.HopDongChiTietREF,
					source.HopDongREF,
					source.BookingREF,
					source.ThoiGianBatDau,
					source.ThoiGianKetThuc, 
					0, 
					0,
					source.CreatedBy,
					source.CreatedAt,
					source.LastModifiedBy,
					source.LastModifiedAt,
					source.DeletedStatus,
					source.DmNhanHangREF, 
					GETDATE());

	--=================================== 3. Xác định phân bổ thay đổi số lượng làm ảnh hưởng đến SLHD của banner, từ đó làm ảnh đến tỉ lệ của phân bổ đó và các phân bổ trong cùng banner
	INSERT INTO #PhanBoThayDoiSoLuong
	(
	    HopDongChiTietID
	)
	SELECT DISTINCT hdct.HopDongChiTietID
    FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID
	WHERE (  hdct.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,680,735,5056) AND
		     (([dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1) OR hdct.DmSanPhamREF = 680) ) AND 
		  hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan AND
		  (  CAST(hdct.LastModifiedAt AS DATE) = @EndDate OR 
		     ((hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1) AND CAST(hd.LastModifiedAt AS DATE) = @EndDate)
		  )

	--=================================== 4. Xác định banner cần xử lý
	CREATE TABLE #DmBannerUpdate 
	(	DmBannerID NVARCHAR(200))
	INSERT INTO #DmBannerUpdate (DmBannerID)
	SELECT DISTINCT tchdctab.DmBannerID
	FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdctab
	INNER JOIN dbo.HopDongChiTiet hdct	ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd  ON hd.HopDongID = hdct.HopDongFK
	WHERE  (tchdctab.DaThucHienUpdateTiLe = 0 OR EXISTS (SELECT 1 FROM #PhanBoThayDoiSoLuong dm WHERE dm.HopDongChiTietID =  hdct.HopDongChiTietID ))
			AND tchdctab.DeletedStatus = 0
			AND hdct.DeletedStatus = 0 
			AND hd.TrangThaiHopDong <> 3 
			AND hd.DeletedStatus = 0
			AND hdct.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,680,735,5056)
			AND (([dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1) OR hdct.DmSanPhamREF = 680)  
	
			

	--================================== 5. thực hiện update
	;WITH CTE_Soluong_All_HD AS (
									SELECT  dm.DmBannerID, 
											ViewHD = SUM(CONVERT(BIGINT, ISNULL(IIF(hdct.DmSanPhamREF = 680, 0,hdct.SoLuong), 0)) * 1000),
											GoiHD = SUM(CONVERT(BIGINT, ISNULL(IIF(hdct.DmSanPhamREF = 680, hdct.SoLuong, 0), 0)) * 1000)
									FROM  #DmBannerUpdate dm
									INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdctab ON tchdctab.DmBannerID = dm.DmBannerID
									INNER JOIN (SELECT HopDongChiTietID,  hdct.SoLuong, hdct.DmSanPhamREF
									            FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
												INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
											    WHERE hdct.DeletedStatus = 0 AND 
												      hd.DeletedStatus = 0 AND
													  hd.TrangThaiHopDong <> 3 AND
													  hdct.DmSanPhamREF IN (231, 238, 339, 342, 337, 240, 370, 598, 613, 680, 735, 5056) AND
										             ([dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1 OR hdct.DmSanPhamREF = 680)) hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
									GROUP BY  dm.DmBannerID )

	UPDATE tchdctab
	SET TiLeThucChayHDCTSoVoiBanner = IIF(hdct.DmSanPhamREF = 680, 
										  IIF(ISNULL(cte.GoiHD, 0) <>0,(ROUND((Convert(FLOAT,hdct.SoLuong)*1000)/Convert(FLOAT,cte.GoiHD),5)*100), 100),
										  IIF(ISNULL(cte.ViewHD, 0) <>0,(ROUND((Convert(FLOAT,hdct.SoLuong)*1000)/Convert(FLOAT,cte.ViewHD),5)*100), 100)),
	    DaThucHienUpdateTiLe = 1
	FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner tchdctab
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN  CTE_Soluong_All_HD cte ON tchdctab.DmBannerID = cte.DmBannerID
	WHERE tchdctab.DeletedStatus = 0
		  AND hdct.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,680,735,5056)
		  AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <>1
		  AND (([dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1) OR hdct.DmSanPhamREF = 680)
	
	DROP TABLE #DmBannerUpdate
	DROP TABLE #ThucChayHopDongChitietTemp

END


```
