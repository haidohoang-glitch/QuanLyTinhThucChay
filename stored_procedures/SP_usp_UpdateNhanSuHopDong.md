# Stored Procedure: `usp_UpdateNhanSuHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.033000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.867000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuHopDongID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@TuNgay` | `datetime(8)` | No |
| `@DenNgay` | `datetime(8)` | No |
| `@DmNhanSuLoaiHopDongREF` | `int(4)` | No |
| `@DmHinhThucNhanSuREF` | `int(4)` | No |
| `@HopDongFileName` | `nvarchar(2)` | No |
| `@HopDongFileNameEncode` | `nvarchar(2)` | No |
| `@GhiChu` | `nvarchar(2)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuHopDong]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateNhanSuHopDong]
	@NhanSuHopDongID int,
	@NhanSuSoYeuLyLichREF int,
	@SoHopDong nvarchar(50),
	@NgayKyHopDong datetime,
	@TuNgay datetime,
	@DenNgay datetime,
	@DmNhanSuLoaiHopDongREF int,
	@DmHinhThucNhanSuREF int,
	@HopDongFileName nvarchar(1),
	@HopDongFileNameEncode nvarchar(1),
	@GhiChu nvarchar(1),
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

UPDATE [dbo].[NhanSuHopDong] SET
	[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,
	[SoHopDong] = @SoHopDong,
	[NgayKyHopDong] = @NgayKyHopDong,
	[TuNgay] = @TuNgay,
	[DenNgay] = @DenNgay,
	[DmNhanSuLoaiHopDongREF] = @DmNhanSuLoaiHopDongREF,
	[DmHinhThucNhanSuREF] = @DmHinhThucNhanSuREF,
	[HopDongFileName] = @HopDongFileName,
	[HopDongFileNameEncode] = @HopDongFileNameEncode,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[NhanSuHopDongID] = @NhanSuHopDongID

--endregion

```
