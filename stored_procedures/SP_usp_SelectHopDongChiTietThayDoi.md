# Stored Procedure: `usp_SelectHopDongChiTietThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:31:21.517000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.990000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietThayDoiID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectHopDongChiTietThayDoi]
-- Create Date: Monday, June 03, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectHopDongChiTietThayDoi]
	@HopDongChiTietThayDoiID int
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[HopDongChiTietThayDoiID],
	[HopDongChiTietREF],
	[HopDongFK],
	[HopDongThayDoiREF],
	[NhanHang],
	[DmNhomNganhREF],
	[TenNhomNganh],
	[DmLoaiREF],
	[TenLoai],
	[DmNhomWebsiteREF],
	[TenNhomWebsite],
	[DmWebsiteREF],
	[TenWebsite],
	[DmSanPhamREF],
	[TenSanPham],
	[DmLoaiBannerREF],
	[TenLoaiBanner],
	[DmChuyenMucREF],
	[TenChuyenMuc],
	[DmViTriREF],
	[TenViTri],
	[ThoiGian],
	[SoLuong],
	[DonViTinh],
	[DonGia],
	[ChietKhau],
	[GiamGia],
	[TiLeTuVan],
	[KhuyenMai],
	[IsKhuyenMai],
	[ChiPhiTuVan],
	[ThanhTien],
	[GhiChu],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
FROM
	[dbo].[HopDongChiTietThayDoi]
WHERE
		[HopDongChiTietThayDoiID] = @HopDongChiTietThayDoiID
 and DeletedStatus <> 1

--endregion

```
