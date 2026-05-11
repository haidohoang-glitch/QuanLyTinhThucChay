# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_New`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-13 17:55:11.217000
- **Ngày sửa cuối**: 2018-09-13 15:02:26.880000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_New] 	
As 	
DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX)
SET @NgayThucHien = 
(
        SELECT MAX(dchdct.LastModifiedAt)
        FROM   ThucChayHopDongChiTietPR dchdct
    )

SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)
PRINT @NgayThucHien
CREATE TABLE #ThucChayHopDongChiTietPR(
	[ThucChayHopDongChiTietPRID] [int] NOT NULL,
	[HopDongREF] [int] NULL,
	[HopDongChiTietREF] [int] NULL,
	[NhanHang] [nvarchar](255) NULL,
	[TenWebsite] [nvarchar](255) NULL,
	[ChuyenMuc] [nvarchar](255) NULL,
	[TieuDiem] [tinyint] NULL,
	[KhuyenMai] [tinyint] NULL,
	[GiaTien] [BIGINT] NULL,
	[ThoiGianBatDau] [datetime] NULL,
	[Link] [nvarchar](max) NULL,
	[GhiChu] [nvarchar](255) NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedAt] [datetime] NOT NULL,
	[LastModifiedBy] [nvarchar](50) NULL,
	[LastModifiedAt] [datetime] NOT NULL,
	[DeletedStatus] [int] NOT NULL,
	[PrintStatus] [int] NOT NULL,
	[RecordStatus] [int] NOT NULL,
	[DmWebsiteREF] [int] NULL,
	[DmChuyenMucREF] [int] NULL,
	[TenChuyenMuc] [nvarchar](200) NULL,
	[DmNhanHangREF] [int] NULL,
	[DmHinhThucQuangCaoREF] [int] NULL,
	[TenHinhThucQuangCao] [nvarchar](200) NULL,
	[SoLuong] [int] NULL,
	[ChietKhau] [float] NULL,
	[DmViTriREF] [int] NULL,
	[TenViTri] [nvarchar](200) NULL,
	[ThucChayHopDongChiTietPrREF] [int] NULL,
	[DmSanPhamREF] [int] NULL,
	[DmDonViTinhREF] INT NULL,
	STATUS INT
)

SET @SQL = 
    '
SELECT 
	tchdctp.ThucChayHopDongChiTietPRID,
	tchdctp.HopDongREF,
	tchdctp.HopDongChiTietREF,
	tchdctp.NhanHang,
	tchdctp.TenWebsite,
	tchdctp.TenChuyenMuc,
	tchdctp.TieuDiem,
	tchdctp.KhuyenMai,
	tchdctp.GiaTien,
	CASE WHEN CONVERT(NVARCHAR(40),tchdctp.ThoiGianBatDau)<=''1900-01-01'' THEN ''1900-01-01'' ELSE CONVERT(DATETIME,tchdctp.ThoiGianBatDau) END,
	tchdctp.Link,
	tchdctp.GhiChu,
	tchdctp.CreatedBy,
	tchdctp.CreatedAt,
	tchdctp.LastModifiedBy,
	tchdctp.LastModifiedAt,
	tchdctp.DeletedStatus,
	tchdctp.PrintStatus,
	tchdctp.RecordStatus,
	tchdctp.DmWebsiteREF,
	tchdctp.DmChuyenMucREF,
	tchdctp.TenChuyenMuc,
	tchdctp.DmNhanHangREF,
	tchdctp.DmHinhThucQuangCaoREF,
	tchdctp.TenHinhThucQuangCao,
	tchdctp.SoLuong,
	tchdctp.ChietKhau,
	tchdctp.DmViTriREF,
	tchdctp.TenViTri,
	tchdctp.ThucChayHopDongChiTietPrREF,
	tchdctp.DmSanPhamREF,
	tchdctp.DmDonViTinhREF,
	0
FROM OPENQUERY(MYSQL,''CALL Abm_get_hdcn_thucchay_pr (''''' + CONVERT(NVARCHAR(50), @NgayThucHien, 120)
    + ''''');'') tchdctp'

PRINT @SQL
INSERT INTO #ThucChayHopDongChiTietPR
EXECUTE
  (
    @SQL
  )
