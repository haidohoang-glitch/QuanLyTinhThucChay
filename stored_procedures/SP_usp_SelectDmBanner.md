# Stored Procedure: `usp_SelectDmBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-24 14:36:13.503000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.170000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_SelectDmBanner]
-- Create Date: Thursday, October 24, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmBanner]
	@DmBannerID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmBannerID],
	[TenBanner],
	[TenBanner_boxapp],
	[LoaiSanPham],
	[Active],
	[NgayBatDau],
	[NgayKetThuc],
	[MoTa],
	[TenFile],
	[Width],
	[Height],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmBanner]
WHERE
		[DmBannerID] = @DmBannerID
 and DeletedStatus <> 1

--endregion

```
