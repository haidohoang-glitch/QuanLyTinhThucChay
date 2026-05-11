# Stored Procedure: `usp_UpdateDmNhomLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:11.710000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.713000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomLamViecID` | `int(4)` | No |
| `@MaNhomLamViec` | `nvarchar(100)` | No |
| `@TenNhomLamViec` | `nvarchar(400)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDmNhomLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmNhomLamViec]
	@DmNhomLamViecID int,
	@MaNhomLamViec nvarchar(50),
	@TenNhomLamViec nvarchar(200),
	@DmBoPhanREF int,
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

UPDATE [dbo].[DmNhomLamViec] SET
	[MaNhomLamViec] = @MaNhomLamViec,
	[TenNhomLamViec] = @TenNhomLamViec,
	[DmBoPhanREF] = @DmBoPhanREF,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmNhomLamViecID] = @DmNhomLamViecID

--endregion

```
