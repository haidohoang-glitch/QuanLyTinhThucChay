# Stored Procedure: `usp_UpdateNhanSuTinhTrang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.157000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.033000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuTinhTrangID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@DmNhanSuTinhTrangREF` | `int(4)` | No |
| `@DmNhomLamViecREF` | `int(4)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuTinhTrang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateNhanSuTinhTrang]
	@NhanSuTinhTrangID int,
	@NhanSuSoYeuLyLichREF int,
	@NgayBatDau datetime,
	@NgayKetThuc datetime,
	@DmNhanSuTinhTrangREF int,
	@DmNhomLamViecREF int,
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

UPDATE [dbo].[NhanSuTinhTrang] SET
	[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,
	[NgayBatDau] = @NgayBatDau,
	[NgayKetThuc] = @NgayKetThuc,
	[DmNhanSuTinhTrangREF] = @DmNhanSuTinhTrangREF,
	[DmNhomLamViecREF] = @DmNhomLamViecREF,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[NhanSuTinhTrangID] = @NhanSuTinhTrangID

--endregion

```
