# Stored Procedure: `Gen_InsertOrUpdate_ThongTinTienVeLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:26:06.960000
- **Ngày sửa cuối**: 2014-12-03 15:42:40.670000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinTienVeLogID` | `int(4)` | No |
| `@ThongTinTienVeREF` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@IsPhieuThu` | `int(4)` | No |
| `@PhieuThuLinkNapTien` | `nvarchar(400)` | No |
| `@GiaTri` | `float(8)` | No |
| `@TaiKhoanKhachHang` | `nvarchar(400)` | No |
| `@ThoiGianLog` | `datetime(8)` | No |
| `@NguoiLog` | `nvarchar(400)` | No |
| `@LoaiLog` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinTienVeLog]
	@ThongTinTienVeLogID INT ,
	@ThongTinTienVeREF INT ,
	@HopDongREF INT ,
	@NgayThanhToan DATETIME ,
	@IsPhieuThu INT ,
	@PhieuThuLinkNapTien NVARCHAR(200) ,
	@GiaTri FLOAT ,
	@TaiKhoanKhachHang NVARCHAR(200) ,
	@ThoiGianLog DATETIME ,
	@NguoiLog NVARCHAR(200) ,
	@LoaiLog INT ,
	@GhiChu NVARCHAR(200) ,
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
	           FROM   [ThongTinTienVeLog]
	           WHERE  [ThongTinTienVeLogID] = @ThongTinTienVeLogID
	       )
	   )
	    UPDATE [dbo].[ThongTinTienVeLog]
	    SET    [ThongTinTienVeREF]    = @ThongTinTienVeREF,
	           [HopDongREF]           = @HopDongREF,
	           [NgayThanhToan]        = @NgayThanhToan,
	           [IsPhieuThu]           = @IsPhieuThu,
	           [PhieuThuLinkNapTien]  = @PhieuThuLinkNapTien,
	           [GiaTri]               = @GiaTri,
	           [TaiKhoanKhachHang]    = @TaiKhoanKhachHang,
	           [ThoiGianLog]          = @ThoiGianLog,
	           [NguoiLog]             = @NguoiLog,
	           [LoaiLog]              = @LoaiLog,
	           [GhiChu]               = @GhiChu,
	           [CreatedBy]            = @CreatedBy,
	           [CreatedAt]            = @CreatedAt,
	           [LastModifiedBy]       = @LastModifiedBy,
	           [LastModifiedAt]       = @LastModifiedAt,
	           [DeletedStatus]        = @DeletedStatus,
	           [PrintStatus]          = @PrintStatus,
	           [RecordStatus]         = @RecordStatus
	    WHERE  [ThongTinTienVeLogID]  = @ThongTinTienVeLogID
	ELSE
	    INSERT INTO [dbo].[ThongTinTienVeLog]
	      (
	        [ThongTinTienVeLogID],
	        [ThongTinTienVeREF],
	        [HopDongREF],
	        [NgayThanhToan],
	        [IsPhieuThu],
	        [PhieuThuLinkNapTien],
	        [GiaTri],
	        [TaiKhoanKhachHang],
	        [ThoiGianLog],
	        [NguoiLog],
	        [LoaiLog],
	        [GhiChu],
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
	        @ThongTinTienVeLogID,
	        @ThongTinTienVeREF,
	        @HopDongREF,
	        @NgayThanhToan,
	        @IsPhieuThu,
	        @PhieuThuLinkNapTien,
	        @GiaTri,
	        @TaiKhoanKhachHang,
	        @ThoiGianLog,
	        @NguoiLog,
	        @LoaiLog,
	        @GhiChu,
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
	      	UPDATE ThongTinTienVe
	      	SET
	      		LastModifiedBy = @NguoiLog,
	      		LastModifiedAt = @ThoiGianLog,
	      		DeletedStatus = 1
	      	WHERE ThongTinTienVeID = @ThongTinTienVeREF
	      END
END
	
```
