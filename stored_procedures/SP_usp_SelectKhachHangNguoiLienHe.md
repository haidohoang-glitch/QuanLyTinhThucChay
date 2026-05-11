# Stored Procedure: `usp_SelectKhachHangNguoiLienHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.110000
- **Ngày sửa cuối**: 2014-10-14 10:39:41.617000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNguoiLienHeID` | `int(4)` | No |

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangNguoiLienHe]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangNguoiLienHe]
	@KhachHangNguoiLienHeID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangNguoiLienHeID],
	[KhachHangREF],
	[ThongTinCaNhanREF],
	[DmNguonDuLieuREF],
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
	[dbo].[KhachHangNguoiLienHe]
WHERE
		[KhachHangNguoiLienHeID] = @KhachHangNguoiLienHeID
 and DeletedStatus <> 1

--endregion


```
