# Stored Procedure: `usp_SelectDmLoaiKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:06.650000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.140000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiKhachHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectDmLoaiKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDmLoaiKhachHang]
	@DmLoaiKhachHangID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DmLoaiKhachHangID],
	[MaLoaiKhachHang],
	[TenLoaiKhachHang],
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
	[dbo].[DmLoaiKhachHang]
WHERE
		[DmLoaiKhachHangID] = @DmLoaiKhachHangID
 and DeletedStatus <> 1

--endregion

```
