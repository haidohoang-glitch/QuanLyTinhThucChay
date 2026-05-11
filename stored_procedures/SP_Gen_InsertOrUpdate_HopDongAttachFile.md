# Stored Procedure: `Gen_InsertOrUpdate_HopDongAttachFile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:42:26.770000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.893000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongAttachFileID` | `bigint(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@fileName` | `nvarchar(400)` | No |
| `@Url` | `nvarchar(400)` | No |
| `@FileTypeREF` | `int(4)` | No |
| `@description` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongAttachFile] 	
@HopDongAttachFileID bigint ,	
@HopDongREF int ,	
@fileName nvarchar (200) ,	
@Url nvarchar (200) ,	
@FileTypeREF int ,	
@description nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [HopDongAttachFile] where [HopDongAttachFileID] = @HopDongAttachFileID))	
UPDATE [dbo].[HopDongAttachFile] SET 	
[HopDongREF] = @HopDongREF,	
[fileName] = @fileName,	
[Url] = @Url,	
[FileTypeREF] = @FileTypeREF,	
[description] = @description,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [HopDongAttachFileID] = @HopDongAttachFileID	
else 	
INSERT INTO [dbo].[HopDongAttachFile] (	
[HopDongAttachFileID],	
[HopDongREF],	
[fileName],	
[Url],	
[FileTypeREF],	
[description],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@HopDongAttachFileID,	
@HopDongREF,	
@fileName,	
@Url,	
@FileTypeREF,	
@description,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
