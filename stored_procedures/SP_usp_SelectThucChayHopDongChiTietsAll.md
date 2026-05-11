# Stored Procedure: `usp_SelectThucChayHopDongChiTietsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:10:43.580000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.980000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectThucChayHopDongChiTietsAll]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThucChayHopDongChiTietsAll]
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
Where DeletedStatus <> 1
--endregion

```
