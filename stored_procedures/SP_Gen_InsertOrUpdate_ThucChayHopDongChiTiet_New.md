# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTiet_New`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-13 17:37:33.997000
- **Ngày sửa cuối**: 2018-10-30 10:43:58.183000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_New] 
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_New] 	

As 	

DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX)
SET @NgayThucHien = 
	(
        SELECT MAX(dchdct.LastModifiedAt)
        FROM   dbo.ThucChayHopDongChiTiet dchdct
		WHERE dchdct.DeletedStatus <> 1
    )

SET @NgayThucHien = DATEADD(HOUR,-8,@NgayThucHien)
--SET @NgayThucHien = '2009-01-01'
PRINT @NgayThucHien
CREATE TABLE #ThucChayHopDongChiTiet(
	[ThucChayHopDongChiTietID] [int] NOT NULL,
	[HopDongREF] [int] NULL,
	[NhanHang] [nvarchar](500) NULL,
	[ThoiGianBatDau] [datetime] NULL,
	[ThoiGianKetThuc] [datetime] NULL,
	[Link] [nvarchar](2000) NULL,
	[DmBannerREF] [nvarchar](255) NULL,
	[TenBanner] [nvarchar](255) NULL,
	[ViTri] [nvarchar](255) NULL,
	[GhiChu] [nvarchar](2555) NULL,
	[BookingREF] [int] NULL,
	[HopDongChiTietREF] [int] NULL,
	[TypeThucChay] [int] NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedAt] [datetime] NOT NULL,
	[LastModifiedBy] [nvarchar](50) NULL,
	[LastModifiedAt] [datetime] NOT NULL,
	[DeletedStatus] [int] NOT NULL,
	[PrintStatus] [int] NOT NULL,
	[RecordStatus] [int] NOT NULL,
	[DmViTriREF] [int] NULL,
	[DmNhanHangREF] [nvarchar](200) NULL,
	[SoLuongThucTreo] [float] NULL,
	[SoLuongThucChay] [float] NULL,
	[DmDonViTinhREF] [bigint] NULL,
	[DonViTinh] [nvarchar](200) NULL,
	[DmHinhThucQuangCaoREF] [int] NULL,
	[TenHinhThucQuangCao] [nvarchar](200) NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](200) NULL,
	[InputType] [int] NULL,
	[IsReadBooking] [int] NULL,
	[KichThuoc]	 [nvarchar](200) NULL,
	[DonGia] FLOAT NULL,
	[ChietKhau] FLOAT NULL, 
	[ThanhTien]  FLOAT NULL,
	[STATUS]   SMALLINT
) 
SET @SQL = 
    '
SELECT 
	tchdct.ThucChayHopDongChiTietID,
	tchdct.HopDongREF,
	tchdct.NhanHang,
	
	CASE WHEN CONVERT(NVARCHAR(40),tchdct.ThoiGianBatDau)<=''1900-01-01'' THEN ''1900-01-01'' ELSE CONVERT(DATETIME,ThoiGianBatDau) END,
	CASE WHEN CONVERT(NVARCHAR(40),tchdct.ThoiGianKetThuc)=''0001-01-01 00:00:00.0000000'' THEN ''9999-01-01'' ELSE CONVERT(DATETIME,ThoiGianKetThuc) END,
	tchdct.Link,
	tchdct.DmBannerREF,
	tchdct.TenBanner,
	tchdct.ViTri,
	tchdct.GhiChu,
	tchdct.BookingREF,
	tchdct.HopDongChiTietREF,
	tchdct.TypeThucChay,
	tchdct.CreatedBy,
	CONVERT(DATETIME,tchdct.CreatedAt) ,
	tchdct.LastModifiedBy,
	CONVERT(DATETIME,LastModifiedAt) ,
	tchdct.DeletedStatus,
	tchdct.PrintStatus,
	tchdct.RecordStatus,
	tchdct.DmViTriREF,
	tchdct.DmNhanHangREF,
	tchdct.SoLuongThucTreo,
	tchdct.SoLuongThucChay,
	tchdct.DmDonViTinhREF,
	tchdct.DonViTinh,
	tchdct.DmHinhThucQuangCaoREF,
	tchdct.TenHinhThucQuangCao,
	tchdct.DmSanPhamREF,
	tchdct.TenSanPham,
	tchdct.InputType,
	tchdct.IsReadBooking,
	tchdct.KichThuoc,
	tchdct.DonGia,
	tchdct.ChietKhau, 
	tchdct.ThanhTien,
	0
