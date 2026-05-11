# Stored Procedure: `Insert_DoanhSoThucChayHopDongCore_ThucThuKhuyenMai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:52.287000
- **Ngày sửa cuối**: 2015-03-27 17:43:52.287000

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

--EXEC dbo].[Insert_DoanhSoThucChayHopDongCore_ThucThuKhuyenMai] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayHopDongCore_ThucThuKhuyenMai] 
		@NgayThucHien DATETIME
AS
BEGIN

	INSERT INTO DoanhSoThucChayHopDongCore
	SELECT * FROM
	(
	SELECT tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF DmNhanVienREF, tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, isnull(khttc.DmHinhThucKhachHangREF,'') AS DmHinhThucKhachHangREF
	, isnull(khttc.TenHinhThucKhachHang,'') AS TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, isnull(hdct.TenLoaiNenTang,'') AS TenLoaiNenTang, isnull(hdct.DmLoaiNenTangREF,0) DmLoaiNenTang, tcdt.DmNhomWebsiteREF NhomWebsite_TagREF, tcdt.TenNhomWebsite TenNhomWebsite_Tag
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri TenViTriBanner, tcdt.DmViTriREF DmViTriBannerREF
	, '' DienGiai
	
	, [dbo].[fn_GetDoanhSoDauKy](
		1,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) ThucThuDauKy
	, (	SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) 
		)ThucThuTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		1,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) +   SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) 
	) ThucThuCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) AS KhuyenMaiDauKy
	, SUM(isnull(tcdt.ThanhTienKM,0) + isnull(tcdt.GiaTriKMThayDoi,0)) AS KhuyenMaiTrongKy
	,( 
	[dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
	) + SUM(isnull(tcdt.ThanhTienKM,0) + isnull(tcdt.GiaTriKMThayDoi,0))
	) AS KhuyenMaiCuoiKy
	
	, 0 NoiBoDauKy
	, 0 NoiBoTrongKy
	, 0 NoiBoCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) SoLuongPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) SoLuongPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) + SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	)	SoLuongPhatSinhCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		)	SoLuongKhuyenMaiPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0)) SoLuongKhuyenMaiPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) + SUM(isnull(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0))
	)	SoLuongKhuyenMaiPhatSinhCuoiKy
	
	, 0	SoLuongNoiBoPhatSinhDauKy
	, 0 SoLuongNoiBoPhatSinhTrongKy
	, 0	SoLuongNoiBoPhatSinhCuoiKy
	
	, 'Admin' CreatedBy
	, Getdate() CreatedAt
	, 'Admin' LastModifiedBy
	, getdate() LastModifiedAt
	, 0 DeletedStatus
	, 0 RecordStatus
	, 0	PrintStatus
	, tcdt.DonViTinh as TenDonViTinh
	, tcdt.TenDangNhap
	,SUM(isnull(tcdt.GiaTriThayDoi,0)) AS ThucChayThayDoiTrongKy
	,0 NoiBoThayDoiTrongKy
	,SUM(isnull(tcdt.GiaTriKMThayDoi,0))  AS KhuyenMaiThayDoiTrongKy
	
	,SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongThayDoiTrongKy
	,0 AS SoLuongNoiBoThayDoiTrongKy
	,SUM(isnull(tcdt.SoLuongKMThayDoi,0)) AS SoLuongKhuyenmaiThayDoiTrongKy
	  FROM ThucChayDaTinhTheoThoiGian tcdt
	  INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
	  -- Doannv sua thanh left join, co ma khach hang khong ton tai trong bang KhachHangThongTinChung
	  LEFT JOIN KhachHangThongTinChung khttc ON khttc.KhachHangThongTinChungID = hd.DmKhachHangREF
	  LEFT JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE 1=1
	AND tcdt.DmSanPhamREF NOT IN (299,337,299,144,585)
	AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
	AND tcdt.HopDongID <> 0	
	AND tcdt.TrangThaiHopDong <> 3
	AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF,@NgayThucHien) =0
	GROUP BY tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF , tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, khttc.DmHinhThucKhachHangREF, khttc.TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.DmNhomWebsiteREF , tcdt.TenNhomWebsite 
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri , tcdt.DmViTriREF ,hdct.TenLoaiNenTang , hdct.DmLoaiNenTangREF
	, tcdt.DonViTinh,tcdt.TenDangNhap
	--, tcdt.ChietKhau, tcdt.IsKhuyenMai
	)A
	WHERE 1=1 
	AND (
		round(A.ThucThuDauKy,0) <>0 OR round(A.ThucThuTrongKy,0) <> 0 
		OR ROUND(A.KhuyenMaiDauKy,0) <> 0 OR ROUND(A.KhuyenMaiTrongKy,0) <> 0 
	)
	UNION
	SELECT * FROM
	(
	SELECT tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF DmNhanVienREF, tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, isnull(khttc.DmHinhThucKhachHangREF,'') AS DmHinhThucKhachHangREF
	, isnull(khttc.TenHinhThucKhachHang,'') AS TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, isnull(hdct.TenLoaiNenTang,'') AS TenLoaiNenTang, isnull(hdct.DmLoaiNenTangREF,0) DmLoaiNenTang, tcdt.DmNhomWebsiteREF NhomWebsite_TagREF, tcdt.TenNhomWebsite TenNhomWebsite_Tag
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri TenViTriBanner, tcdt.DmViTriREF DmViTriBannerREF
	, '' DienGiai
	
	, [dbo].[fn_GetDoanhSoDauKy](
		1,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) ThucThuDauKy
	, (	SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) 
		)ThucThuTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		1,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) +   SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))
	) ThucThuCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) AS KhuyenMaiDauKy
	, SUM(isnull(tcdt.ThanhTienKM,0) + isnull(tcdt.GiaTriKMThayDoi,0)) AS KhuyenMaiTrongKy
	, (
		[dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) +SUM(isnull(tcdt.ThanhTienKM,0) + isnull(tcdt.GiaTriKMThayDoi,0))
		
	) AS KhuyenMaiCuoiKy
	
	, 0 NoiBoDauKy
	, 0 NoiBoTrongKy
	, 0 NoiBoCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) SoLuongPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) SoLuongPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) +  SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	)	SoLuongPhatSinhCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		)	SoLuongKhuyenMaiPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0)) SoLuongKhuyenMaiPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		2,	@NgayThucHien,tcdt.HopDongID,tcdt.SysNhanVienREF,tcdt.DmBoPhanREF,tcdt.HopDongChiTietREF,
		tcdt.DmHinhThucQuangCao,tcdt.DmSanPhamREF,tcdt.DmNhomWebsiteREF,tcdt.DmWebsiteREF,
		tcdt.DmChuyenMucREF,tcdt.DmViTriREF,isnull(hdct.DmLoaiNenTangREF,0),tcdt.DonViTinh,tcdt.TenDangNhap
		) + SUM(isnull(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0))
	)	SoLuongKhuyenMaiPhatSinhCuoiKy
	
	, 0	SoLuongNoiBoPhatSinhDauKy
	, 0 SoLuongNoiBoPhatSinhTrongKy
	, 0	SoLuongNoiBoPhatSinhCuoiKy
	
	, 'Admin' CreatedBy
	, Getdate() CreatedAt
	, 'Admin' LastModifiedBy
	, getdate() LastModifiedAt
	, 0 DeletedStatus
	, 0 RecordStatus
	, 0	PrintStatus
	, tcdt.DonViTinh as TenDonviTinh
	, tcdt.TenDangNhap
	,SUM(isnull(tcdt.GiaTriThayDoi,0)) AS ThucChayThayDoiTrongKy
	,0 NoiBoThayDoiTrongKy
	,SUM(isnull(tcdt.GiaTriKMThayDoi,0))  AS KhuyenMaiThayDoiTrongKy
	
	,SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongThayDoiTrongKy
	,0 AS SoLuongNoiBoThayDoiTrongKy
	,SUM(isnull(tcdt.SoLuongKMThayDoi,0)) AS SoLuongKhuyenmaiThayDoiTrongKy
	  FROM ThucChayDaTinhAdmarKetTheoThoiGian tcdt
	  INNER JOIN HopDong hd ON tcdt.HopDongID = hd.HopDongID
	  -- Doannv sua thanh left join, co ma khach hang khong ton tai trong bang KhachHangThongTinChung
	  LEFT JOIN KhachHangThongTinChung khttc ON khttc.KhachHangThongTinChungID = hd.DmKhachHangREF
	  LEFT JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE 1=1
	--AND tcdt.DmSanPhamREF NOT IN (299,337,299,144,585)
	AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
	AND tcdt.HopDongID <> 0	
	AND tcdt.TrangThaiHopDong <> 3
	AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF,@NgayThucHien) =0
	GROUP BY tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong, tcdt.HopDongID, tcdt.SoHopDong, tcdt.TenNhanVien
	, tcdt.SysNhanVienREF , tcdt.TenPhongBan, tcdt.DmPhongBanREF
	, tcdt.TenBoPhan, tcdt.DmBoPhanREF, tcdt.TenNhomLamViec, tcdt.DmNhomLamViecREF
	, tcdt.TenKhachHang, hd.DmKhachHangREF, khttc.DmHinhThucKhachHangREF, khttc.TenHinhThucKhachHang
	, tcdt.HopDongChiTietREF, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.DmNhomWebsiteREF , tcdt.TenNhomWebsite 
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.TenChuyenMuc, tcdt.DmChuyenMucREF
	, tcdt.TenViTri , tcdt.DmViTriREF ,hdct.TenLoaiNenTang , hdct.DmLoaiNenTangREF
	, tcdt.DonViTinh,tcdt.TenDangNhap
	--, tcdt.ChietKhau, tcdt.IsKhuyenMai
	)A
	WHERE 1=1 
	AND (round(A.ThucThuDauKy,0) <>0 OR round(A.ThucThuTrongKy,0) <> 0 OR 
	ROUND(A.KhuyenMaiDauKy,0) <> 0 OR ROUND(A.KhuyenMaiTrongKy,0) <> 0 )

END

```
