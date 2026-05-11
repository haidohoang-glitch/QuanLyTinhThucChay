# Stored Procedure: `Insert_DoanhSoThucChayHopDongCore_KhuyenMai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-23 11:21:36.310000
- **Ngày sửa cuối**: 2014-12-23 14:52:00.997000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayHopDongCore_KhuyenMai]
	@NgayThucHien DATETIME
AS
BEGIN
	DELETE FROM DoanhSoThucChayHopDongCore
	WHERE (KhuyenMaiPhatSinhDauKy <> 0 OR KhuyenMaiPhatSinhTrongKy <> 0 OR KhuyenMaiPhatSinhCuoiKy <> 0)
	AND NgayThucHien = @NgayThucHien

	INSERT INTO DoanhSoThucChayHopDongCore
	SELECT * FROM
	(
	SELECT tcdt.NgayThucHien, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF DmNhanVienREF, tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, khttc.DmHinhThucKhachHangREF, khttc.TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, hdct.TenLoaiNenTang AS TenLoaiNenTang, hdct.DmLoaiNenTangREF DmLoaiNenTang, tcdt.DmNhomWebsiteREF NhomWebsite_TagREF, tcdt.TenNhomWebsite TenNhomWebsite_Tag
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri TenViTriBanner, tcdt.DmViTriREF DmViTriBannerREF
	, '' DienGiai
	
	, 0 ThucThuDauKy
	, 0 ThucThuTrongKy
	, 0 ThucThuCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0)
		) AS KhuyenMaiDauKy
	, (	SUM(tcdt.ThanhTienThucChayTruocTrietKhau + tcdt.GiaTriKMThayDoi) 
		) AS KhuyenMaiTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0)
		) +   SUM(tcdt.ThanhTienThucChayTruocTrietKhau + tcdt.GiaTriKMThayDoi)
	) AS KhuyenMaiCuoiKy
	
	, 0 NoiBoDauKy
	, 0 NoiBoTrongKy
	, 0 NoiBoCuoiKy
	
	, 'Admin' CreatedBy
	, Getdate() CreatedAt
	, 'Admin' LastModifiedBy
	, getdate() LastModifiedAt
	, 0 DeletedStatus
	, 0 RecordStatus
	, 0	PrintStatus
	  FROM ThucChayDaTinh tcdt
	  INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
	  INNER JOIN KhachHangThongTinChung khttc ON khttc.KhachHangThongTinChungID = hd.DmKhachHangREF
	  LEFT JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE 1=1
	AND tcdt.DmSanPhamREF NOT IN (299,337,299,144,585)
	AND tcdt.NgayThucHien = @NgayThucHien
	AND tcdt.HopDongID <> 0	
	AND (tcdt.ChietKhau =100 OR tcdt.IsKhuyenMai = 1)
	GROUP BY tcdt.NgayThucHien, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF , tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, khttc.DmHinhThucKhachHangREF, khttc.TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.DmNhomWebsiteREF , tcdt.TenNhomWebsite 
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri , tcdt.DmViTriREF ,hdct.TenLoaiNenTang , hdct.DmLoaiNenTangREF
	, tcdt.ChietKhau, tcdt.IsKhuyenMai
	)A
	WHERE 1=1 
	AND (round(A.KhuyenMaiDauKy,0) <>0 OR round(A.KhuyenMaiDauKy,0) <> 0 OR round(A.KhuyenMaiCuoiKy,0) <> 0)
	UNION
	SELECT * FROM
	(
	SELECT tcdt.NgayThucHien, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF DmNhanVienREF, tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, khttc.DmHinhThucKhachHangREF, khttc.TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, hdct.TenLoaiNenTang AS TenLoaiNenTang, hdct.DmLoaiNenTangREF DmLoaiNenTang, tcdt.DmNhomWebsiteREF NhomWebsite_TagREF, tcdt.TenNhomWebsite TenNhomWebsite_Tag
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri TenViTriBanner, tcdt.DmViTriREF DmViTriBannerREF
	, '' DienGiai
	
	, 0 ThucThuDauKy
	, 0 ThucThuTrongKy
	, 0 ThucThuCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0)
		) AS KhuyenMaiDauKy
	, (	SUM(tcdt.ThanhTienThucChayTruocTrietKhau + tcdt.GiaTriKMThayDoi) 
		) AS KhuyenMaiTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0)
		) +   SUM(tcdt.ThanhTienThucChayTruocTrietKhau + tcdt.GiaTriKMThayDoi)
	) AS KhuyenMaiCuoiKy
	
	, 0 NoiBoDauKy
	, 0 NoiBoTrongKy
	, 0 NoiBoCuoiKy
	
	, 'Admin' CreatedBy
	, Getdate() CreatedAt
	, 'Admin' LastModifiedBy
	, getdate() LastModifiedAt
	, 0 DeletedStatus
	, 0 RecordStatus
	, 0	PrintStatus
	  FROM ThucChayDaTinhAdmarket tcdt
	  INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
	  INNER JOIN KhachHangThongTinChung khttc ON khttc.KhachHangThongTinChungID = hd.DmKhachHangREF
	  LEFT JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE 1=1
	--AND tcdt.DmSanPhamREF NOT IN (299,337,299,144,585)
	AND tcdt.NgayThucHien = @NgayThucHien
	AND tcdt.HopDongID <> 0	
	AND (tcdt.ChietKhau =100 OR tcdt.IsKhuyenMai = 1)
	GROUP BY tcdt.NgayThucHien, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF , tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, khttc.DmHinhThucKhachHangREF, khttc.TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.DmNhomWebsiteREF , tcdt.TenNhomWebsite 
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri , tcdt.DmViTriREF ,hdct.TenLoaiNenTang , hdct.DmLoaiNenTangREF
	, tcdt.ChietKhau, tcdt.IsKhuyenMai
	)A
	WHERE 1=1 
	AND (round(A.KhuyenMaiDauKy,0) <>0 OR round(A.KhuyenMaiDauKy,0) <> 0 OR round(A.KhuyenMaiCuoiKy,0) <> 0)
END

```
