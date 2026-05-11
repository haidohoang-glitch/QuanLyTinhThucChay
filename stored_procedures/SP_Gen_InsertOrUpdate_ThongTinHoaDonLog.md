# Stored Procedure: `Gen_InsertOrUpdate_ThongTinHoaDonLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:25:11.703000
- **Ngày sửa cuối**: 2014-12-03 15:40:13.467000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinHoaDonLogID` | `int(4)` | No |
| `@ThongTinHoaDonREF` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHoaDon` | `nvarchar(400)` | No |
| `@NgayXuatHoaDon` | `datetime(8)` | No |
| `@GiaTri` | `float(8)` | No |
| `@NgayTraHoaDon` | `datetime(8)` | No |
| `@SoBangThongKe` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinHoaDonLog]
	@ThongTinHoaDonLogID INT ,
	@ThongTinHoaDonREF INT ,
	@HopDongREF INT ,
	@SoHoaDon NVARCHAR(200) ,
	@NgayXuatHoaDon DATETIME ,
	@GiaTri FLOAT ,
	@NgayTraHoaDon DATETIME ,
	@SoBangThongKe NVARCHAR(200) ,
	@GhiChu NVARCHAR(200) ,
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
	           FROM   [ThongTinHoaDonLog]
	           WHERE  [ThongTinHoaDonLogID] = @ThongTinHoaDonLogID
	       )
	   )
	    UPDATE [dbo].[ThongTinHoaDonLog]
	    SET    [ThongTinHoaDonREF]    = @ThongTinHoaDonREF,
	           [HopDongREF]           = @HopDongREF,
	           [SoHoaDon]             = @SoHoaDon,
	           [NgayXuatHoaDon]       = @NgayXuatHoaDon,
	           [GiaTri]               = @GiaTri,
	           [NgayTraHoaDon]        = @NgayTraHoaDon,
	           [SoBangThongKe]        = @SoBangThongKe,
	           [GhiChu]               = @GhiChu,
	           [ThoiGianLog]          = @ThoiGianLog,
	           [NguoiLog]             = @NguoiLog,
	           [LoaiLog]              = @LoaiLog,
	           [CreatedBy]            = @CreatedBy,
	           [CreatedAt]            = @CreatedAt,
	           [LastModifiedBy]       = @LastModifiedBy,
	           [LastModifiedAt]       = @LastModifiedAt,
	           [DeletedStatus]        = @DeletedStatus,
	           [PrintStatus]          = @PrintStatus,
	           [RecordStatus]         = @RecordStatus
	    WHERE  [ThongTinHoaDonLogID]  = @ThongTinHoaDonLogID
	ELSE
	    INSERT INTO [dbo].[ThongTinHoaDonLog]
	      (
	        [ThongTinHoaDonLogID],
	        [ThongTinHoaDonREF],
	        [HopDongREF],
	        [SoHoaDon],
	        [NgayXuatHoaDon],
	        [GiaTri],
	        [NgayTraHoaDon],
	        [SoBangThongKe],
	        [GhiChu],
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
	        @ThongTinHoaDonLogID,
	        @ThongTinHoaDonREF,
	        @HopDongREF,
	        @SoHoaDon,
	        @NgayXuatHoaDon,
	        @GiaTri,
	        @NgayTraHoaDon,
	        @SoBangThongKe,
	        @GhiChu,
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
	      	UPDATE ThongTinHoaDon
	      	SET
	      		LastModifiedBy = @NguoiLog,
	      		LastModifiedAt = @ThoiGianLog,
	      		DeletedStatus = 1
	      	WHERE ThongTinHoaDonID = @ThongTinHoaDonREF	
	      END
END
	
```
