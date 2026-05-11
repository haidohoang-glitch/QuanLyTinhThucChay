# Stored Procedure: `Gen_InsertOrUpdate_DmQuanHuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 14:43:53.043000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmQuanHuyenID` | `int(4)` | No |
| `@DmTinhThanhPhoREF` | `int(4)` | No |
| `@TenQuanHuyen` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmQuanHuyen] 	
@DmQuanHuyenID int ,	
@DmTinhThanhPhoREF int ,	
@TenQuanHuyen nvarchar (200) ,	
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
if(exists(select * from [DmQuanHuyen] where [DmQuanHuyenID] = @DmQuanHuyenID))	
UPDATE [dbo].[DmQuanHuyen] SET 	
[DmTinhThanhPhoREF] = @DmTinhThanhPhoREF,	
[TenQuanHuyen] = @TenQuanHuyen,	
[ThuTuHienThi] = @ThuTuHienThi,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmQuanHuyenID] = @DmQuanHuyenID	
else 	
INSERT INTO [dbo].[DmQuanHuyen] (	
[DmQuanHuyenID],	
[DmTinhThanhPhoREF],	
[TenQuanHuyen],	
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
@DmQuanHuyenID,	
@DmTinhThanhPhoREF,	
@TenQuanHuyen,	
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
