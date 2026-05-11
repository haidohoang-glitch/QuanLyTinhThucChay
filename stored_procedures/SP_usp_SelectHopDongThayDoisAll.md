# Stored Procedure: `usp_SelectHopDongThayDoisAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:33:33.180000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.863000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectHopDongThayDoisAll]
-- Create Date: Monday, June 03, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectHopDongThayDoisAll]
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
Where DeletedStatus <> 1
--endregion

```
