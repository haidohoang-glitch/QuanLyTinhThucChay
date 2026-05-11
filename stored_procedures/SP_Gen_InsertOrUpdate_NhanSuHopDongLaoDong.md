# Stored Procedure: `Gen_InsertOrUpdate_NhanSuHopDongLaoDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-07 16:36:48.730000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuHopDongLaoDongID` | `int(4)` | No |
| `@TenNhanSu` | `nvarchar(400)` | No |
| `@MaNhanSu` | `nvarchar(400)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@SoHopDongLaoDong` | `nvarchar(400)` | No |
| `@ThoiHanHopDongLaoDong` | `nvarchar(400)` | No |
| `@ThoiHanHopDongLaoDongREF` | `int(4)` | No |
| `@NgayBatDauLamViec` | `datetime(8)` | No |
| `@NgayKetThucLamViec` | `datetime(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@DmHinhThucLaoDongREF` | `int(4)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuHopDongLaoDong] 	
@NhanSuHopDongLaoDongID int ,	
@TenNhanSu nvarchar (200) ,	
@MaNhanSu nvarchar (200) ,	
@NhanSuSoYeuLyLichREF int ,	
@SoHopDongLaoDong nvarchar (200) ,	
@ThoiHanHopDongLaoDong nvarchar (200) ,	
@ThoiHanHopDongLaoDongREF int ,	
@NgayBatDauLamViec datetime ,	
@NgayKetThucLamViec datetime ,	
@NgayKyHopDong datetime ,	
@DmHinhThucLaoDongREF int ,	
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
if(exists(select * from [NhanSuHopDongLaoDong] where [NhanSuHopDongLaoDongID] = @NhanSuHopDongLaoDongID))	
UPDATE [dbo].[NhanSuHopDongLaoDong] SET 	
[TenNhanSu] = @TenNhanSu,	
[MaNhanSu] = @MaNhanSu,	
[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,	
[SoHopDongLaoDong] = @SoHopDongLaoDong,	
[ThoiHanHopDongLaoDong] = @ThoiHanHopDongLaoDong,	
[ThoiHanHopDongLaoDongREF] = @ThoiHanHopDongLaoDongREF,	
[NgayBatDauLamViec] = @NgayBatDauLamViec,	
[NgayKetThucLamViec] = @NgayKetThucLamViec,	
[NgayKyHopDong] = @NgayKyHopDong,	
[DmHinhThucLaoDongREF] = @DmHinhThucLaoDongREF,	
[GhiChu] = @GhiChu,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [NhanSuHopDongLaoDongID] = @NhanSuHopDongLaoDongID	
else 	
INSERT INTO [dbo].[NhanSuHopDongLaoDong] (	
[NhanSuHopDongLaoDongID],	
[TenNhanSu],	
[MaNhanSu],	
[NhanSuSoYeuLyLichREF],	
[SoHopDongLaoDong],	
[ThoiHanHopDongLaoDong],	
[ThoiHanHopDongLaoDongREF],	
[NgayBatDauLamViec],	
[NgayKetThucLamViec],	
[NgayKyHopDong],	
[DmHinhThucLaoDongREF],	
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
@NhanSuHopDongLaoDongID,	
@TenNhanSu,	
@MaNhanSu,	
@NhanSuSoYeuLyLichREF,	
@SoHopDongLaoDong,	
@ThoiHanHopDongLaoDong,	
@ThoiHanHopDongLaoDongREF,	
@NgayBatDauLamViec,	
@NgayKetThucLamViec,	
@NgayKyHopDong,	
@DmHinhThucLaoDongREF,	
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
