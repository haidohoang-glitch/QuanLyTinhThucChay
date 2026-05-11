# Stored Procedure: `usp_SelectThucChaysAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:09:43.890000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.130000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectThucChaysAll]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectThucChaysAll]
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
Where DeletedStatus <> 1

```
