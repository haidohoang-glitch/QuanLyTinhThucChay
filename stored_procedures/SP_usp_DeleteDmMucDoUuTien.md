# Stored Procedure: `usp_DeleteDmMucDoUuTien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:09.747000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.300000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmMucDoUuTienID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteDmMucDoUuTien]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmMucDoUuTien]
	@DmMucDoUuTienID int
AS

SET NOCOUNT ON

Update [dbo].[DmMucDoUuTien]
Set DeletedStatus = 1
WHERE
	[DmMucDoUuTienID] = @DmMucDoUuTienID

--endregion

```
