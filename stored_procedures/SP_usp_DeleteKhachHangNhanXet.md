# Stored Procedure: `usp_DeleteKhachHangNhanXet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.377000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNhanXetID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteKhachHangNhanXet]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteKhachHangNhanXet]
	@KhachHangNhanXetID int
AS

SET NOCOUNT ON

Update [dbo].[KhachHangNhanXet]
Set DeletedStatus = 1
WHERE
	[KhachHangNhanXetID] = @KhachHangNhanXetID

--endregion

```
