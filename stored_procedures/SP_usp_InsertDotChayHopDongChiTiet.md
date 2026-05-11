# Stored Procedure: `usp_InsertDotChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:13:42.187000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.767000

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
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertDotChayHopDongChiTiet]
	@DotChayHopDongChiTietID INT,
	@ViTri NVARCHAR(255),
	@TenWebsite NVARCHAR(100),
	@HopDongREF INT,
	@HopDongChiTietREF INT,
	@ThoiGianBatDau DATETIME,
	@ThoiGianKetThuc DATETIME,
	@ThoiGianBatDauBooking DATETIME,
	@ThoiGianKetThucBooking DATETIME,
	@GhiChu NVARCHAR(255),
	@BookingREF INT,
	@IsWarning INT,
	@DmBannerREF NVARCHAR(255),
	@TenBanner NVARCHAR(255),
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModifiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT
AS
	SET NOCOUNT ON
	IF (
	       EXISTS(
	           SELECT DotChayHopDongChiTietID
	           FROM   [DotChayHopDongChiTiet]
	           WHERE  [DotChayHopDongChiTietID] = @DotChayHopDongChiTietID
	       )
	   )
	    UPDATE [dbo].[DotChayHopDongChiTiet]
	    SET    [ViTri]                    = @ViTri,
	           [TenWebsite]               = @TenWebsite,
	           [HopDongREF]               = @HopDongREF,
	           [HopDongChiTietREF]        = @HopDongChiTietREF,
	           [ThoiGianBatDau]           = @ThoiGianBatDau,
	           [ThoiGianKetThuc]          = @ThoiGianKetThuc,
	           [ThoiGianBatDauBooking]    = @ThoiGianBatDauBooking,
	           [ThoiGianKetThucBooking]   = @ThoiGianKetThucBooking,
	           [GhiChu]                   = @GhiChu,
	           [BookingREF]               = @BookingREF,
	           [IsWarning]                = @IsWarning,
	           [DmBannerREF]              = @DmBannerREF,
	           [TenBanner]                = @TenBanner,
	           CreatedBy                  = @CreatedBy,
	           CreatedAt                  = @CreatedAt,
	           [LastModifiedBy]           = @LastModifiedBy,
	           [LastModifiedAt]           = @LastModifiedAt,
	           [DeletedStatus]            = @DeletedStatus,
	           [PrintStatus]              = @PrintStatus,
	           [RecordStatus]             = @RecordStatus
	    WHERE  [DotChayHopDongChiTietID]  = @DotChayHopDongChiTietID
	ELSE
	    INSERT INTO [dbo].[DotChayHopDongChiTiet]
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
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )

```
