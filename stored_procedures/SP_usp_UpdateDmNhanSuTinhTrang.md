# Stored Procedure: `usp_UpdateDmNhanSuTinhTrang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.843000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.187000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuTinhTrangID` | `int(4)` | No |
| `@MaNhanSuTinhTrang` | `nvarchar(100)` | No |
| `@TenNhanSuTinhTrang` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDmNhanSuTinhTrang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmNhanSuTinhTrang]
	@DmNhanSuTinhTrangID int,
	@MaNhanSuTinhTrang nvarchar(50),
	@TenNhanSuTinhTrang nvarchar(200),
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

UPDATE [dbo].[DmNhanSuTinhTrang] SET
	[MaNhanSuTinhTrang] = @MaNhanSuTinhTrang,
	[TenNhanSuTinhTrang] = @TenNhanSuTinhTrang,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmNhanSuTinhTrangID] = @DmNhanSuTinhTrangID

--endregion

```
