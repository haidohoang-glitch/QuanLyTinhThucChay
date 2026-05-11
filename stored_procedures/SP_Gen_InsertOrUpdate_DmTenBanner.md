# Stored Procedure: `Gen_InsertOrUpdate_DmTenBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:32.363000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.787000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |
| `@TenBanner` | `nvarchar(400)` | No |
| `@InTypeTool` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmTenBanner] 	
@DmBannerID int ,	
@TenBanner nvarchar (200) ,	
@InTypeTool nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmTenBanner] where [DmBannerID] = @DmBannerID))	
UPDATE [dbo].[DmTenBanner] SET 	
[TenBanner] = @TenBanner,	
[InTypeTool] = @InTypeTool,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmBannerID] = @DmBannerID	
else 	
INSERT INTO [dbo].[DmTenBanner] (	
[DmBannerID],	
[TenBanner],	
[InTypeTool],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmBannerID,	
@TenBanner,	
@InTypeTool,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
