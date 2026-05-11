# Stored Procedure: `usp_DeleteNhanSuTinhTrang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.170000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuTinhTrangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteNhanSuTinhTrang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteNhanSuTinhTrang]
	@NhanSuTinhTrangID int
AS

SET NOCOUNT ON

Update [dbo].[NhanSuTinhTrang]
Set DeletedStatus = 1
WHERE
	[NhanSuTinhTrangID] = @NhanSuTinhTrangID

--endregion

```
