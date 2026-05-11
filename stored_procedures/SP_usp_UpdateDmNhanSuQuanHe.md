# Stored Procedure: `usp_UpdateDmNhanSuQuanHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.603000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.203000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuQuanHeID` | `int(4)` | No |
| `@MaNhanSuQuanHe` | `nvarchar(100)` | No |
| `@TenNhanSuQuanHe` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDmNhanSuQuanHe]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmNhanSuQuanHe]
	@DmNhanSuQuanHeID int,
	@MaNhanSuQuanHe nvarchar(50),
	@TenNhanSuQuanHe nvarchar(200),
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

UPDATE [dbo].[DmNhanSuQuanHe] SET
	[MaNhanSuQuanHe] = @MaNhanSuQuanHe,
	[TenNhanSuQuanHe] = @TenNhanSuQuanHe,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmNhanSuQuanHeID] = @DmNhanSuQuanHeID

--endregion

```
