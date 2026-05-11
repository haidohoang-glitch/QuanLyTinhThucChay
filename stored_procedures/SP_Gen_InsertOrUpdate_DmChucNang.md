# Stored Procedure: `Gen_InsertOrUpdate_DmChucNang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:15.570000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.370000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChucNangID` | `int(4)` | No |
| `@TenChucNang` | `nvarchar(400)` | No |
| `@Code` | `nvarchar(400)` | No |
| `@ParentCode` | `nvarchar(400)` | No |
| `@TenHienThi` | `nvarchar(400)` | No |
| `@ThuTuHienThi` | `nvarchar(400)` | No |
| `@HasChildren` | `bigint(8)` | No |
| `@TrangThai` | `int(4)` | No |
| `@Description` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmChucNang] 	
@DmChucNangID int ,	
@TenChucNang nvarchar (200) ,	
@Code nvarchar (200) ,	
@ParentCode nvarchar (200) ,	
@TenHienThi nvarchar (200) ,	
@ThuTuHienThi nvarchar (200) ,	
@HasChildren bigint ,	
@TrangThai int ,	
@Description nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmChucNang] where [DmChucNangID] = @DmChucNangID))	
UPDATE [dbo].[DmChucNang] SET 	
[TenChucNang] = @TenChucNang,	
[Code] = @Code,	
[ParentCode] = @ParentCode,	
[TenHienThi] = @TenHienThi,	
[ThuTuHienThi] = @ThuTuHienThi,	
[HasChildren] = @HasChildren,	
[TrangThai] = @TrangThai,	
[Description] = @Description,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmChucNangID] = @DmChucNangID	
else 	
INSERT INTO [dbo].[DmChucNang] (	
[DmChucNangID],	
[TenChucNang],	
[Code],	
[ParentCode],	
[TenHienThi],	
[ThuTuHienThi],	
[HasChildren],	
[TrangThai],	
[Description],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DmChucNangID,	
@TenChucNang,	
@Code,	
@ParentCode,	
@TenHienThi,	
@ThuTuHienThi,	
@HasChildren,	
@TrangThai,	
@Description,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
