# Stored Procedure: `Gen_InsertOrUpdate_DmChucDanh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:35:57
- **Ngày sửa cuối**: 2016-11-16 09:31:32.997000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChucDanhID` | `int(4)` | No |
| `@MaChucDanh` | `nvarchar(400)` | No |
| `@TenChucDanh` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `bigint(8)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmChucDanh] 	
@DmChucDanhID int ,	
@MaChucDanh nvarchar (200) ,	
@TenChucDanh nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@Active int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmChucDanh] where [DmChucDanhID] = @DmChucDanhID))	
UPDATE [dbo].[DmChucDanh] SET 	
[MaChucDanh] = @MaChucDanh,	
[TenChucDanh] = @TenChucDanh,	
[GhiChu] = @GhiChu,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmChucDanhID] = @DmChucDanhID	
else 	
INSERT INTO [dbo].[DmChucDanh] (	
[DmChucDanhID],	
[MaChucDanh],	
[TenChucDanh],	
[GhiChu],	
[Active],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmChucDanhID,	
@MaChucDanh,	
@TenChucDanh,	
@GhiChu,	
@Active,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)
```
