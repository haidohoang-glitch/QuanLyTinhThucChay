# Stored Procedure: `usp_SelectDotChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:11:50.297000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.967000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDotChayHopDongChiTiet]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDotChayHopDongChiTiet]
	@DotChayHopDongChiTietID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[DotChayHopDongChiTietID],
	[ViTri],
	[TenWebsite],
	[HopDongREF],
	[HopDongChiTietREF],
	[ThoiGianBatDau],
	[ThoiGianKetThuc],
	[ThoiGianBatDauBooking],
	[ThoiGianKetThucBooking],
	[GhiChu],
	[BookingREF],
	[IsWarning],
	[DmBannerREF],
	[TenBanner],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[DotChayHopDongChiTiet]
WHERE
		[DotChayHopDongChiTietID] = @DotChayHopDongChiTietID
 and DeletedStatus <> 1

```
