# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_LOG_New`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-11 17:51:31.447000
- **Ngày sửa cuối**: 2018-10-04 10:36:26.523000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_LOG_New] 	
As 	
begin
	DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX)
	SET @NgayThucHien = 
	(
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   ThucChayHopDongChiTietPRlog dchdct
		)

	SET @NgayThucHien = DATEADD(HOUR,-24,@NgayThucHien)
	PRINT @NgayThucHien
	CREATE TABLE #ThucChayHopDongChiTietPRLog(
		[ThucChayHopDongChiTietPRLogID] [bigint] NOT NULL,
		[ThucChayHopDongChiTietPRREF] [int] NOT NULL,
		[HopDongREF] [bigint] NOT NULL,
		[HopDongChiTietREF] [bigint] NULL,
		[DmWebsiteREF] [int] NULL,
		[TenWebsite] [nvarchar](200) NULL,
		[DmChuyenMucREF] [int] NULL,
		[TenChuyenMuc] [nvarchar](200) NULL,
		[TieuDiem] [int] NULL,
		[DmNhanHangREF] [nvarchar](200) NULL,
		[NhanHang] [nvarchar](200) NULL,
		[KhuyenMai] [int] NULL,
		[GiaTien] [bigint] NULL,
		[ThoiGianBatDau] [datetime] NULL,
		[Link] [nvarchar](200) NULL,
		[GhiChu] [nvarchar](200) NULL,
		[DmHinhThucQuangCaoREF] [int] NULL,
		[TenHinhThucQuangCao] [nvarchar](200) NULL,
		[ThoiGianLog] [datetime] NULL,
		[NguoiLog] [nvarchar](200) NULL,
		[LoaiLog] [int] NULL,
		[CreatedBy] [nvarchar](200) NULL,
		[CreatedAt] [datetime] NULL,
		[LastModifiedBy] [nvarchar](200) NULL,
		[LastModifiedAt] [datetime] NULL,
		[DeletedStatus] [int] NULL,
		[PrintStatus] [int] NULL,
		[RecordStatus] [int] NULL,
		[SoLuong] [int] NULL,
		STATUS INT
	)

	SET @SQL = 
		'
	SELECT 
			tchdctp.ThucChayHopDongChiTietPRLogID,
			tchdctp.ThucChayHopDongChiTietPRREF,
			  tchdctp.HopDongREF,
			  tchdctp.HopDongChiTietREF,
			  tchdctp.DmWebsiteREF,
			  tchdctp.TenWebsite,
			  tchdctp.DmChuyenMucREF,
			  tchdctp.TenChuyenMuc,
			  tchdctp.TieuDiem,
			  tchdctp.DmNhanHangREF,
			  tchdctp.NhanHang,
			  tchdctp.KhuyenMai,
			  tchdctp.GiaTien,
			  (CASE WHEN tchdctp.ThoiGianBatDau = ''0001-01-01''' +  ' THEN ' + '''1900-01-01''' + '
				ELSE tchdctp.ThoiGianBatDau
			  END )ThoiGianBatDau,
			  tchdctp.Link,
			  tchdctp.GhiChu,
			  tchdctp.DmHinhThucQuangCaoREF, 
			  tchdctp.TenHinhThucQuangCao,
			  tchdctp.ThoiGianLog,
			  tchdctp.NguoiLog,
			  tchdctp.LoaiLog,
			  tchdctp.CreatedBy,
			  tchdctp.CreatedAt,
			  tchdctp.LastModifiedBy,
			  tchdctp.LastModifiedAt,
			  tchdctp.DeletedStatus ,
			  tchdctp.PrintStatus ,
			  tchdctp.RecordStatus,
			  tchdctp.SoLuong,
			  0
	FROM OPENQUERY(MYSQL,''CALL Abm_get_hdcn_thucchay_pr_version (''''' + CONVERT(NVARCHAR(50), @NgayThucHien, 120)
		+ ''''');'') tchdctp'

	PRINT @SQL
	INSERT INTO #ThucChayHopDongChiTietPRLog
	EXECUTE
	  (
		@SQL
	  )
	--DROP TABLE #ThucChayHopDongChiTietPR
	   -- Set trang thai = 1 doi voi nhung truong hop sua chua 
		UPDATE #ThucChayHopDongChiTietPRLog
		SET    [STATUS] = 1
		FROM  #ThucChayHopDongChiTietPRLog t INNER JOIN ThucChayHopDongChiTietPRLog  dc
		ON t.[ThucChayHopDongChiTietPRLogID]  = dc.[ThucChayHopDongChiTietPRLogID]
	-- Update nhung row da ton ton                                      
	   UPDATE [dbo].[ThucChayHopDongChiTietPRLog]
			SET    [ThucChayHopDongChiTietPRREF]    = A.ThucChayHopDongChiTietPRREF,
				   [HopDongREF]                     = A.HopDongREF,
				   [HopDongChiTietREF]              = A.HopDongChiTietREF,
				   [DmWebsiteREF]                   = A.DmWebsiteREF,
				   [TenWebsite]                     = A.TenWebsite,
				   [DmChuyenMucREF]                 = A.DmChuyenMucREF,
				   [TenChuyenMuc]                   = A.TenChuyenMuc,
				   [TieuDiem]                       = A.TieuDiem,
				   [DmNhanHangREF]                  = A.DmNhanHangREF,
				   [NhanHang]                       = A.NhanHang,
				   [KhuyenMai]                      = A.KhuyenMai,
				   [GiaTien]                        = A.GiaTien,
				   [ThoiGianBatDau]                 = A.ThoiGianBatDau,
				   [Link]                           = A.Link,
				   [GhiChu]                         = A.ThucChayHopDongChiTietPRREF ,--A.GhiChu,
				   [DmHinhThucQuangCaoREF]          = A.DmHinhThucQuangCaoREF,
				   [TenHinhThucQuangCao]            = A.TenHinhThucQuangCao,
				   [ThoiGianLog]                    = A.ThoiGianLog,
				   [NguoiLog]                       = A.NguoiLog,
				   [LoaiLog]                        = A.LoaiLog,
				   [CreatedBy]                      = A.CreatedBy,
				   [CreatedAt]                      = A.CreatedAt,
				   [LastModifiedBy]                 = A.LastModifiedBy,
				   [LastModifiedAt]                 = A.LastModifiedAt,
				   [DeletedStatus]                  = A.DeletedStatus,
				   [PrintStatus]                    = A.PrintStatus,
				   [RecordStatus]                   = A.RecordStatus,
				   [SoLuong]						= A.SoLuong
		FROM   #ThucChayHopDongChiTietPRLog A 
		WHERE  [STATUS] = 1 AND A.[ThucChayHopDongChiTietPRLogID] = ThucChayHopDongChiTietPRLog.[ThucChayHopDongChiTietPRLogID]
	-- Insert Row chua ton tai
	INSERT INTO [dbo].[ThucChayHopDongChiTietPRLog]
			  (
				[ThucChayHopDongChiTietPRLogID],
				[ThucChayHopDongChiTietPRREF],
				[HopDongREF],
				[HopDongChiTietREF],
				[DmWebsiteREF],
				[TenWebsite],
				[DmChuyenMucREF],
				[TenChuyenMuc],
				[TieuDiem],
				[DmNhanHangREF],
				[NhanHang],
				[KhuyenMai],
				[GiaTien],
				[ThoiGianBatDau],
				[Link],
				[GhiChu],
				[DmHinhThucQuangCaoREF],
				[TenHinhThucQuangCao],
				[ThoiGianLog],
				[NguoiLog],
				[LoaiLog],
				[CreatedBy],
				[CreatedAt],
				[LastModifiedBy],
				[LastModifiedAt],
				[DeletedStatus],
				[PrintStatus],
				[RecordStatus],
				[SoLuong]
			  )
	  
	SELECT 
				 [ThucChayHopDongChiTietPRLogID],
				[ThucChayHopDongChiTietPRREF],
				[HopDongREF],
				[HopDongChiTietREF],
				[DmWebsiteREF],
				[TenWebsite],
				[DmChuyenMucREF],
				[TenChuyenMuc],
				[TieuDiem],
				[DmNhanHangREF],
				[NhanHang],
				[KhuyenMai],
				[GiaTien],
				[ThoiGianBatDau],
				[Link],
				[GhiChu],
				[DmHinhThucQuangCaoREF],
				[TenHinhThucQuangCao],
				[ThoiGianLog],
				[NguoiLog],
				[LoaiLog],
				[CreatedBy],
				[CreatedAt],
				[LastModifiedBy],
				[LastModifiedAt],
				[DeletedStatus],
				[PrintStatus],
				[RecordStatus],
				[SoLuong]
	FROM #ThucChayHopDongChiTietPRLog   dchdct WHERE dchdct.[STATUS]=0

	--Update huy
	UPDATE ThucChayHopDongChiTietPR
	SET   	LastModifiedBy = T.LastModifiedBy,
	      	LastModifiedAt = T.LastModifiedAt,
	      	DeletedStatus = 1
	FROM  #ThucChayHopDongChiTietPRLog t INNER JOIN dbo.ThucChayHopDongChiTietPR  dc
	ON t.[ThucChayHopDongChiTietPRREF]  = dc.[ThucChayHopDongChiTietPRID]
	WHERE t.LoaiLog = 3

END

```
