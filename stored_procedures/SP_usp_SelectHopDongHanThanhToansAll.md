# Stored Procedure: `usp_SelectHopDongHanThanhToansAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:18.983000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.930000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectHopDongHanThanhToansAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectHopDongHanThanhToansAll]
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
Where DeletedStatus <> 1
--endregion

```
