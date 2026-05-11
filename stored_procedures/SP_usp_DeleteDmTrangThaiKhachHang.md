# Stored Procedure: `usp_DeleteDmTrangThaiKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:16.917000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.797000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTrangThaiKhachHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmTrangThaiKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmTrangThaiKhachHang]
	@DmTrangThaiKhachHangID int
AS

SET NOCOUNT ON

Update [dbo].[DmTrangThaiKhachHang]
Set DeletedStatus = 1
WHERE
	[DmTrangThaiKhachHangID] = @DmTrangThaiKhachHangID

--endregion

```
