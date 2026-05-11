# Stored Procedure: `usp_InsertNhanSuNguoiThan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.203000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.833000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuNguoiThanID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@ThongTinCaNhanREF` | `int(4)` | No |
| `@DmNhanSuQuanHeREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
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
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_InsertNhanSuNguoiThan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertNhanSuNguoiThan]
	@NhanSuNguoiThanID int,
	@NhanSuSoYeuLyLichREF int,
	@ThongTinCaNhanREF int,
	@DmNhanSuQuanHeREF int,
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

INSERT INTO [dbo].[NhanSuNguoiThan] (
	[NhanSuNguoiThanID],
	[NhanSuSoYeuLyLichREF],
	[ThongTinCaNhanREF],
	[DmNhanSuQuanHeREF],
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
	@NhanSuNguoiThanID,
	@NhanSuSoYeuLyLichREF,
	@ThongTinCaNhanREF,
	@DmNhanSuQuanHeREF,
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
