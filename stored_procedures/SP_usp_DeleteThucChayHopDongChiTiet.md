# Stored Procedure: `usp_DeleteThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:14:32.583000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.647000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteThucChayHopDongChiTiet]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteThucChayHopDongChiTiet]
	@ThucChayHopDongChiTietID int
AS

SET NOCOUNT ON

Update [dbo].[ThucChayHopDongChiTiet]
Set DeletedStatus = 1
WHERE
	[ThucChayHopDongChiTietID] = @ThucChayHopDongChiTietID

--endregion

```
