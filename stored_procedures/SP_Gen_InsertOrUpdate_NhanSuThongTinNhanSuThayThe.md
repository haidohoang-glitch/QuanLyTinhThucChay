# Stored Procedure: `Gen_InsertOrUpdate_NhanSuThongTinNhanSuThayThe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:37:33.500000
- **Ngày sửa cuối**: 2016-11-16 09:32:27.577000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuThongTinNhanSuThayTheID` | `int(4)` | No |
| `@TenNhanSuMoi` | `nvarchar(400)` | No |
| `@NhanSuSoYeuLyLichMoiREF` | `int(4)` | No |
| `@TenNhanSuCu` | `nvarchar(400)` | No |
| `@NhanSuSoYeuLyLichCuREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HinhThucTuyenDungID` | `int(4)` | No |
| `@HinhThucTuyenDung` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuThongTinNhanSuThayThe] 	
@NhanSuThongTinNhanSuThayTheID int ,	
@TenNhanSuMoi nvarchar (200) ,	
@NhanSuSoYeuLyLichMoiREF int ,	
@TenNhanSuCu nvarchar (200) ,	
@NhanSuSoYeuLyLichCuREF int ,	
@NgayThucHien datetime ,	
@HinhThucTuyenDungID int ,	
@HinhThucTuyenDung nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@active int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [NhanSuThongTinNhanSuThayThe] where [NhanSuThongTinNhanSuThayTheID] = @NhanSuThongTinNhanSuThayTheID))	
UPDATE [dbo].[NhanSuThongTinNhanSuThayThe] SET 	
[TenNhanSuMoi] = @TenNhanSuMoi,	
[NhanSuSoYeuLyLichMoiREF] = @NhanSuSoYeuLyLichMoiREF,	
[TenNhanSuCu] = @TenNhanSuCu,	
[NhanSuSoYeuLyLichCuREF] = @NhanSuSoYeuLyLichCuREF,	
[NgayThucHien] = @NgayThucHien,	
[HinhThucTuyenDungID] = @HinhThucTuyenDungID,	
[HinhThucTuyenDung] = @HinhThucTuyenDung,	
[GhiChu] = @GhiChu,	
[active] = @active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [NhanSuThongTinNhanSuThayTheID] = @NhanSuThongTinNhanSuThayTheID	
else 	
INSERT INTO [dbo].[NhanSuThongTinNhanSuThayThe] (	
[NhanSuThongTinNhanSuThayTheID],	
[TenNhanSuMoi],	
[NhanSuSoYeuLyLichMoiREF],	
[TenNhanSuCu],	
[NhanSuSoYeuLyLichCuREF],	
[NgayThucHien],	
[HinhThucTuyenDungID],	
[HinhThucTuyenDung],	
[GhiChu],	
[active],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@NhanSuThongTinNhanSuThayTheID,	
@TenNhanSuMoi,	
@NhanSuSoYeuLyLichMoiREF,	
@TenNhanSuCu,	
@NhanSuSoYeuLyLichCuREF,	
@NgayThucHien,	
@HinhThucTuyenDungID,	
@HinhThucTuyenDung,	
@GhiChu,	
@active,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)
```