FROM OPENQUERY(MySQL,''CALL Abm_get_hdcn_thucchay (''''' + CONVERT(NVARCHAR(50), @NgayThucHien, 120)
    + ''''');'') tchdct
	
	'

PRINT @SQL
INSERT INTO #ThucChayHopDongChiTiet
EXECUTE
  (
    @SQL
  )

  --SELECT * FROM #ThucChayHopDongChiTiet
  --WHERE ThucChayHopDongChiTietID = 104203

--SELECT * FROM #DmSanPham
   -- Set trang thai = 1 doi voi nhung truong hop sua chua 
	--SET @NhanHang =  [dbo].[ReplaceNhanHangDoubleNhay](@NhanHang)
    UPDATE #ThucChayHopDongChiTiet 
    SET    [STATUS] = 1
    FROM  #ThucChayHopDongChiTiet t INNER JOIN dbo.ThucChayHopDongChiTiet dc
    ON t.ThucChayHopDongChiTietID = dc.ThucChayHopDongChiTietID
-- Update nhung row da ton ton                                      
   UPDATE [dbo].[ThucChayHopDongChiTiet]
	    SET    [HopDongREF]                = A.HopDongREF,
	           [HopDongChiTietREF]         = A.HopDongChiTietREF,
	           [DmBannerREF]               = A.DmBannerREF,
	           [TenBanner]                 = A.TenBanner,
	           [DmViTriREF]                = A.DmViTriREF,
	           [ViTri]                     = A.ViTri,
	           [DmNhanHangREF]             = A.DmNhanHangREF,
	           [NhanHang]                  = [dbo].[ReplaceNhanHangDoubleNhay](A.NhanHang),
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
	           [CreatedBy]                 = A.CreatedBy,
	           [CreatedAt]                 = A.CreatedAt,
	           [LastModifiedBy]            = A.LastModifiedBy,
	           [LastModifiedAt]            = A.LastModifiedAt,
			   [KichThuoc]				   = A.KichThuoc,
			   [DonGia]					   = A.DonGia,
			   [ChietKhau]				   = A.ChietKhau, 
			   [ThanhTien]			       = A.ThanhTien
    FROM   #ThucChayHopDongChiTiet A 
    WHERE  [STATUS] = 1 AND A.ThucChayHopDongChiTietID=ThucChayHopDongChiTiet.ThucChayHopDongChiTietID
-- Insert Row chua ton tai
INSERT INTO [dbo].[ThucChayHopDongChiTiet]
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
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
			[KichThuoc],
			[DonGia] ,
			[ChietKhau] , 
			[ThanhTien] 
	      )
SELECT 
			[ThucChayHopDongChiTietID],
	        [HopDongREF],
	        [HopDongChiTietREF],
	        [DmBannerREF],
	        [TenBanner],
	        [DmViTriREF],
	        [ViTri],
	        [DmNhanHangREF],
	        [dbo].[ReplaceNhanHangDoubleNhay]([NhanHang]),
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
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
			[KichThuoc],
			[DonGia] ,
			[ChietKhau] , 
			[ThanhTien] 
FROM #ThucChayHopDongChiTiet dchdct WHERE dchdct.[STATUS]=0

DROP TABLE #ThucChayHopDongChiTiet


```
