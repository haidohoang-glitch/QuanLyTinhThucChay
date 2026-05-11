# Stored Procedure: `usp_DeleteDmNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-27 10:20:20.693000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_DeleteDmNhanHang]
-- Create Date: Monday, November 18, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNhanHang]
	@DmNhanHangID int
AS

SET NOCOUNT ON

Update [dbo].[DmNhanHang]
Set DeletedStatus = 1
WHERE
	[DmNhanHangID] = @DmNhanHangID

--endregion

```
