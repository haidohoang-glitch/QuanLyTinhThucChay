# Stored Procedure: `Gen_InsertOrUpdate_HopDongThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:42:00.980000
- **Ngày sửa cuối**: 2017-07-13 17:03:00.553000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongThayDoiID` | `int(4)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@LoaiThayDoi` | `int(4)` | No |
| `@NgayThayDoi` | `datetime(8)` | No |
| `@NganhHang` | `nvarchar(400)` | No |
| `@NhanHopDong` | `nvarchar(400)` | No |
| `@GiaTriHopDong` | `float(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongThayDoi] 	
@HopDongThayDoiID int ,	
@HopDongFK int ,	
@LoaiThayDoi int ,	
@NgayThayDoi datetime ,	
@NganhHang nvarchar (200) ,	
@NhanHopDong nvarchar (200) ,	
@GiaTriHopDong float ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [HopDongThayDoi] where [HopDongThayDoiID] = @HopDongThayDoiID))	
UPDATE [dbo].[HopDongThayDoi] SET 	
[HopDongFK] = @HopDongFK,	
[LoaiThayDoi] = @LoaiThayDoi,	
[NgayThayDoi] = @NgayThayDoi,	
[NganhHang] = @NganhHang,	
[NhanHopDong] = @NhanHopDong,	
[GiaTriHopDong] = @GiaTriHopDong,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [HopDongThayDoiID] = @HopDongThayDoiID	
else 	
INSERT INTO [dbo].[HopDongThayDoi] (	
[HopDongThayDoiID],	
[HopDongFK],	
[LoaiThayDoi],	
[NgayThayDoi],	
[NganhHang],	
[NhanHopDong],	
[GiaTriHopDong],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@HopDongThayDoiID,	
@HopDongFK,	
@LoaiThayDoi,	
@NgayThayDoi,	
@NganhHang,	
@NhanHopDong,	
@GiaTriHopDong,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
