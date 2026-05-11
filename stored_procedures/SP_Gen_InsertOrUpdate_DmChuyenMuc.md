# Stored Procedure: `Gen_InsertOrUpdate_DmChuyenMuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:57:25.877000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.357000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChuyenMucID` | `int(4)` | No |
| `@TenChuyenMuc` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmChuyenMuc] 	
@DmChuyenMucID int ,	
@TenChuyenMuc nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmChuyenMuc] where [DmChuyenMucID] = @DmChuyenMucID))	
UPDATE [dbo].[DmChuyenMuc] SET 	
[TenChuyenMuc] = @TenChuyenMuc,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmChuyenMucID] = @DmChuyenMucID	
else 	
INSERT INTO [dbo].[DmChuyenMuc] (	
[DmChuyenMucID],	
[TenChuyenMuc],	
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
@DmChuyenMucID,	
@TenChuyenMuc,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
