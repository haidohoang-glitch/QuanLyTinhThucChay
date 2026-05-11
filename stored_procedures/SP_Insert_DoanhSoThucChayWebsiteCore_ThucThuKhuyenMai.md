# Stored Procedure: `Insert_DoanhSoThucChayWebsiteCore_ThucThuKhuyenMai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:09.300000
- **Ngày sửa cuối**: 2015-03-27 17:44:09.300000

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
--EXEC [dbo].[Insert_DoanhSoThucChayWebsiteCore_ThucThuKhuyenMai] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayWebsiteCore_ThucThuKhuyenMai]
	@NgayThucHien DATETIME
AS
BEGIN
	INSERT INTO DoanhSoThucChayWebsiteCore
	SELECT A.* 
	FROM   (
	           SELECT tcdt.NgayThucHien,
	                  tcdt.DmSanPhamREF,
	                  dsp.TenSanPham,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF,
	                  '' DienGiai,
	                  [dbo].[fn_GetDoanhSoDauKy_Of_DoanhSoThucChayWebsiteCore](
	                  	1, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF,
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
	                  ThucThuDauKy,
	                  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
	                  ThucThuTrongKy,
	                  (
	                      [dbo].[fn_GetDoanhSoDauKy_Of_DoanhSoThucChayWebsiteCore](
	                      	1, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF, tcdt.SysNhanVienREF,
	            tcdt.DmPhongBanREF,
	            tcdt.DmBoPhanREF,
	            tcdt.DmNhomLamViecREF,
	            tcdt.DmHinhThucQuangCao,
	            hd.DmKhachHangREF,
	            tcdt.DmViTriREF,
	            tcdt.HopDongID,
	            tcdt.DonViTinh,
	            tcdt.TenDangNhap) 
	                      + SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
	                  ) ThucThuCuoiKy,
	                  [dbo].[fn_GetDoanhSoDauKy_Of_DoanhSoThucChayWebsiteCore](
	                  	2, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF,
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
	                  KhuyenMaiDauKy,
	                  SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) 
	                  KhuyenMaiTrongKy,
	                  (
	                      [dbo].[fn_GetDoanhSoDauKy_Of_DoanhSoThucChayWebsiteCore](
	                      	2, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF, tcdt.SysNhanVienREF,
	            tcdt.DmPhongBanREF,
	            tcdt.DmBoPhanREF,
	            tcdt.DmNhomLamViecREF,
	            tcdt.DmHinhThucQuangCao,
	            hd.DmKhachHangREF,
	            tcdt.DmViTriREF,
	            tcdt.HopDongID,
	            tcdt.DonViTinh,
	            tcdt.TenDangNhap) 
	                      + SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
	                  ) KhuyenMaiCuoiKy,
	                  0 NoiBoDauKy,
	                  0 NoiBoTrongKy,
	                  0 NoiBoCuoiKy,
	                  [dbo].[fn_GetSoLuongDauKy_Of_DoanhSoThucChayWebsiteCore](
	                  	1, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF,
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
	                  SoLuongPhatSinhDauKy,
	                  SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) 
	                  SoLuongPhatSinhTrongKy,
	                  (
	                      [dbo].[fn_GetSoLuongDauKy_Of_DoanhSoThucChayWebsiteCore](
	                      	1, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF, tcdt.SysNhanVienREF,
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
	                  ) SoLuongPhatSinhCuoiKy,
	                  [dbo].[fn_GetSoLuongDauKy_Of_DoanhSoThucChayWebsiteCore](
	                  	2, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF,
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
	                  SoLuongKhuyenMaiPhatSinhDauKy,
	                  SUM(isnull(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0)) 
	                  SoLuongKhuyenMaiPhatSinhTrongKy,
	                  (
	                      [dbo].[fn_GetSoLuongDauKy_Of_DoanhSoThucChayWebsiteCore](
	                      	2, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF, tcdt.SysNhanVienREF,
	            tcdt.DmPhongBanREF,
	            tcdt.DmBoPhanREF,
	            tcdt.DmNhomLamViecREF,
	            tcdt.DmHinhThucQuangCao,
	            hd.DmKhachHangREF,
	            tcdt.DmViTriREF,
	            tcdt.HopDongID,
	            tcdt.DonViTinh,
	            tcdt.TenDangNhap) 
	                      + SUM(isnull(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0))
	                  ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	                  0 SoLuongNoiBoPhatSinhDauKy,
	                  0 SoLuongNoiBoPhatSinhTrongKy,
	                  0 SoLuongNoiBoPhatSinhCuoiKy,
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
					   SUM(isnull(tcdt.GiaTriThayDoi,0)) AS ThucChayThayDoiTrongKy,
					   0 AS NoiBoThayDoiTrongKy,
					   SUM(isnull(tcdt.GiaTriKMThayDoi,0)) AS KhuyenMaiThayDoiTrongKy,
					   SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongThayDoiTrongKy,
					   0 AS SoLuongNoiBoThayDoiTrongKy,
					   SUM(Isnull(tcdt.SoLuongKMThayDoi,0)) AS SoLuongKhuyenMaiThayDoiTrongKy
	           FROM   ThucChayDaTinh tcdt
	                  INNER JOIN DmSanPham dsp
	                       ON  tcdt.DmSanPhamREF = dsp.DmSanPhamID
						LEFT JOIN HopDong hd 
						ON tcdt.HopDongID = hd.HopDongID
	           WHERE  1 = 1
	                  AND tcdt.TrangThaiHopDong <> 3
	                  AND CONVERT(date, tcdt.NgayThucHien) = @NgayThucHien
	                  AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF, @NgayThucHien) = 
	                      0
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
	       )A
	WHERE  (
	           ISNULL(A.ThucThuTrongKy, 0) <> 0
	           OR ISNULL(A.KhuyenMaiTrongKy, 0) <> 0
	       )
END

```
