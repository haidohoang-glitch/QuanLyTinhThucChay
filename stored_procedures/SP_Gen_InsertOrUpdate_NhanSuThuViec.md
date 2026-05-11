# Stored Procedure: `Gen_InsertOrUpdate_NhanSuThuViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:36:34.060000
- **Ngày sửa cuối**: 2016-11-16 09:31:47.447000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuThuViecID` | `int(4)` | No |
| `@TenNhanSu` | `nvarchar(400)` | No |
| `@MaNhanSu` | `nvarchar(400)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@NgayBatDauThuViec` | `datetime(8)` | No |
| `@NgayKetThucThuViec` | `datetime(8)` | No |
| `@NgayDanhGia` | `datetime(8)` | No |
| `@NoiDungDanhGia` | `nvarchar(400)` | No |
| `@KetQuaHoanThanhThuViecYN` | `int(4)` | No |
| `@NhanSuSoYeuLyLichDanhGiaREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuThuViec] 	
@NhanSuThuViecID int ,	
@TenNhanSu nvarchar (200) ,	
@MaNhanSu nvarchar (200) ,	
@NhanSuSoYeuLyLichREF int ,	
@NgayBatDauThuViec datetime ,	
@NgayKetThucThuViec datetime ,	
@NgayDanhGia datetime ,	
@NoiDungDanhGia nvarchar (200) ,	
@KetQuaHoanThanhThuViecYN int ,	
@NhanSuSoYeuLyLichDanhGiaREF int ,	
@GhiChu nvarchar (200) ,	
@Active bigint ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [NhanSuThuViec] where [NhanSuThuViecID] = @NhanSuThuViecID))	
UPDATE [dbo].[NhanSuThuViec] SET 	
[TenNhanSu] = @TenNhanSu,	
[MaNhanSu] = @MaNhanSu,	
[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,	
[NgayBatDauThuViec] = @NgayBatDauThuViec,	
[NgayKetThucThuViec] = @NgayKetThucThuViec,	
[NgayDanhGia] = @NgayDanhGia,	
[NoiDungDanhGia] = @NoiDungDanhGia,	
[KetQuaHoanThanhThuViecYN] = @KetQuaHoanThanhThuViecYN,	
[NhanSuSoYeuLyLichDanhGiaREF] = @NhanSuSoYeuLyLichDanhGiaREF,	
[GhiChu] = @GhiChu,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [NhanSuThuViecID] = @NhanSuThuViecID	
else 	
INSERT INTO [dbo].[NhanSuThuViec] (	
[NhanSuThuViecID],	
[TenNhanSu],	
[MaNhanSu],	
[NhanSuSoYeuLyLichREF],	
[NgayBatDauThuViec],	
[NgayKetThucThuViec],	
[NgayDanhGia],	
[NoiDungDanhGia],	
[KetQuaHoanThanhThuViecYN],	
[NhanSuSoYeuLyLichDanhGiaREF],	
[GhiChu],	
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
@NhanSuThuViecID,	
@TenNhanSu,	
@MaNhanSu,	
@NhanSuSoYeuLyLichREF,	
@NgayBatDauThuViec,	
@NgayKetThucThuViec,	
@NgayDanhGia,	
@NoiDungDanhGia,	
@KetQuaHoanThanhThuViecYN,	
@NhanSuSoYeuLyLichDanhGiaREF,	
@GhiChu,	
@Active,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)
```
