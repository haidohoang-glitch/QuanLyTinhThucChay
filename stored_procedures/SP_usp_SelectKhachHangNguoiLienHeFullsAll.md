# Stored Procedure: `usp_SelectKhachHangNguoiLienHeFullsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:29.697000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.090000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangNguoiLienHeFullsAll]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangNguoiLienHeFullsAll]
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
Where DeletedStatus <> 1
--endregion

```
