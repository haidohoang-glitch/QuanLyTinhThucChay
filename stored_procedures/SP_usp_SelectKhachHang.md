# Stored Procedure: `usp_SelectKhachHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:20.140000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.667000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHang]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHang]
	@KhachHangID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangID],
	[MaKhachHang],
	[ThongTinCaNhanREF],
	[ThongTinToChucREF],
	[DmHinhThucKhachHangREF],
	[DmLoaiKhachHangREF],
	[NguoiQuanLyREF],
	[IsTruSoChinh],
	[KhachHangREF],
	[DmTrangThaiKhachHangREF],
	[Level],
	[QuyMoCongTy],
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
	[dbo].[KhachHang]
WHERE
		[KhachHangID] = @KhachHangID
 and DeletedStatus <> 1

--endregion

```
