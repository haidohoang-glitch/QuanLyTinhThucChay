# Stored Procedure: `Gen_InsertOrUpdate_DmNhomWebsiteTag`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:30.510000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.550000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomWebsiteTagID` | `int(4)` | No |
| `@TenNhomWebsiteTag` | `nvarchar(400)` | No |
| `@TypeNhomWebsiteTag` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmNhomWebsiteTag] 	
@DmNhomWebsiteTagID int ,	
@TenNhomWebsiteTag nvarchar (200) ,	
@TypeNhomWebsiteTag int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmNhomWebsiteTag] where [DmNhomWebsiteTagID] = @DmNhomWebsiteTagID))	
UPDATE [dbo].[DmNhomWebsiteTag] SET 	
[TenNhomWebsiteTag] = @TenNhomWebsiteTag,	
[TypeNhomWebsiteTag] = @TypeNhomWebsiteTag,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmNhomWebsiteTagID] = @DmNhomWebsiteTagID	
else 	
INSERT INTO [dbo].[DmNhomWebsiteTag] (	
[DmNhomWebsiteTagID],	
[TenNhomWebsiteTag],	
[TypeNhomWebsiteTag],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmNhomWebsiteTagID,	
@TenNhomWebsiteTag,	
@TypeNhomWebsiteTag,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
