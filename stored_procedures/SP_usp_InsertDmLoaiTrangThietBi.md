# Stored Procedure: `usp_InsertDmLoaiTrangThietBi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:08.943000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.903000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiTrangThietBiID` | `int(4)` | No |
| `@MaLoaiTrangThietBi` | `nvarchar(100)` | No |
| `@TenLoaiTrangThietBi` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertDmLoaiTrangThietBi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDmLoaiTrangThietBi]
	@DmLoaiTrangThietBiID int,
	@MaLoaiTrangThietBi nvarchar(50),
	@TenLoaiTrangThietBi nvarchar(200),
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

INSERT INTO [dbo].[DmLoaiTrangThietBi] (
	[DmLoaiTrangThietBiID],
	[MaLoaiTrangThietBi],
	[TenLoaiTrangThietBi],
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
	@DmLoaiTrangThietBiID,
	@MaLoaiTrangThietBi,
	@TenLoaiTrangThietBi,
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
