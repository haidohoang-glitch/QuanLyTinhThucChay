# Stored Procedure: `usp_InsertNhanSuTrangThietBi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.237000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.027000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuTrangThietBiID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@DmTrangThietBiREF` | `int(4)` | No |
| `@NgayCap` | `datetime(8)` | No |
| `@NgayHetHan` | `datetime(8)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertNhanSuTrangThietBi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertNhanSuTrangThietBi]
	@NhanSuTrangThietBiID int,
	@NhanSuSoYeuLyLichREF int,
	@DmTrangThietBiREF int,
	@NgayCap datetime,
	@NgayHetHan datetime,
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

INSERT INTO [dbo].[NhanSuTrangThietBi] (
	[NhanSuTrangThietBiID],
	[NhanSuSoYeuLyLichREF],
	[DmTrangThietBiREF],
	[NgayCap],
	[NgayHetHan],
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
	@NhanSuTrangThietBiID,
	@NhanSuSoYeuLyLichREF,
	@DmTrangThietBiREF,
	@NgayCap,
	@NgayHetHan,
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
