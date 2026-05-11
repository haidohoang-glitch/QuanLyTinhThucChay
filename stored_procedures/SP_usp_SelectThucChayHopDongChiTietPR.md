# Stored Procedure: `usp_SelectThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-09 11:13:12.153000
- **Ngày sửa cuối**: 2014-11-19 12:24:45.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   ceo
-- Stored Procedure Name: [dbo].[usp_SelectThucChayHopDongChiTietPR]
-- Create Date: 09 Tháng Bảy 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThucChayHopDongChiTietPR]
	@ThucChayHopDongChiTietPRID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[ThucChayHopDongChiTietPRID],
	[HopDongREF],
	[HopDongChiTietREF],
	[NhanHang],
	[TenWebsite],
	[ChuyenMuc],
	[TieuDiem],
	[KhuyenMai],
	[GiaTien],
	[ThoiGianBatDau],
	[Link],
	[GhiChu],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[ThucChayHopDongChiTietPR]
WHERE
		[ThucChayHopDongChiTietPRID] = @ThucChayHopDongChiTietPRID
 and DeletedStatus <> 1

--endregion

```
