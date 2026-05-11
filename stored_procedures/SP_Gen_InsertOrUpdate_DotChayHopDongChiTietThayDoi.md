# Stored Procedure: `Gen_InsertOrUpdate_DotChayHopDongChiTietThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:42:21.410000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.940000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayHopDongChiTietThayDoiID` | `bigint(8)` | No |
| `@ViTri` | `nvarchar(400)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@HopDongREF` | `bigint(8)` | No |
| `@HopDongThayDoiREF` | `bigint(8)` | No |
| `@HopDongChiTietREF` | `bigint(8)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@ThoiGianBatDauBooking` | `datetime(8)` | No |
| `@ThoiGianKetThucBooking` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@TenBanner` | `nvarchar(400)` | No |
| `@DmBannerREF` | `nvarchar(400)` | No |
| `@BookingREF` | `bigint(8)` | No |
| `@IsWarning` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DotChayHopDongChiTietThayDoi] 	
@DotChayHopDongChiTietThayDoiID bigint ,	
@ViTri nvarchar (200) ,	
@TenWebsite nvarchar (200) ,	
@HopDongREF bigint ,	
@HopDongThayDoiREF bigint ,	
@HopDongChiTietREF bigint ,	
@ThoiGianBatDau datetime ,	
@ThoiGianKetThuc datetime ,	
@ThoiGianBatDauBooking datetime ,	
@ThoiGianKetThucBooking datetime ,	
@GhiChu nvarchar (200) ,	
@TenBanner nvarchar (200) ,	
@DmBannerREF nvarchar (200) ,	
@BookingREF bigint ,	
@IsWarning int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DotChayHopDongChiTietThayDoi] where [DotChayHopDongChiTietThayDoiID] = @DotChayHopDongChiTietThayDoiID))	
UPDATE [dbo].[DotChayHopDongChiTietThayDoi] SET 	
[ViTri] = @ViTri,	
[TenWebsite] = @TenWebsite,	
[HopDongREF] = @HopDongREF,	
[HopDongThayDoiREF] = @HopDongThayDoiREF,	
[HopDongChiTietREF] = @HopDongChiTietREF,	
[ThoiGianBatDau] = @ThoiGianBatDau,	
[ThoiGianKetThuc] = @ThoiGianKetThuc,	
[ThoiGianBatDauBooking] = @ThoiGianBatDauBooking,	
[ThoiGianKetThucBooking] = @ThoiGianKetThucBooking,	
[GhiChu] = @GhiChu,	
[TenBanner] = @TenBanner,	
[DmBannerREF] = @DmBannerREF,	
[BookingREF] = @BookingREF,	
[IsWarning] = @IsWarning,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DotChayHopDongChiTietThayDoiID] = @DotChayHopDongChiTietThayDoiID	
else 	
INSERT INTO [dbo].[DotChayHopDongChiTietThayDoi] (	
[DotChayHopDongChiTietThayDoiID],	
[ViTri],	
[TenWebsite],	
[HopDongREF],	
[HopDongThayDoiREF],	
[HopDongChiTietREF],	
[ThoiGianBatDau],	
[ThoiGianKetThuc],	
[ThoiGianBatDauBooking],	
[ThoiGianKetThucBooking],	
[GhiChu],	
[TenBanner],	
[DmBannerREF],	
[BookingREF],	
[IsWarning],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DotChayHopDongChiTietThayDoiID,	
@ViTri,	
@TenWebsite,	
@HopDongREF,	
@HopDongThayDoiREF,	
@HopDongChiTietREF,	
@ThoiGianBatDau,	
@ThoiGianKetThuc,	
@ThoiGianBatDauBooking,	
@ThoiGianKetThucBooking,	
@GhiChu,	
@TenBanner,	
@DmBannerREF,	
@BookingREF,	
@IsWarning,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
