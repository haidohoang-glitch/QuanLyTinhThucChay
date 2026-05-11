# Stored Procedure: `usp_InsertKhachHangChienDich`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.437000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.650000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangChienDichID` | `int(4)` | No |
| `@MaChienDich` | `nvarchar(100)` | No |
| `@TenChienDich` | `nvarchar(400)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@NoiDungChienDich` | `nvarchar(8000)` | No |
| `@KhachHangREF` | `int(4)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertKhachHangChienDich]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertKhachHangChienDich]
	@KhachHangChienDichID int,
	@MaChienDich nvarchar(50),
	@TenChienDich nvarchar(200),
	@NgayBatDau datetime,
	@NgayKetThuc datetime,
	@NoiDungChienDich nvarchar(4000),
	@KhachHangREF int,
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

INSERT INTO [dbo].[KhachHangChienDich] (
	[KhachHangChienDichID],
	[MaChienDich],
	[TenChienDich],
	[NgayBatDau],
	[NgayKetThuc],
	[NoiDungChienDich],
	[KhachHangREF],
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
	@KhachHangChienDichID,
	@MaChienDich,
	@TenChienDich,
	@NgayBatDau,
	@NgayKetThuc,
	@NoiDungChienDich,
	@KhachHangREF,
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
