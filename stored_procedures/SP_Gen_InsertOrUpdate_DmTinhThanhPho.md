# Stored Procedure: `Gen_InsertOrUpdate_DmTinhThanhPho`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-26 16:39:34.700000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTinhThanhPhoID` | `int(4)` | No |
| `@TenTinhThanhPho` | `nvarchar(400)` | No |
| `@DmDatNuocREF` | `int(4)` | No |
| `@ThuTuHienThi` | `int(4)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmTinhThanhPho] 	
@DmTinhThanhPhoID int ,	
@TenTinhThanhPho nvarchar (200) ,	
@DmDatNuocREF int ,	
@ThuTuHienThi int ,	
@Active int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmTinhThanhPho] where [DmTinhThanhPhoID] = @DmTinhThanhPhoID))	
UPDATE [dbo].[DmTinhThanhPho] SET 	
[TenTinhThanhPho] = @TenTinhThanhPho,	
[DmDatNuocREF] = @DmDatNuocREF,	
[ThuTuHienThi] = @ThuTuHienThi,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmTinhThanhPhoID] = @DmTinhThanhPhoID	
else 	
INSERT INTO [dbo].[DmTinhThanhPho] (	
[DmTinhThanhPhoID],	
[TenTinhThanhPho],	
[DmDatNuocREF],	
[ThuTuHienThi],	
[Active],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmTinhThanhPhoID,	
@TenTinhThanhPho,	
@DmDatNuocREF,	
@ThuTuHienThi,	
@Active,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
