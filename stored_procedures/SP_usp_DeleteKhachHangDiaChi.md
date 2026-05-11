# Stored Procedure: `usp_DeleteKhachHangDiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:27.850000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangDiaChiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteKhachHangDiaChi]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteKhachHangDiaChi]
	@KhachHangDiaChiID int
AS

SET NOCOUNT ON

Update [dbo].[KhachHangDiaChi]
Set DeletedStatus = 1
WHERE
	[KhachHangDiaChiID] = @KhachHangDiaChiID

--endregion

```
