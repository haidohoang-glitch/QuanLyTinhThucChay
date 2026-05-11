# Stored Procedure: `usp_DeleteHopDongChiTietThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:31:22.260000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietThayDoiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteHopDongChiTietThayDoi]
-- Create Date: Monday, June 03, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteHopDongChiTietThayDoi]
	@HopDongChiTietThayDoiID int
AS

SET NOCOUNT ON

Update [dbo].[HopDongChiTietThayDoi]
Set DeletedStatus = 1
WHERE
	[HopDongChiTietThayDoiID] = @HopDongChiTietThayDoiID

--endregion

```
