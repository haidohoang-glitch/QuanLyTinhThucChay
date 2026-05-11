# Stored Procedure: `usp_SelectDmNhanSuLoaiThuongPhat`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:10.490000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanSuLoaiThuongPhatID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmNhanSuLoaiThuongPhat]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmNhanSuLoaiThuongPhat]
	@DmNhanSuLoaiThuongPhatID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmNhanSuLoaiThuongPhatID],
	[MaNhanSuLoaiThuongPhat],
	[TenNhanSuLoaiThuongPhat],
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
	[dbo].[DmNhanSuLoaiThuongPhat]
WHERE
		[DmNhanSuLoaiThuongPhatID] = @DmNhanSuLoaiThuongPhatID
 and DeletedStatus <> 1

--endregion

```
