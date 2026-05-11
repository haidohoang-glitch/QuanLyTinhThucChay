# Stored Procedure: `Insert_DoanhSoThucChayHopDongCore_HDOnline_ThucThuKhuyenMai_ALL`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:08.357000
- **Ngày sửa cuối**: 2015-03-27 17:44:08.357000

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
--EXEC [dbo].[Insert_DoanhSoThucChayHopDongCore_HDOnline_ThucThuKhuyenMai] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayHopDongCore_HDOnline_ThucThuKhuyenMai_ALL] 
		@NgayThucHien DATETIME
AS
BEGIN
	
	INSERT INTO DoanhSoThucChayHopDongCore
	SELECT * FROM 
	(
	SELECT tcdt.NgayThucHien, isnull(tcdt.DmMaHopDongREF,0) AS DmMaHopDongREF, isnull(tcdt.TenMaHopDong,'') AS TenMaHopDong, 0 AS HopDongID, '' AS SoHopDong
	, '' AS TenNhanVien, 0 AS DmNhanVienREF, '' AS TenPhongBan, 0 AS DmPhongBanREF
	, '' AS TenBoPhan, 0 AS DmBoPhanREF, '' AS TenNhomLamViec, 0 AS DmNhomLamViecREF
	, '' AS TenKhachHang, 0 AS DmKhachHangREF, 0  DmHinhThucKhachHangREF, 'Khach hang chay online' AS TenHinhThucKhachHang
	, 0 AS HopDongChiTietREF, isnull(tcdt.DmHinhThucQuangCao,0) AS DmHinhThucQuangCao, isnull(tcdt.TenHinhThucQuangCao,'') AS TenHinhThucQuangCao, 
	isnull(tcdt.DmSanPhamREF,0) AS DmSanPhamREF , isnull(tcdt.TenSanPham,'') AS TenSanPham
	, '' AS TenLoaiNenTang, 0 AS DmLoaiNenTang, 0 AS NhomWebsite_TagREF, '' AS TenNhomWebsite_Tag
	, isnull(tcdt.TenWebsite,'') AS TenWebsite, isnull(tcdt.DmWebsiteREF,0) AS DmWebsiteREF , '' AS TenChuyenMuc, 0 AS DmChuyenMucREF
	, '' AS TenViTriBanner, 0 AS DmViTriBannerREF
	, '' DienGiai
	
	, [dbo].[fn_GetDoanhSoDauKy](
		1,	@NgayThucHien,0,0,0, 0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) ThucThuDauKy
	, SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) ThucThuTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		1,	@NgayThucHien,0,0,0,0
		,isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) +   SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))
	) ThucThuCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,0,0,0, 0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) AS KhuyenMaiDauKy
	, SUM(isnull(tcdt.ThanhTienKM,0) + isnull(tcdt.GiaTriKMThayDoi,0)) AS KhuyenMaiTrongKy
	, (
		[dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) + SUM(isnull(tcdt.ThanhTienKM,0) + isnull(tcdt.GiaTriKMThayDoi,0))
		
	) KhuyenMaiCuoiKy
	
	, 0 NoiBoDauKy
	, 0 NoiBoTrongKy
	, 0 NoiBoCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) SoLuongPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) SoLuongPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) + SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	)	SoLuongPhatSinhCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		)	SoLuongKhuyenMaiPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0)) SoLuongKhuyenMaiPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
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
	, isnull(tcdt.DonViTinh,'') as TenDonViTinh
	, '' as TenDangNhap
	,SUM(isnull(tcdt.GiaTriThayDoi,0)) AS ThucChayThayDoiTrongKy
	,0 NoiBoThayDoiTrongKy
	,SUM(isnull(tcdt.GiaTriKMThayDoi,0))  AS KhuyenMaiThayDoiTrongKy
	
	,SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongThayDoiTrongKy
	,0 AS SoLuongNoiBoThayDoiTrongKy
	,SUM(isnull(tcdt.SoLuongKMThayDoi,0)) AS SoLuongKhuyenmaiThayDoiTrongKy
	  FROM ThucChayDaTinh tcdt
	WHERE 1=1
	AND (tcdt.DmSanPhamREF NOT IN (299,337,299,144,585) AND NOT(tcdt.DmSanPhamREF = 375 AND year(tcdt.NgayThucHien) = 2013)
	) --Danh sach cac SP Admarket
	AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
	AND tcdt.HopDongID = 0
	AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
	GROUP BY tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong
	, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.TenWebsite, tcdt.DmWebsiteREF
	, tcdt.DonViTinh 
	)A
	WHERE 1=1
	AND (round(A.ThucThuDauKy,0) <> 0 OR round(A.ThucThuTrongKy,0) <> 0
	 OR ROUND(a.KhuyenMaiDauKy,0) <> 0 OR ROUND(a.KhuyenMaiTrongKy,0) <> 0)
	UNION
	SELECT * FROM 
	(
	SELECT tcdt.NgayThucHien, isnull(tcdt.DmMaHopDongREF,0) AS DmMaHopDongREF, isnull(tcdt.TenMaHopDong,'') AS TenMaHopDong, 0 AS HopDongID, '' AS SoHopDong
	, '' AS TenNhanVien, 0 AS DmNhanVienREF, '' AS TenPhongBan, 0 AS DmPhongBanREF
	, '' AS TenBoPhan, 0 AS DmBoPhanREF, '' AS TenNhomLamViec, 0 AS DmNhomLamViecREF
	, '' AS TenKhachHang, 0 AS DmKhachHangREF, 0  DmHinhThucKhachHangREF, 'Khach hang chay online' AS TenHinhThucKhachHang
	, 0 AS HopDongChiTietREF, isnull(tcdt.DmHinhThucQuangCao,0) AS DmHinhThucQuangCao, isnull(tcdt.TenHinhThucQuangCao,'') AS TenHinhThucQuangCao, 
	isnull(tcdt.DmSanPhamREF,0) AS DmSanPhamREF , isnull(tcdt.TenSanPham,'') AS TenSanPham
	, '' AS TenLoaiNenTang, 0 AS DmLoaiNenTang, 0 AS NhomWebsite_TagREF, '' AS TenNhomWebsite_Tag
	, isnull(tcdt.TenWebsite,'') AS TenWebsite, isnull(tcdt.DmWebsiteREF,0) AS DmWebsiteREF , '' AS TenChuyenMuc, 0 AS DmChuyenMucREF
	, '' AS TenViTriBanner, 0 AS DmViTriBannerREF
	, '' DienGiai
	
	, [dbo].[fn_GetDoanhSoDauKy](
		1,	@NgayThucHien,0,0,0, 0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) ThucThuDauKy
	, SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) ThucThuTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		1,	@NgayThucHien,0,0,0,0
		,isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) +   SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))
	) ThucThuCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,0,0,0, 0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) AS KhuyenMaiDauKy
	, SUM(isnull(tcdt.ThanhTienKM,0) + isnull(tcdt.GiaTriKMThayDoi,0)) AS KhuyenMaiTrongKy
	, (
		[dbo].[fn_GetDoanhSoDauKy](
		2,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) + SUM(isnull(tcdt.ThanhTienKM,0) + isnull(tcdt.GiaTriKMThayDoi,0))
		
	) KhuyenMaiCuoiKy
	
	, 0 NoiBoDauKy
	, 0 NoiBoTrongKy
	, 0 NoiBoCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) SoLuongPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) SoLuongPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) + SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	)	SoLuongPhatSinhCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		)	SoLuongKhuyenMaiPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChayKM,0) + isnull(tcdt.SoLuongKMThayDoi,0)) SoLuongKhuyenMaiPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		1,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
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
	, isnull(tcdt.DonViTinh,'') as TenDonViTinh
	, '' as TenDangNhap
	,SUM(isnull(tcdt.GiaTriThayDoi,0)) AS ThucChayThayDoiTrongKy
	,0 NoiBoThayDoiTrongKy
	,SUM(isnull(tcdt.GiaTriKMThayDoi,0))  AS KhuyenMaiThayDoiTrongKy
	
	,SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongThayDoiTrongKy
	,0 AS SoLuongNoiBoThayDoiTrongKy
	,SUM(isnull(tcdt.SoLuongKMThayDoi,0)) AS SoLuongKhuyenmaiThayDoiTrongKy
	  FROM ThucChayDaTinhAdmarKet tcdt
	WHERE 1=1
	AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
	AND tcdt.HopDongID = 0
	AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
	GROUP BY tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong
	, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.TenWebsite, tcdt.DmWebsiteREF, tcdt.DonViTinh
	)A
	WHERE 1=1
	AND (round(A.ThucThuDauKy,0) <> 0 OR round(A.ThucThuTrongKy,0) <> 0
	OR ROUND(a.KhuyenMaiDauKy,0) <> 0 OR ROUND(a.KhuyenMaiTrongKy,0) <> 0)

END

```
