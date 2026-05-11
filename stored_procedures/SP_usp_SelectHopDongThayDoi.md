# Stored Procedure: `usp_SelectHopDongThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:33:33.457000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.890000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongThayDoiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectHopDongThayDoi]
-- Create Date: Monday, June 03, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectHopDongThayDoi]
	@HopDongThayDoiID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[HopDongThayDoiID],
	[HopDongFK],
	[LoaiThayDoi],
	[NgayThayDoi],
	[NganhHang],
	[NhanHopDong],
	[GiaTriHopDong],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[HopDongThayDoi]
WHERE
		[HopDongThayDoiID] = @HopDongThayDoiID
 and DeletedStatus <> 1

--endregion

```
