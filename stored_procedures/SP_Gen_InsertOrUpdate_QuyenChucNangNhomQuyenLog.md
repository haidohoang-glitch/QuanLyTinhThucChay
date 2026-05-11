# Stored Procedure: `Gen_InsertOrUpdate_QuyenChucNangNhomQuyenLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:31:01.823000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.880000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@QuyenChucNangNhomQuyenLogID` | `int(4)` | No |
| `@DmNhomNguoiDungREF` | `int(4)` | No |
| `@TenNhomNguoiDung` | `nvarchar(400)` | No |
| `@DmChucNangREF` | `int(4)` | No |
| `@TenChucNang` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_QuyenChucNangNhomQuyenLog]
	@QuyenChucNangNhomQuyenLogID INT ,
	@DmNhomNguoiDungREF INT ,
	@TenNhomNguoiDung NVARCHAR(200) ,
	@DmChucNangREF INT ,
	@TenChucNang NVARCHAR(200) ,
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
	           FROM   [QuyenChucNangNhomQuyenLog]
	           WHERE  [QuyenChucNangNhomQuyenLogID] = @QuyenChucNangNhomQuyenLogID
	       )
	   )
	    UPDATE [dbo].[QuyenChucNangNhomQuyenLog]
	    SET    [DmNhomNguoiDungREF]           = @DmNhomNguoiDungREF,
	           [TenNhomNguoiDung]             = @TenNhomNguoiDung,
	           [DmChucNangREF]                = @DmChucNangREF,
	           [TenChucNang]                  = @TenChucNang,
	           [GhiChu]                       = @GhiChu,
	           [ThoiGianLog]                  = @ThoiGianLog,
	           [NguoiLog]                     = @NguoiLog,
	           [LoaiLog]                      = @LoaiLog,
	           [CreatedBy]                    = @CreatedBy,
	           [CreatedAt]                    = @CreatedAt,
	           [LastModifiedBy]               = @LastModifiedBy,
	           [LastModifiedAt]               = @LastModifiedAt,
	           [DeletedStatus]                = @DeletedStatus,
	           [PrintStatus]                  = @PrintStatus,
	           [RecordStatus]                 = @RecordStatus
	    WHERE  [QuyenChucNangNhomQuyenLogID]  = @QuyenChucNangNhomQuyenLogID
	ELSE
	    INSERT INTO [dbo].[QuyenChucNangNhomQuyenLog]
	      (
	        [QuyenChucNangNhomQuyenLogID],
	        [DmNhomNguoiDungREF],
	        [TenNhomNguoiDung],
	        [DmChucNangREF],
	        [TenChucNang],
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
	        @QuyenChucNangNhomQuyenLogID,
	        @DmNhomNguoiDungREF,
	        @TenNhomNguoiDung,
	        @DmChucNangREF,
	        @TenChucNang,
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
	      	UPDATE QuyenChucNangNhomQuyen
	      	SET DeletedStatus = 1
	      	,LastModifiedAt = @ThoiGianLog
	      	,LastModifiedBy = @NguoiLog
	      	WHERE DmNhomNguoiDungREF = @DmNhomNguoiDungREF
	      	AND DmChucNangREF = @DmChucNangREF
	      END
	      
END

```
