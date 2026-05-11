# Stored Procedure: `usp_UpdateThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:06:52.170000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(510)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@Link` | `nvarchar(2)` | No |
| `@DmBannerREF` | `nvarchar(510)` | No |
| `@TenBanner` | `nvarchar(510)` | No |
| `@ViTri` | `nvarchar(510)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@BookingREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@TypeThucChay` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_UpdateThucChayHopDongChiTiet]
	@ThucChayHopDongChiTietID int,
	@HopDongREF int,
	@NhanHang nvarchar(255),
	@ThoiGianBatDau datetime,
	@ThoiGianKetThuc datetime,
	@Link nvarchar(1),
	@DmBannerREF nvarchar(255),
	@TenBanner nvarchar(255),
	@ViTri nvarchar(255),
	@GhiChu nvarchar(255),
	@BookingREF int,
	@HopDongChiTietREF int,
	@TypeThucChay int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[ThucChayHopDongChiTiet] SET
	[HopDongREF] = @HopDongREF,
	[NhanHang] = @NhanHang,
	[ThoiGianBatDau] = @ThoiGianBatDau,
	[ThoiGianKetThuc] = @ThoiGianKetThuc,
	[Link] = @Link,
	[DmBannerREF] = @DmBannerREF,
	[TenBanner] = @TenBanner,
	[ViTri] = @ViTri,
	[GhiChu] = @GhiChu,
	[BookingREF] = @BookingREF,
	[HopDongChiTietREF] = @HopDongChiTietREF,
	[TypeThucChay] = @TypeThucChay,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[ThucChayHopDongChiTietID] = @ThucChayHopDongChiTietID

```
