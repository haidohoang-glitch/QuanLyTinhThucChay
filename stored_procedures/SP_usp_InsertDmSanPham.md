# Stored Procedure: `usp_InsertDmSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:29:23.083000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamID` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Code` | `nvarchar(400)` | No |
| `@DmNhomSanPhamREF` | `int(4)` | No |
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
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_InsertDmSanPham]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDmSanPham]
	@DmSanPhamID int,
	@TenSanPham nvarchar(200),
	@GhiChu nvarchar(4000),
	@Code nvarchar(200),
	@DmNhomSanPhamREF int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON
if(exists(select * from [DmSanPham] where DmSanPhamID =@DmSanPhamID)) 
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
else
INSERT INTO [dbo].[DmSanPham] (
	[DmSanPhamID],
	[TenSanPham],
	[GhiChu],
	[Code],
	[DmNhomSanPhamREF],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@DmSanPhamID,
	@TenSanPham,
	@GhiChu,
	@Code,
	@DmNhomSanPhamREF,
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
