# Stored Procedure: `usp_DeleteDmBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-24 14:35:26.680000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_DeleteDmBanner]
-- Create Date: Thursday, October 24, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDmBanner]
	@DmBannerID int
AS

SET NOCOUNT ON

Update [dbo].[DmBanner]
Set DeletedStatus = 1
WHERE
	[DmBannerID] = @DmBannerID

--endregion

```
