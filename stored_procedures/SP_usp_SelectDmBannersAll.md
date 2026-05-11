# Stored Procedure: `usp_SelectDmBannersAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-24 14:36:13.250000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.163000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_SelectDmBannersAll]
-- Create Date: Thursday, October 24, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmBannersAll]
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
Where DeletedStatus <> 1
--endregion

```
