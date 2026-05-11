# Stored Procedure: `Insert_DoanhSoTienVeCore_NoiBo_History`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-12 10:46:59.347000
- **Ngày sửa cuối**: 2015-06-12 10:46:59.347000

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
--EXEC [dbo].[Insert_DoanhSoTienVeCore_NoiBo_History] '2013-01-03'
CREATE PROCEDURE [dbo].[Insert_DoanhSoTienVeCore_NoiBo_History]
	@NgayThucHien DATETIME
AS
BEGIN
		INSERT INTO DoanhSoTienVeCore
		SELECT @NgayThucHien, hd.HopDongID, hd.SoHopDong
		, hd.NgayDanhSoHopDong
		, hd.NgayKyHopDong
		, hd.TenNhanVien
		, hd.SysNhanVienREF DmNhanVienREF
		, hd.TenPhongBan, isnull(hd.DmPhongBanREF,0) PhongBanREF
		, hd.TenBoPhan, isnull(hd.DmBoPhanREF,0) BoPhanREF
		, hd.TenNhom, isnull(hd.DmNhomREF,0) NhomREF
		, hd.TenKhachHang, hd.DmKhachHangREF
		, khttc.DmHinhThucKhachHangREF
		, khttc.TenHinhThucKhachHang
		, hdct.HopDongChiTietID
		, hdct.DmLoaiREF DmHinhThucQuangCaoREF
		, hdct.TenLoai TenHinhThucQuangCao
		, hdct.DmSanPhamREF
		, hdct.TenSanPham
		, hdct.DmNhomWebsiteREF DmNhomWebsite_TagREF
		, hdct.TenNhomWebsite NhomWebsite_Tag
		, hdct.TenWebsite	, isnull(hdct.DmWebsiteREF,0) AS DmWebsiteREF
		, isnull(hdct.DmChuyenMucREF,0) AS DmChuyenMucREF	, hdct.TenChuyenMuc
		, hdct.TenViTri TenViTriBanner	, isnull(hdct.DmViTriREF,0) ViTriBannerREF
		, isnull(hdct.DmLoaiNenTangREF,0) AS DmLoaiNenTangREF , hdct.TenLoaiNenTang
		--SoLuongThucThu
		, 0 SoLuongPhatSinhDauKy
		, 0 SoLuongPhatSinhTrongKy
		, 0 SoLuongPhatSinhCuoiKy
		--SoLuongKM
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE 0 	
			END	
		) SoLuongKMPhatSinhDauKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN  hdct.SoLuong
				ELSE 0	END) SoLuongKMPhatSinhTrongKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN   hdct.SoLuong
				ELSE 0
		  END	) SoLuongKMPhatSinhCuoiKy
		--SoLuongNB
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE 0 	
			END	
		)SoLuongNBPhatSinhDauKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE hdct.SoLuong	END) SoLuongNBPhatSinhTrongKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE   hdct.SoLuong
		  END	) SoLuongNBPhatSinhCuoiKy
		, hdct.DonViTinhREF
		, isnull(hdct.DonViTinh,'') AS DonViTinh
		, hdct.DonGia
		, hdct.ChietKhau
		--ThanhTienThucThu
		, 0 SoLuongPhatSinhDauKy
		, 0 SoLuongPhatSinhTrongKy
		, 0 SoLuongPhatSinhCuoiKy
		--ThanhTienKM
		, 0 ThanhTienKhuyenMaiDauKy
		, 0 ThanhTienKhuyenMaiPhatSinh
		, 0 ThanhTienKhuyenMaiCuoiKy	
		--ThanhTienNoiBo
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE 0 	END		) NoiBoPhatSinhDauKy
		, 
		(
		CASE WHEN hdct.ChietKhau = 100 THEN 0
		ELSE 
		[dbo].[fn_GetThanhTienByNgay_DoanhSoTienVeCore]
			 (
			  @NgayThucHien,
			  hd.HopDongID,
			  A.ThongTinTienVeID,
			  hdct.ThanhTien
			 )
		end ) ThanhTienNoiBoTrongKy
		, (CASE WHEN hdct.ChietKhau = 100 THEN 0
		ELSE 
		[dbo].[fn_GetThanhTienByNgay_DoanhSoTienVeCore]
			 (@NgayThucHien,
			  hd.HopDongID,
			  A.ThongTinTienVeID,
			  hdct.ThanhTien
			 )
			 END ) ThanhTienNoiBoCuoiKy
		, hd.TrangThaiHopDong		
		, N'DATA_HISTORY' DienGiai
		, 'ASD' CreatedBy
		, GETDATE() CreatedAt
		, 'ASD' LastModifiedBy
		, GETDATE() LastModifiedAt
		, 0 RecordStatus
		, 0 DeletedStatus
		, 0 PrintStatus
		, 0 TypeRecordStatus -- 0 La chay du lieu qua khu
	    , A.NgayThanhToan,
		  A.ThongTinTienVeID,
		  hd.DmMaHopDongREF
		FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
		INNER JOIN 
		(SELECT tthd.HopDongREF,CONVERT(DATE,tthd.NgayThanhToan) AS NgayThanhToan, tthd.ThongTinTienVeID, tthd.GiaTri
		   FROM ThongTinTienVe tthd WHERE Convert(date,tthd.NgayThanhToan) = Convert(date,@NgayThucHien)  AND tthd.DeletedStatus = 0) A
		ON A.HopDongREF = hd.HopDongID
		WHERE 1=1 --convert(date,hd.NgayDanhSoHopDong) = @NgayThucHien
		AND hdct.DeletedStatus = 0
		AND hd.DeletedStatus = 0
		AND hd.TrangThaiHopDong <> 3
		AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF, @NgayThucHien) = 1
		AND (SELECT SUM(ThanhTien) FROM HopDongChiTiet hdct2 WHERE hdct2.HopDongFK = hd.HopDongID) > 0
		AND hd.GiaTriHopDong > 0
		AND hdct.ChietKhau <> 100
		--AND [dbo].[fn_CheckTienVe_DoanhSoTienVeCore](@NgayThucHien,hd.HopDongID) > 0
END

```
