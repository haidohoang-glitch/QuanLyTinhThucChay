# Stored Procedure: `usp_DeleteKhachHangNguoiLienHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.983000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.027000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNguoiLienHeID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteKhachHangNguoiLienHe]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteKhachHangNguoiLienHe]
	@KhachHangNguoiLienHeID int
AS

SET NOCOUNT ON

Update [dbo].[KhachHangNguoiLienHe]
Set DeletedStatus = 1
WHERE
	[KhachHangNguoiLienHeID] = @KhachHangNguoiLienHeID

--endregion

```
