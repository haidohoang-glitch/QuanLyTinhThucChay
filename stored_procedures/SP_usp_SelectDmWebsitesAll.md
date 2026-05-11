# Stored Procedure: `usp_SelectDmWebsitesAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:32:34.003000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.137000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDmWebsitesAll]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmWebsitesAll]
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
Where DeletedStatus <> 1
--endregion

```
