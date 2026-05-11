# Stored Procedure: `Gen_InsertOrUpdate_DmLoaiBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:36.880000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.217000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiBannerID` | `int(4)` | No |
| `@MaLoaiBanner` | `nvarchar(400)` | No |
| `@TenLoaiBanner` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmLoaiBanner] 	
@DmLoaiBannerID int ,	
@MaLoaiBanner nvarchar (200) ,	
@TenLoaiBanner nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmLoaiBanner] where [DmLoaiBannerID] = @DmLoaiBannerID))	
UPDATE [dbo].[DmLoaiBanner] SET 	
[MaLoaiBanner] = @MaLoaiBanner,	
[TenLoaiBanner] = @TenLoaiBanner,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmLoaiBannerID] = @DmLoaiBannerID	
else 	
INSERT INTO [dbo].[DmLoaiBanner] (	
[DmLoaiBannerID],	
[MaLoaiBanner],	
[TenLoaiBanner],	
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
@DmLoaiBannerID,	
@MaLoaiBanner,	
@TenLoaiBanner,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
