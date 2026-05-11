# Stored Procedure: `usp_UpdateDmTinhTrangLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:16.013000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.800000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTinhTrangLamViecID` | `int(4)` | No |
| `@MaTinhTrangLamViec` | `nvarchar(100)` | No |
| `@TenTinhTrangLamViec` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDmTinhTrangLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmTinhTrangLamViec]
	@DmTinhTrangLamViecID int,
	@MaTinhTrangLamViec nvarchar(50),
	@TenTinhTrangLamViec nvarchar(200),
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

UPDATE [dbo].[DmTinhTrangLamViec] SET
	[MaTinhTrangLamViec] = @MaTinhTrangLamViec,
	[TenTinhTrangLamViec] = @TenTinhTrangLamViec,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmTinhTrangLamViecID] = @DmTinhTrangLamViecID

--endregion

```
