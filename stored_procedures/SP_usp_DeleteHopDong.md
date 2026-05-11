# Stored Procedure: `usp_DeleteHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:14:32.630000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.047000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteHopDong]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteHopDong]
	@HopDongID int
AS

SET NOCOUNT ON

Update [dbo].[HopDong]
Set DeletedStatus = 1
WHERE
	[HopDongID] = @HopDongID

--endregion

```
