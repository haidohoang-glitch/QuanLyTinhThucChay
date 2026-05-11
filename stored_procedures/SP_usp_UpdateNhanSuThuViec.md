# Stored Procedure: `usp_UpdateNhanSuThuViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.060000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.100000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuThuViecID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@TuNgay` | `datetime(8)` | No |
| `@DenNgay` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateNhanSuThuViec]
	@NhanSuThuViecID int,
	@NhanSuSoYeuLyLichREF int,
	@TuNgay datetime,
	@DenNgay datetime,
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[NhanSuThuViec] SET
	[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,
	[TuNgay] = @TuNgay,
	[DenNgay] = @DenNgay,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[NhanSuThuViecID] = @NhanSuThuViecID

--endregion

```
