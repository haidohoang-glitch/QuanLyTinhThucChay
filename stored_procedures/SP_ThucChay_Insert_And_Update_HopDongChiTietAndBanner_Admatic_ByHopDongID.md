# Stored Procedure: `ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic_ByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-15 17:59:59.683000
- **Ngày sửa cuối**: 2019-03-12 09:11:36.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic_ByHopDongID] 1004380
CREATE PROCEDURE [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic_ByHopDongID]
	@HopDongID INT
AS
BEGIN
	CREATE TABLE #ThucChayHopDongChiTietAndBanner_Admatic(
			[ThucChayHopDongChiTietID] [int] NULL,
			[DmBannerID] [nvarchar](50) NULL,
			[HopDongChiTietREF] [int] NULL,
			[HopDongREF] [int] NULL,
			[BookingREF] [int] NULL,
			[ThoiGianBatDau] [datetime] NULL,
			[ThoiGianKetThuc] [datetime] NULL,
			[TiLeThucChayHDCTSoVoiBanner] [float] NULL,
			[DaThucHienUpdateTiLe] [tinyint] NULL,
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
		
		INSERT INTO #ThucChayHopDongChiTietAndBanner_Admatic
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
	
		SELECT DISTINCT ThucChayHopDongChiTietID, CONVERT(INT,DmBannerREF)DmBannerREF
		, -1 AS HopDongChiTietREF, HopDongREF,0 AS BookingREF, ThoiGianBatDau, ThoiGianKetThuc
		, 100 TiLeThucChayHDCTSoVoiBanner
		, 1 DaThucHienUpdateTile
		, CreatedBy, CreatedAt
		, LastModifiedBy, LastModifiedAt
		, DeletedStatus
		, DmNhanHangREF
		, 0 DonGiaBanner
		, DmHinhThucQuangCaoREF
		, DmSanPhamREF
		, (SELECT TOP 1 (CASE WHEN LoaiDonGiaTheoDVT = 1 THEN N'CPC'
							WHEN LoaiDonGiaTheoDVT IN (2,3) THEN N'CPM'
							WHEN LoaiDonGiaTheoDVT IN (4) THEN N'TRUE VIEW'
						ELSE N''
						END)
			FROM dbo.AdmaticDonGiaBanner
			WHERE DmBannerID = DmBannerREF
		)DonViTinh
		, 0 [Status] 
		FROM dbo.ThucChayHopDongChiTiet
		WHERE DmHinhThucQuangCaoREF = 42
		AND HopDongREF = @HopDongID
		AND DeletedStatus = 0
		AND ISNULL(HopDongREF,0) <> 0
		AND DmSanPhamREF NOT IN (736,817) -- chi phí công nghệ, chi phi marketing fee
		
		----CHECK THEM THONG TIN TRUNG HOP BANNER, SANPHAM
		--DELETE FROM #ThucChayHopDongChiTietAndBanner_Admatic
		--WHERE ThucChayHopDongChiTietID IN 
		--(
		--	SELECT tc.ThucChayHopDongChiTietID FROM #ThucChayHopDongChiTietAndBanner_Admatic tc
		--	INNER JOIN 
		--	(
		--		SELECT A.DmBannerREF, A.DmSanPhamREF, COUNT(A.DmBannerREF)sl FROM #ThucChayHopDongChiTietAndBanner_Admatic A
		--		GROUP BY A.DmBannerREF, A.DmSanPhamREF HAVING COUNT(A.DmBannerREF)>1
		--	)A ON tc.DmBannerREF = A.DmBannerREF AND A.DmSanPhamREF = tc.DmSanPhamREF 
		--	WHERE ISNULL(tc.HopDongChiTietREF,0) IN (-1,0)
		--)

		UPDATE #ThucChayHopDongChiTietAndBanner_Admatic
		SET [Status] = 1
		FROM #ThucChayHopDongChiTietAndBanner_Admatic t
		INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic dc
		ON t.DmBannerID = dc.DmBannerID
		AND t.DmSanPhamID = dc.DmSanPhamID
		AND dc.HopDongREF = t.HopDongREF

		--AND t.ThoiGianBatDau = dc.ThoiGianBatDau
		--AND t.ThoiGianKetThuc = dc.ThoiGianKetThuc

		--SELECT * FROM #ThucChayHopDongChiTietAndBanner_Admatic

		INSERT INTO dbo.ThucChayHopDongChiTietAndBanner_Admatic
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
		          DmSanPhamID,
				  DonViTinh
		        )
	SELECT ThucChayHopDongChiTietID ,
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
		          DonViTinh  
		FROM #ThucChayHopDongChiTietAndBanner_Admatic
		WHERE [Status] = 0

		UPDATE [dbo].[ThucChayHopDongChiTietAndBanner_Admatic]
		   SET [ThucChayHopDongChiTietID] = hdct.ThucChayHopDongChiTietID
			  ,[DmBannerID] = hdct.DmBannerID
			  ,[HopDongChiTietREF] = hdct.HopDongChiTietREF
			  ,[HopDongREF] = hdct.HopDongREF
			  ,[BookingREF] = hdct.BookingREF
			  ,[ThoiGianBatDau] = hdct.ThoiGianBatDau
			  ,[ThoiGianKetThuc] = hdct.ThoiGianKetThuc
			  --,[TiLeThucChayHDCTSoVoiBanner] = hdct.TiLeThucChayHDCTSoVoiBanner
			  --,[DaThucHienUpdateTiLe] = hdct.DaThucHienUpdateTiLe
			  ,[CreatedBy] = hdct.CreatedBy
			  ,[CreatedAt] = hdct.CreatedAt
			  ,[LastModifiedBy] = hdct.LastModifiedBy
			  ,[LastModifiedAt] = hdct.LastModifiedAt
			  ,[DeletedStatus] = hdct.DeletedStatus
			  ,[DsNhanHangREF] = hdct.DsNhanHangREF
			  --,[DonGia_Banner] = hdct.DonGia_Banner
			  ,[DmHinhThucQuangCaoID] = hdct.DmHinhThucQuangCaoID
			  ,[DmSanPhamID] = hdct.DmSanPhamID
			  ,[DonViTinh] = hdct.DonViTinh
		FROM #ThucChayHopDongChiTietAndBanner_Admatic hdct
	    WHERE  [dbo].[ThucChayHopDongChiTietAndBanner_Admatic].ThucChayHopDongChiTietID = hdct.ThucChayHopDongChiTietID 
		AND hdct.[STATUS]=1

		DROP TABLE #ThucChayHopDongChiTietAndBanner_Admatic

		--UPDATE DON GIA  BANNER VA TiLeThucChayHDCTSoVoiBanner, DaThucHienUpdateTiLe
	--SELECT '1'

END

```
