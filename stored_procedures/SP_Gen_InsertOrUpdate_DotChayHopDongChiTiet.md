# Stored Procedure: `Gen_InsertOrUpdate_DotChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:36:49.263000
- **Ngày sửa cuối**: 2017-07-08 11:53:04.693000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayHopDongChiTietID` | `bigint(8)` | No |
| `@ViTri` | `nvarchar(400)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@HopDongREF` | `bigint(8)` | No |
| `@HopDongChiTietREF` | `bigint(8)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@ThoiGianBatDauBooking` | `datetime(8)` | No |
| `@ThoiGianKetThucBooking` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@BookingREF` | `bigint(8)` | No |
| `@IsWarning` | `int(4)` | No |
| `@DmBannerREF` | `nvarchar(400)` | No |
| `@TenBanner` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DotChayHopDongChiTiet] 	
@DotChayHopDongChiTietID bigint ,	
@ViTri nvarchar (200) ,	
@TenWebsite nvarchar (200) ,	
@HopDongREF bigint ,	
@HopDongChiTietREF bigint ,	
@ThoiGianBatDau datetime ,	
@ThoiGianKetThuc datetime ,	
@ThoiGianBatDauBooking datetime ,	
@ThoiGianKetThucBooking datetime ,	
@GhiChu nvarchar (200) ,	
@BookingREF bigint ,	
@IsWarning int ,	
@DmBannerREF nvarchar (200) ,	
@TenBanner nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
BEGIN
	IF(exists(select * from [DotChayHopDongChiTiet] where [DotChayHopDongChiTietID] = @DotChayHopDongChiTietID))	
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
	[CreatedBy] = @CreatedBy,	
	[CreatedAt] = @CreatedAt,	
	[LastModifiedBy] = @LastModifiedBy,	
	[LastModifiedAt] = @LastModifiedAt,	
	[PrintStatus] = @PrintStatus,	
	[RecordStatus] = @RecordStatus where [DotChayHopDongChiTietID] = @DotChayHopDongChiTietID	
	else 	
	INSERT INTO [dbo].[DotChayHopDongChiTiet] (	
	[DotChayHopDongChiTietID],	
	[ViTri],	
	[TenWebsite],	
	[HopDongREF],	
	[HopDongChiTietREF],	
	[ThoiGianBatDau],	
	[ThoiGianKetThuc],	
	[ThoiGianBatDauBooking],	
	[ThoiGianKetThucBooking],	
	[GhiChu],	
	[BookingREF],	
	[IsWarning],	
	[DmBannerREF],	
	[TenBanner],	
	[CreatedBy],	
	[CreatedAt],	
	[LastModifiedBy],	
	[LastModifiedAt],	
	[DeletedStatus],	
	[PrintStatus],	
	[RecordStatus])	
	Values 	
	(	
	@DotChayHopDongChiTietID,	
	@ViTri,	
	@TenWebsite,	
	@HopDongREF,	
	@HopDongChiTietREF,	
	@ThoiGianBatDau,	
	@ThoiGianKetThuc,	
	@ThoiGianBatDauBooking,	
	@ThoiGianKetThucBooking,	
	@GhiChu,	
	@BookingREF,	
	@IsWarning,	
	@DmBannerREF,	
	@TenBanner,	
	@CreatedBy,	
	@CreatedAt,	
	@LastModifiedBy,	
	@LastModifiedAt,	
	@DeletedStatus,	
	@PrintStatus,	
	@RecordStatus)
END
```
