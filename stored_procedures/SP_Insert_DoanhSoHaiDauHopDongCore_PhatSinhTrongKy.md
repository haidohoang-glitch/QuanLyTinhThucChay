# Stored Procedure: `Insert_DoanhSoHaiDauHopDongCore_PhatSinhTrongKy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 16:42:56.657000
- **Ngày sửa cuối**: 2015-04-22 16:42:56.657000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[Insert_DoanhSoHaiDauHopDongCore_PhatSinhTrongKy] '2014-01-31',23318,52984,58

CREATE PROCEDURE [dbo].[Insert_DoanhSoHaiDauHopDongCore_PhatSinhTrongKy]
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmMaHopDongREF INT
AS
BEGIN
	DECLARE @IsHopDongNoiBo INT --1: HD Noi Bo, 0: HopDong KHONG la Noi Bo
	SET @IsHopDongNoiBo = 0
	SET @IsHopDongNoiBo = [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](@DmMaHopDongREF, @NgayThucHien)
	PRINT(@IsHopDongNoiBo)
	--1. TINH DU LIEU PHAT SINH CHO HOP DONG KHONG PHAI LA NOI BO
	IF(@IsHopDongNoiBo = 0)
	BEGIN
		INSERT INTO DoanhSoHaiDauHopDongCore
		SELECT * FROM 
		(
			SELECT @NgayThucHien NgayThucHien
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
					ELSE [dbo].[fn_GetSoLuongDauKy_DoanhSoHaiDauHopDongCore]
						(1,
						@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,''))
				END	)SoLuongPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE hdct.SoLuong - [dbo].[fn_GetSoLuongDauKy_DoanhSoHaiDauHopDongCore]
						(1,
						@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,''))
					END) SoLuongPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE  hdct.SoLuong
			  END	)SoLuongPhatSinhCuoiKy
			--SoLuongKM
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN [dbo].[fn_GetSoLuongDauKy_DoanhSoHaiDauHopDongCore]
						(2,
						@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,''))
					ELSE 0 	END		)SoLuongKMPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong - [dbo].[fn_GetSoLuongDauKy_DoanhSoHaiDauHopDongCore]
						(2,
						@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,''))
					ELSE 0	END ) SoLuongKMPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong
					ELSE 0  END	)SoLuongKMPhatSinhCuoiKy
			--SoLuongNB
			, 0 SoLuongNoiBoPhatSinhDauKy
			, 0 SoLuongNoiBoPhatSinhTrongKy
			, 0 SoLuongNoiBoPhatSinhCuoiKy
			, hdct.DonViTinhREF
			, isnull(hdct.DonViTinh,'') AS DonViTinh
			, hd.TenDangNhap
			, hdct.DonGia
			, hdct.ChietKhau
			--ThanhTienThucThu
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE [dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauHopDongCore](1,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
													@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,'')) 	
				END		)ThucThuPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE hdct.ThanhTien -[dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauHopDongCore](1,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
													@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,''))
				END) ThucThuPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE hdct.ThanhTien  
				END	)ThucThuPhatSinhCuoiKy
			--ThanhTienKM
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN [dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauHopDongCore](2,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
													@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,''))
					ELSE 0 	
				 END )KhuyenMaiPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong*hdct.DonGia - [dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauHopDongCore](2,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
													@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,''))
					ELSE 0
				END) KhuyenMaiPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN (hdct.SoLuong*hdct.DonGia)
					ELSE  0
				END	)KhuyenMaiPhatSinhCuoiKy
			--ThanhTienNoiBo
			, 0 NoiBoPhatSinhDauKy
			, 0 NoiBoPhatSinhTrongKy
			, 0 NoiBoPhatSinhCuoiKy
			, hd.TrangThaiHopDong	
			, N'Chay du lieu phat sinh' DienGiai
			, 'ASD' CreatedBy
			, GETDATE() CreatedAt
			, 'ASD' LastModifiedBy
			, GETDATE() LastModifiedAt
			, 0 RecordStatus
			, 0 DeletedStatus
			, 0 PrintStatus
			, 1 TypeRecordStatus -- 0 La chay du lieu qua khu
			, (SELECT top 1 dft.FileTypeName
			   FROM HopDongAttachFile hdaf INNER JOIN 
			   DmFileType dft ON dft.DmFileTypeID = hdaf.FileTypeREF
			   WHERE hdaf.HopDongREF = hd.HopDongID
			   and hdaf.LastModifiedAt = @NgayThucHien
			  ) AS TenFileType
			, (SELECT top 1 hdaf.FileTypeREF
			   FROM HopDongAttachFile hdaf WHERE hdaf.HopDongREF = hd.HopDongID
			   and hdaf.LastModifiedAt = @NgayThucHien
			  ) AS FileTypeREF
			, (SELECT top 1 hdafbc.NgayNhanBanCung FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
			AND hdafbc.NgayNhanBanCung IS NOT NULL
			) AS NgayNhanBanCung
			, (SELECT top 1 hdafbc.NgayChuyenChoKeToan FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
			AND hdafbc.NgayChuyenChoKeToan IS NOT NULL) AS NgayChuyenChoKeToan
			,hd.NgayDanhSoHopDong
			,hd.NgayKyHopDong
			,hd.DmMaHopDongREF
			FROM HopDong hd
			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
			WHERE hd.HopDongID = @HopDongID
			AND hdct.HopDongChiTietID = @HopDongChiTietREF
			AND hd.IsBanCung =1
			AND hd.TrangThaiHopDong <>3
			AND hdct.DeletedStatus = 0
		)A
		WHERE (A.SoLuongPhatSinhTrongKy <> 0 OR A.SoLuongKMPhatSinhTrongKy <>0 
		OR A.ThucThuPhatSinhTrongKy<> 0 OR A.KhuyenMaiPhatSinhTrongKy <> 0) 	
	END
	--1. TINH DU LIEU PHAT SINH CHO HOP DONG NOI BO
	ELSE
		BEGIN
			INSERT INTO DoanhSoHaiDauHopDongCore
			SELECT * FROM
			(
				SELECT @NgayThucHien NgayThucHien
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
				, 0 SoLuongPhatSinhDauKy
				, 0 SoLuongPhatSinhTrongKy
				, 0 SoLuongPhatSinhCuoiKy
				--SoLuongKM
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN [dbo].[fn_GetSoLuongDauKy_DoanhSoHaiDauHopDongCore]
							(2,
							@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,'')) 	
						ELSE 0	
					END	
				) SoLuongKMPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong - [dbo].[fn_GetSoLuongDauKy_DoanhSoHaiDauHopDongCore]
							(2,
							@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,'')) 	
						ELSE 0
						END
				) SoLuongKMPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN  hdct.SoLuong
						ELSE 0
				  END	
				) SoLuongKMPhatSinhCuoiKy
						
				--SoLuongNB
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE [dbo].[fn_GetSoLuongDauKy_DoanhSoHaiDauHopDongCore]
							(3,
							@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,'')) 	
					END	
				) SoLuongNoiBoPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE hdct.SoLuong - [dbo].[fn_GetSoLuongDauKy_DoanhSoHaiDauHopDongCore]
							(3,
							@NgayThucHien,
													hd.HopDongID,
													hd.SysNhanVienREF,
													isnull(hd.DmBoPhanREF,0),
													isnull(hd.DmPhongBanREF,0),
													isnull(hd.DmNhomLamViecREF,0),
													hd.DmKhachHangREF,
													hdct.HopDongChiTietID,
													hdct.DmLoaiREF,
													hdct.DmSanPhamREF,
													isnull(hdct.DmWebsiteREF,0),
													isnull(hdct.DmChuyenMucREF,0),
													isnull(hdct.DmViTriREF,0),
													isnull(hdct.DmLoaiNenTangREF,0),
													ISNULL(hdct.DonViTinh,'')) 	
						END
				) SoLuongNoiBoPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE  hdct.SoLuong
				  END	
				) SoLuongNoiBoPhatSinhCuoiKy
				, hdct.DonViTinhREF
				, isnull(hdct.DonViTinh,'') AS DonViTinh
				, hd.TenDangNhap
				, hdct.DonGia
				, hdct.ChietKhau
				--ThanhTienThucThu
				, 0 ThucThuPhatSinhDauKy
				, 0 ThucThuPhatSinhTrongKy
				, 0 ThucThuPhatSinhCuoiKy
				--ThanhTienKM
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN [dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauHopDongCore](2,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
														@NgayThucHien,
														hd.HopDongID,
														hd.SysNhanVienREF,
														isnull(hd.DmBoPhanREF,0),
														isnull(hd.DmPhongBanREF,0),
														isnull(hd.DmNhomLamViecREF,0),
														hd.DmKhachHangREF,
														hdct.HopDongChiTietID,
														hdct.DmLoaiREF,
														hdct.DmSanPhamREF,
														isnull(hdct.DmWebsiteREF,0),
														isnull(hdct.DmChuyenMucREF,0),
														isnull(hdct.DmViTriREF,0),
														isnull(hdct.DmLoaiNenTangREF,0),
														ISNULL(hdct.DonViTinh,''))
						ELSE 0 	
					END		) KhuyenMaiPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN hdct.ThanhTien -[dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauHopDongCore](2,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
														@NgayThucHien,
														hd.HopDongID,
														hd.SysNhanVienREF,
														isnull(hd.DmBoPhanREF,0),
														isnull(hd.DmPhongBanREF,0),
														isnull(hd.DmNhomLamViecREF,0),
														hd.DmKhachHangREF,
														hdct.HopDongChiTietID,
														hdct.DmLoaiREF,
														hdct.DmSanPhamREF,
														isnull(hdct.DmWebsiteREF,0),
														isnull(hdct.DmChuyenMucREF,0),
														isnull(hdct.DmViTriREF,0),
														isnull(hdct.DmLoaiNenTangREF,0),
														ISNULL(hdct.DonViTinh,''))
						ELSE 0
					END
				) KhuyenMaiPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN hdct.ThanhTien
						ELSE 0
					END	
				) KhuyenMaiPhatSinhCuoiKy
				--ThanhTienNoiBo
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE [dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauHopDongCore](3,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
														@NgayThucHien,
														hd.HopDongID,
														hd.SysNhanVienREF,
														isnull(hd.DmBoPhanREF,0),
														isnull(hd.DmPhongBanREF,0),
														isnull(hd.DmNhomLamViecREF,0),
														hd.DmKhachHangREF,
														hdct.HopDongChiTietID,
														hdct.DmLoaiREF,
														hdct.DmSanPhamREF,
														isnull(hdct.DmWebsiteREF,0),
														isnull(hdct.DmChuyenMucREF,0),
														isnull(hdct.DmViTriREF,0),
														isnull(hdct.DmLoaiNenTangREF,0),
														ISNULL(hdct.DonViTinh,'')) 	
					END		) NoiBoPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE hdct.ThanhTien -[dbo].[fn_GetDoanhSoDauKy_DoanhSoHaiDauHopDongCore](3,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
														@NgayThucHien,
														hd.HopDongID,
														hd.SysNhanVienREF,
														isnull(hd.DmBoPhanREF,0),
														isnull(hd.DmPhongBanREF,0),
														isnull(hd.DmNhomLamViecREF,0),
														hd.DmKhachHangREF,
														hdct.HopDongChiTietID,
														hdct.DmLoaiREF,
														hdct.DmSanPhamREF,
														isnull(hdct.DmWebsiteREF,0),
														isnull(hdct.DmChuyenMucREF,0),
														isnull(hdct.DmViTriREF,0),
														isnull(hdct.DmLoaiNenTangREF,0),
														ISNULL(hdct.DonViTinh,''))
					END) NoiBoPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE hdct.ThanhTien  
					END	) NoiBoPhatSinhCuoiKy
				, hd.TrangThaiHopDong	
				, N'Chay du lieu phat sinh' DienGiai
				, 'ASD' CreatedBy
				, GETDATE() CreatedAt
				, 'ASD' LastModifiedBy
				, GETDATE() LastModifiedAt
				, 0 RecordStatus
				, 0 DeletedStatus
				, 0 PrintStatus
				, 1 TypeRecordStatus -- 0 La chay du lieu qua khu
				, (SELECT top 1 dft.FileTypeName
				   FROM HopDongAttachFile hdaf INNER JOIN 
				   DmFileType dft ON dft.DmFileTypeID = hdaf.FileTypeREF
				   WHERE hdaf.HopDongREF = hd.HopDongID
				   and hdaf.LastModifiedAt = @NgayThucHien
				  ) AS TenFileType
				, (SELECT top 1 hdaf.FileTypeREF
				   FROM HopDongAttachFile hdaf WHERE hdaf.HopDongREF = hd.HopDongID
				   and hdaf.LastModifiedAt = @NgayThucHien
				  ) AS FileTypeREF
				, (SELECT top 1 hdafbc.NgayNhanBanCung FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
				AND hdafbc.NgayNhanBanCung IS NOT NULL
				) AS NgayNhanBanCung
				, (SELECT top 1 hdafbc.NgayChuyenChoKeToan FROM HopDongAttachFileBanCung hdafbc WHERE hdafbc.HopDongREF = hd.HopDongID
				AND hdafbc.NgayChuyenChoKeToan IS NOT NULL) AS NgayChuyenChoKeToan
			    ,hd.NgayDanhSoHopDong
			    ,hd.NgayKyHopDong
			    ,hd.DmMaHopDongREF
				FROM HopDong hd
				INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
				WHERE hd.HopDongID = @HopDongID
				AND hdct.HopDongFK = @HopDongChiTietREF
				AND hd.IsBanCung = 1
				AND hd.TrangThaiHopDong <>3
			    AND hdct.DeletedStatus = 0
			)A
			WHERE (A.SoLuongKMPhatSinhTrongKy <> 0 OR A.SoLuongNoiBoPhatSinhTrongKy <> 0
			OR A.KhuyenMaiPhatSinhTrongKy <> 0 OR A.NoiBoPhatSinhTrongKy <>0)	
		END
		
END

```
