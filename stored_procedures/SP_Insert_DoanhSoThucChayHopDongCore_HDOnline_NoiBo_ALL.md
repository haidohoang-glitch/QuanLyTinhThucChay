# Stored Procedure: `Insert_DoanhSoThucChayHopDongCore_HDOnline_NoiBo_ALL`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:08.383000
- **Ngày sửa cuối**: 2015-03-27 17:44:08.383000

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
--EXEC [dbo].[Insert_DoanhSoThucChayHopDongCore_HDOnline_NoiBo] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayHopDongCore_HDOnline_NoiBo_ALL] 
		@NgayThucHien DATETIME
AS
BEGIN

	INSERT INTO DoanhSoThucChayHopDongCore
	SELECT * FROM 
	(
	SELECT tcdt.NgayThucHien, ISNULL(tcdt.DmMaHopDongREF,0) AS DmMaHopDongREF, ISNULL(tcdt.TenMaHopDong,'') AS TenMaHopDong, 0 AS HopDongID, '' AS SoHopDong, '' AS TenNhanVien
	, 0 AS DmNhanVienREF, '' AS TenPhongBan, 0 AS DmPhongBanREF
	, '' AS TenBoPhan, 0 AS DmBoPhanREF, '' AS TenNhomLamViec, 0 AS DmNhomLamViecREF
	, '' AS TenKhachHang, 0 DmKhachHangREF, 0 DmHinhThucKhachHangREF, 'Khach hang chay online' AS TenHinhThucKhachHang
	, 0 AS HopDongChiTietREF, isnull(tcdt.DmHinhThucQuangCao,0) AS DmHinhThucQuangCao, isnull(tcdt.TenHinhThucQuangCao,'') AS TenHinhThucQuangCao, isnull(tcdt.DmSanPhamREF,0) AS DmSanPhamREF, isnull(tcdt.TenSanPham,'') AS TenSanPham
	, '' AS TenLoaiNenTang, 0 DmLoaiNenTang, '' AS NhomWebsite_TagREF, '' AS TenNhomWebsite_Tag
	,ISNULL(tcdt.TenWebsite,'') AS TenWebsite, isnull(tcdt.DmWebsiteREF,0) AS DmWebsiteREF, '' AS TenChuyenMuc, 0 AS DmChuyenMucREF
	, '' AS TenViTriBanner, 0 AS DmViTriBannerREF
	, '' DienGiai
	
	, 0 ThucThuDauKy
	, 0 ThucThuTrongKy
	, 0 ThucThuCuoiKy
	
	, 0 AS KhuyenMaiDauKy
	, 0 AS KhuyenMaiTrongKy
	, 0 KhuyenMaiCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		3,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) NoiBoDauKy
	, SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) NoiBoTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		3,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) +   SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0))
	) NoiBoCuoiKy
	
	, 0 SoLuongPhatSinhDauKy
	, 0 SoLuongPhatSinhTrongKy
	, 0	SoLuongPhatSinhCuoiKy
	
	, 0	SoLuongKhuyenMaiPhatSinhDauKy
	, 0	SoLuongKhuyenMaiPhatSinhTrongKy
	, 0	SoLuongKhuyenMaiPhatSinhCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		3,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		)	SoLuongNoiBoPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) SoLuongNoiBoPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		3,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) + SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	)	SoLuongNoiBoPhatSinhCuoiKy
	
	, 'Admin' CreatedBy
	, Getdate() CreatedAt
	, 'Admin' LastModifiedBy
	, getdate() LastModifiedAt
	, 0 DeletedStatus
	, 0 RecordStatus
	, 0	PrintStatus
	, isnull(tcdt.DonViTinh,'') as TenDonViTinh
	, '' as TenDangNhap
	,0 AS ThucChayThayDoiTrongKy
	,SUM(isnull(tcdt.GiaTriThayDoi,0)) NoiBoThayDoiTrongKy
	,0 AS KhuyenMaiThayDoiTrongKy
	,0 AS SoLuongThayDoiTrongKy
	,SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongNoiBoThayDoiTrongKy
	,0 AS SoLuongKhuyenmaiThayDoiTrongKy
	  FROM ThucChayDaTinh tcdt
	WHERE 1=1
	AND (tcdt.DmSanPhamREF NOT IN (299,337,299,144,585) AND NOT(tcdt.DmSanPhamREF = 375 AND year(tcdt.NgayThucHien) = 2013)
	) --Danh sach cac SP Admarket
	AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
	AND tcdt.HopDongID = 0
	AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) <>0
	GROUP BY tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong
	, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.TenWebsite, tcdt.DmWebsiteREF,tcdt.DonViTinh
	)A
	WHERE 1=1
	AND (round(A.NoiBoDauKy,0) <> 0 OR round(A.NoiBoTrongKy,0) <> 0)
	UNION
	SELECT * FROM 
	(
	SELECT tcdt.NgayThucHien, isnull(tcdt.DmMaHopDongREF,0) AS DmMaHopDongREF, isnull(tcdt.TenMaHopDong,'') AS TenMaHopDong, 0 AS HopDongID, '' AS SoHopDong, '' AS TenNhanVien
	, 0 AS DmNhanVienREF, '' AS TenPhongBan, 0 AS DmPhongBanREF
	, '' AS TenBoPhan, 0 AS DmBoPhanREF, '' AS TenNhomLamViec, 0 AS DmNhomLamViecREF
	, '' AS TenKhachHang, 0 DmKhachHangREF, 0 DmHinhThucKhachHangREF, 'Khach hang chay online' AS TenHinhThucKhachHang
	, 0 AS HopDongChiTietREF, isnull(tcdt.DmHinhThucQuangCao,0) AS DmHinhThucQuangCao, isnull(tcdt.TenHinhThucQuangCao,'')AS TenHinhThucQuangCao,
	 isnull(tcdt.DmSanPhamREF,0) AS DmSanPhamREF, isnull(tcdt.TenSanPham,'') AS TenSanPham
	, '' AS TenLoaiNenTang, 0 DmLoaiNenTang, 0 AS NhomWebsite_TagREF, '' AS TenNhomWebsite_Tag
	, isnull(tcdt.TenWebsite,'') AS TenWebsite, isnull(tcdt.DmWebsiteREF,0)AS DmWebsiteREF, '' AS TenChuyenMuc, 0 AS DmChuyenMucREF
	, '' AS TenViTriBanner, 0 AS DmViTriBannerREF
	, '' DienGiai
	, 0 ThucThuDauKy
	, 0 ThucThuTrongKy
	, 0 ThucThuCuoiKy
	
	, 0 AS KhuyenMaiDauKy
	, 0 AS KhuyenMaiTrongKy
	, 0 KhuyenMaiCuoiKy
	
	, [dbo].[fn_GetDoanhSoDauKy](
		3,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) NoiBoDauKy
	, SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) NoiBoTrongKy
	, ([dbo].[fn_GetDoanhSoDauKy](
		3,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) +   SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)) 
	) NoiBoCuoiKy
	
	, 0 SoLuongPhatSinhDauKy
	, 0 SoLuongPhatSinhTrongKy
	, 0	SoLuongPhatSinhCuoiKy
	
	, 0	SoLuongKhuyenMaiPhatSinhDauKy
	, 0	SoLuongKhuyenMaiPhatSinhTrongKy
	, 0	SoLuongKhuyenMaiPhatSinhCuoiKy
	
	, [dbo].[fn_GetSoLuongDauKy](
		3,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		)	SoLuongNoiBoPhatSinhDauKy
	, SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)) SoLuongNoiBoPhatSinhTrongKy
	, ([dbo].[fn_GetSoLuongDauKy](
		3,	@NgayThucHien,0,0,0,0,
		isnull(tcdt.DmHinhThucQuangCao,0),isnull(tcdt.DmSanPhamREF,0),0,isnull(tcdt.DmWebsiteREF,0),0,0,0,isnull(tcdt.DonViTinh,''),''
		) + SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0))
	)	SoLuongNoiBoPhatSinhCuoiKy
	
	, 'Admin' CreatedBy
	, Getdate() CreatedAt
	, 'Admin' LastModifiedBy
	, getdate() LastModifiedAt
	, 0 DeletedStatus
	, 0 RecordStatus
	, 0	PrintStatus
	, isnull(tcdt.DonViTinh,0) as TenDonViTinh
	, '' as TenDangNhap
	,0 AS ThucChayThayDoiTrongKy
	,SUM(isnull(tcdt.GiaTriThayDoi,0)) NoiBoThayDoiTrongKy
	,0 AS KhuyenMaiThayDoiTrongKy
	,0 AS SoLuongThayDoiTrongKy
	,SUM(isnull(tcdt.SoLuongThayDoi,0)) AS SoLuongNoiBoThayDoiTrongKy
	,0 AS SoLuongKhuyenmaiThayDoiTrongKy
	  FROM ThucChayDaTinhAdmarKet tcdt
	WHERE 1=1
	AND convert(date,tcdt.NgayThucHien) = @NgayThucHien
	AND tcdt.HopDongID = 0
	AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) <>0
	GROUP BY tcdt.NgayThucHien, tcdt.DmMaHopDongREF, tcdt.TenMaHopDong
	, tcdt.DmHinhThucQuangCao, tcdt.TenHinhThucQuangCao, tcdt.DmSanPhamREF, tcdt.TenSanPham
	, tcdt.TenWebsite, tcdt.DmWebsiteREF,tcdt.DonViTinh
	)A
	WHERE 1=1
	AND (round(A.NoiBoDauKy,0) <> 0 OR round(A.NoiBoTrongKy,0) <> 0)

END

```
