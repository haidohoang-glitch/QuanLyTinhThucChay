# Stored Procedure: `usp_DeleteDmSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:29:23.543000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.253000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteDmSanPham]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmSanPham]
	@DmSanPhamID int
AS

SET NOCOUNT ON

Update [dbo].[DmSanPham]
Set DeletedStatus = 1
WHERE
	[DmSanPhamID] = @DmSanPhamID

--endregion

```
