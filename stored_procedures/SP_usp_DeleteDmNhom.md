# Stored Procedure: `usp_DeleteDmNhom`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:33:06.387000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.847000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhomID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteDmNhom]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNhom]
	@DmNhomID int
AS

SET NOCOUNT ON

Update [dbo].[DmNhom]
Set DeletedStatus = 1
WHERE
	[DmNhomID] = @DmNhomID

--endregion

```
