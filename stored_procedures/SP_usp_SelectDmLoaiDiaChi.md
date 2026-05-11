# Stored Procedure: `usp_SelectDmLoaiDiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:06.083000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.527000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiDiaChiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmLoaiDiaChi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmLoaiDiaChi]
	@DmLoaiDiaChiID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmLoaiDiaChiID],
	[MaLoaiDiaChi],
	[TenLoaiDiaChi],
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
	[dbo].[DmLoaiDiaChi]
WHERE
		[DmLoaiDiaChiID] = @DmLoaiDiaChiID
 and DeletedStatus <> 1

--endregion

```
