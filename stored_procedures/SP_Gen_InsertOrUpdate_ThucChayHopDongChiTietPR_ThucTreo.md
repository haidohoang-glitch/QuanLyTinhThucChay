# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_ThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-03 12:00:41.010000
- **Ngày sửa cuối**: 2024-10-29 10:07:14.417000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_ThucTreo]
*/

CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietPR_ThucTreo] 	
As 	
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SQL NVARCHAR(MAX), @SQL_UPDATE NVARCHAR(MAX),@server_id nvarchar(100) = '', @database nvarchar(100) = '', @daunhay nvarchar(10) = ''''

	SET @server_id =
	(SELECT TOP (1) (SERVER_ID) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCTREO' ORDER BY id)

	SET @database= 
	(SELECT TOP (1) (DATA_NAME) FROM dbo.Cau_hinh_linkserver WHERE deletedstatus = 0 AND GROUP_INPUT = N'THUCTREO' ORDER BY id)

	SET @NgayThucHien = 
	ISNULL((
			SELECT MAX(dchdct.LastModifiedAt)
			FROM   dbo.ThucChayHopDongChiTietPR dchdct
		),'1900-01-01')

	SET @NgayThucHien = DATEADD(HOUR,-30,@NgayThucHien)

	PRINT @NgayThucHien
	--SET @NgayThucHien = '2021-09-01'
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
		[parent_id] INT NULL,
		[chuyenmuccms_id] INT NULL,
		STATUS INT
	)

	SET @SQL =
	'INSERT INTO #ThucChayHopDongChiTietPR
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
		[parent_id],
		[chuyenmuccms_id],
		STATUS
	) '

	SET @SQL +=
	'SELECT id,
		   Contract_Id,
		   Contract_Detail_Id,
		   TenNhanHang,
		   Ten_Website,
		   TenChuyenMuc,
		   TieuDiem,
		   KhuyenMai,
		   DonGia,
		   --CAST(CONVERT(VARCHAR(100), (IIF(ThoiGianBatDau = '+ @daunhay + '0001-01-01' + @daunhay +',' + @daunhay +'1900-01-01' + @daunhay + ',ThoiGianBatDau)), 102) AS DATETIME) ThoiGianBatDau ,
		   IIF(ThoiGianBatDau IS NULL,'+ @daunhay + '1900-01-01' + @daunhay +', ThoiGianBatDau) as ThoiGianBatDau,
		   Link,
		   GhiChu,
		   IIF(Created_By IS NULL,'''',Created_By) Created_By,
		   IIF(Created_At IS NULL,'+ @daunhay + '1900-01-01' + @daunhay +', Created_At) Created_At,
		   Last_Modified_By,
		   IIF(Last_Modified_At IS NULL,'+ @daunhay + '1900-01-01' + @daunhay +',Last_Modified_At) Last_Modified_At,
		   Deleted_Status,
		   0 AS PrintStatus,
		   0 AS RecorsStatus,
		   Website_id,
		   NhanHang_Id,
		   Product_Formality_Id,
		   '''' TenHinhThucQuangCao,
		   SoLuong,
		   ChietKhau,
		   0 DmViTriREF,
		   ViTri,
		   Parent_id,
		   Product_Id,
		   DonViTinh_Id, 
		   [parent_id],
		   [chuyenmuccms_id],
		   0 Status_syn
	 FROM  ' + @server_id + '.' + @database + '.dbo.ThucTreo_PR
	 WHERE Last_Modified_At >= ' + @daunhay + convert(nvarchar(23),@ngaythuchien,121)+ @daunhay+' '

	PRINT @SQL
	EXEC(@SQL)	
	-- Set trang thai = 1 doi voi nhung truong hop sua chua 
	UPDATE #ThucChayHopDongChiTietPR
	SET    [STATUS] = 1
	FROM  #ThucChayHopDongChiTietPR t INNER JOIN dbo.ThucChayHopDongChiTietPR  dc
	ON t.ThucChayHopDongChiTietPRID = dc.ThucChayHopDongChiTietPRID

	--UPDATE LAI THONG TIN CHUYEN MỤC CHO DANG CHI PHI
	SET @SQL_UPDATE =
	'UPDATE t
	SET t.Chuyenmuc = ISNULL((select top (1) tr.tenchuyenmuc FROM ' + @server_id + '.' + @database + '.dbo.ThucTreo_PR tr 
								where tr.id = t.parent_id
								order by tr.id),''''),
		t.Chuyenmuccms_id = ISNULL((select top (1) tr.Chuyenmuccms_id FROM ' + @server_id + '.' + @database + '.dbo.ThucTreo_PR tr 
								where tr.id = t.parent_id
								order by tr.id),0)
	FROM  #ThucChayHopDongChiTietPR t INNER JOIN dbo.ThucChayHopDongChiTietPR  dc
	ON t.ThucChayHopDongChiTietPRID = dc.ThucChayHopDongChiTietPRID
	WHERE t.Chuyenmuc = N''''
	AND t.parent_id <> 0'

	--PRINT @SQL_UPDATE
	EXEC(@SQL_UPDATE)	

	-- Update nhung row da ton ton                                      
	UPDATE T
		SET    T.[HopDongREF]                  = A.HopDongREF,
		        T.[HopDongChiTietREF]           = A.HopDongChiTietREF,
		        T.[DmWebsiteREF]                = A.DmWebsiteREF,
		        T.[TenWebsite]                  = A.TenWebsite,
		        T.[DmChuyenMucREF]              = A.DmChuyenMucREF,
		        T.ChuyenMuc		               = A.ChuyenMuc,
				T.TenChuyenMuc				   = A.ChuyenMuc,
		        T.[TieuDiem]                    = A.TieuDiem,
		        T.[DmNhanHangREF]               = A.DmNhanHangREF,
		        T.[NhanHang]                    = [dbo].[ReplaceNhanHangDoubleNhay](A.NhanHang),
		        T.[KhuyenMai]                   = ISNULL(A.KhuyenMai,0),
		        T.[GiaTien]                     = A.GiaTien,
		        T.[ThoiGianBatDau]              = A.ThoiGianBatDau,
		        T.[Link]                        = A.Link,
		        T.[GhiChu]                      = A.GhiChu,
		        T.[DmHinhThucQuangCaoREF]       = A.[DmHinhThucQuangCaoREF],
		        T.[TenHinhThucQuangCao]         = A.[TenHinhThucQuangCao],
		        T.[CreatedBy]                   = A.CreatedBy,
		        T.[CreatedAt]                   = A.CreatedAt,
		        T.[LastModifiedBy]              = A.LastModifiedBy,
		        T.[LastModifiedAt]              = A.LastModifiedAt,
				T.[DeletedStatus]				 = A.DeletedStatus,
		        T.[PrintStatus]                 = A.PrintStatus,
		        T.[SoLuong]					 = A.SoLuong,
		        T.[ChietKhau]					 = A.ChietKhau,
		        T.[DmViTriREF]					 = A.DmViTriREF,
		        T.[TenViTri]					 = A.TenViTri,
		        T.[ThucChayHopDongChiTietPrREF] = A.ThucChayHopDongChiTietPrREF,
		        T.[DmSanPhamREF]				 = A.DmSanPhamREF,
				T.[DmDonViTinhREF]				= A.DmDonViTinhREF,
				T.[parent_id]					= A.[parent_id],
				T.[chuyenmuccms_id]			= A.[chuyenmuccms_id]
	FROM  [dbo].[ThucChayHopDongChiTietPR] T 
	INNER JOIN #ThucChayHopDongChiTietPR A ON A.ThucChayHopDongChiTietPRID = T.ThucChayHopDongChiTietPRID
	WHERE  A.[STATUS] = 1

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
				[DmDonViTinhREF],
				[parent_id],
				[chuyenmuccms_id]
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
		        ISNULL([KhuyenMai],0),
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
				[DmDonViTinhREF],
				[parent_id],
				[chuyenmuccms_id]
	FROM #ThucChayHopDongChiTietPR   dchdct WHERE dchdct.[STATUS]=0
END


```
