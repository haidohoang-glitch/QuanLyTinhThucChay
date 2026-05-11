# Stored Procedure: `usp_SelectDmNhanSuLoaiHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.260000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.250000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuLoaiHopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmNhanSuLoaiHopDong]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNhanSuLoaiHopDong]
	@DmNhanSuLoaiHopDongID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNhanSuLoaiHopDongID],
	[MaLoaiHopDong],
	[TenLoaiHopDong],
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
	[dbo].[DmNhanSuLoaiHopDong]
WHERE
		[DmNhanSuLoaiHopDongID] = @DmNhanSuLoaiHopDongID
 and DeletedStatus <> 1

--endregion

```
