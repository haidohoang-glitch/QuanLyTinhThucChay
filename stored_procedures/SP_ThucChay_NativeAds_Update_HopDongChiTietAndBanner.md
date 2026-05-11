# Stored Procedure: `ThucChay_NativeAds_Update_HopDongChiTietAndBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-03-07 17:08:52.870000
- **Ngày sửa cuối**: 2025-03-07 17:08:52.870000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayCheckThayDoi` | `date(3)` | No |
| `@NgayDanhSoGioiHan` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChay_NativeAds_Update_HopDongChiTietAndBanner]
	@NgayCheckThayDoi DATE,
	@NgayDanhSoGioiHan DATE = NULL
AS
BEGIN

	CREATE TABLE #ThucChayHopDongChitietTemp
	(		[ThucChayHopDongChiTietID] [int] NULL,
			[DmBannerID] [nvarchar](50) NULL,
			[HopDongChiTietREF] [int] NULL,
			[HopDongREF] [int] NULL,
			[BookingREF] [int] NULL,
			[ThoiGianBatDau] [datetime] NULL,
			[ThoiGianKetThuc] [datetime] NULL,
			[TiLeThucChayHDCTSoVoiBanner] FLOAT NULL,
			[DaThucHienUpdateTiLe] [tinyint] NULL,
			[CreatedBy] [nvarchar](50) NULL,
			[CreatedAt] [datetime] NULL,
			[LastModifiedBy] [nvarchar](50) NULL,
			[LastModifiedAt] [datetime] NULL,
			[DeletedStatus] [int] NULL,
			[DsNhanHangREF] [nvarchar](200) NULL,
			[DonGia_Banner] [float] NOT NULL,
			[DmHinhThucQuangCaoID] [int] NOT NULL,
			[DmSanPhamID] [int] NOT NULL,
			[DonViTinh] [nvarchar](50) NULL,
			[Status]  [int] NULL,
	)

	CREATE TABLE #PhanBoThayDoiSoLuong
	(   HopDongChiTietID INT)

	--===================================== 1. Xác định bản ghi thucchayhopdongchitiet thay đổi =====================================================================
	INSERT INTO #ThucChayHopDongChitietTemp
		        ( ThucChayHopDongChiTietID ,
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
		          DmSanPhamID ,
		          DonViTinh ,
		          Status
		        )
	SELECT  DISTINCT  tchdct.ThucChayHopDongChiTietID
					, CONVERT(INT,tchdct.DmBannerREF)DmBannerREF
					, tchdct.HopDongChiTietREF AS HopDongChiTietREF
					, tchdct.HopDongREF
					, tchdct.BookingREF AS BookingREF
					, tchdct.ThoiGianBatDau
					, tchdct.ThoiGianKetThuc
					, 0 TiLeThucChayHDCTSoVoiBanner
					, 0 DaThucHienUpdateTile
					, tchdct.CreatedBy, tchdct.CreatedAt
					, tchdct.LastModifiedBy,tchdct.LastModifiedAt
					, tchdct.DeletedStatus
					, tchdct.DmNhanHangREF
					, ISNULL(hdct.DonGia,0) DonGiaBanner
					, tchdct.DmHinhThucQuangCaoREF
					, tchdct.DmSanPhamREF
					, '' DonViTinh
					, 0 [Status] 
	FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = tchdct.HopDongREF
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
	WHERE (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan )
		  AND hd.TrangThaiHopDong NOT IN (0, 3)
		  AND hdct.DeletedStatus = 0
		  AND hdct.DmSanPhamREF IN (821,5133, 733)
		  AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
		  AND hdct.DonViTinhREF <> 3 
		  AND tchdct.DmSanPhamREF IN ( 821,5133, 733)
		  AND CONVERT(DATE,tchdct.LastModifiedAt) >= @NgayCheckThayDoi
		

	--==================================== 2. Thực hiện merge data thucchayhopdongchitiet thêm mới hoặc thay đổi ===================================================================
	MERGE INTO ABM_Data_ThucChay.dbo.ThucChayHopDongChiTietAndBanner_Native_Ads AS target
	USING #ThucChayHopDongChitietTemp AS source
	ON  target.ThucChayHopDongChiTietID = source.ThucChayHopDongChiTietID
	WHEN MATCHED THEN 
	UPDATE SET	    target.DmBannerID = source.DmBannerID,
					target.HopDongChiTietREF = source.HopDongChiTietREF,
					target.HopDongREF = source.HopDongREF,
					target.BookingREF = source.BookingREF,
					target.ThoiGianBatDau = source.ThoiGianBatDau,
					target.ThoiGianKetThuc = source.ThoiGianKetThuc,
					target.TiLeThucChayHDCTSoVoiBanner = IIF(source.DeletedStatus = 1, 0, target.TiLeThucChayHDCTSoVoiBanner), 
					target.DaThucHienUpdateTiLe = IIF(source.DeletedStatus = 1, 1, target.DaThucHienUpdateTiLe),
					target.CreatedBy = source.CreatedBy,
					target.CreatedAt = source.CreatedAt,
					target.LastModifiedBy = source.LastModifiedBy,
					target.LastModifiedAt = source.LastModifiedAt,
					target.DeletedStatus = source.DeletedStatus,
					target.DsNhanHangREF = source.DsNhanHangREF,
					target.DonGia_Banner = source.DonGia_Banner,   --
					target.DmHinhThucQuangCaoID = source.DmHinhThucQuangCaoID,
					target.DmSanPhamID = source.DmSanPhamID,
					target.DonViTinh = source.DonViTinh
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
		          DsNhanHangREF ,
		          DonGia_Banner ,
		          DmHinhThucQuangCaoID ,
		          DmSanPhamID,
				  DonViTinh) 
	VALUES (	    source.ThucChayHopDongChiTietID ,
					source.DmBannerID ,
					source.HopDongChiTietREF ,
					source.HopDongREF ,
					source.BookingREF ,
					source.ThoiGianBatDau ,
					source.ThoiGianKetThuc ,
					source.TiLeThucChayHDCTSoVoiBanner ,
					source.DaThucHienUpdateTiLe ,
					source.CreatedBy ,
					source.CreatedAt ,
					source.LastModifiedBy ,
					source.LastModifiedAt ,
					source.DeletedStatus ,
					source.DsNhanHangREF ,
					source.DonGia_Banner ,
					source.DmHinhThucQuangCaoID ,
					source.DmSanPhamID,
					source.DonViTinh);

	--=================================== 3. Xác định phân bổ thay đổi số lượng làm ảnh hưởng đến SLHD của banner, từ đó làm ảnh đến tỉ lệ của phân bổ đó và các phân bổ trong cùng banner
	INSERT INTO #PhanBoThayDoiSoLuong
	(
	    HopDongChiTietID
	)
	SELECT DISTINCT hdct.HopDongChiTietID
    FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hdct.HopDongFK = hd.HopDongID
	WHERE    hdct.DmSanPhamREF IN (821,5133, 733) AND
		     hdct.DonViTinhREF <> 3  AND 
			 (@NgayDanhSoGioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan ) AND
		  (  CAST(hdct.LastModifiedAt AS DATE) = @NgayCheckThayDoi OR 
		     ((hd.TrangThaiHopDong = 3 OR hd.DeletedStatus = 1) AND CAST(hd.LastModifiedAt AS DATE) = @NgayCheckThayDoi)
		  )

	--=================================== 4. Xác định banner cần xử lý
	CREATE TABLE #DmBannerUpdate 
	(	DmBannerID NVARCHAR(200))
	INSERT INTO #DmBannerUpdate (DmBannerID)
	SELECT DISTINCT tchdctab.DmBannerID
	FROM ABM_Data_ThucChay.dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
	INNER JOIN dbo.HopDongChiTiet hdct	ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd  ON hd.HopDongID = hdct.HopDongFK
	WHERE  (tchdctab.DaThucHienUpdateTiLe = 0 OR EXISTS (SELECT 1 FROM #PhanBoThayDoiSoLuong dm WHERE dm.HopDongChiTietID =  hdct.HopDongChiTietID ))
			AND tchdctab.DeletedStatus = 0
			AND hd.TrangThaiHopDong NOT IN (0, 3) 
			AND hd.DeletedStatus = 0
			AND hdct.DeletedStatus = 0
			AND hdct.DmSanPhamREF IN (821,5133, 733)
			AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
			AND hdct.DonViTinhREF <> 3 
	
			

	--================================== 5. thực hiện update
	;WITH CTE_Soluong_All_HD AS (
									SELECT  dm.DmBannerID, 
											TongGoi = sum(convert(bigint,ISNULL(hdct.SoLuong,0))*ISNULL(hdct.DonGia,0))
									FROM  #DmBannerUpdate dm
									INNER JOIN ABM_Data_ThucChay.dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab ON tchdctab.DmBannerID = dm.DmBannerID
									INNER JOIN (SELECT HopDongChiTietID,  hdct.SoLuong, hdct.Dongia, hdct.DmSanPhamREF
									            FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
												INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
											    WHERE hdct.DeletedStatus = 0 AND 
												      hd.DeletedStatus = 0 AND
													  hd.TrangThaiHopDong <> 3 
													  AND hdct.DmSanPhamREF IN  (821,5133, 733)
													  AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
													  AND hdct.DonViTinhREF <> 3 
												) hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
									WHERE tchdctab.DmHinhThucQuangCaoID <> 42 AND tchdctab.DeletedStatus = 0
									GROUP BY  dm.DmBannerID )

	UPDATE tchdctab
	SET TiLeThucChayHDCTSoVoiBanner = IIF(ISNULL(cte.TongGoi, 0) <>0,(ROUND((Convert(FLOAT,hdct.SoLuong*hdct.DonGia))/Convert(FLOAT,cte.TongGoi),5)*100), 100),
	    DaThucHienUpdateTiLe = 1
	FROM ABM_Data_ThucChay.dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdctab.HopDongChiTietREF
	INNER JOIN  CTE_Soluong_All_HD cte ON tchdctab.DmBannerID = cte.DmBannerID 
	WHERE tchdctab.DeletedStatus = 0
		  AND hdct.DmSanPhamREF IN  (821,5133, 733)
		  AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
		  AND hdct.DonViTinhREF <> 3 
		 
	
	DROP TABLE #DmBannerUpdate
	DROP TABLE #ThucChayHopDongChitietTemp

END


```
