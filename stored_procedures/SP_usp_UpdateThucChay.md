# Stored Procedure: `usp_UpdateThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:08:33.627000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayID` | `int(4)` | No |
| `@SoHopDong` | `int(4)` | No |
| `@DanhsachDmBookingREF` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(510)` | No |
| `@DmNhomWebsiteREF` | `int(4)` | No |
| `@TenNhomWebsite` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(510)` | No |
| `@DmChienDichREF` | `int(4)` | No |
| `@TenChienDich` | `nvarchar(510)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@TenBanner` | `nvarchar(512)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateThucChay]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateThucChay]
	@ThucChayID int,
	@SoHopDong int,
	@DanhsachDmBookingREF nvarchar(100),
	@DmSanPhamREF int,
	@TenSanPham nvarchar(255),
	@DmNhomWebsiteREF int,
	@TenNhomWebsite int,
	@DmWebsiteREF int,
	@TenWebsite nvarchar(255),
	@DmChienDichREF int,
	@TenChienDich nvarchar(255),
	@DmBannerREF int,
	@TenBanner nvarchar(256),
	@NgayThucHien datetime,
	@TongViewThucChay float,
	@TongClickThucChay float,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[ThucChay] SET
	[SoHopDong] = @SoHopDong,
	[DanhsachDmBookingREF] = @DanhsachDmBookingREF,
	[DmSanPhamREF] = @DmSanPhamREF,
	[TenSanPham] = @TenSanPham,
	[DmNhomWebsiteREF] = @DmNhomWebsiteREF,
	[TenNhomWebsite] = @TenNhomWebsite,
	[DmWebsiteREF] = @DmWebsiteREF,
	[TenWebsite] = @TenWebsite,
	[DmChienDichREF] = @DmChienDichREF,
	[TenChienDich] = @TenChienDich,
	[DmBannerREF] = @DmBannerREF,
	[TenBanner] = @TenBanner,
	[NgayThucHien] = @NgayThucHien,
	[TongViewThucChay] = @TongViewThucChay,
	[TongClickThucChay] = @TongClickThucChay,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[ThucChayID] = @ThucChayID

```
