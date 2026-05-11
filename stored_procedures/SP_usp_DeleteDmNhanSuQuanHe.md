# Stored Procedure: `usp_DeleteDmNhanSuQuanHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.627000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.220000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuQuanHeID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmNhanSuQuanHe]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNhanSuQuanHe]
	@DmNhanSuQuanHeID int
AS

SET NOCOUNT ON

Update [dbo].[DmNhanSuQuanHe]
Set DeletedStatus = 1
WHERE
	[DmNhanSuQuanHeID] = @DmNhanSuQuanHeID

--endregion

```
