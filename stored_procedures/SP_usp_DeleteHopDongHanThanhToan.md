# Stored Procedure: `usp_DeleteHopDongHanThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:18.540000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.913000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongHanThanhToanID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_DeleteHopDongHanThanhToan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteHopDongHanThanhToan]
	@HopDongHanThanhToanID int
AS

SET NOCOUNT ON

Update [dbo].[HopDongHanThanhToan]
Set DeletedStatus = 1
WHERE
	[HopDongHanThanhToanID] = @HopDongHanThanhToanID

--endregion

```
