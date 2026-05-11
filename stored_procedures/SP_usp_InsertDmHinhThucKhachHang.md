# Stored Procedure: `usp_InsertDmHinhThucKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:04.217000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.113000

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
-- Stored Procedure Name: [dbo].[usp_InsertDmHinhThucKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDmHinhThucKhachHang]
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

INSERT INTO [dbo].[DmHinhThucKhachHang] (
	[DmHinhThucKhachHangID],
	[MaHinhThucKhachHang],
	[TenHinhThucKhachHang],
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
	@DmHinhThucKhachHangID,
	@MaHinhThucKhachHang,
	@TenHinhThucKhachHang,
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
