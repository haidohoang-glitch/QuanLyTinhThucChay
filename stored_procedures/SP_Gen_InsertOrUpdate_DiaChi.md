# Stored Procedure: `Gen_InsertOrUpdate_DiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-15 16:35:20.007000
- **Ngày sửa cuối**: 2015-04-15 17:11:40.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmKhachHangThongTinChungREF` | `bigint(8)` | No |
| `@SoNha` | `nvarchar(400)` | No |
| `@DuongPho` | `nvarchar(400)` | No |
| `@DmQuanHuyenREF` | `int(4)` | No |
| `@TenQuanHuyen` | `nvarchar(400)` | No |
| `@DmTinhThanhPhoREF` | `int(4)` | No |
| `@TenTinhThanhPho` | `nvarchar(400)` | No |
| `@DmQuocGiaREF` | `int(4)` | No |
| `@TenQuocGia` | `nvarchar(400)` | No |
| `@DmLoaiDiaChiREF` | `int(4)` | No |
| `@IsTruSoChinh` | `int(4)` | No |
| `@DiaChiText` | `nvarchar(400)` | No |
| `@ghichu` | `nvarchar(400)` | No |
| `@IsActive` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DiaChi]
	@DmKhachHangThongTinChungREF BIGINT ,
	@SoNha NVARCHAR(200) ,
	@DuongPho NVARCHAR(200) ,
	@DmQuanHuyenREF INT ,
	@TenQuanHuyen NVARCHAR(200) ,
	@DmTinhThanhPhoREF INT ,
	@TenTinhThanhPho NVARCHAR(200) ,
	@DmQuocGiaREF INT ,
	@TenQuocGia NVARCHAR(200) ,
	@DmLoaiDiaChiREF INT ,
	@IsTruSoChinh INT ,
	@DiaChiText NVARCHAR(200) ,
	@ghichu NVARCHAR(200) ,
	@IsActive INT ,
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
	           FROM   [DiaChi]
	           WHERE  [DmKhachHangThongTinChungREF] = @DmKhachHangThongTinChungREF
	       )
	   )
	    UPDATE [dbo].[DiaChi]
	    SET    [SoNha]                        = @SoNha,
	           [DuongPho]                     = @DuongPho,
	           [DmQuanHuyenREF]               = @DmQuanHuyenREF,
	           [TenQuanHuyen]                 = @TenQuanHuyen,
	           [DmTinhThanhPhoREF]            = @DmTinhThanhPhoREF,
	           [TenTinhThanhPho]              = @TenTinhThanhPho,
	           [DmQuocGiaREF]                 = @DmQuocGiaREF,
	           [TenQuocGia]                   = @TenQuocGia,
	           [DmLoaiDiaChiREF]              = @DmLoaiDiaChiREF,
	           [IsTruSoChinh]                 = @IsTruSoChinh,
	           [DiaChiText]                   = @DiaChiText,
	           [ghichu]                       = @ghichu,
	           [Active]                     = @IsActive,
	           [CreatedBy]                    = @CreatedBy,
	           [CreatedAt]                    = @CreatedAt,
	           [LastModifiedBy]               = @LastModifiedBy,
	           [LastModifiedAt]               = @LastModifiedAt,
	           [DeletedStatus]                = @DeletedStatus,
	           [PrintStatus]                  = @PrintStatus,
	           [RecordStatus]                 = @RecordStatus
	    WHERE  [DmKhachHangThongTinChungREF]  = @DmKhachHangThongTinChungREF
	ELSE
	    INSERT INTO [dbo].[DiaChi]
	      (
	        [DmKhachHangThongTinChungREF],
	        [SoNha],
	        [DuongPho],
	        [DmQuanHuyenREF],
	        [TenQuanHuyen],
	        [DmTinhThanhPhoREF],
	        [TenTinhThanhPho],
	        [DmQuocGiaREF],
	        [TenQuocGia],
	        [DmLoaiDiaChiREF],
	        [IsTruSoChinh],
	        [DiaChiText],
	        [ghichu],
	        [Active],
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
	        @DmKhachHangThongTinChungREF,
	        @SoNha,
	        @DuongPho,
	        @DmQuanHuyenREF,
	        @TenQuanHuyen,
	        @DmTinhThanhPhoREF,
	        @TenTinhThanhPho,
	        @DmQuocGiaREF,
	        @TenQuocGia,
	        @DmLoaiDiaChiREF,
	        @IsTruSoChinh,
	        @DiaChiText,
	        @ghichu,
	        @IsActive,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )
```
