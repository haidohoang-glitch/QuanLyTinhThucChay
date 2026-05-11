# Stored Procedure: `Gen_InsertOrUpdate_DmTaiKhoanAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:48:42.957000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTaiKhoanAdmarketID` | `int(4)` | No |
| `@TenTaiKhoanAdMarket` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmTaiKhoanAdmarket] 	
@DmTaiKhoanAdmarketID int ,	
@TenTaiKhoanAdMarket nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmTaiKhoanAdmarket] where [DmTaiKhoanAdmarketID] = @DmTaiKhoanAdmarketID))	
UPDATE [dbo].[DmTaiKhoanAdmarket] SET 	
[TenTaiKhoanAdMarket] = @TenTaiKhoanAdMarket,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmTaiKhoanAdmarketID] = @DmTaiKhoanAdmarketID	
else 	
INSERT INTO [dbo].[DmTaiKhoanAdmarket] (	
[DmTaiKhoanAdmarketID],	
[TenTaiKhoanAdMarket],	
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
@DmTaiKhoanAdmarketID,	
@TenTaiKhoanAdMarket,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
