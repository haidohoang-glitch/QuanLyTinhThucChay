# Stored Procedure: `Gen_InsertOrUpdate_DmTaiKhoanGGAndFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-05 11:28:20.363000
- **Ngày sửa cuối**: 2015-03-05 11:28:20.363000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTaiKhoanGGAndFBID` | `int(4)` | No |
| `@TenTaiKhoan` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@DeleteStatus` | `int(4)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_DmTaiKhoanGGAndFB] 	
@DmTaiKhoanGGAndFBID int ,	
@TenTaiKhoan nvarchar (200) ,	
@DmSanPhamREF int ,	
@GhiChu nvarchar (200) ,	
@DeleteStatus int ,	
@CreatedAt datetime ,	
@CreatedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@LastModifiedBy nvarchar (200) 	
As 	
if(exists(select * from [DmTaiKhoanGGAndFB] where [DmTaiKhoanGGAndFBID] = @DmTaiKhoanGGAndFBID))	
UPDATE [dbo].[DmTaiKhoanGGAndFB] SET 	
[TenTaiKhoan] = @TenTaiKhoan,	
[DmSanPhamREF] = @DmSanPhamREF,	
[GhiChu] = @GhiChu,	
[DeleteStatus] = @DeleteStatus,	
[CreatedAt] = @CreatedAt,	
[CreatedBy] = @CreatedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[LastModifiedBy] = @LastModifiedBy where [DmTaiKhoanGGAndFBID] = @DmTaiKhoanGGAndFBID	
else 	
INSERT INTO [dbo].[DmTaiKhoanGGAndFB] (	
[DmTaiKhoanGGAndFBID],	
[TenTaiKhoan],	
[DmSanPhamREF],	
[GhiChu],	
[DeleteStatus],	
[CreatedAt],	
[CreatedBy],	
[LastModifiedAt],	
[LastModifiedBy])	
Values 	
(	
@DmTaiKhoanGGAndFBID,	
@TenTaiKhoan,	
@DmSanPhamREF,	
@GhiChu,	
@DeleteStatus,	
@CreatedAt,	
@CreatedBy,	
@LastModifiedAt,	
@LastModifiedBy)
```
