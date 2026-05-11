# Stored Procedure: `Gen_InsertOrUpdate_DmBoPhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:36:00.857000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBoPhanID` | `int(4)` | No |
| `@TenBoPhan` | `nvarchar(400)` | No |
| `@DmPhongBanFK` | `int(4)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmBoPhan] 	
@DmBoPhanID int ,	
@TenBoPhan nvarchar (200) ,	
@DmPhongBanFK int ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmBoPhan] where [DmBoPhanID] = @DmBoPhanID))	
UPDATE [dbo].[DmBoPhan] SET 	
[TenBoPhan] = @TenBoPhan,	
[DmPhongBanFK] = @DmPhongBanFK,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmBoPhanID] = @DmBoPhanID	
else 	
INSERT INTO [dbo].[DmBoPhan] (	
[DmBoPhanID],	
[TenBoPhan],	
[DmPhongBanFK],	
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
@DmBoPhanID,	
@TenBoPhan,	
@DmPhongBanFK,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
