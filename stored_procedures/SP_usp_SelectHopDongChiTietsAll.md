# Stored Procedure: `usp_SelectHopDongChiTietsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:10:57.470000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.153000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_SelectHopDongChiTietsAll]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_SelectHopDongChiTietsAll]
AS

SET NOCOUNT ON
SET TRANSACTION ISOLATION LEVEL READ COMMITTED

SELECT
	[HopDongChiTietID],
	[HopDongFK],
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
	[dbo].[HopDongChiTiet]
Where DeletedStatus <> 1

```
