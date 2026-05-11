# Stored Procedure: `Gen_InsertOrUpdate_DmNhomNguoiDung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:32:13.647000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomNguoiDungID` | `int(4)` | No |
| `@TenNhomNguoiDung` | `nvarchar(400)` | No |
| `@MaNhomNguoiDung` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmNhomNguoiDung] 	
@DmNhomNguoiDungID int ,	
@TenNhomNguoiDung nvarchar (200) ,	
@MaNhomNguoiDung nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmNhomNguoiDung] where [DmNhomNguoiDungID] = @DmNhomNguoiDungID))	
UPDATE [dbo].[DmNhomNguoiDung] SET 	
[TenNhomNguoiDung] = @TenNhomNguoiDung,	
[MaNhomNguoiDung] = @MaNhomNguoiDung,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmNhomNguoiDungID] = @DmNhomNguoiDungID	
else 	
INSERT INTO [dbo].[DmNhomNguoiDung] (	
[DmNhomNguoiDungID],	
[TenNhomNguoiDung],	
[MaNhomNguoiDung],	
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
@DmNhomNguoiDungID,	
@TenNhomNguoiDung,	
@MaNhomNguoiDung,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
