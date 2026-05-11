# Stored Procedure: `Gen_InsertOrUpdate_DmSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:24.527000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.673000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamID` | `bigint(8)` | No |
| `@MaSanPham` | `nvarchar(400)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `bigint(8)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmSanPham] 	
@DmSanPhamID bigint ,	
@MaSanPham nvarchar (200) ,	
@TenSanPham nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmSanPham] where [DmSanPhamID] = @DmSanPhamID))	
UPDATE [dbo].[DmSanPham] SET 	
[MaSanPham] = @MaSanPham,	
[TenSanPham] = @TenSanPham,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmSanPhamID] = @DmSanPhamID	
else 	
INSERT INTO [dbo].[DmSanPham] (	
[DmSanPhamID],	
[MaSanPham],	
[TenSanPham],	
[GhiChu],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmSanPhamID,	
@MaSanPham,	
@TenSanPham,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
