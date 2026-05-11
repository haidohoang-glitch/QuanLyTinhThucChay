# Stored Procedure: `usp_SelectDmLoaiThongTinLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:07.887000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiThongTinLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmLoaiThongTinLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmLoaiThongTinLamViec]
	@DmLoaiThongTinLamViecID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmLoaiThongTinLamViecID],
	[MaLoaiThongTinLamViec],
	[TenLoaiThongTinLamViec],
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
	[dbo].[DmLoaiThongTinLamViec]
WHERE
		[DmLoaiThongTinLamViecID] = @DmLoaiThongTinLamViecID
 and DeletedStatus <> 1

--endregion

```
