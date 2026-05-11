# Stored Procedure: `Gen_InsertOrUpdate_QuyenChiTietNhomQuyenDoiTuongQuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:31:03.303000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.950000

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
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_QuyenChiTietNhomQuyenDoiTuongQuyen]
	@QuyenChiTietNQTungDoiTuongQuyenREF INT ,
	@DmNhomNguoiDungREF INT ,
	@DmDoiTuongQuyenFK INT ,
	@TenDoiTuongQuyen NVARCHAR(200) ,
	@ChiTietDoiTuongQuyenREF INT ,
	@TenChiTietDoiTuongQuyen NVARCHAR(200) ,
	@GhiChu NVARCHAR(200) ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT
AS

	IF (
	       EXISTS(
	           SELECT *
	           FROM   [QuyenChiTietNhomQuyenDoiTuongQuyen]
	           WHERE  QuyenChiTietNQTungDoiTuongQuyenREF = @QuyenChiTietNQTungDoiTuongQuyenREF
	           AND DmDoiTuongQuyenFK = @DmDoiTuongQuyenFK
	       )
	   )
	    UPDATE [dbo].[QuyenChiTietNhomQuyenDoiTuongQuyen]
	    SET    [QuyenChiTietNQTungDoiTuongQuyenREF]  = @QuyenChiTietNQTungDoiTuongQuyenREF,
	           [DmNhomNguoiDungREF]                  = @DmNhomNguoiDungREF,
	           [DmDoiTuongQuyenFK]                   = @DmDoiTuongQuyenFK,
	           [TenDoiTuongQuyen]                    = @TenDoiTuongQuyen,
	           [ChiTietDoiTuongQuyenREF]             = @ChiTietDoiTuongQuyenREF,
	           [TenChiTietDoiTuongQuyen]             = @TenChiTietDoiTuongQuyen,
	           [GhiChu]                              = @GhiChu,
	           [CreatedBy]                           = @CreatedBy,
	           [CreatedAt]                           = @CreatedAt,
	           [LastModifiedBy]                      = @LastModifiedBy,
	           [LastModifiedAt]                      = @LastModifiedAt,
	           [DeletedStatus]                       = @DeletedStatus,
	           [PrintStatus]                         = @PrintStatus,
	           [RecordStatus]                        = @RecordStatus
	    WHERE  QuyenChiTietNQTungDoiTuongQuyenREF = @QuyenChiTietNQTungDoiTuongQuyenREF
	           AND DmDoiTuongQuyenFK = @DmDoiTuongQuyenFK
	ELSE
	    INSERT INTO [dbo].[QuyenChiTietNhomQuyenDoiTuongQuyen]
	      (
	        [QuyenChiTietNQTungDoiTuongQuyenREF],
	        [DmNhomNguoiDungREF],
	        [DmDoiTuongQuyenFK],
	        [TenDoiTuongQuyen],
	        [ChiTietDoiTuongQuyenREF],
	        [TenChiTietDoiTuongQuyen],
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
	        @QuyenChiTietNQTungDoiTuongQuyenREF,
	        @DmNhomNguoiDungREF,
	        @DmDoiTuongQuyenFK,
	        @TenDoiTuongQuyen,
	        @ChiTietDoiTuongQuyenREF,
	        @TenChiTietDoiTuongQuyen,
	        @GhiChu,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )

```
