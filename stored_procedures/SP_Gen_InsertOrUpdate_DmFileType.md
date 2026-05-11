# Stored Procedure: `Gen_InsertOrUpdate_DmFileType`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 15:44:10.697000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.280000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmFileTypeID` | `bigint(8)` | No |
| `@FileTypeName` | `nvarchar(400)` | No |
| `@Ordering` | `int(4)` | No |
| `@LoaiFileCanBanCung` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmFileType] 	
@DmFileTypeID bigint ,	
@FileTypeName nvarchar (200) ,	
@Ordering int ,	
@LoaiFileCanBanCung int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmFileType] where [DmFileTypeID] = @DmFileTypeID))	
UPDATE [dbo].[DmFileType] SET 	
[FileTypeName] = @FileTypeName,	
[Ordering] = @Ordering,	
[LoaiFileCanBanCung] = @LoaiFileCanBanCung,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmFileTypeID] = @DmFileTypeID	
else 	
INSERT INTO [dbo].[DmFileType] (	
[DmFileTypeID],	
[FileTypeName],	
[Ordering],	
[LoaiFileCanBanCung],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmFileTypeID,	
@FileTypeName,	
@Ordering,	
@LoaiFileCanBanCung,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
