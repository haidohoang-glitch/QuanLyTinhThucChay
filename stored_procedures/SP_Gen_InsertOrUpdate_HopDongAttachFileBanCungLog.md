# Stored Procedure: `Gen_InsertOrUpdate_HopDongAttachFileBanCungLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-20 10:37:15.653000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongAttachFileBanCungID` | `int(4)` | No |
| `@HopDongAttachFileREF` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@NgayNhanBanCung` | `datetime(8)` | No |
| `@NgayNhanBanFax` | `datetime(8)` | No |
| `@NgayChuyenChoKeToan` | `datetime(8)` | No |
| `@KhongTheNhapBanCung` | `int(4)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongAttachFileBanCungLog]
	@HopDongAttachFileBanCungID INT ,
	@HopDongAttachFileREF INT ,
	@HopDongREF INT ,
	@NgayNhanBanCung DATETIME ,
	@NgayNhanBanFax DATETIME ,
	@NgayChuyenChoKeToan DATETIME ,
	@KhongTheNhapBanCung INT ,
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
	           FROM   [HopDongAttachFileBanCungLog]
	           WHERE  1 > 2
	       )
	   )
	    UPDATE [dbo].[HopDongAttachFileBanCungLog]
	    SET    [HopDongAttachFileBanCungID]  = @HopDongAttachFileBanCungID,
	           [HopDongAttachFileREF]        = @HopDongAttachFileREF,
	           [HopDongREF]                  = @HopDongREF,
	           [NgayNhanBanCung]             = @NgayNhanBanCung,
	           [NgayNhanBanFax]              = @NgayNhanBanFax,
	           [NgayChuyenChoKeToan]         = @NgayChuyenChoKeToan,
	           [KhongTheNhapBanCung]         = @KhongTheNhapBanCung,
	           [GhiChu]                      = @GhiChu,
	           [ThoiGianLog]                 = @ThoiGianLog,
	           [NguoiLog]                    = @NguoiLog,
	           [LoaiLog]                     = @LoaiLog,
	           [CreatedBy]                   = @CreatedBy,
	           [CreatedAt]                   = @CreatedAt,
	           [LastModifiedBy]              = @LastModifiedBy,
	           [LastModifiedAt]              = @LastModifiedAt,
	           [DeletedStatus]               = @DeletedStatus,
	           [PrintStatus]                 = @PrintStatus,
	           [RecordStatus]                = @RecordStatus
	    WHERE  1 > 2
	ELSE
	    INSERT INTO [dbo].[HopDongAttachFileBanCungLog]
	      (
	        [HopDongAttachFileBanCungID],
	        [HopDongAttachFileREF],
	        [HopDongREF],
	        [NgayNhanBanCung],
	        [NgayNhanBanFax],
	        [NgayChuyenChoKeToan],
	        [KhongTheNhapBanCung],
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
	        @HopDongAttachFileBanCungID,
	        @HopDongAttachFileREF,
	        @HopDongREF,
	        @NgayNhanBanCung,
	        @NgayNhanBanFax,
	        @NgayChuyenChoKeToan,
	        @KhongTheNhapBanCung,
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
	      	UPDATE HopDongAttachFileBanCung
	      	SET
	      		LastModifiedBy = @NguoiLog,
	      		LastModifiedAt = @ThoiGianLog,
	      		DeletedStatus = 1
	      	WHERE HopDongAttachFileBanCungID = @HopDongAttachFileBanCungID	
	      END
END

```
