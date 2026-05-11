# Function: `GetDistinctHopDongChiTietThayDoi`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-06-04 11:00:17.153000
- **Ngày sửa cuối**: 2016-08-18 19:16:38.227000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[GetDistinctHopDongChiTietThayDoi]
(	

)
RETURNS 
@HopDongChiTiet TABLE (
	 NgayThayDoi DATETIME,
	[HopDongChiTietID] [int] NOT NULL,
	[HopDongFK] [int] NOT NULL,
	[NhanHang] [nvarchar](500) NULL,
	[DmNhomNganhREF] [int] NULL,
	[TenNhomNganh] [nvarchar](500) NULL,
	[DmLoaiREF] [int] NULL,
	[TenLoai] [nvarchar](500) NULL,
	[DmNhomWebsiteREF] [int] NULL,
	[TenNhomWebsite] [nvarchar](500) NULL,
	[DmWebsiteREF] [int] NULL,
	[TenWebsite] [nvarchar](500) NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](500) NULL,
	[DmLoaiBannerREF] [int] NULL,
	[TenLoaiBanner] [nvarchar](500) NULL,
	[DmChuyenMucREF] [int] NULL,
	[TenChuyenMuc] [nvarchar](500) NULL,
	[DmViTriREF] [int] NULL,
	[TenViTri] [nvarchar](500) NULL,
	[ThoiGian] [nvarchar](50) NULL,
	[SoLuong] [int] NULL,
	[DonViTinh] [nvarchar](500) NULL,
	[DonGia] [float] NULL,
	[ChietKhau] [float] NULL,
	[GiamGia] [float] NULL,
	[TiLeTuVan] [float] NULL,
	[KhuyenMai] [nvarchar](50) NULL,
	[IsKhuyenMai] [int] NULL,
	[ChiPhiTuVan] [float] NULL,
	[ThanhTien] [float] NULL,
	[GhiChu] [nvarchar](500) NULL,
	[CreatedBy] [nvarchar](50) NULL,
	[CreatedAt] [datetime] NOT NULL,
	[LastModifiedBy] [nvarchar](50) NULL,
	[LastModifiedAt] [datetime] NOT NULL,
	[DeletedStatus] [int] NOT NULL,
	[PrintStatus] [int] NOT NULL,
	[RecordStatus] [int] NOT NULL
	)
AS
BEGIN

DECLARE @TableTemp TABLE
(
	NgayThayDoi DATETIME,
	HopDongChiTietID nvarchar(50),
	HopDongFK  NVARCHAR(50)
)

DECLARE @NgayThayDoi NVARCHAR(50), @HopDongChiTietREF NVARCHAR(50), @HopDongFK NVARCHAR(50)

DECLARE Record_Cursor CURSOR FOR 
	SELECT 
	DISTINCT 
	convert(VARCHAR(50), B.NgayThayDoi, 103),
	A.HopDongChiTietREF ,
	A.HopDongFK 
	FROM dbo.HopDongChiTietThayDoi A 
	INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
	WHERE A.DeletedStatus <> 1 AND B.DeletedStatus <> 1
	
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into 
		@NgayThayDoi,
		@HopDongChiTietREF
		,
		@HopDongFK
		
WHILE @@FETCH_STATUS = 0
	BEGIN

	INSERT INTO @HopDongChiTiet 
	SELECT 
		TOP 1
		B.NgayThayDoi AS NgayThayDoi,
		A.HopDongChiTietREF AS  HopDongChiTietID ,
		A.HopDongFK  ,
		ISNULL(A.NhanHang,'') ,
		A.DmNhomNganhREF ,
		ISNULL(A.TenNhomNganh,'') ,
		A.DmLoaiREF ,
		ISNULL(A.TenLoai,'') ,
		ISNULL(A.DmNhomWebsiteREF,'') ,
		ISNULL(A.TenNhomWebsite,'') ,
		A.DmWebsiteREF ,
		A.TenWebsite ,
		A.DmSanPhamREF ,
		A.TenSanPham ,
		A.DmLoaiBannerREF ,
		A.TenLoaiBanner ,
		A.DmChuyenMucREF ,
		A.TenChuyenMuc ,
		A.DmViTriREF ,
		A.TenViTri ,
		A.ThoiGian ,
		A.SoLuong ,
		A.DonViTinh ,
		A.DonGia ,
		A.ChietKhau ,
		A.GiamGia ,
		A.TiLeTuVan ,
		A.KhuyenMai ,
		A.IsKhuyenMai ,
		A.ChiPhiTuVan ,
		A.ThanhTien ,
		A.GhiChu ,
		A.CreatedBy ,
		A.CreatedAt  ,
		A.LastModifiedBy ,
		A.LastModifiedAt  ,
		A.DeletedStatus  ,
		A.PrintStatus  ,
		A.RecordStatus  

	FROM dbo.HopDongChiTietThayDoi A 
	INNER JOIN dbo.HopDongThayDoi B ON A.HopDongFK = B.HopDongFK
	WHERE 
	A.DeletedStatus <> 1 AND 
	B.DeletedStatus <> 1 AND 
	convert(VARCHAR(50), B.NgayThayDoi, 103) = @NgayThayDoi AND
	A.HopDongChiTietREF = @HopDongChiTietREF 
	AND 
	A.HopDongFK = @HopDongFK
	ORDER BY B.NgayThayDoi DESC 


	FETCH NEXT FROM Record_Cursor into 
			@NgayThayDoi,
			@HopDongChiTietREF,
			@HopDongFK
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

	return 
End


--select * from [dbo].[GetDistinctHopDongChiTietThayDoi]()
```
