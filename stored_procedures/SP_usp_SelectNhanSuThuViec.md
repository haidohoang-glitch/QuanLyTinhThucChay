# Stored Procedure: `usp_SelectNhanSuThuViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:23.093000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.977000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuThuViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectNhanSuThuViec]
	@NhanSuThuViecID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[NhanSuThuViecID],
	[NhanSuSoYeuLyLichREF],
	[TuNgay],
	[DenNgay],
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
	[dbo].[NhanSuThuViec]
WHERE
		[NhanSuThuViecID] = @NhanSuThuViecID
 and DeletedStatus <> 1

--endregion

```
