# Stored Procedure: `Gen_InsertOrUpdate_NhanSuQuaTrinhCongTac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-09 17:34:07.277000
- **Ngày sửa cuối**: 2014-12-04 10:59:06.920000

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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_NhanSuQuaTrinhCongTac]
	@NhanSuQuaTrinhCongTacID INT ,
	@TenNhanSu NVARCHAR(200) ,
	@MaNhanSu NVARCHAR(200) ,
	@NhanSuSoYeuLyLichREF INT ,
	@SoHopDongLaoDong NVARCHAR(200) ,
	@HinhThucLaoDongREF INT ,
	@DmPhongBanREF BIGINT ,
	@DmBoPhanREF BIGINT ,
	@DmNhomREF INT ,
	@DmDiaDiemLamViecREF BIGINT ,
	@DmChucDanhREF INT ,
	@NgayBatDauLamViec DATETIME ,
	@NgayKetThucLamViec DATETIME ,
	@NgayDiLam DATETIME ,
	@NgayNghiViec DATETIME ,
	@GhiChu NVARCHAR(200) ,
	@Active INT ,
	@NhanSuSoYeuLyLichThayTheREF INT ,
	@HinhThucTuyenDungID INT ,
	@HinhThucTuyenDung NVARCHAR(200) ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT
AS
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [NhanSuQuaTrinhCongTac]
	           WHERE  [NhanSuQuaTrinhCongTacID] = @NhanSuQuaTrinhCongTacID
	       )
	   )
	    UPDATE [dbo].[NhanSuQuaTrinhCongTac]
	    SET    [TenNhanSu]                    = @TenNhanSu,
	           [MaNhanSu]                     = @MaNhanSu,
	           [NhanSuSoYeuLyLichREF]         = @NhanSuSoYeuLyLichREF,
	           [SoHopDongLaoDong]             = @SoHopDongLaoDong,
	           [HinhThucLaoDongREF]           = @HinhThucLaoDongREF,
	           [DmPhongBanREF]                = @DmPhongBanREF,
	           [DmBoPhanREF]                  = @DmBoPhanREF,
	           [DmNhomREF]                    = @DmNhomREF,
	           [DmDiaDiemLamViecREF]          = @DmDiaDiemLamViecREF,
	           [DmChucDanhREF]                = @DmChucDanhREF,
	           [NgayBatDauLamViec]            = @NgayBatDauLamViec,
	           [NgayKetThucLamViec]           = @NgayKetThucLamViec,
	           [NgayDiLam]                    = @NgayDiLam,
	           [NgayNghiViec]                 = @NgayNghiViec,
	           [GhiChu]                       = @GhiChu,
	           [Active]                       = @Active,
	           [NhanSuSoYeuLyLichThayTheREF]  = @NhanSuSoYeuLyLichThayTheREF,
	           [HinhThucTuyenDungID]          = @HinhThucTuyenDungID,
	           [HinhThucTuyenDung]            = @HinhThucTuyenDung,
	           [CreatedBy]                    = @CreatedBy,
	           [CreatedAt]                    = @CreatedAt,
	           [LastModifiedBy]               = @LastModifiedBy,
	           [LastModifiedAt]               = @LastModifiedAt,
	           [DeletedStatus]                = @DeletedStatus,
	           [PrintStatus]                  = @PrintStatus,
	           [RecordStatus]                 = @RecordStatus
	    WHERE  [NhanSuQuaTrinhCongTacID]      = @NhanSuQuaTrinhCongTacID
	ELSE
	    INSERT INTO [dbo].[NhanSuQuaTrinhCongTac]
	      (
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
	        [RecordStatus]
	      )
	    VALUES
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
	        @RecordStatus
	      )

```
