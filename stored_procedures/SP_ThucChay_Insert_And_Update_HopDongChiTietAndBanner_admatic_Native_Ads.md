# Stored Procedure: `ThucChay_Insert_And_Update_HopDongChiTietAndBanner_admatic_Native_Ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-12-10 16:00:04.573000
- **Ngày sửa cuối**: 2021-06-04 17:03:41.147000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Native_Ads]
[dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads]
*/
CREATE PROCEDURE [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_admatic_Native_Ads]
	@NgayThucHien DATETIME
AS
BEGIN
	CREATE TABLE #ThucChayHopDongChiTietAndBanner_Native_Ads(
			[ThucChayHopDongChiTietID] [int] NULL,
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
			[DonGia_Banner] [int] NOT NULL,
			[DmHinhThucQuangCaoID] [int] NOT NULL,
			[DmSanPhamID] [int] NOT NULL,
			[DonViTinh] [nvarchar](50) NULL,
			[Status]  [int] NULL,
		) 
		
		INSERT INTO #ThucChayHopDongChiTietAndBanner_Native_Ads
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

		SELECT DISTINCT tchdct.ThucChayHopDongChiTietID, CONVERT(INT,tchdct.DmBannerREF)DmBannerREF
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
		FROM dbo.ThucChayHopDongChiTiet tchdct
		LEFT JOIN 
		(SELECT * FROM dbo.HopDongChiTiet hdct
			WHERE hdct.DmSanPhamREF IN (821, 5133)
			AND hdct.DeletedStatus = 0
			AND hdct.DmLoaiREF = 42
			AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13))
			AND hdct.DonViTinhREF <> 3 --KHONG PHAI DON VI TINH NGAY
		)hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DmSanPhamREF = 821 --Native Ads
		AND CONVERT(DATE,tchdct.LastModifiedAt) >= @NgayThucHien
		AND tchdct.DeletedStatus = 0
		
		--CAP NHAT THONG TIN TRANG THAI VA TI LE BANNER
		UPDATE t
		SET t.[Status] = 1
		FROM #ThucChayHopDongChiTietAndBanner_Native_Ads t
		INNER JOIN dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] dc
		ON t.ThucChayHopDongChiTietID = dc.ThucChayHopDongChiTietID
		

		INSERT INTO dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads]
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
		FROM #ThucChayHopDongChiTietAndBanner_Native_Ads
		WHERE [Status] = 0

		UPDATE [dbo].[ThucChayHopDongChiTietAndBanner_Native_Ads]
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
		FROM #ThucChayHopDongChiTietAndBanner_Native_Ads hdct
	    WHERE  [dbo].[ThucChayHopDongChiTietAndBanner_Native_Ads].ThucChayHopDongChiTietID = hdct.ThucChayHopDongChiTietID 
		AND hdct.[STATUS]=1

		DROP TABLE #ThucChayHopDongChiTietAndBanner_Native_Ads
		
END

```
