# Stored Procedure: `usp_DeleteKhachHangThongTinLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.727000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangThongTinLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteKhachHangThongTinLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteKhachHangThongTinLamViec]
	@KhachHangThongTinLamViecID int
AS

SET NOCOUNT ON

Update [dbo].[KhachHangThongTinLamViec]
Set DeletedStatus = 1
WHERE
	[KhachHangThongTinLamViecID] = @KhachHangThongTinLamViecID

--endregion

```
