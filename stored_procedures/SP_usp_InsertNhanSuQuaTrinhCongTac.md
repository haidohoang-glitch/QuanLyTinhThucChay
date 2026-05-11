# Stored Procedure: `usp_InsertNhanSuQuaTrinhCongTac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.293000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuQuaTrinhCongTacID` | `int(4)` | No |
| `@SoHopDongLaoDong` | `nvarchar(100)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@HinhThucLaoDong` | `int(4)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomLamViecREF` | `int(4)` | No |
| `@DmDiaDiemLamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |
| `@NgayBatDauLamViec` | `datetime(8)` | No |
| `@NgayNghiViec` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_InsertNhanSuQuaTrinhCongTac]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertNhanSuQuaTrinhCongTac]
	@NhanSuQuaTrinhCongTacID int,
	@SoHopDongLaoDong nvarchar(50),
	@NhanSuSoYeuLyLichREF int,
	@HinhThucLaoDong int,
	@DmPhongBanREF int,
	@DmBoPhanREF int,
	@DmNhomLamViecREF int,
	@DmDiaDiemLamViecREF int,
	@DmChucDanhREF int,
	@NgayBatDauLamViec datetime,
	@NgayNghiViec datetime,
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON
IF(EXISTS(SELECT * FROM dbo.NhanSuQuaTrinhCongTac WHERE NhanSuQuaTrinhCongTacID = @NhanSuQuaTrinhCongTacID AND DeletedStatus <> 1))
UPDATE [dbo].[NhanSuQuaTrinhCongTac] SET
	[SoHopDongLaoDong] = @SoHopDongLaoDong,
	[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,
	[HinhThucLaoDong] = @HinhThucLaoDong,
	[DmPhongBanREF] = @DmPhongBanREF,
	[DmBoPhanREF] = @DmBoPhanREF,
	[DmNhomLamViecREF] = @DmNhomLamViecREF,
	[DmDiaDiemLamViecREF] = @DmDiaDiemLamViecREF,
	[DmChucDanhREF] = @DmChucDanhREF,
	[NgayBatDauLamViec] = @NgayBatDauLamViec,
	[NgayNghiViec] = @NgayNghiViec,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[NhanSuQuaTrinhCongTacID] = @NhanSuQuaTrinhCongTacID
else
INSERT INTO [dbo].[NhanSuQuaTrinhCongTac] (
	[NhanSuQuaTrinhCongTacID],
	[SoHopDongLaoDong],
	[NhanSuSoYeuLyLichREF],
	[HinhThucLaoDong],
	[DmPhongBanREF],
	[DmBoPhanREF],
	[DmNhomLamViecREF],
	[DmDiaDiemLamViecREF],
	[DmChucDanhREF],
	[NgayBatDauLamViec],
	[NgayNghiViec],
	[GhiChu],
	[Active],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@NhanSuQuaTrinhCongTacID,
	@SoHopDongLaoDong,
	@NhanSuSoYeuLyLichREF,
	@HinhThucLaoDong,
	@DmPhongBanREF,
	@DmBoPhanREF,
	@DmNhomLamViecREF,
	@DmDiaDiemLamViecREF,
	@DmChucDanhREF,
	@NgayBatDauLamViec,
	@NgayNghiViec,
	@GhiChu,
	@Active,
	@CreatedBy,
	@CreatedAt,
	@LastModifiedBy,
	@LastModifiedAt,
	@DeletedStatus,
	@PrintStatus,
	@RecordStatus
)

--endregion

```
