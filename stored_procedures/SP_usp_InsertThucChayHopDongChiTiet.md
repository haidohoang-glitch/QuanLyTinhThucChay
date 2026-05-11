# Stored Procedure: `usp_InsertThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:12:34.203000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.360000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(510)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@Link` | `nvarchar(510)` | No |
| `@DmBannerREF` | `nvarchar(510)` | No |
| `@TenBanner` | `nvarchar(510)` | No |
| `@ViTri` | `nvarchar(510)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@BookingREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@TypeThucChay` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertThucChayHopDongChiTiet]
	@ThucChayHopDongChiTietID INT,
	@HopDongREF INT,
	@NhanHang NVARCHAR(255),
	@ThoiGianBatDau DATETIME,
	@ThoiGianKetThuc DATETIME,
	@Link NVARCHAR(255),
	@DmBannerREF NVARCHAR(255),
	@TenBanner NVARCHAR(255),
	@ViTri NVARCHAR(255),
	@GhiChu NVARCHAR(255),
	@BookingREF INT,
	@HopDongChiTietREF INT,
	@TypeThucChay INT,
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
	           SELECT HopDongREF
	           FROM   [ThucChayHopDongChiTiet]
	           WHERE  [ThucChayHopDongChiTietID] = @ThucChayHopDongChiTietID
	       )
	   )
	    UPDATE [dbo].[ThucChayHopDongChiTiet]
	    SET    [HopDongREF]                = @HopDongREF,
	           [NhanHang]                  = @NhanHang,
	           [ThoiGianBatDau]            = @ThoiGianBatDau,
	           [ThoiGianKetThuc]           = @ThoiGianKetThuc,
	           [Link]                      = @Link,
	           [DmBannerREF]               = @DmBannerREF,
	           [TenBanner]                 = @TenBanner,
	           [ViTri]                     = @ViTri,
	           [GhiChu]                    = @GhiChu,
	           [BookingREF]                = @BookingREF,
	           [HopDongChiTietREF]         = @HopDongChiTietREF,
	           [TypeThucChay]              = @TypeThucChay,
	           [LastModifiedBy]            = @LastModifiedBy,
	           [LastModifiedAt]            = @LastModifiedAt,
	           [DeletedStatus]             = @DeletedStatus,
	           [PrintStatus]               = @PrintStatus
	    WHERE  [ThucChayHopDongChiTietID]  = @ThucChayHopDongChiTietID
	ELSE
	    INSERT INTO [dbo].[ThucChayHopDongChiTiet]
	      (
	        [ThucChayHopDongChiTietID],
	        [HopDongREF],
	        [NhanHang],
	        [ThoiGianBatDau],
	        [ThoiGianKetThuc],
	        [Link],
	        [DmBannerREF],
	        [TenBanner],
	        [ViTri],
	        [GhiChu],
	        [BookingREF],
	        [HopDongChiTietREF],
	        [TypeThucChay],
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
	        @ThucChayHopDongChiTietID,
	        @HopDongREF,
	        @NhanHang,
	        @ThoiGianBatDau,
	        @ThoiGianKetThuc,
	        @Link,
	        @DmBannerREF,
	        @TenBanner,
	        @ViTri,
	        @GhiChu,
	        @BookingREF,
	        @HopDongChiTietREF,
	        @TypeThucChay,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )

```
