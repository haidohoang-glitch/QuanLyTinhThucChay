# Stored Procedure: `usp_SelectHopDongChiTietThayDoisAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:31:21.227000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.970000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectHopDongChiTietThayDoisAll]
-- Create Date: Monday, June 03, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectHopDongChiTietThayDoisAll]
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
Where DeletedStatus <> 1
--endregion

```
