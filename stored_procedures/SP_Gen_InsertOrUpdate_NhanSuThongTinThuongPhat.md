# Stored Procedure: `Gen_InsertOrUpdate_NhanSuThongTinThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:37:30.937000
- **Ngày sửa cuối**: 2016-11-16 09:32:19.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuThongTinThuongPhatID` | `int(4)` | No |
| `@TenNhanSu` | `nvarchar(400)` | No |
| `@MaNhanSu` | `nvarchar(400)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@SoHieuThongBao` | `nvarchar(400)` | No |
| `@PhanTramThuongPhat` | `int(4)` | No |
| `@NoiDungThuongPhat` | `nvarchar(400)` | No |
| `@Active` | `bigint(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuThongTinThuongPhat] 	
@NhanSuThongTinThuongPhatID int ,	
@TenNhanSu nvarchar (200) ,	
@MaNhanSu nvarchar (200) ,	
@NhanSuSoYeuLyLichREF int ,	
@SoHieuThongBao nvarchar (200) ,	
@PhanTramThuongPhat int ,	
@NoiDungThuongPhat nvarchar (200) ,	
@Active bigint ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [NhanSuThongTinThuongPhat] where [NhanSuThongTinThuongPhatID] = @NhanSuThongTinThuongPhatID))	
UPDATE [dbo].[NhanSuThongTinThuongPhat] SET 	
[TenNhanSu] = @TenNhanSu,	
[MaNhanSu] = @MaNhanSu,	
[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,	
[SoHieuThongBao] = @SoHieuThongBao,	
[PhanTramThuongPhat] = @PhanTramThuongPhat,	
[NoiDungThuongPhat] = @NoiDungThuongPhat,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [NhanSuThongTinThuongPhatID] = @NhanSuThongTinThuongPhatID	
else 	
INSERT INTO [dbo].[NhanSuThongTinThuongPhat] (	
[NhanSuThongTinThuongPhatID],	
[TenNhanSu],	
[MaNhanSu],	
[NhanSuSoYeuLyLichREF],	
[SoHieuThongBao],	
[PhanTramThuongPhat],	
[NoiDungThuongPhat],	
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
@NhanSuThongTinThuongPhatID,	
@TenNhanSu,	
@MaNhanSu,	
@NhanSuSoYeuLyLichREF,	
@SoHieuThongBao,	
@PhanTramThuongPhat,	
@NoiDungThuongPhat,	
@Active,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)
```
