# Stored Procedure: `Gen_InsertOrUpdate_DmHinhThucQuangCao`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-10 10:54:02.710000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.237000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmHinhThucQuangCaoID` | `int(4)` | No |
| `@MaDmHinhThucQuangCao` | `nvarchar(400)` | No |
| `@TenHinhThucQuangCao` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmHinhThucQuangCao] 	
@DmHinhThucQuangCaoID int ,	
@MaDmHinhThucQuangCao nvarchar (200) ,	
@TenHinhThucQuangCao nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmHinhThucQuangCao] where [DmHinhThucQuangCaoID] = @DmHinhThucQuangCaoID))	
UPDATE [dbo].[DmHinhThucQuangCao] SET 	
[MaDmHinhThucQuangCao] = @MaDmHinhThucQuangCao,	
[TenHinhThucQuangCao] = @TenHinhThucQuangCao,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmHinhThucQuangCaoID] = @DmHinhThucQuangCaoID	
else 	
INSERT INTO [dbo].[DmHinhThucQuangCao] (	
[DmHinhThucQuangCaoID],	
[MaDmHinhThucQuangCao],	
[TenHinhThucQuangCao],	
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
@DmHinhThucQuangCaoID,	
@MaDmHinhThucQuangCao,	
@TenHinhThucQuangCao,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
