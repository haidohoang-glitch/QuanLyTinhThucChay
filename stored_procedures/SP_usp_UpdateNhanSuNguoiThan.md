# Stored Procedure: `usp_UpdateNhanSuNguoiThan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:22.220000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.820000

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
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuNguoiThan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateNhanSuNguoiThan]
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

UPDATE [dbo].[NhanSuNguoiThan] SET
	[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,
	[ThongTinCaNhanREF] = @ThongTinCaNhanREF,
	[DmNhanSuQuanHeREF] = @DmNhanSuQuanHeREF,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[NhanSuNguoiThanID] = @NhanSuNguoiThanID

--endregion

```
