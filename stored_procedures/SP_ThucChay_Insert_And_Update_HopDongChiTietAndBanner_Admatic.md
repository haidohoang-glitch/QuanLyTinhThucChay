# Stored Procedure: `ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-12-05 17:19:34.120000
- **Ngày sửa cuối**: 2025-09-29 14:14:20.353000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic] '2017-07-17'
CREATE PROCEDURE [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Admatic]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @NgayDanhSoGioiHan DateTime = '2020-07-20'
	, @NgayDanhSoGioiHan_MKT datetime = '2025-10-10'
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
	
		SELECT DISTINCT tt.ThucChayHopDongChiTietID, CONVERT(INT,tt.DmBannerREF)DmBannerREF
		,-1 AS HopDongChiTietREF, tt.HopDongREF,0 AS BookingREF, tt.ThoiGianBatDau, tt.ThoiGianKetThuc
		, 100 TiLeThucChayHDCTSoVoiBanner
		, 1 DaThucHienUpdateTile
		, tt.CreatedBy, tt.CreatedAt
		, tt.LastModifiedBy, tt.LastModifiedAt
		, tt.DeletedStatus
		, tt.DmNhanHangREF
		, 0 DonGiaBanner
		, tt.DmHinhThucQuangCaoREF
		, tt.DmSanPhamREF
		, (SELECT TOP 1 (CASE WHEN LoaiDonGiaTheoDVT = 1 THEN N'CPC'
							WHEN LoaiDonGiaTheoDVT IN (2,3) THEN N'CPM'
							WHEN LoaiDonGiaTheoDVT IN (4) THEN N'TRUE VIEW'
						ELSE N''
						END)
			FROM dbo.AdmaticDonGiaBanner
			WHERE DmBannerID = tt.DmBannerREF
		)DonViTinh
		, 0 [Status] 
		FROM dbo.ThucChayHopDongChiTiet tt
		INNER JOIN dbo.HopDong hd on hd.HopDongID = tt.HopDongREF
		WHERE DmHinhThucQuangCaoREF = 42
		AND CONVERT(DATE,tt.LastModifiedAt) >= @NgayThucHien
		AND CONVERT(DATE,hd.NgayDanhSoHopDong) < @NgayDanhSoGioiHan
		AND tt.DeletedStatus = 0
		AND ISNULL(tt.HopDongREF,0) <> 0
		--AND tt.DmSanPhamREF NOT IN (736,817) -- chi phí công nghệ, chi phi marketing fee
		AND tt.DmSanPhamREF NOT IN (736) -- chi phí công nghệ, chi phi marketing fee

		--HAIDH COMMENT 16092025 THEM SANPHAM MKT-FEE CHO VIEC TINH THUC CHAY THEO TIEN VE
		AND NOT (hd.NgayDanhSoHopDong <@NgayDanhSoGioiHan_MKT and tt.DmSanPhamREF = 817) 
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

		--CAP NHAT DON GIA BANNER VOI TRUONG HOP DA CO GIA NHUNG CHUA DC CAP NHAT
		UPDATE [dbo].[ThucChayHopDongChiTietAndBanner_Admatic]
		SET DonGia_Banner = ISNULL((SELECT TOP 1 DonGiaBanner_VAT/1.1 FROM dbo.AdmaticDonGiaBanner WHERE DmBannerID = [dbo].[ThucChayHopDongChiTietAndBanner_Admatic].DmBannerID ORDER BY CreatedAt DESC),0)
		WHERE DonGia_Banner = 0

		DROP TABLE #ThucChayHopDongChiTietAndBanner_Admatic
		
END

```
