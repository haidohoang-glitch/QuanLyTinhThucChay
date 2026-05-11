# Stored Procedure: `Insert_DoanhSoThucChayhopDongTheoThoiGian`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:43.063000
- **Ngày sửa cuối**: 2015-03-27 17:43:43.063000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[Insert_DoanhSoThucChayhopDongTheoThoiGian] '2013-01-01','2014-12-31'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayhopDongTheoThoiGian]
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DELETE FROM DoanhSoThucChayHopDongTheoThoiGian
	INSERT INTO DoanhSoThucChayHopDongTheoThoiGian
	SELECT 
		NgayThucHien,
		DmMaHopDongREF,
		TenMaHopDong,
		HopDongID,
		SoHopDong,
		TenNhanVien,
		DmNhanVienREF,
		TenPhongBan,
		PhongBanREF,
		TenBoPhan,
		BoPhanREF,
		TenNhom,
		NhomREF,
		TenKhachHang,
		DmKhachHangREF,
		DmHinhThucKhachHangREF,
		TenHinhThucKhachHang,
		HopDongChiTietREF,
		DmHinhThucQuangCaoREF,
		TenHinhThucQuangCao,
		DmSanPhamREF,
		TenSanPham,
		TenLoaiNenTang,
		DmLoaiNenTangREF,
		NhomWebsite_TagREF,
		TenNhomWebsite_Tag,
		TenWebsite,
		DmWebsiteREF,
		TenChuyenMuc,
		DmChuyenMucREF,
		TenViTriBanner,
		VitriBannerREF,
		DienGiai,
		ThucChayPhatSinhDauKy,
		ThucChayPhatSinhTrongKy,
		ThucChayPhatSinhCuoiKy,
		KhuyenMaiPhatSinhDauKy,
		KhuyenMaiPhatSinhTrongKy,
		KhuyenMaiPhatSinhCuoiKy,
		NoiBoPhatSinhDauKy,
		NoiBoPhatSinhTrongKy,
		NoiBoPhatSinhCuoiKy,
		SoLuongPhatSinhDauKy,
		SoLuongPhatSinhTrongKy,
		SoLuongPhatSinhCuoiKy,
		SoLuongKhuyenMaiPhatSinhDauKy,
		SoLuongKhuyenMaiPhatSinhTrongKy,
		SoLuongKhuyenMaiPhatSinhCuoiKy,
		SoLuongNoiBoPhatSinhDauKy,
		SoLuongNoiBoPhatSinhTrongKy,
		SoLuongNoiBoPhatSinhCuoiKy,
		CreatedBy,
		CreatedAt,
		LastModifiedBy,
		LastModifiedAt,
		DeletedStatus,
		RecordStatus,
		PrintStatus,
		dstchdc.TenDonViTinh,
		dstchdc.UserName,
		dstchdc.ThucChayThayDoiTrongKy,
		dstchdc.NoiBoThayDoiTrongKy,
		dstchdc.KhuyenMaiThayDoiTrongKy,
		dstchdc.SoLuongThayDoiTrongKy,
		dstchdc.SoLuongNoiBoThayDoiTrongKy,
		dstchdc.SoLuongKhuyenMaiThayDoiTrongKy
	FROM DoanhSoThucChayHopDongCore dstchdc WHERE dstchdc.NgayThucHien BETWEEN @FromDate AND @ToDate
	
END

```
