# Stored Procedure: `Gen_InsertOrUpdate_ThucTreoVungMienLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:27:16.500000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucTreoVungMienLogID` | `int(4)` | No |
| `@VungMienID` | `int(4)` | No |
| `@BookingREF` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinhREF` | `int(4)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@DotChayChiTietREF` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecodStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucTreoVungMienLog]
	@ThucTreoVungMienLogID INT ,
	@VungMienID INT ,
	@BookingREF INT ,
	@SoLuong INT ,
	@DonViTinhREF INT ,
	@ThoiGianBatDau DATETIME ,
	@ThoiGianKetThuc DATETIME ,
	@DmBannerREF INT ,
	@DotChayChiTietREF INT ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecodStatus INT
AS
BEGIN
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [ThucTreoVungMienLog]
	           WHERE  [ThucTreoVungMienLogID] = @ThucTreoVungMienLogID
	       )
	   )
	    UPDATE [dbo].[ThucTreoVungMienLog]
	    SET    [VungMienID]             = @VungMienID,
	           [BookingREF]             = @BookingREF,
	           [SoLuong]                = @SoLuong,
	           [DonViTinhREF]           = @DonViTinhREF,
	           [ThoiGianBatDau]         = @ThoiGianBatDau,
	           [ThoiGianKetThuc]        = @ThoiGianKetThuc,
	           [DmBannerREF]            = @DmBannerREF,
	           [DotChayChiTietREF]      = @DotChayChiTietREF,
	           [CreatedBy]              = @CreatedBy,
	           [CreatedAt]              = @CreatedAt,
	           [LastModifiedBy]         = @LastModifiedBy,
	           [LastModifiedAt]         = @LastModifiedAt,
	           [DeletedStatus]          = @DeletedStatus,
	           [PrintStatus]            = @PrintStatus,
	           [RecodStatus]            = @RecodStatus
	    WHERE  [ThucTreoVungMienLogID]  = @ThucTreoVungMienLogID
	ELSE
	    INSERT INTO [dbo].[ThucTreoVungMienLog]
	      (
	        [ThucTreoVungMienLogID],
	        [VungMienID],
	        [BookingREF],
	        [SoLuong],
	        [DonViTinhREF],
	        [ThoiGianBatDau],
	        [ThoiGianKetThuc],
	        [DmBannerREF],
	        [DotChayChiTietREF],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecodStatus]
	      )
	    VALUES
	      (
	        @ThucTreoVungMienLogID,
	        @VungMienID,
	        @BookingREF,
	        @SoLuong,
	        @DonViTinhREF,
	        @ThoiGianBatDau,
	        @ThoiGianKetThuc,
	        @DmBannerREF,
	        @DotChayChiTietREF,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecodStatus
	      )
END

```
