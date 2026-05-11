# Stored Procedure: `usp_DeleteDmWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:32:33.673000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.250000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmWebsiteID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteDmWebsite]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmWebsite]
	@DmWebsiteID int
AS

SET NOCOUNT ON

Update [dbo].[DmWebsite]
Set DeletedStatus = 1
WHERE
	[DmWebsiteID] = @DmWebsiteID

--endregion

```
