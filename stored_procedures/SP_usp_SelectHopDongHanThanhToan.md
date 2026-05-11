# Stored Procedure: `usp_SelectHopDongHanThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:18.807000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.953000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongHanThanhToanID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectHopDongHanThanhToan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectHopDongHanThanhToan]
	@HopDongHanThanhToanID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[HopDongHanThanhToanID],
	[HopDongREF],
	[LanThanhToan],
	[NgayThanhToan],
	[SoTien],
	[NgayDuDinhThanhToan],
	[GiaTriDaThanhToan],
	[GhiChu],
	[Active],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[HopDongHanThanhToan]
WHERE
		[HopDongHanThanhToanID] = @HopDongHanThanhToanID
 and DeletedStatus <> 1

--endregion

```
