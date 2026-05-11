# Stored Procedure: `Gen_InsertOrUpdate_DotChayChiTietHopDongChiTietLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:38:50.557000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.003000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayChiTietHopDongChiTietLogID` | `int(4)` | No |
| `@DotChayChiTietHopDongChiTietREF` | `int(4)` | No |
| `@DotChayHopDongChitietREF` | `int(4)` | No |
| `@BookingREF` | `int(4)` | No |
| `@SoLuong` | `float(8)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@VungMienID` | `int(4)` | No |
| `@TenVungMien` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DotChayChiTietHopDongChiTietLog]
	@DotChayChiTietHopDongChiTietLogID INT ,
	@DotChayChiTietHopDongChiTietREF INT ,
	@DotChayHopDongChitietREF INT ,
	@BookingREF INT ,
	@SoLuong FLOAT ,
	@ThoiGianBatDau DATETIME ,
	@ThoiGianKetThuc DATETIME ,
	@VungMienID INT ,
	@TenVungMien NVARCHAR(200) ,
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
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [DotChayChiTietHopDongChiTietLog]
	           WHERE  [DotChayChiTietHopDongChiTietLogID] = @DotChayChiTietHopDongChiTietLogID
	       )
	   )
	    UPDATE [dbo].[DotChayChiTietHopDongChiTietLog]
	    SET    [DotChayChiTietHopDongChiTietREF]    = @DotChayChiTietHopDongChiTietREF,
	           [DotChayHopDongChitietREF]           = @DotChayHopDongChitietREF,
	           [BookingREF]                         = @BookingREF,
	           [SoLuong]                            = @SoLuong,
	           [ThoiGianBatDau]                     = @ThoiGianBatDau,
	           [ThoiGianKetThuc]                    = @ThoiGianKetThuc,
	           [VungMienID]                         = @VungMienID,
	           [TenVungMien]                        = @TenVungMien,
	           [ThoiGianLog]                        = @ThoiGianLog,
	           [NguoiLog]                           = @NguoiLog,
	           [LoaiLog]                            = @LoaiLog,
	           [CreatedBy]                          = @CreatedBy,
	           [CreatedAt]                          = @CreatedAt,
	           [LastModifiedBy]                     = @LastModifiedBy,
	           [LastModifiedAt]                     = @LastModifiedAt,
	           [DeletedStatus]                      = @DeletedStatus,
	           [PrintStatus]                        = @PrintStatus,
	           [RecordStatus]                       = @RecordStatus
	    WHERE  [DotChayChiTietHopDongChiTietLogID]  = @DotChayChiTietHopDongChiTietLogID
	ELSE
	    INSERT INTO [dbo].[DotChayChiTietHopDongChiTietLog]
	      (
	        [DotChayChiTietHopDongChiTietLogID],
	        [DotChayChiTietHopDongChiTietREF],
	        [DotChayHopDongChitietREF],
	        [BookingREF],
	        [SoLuong],
	        [ThoiGianBatDau],
	        [ThoiGianKetThuc],
	        [VungMienID],
	        [TenVungMien],
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
	        @DotChayChiTietHopDongChiTietLogID,
	        @DotChayChiTietHopDongChiTietREF,
	        @DotChayHopDongChitietREF,
	        @BookingREF,
	        @SoLuong,
	        @ThoiGianBatDau,
	        @ThoiGianKetThuc,
	        @VungMienID,
	        @TenVungMien,
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
	      IF(@LoaiLog = 3)
	      BEGIN
	      	UPDATE DotChayChiTietHopDongChiTiet
	      	SET
	      		LastModifiedBy = @NguoiLog,
	      		LastModifiedAt = @ThoiGianLog,
	      		DeletedStatus = 1
	      	WHERE DotChayChiTietHopDongChiTietID = @DotChayChiTietHopDongChiTietREF
	      	
	      END
END

```
