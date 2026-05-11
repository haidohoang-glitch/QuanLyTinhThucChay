# Stored Procedure: `usp_SelectNhanSuTrangThietBisAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.610000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.017000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuTrangThietBisAll]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuTrangThietBisAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuTrangThietBiID],
	[NhanSuSoYeuLyLichREF],
	[DmTrangThietBiREF],
	[NgayCap],
	[NgayHetHan],
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
	[dbo].[NhanSuTrangThietBi]
Where DeletedStatus <> 1
--endregion

```
