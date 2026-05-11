# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_ThucTreo_asd14`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-08-31 10:53:49.903000
- **Ngày sửa cuối**: 2021-08-31 10:53:49.903000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_ThucTreo_asd14]
*/

create PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_ThucTreo_asd14] 	
As 	
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX)
	SET @NgayThucHien = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   dbo.ThucChayHopDongChiTietPR dchdct
		),'1900-01-01')

	SET @NgayThucHien = DATEADD(HOUR,-30,@NgayThucHien)

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
		[ThoiGianBatDau] DATETIME NULL,
		[Link] [nvarchar](max) NULL,
		[GhiChu] [nvarchar](255) NULL,
		[CreatedBy] [nvarchar](50) NULL,
		[CreatedAt] [datetime]  NULL,
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


	INSERT INTO #ThucChayHopDongChiTietPR
	(
		ThucChayHopDongChiTietPRID,
		HopDongREF,
		HopDongChiTietREF,
		NhanHang,
		TenWebsite,
		ChuyenMuc,
		TieuDiem,
		KhuyenMai,
		GiaTien,
		ThoiGianBatDau,
		Link,
		GhiChu,
		CreatedBy,
		CreatedAt,
		LastModifiedBy,
		LastModifiedAt,
		DeletedStatus,
		PrintStatus,
		RecordStatus,
		DmWebsiteREF,
		DmNhanHangREF,
		DmHinhThucQuangCaoREF,
		TenHinhThucQuangCao,
		SoLuong,
		ChietKhau,
		DmViTriREF,
		TenViTri,
		ThucChayHopDongChiTietPrREF,
		DmSanPhamREF,
		DmDonViTinhREF,
		STATUS
	)

	SELECT id,
		   Contract_Id,
		   Contract_Detail_Id,
		   TenNhanHang,
		   Ten_Website,
		   TenChuyenMuc,
		   TieuDiem,
		   KhuyenMai,
		   DonGia,
		   --CAST(CONVERT(VARCHAR(100), (IIF(ThoiGianBatDau = '0001.01.01','1900-01-01',ThoiGianBatDau)), 102) AS DATETIME) ThoiGianBatDau ,
		   IIF(ThoiGianBatDau IS NULL,'1900-01-01', ThoiGianBatDau) as ThoiGianBatDau,
		   Link,
		   GhiChu,
		   IIF(Created_By IS NULL,'',Created_By) Created_By,
		   IIF(Created_At IS NULL,'1900-01-01', Created_At) Created_At,
		   Last_Modified_By,
		   IIF(Last_Modified_At IS NULL,'1900-01-01',Last_Modified_At) Last_Modified_At,
		   Deleted_Status,
		   0 AS PrintStatus,
		   0 AS RecorsStatus,
		   Website_id,
		   NhanHang_Id,
		   Product_Formality_Id,
		   '' TenHinhThucQuangCao,
		   SoLuong,
		   ChietKhau,
		   0 DmViTriREF,
		   ViTri,
		   Parent_id,
		   Product_Id,
		   DonViTinh_Id, 
		   0 Status_syn
	 FROM asd14.ThucTreo.dbo.ThucTreo_PR
	 WHERE Last_Modified_At >= @NgayThucHien

	 --SELECT * FROM #ThucChayHopDongChiTietPR

	--DROP TABLE #ThucChayHopDongChiTietPR
	   -- Set trang thai = 1 doi voi nhung truong hop sua chua 
	    UPDATE #ThucChayHopDongChiTietPR
	    SET    [STATUS] = 1
	    FROM  #ThucChayHopDongChiTietPR t INNER JOIN dbo.ThucChayHopDongChiTietPR  dc
	    ON t.ThucChayHopDongChiTietPRID = dc.ThucChayHopDongChiTietPRID

	-- Update nhung row da ton ton                                      
	   UPDATE [dbo].[ThucChayHopDongChiTietPR]
		    SET    [HopDongREF]                  = A.HopDongREF,
		           [HopDongChiTietREF]           = A.HopDongChiTietREF,
		           [DmWebsiteREF]                = A.DmWebsiteREF,
		           [TenWebsite]                  = A.TenWebsite,
		           [DmChuyenMucREF]              = A.DmChuyenMucREF,
		           ChuyenMuc		             = A.ChuyenMuc,
				   TenChuyenMuc					 = A.ChuyenMuc,
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
				   [DeletedStatus]				 = A.DeletedStatus,
		           [PrintStatus]                 = A.PrintStatus,
		           [SoLuong]					 = A.SoLuong,
		           [ChietKhau]					 = A.ChietKhau,
		           [DmViTriREF]					 = A.DmViTriREF,
		           [TenViTri]					 = A.TenViTri,
		           [ThucChayHopDongChiTietPrREF] = A.ThucChayHopDongChiTietPrREF,
		           [DmSanPhamREF]				 = A.DmSanPhamREF,
				   [DmDonViTinhREF]				= A.DmDonViTinhREF
	    FROM   #ThucChayHopDongChiTietPR A 
	    WHERE  [STATUS] = 1 AND A.ThucChayHopDongChiTietPRID = dbo.ThucChayHopDongChiTietPR.ThucChayHopDongChiTietPRID
	-- Insert Row chua ton tai
	INSERT INTO [dbo].[ThucChayHopDongChiTietPR]
		      (
		        [ThucChayHopDongChiTietPRID],
		        [HopDongREF],
		        [HopDongChiTietREF],
		        [DmWebsiteREF],
		        [TenWebsite],
		        [DmChuyenMucREF],
		        ChuyenMuc,
				TenChuyenMuc,
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
		        ChuyenMuc,
				ChuyenMuc,
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
END


```
