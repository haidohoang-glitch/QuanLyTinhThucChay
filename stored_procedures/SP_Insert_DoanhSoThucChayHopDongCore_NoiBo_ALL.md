# Stored Procedure: `Insert_DoanhSoThucChayHopDongCore_NoiBo_ALL`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:08.100000
- **Ngày sửa cuối**: 2015-03-27 17:44:08.100000

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

--EXEC [dbo].[Insert_DoanhSoThucChayHopDongCore_NoiBo] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayHopDongCore_NoiBo_ALL] 
		@NgayThucHien DATETIME
AS
BEGIN
	
	INSERT INTO DoanhSoThucChayHopDongCore
	SELECT * FROM 
	(
	SELECT tcdt.NgayThucHien, isnull(tcdt.DmMaHopDongREF,0) AS DmMaHopDongREF, isnull(tcdt.TenMaHopDong,'') AS TenMaHopDong, isnull(tcdt.HopDongID,0) AS HopDongID, isnull(tcdt.SoHopDong,'') AS SoHopDong, isnull(tcdt.TenNhanVien,'') AS TenNhanVien
	, isnull(tcdt.SysNhanVienREF,0) as DmNhanVienREF, isnull(tcdt.TenPhongBan,'') AS TenPhongBan, isnull(tcdt.DmPhongBanREF,0) AS  DmPhongBanREF
	, isnull(tcdt.TenBoPhan,'') AS TenBoPhan, isnull(tcdt.DmBoPhanREF,0) AS DmBoPhanREF , isnull(tcdt.TenNhomLamViec,'') AS TenNhomLamViec, isnull(tcdt.DmNhomLamViecREF,0) AS DmNhomLamViecREF
	, isnull(tcdt.TenKhachHang,'') AS TenKhachHang, isnull(hd.DmKhachHangREF,0) AS DmKhachHangREF, isnull(khttc.DmHinhThucKhachHangREF,'') AS DmHinhThucKhachHangREF
	, isnull(khttc.TenHinhThucKhachHang,'') AS TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, isnull(tcdt.DmHinhThucQuangCao,0) AS DmHinhThucQuangCao, isnull(tcdt.TenHinhThucQuangCao,'') AS TenHinhThucQuangCao
	, isnull(tcdt.DmSanPhamREF,0) AS DmSanPhamREF, isnull(tcdt.TenSanPham,'') AS TenSanPham
	, isnull(hdct.TenLoaiNenTang,'') AS TenLoaiNenTang, isnull(hdct.DmLoaiNenTangREF,0) DmLoaiNenTang, isnull(tcdt.DmNhomWebsiteREF,0) NhomWebsite_TagREF, isnull(tcdt.TenNhomWebsite,'') TenNhomWebsite_Tag
	, isnull(tcdt.TenWebsite,'') AS TenWebsite, isnull(tcdt.DmWebsiteREF,0) AS DmWebsiteREF, isnull(tcdt.TenChuyenMuc,'') AS TenChuyenMuc, isnull(tcdt.DmChuyenMucREF,0) AS DmChuyenMucREF
	, isnull(tcdt.TenViTri,'') TenViTriBanner, isnull(tcdt.DmViTriREF,0) DmViTriBannerREF
	, '' DienGiai
	
	, 0 ThucThuDauKy
	, 0 ThucThuTrongKy
	, 0 ThucThuCuoiKy
	
	, 0 AS KhuyenMaiDauKy
	, 0 AS KhuyenMaiTrongKy
	, 0 AS KhuyenMaiCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		3,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),isnull(tcdt.DmNhomWebsiteREF,0),isnull(tcdt.DmWebsiteREF,0),
		isnull(tcdt.DmChuyenMucREF,0),isnull(tcdt.DmViTriREF,0),isnull(hdct.DmLoaiNenTangREF,0),isnull(tcdt.DonViTinh,''),isnull(tcdt.TenDangNhap,'')
		) NoiBoDauKy
	, (	SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) 
		) NoiBoTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		3,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),isnull(tcdt.DmNhomWebsiteREF,0),isnull(tcdt.DmWebsiteREF,0),
		isnull(tcdt.DmChuyenMucREF,0),isnull(tcdt.DmViTriREF,0),isnull(hdct.DmLoaiNenTangREF,0),isnull(tcdt.DonViTinh,''),isnull(tcdt.TenDangNhap,'')
		) +   SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) 
	) NoiBoCuoiKy
	
	, 0 SoLuongPhatSinhDauKy
	, 0 SoLuongPhatSinhTrongKy
	, 0	SoLuongPhatSinhCuoiKy
	
	, 0	SoLuongKhuyenMaiPhatSinhDauKy
	, 0	SoLuongKhuyenMaiPhatSinhTrongKy
	, 0	SoLuongKhuyenMaiPhatSinhCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		3,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),isnull(tcdt.DmNhomWebsiteREF,0),isnull(tcdt.DmWebsiteREF,0),
		isnull(tcdt.DmChuyenMucREF,0),isnull(tcdt.DmViTriREF,0),isnull(hdct.DmLoaiNenTangREF,0),isnull(tcdt.DonViTinh,''),isnull(tcdt.TenDangNhap,'')
		)	SoLuongNoiBoPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) SoLuongNoiBoPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		3,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),isnull(tcdt.DmNhomWebsiteREF,0),isnull(tcdt.DmWebsiteREF,0),
		isnull(tcdt.DmChuyenMucREF,0),isnull(tcdt.DmViTriREF,0),isnull(hdct.DmLoaiNenTangREF,0),isnull(tcdt.DonViTinh,''),isnull(tcdt.TenDangNhap,'')
		) + SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	)	SoLuongNoiBoPhatSinhCuoiKy
	
	, 'Admin' CreatedBy
	, Getdate() CreatedAt
	, 'Admin' LastModifiedBy
	, getdate() LastModifiedAt
	, 0 DeletedStatus
	, 0 RecordStatus
	, 0	PrintStatus
	, tcdt.DonViTinh as TenDonViTinh
	, tcdt.TenDangNhap
	,0 AS ThucChayThayDoiTrongKy
	,SUM(isnull(tcdt.GiaTriThayDoi,0)) NoiBoThayDoiTrongKy
	,0 AS KhuyenMaiThayDoiTrongKy
	,0 AS SoLuongThayDoiTrongKy
	,SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongNoiBoThayDoiTrongKy
	,0 AS SoLuongKhuyenmaiThayDoiTrongKy
	  FROM ThucChayDaTinh tcdt
	  INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
	  LEFT JOIN KhachHangThongTinChung khttc ON khttc.KhachHangThongTinChungID = hd.DmKhachHangREF
	  LEFT JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE 1=1
	AND tcdt.DmSanPhamREF NOT IN (299,337,299,144,585)--Danh sach san pham cua Admarket
	AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
	AND tcdt.HopDongID <> 0	
	AND tcdt.TrangThaiHopDong <> 3
	AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF,@NgayThucHien) > 0
	GROUP BY tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF , tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, khttc.DmHinhThucKhachHangREF, khttc.TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.DmNhomWebsiteREF , tcdt.TenNhomWebsite 
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri , tcdt.DmViTriREF ,hdct.TenLoaiNenTang , hdct.DmLoaiNenTangREF
	, tcdt.DonViTinh
	, tcdt.TenDangNhap
	--, tcdt.ChietKhau, tcdt.IsKhuyenMai
	)A
	WHERE 1=1
	AND (round(A.NoiBoDauKy,0) <> 0 OR round(A.NoiBoTrongKy,0) <> 0)
	UNION
	SELECT * FROM 
	(
	SELECT tcdt.NgayThucHien, isnull(tcdt.DmMaHopDongREF,0) AS DmMaHopDongREF, isnull(tcdt.TenMaHopDong,'') AS TenMaHopDong, isnull(tcdt.HopDongID,0) AS HopDongID, isnull(tcdt.SoHopDong,'') AS SoHopDong, isnull(tcdt.TenNhanVien,'') AS TenNhanVien
	, isnull(tcdt.SysNhanVienREF,0) as DmNhanVienREF, isnull(tcdt.TenPhongBan,'') AS TenPhongBan, isnull(tcdt.DmPhongBanREF,0) AS  DmPhongBanREF
	, isnull(tcdt.TenBoPhan,'') AS TenBoPhan, isnull(tcdt.DmBoPhanREF,0) AS DmBoPhanREF , isnull(tcdt.TenNhomLamViec,'') AS TenNhomLamViec, isnull(tcdt.DmNhomLamViecREF,0) AS DmNhomLamViecREF
	, isnull(tcdt.TenKhachHang,'') AS TenKhachHang, isnull(hd.DmKhachHangREF,0) AS DmKhachHangREF, isnull(khttc.DmHinhThucKhachHangREF,'') AS DmHinhThucKhachHangREF
	, isnull(khttc.TenHinhThucKhachHang,'') AS TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, isnull(tcdt.DmHinhThucQuangCao,0) AS DmHinhThucQuangCao, isnull(tcdt.TenHinhThucQuangCao,'') AS TenHinhThucQuangCao
	, isnull(tcdt.DmSanPhamREF,0) AS DmSanPhamREF, isnull(tcdt.TenSanPham,'') AS TenSanPham
	, isnull(hdct.TenLoaiNenTang,'') AS TenLoaiNenTang, isnull(hdct.DmLoaiNenTangREF,0) DmLoaiNenTang, isnull(tcdt.DmNhomWebsiteREF,0) NhomWebsite_TagREF, isnull(tcdt.TenNhomWebsite,'') TenNhomWebsite_Tag
	, isnull(tcdt.TenWebsite,'') AS TenWebsite, isnull(tcdt.DmWebsiteREF,0) AS DmWebsiteREF, isnull(tcdt.TenChuyenMuc,'') AS TenChuyenMuc, isnull(tcdt.DmChuyenMucREF,0) AS DmChuyenMucREF
	, isnull(tcdt.TenViTri,'') TenViTriBanner, isnull(tcdt.DmViTriREF,0) DmViTriBannerREF
	, '' DienGiai
	
	, 0 ThucThuDauKy
	, 0 ThucThuTrongKy
	, 0 ThucThuCuoiKy
	
	, 0 AS KhuyenMaiDauKy
	, 0 AS KhuyenMaiTrongKy
	, 0 AS KhuyenMaiCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		3,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),isnull(tcdt.DmNhomWebsiteREF,0),isnull(tcdt.DmWebsiteREF,0),
		isnull(tcdt.DmChuyenMucREF,0),isnull(tcdt.DmViTriREF,0),isnull(hdct.DmLoaiNenTangREF,0),isnull(tcdt.DonViTinh,''),isnull(tcdt.TenDangNhap,'')
		) NoiBoDauKy
	, (	SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) 
		) NoiBoTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		3,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),isnull(tcdt.DmNhomWebsiteREF,0),isnull(tcdt.DmWebsiteREF,0),
		isnull(tcdt.DmChuyenMucREF,0),isnull(tcdt.DmViTriREF,0),isnull(hdct.DmLoaiNenTangREF,0),isnull(tcdt.DonViTinh,''),isnull(tcdt.TenDangNhap,'')
		) +   SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) 
	) NoiBoCuoiKy
	
	, 0 SoLuongPhatSinhDauKy
	, 0 SoLuongPhatSinhTrongKy
	, 0	SoLuongPhatSinhCuoiKy
	
	, 0	SoLuongKhuyenMaiPhatSinhDauKy
	, 0	SoLuongKhuyenMaiPhatSinhTrongKy
	, 0	SoLuongKhuyenMaiPhatSinhCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		3,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),isnull(tcdt.DmNhomWebsiteREF,0),isnull(tcdt.DmWebsiteREF,0),
		isnull(tcdt.DmChuyenMucREF,0),isnull(tcdt.DmViTriREF,0),isnull(hdct.DmLoaiNenTangREF,0),isnull(tcdt.DonViTinh,''),isnull(tcdt.TenDangNhap,'')
		)	SoLuongNoiBoPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) SoLuongNoiBoPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		3,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),isnull(tcdt.DmNhomWebsiteREF,0),isnull(tcdt.DmWebsiteREF,0),
		isnull(tcdt.DmChuyenMucREF,0),isnull(tcdt.DmViTriREF,0),isnull(hdct.DmLoaiNenTangREF,0),isnull(tcdt.DonViTinh,''),isnull(tcdt.TenDangNhap,'')
		) + SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	)	SoLuongNoiBoPhatSinhCuoiKy
	
	, 'Admin' CreatedBy
	, Getdate() CreatedAt
	, 'Admin' LastModifiedBy
	, getdate() LastModifiedAt
	, 0 DeletedStatus
	, 0 RecordStatus
	, 0	PrintStatus
	, tcdt.DonViTinh as TenDonViTinh
	, tcdt.TenDangNhap
	,0 AS ThucChayThayDoiTrongKy
	,SUM(isnull(tcdt.GiaTriThayDoi,0)) NoiBoThayDoiTrongKy
	,0 AS KhuyenMaiThayDoiTrongKy
	,0 AS SoLuongThayDoiTrongKy
	,SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongNoiBoThayDoiTrongKy
	,0 AS SoLuongKhuyenmaiThayDoiTrongKy
	  FROM ThucChayDaTinhAdmarKet tcdt
	  INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
	  LEFT JOIN KhachHangThongTinChung khttc ON khttc.KhachHangThongTinChungID = hd.DmKhachHangREF
	  LEFT JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE 1=1
	--AND tcdt.DmSanPhamREF NOT IN (299,337,299,144,585)--Danh sach san pham cua Admarket
	AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
	AND tcdt.HopDongID <> 0	
	AND tcdt.TrangThaiHopDong <> 3
	AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF,@NgayThucHien) > 0
	GROUP BY tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF , tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, khttc.DmHinhThucKhachHangREF, khttc.TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.DmNhomWebsiteREF , tcdt.TenNhomWebsite 
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri , tcdt.DmViTriREF ,hdct.TenLoaiNenTang , hdct.DmLoaiNenTangREF
	, tcdt.DonViTinh
	, tcdt.TenDangNhap
	--, tcdt.ChietKhau, tcdt.IsKhuyenMai
	)A
	WHERE 1=1
	AND (round(A.NoiBoDauKy,0) <> 0 OR round(A.NoiBoTrongKy,0) <> 0 )
	
END

```
