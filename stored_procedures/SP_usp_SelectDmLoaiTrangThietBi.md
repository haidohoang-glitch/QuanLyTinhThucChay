# Stored Procedure: `usp_SelectDmLoaiTrangThietBi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:09.493000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.817000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiTrangThietBiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmLoaiTrangThietBi]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmLoaiTrangThietBi]
	@DmLoaiTrangThietBiID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmLoaiTrangThietBiID],
	[MaLoaiTrangThietBi],
	[TenLoaiTrangThietBi],
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
	[dbo].[DmLoaiTrangThietBi]
WHERE
		[DmLoaiTrangThietBiID] = @DmLoaiTrangThietBiID
 and DeletedStatus <> 1

--endregion

```
