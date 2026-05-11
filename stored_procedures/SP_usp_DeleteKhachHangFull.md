# Stored Procedure: `usp_DeleteKhachHangFull`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:28.683000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.117000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteKhachHangFull]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteKhachHangFull]
	@KhachHangID int
AS

SET NOCOUNT ON

Update [dbo].[KhachHangFull]
Set DeletedStatus = 1
WHERE
	[KhachHangID] = @KhachHangID

--endregion

```
