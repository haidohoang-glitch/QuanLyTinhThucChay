# Stored Procedure: `Gen_InsertOrUpdate_DmLoaiSanPhamDetail`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:26.263000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiSanPhamDetailId` | `int(4)` | No |
| `@DmLoaiSanPhamFK` | `int(4)` | No |
| `@DmSanPhamFK` | `int(4)` | No |
| `@DmSanPhamName` | `nvarchar(400)` | No |
| `@DmLoaiSanPhamName` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmLoaiSanPhamDetail] 	
@DmLoaiSanPhamDetailId int ,	
@DmLoaiSanPhamFK int ,	
@DmSanPhamFK int ,	
@DmSanPhamName nvarchar (200) ,	
@DmLoaiSanPhamName nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmLoaiSanPhamDetail] where [DmLoaiSanPhamDetailId] = @DmLoaiSanPhamDetailId))	
UPDATE [dbo].[DmLoaiSanPhamDetail] SET 	
[DmLoaiSanPhamFK] = @DmLoaiSanPhamFK,	
[DmSanPhamFK] = @DmSanPhamFK,	
[DmSanPhamName] = @DmSanPhamName,	
[DmLoaiSanPhamName] = @DmLoaiSanPhamName,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmLoaiSanPhamDetailId] = @DmLoaiSanPhamDetailId	
else 	
INSERT INTO [dbo].[DmLoaiSanPhamDetail] (	
[DmLoaiSanPhamDetailId],	
[DmLoaiSanPhamFK],	
[DmSanPhamFK],	
[DmSanPhamName],	
[DmLoaiSanPhamName],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmLoaiSanPhamDetailId,	
@DmLoaiSanPhamFK,	
@DmSanPhamFK,	
@DmSanPhamName,	
@DmLoaiSanPhamName,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
