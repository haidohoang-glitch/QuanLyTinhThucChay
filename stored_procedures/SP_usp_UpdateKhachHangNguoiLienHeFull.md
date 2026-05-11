# Stored Procedure: `usp_UpdateKhachHangNguoiLienHeFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:29.430000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNguoiLienHeID` | `int(4)` | No |
| `@KhachHangREF` | `int(4)` | No |
| `@HoVaTen` | `nvarchar(100)` | No |
| `@ChucVu` | `nvarchar(100)` | No |
| `@DiaChi` | `nvarchar(8000)` | No |
| `@Email` | `nvarchar(400)` | No |
| `@DienThoai` | `nvarchar(100)` | No |
| `@Fax` | `nvarchar(100)` | No |
| `@DienThoai2` | `nvarchar(100)` | No |
| `@DienThoai3` | `nvarchar(100)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateKhachHangNguoiLienHeFull]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateKhachHangNguoiLienHeFull]
	@KhachHangNguoiLienHeID int,
	@KhachHangREF int,
	@HoVaTen nvarchar(50),
	@ChucVu nvarchar(50),
	@DiaChi nvarchar(4000),
	@Email nvarchar(200),
	@DienThoai nvarchar(50),
	@Fax nvarchar(50),
	@DienThoai2 nvarchar(50),
	@DienThoai3 nvarchar(50),
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[KhachHangNguoiLienHeFull] SET
	[KhachHangREF] = @KhachHangREF,
	[HoVaTen] = @HoVaTen,
	[ChucVu] = @ChucVu,
	[DiaChi] = @DiaChi,
	[Email] = @Email,
	[DienThoai] = @DienThoai,
	[Fax] = @Fax,
	[DienThoai2] = @DienThoai2,
	[DienThoai3] = @DienThoai3,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[KhachHangNguoiLienHeID] = @KhachHangNguoiLienHeID

--endregion

```
