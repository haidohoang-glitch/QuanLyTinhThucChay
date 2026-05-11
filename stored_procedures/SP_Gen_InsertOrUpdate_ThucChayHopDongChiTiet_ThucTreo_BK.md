# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreo_BK`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-10-27 14:54:53.363000
- **Ngày sửa cuối**: 2021-10-27 14:54:53.363000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreo] 
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet_ThucTreo_BK] 	
As 	
BEGIN
    --SELECT TOP 10 * INTO ThucChayHopDongChiTiet FROM dbo.ThucChayHopDongChiTiet t
	--WHERE t.CreatedAt >= '2019-01-01'

DECLARE @NgayThucHien DATETIME
DECLARE @SQL NVARCHAR(MAX)
SET @NgayThucHien = 
	(
        SELECT MAX(dchdct.LastModifiedAt)
        FROM   dbo.ThucChayHopDongChiTiet dchdct
		WHERE ISNULL(loaiThucTreo ,'') = ''
    )

SET @NgayThucHien = DATEADD(HOUR,-100,@NgayThucHien)
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
	[LoaiThucTreo] NVARCHAR(50),
	[STATUS]   SMALLINT
) 


INSERT INTO #ThucChayHopDongChiTiet
(
    ThucChayHopDongChiTietID,
    HopDongREF,
    NhanHang,
    ThoiGianBatDau,
    ThoiGianKetThuc,
    Link,
    DmBannerREF,
    TenBanner,
    ViTri,
    GhiChu,
    BookingREF,
    HopDongChiTietREF,
    TypeThucChay,
    CreatedBy,
    CreatedAt,
    LastModifiedBy,
    LastModifiedAt,
    DeletedStatus,
    PrintStatus,
    RecordStatus,
    DmViTriREF,
    DmNhanHangREF,
    SoLuongThucTreo,
    SoLuongThucChay,
    DmDonViTinhREF,
    DonViTinh,
    DmHinhThucQuangCaoREF,
    TenHinhThucQuangCao,
    DmSanPhamREF,
    TenSanPham,
    InputType,
    IsReadBooking,
    KichThuoc,
    DonGia,
    ChietKhau,
    ThanhTien,
    LoaiThucTreo,
    STATUS
)
	SELECT   tt.Id,
			 tt.Contract_Id,
			 tt.TenNhanHang,
			 IIF(tt.ThoiGianBatDau = '0001-01-01','2010-01-01',IIF(tt.ThoiGianBatDau IS NULL, '2010-01-01',tt.ThoiGianBatDau))ThoiGianBatDau,
			 IIF(tt.ThoiGianKetThuc = '0001-01-01','2010-01-01',IIF(tt.ThoiGianKetThuc IS NULL, '2010-01-01',tt.ThoiGianKetThuc))ThoiGianKetThuc,
			 tt.Link,
			 tt.Banner_Id,
			 tt.TenBanner,
			 tt.Zone_Name,
			 tt.GhiChu,
			 tt.Booking_Id,
			 tt.Contract_Detail_Id,
			 tt.typethucchay,
			 tt.Created_By,
			 ISNULL(tt.Created_At,tt.Last_Modified_At)Created_At,
			 tt.Last_Modified_By,
             tt.Last_Modified_At,
             tt.Deleted_Status,
			 0 AS Prinstatus,
			 0 AS RecordStatus,
			 0 Zone_Id,
             tt.Dm_NhanHang_Id,
			 tt.SoLuong AS SoLuongTreo,
			 tt.SoLuong AS SoLuongChay,
			 tt.DonViTinh_Id,
			 '' DonViTinh,
			 tt.Product_Formality_Id,
			 ISNULL((SELECT TOP 1 t.TenHinhThucQuangCao FROM dbo.DmHinhThucQuangCao t WHERE t.DmHinhThucQuangCaoID = tt.Product_Formality_Id ORDER BY t.DmHinhThucQuangCaoID),'') TenHinhThucQuangCao,
			 tt.Product_Id,
			 '' Product_name,
			 1 as InputType, --thuc treo
			 tt.Is_ReadBooking,
			 tt.Banner_size,
			 tt.DonGia,
			 tt.ChietKhau,
             tt.ThanhTien,
			 '' LoaiThucTreo,
             0 AS [Status] 
			 FROM [192.168.23.150].[ThucTreo].dbo.ThucTreo tt
			WHERE tt.Last_Modified_At >= @NgayThucHien




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
				   [ThanhTien]			       = A.ThanhTien,
				   [DeletedStatus]			   = A.DeletedStatus
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
				[ThanhTien] ,
				[LoaiThucTreo]
			  )
	SELECT 
				[dchdct].[ThucChayHopDongChiTietID],
				[dchdct].[HopDongREF],
				[dchdct].[HopDongChiTietREF],
				[dchdct].[DmBannerREF],
				[dchdct].[TenBanner],
				[dchdct].[DmViTriREF],
				[dchdct].[ViTri],
				[dchdct].[DmNhanHangREF],
				[dbo].[ReplaceNhanHangDoubleNhay]([dchdct].[NhanHang]),
				[dchdct].[BookingREF],
				[dchdct].[ThoiGianBatDau],
				[dchdct].[ThoiGianKetThuc],
				[dchdct].[SoLuongThucTreo],
				[dchdct].[SoLuongThucChay],
				[dchdct].[DmDonViTinhREF],
				[dchdct].[DonViTinh],
				[dchdct].[TypeThucChay],
				[dchdct].[Link],
				[dchdct].[GhiChu],
				[dchdct].[DmHinhThucQuangCaoREF],
				[dchdct].[TenHinhThucQuangCao],
				[dchdct].[DmSanPhamREF],
				[dchdct].[TenSanPham],
				[dchdct].[InputType],
				[dchdct].[IsReadBooking],
				[dchdct].[CreatedBy],
				[dchdct].[CreatedAt],
				[dchdct].[LastModifiedBy],
				[dchdct].[LastModifiedAt],
				[dchdct].[DeletedStatus],
				[dchdct].[PrintStatus],
				[dchdct].[RecordStatus],
				[dchdct].[KichThuoc],
				[dchdct].[DonGia] ,
				[dchdct].[ChietKhau] , 
				[dchdct].[ThanhTien] ,
				[dchdct].[LoaiThucTreo]
	FROM #ThucChayHopDongChiTiet dchdct WHERE dchdct.[STATUS]=0

	DROP TABLE #ThucChayHopDongChiTiet

END

```
