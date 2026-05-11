# Stored Procedure: `Gen_InsertOrUpdate_DmNganHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-26 16:39:38.143000
- **Ngày sửa cuối**: 2016-11-16 09:31:31.830000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNganHangID` | `int(4)` | No |
| `@TenVietTat` | `nvarchar(400)` | No |
| `@TenNganHang` | `nvarchar(400)` | No |
| `@TenGiaoDichTiengAnh` | `nvarchar(400)` | No |
| `@DiaChi` | `nvarchar(400)` | No |
| `@SoDienThoai` | `nvarchar(400)` | No |
| `@Website` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DmNganHang] 	
@DmNganHangID int ,	
@TenVietTat nvarchar (200) ,	
@TenNganHang nvarchar (200) ,	
@TenGiaoDichTiengAnh nvarchar (200) ,	
@DiaChi nvarchar (200) ,	
@SoDienThoai nvarchar (200) ,	
@Website nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DmNganHang] where [DmNganHangID] = @DmNganHangID))	
UPDATE [dbo].[DmNganHang] SET 	
[TenVietTat] = @TenVietTat,	
[TenNganHang] = @TenNganHang,	
[TenGiaoDichTiengAnh] = @TenGiaoDichTiengAnh,	
[DiaChi] = @DiaChi,	
[SoDienThoai] = @SoDienThoai,	
[Website] = @Website,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DmNganHangID] = @DmNganHangID	
else 	
INSERT INTO [dbo].[DmNganHang] (	
[DmNganHangID],	
[TenVietTat],	
[TenNganHang],	
[TenGiaoDichTiengAnh],	
[DiaChi],	
[SoDienThoai],	
[Website],	
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
@DmNganHangID,	
@TenVietTat,	
@TenNganHang,	
@TenGiaoDichTiengAnh,	
@DiaChi,	
@SoDienThoai,	
@Website,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)
```
