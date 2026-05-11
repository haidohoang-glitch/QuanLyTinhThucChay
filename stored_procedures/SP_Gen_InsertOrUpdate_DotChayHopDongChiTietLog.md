# Stored Procedure: `Gen_InsertOrUpdate_DotChayHopDongChiTietLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:36:34.343000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.960000

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
| `@TypeAdd` | `int(4)` | No |
| `@ThoiGianLog` | `datetime(8)` | No |
| `@NguoiLog` | `nvarchar(400)` | No |
| `@LoaiLog` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DotChayHopDongChiTietLog]
	@DotChayHopDongChiTietID BIGINT ,
	@ViTri NVARCHAR(200) ,
	@TenWebsite NVARCHAR(200) ,
	@HopDongREF BIGINT ,
	@HopDongChiTietREF BIGINT ,
	@ThoiGianBatDau DATETIME ,
	@ThoiGianKetThuc DATETIME ,
	@ThoiGianBatDauBooking DATETIME ,
	@ThoiGianKetThucBooking DATETIME ,
	@GhiChu NVARCHAR(200) ,
	@BookingREF BIGINT ,
	@IsWarning INT ,
	@DmBannerREF NVARCHAR(200) ,
	@TenBanner NVARCHAR(200) ,
	@TypeAdd INT ,
	@ThoiGianLog DATETIME ,
	@NguoiLog NVARCHAR(200) ,
	@LoaiLog INT ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT
AS
BEGIN
	DECLARE @IsExist INT
	SET @IsExist = (
	        SELECT COUNT(dchdctl.DotChayHopDongChiTietID)
	        FROM   DotChayHopDongChiTietLog dchdctl
	        WHERE  dchdctl.DotChayHopDongChiTietID = @DotChayHopDongChiTietID
	               AND dchdctl.ThoiGianLog = @ThoiGianLog
	               AND dchdctl.LoaiLog = @LoaiLog
	    )
	
	IF (@IsExist = 0)
	BEGIN
	    INSERT INTO [dbo].[DotChayHopDongChiTietLog]
	      (
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
	        [TypeAdd],
	        [ThoiGianLog],
	        [NguoiLog],
	        [LoaiLog],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus]
	      )
	    VALUES
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
	        @TypeAdd,
	        @ThoiGianLog,
	        @NguoiLog,
	        @LoaiLog,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )
	END
	
	IF (@LoaiLog = 3)
	BEGIN
	    UPDATE DotChayHopDongChiTiet
	    SET    LastModifiedBy           = @NguoiLog,
	           LastModifiedAt           = @ThoiGianLog,
	           DeletedStatus            = 1
	    WHERE  DotChayHopDongChiTietID  = @DotChayHopDongChiTietID
	END
END

```
