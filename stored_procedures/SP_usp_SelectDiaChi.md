# Stored Procedure: `usp_SelectDiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:02.610000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.217000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DiaChiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDiaChi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDiaChi]
	@DiaChiID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DiaChiID],
	[SoNha],
	[DuongPho],
	[DmQuanHuyenREF],
	[DmTinhThanhPhoREF],
	[DmQuocGiaREF],
	[DmLoaiDiaChiREF],
	[IsTruSoChinh],
	[DiaChiText],
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
	[dbo].[DiaChi]
WHERE
		[DiaChiID] = @DiaChiID
 and DeletedStatus <> 1

--endregion

```
