# Stored Procedure: `usp_DeleteDmNhanSuTinhTrang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.867000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuTinhTrangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmNhanSuTinhTrang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNhanSuTinhTrang]
	@DmNhanSuTinhTrangID int
AS

SET NOCOUNT ON

Update [dbo].[DmNhanSuTinhTrang]
Set DeletedStatus = 1
WHERE
	[DmNhanSuTinhTrangID] = @DmNhanSuTinhTrangID

--endregion

```
