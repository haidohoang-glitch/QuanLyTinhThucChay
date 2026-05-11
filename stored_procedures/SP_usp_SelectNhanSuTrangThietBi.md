# Stored Procedure: `usp_SelectNhanSuTrangThietBi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.340000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuTrangThietBiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuTrangThietBi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuTrangThietBi]
	@NhanSuTrangThietBiID int
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
WHERE
		[NhanSuTrangThietBiID] = @NhanSuTrangThietBiID
 and DeletedStatus <> 1

--endregion

```
