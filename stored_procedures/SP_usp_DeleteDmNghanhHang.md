# Stored Procedure: `usp_DeleteDmNghanhHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:11:32.637000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNghanhHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_DeleteDmNghanhHang]
-- Create Date: Monday, November 18, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmNghanhHang]
	@DmNghanhHangID int
AS

SET NOCOUNT ON

Update [dbo].[DmNghanhHang]
Set DeletedStatus = 1
WHERE
	[DmNghanhHangID] = @DmNghanhHangID

--endregion

```
