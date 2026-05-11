# Stored Procedure: `usp_InsertDiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:02.353000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.177000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DiaChiID` | `int(4)` | No |
| `@SoNha` | `nvarchar(400)` | No |
| `@DuongPho` | `nvarchar(400)` | No |
| `@DmQuanHuyenREF` | `int(4)` | No |
| `@DmTinhThanhPhoREF` | `int(4)` | No |
| `@DmQuocGiaREF` | `int(4)` | No |
| `@DmLoaiDiaChiREF` | `int(4)` | No |
| `@IsTruSoChinh` | `int(4)` | No |
| `@DiaChiText` | `nvarchar(8000)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertDiaChi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDiaChi]
	@DiaChiID int,
	@SoNha nvarchar(200),
	@DuongPho nvarchar(200),
	@DmQuanHuyenREF int,
	@DmTinhThanhPhoREF int,
	@DmQuocGiaREF int,
	@DmLoaiDiaChiREF int,
	@IsTruSoChinh int,
	@DiaChiText nvarchar(4000),
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

INSERT INTO [dbo].[DiaChi] (
	[DiaChiID],
	[SoNha],
	[DuongPho],
	[DmQuanHuyenREF],
	[DmTinhThanhPhoREF],
	[DmQuocGiaREF],
	[DmLoaiDiaChiREF],
	[IsTruSoChinh],
	[DiaChiText],
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
	@DiaChiID,
	@SoNha,
	@DuongPho,
	@DmQuanHuyenREF,
	@DmTinhThanhPhoREF,
	@DmQuocGiaREF,
	@DmLoaiDiaChiREF,
	@IsTruSoChinh,
	@DiaChiText,
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
