# Stored Procedure: `usp_SelectDmBoPhanNghiepVusAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-16 11:39:20.540000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.263000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDmBoPhanNghiepVusAll]
-- Create Date: Thursday, December 16, 2010
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmBoPhanNghiepVusAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmBoPhanNghiepVuID],
	[DmPhongBanFK],
	[TenBoPhanNghiepVu],
	[DmNgonNguREF],
	[GhiChu],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DmBoPhanNghiepVu]
Where DeletedStatus <> 1
--endregion

```
