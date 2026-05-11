# Stored Procedure: `Gen_InsertOrUpdate_QuyenChiTietNhomQuyenDoiTuongQuyenLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:31:03
- **Ngày sửa cuối**: 2014-11-19 12:16:51.937000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@QuyenChiTietNQTungDoiTuongQuyenREF` | `int(4)` | No |
| `@DmNhomNguoiDungREF` | `int(4)` | No |
| `@DmDoiTuongQuyenFK` | `int(4)` | No |
| `@TenDoiTuongQuyen` | `nvarchar(400)` | No |
| `@ChiTietDoiTuongQuyenREF` | `int(4)` | No |
| `@TenChiTietDoiTuongQuyen` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_QuyenChiTietNhomQuyenDoiTuongQuyenLog]
	@QuyenChiTietNQTungDoiTuongQuyenREF INT ,
	@DmNhomNguoiDungREF INT ,
	@DmDoiTuongQuyenFK INT ,
	@TenDoiTuongQuyen NVARCHAR(200) ,
	@ChiTietDoiTuongQuyenREF INT ,
	@TenChiTietDoiTuongQuyen NVARCHAR(200) ,
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
	           FROM   [QuyenChiTietNhomQuyenDoiTuongQuyenLog]
	           WHERE QuyenChiTietNQTungDoiTuongQuyenREF = @QuyenChiTietNQTungDoiTuongQuyenREF
	           AND DmDoiTuongQuyenFK = @DmDoiTuongQuyenFK
	           AND DmNhomNguoiDungREF = @DmNhomNguoiDungREF
	           AND ThoiGianLog = @ThoiGianLog
	           AND NguoiLog = @NguoiLog
	           AND LoaiLog = @LoaiLog
	       )
	   )
	    UPDATE [dbo].[QuyenChiTietNhomQuyenDoiTuongQuyenLog]
	    SET    [QuyenChiTietNQTungDoiTuongQuyenREF]  = @QuyenChiTietNQTungDoiTuongQuyenREF,
	           [DmNhomNguoiDungREF]                  = @DmNhomNguoiDungREF,
	           [DmDoiTuongQuyenFK]                   = @DmDoiTuongQuyenFK,
	           [TenDoiTuongQuyen]                    = @TenDoiTuongQuyen,
	           [ChiTietDoiTuongQuyenREF]             = @ChiTietDoiTuongQuyenREF,
	           [TenChiTietDoiTuongQuyen]             = @TenChiTietDoiTuongQuyen,
	           [GhiChu]                              = @GhiChu,
	           [ThoiGianLog]                         = @ThoiGianLog,
	           [NguoiLog]                            = @NguoiLog,
	           [LoaiLog]                             = @LoaiLog,
	           [CreatedBy]                           = @CreatedBy,
	           [CreatedAt]                           = @CreatedAt,
	           [LastModifiedBy]                      = @LastModifiedBy,
	           [LastModifiedAt]                      = @LastModifiedAt,
	           [DeletedStatus]                       = @DeletedStatus,
	           [PrintStatus]                         = @PrintStatus,
	           [RecordStatus]                        = @RecordStatus
	    WHERE QuyenChiTietNQTungDoiTuongQuyenREF = @QuyenChiTietNQTungDoiTuongQuyenREF
	           AND DmDoiTuongQuyenFK = @DmDoiTuongQuyenFK
	           AND DmNhomNguoiDungREF = @DmNhomNguoiDungREF
	           AND ThoiGianLog = @ThoiGianLog
	           AND NguoiLog = @NguoiLog
	           AND LoaiLog = @LoaiLog
	ELSE
	    INSERT INTO [dbo].[QuyenChiTietNhomQuyenDoiTuongQuyenLog]
	      (
	        [QuyenChiTietNQTungDoiTuongQuyenREF],
	        [DmNhomNguoiDungREF],
	        [DmDoiTuongQuyenFK],
	        [TenDoiTuongQuyen],
	        [ChiTietDoiTuongQuyenREF],
	        [TenChiTietDoiTuongQuyen],
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
	        @QuyenChiTietNQTungDoiTuongQuyenREF,
	        @DmNhomNguoiDungREF,
	        @DmDoiTuongQuyenFK,
	        @TenDoiTuongQuyen,
	        @ChiTietDoiTuongQuyenREF,
	        @TenChiTietDoiTuongQuyen,
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
	      	UPDATE QuyenChiTietNhomQuyenDoiTuongQuyen
	      	SET DeletedStatus = 1
	      	, LastModifiedAt = @ThoiGianLog
	      	, LastModifiedBy = @NguoiLog
	      	WHERE QuyenChiTietNQTungDoiTuongQuyenREF = @QuyenChiTietNQTungDoiTuongQuyenREF
	      	AND DmDoiTuongQuyenFK = @DmDoiTuongQuyenFK
	      END
END

```
