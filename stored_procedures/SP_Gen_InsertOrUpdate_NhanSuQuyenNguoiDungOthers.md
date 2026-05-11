# Stored Procedure: `Gen_InsertOrUpdate_NhanSuQuyenNguoiDungOthers`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-12-11 15:52:06.057000
- **Ngày sửa cuối**: 2015-12-11 15:52:06.057000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuQuyenNguoiDungOtherID` | `int(4)` | No |
| `@DmNhomNguoiDungREF` | `int(4)` | No |
| `@MaNhomNguoiDung` | `nvarchar(400)` | No |
| `@TenNhomNguoiDung` | `nvarchar(400)` | No |
| `@LoaiQuyenREF` | `int(4)` | No |
| `@TenLoaiQuyen` | `nvarchar(400)` | No |
| `@ResourceID` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuQuyenNguoiDungOthers] 	
@NhanSuQuyenNguoiDungOtherID int ,	
@DmNhomNguoiDungREF int ,	
@MaNhomNguoiDung nvarchar (200) ,	
@TenNhomNguoiDung nvarchar (200) ,	
@LoaiQuyenREF int ,	
@TenLoaiQuyen nvarchar (200) ,	
@ResourceID int ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@RecordStatus int ,	
@PrintStatus int 	
As 	
if(exists(select * from [NhanSuQuyenNguoiDungOthers] where [NhanSuQuyenNguoiDungOtherID] = @NhanSuQuyenNguoiDungOtherID))	
UPDATE [dbo].[NhanSuQuyenNguoiDungOthers] SET 	
[DmNhomNguoiDungREF] = @DmNhomNguoiDungREF,	
[MaNhomNguoiDung] = @MaNhomNguoiDung,	
[TenNhomNguoiDung] = @TenNhomNguoiDung,	
[LoaiQuyenREF] = @LoaiQuyenREF,	
[TenLoaiQuyen] = @TenLoaiQuyen,	
[ResourceID] = @ResourceID,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[RecordStatus] = @RecordStatus,	
[PrintStatus] = @PrintStatus where [NhanSuQuyenNguoiDungOtherID] = @NhanSuQuyenNguoiDungOtherID	
else 	
INSERT INTO [dbo].[NhanSuQuyenNguoiDungOthers] (	
[NhanSuQuyenNguoiDungOtherID],	
[DmNhomNguoiDungREF],	
[MaNhomNguoiDung],	
[TenNhomNguoiDung],	
[LoaiQuyenREF],	
[TenLoaiQuyen],	
[ResourceID],	
[GhiChu],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[RecordStatus],	
[PrintStatus])	
Values 	
(	
@NhanSuQuyenNguoiDungOtherID,	
@DmNhomNguoiDungREF,	
@MaNhomNguoiDung,	
@TenNhomNguoiDung,	
@LoaiQuyenREF,	
@TenLoaiQuyen,	
@ResourceID,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@RecordStatus,	
@PrintStatus)
```
