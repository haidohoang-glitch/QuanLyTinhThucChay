# Stored Procedure: `ThucChay_Admatic_Update_HopDongChiTietAndBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-10 17:06:14.890000
- **Ngày sửa cuối**: 2025-09-16 14:25:32.623000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |

## Definition (Source Code)

```sql

--EXEC [dbo].[ThucChay_Admatic_Update_HopDongChiTietAndBanner]
--			@NgayThucHien = '2025-04-15',
--			@NgayDanhSoGioiHan = '2022-04-15'

CREATE PROCEDURE [dbo].[ThucChay_Admatic_Update_HopDongChiTietAndBanner]
	@NgayThucHien DATE,
	@NgayDanhSoGioiHan DATE = NULL
AS
BEGIN
	DECLARE @NgayDanhSoGioiHan_MKT DATE = '2025-10-01'
	CREATE TABLE #ThucChayHopDongChiTietAndBanner_Admatic(
			[ThucChayHopDongChiTietID] [int] NULL,
			[DmBannerID] [nvarchar](50) NULL,
			[HopDongChiTietREF] [int] NULL,
			[HopDongREF] [int] NULL,
			[BookingREF] [int] NULL,
			[ThoiGianBatDau] [datetime] NULL,
			[ThoiGianKetThuc] [datetime] NULL,
			[CreatedBy] [nvarchar](50) NULL,
			[CreatedAt] [datetime] NULL,
			[LastModifiedBy] [nvarchar](50) NULL,
			[LastModifiedAt] [datetime] NULL,
			[DeletedStatus] [int] NULL,
			[DsNhanHangREF] [nvarchar](200) NULL,
			[DonGia_Banner] [int] NOT NULL,
			[DmHinhThucQuangCaoID] [int] NOT NULL,
			[DmSanPhamID] [int] NOT NULL,
			[DonViTinh] [nvarchar](50) NULL,
			[Status]  [int] NULL,
		) 
		
		--======================================1. Xác định dữ liệu cần merge ================================
		INSERT INTO #ThucChayHopDongChiTietAndBanner_Admatic
		        ( ThucChayHopDongChiTietID ,
		          DmBannerID ,
		          HopDongChiTietREF ,
		          HopDongREF ,
		          BookingREF ,
		          ThoiGianBatDau ,
		          ThoiGianKetThuc ,
		          CreatedBy ,
		          CreatedAt ,
		          LastModifiedBy ,
		          LastModifiedAt ,
		          DeletedStatus ,
		          DsNhanHangREF ,
		          DonGia_Banner ,
		          DmHinhThucQuangCaoID ,
		          DmSanPhamID ,
		          DonViTinh ,
		          Status
		        )
	
		SELECT  ThucChayHopDongChiTietID, 
				DmBannerREF = CONVERT(INT,DmBannerREF), 
				HopDongChiTietREF, 
				HopDongREF, 
				BookingREF, 
				ThoiGianBatDau, 
				ThoiGianKetThuc, 
				CreatedBy, 
				CreatedAt, 
				LastModifiedBy, 
				LastModifiedAt, 
				DeletedStatus, 
				DmNhanHangREF, 
				DonGiaBanner = ISNULL(dg.dongiabanner, 0), 
				DmHinhThucQuangCaoREF, 
				DmSanPhamREF,
				DonViTinh = dg.donvitinh,
			    [Status] = 0  
		FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
		OUTER APPLY (SELECT TOP 1 donvitinh = CASE WHEN LoaiDonGiaTheoDVT = 1 THEN N'CPC'
														WHEN LoaiDonGiaTheoDVT IN (2,3) THEN N'CPM'
														WHEN LoaiDonGiaTheoDVT IN (4) THEN N'TRUE VIEW'
														ELSE N''
												   END,
								  dongiabanner = DonGiaBanner_VAT/1.1 
					 FROM ABM_Data_ThucChay.dbo.AdmaticDonGiaBanner dg
					 WHERE dg.DmBannerID = tchdct.DmBannerREF
					 ORDER BY dg.CreatedAt DESC) dg
		WHERE DmHinhThucQuangCaoREF = 42
			  AND CONVERT(DATE,LastModifiedAt) >= @NgayThucHien

		--============================== 2. Thực hiện merge data thucchayhopdongchietiet vào bảng ThucChayHopDongChiTietAndBanner_Admatic và bảng ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic
		MERGE INTO ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Admatic AS TARGET
		USING #ThucChayHopDongChiTietAndBanner_Admatic AS SOURCE
		ON   TARGET.[ThucChayHopDongChiTietID] = SOURCE.ThucChayHopDongChiTietID
		WHEN MATCHED THEN 
		UPDATE SET	   TARGET.[DmBannerID] = SOURCE.DmBannerID
					  ,TARGET.[HopDongChiTietREF] = SOURCE.HopDongChiTietREF
					  ,TARGET.[HopDongREF] = SOURCE.HopDongREF
					  ,TARGET.[BookingREF] = SOURCE.BookingREF
					  ,TARGET.[ThoiGianBatDau] = SOURCE.ThoiGianBatDau
					  ,TARGET.[ThoiGianKetThuc] = SOURCE.ThoiGianKetThuc
					  ,TARGET.[CreatedBy] = SOURCE.CreatedBy
					  ,TARGET.[CreatedAt] = SOURCE.CreatedAt
					  ,TARGET.[LastModifiedBy] = SOURCE.LastModifiedBy
					  ,TARGET.[LastModifiedAt] = SOURCE.LastModifiedAt
					  ,TARGET.[DeletedStatus] = SOURCE.DeletedStatus
					  ,TARGET.[DsNhanHangREF] = SOURCE.DsNhanHangREF
					  ,TARGET.[DmHinhThucQuangCaoID] = SOURCE.DmHinhThucQuangCaoID
					  ,TARGET.[DmSanPhamID] = SOURCE.DmSanPhamID
					  ,TARGET.[DonViTinh] = SOURCE.DonViTinh
		WHEN NOT MATCHED BY TARGET THEN 
		INSERT (	  ThucChayHopDongChiTietID ,
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
					  DsNhanHangREF ,
					  DonGia_Banner ,
					  DmHinhThucQuangCaoID ,
					  DmSanPhamID,
					  DonViTinh )
		VALUES(		  SOURCE.ThucChayHopDongChiTietID ,
					  SOURCE.DmBannerID ,
					  SOURCE.HopDongChiTietREF ,
					  SOURCE.HopDongREF ,
					  SOURCE.BookingREF ,
					  SOURCE.ThoiGianBatDau ,
					  SOURCE.ThoiGianKetThuc ,
					  0 ,
					  0 ,
					  SOURCE.CreatedBy ,
					  SOURCE.CreatedAt ,
					  SOURCE.LastModifiedBy ,
					  SOURCE.LastModifiedAt ,
					  SOURCE.DeletedStatus ,
					  SOURCE.DsNhanHangREF ,
					  SOURCE.DonGia_Banner ,
					  SOURCE.DmHinhThucQuangCaoID ,
					  SOURCE.DmSanPhamID ,
					  SOURCE.DonViTinh ); 


		MERGE INTO ABM_Data_ThucChay.dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] AS TARGET
		USING #ThucChayHopDongChiTietAndBanner_Admatic AS SOURCE
		ON   TARGET.[ThucChayHopDongChiTietREF] = SOURCE.ThucChayHopDongChiTietID
		WHEN MATCHED THEN 
		UPDATE SET	   TARGET.[DmBannerREF] = SOURCE.DmBannerID
					  ,TARGET.[HopDongChiTietREF] = SOURCE.HopDongChiTietREF
					  ,TARGET.[HopDongREF] = SOURCE.HopDongREF
					  ,TARGET.[BookingREF] = SOURCE.BookingREF
					  ,TARGET.[ThoiGianBatDau] = SOURCE.ThoiGianBatDau
					  ,TARGET.[ThoiGianKetThuc] = SOURCE.ThoiGianKetThuc
					  ,TARGET.[TiLeThucChayHDCTSoVoiBanner] = 0 
					  ,TARGET.[DaThucHienUpdateTiLe] = 0 
					  ,TARGET.[CreatedBy] = SOURCE.CreatedBy
					  ,TARGET.[CreatedAt] = SOURCE.CreatedAt
					  ,TARGET.[LastModifiedBy] = SOURCE.LastModifiedBy
					  ,TARGET.[LastModifiedAt] = SOURCE.LastModifiedAt
					  ,TARGET.[DeletedStatus] = SOURCE.DeletedStatus
					  ,TARGET.[DsNhanHangREF] = SOURCE.DsNhanHangREF
					  ,TARGET.[DmHinhThucQuangCaoREF] = SOURCE.DmHinhThucQuangCaoID
					  ,TARGET.[DmSanPhamREF] = SOURCE.DmSanPhamID
		WHEN NOT MATCHED BY TARGET THEN 
		INSERT (	  ThucChayHopDongChiTietREF ,
					  DmBannerREF ,
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
					  DsNhanHangREF ,
					  DmHinhThucQuangCaoREF ,
					  DmSanPhamREF)
		VALUES(		  SOURCE.ThucChayHopDongChiTietID ,
					  SOURCE.DmBannerID ,
					  SOURCE.HopDongChiTietREF ,
					  SOURCE.HopDongREF ,
					  SOURCE.BookingREF ,
					  SOURCE.ThoiGianBatDau ,
					  SOURCE.ThoiGianKetThuc ,
					  0 ,
					  0 ,
					  SOURCE.CreatedBy ,
					  SOURCE.CreatedAt ,
					  SOURCE.LastModifiedBy ,
					  SOURCE.LastModifiedAt ,
					  SOURCE.DeletedStatus ,
					  SOURCE.DsNhanHangREF ,
					  SOURCE.DmHinhThucQuangCaoID ,
					  SOURCE.DmSanPhamID); 


	--================================================ 3. Update đơn giá với data không trong phạm vi data merge của lần ETL hiện tại nhưng chưa có thông tin đơn giá =========================================
	UPDATE tchdctab
	SET DonGia_Banner = ISNULL(dg.dongia,0)
	FROM ABM_Data_ThucChay.[dbo].[ThucChayHopDongChiTietAndBanner_Admatic] tchdctab
	OUTER APPLY (SELECT TOP 1 dongia = DonGiaBanner_VAT/1.1 
					FROM ABM_Data_ThucChay.dbo.AdmaticDonGiaBanner  dg
					WHERE dg.DmBannerID = tchdctab.DmBannerID
					ORDER BY CreatedAt DESC) dg
	WHERE tchdctab.DonGia_Banner = 0

	--=================================== 4. Xác định phân bổ thay đổi thành tiền HD làm ảnh hưởng đến tổng thành tiền HD của banner, từ đó làm ảnh đến tỉ lệ của phân bổ đó và các phân bổ trong cùng banner
	CREATE TABLE #PhanBoThayDoiThanhTien (HopDongChiTietID INT)
	INSERT INTO #PhanBoThayDoiThanhTien
	(
	    HopDongChiTietID
	)
	SELECT DISTINCT hdct.HopDongChiTietID
    FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID
	WHERE (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan) AND

		  NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13)) AND
		  hdct.DmLoaiREF = 42 AND 		  
		  (  CAST(hdct.LastModifiedAt AS DATE) = @NgayThucHien OR 
		     ((hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1) AND CAST(hd.LastModifiedAt AS DATE) = @NgayThucHien)
		  )

    --================================= 5. Xác định danh mục banner cần update tỉ lệ
	CREATE TABLE #DmBannerUpdate 
	(	DmBannerID NVARCHAR(200))
	INSERT INTO #DmBannerUpdate (DmBannerID)
	SELECT DISTINCT tchdctab.DmBannerREF
	FROM ABM_Data_ThucChay.dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] tchdctab
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct  ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong  hd ON hd.HopDongID = hdct.HopDongFK
	WHERE (tchdctab.DaThucHienUpdateTiLe = 0 OR EXISTS (SELECT 1 FROM #PhanBoThayDoiThanhTien dm WHERE dm.HopDongChiTietID =  hdct.HopDongChiTietID ))
	      AND tchdctab.DeletedStatus = 0
		  AND tchdctab.DmSanPhamREF <> 817 --HAIDH COMMENT 16/04/2025 loai tru viec tinh ti le cho san pham Marketing Fee vi no duoc treo cung banner voi phan bo chinh va duoc tinh la 100 tien thuc chay

	--==================================6. Thực hiện update tỉ lệ
	;WITH CTE_Soluong_All_HD AS (
									SELECT  dm.DmBannerID, 
									        TongGoi = SUM(ISNULL(hdct.SoLuong*hdct.DonGia, 0))
									FROM  #DmBannerUpdate dm
									INNER JOIN ABM_Data_ThucChay.dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] tchdctab ON tchdctab.DmBannerREF = dm.DmBannerID
									INNER JOIN (SELECT HopDongChiTietID,  hdct.SoLuong, hdct.DonGia
									            FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
												INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
											    WHERE hdct.DeletedStatus = 0 AND 
												      hd.DeletedStatus = 0 AND
													  hd.TrangThaiHopDong <> 3 AND
													  hdct.DmSanPhamREF <> 817 AND --HAIDH COMMENT 16/04/2025 loai tru viec tinh ti le cho san pham Marketing Fee vi no duoc treo cung banner voi phan bo chinh va duoc tinh la 100 tien thuc chay
													  hdct.DmLoaiREF = 42) hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
									WHERE tchdctab.DeletedStatus = 0
									GROUP BY  dm.DmBannerID )

	UPDATE tchdctab
	SET TiLeThucChayHDCTSoVoiBanner = IIF(ISNULL(cte.TongGoi, 0) <>0,ROUND(Convert(FLOAT,ISNULL(hdct.SoLuong*hdct.DonGia, 0))/Convert(FLOAT,cte.TongGoi),5)*100, 100),
	    DaThucHienUpdateTiLe = 1
	FROM ABM_Data_ThucChay.dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] tchdctab
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN  CTE_Soluong_All_HD cte ON tchdctab.DmBannerREF = cte.DmBannerID 
	WHERE tchdctab.DeletedStatus = 0
		  AND hdct.DmLoaiREF = 42
	AND tchdctab.DmSanPhamREF <> 817 --HAIDH COMMENT 16/04/2025 loai tru viec tinh ti le cho san pham Marketing Fee vi no duoc treo cung banner voi phan bo chinh va duoc tinh la 100 tien thuc chay

	--==================================7. Thực hiện update tỉ lệ cho sản phẩm Marketing fee - HAIDH COMMENT 16/09/2025
	UPDATE tchdctab
	SET TiLeThucChayHDCTSoVoiBanner = 100,
	    DaThucHienUpdateTiLe = 1
	FROM ABM_Data_ThucChay.dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] tchdctab
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID
	INNER JOIN  #DmBannerUpdate cte ON tchdctab.DmBannerREF = cte.DmBannerID 
	WHERE tchdctab.DeletedStatus = 0
		  AND hdct.DmLoaiREF = 42
	AND tchdctab.DmSanPhamREF = 817 --HAIDH COMMENT 16/04/2025 loai tru viec tinh ti le cho san pham Marketing Fee vi no duoc treo cung banner voi phan bo chinh va duoc tinh la 100 tien thuc chay
	AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan_MKT

	DROP TABLE #ThucChayHopDongChiTietAndBanner_Admatic
	DROP TABLE #DmBannerUpdate
	DROP TABLE #PhanBoThayDoiThanhTien


END

```
