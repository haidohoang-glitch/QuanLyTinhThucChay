# Stored Procedure: `usp_SelectKhachHangThongTinLamViec`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:21.773000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.940000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangThongTinLamViecID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectKhachHangThongTinLamViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectKhachHangThongTinLamViec]
	@KhachHangThongTinLamViecID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[KhachHangThongTinLamViecID],
	[NgayLamViec],
	[ThongTinCaNhanREF],
	[KhachHangNguoiLienHeREF],
	[MucDichCongViec],
	[TieuDe],
	[NoiDungLamViec],
	[DmMucDoUuTienREF],
	[DmLoaiThongTinLamViecREF],
	[DmLinhVucLamViecREF],
	[DmTinhTrangLamViecREF],
	[KetQua],
	[NgayLamViecKeTiep],
	[AttachFilename],
	[AttachFilenameEncode],
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
	[dbo].[KhachHangThongTinLamViec]
WHERE
		[KhachHangThongTinLamViecID] = @KhachHangThongTinLamViecID
 and DeletedStatus <> 1

--endregion

```
