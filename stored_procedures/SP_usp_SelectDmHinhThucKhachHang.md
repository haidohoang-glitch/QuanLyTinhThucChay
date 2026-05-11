# Stored Procedure: `usp_SelectDmHinhThucKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:04.443000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.183000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmHinhThucKhachHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmHinhThucKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmHinhThucKhachHang]
	@DmHinhThucKhachHangID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmHinhThucKhachHangID],
	[MaHinhThucKhachHang],
	[TenHinhThucKhachHang],
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
	[dbo].[DmHinhThucKhachHang]
WHERE
		[DmHinhThucKhachHangID] = @DmHinhThucKhachHangID
 and DeletedStatus <> 1

--endregion

```
