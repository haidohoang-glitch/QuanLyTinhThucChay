# Stored Procedure: `usp_UpdateDmSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:29:23.293000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.110000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamID` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Code` | `nvarchar(400)` | No |
| `@DmNhomSanPhamREF` | `int(4)` | No |
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
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_UpdateDmSanPham]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmSanPham]
	@DmSanPhamID int,
	@TenSanPham nvarchar(200),
	@GhiChu nvarchar(4000),
	@Code nvarchar(200),
	@DmNhomSanPhamREF int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[DmSanPham] SET
	[TenSanPham] = @TenSanPham,
	[GhiChu] = @GhiChu,
	[Code] = @Code,
	[DmNhomSanPhamREF] = @DmNhomSanPhamREF,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmSanPhamID] = @DmSanPhamID

--endregion

```
