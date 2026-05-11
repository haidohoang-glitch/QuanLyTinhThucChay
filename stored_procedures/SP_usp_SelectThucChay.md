# Stored Procedure: `usp_SelectThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:10:44.087000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.127000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectThucChay]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThucChay]
	@ThucChayID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[ThucChayID],
	[SoHopDong],
	[DanhsachDmBookingREF],
	[DmSanPhamREF],
	[TenSanPham],
	[DmNhomWebsiteREF],
	[TenNhomWebsite],
	[DmWebsiteREF],
	[TenWebsite],
	[DmChienDichREF],
	[TenChienDich],
	[DmBannerREF],
	[TenBanner],
	[NgayThucHien],
	[TongViewThucChay],
	[TongClickThucChay],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[ThucChay]
WHERE
		[ThucChayID] = @ThucChayID
 and DeletedStatus <> 1

--endregion

```
