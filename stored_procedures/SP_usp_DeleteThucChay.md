# Stored Procedure: `usp_DeleteThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:14:32.603000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.247000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteThucChay]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteThucChay]
	@ThucChayID int
AS

SET NOCOUNT ON

Update [dbo].[ThucChay]
Set DeletedStatus = 1
WHERE
	[ThucChayID] = @ThucChayID

--endregion

```
