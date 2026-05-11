# Stored Procedure: `Gen_InsertOrUpdate_DmNhom`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:36:04.597000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.587000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomID` | `bigint(8)` | No |
| `@TenNhom` | `nvarchar(400)` | No |
| `@DmBoPhanREF` | `bigint(8)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmNhom] 	
@DmNhomID bigint ,	
@TenNhom nvarchar (200) ,	
@DmBoPhanREF bigint ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus bigint ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmNhom] where [DmNhomID] = @DmNhomID))	
UPDATE [dbo].[DmNhom] SET 	
[TenNhom] = @TenNhom,	
[DmBoPhanREF] = @DmBoPhanREF,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmNhomID] = @DmNhomID	
else 	
INSERT INTO [dbo].[DmNhom] (	
[DmNhomID],	
[TenNhom],	
[DmBoPhanREF],	
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
@DmNhomID,	
@TenNhom,	
@DmBoPhanREF,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
