# Stored Procedure: `Insert_DoanhSoThucChayWebsiteCore_NoiBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:09.507000
- **Ngày sửa cuối**: 2015-03-27 17:44:09.507000

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
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayWebsiteCore_NoiBo]
	@NgayThucHien DATETIME
AS
BEGIN
	INSERT INTO DoanhSoThucChayWebsiteCore
	SELECT tcdt.NgayThucHien,
	       tcdt.DmSanPhamREF,
	       dsp.TenSanPham,
	       tcdt.TenWebsite,
	       tcdt.DmWebsiteREF,
	       '' DienGiai,
	       0 ThucThuDauKy,
	       0 ThucThuTrongKy,
	       0 ThucThuCuoiKy,
	       0 KhuyenMaiDauKy,
	       0 KhuyenMaiTrongKy,
	       0 KhuyenMaiCuoiKy,
	       [dbo].[fn_GetDoanhSoDauKy_Of_DoanhSoThucChayWebsiteCore]
	       (3, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF,
	        tcdt.SysNhanVienREF,
	            tcdt.DmPhongBanREF,
	            tcdt.DmBoPhanREF,
	            tcdt.DmNhomLamViecREF,
	            tcdt.DmHinhThucQuangCao,
	            hd.DmKhachHangREF,
	            tcdt.DmViTriREF,
	            tcdt.HopDongID,
	            tcdt.DonViTinh,
	            tcdt.TenDangNhap) 
	       NoiBoDauKy,
	       SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
	       NoiBoTrongKy,
	       (
	           [dbo].[fn_GetDoanhSoDauKy_Of_DoanhSoThucChayWebsiteCore]
	           (
	           	3,
	            @NgayThucHien, 
	            tcdt.DmSanPhamREF, 
	            tcdt.DmWebsiteREF,
	            tcdt.SysNhanVienREF,
	            tcdt.DmPhongBanREF,
	            tcdt.DmBoPhanREF,
	            tcdt.DmNhomLamViecREF,
	            tcdt.DmHinhThucQuangCao,
	            hd.DmKhachHangREF,
	            tcdt.DmViTriREF,
	            tcdt.HopDongID,
	            tcdt.DonViTinh,
	            tcdt.TenDangNhap
	           ) 
	           + SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
	       ) NoiBoCuoiKy,
	       0 SoLuongPhatSinhDauKy,
	       0 SoLuongPhatSinhTrongKy,
	       0 SoLuongPhatSinhCuoiKy,
	       0 SoLuongKhuyenMaiPhatSinhDauKy,
	       0 SoLuongKhuyenMaiPhatSinhTrongKy,
	       0 SoLuongKhuyenMaiPhatSinhCuoiKy,
	       [dbo].[fn_GetSoLuongDauKy_Of_DoanhSoThucChayWebsiteCore](
	       	3, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF,
	        tcdt.SysNhanVienREF,
	            tcdt.DmPhongBanREF,
	            tcdt.DmBoPhanREF,
	            tcdt.DmNhomLamViecREF,
	            tcdt.DmHinhThucQuangCao,
	            hd.DmKhachHangREF,
	            tcdt.DmViTriREF,
	            tcdt.HopDongID,
	            tcdt.DonViTinh,
	            tcdt.TenDangNhap) 
	       SoLuongNoiBoPhatSinhDauKy,
	       SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) 
	       SoLuongNoiBoPhatSinhTrongKy,
	       (
	           [dbo].[fn_GetSoLuongDauKy_Of_DoanhSoThucChayWebsiteCore](
	           	3, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF, tcdt.SysNhanVienREF,
	            tcdt.DmPhongBanREF,
	            tcdt.DmBoPhanREF,
	            tcdt.DmNhomLamViecREF,
	            tcdt.DmHinhThucQuangCao,
	            hd.DmKhachHangREF,
	            tcdt.DmViTriREF,
	            tcdt.HopDongID,
	            tcdt.DonViTinh,
	            tcdt.TenDangNhap) 
	           + SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	       ) SoLuongNoiBoPhatSinhCuoiKy,
	       'Admin' CreatedBy,
	       GETDATE() CreatedAt,
	       'Admin' LastModifiedBy,
	       GETDATE() LastModifiedAt,
	       0 DeletedStatus,
	       0 RecordStatus,
	       0 PrintStatus,
	       tcdt.TenNhanVien,
	       tcdt.SysNhanVienREF,
	       tcdt.TenPhongBan,
	       tcdt.DmPhongBanREF,
	       tcdt.TenBoPhan,
	       tcdt.DmBoPhanREF,
	       tcdt.TenNhomLamViec,
	       tcdt.DmNhomLamViecREF,
	       tcdt.TenHinhThucQuangCao,
	       tcdt.DmHinhThucQuangCao,
	       tcdt.TenKhachHang,
	       hd.DmKhachHangREF,
	       tcdt.SoHopDong,
	       tcdt.HopDongID,
	       tcdt.TenViTri,
	       tcdt.DmViTriREF,
	       tcdt.DonViTinh,
	       tcdt.TenDangNhap,
	       0 AS ThucChayThayDoiTrongKy,
	       SUM(isnull(tcdt.GiaTriThayDoi,0)) AS NoiBoThayDoiTrongKy,
	       0 AS KhuyenMaiThayDoiTrongKy,
	       0 AS SoLuongThayDoiTrongKy,
	       SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongNoiBoThayDoiTrongKy,
	       0 AS SoLuongKhuyenMaiThayDoiTrongKy
	FROM   ThucChayDaTinh tcdt
	       LEFT JOIN DmSanPham dsp
	            ON  tcdt.DmSanPhamREF = dsp.DmSanPhamID
	       LEFT JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
	WHERE  1 = 1
	       AND tcdt.TrangThaiHopDong <> 3
	       AND CONVERT(date, tcdt.NgayThucHien) = @NgayThucHien
	       AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF, @NgayThucHien) 
	           > 0
	GROUP BY
	       tcdt.NgayThucHien,
	       tcdt.DmSanPhamREF,
	       dsp.TenSanPham,
	       tcdt.TenWebsite,
	       tcdt.DmWebsiteREF,
	       tcdt.TenNhanVien,
	       tcdt.SysNhanVienREF,
	       tcdt.TenPhongBan,
	       tcdt.DmPhongBanREF,
	       tcdt.TenBoPhan,
	       tcdt.DmBoPhanREF,
	       tcdt.TenNhomLamViec,
	       tcdt.DmNhomLamViecREF,
	       tcdt.TenHinhThucQuangCao,
	       tcdt.DmHinhThucQuangCao,
	       tcdt.TenKhachHang,
	       hd.DmKhachHangREF,
	       tcdt.SoHopDong,
	       tcdt.HopDongID,
	       tcdt.TenViTri,
	       tcdt.DmViTriREF,
	       tcdt.DonViTinh,
	       tcdt.TenDangNhap
END

```
