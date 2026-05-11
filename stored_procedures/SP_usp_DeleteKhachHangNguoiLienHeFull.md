# Stored Procedure: `usp_DeleteKhachHangNguoiLienHeFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:29.513000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.100000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNguoiLienHeID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteKhachHangNguoiLienHeFull]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteKhachHangNguoiLienHeFull]
	@KhachHangNguoiLienHeID int
AS

SET NOCOUNT ON

Update [dbo].[KhachHangNguoiLienHeFull]
Set DeletedStatus = 1
WHERE
	[KhachHangNguoiLienHeID] = @KhachHangNguoiLienHeID

--endregion

```
