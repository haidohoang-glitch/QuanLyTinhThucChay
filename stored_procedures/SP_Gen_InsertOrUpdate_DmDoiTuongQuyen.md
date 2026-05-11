# Stored Procedure: `Gen_InsertOrUpdate_DmDoiTuongQuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:22.990000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.323000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmDoiTuongQuyenID` | `int(4)` | No |
| `@TenDoiTuongQuyen` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmDoiTuongQuyen] 	
@DmDoiTuongQuyenID int ,	
@TenDoiTuongQuyen nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmDoiTuongQuyen] where [DmDoiTuongQuyenID] = @DmDoiTuongQuyenID))	
UPDATE [dbo].[DmDoiTuongQuyen] SET 	
[TenDoiTuongQuyen] = @TenDoiTuongQuyen,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmDoiTuongQuyenID] = @DmDoiTuongQuyenID	
else 	
INSERT INTO [dbo].[DmDoiTuongQuyen] (	
[DmDoiTuongQuyenID],	
[TenDoiTuongQuyen],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmDoiTuongQuyenID,	
@TenDoiTuongQuyen,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
