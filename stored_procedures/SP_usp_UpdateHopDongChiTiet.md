# Stored Procedure: `usp_UpdateHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:08:51.340000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.113000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@NhanHang` | `nvarchar(510)` | No |
| `@DmNhomNganhREF` | `int(4)` | No |
| `@TenNhomNganh` | `nvarchar(100)` | No |
| `@DmLoaiREF` | `int(4)` | No |
| `@TenLoai` | `nvarchar(100)` | No |
| `@DmNhomWebsiteREF` | `int(4)` | No |
| `@TenNhomWebsite` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@DmLoaiBannerREF` | `int(4)` | No |
| `@TenLoaiBanner` | `nvarchar(100)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@TenChuyenMuc` | `nvarchar(200)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |
| `@ThoiGian` | `nvarchar(100)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@GiamGia` | `float(8)` | No |
| `@TiLeTuVan` | `float(8)` | No |
| `@KhuyenMai` | `nvarchar(100)` | No |
| `@IsKhuyenMai` | `int(4)` | No |
| `@ChiPhiTuVan` | `float(8)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_UpdateHopDongChiTiet]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateHopDongChiTiet]
	@HopDongChiTietID int,
	@HopDongFK int,
	@NhanHang nvarchar(255),
	@DmNhomNganhREF int,
	@TenNhomNganh nvarchar(50),
	@DmLoaiREF int,
	@TenLoai nvarchar(50),
	@DmNhomWebsiteREF int,
	@TenNhomWebsite nvarchar(100),
	@DmWebsiteREF int,
	@TenWebsite nvarchar(100),
	@DmSanPhamREF int,
	@TenSanPham nvarchar(100),
	@DmLoaiBannerREF int,
	@TenLoaiBanner nvarchar(50),
	@DmChuyenMucREF int,
	@TenChuyenMuc nvarchar(100),
	@DmViTriREF int,
	@TenViTri nvarchar(50),
	@ThoiGian nvarchar(50),
	@SoLuong int,
	@DonViTinh nvarchar(50),
	@DonGia float,
	@ChietKhau float,
	@GiamGia float,
	@TiLeTuVan float,
	@KhuyenMai nvarchar(50),
	@IsKhuyenMai int,
	@ChiPhiTuVan float,
	@ThanhTien float,
	@GhiChu nvarchar(255),
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[HopDongChiTiet] SET
	[HopDongFK] = @HopDongFK,
	[NhanHang] = @NhanHang,
	[DmNhomNganhREF] = @DmNhomNganhREF,
	[TenNhomNganh] = @TenNhomNganh,
	[DmLoaiREF] = @DmLoaiREF,
	[TenLoai] = @TenLoai,
	[DmNhomWebsiteREF] = @DmNhomWebsiteREF,
	[TenNhomWebsite] = @TenNhomWebsite,
	[DmWebsiteREF] = @DmWebsiteREF,
	[TenWebsite] = @TenWebsite,
	[DmSanPhamREF] = @DmSanPhamREF,
	[TenSanPham] = @TenSanPham,
	[DmLoaiBannerREF] = @DmLoaiBannerREF,
	[TenLoaiBanner] = @TenLoaiBanner,
	[DmChuyenMucREF] = @DmChuyenMucREF,
	[TenChuyenMuc] = @TenChuyenMuc,
	[DmViTriREF] = @DmViTriREF,
	[TenViTri] = @TenViTri,
	[ThoiGian] = @ThoiGian,
	[SoLuong] = @SoLuong,
	[DonViTinh] = @DonViTinh,
	[DonGia] = @DonGia,
	[ChietKhau] = @ChietKhau,
	[GiamGia] = @GiamGia,
	[TiLeTuVan] = @TiLeTuVan,
	[KhuyenMai] = @KhuyenMai,
	[IsKhuyenMai] = @IsKhuyenMai,
	[ChiPhiTuVan] = @ChiPhiTuVan,
	[ThanhTien] = @ThanhTien,
	[GhiChu] = @GhiChu,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[HopDongChiTietID] = @HopDongChiTietID

```
