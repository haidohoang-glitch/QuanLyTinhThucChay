# Stored Procedure: `usp_UpdateDmHinhThucKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:04.327000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.037000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmHinhThucKhachHangID` | `int(4)` | No |
| `@MaHinhThucKhachHang` | `nvarchar(100)` | No |
| `@TenHinhThucKhachHang` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDmHinhThucKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmHinhThucKhachHang]
	@DmHinhThucKhachHangID int,
	@MaHinhThucKhachHang nvarchar(50),
	@TenHinhThucKhachHang nvarchar(200),
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

UPDATE [dbo].[DmHinhThucKhachHang] SET
	[MaHinhThucKhachHang] = @MaHinhThucKhachHang,
	[TenHinhThucKhachHang] = @TenHinhThucKhachHang,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmHinhThucKhachHangID] = @DmHinhThucKhachHangID

--endregion

```
