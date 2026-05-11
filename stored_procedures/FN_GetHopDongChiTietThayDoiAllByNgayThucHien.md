# Function: `GetHopDongChiTietThayDoiAllByNgayThucHien`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-06-07 11:22:21.930000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[GetHopDongChiTietThayDoiAllByNgayThucHien]
(	
	@NgayThucHien datetime,
	@HopDongChiTietID int
)
RETURNS 
@HopDongChiTiet TABLE (
	 NgayThayDoi DATETIME,
	[HopDongChiTietID] [int] NOT NULL,
	[HopDongFK] [int] NOT NULL,
	[NhanHang] [nvarchar](255) NULL,
	[DmNhomNganhREF] [int] NULL,
	[TenNhomNganh] [nvarchar](50) NULL,
	[DmLoaiREF] [int] NULL,
	[TenLoai] [nvarchar](50) NULL,
	[DmNhomWebsiteREF] [int] NULL,
	[TenNhomWebsite] [nvarchar](100) NULL,
	[DmWebsiteREF] [int] NULL,
	[TenWebsite] [nvarchar](100) NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](100) NULL,
	[DmLoaiBannerREF] [int] NULL,
	[TenLoaiBanner] [nvarchar](50) NULL,
	[DmChuyenMucREF] [int] NULL,
	[TenChuyenMuc] [nvarchar](100) NULL,
	[DmViTriREF] [int] NULL,
	[TenViTri] [nvarchar](50) NULL,
	[ThoiGian] [nvarchar](50) NULL,
	[SoLuong] [int] NULL,
	[DonViTinh] [nvarchar](50) NULL,
	[DonGia] [float] NULL,
	[ChietKhau] [float] NULL,
	[GiamGia] [float] NULL,
	[TiLeTuVan] [float] NULL,
	[KhuyenMai] [nvarchar](50) NULL,
	[IsKhuyenMai] [int] NULL,
	[ChiPhiTuVan] [float] NULL,
	[ThanhTien] [float] NULL,
	[GhiChu] [nvarchar](255) NULL,
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
	
	INSERT INTO @HopDongChiTiet	 					
							SELECT Top 1 A.* 
							FROM dbo.HopDongChiTietAllTemp A
							INNER JOIN dbo.HopDong B ON A.HopDongFK = B.HopDongID
							WHERE 
							A.DeletedStatus <> 1 AND 
							B.DeletedStatus <> 1 AND
							[HopDongChiTietID] = @HopDongChiTietID AND
							NgayThayDoi <= @NgayThucHien 
							Order by NgayThayDoi Desc


	
	return 
End

```
