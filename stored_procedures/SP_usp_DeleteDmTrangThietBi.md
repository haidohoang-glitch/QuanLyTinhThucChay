# Stored Procedure: `usp_DeleteDmTrangThietBi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:17.517000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.777000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmTrangThietBiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmTrangThietBi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmTrangThietBi]
	@DmTrangThietBiID int
AS

SET NOCOUNT ON

Update [dbo].[DmTrangThietBi]
Set DeletedStatus = 1
WHERE
	[DmTrangThietBiID] = @DmTrangThietBiID

--endregion

```
