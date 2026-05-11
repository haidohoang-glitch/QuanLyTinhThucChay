# Stored Procedure: `usp_InsertDmLoaiThongTinLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:07.393000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.333000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiThongTinLamViecID` | `int(4)` | No |
| `@MaLoaiThongTinLamViec` | `nvarchar(100)` | No |
| `@TenLoaiThongTinLamViec` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertDmLoaiThongTinLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDmLoaiThongTinLamViec]
	@DmLoaiThongTinLamViecID int,
	@MaLoaiThongTinLamViec nvarchar(50),
	@TenLoaiThongTinLamViec nvarchar(200),
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

INSERT INTO [dbo].[DmLoaiThongTinLamViec] (
	[DmLoaiThongTinLamViecID],
	[MaLoaiThongTinLamViec],
	[TenLoaiThongTinLamViec],
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
	@DmLoaiThongTinLamViecID,
	@MaLoaiThongTinLamViec,
	@TenLoaiThongTinLamViec,
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
