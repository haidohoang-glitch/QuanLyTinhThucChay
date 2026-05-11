# Stored Procedure: `usp_DeleteThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-09 11:13:12.287000
- **Ngày sửa cuối**: 2014-11-19 12:24:45.850000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   ceo
-- Stored Procedure Name: [dbo].[usp_DeleteThucChayHopDongChiTietPR]
-- Create Date: 09 Tháng Bảy 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteThucChayHopDongChiTietPR]
	@ThucChayHopDongChiTietPRID int
AS

SET NOCOUNT ON

Update [dbo].[ThucChayHopDongChiTietPR]
Set DeletedStatus = 1
WHERE
	[ThucChayHopDongChiTietPRID] = @ThucChayHopDongChiTietPRID

--endregion

```
