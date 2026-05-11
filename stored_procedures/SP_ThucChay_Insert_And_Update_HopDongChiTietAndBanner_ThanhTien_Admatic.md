# Stored Procedure: `ThucChay_Insert_And_Update_HopDongChiTietAndBanner_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-06-16 14:31:59.603000
- **Ngày sửa cuối**: 2021-06-04 16:57:26.603000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_ThanhTien_Admatic] '2021-05-27'
select * from  [ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic]
where [HopDongREF] = 1024535
*/


CREATE PROCEDURE [dbo].[ThucChay_Insert_And_Update_HopDongChiTietAndBanner_ThanhTien_Admatic]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @NgayDanhSoHopDong Datetime = '2020-07-01'
	CREATE TABLE #ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic(
			[ThucChayHopDongChiTietREF] [int] NULL,
			[DmBannerREF] [nvarchar](50) NULL,
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
			[DmHinhThucQuangCaoREF] [int] NOT NULL,
			[DmSanPhamREF] [int] NOT NULL,
			[Status]  [int] NULL,
		) 
		
		INSERT INTO #ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic
		        ( [ThucChayHopDongChiTietREF] ,
		          [DmBannerREF] ,
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
		          [DmHinhThucQuangCaoREF] ,
		          [DmSanPhamREF] ,
		          [Status]
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
		, tchdct.DmHinhThucQuangCaoREF
		, tchdct.DmSanPhamREF
		, 0 [Status] 
		FROM dbo.ThucChayHopDongChiTiet tchdct
		LEFT JOIN 
		(SELECT hd.NgayDanhSoHopDong,hdct.* FROM dbo.HopDongChiTiet hdct
			inner join hopdong hd on hdct.HopDongFK = hd.HopDongID
			WHERE 1=1
			AND hdct.DeletedStatus = 0
			AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13))
			AND hdct.DmLoaiREF = 42 --admatic
		)hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		and (hdct.DmSanPhamREF = 733 or hdct.DmSanPhamREF = tchdct.DmSanPhamREF)
		WHERE 1=1
		AND CONVERT(DATE,tchdct.LastModifiedAt) >= @NgayThucHien
		--AND tchdct.DeletedStatus = 0 haidh comment de lay thong tin banner xoa
		AND hdct.NgayDanhSoHopDong >= @NgayDanhSoHopDong
		
		--CAP NHAT THONG TIN TRANG THAI VA TI LE BANNER
		UPDATE t
		SET t.[Status] = 1
		FROM #ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic t
		INNER JOIN dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] dc
		ON t.ThucChayHopDongChiTietREF = dc.ThucChayHopDongChiTietREF
		


		INSERT INTO dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic]
		        ( ThucChayHopDongChiTietREF ,
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
		          DmSanPhamREF
				  
		        )
	SELECT ThucChayHopDongChiTietREF ,
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
		          DmSanPhamREF 
		FROM #ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic
		WHERE [Status] = 0

		UPDATE [dbo].[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic]
		   SET [ThucChayHopDongChiTietREF] = hdct.ThucChayHopDongChiTietREF
			  ,[DmBannerREF] = hdct.DmBannerREF
			  ,[HopDongChiTietREF] = hdct.HopDongChiTietREF
			  ,[HopDongREF] = hdct.HopDongREF
			  ,[BookingREF] = hdct.BookingREF
			  ,[ThoiGianBatDau] = hdct.ThoiGianBatDau
			  ,[ThoiGianKetThuc] = hdct.ThoiGianKetThuc
			  ,[CreatedBy] = hdct.CreatedBy
			  ,[CreatedAt] = hdct.CreatedAt
			  ,[LastModifiedBy] = hdct.LastModifiedBy
			  ,[LastModifiedAt] = hdct.LastModifiedAt
			  ,[DeletedStatus] = hdct.DeletedStatus
			  ,[DsNhanHangREF] = hdct.DsNhanHangREF
			  ,[DmHinhThucQuangCaoREF] = hdct.DmHinhThucQuangCaoREF
			  ,[DmSanPhamREF] = hdct.DmSanPhamREF
			 FROM #ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic hdct
	    WHERE  [dbo].[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic].ThucChayHopDongChiTietREF = hdct.ThucChayHopDongChiTietREF
		AND hdct.[STATUS]=1

		--UPDATE TI LE CUA CAC BANNER BI XOA 
		UPDATE tc
		SET tc.TiLeThucChayHDCTSoVoiBanner = 0
		FROM dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic tc
		WHERE tc.DeletedStatus = 1

		DROP TABLE #ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic
		
END



```
