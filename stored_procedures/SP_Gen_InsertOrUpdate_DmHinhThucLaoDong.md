# Stored Procedure: `Gen_InsertOrUpdate_DmHinhThucLaoDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:35:52.883000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.260000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmHinhThucLaoDongID` | `int(4)` | No |
| `@TenHinhThucLaoDong` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmHinhThucLaoDong] 	
@DmHinhThucLaoDongID int ,	
@TenHinhThucLaoDong nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmHinhThucLaoDong] where [DmHinhThucLaoDongID] = @DmHinhThucLaoDongID))	
UPDATE [dbo].[DmHinhThucLaoDong] SET 	
[TenHinhThucLaoDong] = @TenHinhThucLaoDong,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmHinhThucLaoDongID] = @DmHinhThucLaoDongID	
else 	
INSERT INTO [dbo].[DmHinhThucLaoDong] (	
[DmHinhThucLaoDongID],	
[TenHinhThucLaoDong],	
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
@DmHinhThucLaoDongID,	
@TenHinhThucLaoDong,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
