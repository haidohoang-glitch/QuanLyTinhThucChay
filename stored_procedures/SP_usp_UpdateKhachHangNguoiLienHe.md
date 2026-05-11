# Stored Procedure: `usp_UpdateKhachHangNguoiLienHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.953000
- **Ngày sửa cuối**: 2014-10-14 10:39:38.947000

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
-- Stored Procedure Name: [dbo].[usp_UpdateKhachHangNguoiLienHe]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateKhachHangNguoiLienHe]
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

UPDATE [dbo].[KhachHangNguoiLienHe] SET
	[KhachHangREF] = @KhachHangREF,
	[ThongTinCaNhanREF] = @ThongTinCaNhanREF,
	[DmNguonDuLieuREF] = @DmNguonDuLieuREF,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[KhachHangNguoiLienHeID] = @KhachHangNguoiLienHeID

--endregion


```
