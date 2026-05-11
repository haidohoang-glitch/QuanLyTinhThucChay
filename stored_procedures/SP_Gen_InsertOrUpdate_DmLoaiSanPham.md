# Stored Procedure: `Gen_InsertOrUpdate_DmLoaiSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:22.933000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.493000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiSanPhamID` | `int(4)` | No |
| `@MaLoaiSanPham` | `nvarchar(400)` | No |
| `@TenLoaiSanPham` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmLoaiSanPham] 	
@DmLoaiSanPhamID int ,	
@MaLoaiSanPham nvarchar (200) ,	
@TenLoaiSanPham nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmLoaiSanPham] where [DmLoaiSanPhamID] = @DmLoaiSanPhamID))	
UPDATE [dbo].[DmLoaiSanPham] SET 	
[MaLoaiSanPham] = @MaLoaiSanPham,	
[TenLoaiSanPham] = @TenLoaiSanPham,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmLoaiSanPhamID] = @DmLoaiSanPhamID	
else 	
INSERT INTO [dbo].[DmLoaiSanPham] (	
[DmLoaiSanPhamID],	
[MaLoaiSanPham],	
[TenLoaiSanPham],	
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
@DmLoaiSanPhamID,	
@MaLoaiSanPham,	
@TenLoaiSanPham,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
