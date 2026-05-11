# Stored Procedure: `ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Native_Ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-17 15:57:36.690000
- **Ngày sửa cuối**: 2021-05-26 09:29:41.150000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Native_Ads] '2021-04-23'
[dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads]
*/
CREATE PROCEDURE [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Native_Ads]
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
			[DonGia_Banner] [float] NOT NULL,
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
			WHERE hdct.DmSanPhamREF IN (821,5133)
			AND hdct.DeletedStatus = 0
			AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
			AND hdct.DonViTinhREF <> 3 --KHONG PHAI DON VI TINH NGAY
		)hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DmSanPhamREF IN ( 821,5133) --Native Ads, OnImage
		AND CONVERT(DATE,tchdct.LastModifiedAt) >= @NgayThucHien
		
		
		--cap nhap trang thai ban ghi
		UPDATE hdct
		set hdct.status = 1
		from #ThucChayHopDongChiTietAndBanner_Native_Ads hdct  
		INNER JOIN [dbo].[ThucChayHopDongChiTietAndBanner_Native_Ads] tc
		 on tc.ThucChayHopDongChiTietID = hdct.ThucChayHopDongChiTietID 


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


		--select * from #ThucChayHopDongChiTietAndBanner_Native_Ads

		--select tc.*,hdct.ThucChayHopDongChiTietID as od FROM [dbo].[ThucChayHopDongChiTietAndBanner_Native_Ads] tc INNER JOIN 
		--#ThucChayHopDongChiTietAndBanner_Native_Ads hdct on tc.ThucChayHopDongChiTietID = hdct.ThucChayHopDongChiTietID 
	 --   WHERE  1=1
		--AND hdct.[STATUS]=1

		UPDATE tc
		   SET tc.[ThucChayHopDongChiTietID] = hdct.ThucChayHopDongChiTietID
			  ,tc.[DmBannerID] = hdct.DmBannerID
			  ,tc.[HopDongChiTietREF] = hdct.HopDongChiTietREF
			  ,tc.[HopDongREF] = hdct.HopDongREF
			  ,tc.[BookingREF] = hdct.BookingREF
			  ,tc.[ThoiGianBatDau] = hdct.ThoiGianBatDau
			  ,tc.[ThoiGianKetThuc] = hdct.ThoiGianKetThuc
			  --,tc.[TiLeThucChayHDCTSoVoiBanner] = hdct.TiLeThucChayHDCTSoVoiBanner
			  --,tc.[DaThucHienUpdateTiLe] = hdct.DaThucHienUpdateTiLe
			  ,tc.[CreatedBy] = hdct.CreatedBy
			  ,tc.[CreatedAt] = hdct.CreatedAt
			  ,tc.[LastModifiedBy] = hdct.LastModifiedBy
			  ,tc.[LastModifiedAt] = hdct.LastModifiedAt
			  ,tc.[DeletedStatus] = hdct.DeletedStatus
			  ,tc.[DsNhanHangREF] = hdct.DsNhanHangREF
			  --,tc.[DonGia_Banner] = hdct.DonGia_Banner
			  ,tc.[DmHinhThucQuangCaoID] = hdct.DmHinhThucQuangCaoID
			  ,tc.[DmSanPhamID] = hdct.DmSanPhamID
			  ,tc.[DonViTinh] = hdct.DonViTinh
		FROM [dbo].[ThucChayHopDongChiTietAndBanner_Native_Ads] tc INNER JOIN 
		#ThucChayHopDongChiTietAndBanner_Native_Ads hdct on tc.ThucChayHopDongChiTietID = hdct.ThucChayHopDongChiTietID 
	    WHERE  1=1
		AND hdct.[STATUS]=1

		--THUC HIEN CAP NHAP
		UPDATE TC
		SET TC.TiLeThucChayHDCTSoVoiBanner = 0
		FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] TC
		WHERE TC.DeletedStatus = 1

		--Thuc hien check log 2021-05-25
		insert into dbo.Log_ThucChayHopDongChitietAndBanner
		SELECT tt.DmBannerid as DmBanner, @NgayThucHien AS NgayThucHien, '[ThucChayHopDongChiTietAndBanner_Native_Ads]' AS Table_Name, tt.[status] as Actions, getdate() createat 
		from #ThucChayHopDongChiTietAndBanner_Native_Ads tt

		DROP TABLE #ThucChayHopDongChiTietAndBanner_Native_Ads
		
END



```
