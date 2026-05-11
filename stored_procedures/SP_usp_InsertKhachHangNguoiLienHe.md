# Stored Procedure: `usp_InsertKhachHangNguoiLienHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.880000
- **Ngày sửa cuối**: 2014-10-14 10:39:46.113000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNguoiLienHeID` | `int(4)` | No |
| `@KhachHangREF` | `int(4)` | No |
| `@ThongTinCaNhanREF` | `int(4)` | No |
| `@DmNguonDuLieuREF` | `int(4)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertKhachHangNguoiLienHe]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertKhachHangNguoiLienHe]
	@KhachHangNguoiLienHeID int,
	@KhachHangREF int,
	@ThongTinCaNhanREF int,
	@DmNguonDuLieuREF int,
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

INSERT INTO [dbo].[KhachHangNguoiLienHe] (
	[KhachHangNguoiLienHeID],
	[KhachHangREF],
	[ThongTinCaNhanREF],
	[DmNguonDuLieuREF],
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
	@KhachHangNguoiLienHeID,
	@KhachHangREF,
	@ThongTinCaNhanREF,
	@DmNguonDuLieuREF,
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
