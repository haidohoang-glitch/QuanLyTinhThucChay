# Stored Procedure: `usp_DeleteDmBoPhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:03.083000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.873000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBoPhanID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmBoPhan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmBoPhan]
	@DmBoPhanID int
AS

SET NOCOUNT ON

Update [dbo].[DmBoPhan]
Set DeletedStatus = 1
WHERE
	[DmBoPhanID] = @DmBoPhanID

--endregion

```