--DROP TABLE #ThucChayHopDongChiTietPR
   -- Set trang thai = 1 doi voi nhung truong hop sua chua 
    UPDATE #ThucChayHopDongChiTietPR
    SET    [STATUS] = 1
    FROM  #ThucChayHopDongChiTietPR t INNER JOIN ThucChayHopDongChiTietPR  dc
    ON t.ThucChayHopDongChiTietPRID = dc.ThucChayHopDongChiTietPRID
-- Update nhung row da ton ton                                      
   UPDATE [dbo].[ThucChayHopDongChiTietPR]
	    SET    [HopDongREF]                  = A.HopDongREF,
	           [HopDongChiTietREF]           = A.HopDongChiTietREF,
	           [DmWebsiteREF]                = A.DmWebsiteREF,
	           [TenWebsite]                  = A.TenWebsite,
	           [DmChuyenMucREF]              = A.DmChuyenMucREF,
	           [TenChuyenMuc]                = A.TenChuyenMuc,
	           [TieuDiem]                    = A.TieuDiem,
	           [DmNhanHangREF]               = A.DmNhanHangREF,
	           [NhanHang]                    = [dbo].[ReplaceNhanHangDoubleNhay](A.NhanHang),
	           [KhuyenMai]                   = A.KhuyenMai,
	           [GiaTien]                     = A.GiaTien,
	           [ThoiGianBatDau]              = A.ThoiGianBatDau,
	           [Link]                        = A.Link,
	           [GhiChu]                      = A.GhiChu,
	           [DmHinhThucQuangCaoREF]       = A.[DmHinhThucQuangCaoREF],
	           [TenHinhThucQuangCao]         = A.[TenHinhThucQuangCao],
	           [CreatedBy]                   = A.CreatedBy,
	           [CreatedAt]                   = A.CreatedAt,
	           [LastModifiedBy]              = A.LastModifiedBy,
	           [LastModifiedAt]              = A.LastModifiedAt,
	           [PrintStatus]                 = A.PrintStatus,
	           [SoLuong]					 = A.SoLuong,
	           [ChietKhau]					 = A.ChietKhau,
	           [DmViTriREF]					 = A.DmViTriREF,
	           [TenViTri]					 = A.TenViTri,
	           [ThucChayHopDongChiTietPrREF] = A.ThucChayHopDongChiTietPrREF,
	           [DmSanPhamREF]				 = A.DmSanPhamREF,
			   [DmDonViTinhREF]				= A.DmDonViTinhREF
    FROM   #ThucChayHopDongChiTietPR A 
    WHERE  [STATUS] = 1 AND A.ThucChayHopDongChiTietPRID = ThucChayHopDongChiTietPR.ThucChayHopDongChiTietPRID
-- Insert Row chua ton tai
INSERT INTO [dbo].[ThucChayHopDongChiTietPR]
	      (
	        [ThucChayHopDongChiTietPRID],
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
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
	        [SoLuong],
	        [ChietKhau],
            [DmViTriREF],
            [TenViTri],
            [ThucChayHopDongChiTietPrREF],
            [DmSanPhamREF],
			[DmDonViTinhREF]
	      )
SELECT 
			[ThucChayHopDongChiTietPRID],
	        [HopDongREF],
	        [HopDongChiTietREF],
	        [DmWebsiteREF],
	        [TenWebsite],
	        [DmChuyenMucREF],
	        [TenChuyenMuc],
	        [TieuDiem],
	        [DmNhanHangREF],
	        [dbo].[ReplaceNhanHangDoubleNhay]([NhanHang]),
	        [KhuyenMai],
	        [GiaTien],
	        [ThoiGianBatDau],
	        [Link],
	        [GhiChu],
	        [DmHinhThucQuangCaoREF],
	        [TenHinhThucQuangCao],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
	        [SoLuong],
	        [ChietKhau],
            [DmViTriREF],
            [TenViTri],
            [ThucChayHopDongChiTietPrREF],
            [DmSanPhamREF],
			[DmDonViTinhREF]
FROM #ThucChayHopDongChiTietPR   dchdct WHERE dchdct.[STATUS]=0



```
