# Stored Procedure: `usp_DeleteHopDongThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:33:34.653000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.887000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongThayDoiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteHopDongThayDoi]
-- Create Date: Monday, June 03, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteHopDongThayDoi]
	@HopDongThayDoiID int
AS

SET NOCOUNT ON

Update [dbo].[HopDongThayDoi]
Set DeletedStatus = 1
WHERE
	[HopDongThayDoiID] = @HopDongThayDoiID

--endregion

```
