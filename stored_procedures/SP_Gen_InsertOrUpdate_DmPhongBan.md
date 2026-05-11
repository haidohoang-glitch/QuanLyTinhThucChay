# Stored Procedure: `Gen_InsertOrUpdate_DmPhongBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:35:58.783000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.523000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhongBanID` | `int(4)` | No |
| `@MaSoPhongBan` | `nvarchar(400)` | No |
| `@TenPhongBan` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmPhongBan] 	
@DmPhongBanID int ,	
@MaSoPhongBan nvarchar (200) ,	
@TenPhongBan nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmPhongBan] where [DmPhongBanID] = @DmPhongBanID))	
UPDATE [dbo].[DmPhongBan] SET 	
[MaSoPhongBan] = @MaSoPhongBan,	
[TenPhongBan] = @TenPhongBan,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmPhongBanID] = @DmPhongBanID	
else 	
INSERT INTO [dbo].[DmPhongBan] (	
[DmPhongBanID],	
[MaSoPhongBan],	
[TenPhongBan],	
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
@DmPhongBanID,	
@MaSoPhongBan,	
@TenPhongBan,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
