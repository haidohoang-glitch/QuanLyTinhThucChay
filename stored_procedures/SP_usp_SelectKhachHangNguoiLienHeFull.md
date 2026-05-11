# Stored Procedure: `usp_SelectKhachHangNguoiLienHeFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:29.573000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.093000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNguoiLienHeID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangNguoiLienHeFull]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangNguoiLienHeFull]
	@KhachHangNguoiLienHeID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangNguoiLienHeID],
	[KhachHangREF],
	[HoVaTen],
	[ChucVu],
	[DiaChi],
	[Email],
	[DienThoai],
	[Fax],
	[DienThoai2],
	[DienThoai3],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[KhachHangNguoiLienHeFull]
WHERE
		[KhachHangNguoiLienHeID] = @KhachHangNguoiLienHeID
 and DeletedStatus <> 1

--endregion

```
