# Stored Procedure: `usp_SelectDotChayHopDongChiTietsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:11:38.093000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.963000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectDotChayHopDongChiTietsAll]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectDotChayHopDongChiTietsAll]
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
Where DeletedStatus <> 1

```
