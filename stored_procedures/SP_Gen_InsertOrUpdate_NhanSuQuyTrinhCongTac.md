# Stored Procedure: `Gen_InsertOrUpdate_NhanSuQuyTrinhCongTac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-09 16:29:24.437000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.073000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuQuaTrinhCongTacID` | `int(4)` | No |
| `@TenNhanSu` | `nvarchar(400)` | No |
| `@MaNhanSu` | `nvarchar(400)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@SoHopDongLaoDong` | `nvarchar(400)` | No |
| `@HinhThucLaoDongREF` | `int(4)` | No |
| `@DmPhongBanREF` | `bigint(8)` | No |
| `@DmBoPhanREF` | `bigint(8)` | No |
| `@DmNhomREF` | `int(4)` | No |
| `@DmDiaDiemLamViecREF` | `bigint(8)` | No |
| `@DmChucDanhREF` | `int(4)` | No |
| `@NgayBatDauLamViec` | `datetime(8)` | No |
| `@NgayKetThucLamViec` | `datetime(8)` | No |
| `@NgayDiLam` | `datetime(8)` | No |
| `@NgayNghiViec` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Active` | `int(4)` | No |
| `@NhanSuSoYeuLyLichThayTheREF` | `int(4)` | No |
| `@HinhThucTuyenDungID` | `int(4)` | No |
| `@HinhThucTuyenDung` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuQuyTrinhCongTac] 	
@NhanSuQuaTrinhCongTacID int ,	
@TenNhanSu nvarchar (200) ,	
@MaNhanSu nvarchar (200) ,	
@NhanSuSoYeuLyLichREF int ,	
@SoHopDongLaoDong nvarchar (200) ,	
@HinhThucLaoDongREF int ,	
@DmPhongBanREF bigint ,	
@DmBoPhanREF bigint ,	
@DmNhomREF int ,	
@DmDiaDiemLamViecREF bigint ,	
@DmChucDanhREF int ,	
@NgayBatDauLamViec datetime ,	
@NgayKetThucLamViec datetime ,	
@NgayDiLam datetime ,	
@NgayNghiViec datetime ,	
@GhiChu nvarchar (200) ,	
@Active int ,	
@NhanSuSoYeuLyLichThayTheREF int ,	
@HinhThucTuyenDungID int ,	
@HinhThucTuyenDung nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [NhanSuQuyTrinhCongTac] where 1>2))	
UPDATE [dbo].[NhanSuQuyTrinhCongTac] SET 	
[NhanSuQuaTrinhCongTacID] = @NhanSuQuaTrinhCongTacID,	
[TenNhanSu] = @TenNhanSu,	
[MaNhanSu] = @MaNhanSu,	
[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,	
[SoHopDongLaoDong] = @SoHopDongLaoDong,	
[HinhThucLaoDongREF] = @HinhThucLaoDongREF,	
[DmPhongBanREF] = @DmPhongBanREF,	
[DmBoPhanREF] = @DmBoPhanREF,	
[DmNhomREF] = @DmNhomREF,	
[DmDiaDiemLamViecREF] = @DmDiaDiemLamViecREF,	
[DmChucDanhREF] = @DmChucDanhREF,	
[NgayBatDauLamViec] = @NgayBatDauLamViec,	
[NgayKetThucLamViec] = @NgayKetThucLamViec,	
[NgayDiLam] = @NgayDiLam,	
[NgayNghiViec] = @NgayNghiViec,	
[GhiChu] = @GhiChu,	
[Active] = @Active,	
[NhanSuSoYeuLyLichThayTheREF] = @NhanSuSoYeuLyLichThayTheREF,	
[HinhThucTuyenDungID] = @HinhThucTuyenDungID,	
[HinhThucTuyenDung] = @HinhThucTuyenDung,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where 1>2	
else 	
INSERT INTO [dbo].[NhanSuQuyTrinhCongTac] (	
[NhanSuQuaTrinhCongTacID],	
[TenNhanSu],	
[MaNhanSu],	
[NhanSuSoYeuLyLichREF],	
[SoHopDongLaoDong],	
[HinhThucLaoDongREF],	
[DmPhongBanREF],	
[DmBoPhanREF],	
[DmNhomREF],	
[DmDiaDiemLamViecREF],	
[DmChucDanhREF],	
[NgayBatDauLamViec],	
[NgayKetThucLamViec],	
[NgayDiLam],	
[NgayNghiViec],	
[GhiChu],	
[Active],	
[NhanSuSoYeuLyLichThayTheREF],	
[HinhThucTuyenDungID],	
[HinhThucTuyenDung],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@NhanSuQuaTrinhCongTacID,	
@TenNhanSu,	
@MaNhanSu,	
@NhanSuSoYeuLyLichREF,	
@SoHopDongLaoDong,	
@HinhThucLaoDongREF,	
@DmPhongBanREF,	
@DmBoPhanREF,	
@DmNhomREF,	
@DmDiaDiemLamViecREF,	
@DmChucDanhREF,	
@NgayBatDauLamViec,	
@NgayKetThucLamViec,	
@NgayDiLam,	
@NgayNghiViec,	
@GhiChu,	
@Active,	
@NhanSuSoYeuLyLichThayTheREF,	
@HinhThucTuyenDungID,	
@HinhThucTuyenDung,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
