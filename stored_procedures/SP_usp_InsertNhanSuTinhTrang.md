# Stored Procedure: `usp_InsertNhanSuTinhTrang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.133000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.047000

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
-- Stored Procedure Name: [dbo].[usp_InsertNhanSuTinhTrang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertNhanSuTinhTrang]
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

INSERT INTO [dbo].[NhanSuTinhTrang] (
	[NhanSuTinhTrangID],
	[NhanSuSoYeuLyLichREF],
	[NgayBatDau],
	[NgayKetThuc],
	[DmNhanSuTinhTrangREF],
	[DmNhomLamViecREF],
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
	@NhanSuTinhTrangID,
	@NhanSuSoYeuLyLichREF,
	@NgayBatDau,
	@NgayKetThuc,
	@DmNhanSuTinhTrangREF,
	@DmNhomLamViecREF,
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
