# Stored Procedure: `usp_SelectNhanSuTinhTrang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.183000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.043000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuTinhTrangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuTinhTrang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuTinhTrang]
	@NhanSuTinhTrangID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuTinhTrangID],
	[NhanSuSoYeuLyLichREF],
	[NgayBatDau],
	[NgayKetThuc],
	[DmNhanSuTinhTrangREF],
	[DmNhomLamViecREF],
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
	[dbo].[NhanSuTinhTrang]
WHERE
		[NhanSuTinhTrangID] = @NhanSuTinhTrangID
 and DeletedStatus <> 1

--endregion

```
