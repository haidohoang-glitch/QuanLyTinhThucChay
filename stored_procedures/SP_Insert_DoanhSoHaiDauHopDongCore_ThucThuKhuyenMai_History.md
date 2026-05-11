# Stored Procedure: `Insert_DoanhSoHaiDauHopDongCore_ThucThuKhuyenMai_History`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 16:42:56.597000
- **Ngày sửa cuối**: 2015-04-22 16:42:56.597000

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
--EXEC [dbo].[Insert_DoanhSoHaiDauHopDongCore_ThucThuKhuyenMai_History] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_DoanhSoHaiDauHopDongCore_ThucThuKhuyenMai_History]
	@NgayThucHien DATETIME
AS
BEGIN
		INSERT INTO DoanhSoHaiDauHopDongCore
		SELECT @NgayThucHien
		    , hd.HopDongID
			, hd.SoHopDong
			, hd.TenNhanVien
			, hd.SysNhanVienREF DmNhanVienREF
			, hd.TenPhongBan
			, isnull(hd.DmPhongBanREF,0) PhongBanREF
			, hd.TenBoPhan
			, isnull(hd.DmBoPhanREF,0)  BoPhanREF
			, hd.TenNhom
			, isnull(hd.DmNhomREF,0) NhomREF
			, hd.TenKhachHang
			, hd.DmKhachHangREF
			, khttc.DmHinhThucKhachHangREF
			, khttc.TenHinhThucKhachHang
			, hdct.HopDongChiTietID
			, hdct.DmLoaiREF DmHinhThucQuangCaoREF
			, hdct.TenLoai TenHinhThucQuangCao
			, hdct.DmSanPhamREF
			, hdct.TenSanPham
			, hdct.DmNhomWebsiteREF DmNhomWebsite_TagREF
			, hdct.TenNhomWebsite NhomWebsite_Tag
			, hdct.TenWebsite	
			, isnull(hdct.DmWebsiteREF,0) AS DmWebsiteREF
			, isnull(hdct.DmChuyenMucREF,0)	 AS DmChuyenMucREF
			, hdct.TenChuyenMuc
			, hdct.TenViTri TenViTriBanner	
			, isnull(hdct.DmViTriREF,0) ViTriBannerREF
			, isnull(hdct.DmLoaiNenTangREF,0) AS DmLoaiNenTangREF
			, hdct.TenLoaiNenTang
		--SoLuongThucThu
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE 0 	
			END	
		)SoLuongPhatSinhDauKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE hdct.SoLuong	END) SoLuongPhatSinhTrongKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE   hdct.SoLuong
		  END	)SoLuongPhatSinhCuoiKy
		--SoLuongKM
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE 0 	END		)SoLuongPhatSinhDauKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong
				ELSE 0	END ) SoLuongPhatSinhTrongKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong
				ELSE 0  END	)SoLuongPhatSinhCuoiKy
		--SoLuongNB
		, 0 SoLuongPhatSinhDauKy
		, 0 SoLuongPhatSinhTrongKy
		, 0 SoLuongPhatSinhCuoiKy
		, hdct.DonViTinhREF
		
		, isnull(hdct.DonViTinh,'') AS DonViTinh
		, hd.TenDangNhap
		, hdct.DonGia
		, hdct.ChietKhau
		--ThanhTienThucThu
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE 0 	END		)SoLuongPhatSinhDauKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE hdct.ThanhTien	END) SoLuongPhatSinhTrongKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE hdct.ThanhTien  END	)SoLuongPhatSinhCuoiKy
		--ThanhTienKM
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN 0
				ELSE 0 	END		)SoLuongPhatSinhDauKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN round(hdct.SoLuong*hdct.DonGia,0)
				ELSE 0	END) SoLuongPhatSinhTrongKy
		, (
			CASE WHEN hdct.ChietKhau = 100 THEN round(hdct.SoLuong*hdct.DonGia,0)
				ELSE 0  END	)SoLuongPhatSinhCuoiKy		
		--ThanhTienNoiBo
		, 0 NoiBoPhatSinhDauKy
		, 0 NoiBoPhatSinhTrongKy
		, 0 NoiBoPhatSinhCuoiKy
		, hd.TrangThaiHopDong
		, N'Chay du lieu qua ky' DienGiai
		, 'ASD' CreatedBy
		, GETDATE() CreatedAt
		, 'ASD' LastModifiedBy
		, GETDATE() LastModifiedAt
		, 0 RecordStatus
		, 0 DeletedStatus
		, 0 PrintStatus
		, 0 TypeRecordStatus -- 0 La chay du lieu qua khu
		, N'Hop Dong Ban Cung' AS TenFileType
		, 0 AS FileTypeREF
		, (SELECT top 1 hdafbc.NgayNhanBanCung FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
		AND hdafbc.NgayNhanBanCung IS NOT NULL) AS NgayNhanBanCung
		, (SELECT top 1 hdafbc.NgayChuyenChoKeToan FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
		AND hdafbc.NgayChuyenChoKeToan IS NOT NULL) AS NgayChuyenChoKeToan
		, hd.NgayDanhSoHopDong
		, hd.NgayKyHopDong
		, hd.DmMaHopDongREF
		FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
		WHERE convert(date,hd.NgayDanhSoHopDong) = @NgayThucHien
		AND hdct.DeletedStatus = 0
		AND hd.DeletedStatus = 0
		AND hd.TrangThaiHopDong <> 3
		AND hd.IsBanCung = 1
		AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](hd.DmMaHopDongREF, @NgayThucHien) = 0
	
END

```
