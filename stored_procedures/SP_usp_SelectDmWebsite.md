# Stored Procedure: `usp_SelectDmWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:32:33.723000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.140000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmWebsiteID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDmWebsite]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmWebsite]
	@DmWebsiteID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmWebsiteID],
	[TenWebsite],
	[WebsiteLink],
	[GhiChu],
	[Code],
	[DmGroupTypeREF],
	[IsThuongMaiDienTu],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmWebsite]
WHERE
		[DmWebsiteID] = @DmWebsiteID
 and DeletedStatus <> 1

--endregion

```
