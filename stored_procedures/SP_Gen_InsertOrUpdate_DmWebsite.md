# Stored Procedure: `Gen_InsertOrUpdate_DmWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:28.470000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.667000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmWebsiteID` | `bigint(8)` | No |
| `@DomainWebsite` | `nvarchar(400)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmWebsite] 	
@DmWebsiteID bigint ,	
@DomainWebsite nvarchar (200) ,	
@TenWebsite nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmWebsite] where [DmWebsiteID] = @DmWebsiteID))	
UPDATE [dbo].[DmWebsite] SET 	
[DomainWebsite] = @DomainWebsite,	
[TenWebsite] = @TenWebsite,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmWebsiteID] = @DmWebsiteID	
else 	
INSERT INTO [dbo].[DmWebsite] (	
[DmWebsiteID],	
[DomainWebsite],	
[TenWebsite],	
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
@DmWebsiteID,	
@DomainWebsite,	
@TenWebsite,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
