# Stored Procedure: `usp_SelectThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:10:43.830000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectThucChayHopDongChiTiet]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThucChayHopDongChiTiet]
	@ThucChayHopDongChiTietID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[ThucChayHopDongChiTietID],
	[HopDongREF],
	[NhanHang],
	[ThoiGianBatDau],
	[ThoiGianKetThuc],
	[Link],
	[DmBannerREF],
	[TenBanner],
	[ViTri],
	[GhiChu],
	[BookingREF],
	[HopDongChiTietREF],
	[TypeThucChay],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[ThucChayHopDongChiTiet]
WHERE
		[ThucChayHopDongChiTietID] = @ThucChayHopDongChiTietID
 and DeletedStatus <> 1

--endregion

```
