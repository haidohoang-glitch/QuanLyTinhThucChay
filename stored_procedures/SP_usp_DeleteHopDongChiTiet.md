# Stored Procedure: `usp_DeleteHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:14:32.617000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.257000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteHopDongChiTiet]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteHopDongChiTiet]
	@HopDongChiTietID int
AS

SET NOCOUNT ON

Update [dbo].[HopDongChiTiet]
Set DeletedStatus = 1
WHERE
	[HopDongChiTietID] = @HopDongChiTietID

--endregion

```
