# Stored Procedure: `usp_SelectDmNhomsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:33:06.653000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.950000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDmNhomsAll]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNhomsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNhomID],
	TenNhom,
	[GhiChu],
	[DmBoPhanREF],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmNhom]
Where DeletedStatus <> 1
--endregion

```
