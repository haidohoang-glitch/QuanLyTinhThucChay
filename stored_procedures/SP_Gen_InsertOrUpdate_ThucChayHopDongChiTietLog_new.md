# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTietLog_new`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-08 10:14:09.937000
- **Ngày sửa cuối**: 2018-10-30 10:43:31.943000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietLog_new]

AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX)
	

	SET @NgayThucHien = 
	(
			SELECT MAX(dchdct.[ThoiGianLog])
			FROM   dbo.ThucChayHopDongChiTietLog dchdct
		)

	SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)
	PRINT @NgayThucHien

	CREATE TABLE #ThucChayHopDongChiTietLog(
		[ThucChayHopDongChiTietID] [bigint] NULL,
		[HopDongREF] [bigint] NULL,
		[HopDongChiTietREF] [bigint] NULL,
		[DmBannerREF] [nvarchar](200) NULL,
		[TenBanner] [nvarchar](200) NULL,
		[DmViTriREF] [int] NULL,
		[ViTri] [nvarchar](200) NULL,
		[DmNhanHangREF] [nvarchar](200) NULL,
		[NhanHang] [nvarchar](200) NULL,
		[BookingREF] [bigint] NULL,
		[ThoiGianBatDau] date NULL,
		[ThoiGianKetThuc] date NULL,
		[SoLuongThucTreo] [float] NULL,
		[SoLuongThucChay] [float] NULL,
		[DmDonViTinhREF] [int] NULL,
		[DonViTinh] [nvarchar](200) NULL,
		[TypeThucChay] [int] NULL,
		[Link] [nvarchar](200) NULL,
		[GhiChu] [nvarchar](200) NULL,
		[DmHinhThucQuangCaoREF] [int] NULL,
		[TenHinhThucQuangCao] [nvarchar](200) NULL,
		[DmSanPhamREF] [int] NULL,
		[TenSanPham] [nvarchar](200) NULL,
		[InputType] [int] NULL,
		[IsReadBooking] [int] NULL,
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
		STATUS INT
	)
	
	SET @SQL = 
		'
	SELECT 
		tchdctp.ThucChayHopDongChiTietID,
        tchdctp.HopDongREF,
        tchdctp.HopDongChiTietREF,
        tchdctp.DmBannerREF,
        tchdctp.TenBanner,
        tchdctp.DmViTriREF,
        tchdctp.ViTri,
        tchdctp.DmNhanHangREF,
        tchdctp.NhanHang,
        tchdctp.BookingREF,
        tchdctp.ThoiGianBatDau,
        tchdctp.ThoiGianKetThuc,
        tchdctp.SoLuongThucTreo,
        tchdctp.SoLuongThucChay,
        tchdctp.DmDonViTinhREF,
        tchdctp.DonViTinh,
        tchdctp.TypeThucChay,
        tchdctp.Link,
        tchdctp.GhiChu,
        tchdctp.DmHinhThucQuangCaoREF,
        tchdctp.TenHinhThucQuangCao,
        tchdctp.DmSanPhamREF,
        tchdctp.TenSanPham,
        tchdctp.InputType,
        tchdctp.IsReadBooking,
        tchdctp.ThoiGianLog,
        tchdctp.NguoiLog,
        tchdctp.LoaiLog,
        tchdctp.CreatedBy,
        tchdctp.CreatedAt,
        tchdctp.LastModifiedBy,
        tchdctp.LastModifiedAt,
        tchdctp.DeletedStatus,
        tchdctp.PrintStatus,
        tchdctp.RecordStatus , 
		0
	FROM OPENQUERY(MYSQL,''CALL Abm_get_hdcn_thucchay_logging (''''' + CONVERT(NVARCHAR(50), @NgayThucHien, 120)
		+ ''''');'') tchdctp'

	PRINT @SQL
	INSERT INTO #ThucChayHopDongChiTietLog
	EXECUTE
	  (
		@SQL
	  )
	
	--DROP TABLE #ThucChayHopDongChiTietPR
	-- Set trang thai = 1 doi voi nhung truong hop sua chua 
	UPDATE #ThucChayHopDongChiTietLog
	SET    NhanHang =''
	WHERE NhanHang IS NULL


	UPDATE #ThucChayHopDongChiTietLog
	SET    NhanHang = REPLACE(NhanHang, '''''','''')
	
	--CAP NHAT THONG TIN TRANG THAI
	UPDATE #ThucChayHopDongChiTietLog
	SET    [STATUS] = 1
	FROM  #ThucChayHopDongChiTietLog t INNER JOIN dbo.ThucChayHopDongChiTietLog  dc
	ON t.ThucChayHopDongChiTietID  = dc.ThucChayHopDongChiTietID
	AND t.ThoiGianLog  = dc.ThoiGianLog 
	AND t.LoaiLog  = dc.LoaiLog
	 
	--print 'Update'
	UPDATE [dbo].[ThucChayHopDongChiTietLog]
	SET    [ThucChayHopDongChiTietID]  = A.ThucChayHopDongChiTietID,
	        [HopDongREF]                = A.HopDongREF,
	        [HopDongChiTietREF]         = A.HopDongChiTietREF,
	        [DmBannerREF]               = A.DmBannerREF,
	        [TenBanner]                 = A.TenBanner,
	        [DmViTriREF]                = A.DmViTriREF,
	        [ViTri]                     = A.ViTri,
	        [DmNhanHangREF]             = A.DmNhanHangREF,
	        [NhanHang]                  = A.NhanHang,
	        [BookingREF]                = A.BookingREF,
	        [ThoiGianBatDau]            = A.ThoiGianBatDau,
	        [ThoiGianKetThuc]           = A.ThoiGianKetThuc,
	        [SoLuongThucTreo]           = A.SoLuongThucTreo,
	        [SoLuongThucChay]           = A.SoLuongThucChay,
	        [DmDonViTinhREF]            = A.DmDonViTinhREF,
	        [DonViTinh]                 = A.DonViTinh,
	        [TypeThucChay]              = A.TypeThucChay,
	        [Link]                      = A.Link,
	        [GhiChu]                    = A.GhiChu,
	        [DmHinhThucQuangCaoREF]     = A.DmHinhThucQuangCaoREF,
	        [TenHinhThucQuangCao]       = A.TenHinhThucQuangCao,
	        [DmSanPhamREF]              = A.DmSanPhamREF,
	        [TenSanPham]                = A.TenSanPham,
	        [InputType]                 = A.InputType,
	        [IsReadBooking]             = A.IsReadBooking,
	        [ThoiGianLog]               = A.ThoiGianLog,
	        [NguoiLog]                  = A.NguoiLog,
	        [LoaiLog]                   = A.LoaiLog,
	        [CreatedBy]                 = A.CreatedBy,
	        [CreatedAt]                 = A.CreatedAt,
	        [LastModifiedBy]            = A.LastModifiedBy,
	        [LastModifiedAt]            = A.LastModifiedAt,
	        [DeletedStatus]             = A.DeletedStatus,
	        [PrintStatus]               = A.PrintStatus,
	        [RecordStatus]              = A.RecordStatus
	FROM   #ThucChayHopDongChiTietLog A 
	WHERE  [STATUS] = 1 AND A.ThucChayHopDongChiTietID = ThucChayHopDongChiTietLog.ThucChayHopDongChiTietID
	AND A.ThoiGianLog  = ThucChayHopDongChiTietLog.ThoiGianLog 
	AND A.LoaiLog  = ThucChayHopDongChiTietLog.LoaiLog
	
	--INSERT INTO
	INSERT INTO [dbo].[ThucChayHopDongChiTietLog]
	    (
	    [ThucChayHopDongChiTietID],
	    [HopDongREF],
	    [HopDongChiTietREF],
	    [DmBannerREF],
	    [TenBanner],
	    [DmViTriREF],
	    [ViTri],
	    [DmNhanHangREF],
	    [NhanHang],
	    [BookingREF],
	    [ThoiGianBatDau],
	    [ThoiGianKetThuc],
	    [SoLuongThucTreo],
	    [SoLuongThucChay],
	    [DmDonViTinhREF],
	    [DonViTinh],
	    [TypeThucChay],
	    [Link],
	    [GhiChu],
	    [DmHinhThucQuangCaoREF],
	    [TenHinhThucQuangCao],
	    [DmSanPhamREF],
	    [TenSanPham],
	    [InputType],
	    [IsReadBooking],
	    [ThoiGianLog],
	    [NguoiLog],
	    [LoaiLog],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModifiedBy],
	    [LastModifiedAt],
	    [DeletedStatus],
	    [PrintStatus],
	    [RecordStatus]
	    )
	SELECT  [ThucChayHopDongChiTietID],
	    [HopDongREF],
	    [HopDongChiTietREF],
	    [DmBannerREF],
	    [TenBanner],
	    [DmViTriREF],
	    [ViTri],
	    [DmNhanHangREF],
	    [NhanHang],
	    [BookingREF],
	    [ThoiGianBatDau],
	    [ThoiGianKetThuc],
	    [SoLuongThucTreo],
	    [SoLuongThucChay],
	    [DmDonViTinhREF],
	    [DonViTinh],
	    [TypeThucChay],
	    [Link],
	    [GhiChu],
	    [DmHinhThucQuangCaoREF],
	    [TenHinhThucQuangCao],
	    [DmSanPhamREF],
	    [TenSanPham],
	    [InputType],
	    [IsReadBooking],
	    [ThoiGianLog],
	    [NguoiLog],
	    [LoaiLog],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModifiedBy],
	    [LastModifiedAt],
	    [DeletedStatus],
	    [PrintStatus],
	    [RecordStatus] FROM #ThucChayHopDongChiTietLog
		WHERE [STATUS] = 0
	

	--Update huy
	UPDATE dbo.ThucChayHopDongChiTiet
	SET   	LastModifiedBy = ISNULL(T.NguoiLog,''),
	      	LastModifiedAt = ISNULL(T.ThoiGianLog,GETDATE()),
	      	DeletedStatus = 1
	FROM  #ThucChayHopDongChiTietLog t INNER JOIN dbo.ThucChayHopDongChiTiet  dc
	ON t.[ThucChayHopDongChiTietID]  = dc.[ThucChayHopDongChiTietID]
	WHERE t.LoaiLog = 3

END

```
