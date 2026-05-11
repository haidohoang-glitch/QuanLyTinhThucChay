# Stored Procedure: `usp_DeleteKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.070000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.677000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteKhachHang]
	@KhachHangID int
AS

SET NOCOUNT ON

Update [dbo].[KhachHang]
Set DeletedStatus = 1
WHERE
	[KhachHangID] = @KhachHangID

--endregion

```
