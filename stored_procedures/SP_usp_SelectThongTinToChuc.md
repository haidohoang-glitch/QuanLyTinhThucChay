# Stored Procedure: `usp_SelectThongTinToChuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:26.547000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.700000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinToChucID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_SelectThongTinToChuc]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThongTinToChuc]
	@ThongTinToChucID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[ThongTinToChucID],
	[MaThongTinToChuc],
	[TenToChuc],
	[GiayPhepKinhDoanh],
	[NgayThanhLap],
	[NoiCapGiayPhepKinhDoanh],
	[MaSoThue],
	[DienThoai],
	[Fax],
	[Email],
	[Website],
	[DmLoaiToChucREF],
	[DiaChiREF],
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
	[dbo].[ThongTinToChuc]
WHERE
		[ThongTinToChucID] = @ThongTinToChucID
 and DeletedStatus <> 1

--endregion

```
