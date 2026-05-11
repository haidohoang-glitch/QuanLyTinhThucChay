# Stored Procedure: `usp_UpdateDotChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:09:18.690000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.137000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayHopDongChiTietID` | `int(4)` | No |
| `@ViTri` | `nvarchar(510)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@ThoiGianBatDauBooking` | `datetime(8)` | No |
| `@ThoiGianKetThucBooking` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@BookingREF` | `int(4)` | No |
| `@IsWarning` | `int(4)` | No |
| `@DmBannerREF` | `nvarchar(510)` | No |
| `@TenBanner` | `nvarchar(510)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDotChayHopDongChiTiet]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDotChayHopDongChiTiet]
	@DotChayHopDongChiTietID int,
	@ViTri nvarchar(255),
	@TenWebsite nvarchar(100),
	@HopDongREF int,
	@HopDongChiTietREF int,
	@ThoiGianBatDau datetime,
	@ThoiGianKetThuc datetime,
	@ThoiGianBatDauBooking datetime,
	@ThoiGianKetThucBooking datetime,
	@GhiChu nvarchar(255),
	@BookingREF int,
	@IsWarning int,
	@DmBannerREF nvarchar(255),
	@TenBanner nvarchar(255),
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[DotChayHopDongChiTiet] SET
	[ViTri] = @ViTri,
	[TenWebsite] = @TenWebsite,
	[HopDongREF] = @HopDongREF,
	[HopDongChiTietREF] = @HopDongChiTietREF,
	[ThoiGianBatDau] = @ThoiGianBatDau,
	[ThoiGianKetThuc] = @ThoiGianKetThuc,
	[ThoiGianBatDauBooking] = @ThoiGianBatDauBooking,
	[ThoiGianKetThucBooking] = @ThoiGianKetThucBooking,
	[GhiChu] = @GhiChu,
	[BookingREF] = @BookingREF,
	[IsWarning] = @IsWarning,
	[DmBannerREF] = @DmBannerREF,
	[TenBanner] = @TenBanner,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DotChayHopDongChiTietID] = @DotChayHopDongChiTietID

```
