# Stored Procedure: `Gen_InsertOrUpdate_QuyenChucNangNhomQuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:31:02.660000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.910000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomNguoiDungREF` | `int(4)` | No |
| `@TenNhomNguoiDung` | `nvarchar(400)` | No |
| `@DmChucNangREF` | `int(4)` | No |
| `@TenChucNang` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_QuyenChucNangNhomQuyen]
	@DmNhomNguoiDungREF INT ,
	@TenNhomNguoiDung NVARCHAR(200) ,
	@DmChucNangREF INT ,
	@TenChucNang NVARCHAR(200) ,
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
	           FROM   [QuyenChucNangNhomQuyen]
	           WHERE DmNhomNguoiDungREF =  @DmNhomNguoiDungREF
	           AND DmChucNangREF = @DmChucNangREF
	           AND CreatedAt = @CreatedAt
	       )
	   )
	    UPDATE [dbo].[QuyenChucNangNhomQuyen]
	    SET    [DmNhomNguoiDungREF]  = @DmNhomNguoiDungREF,
	           [TenNhomNguoiDung]    = @TenNhomNguoiDung,
	           [DmChucNangREF]       = @DmChucNangREF,
	           [TenChucNang]         = @TenChucNang,
	           [GhiChu]              = @GhiChu,
	           [CreatedBy]           = @CreatedBy,
	           [CreatedAt]           = @CreatedAt,
	           [LastModifiedBy]      = @LastModifiedBy,
	           [LastModifiedAt]      = @LastModifiedAt,
	           [DeletedStatus]       = @DeletedStatus,
	           [PrintStatus]         = @PrintStatus,
	           [RecordStatus]        = @RecordStatus
	    WHERE  DmNhomNguoiDungREF =  @DmNhomNguoiDungREF
	           AND DmChucNangREF = @DmChucNangREF
	           AND CreatedAt = @CreatedAt
	ELSE
	    INSERT INTO [dbo].[QuyenChucNangNhomQuyen]
	      (
	        [DmNhomNguoiDungREF],
	        [TenNhomNguoiDung],
	        [DmChucNangREF],
	        [TenChucNang],
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
	        @DmNhomNguoiDungREF,
	        @TenNhomNguoiDung,
	        @DmChucNangREF,
	        @TenChucNang,
	        @GhiChu,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )
END

```
