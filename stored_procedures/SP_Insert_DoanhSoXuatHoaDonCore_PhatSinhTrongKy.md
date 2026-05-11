# Stored Procedure: `Insert_DoanhSoXuatHoaDonCore_PhatSinhTrongKy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-12 10:47:03.460000
- **Ngày sửa cuối**: 2015-06-12 10:47:03.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |
| `@ThongTinHoaDonID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[Insert_DoanhSoXuatHoaDonCore_PhatSinhTrongKy] '2015-01-16',26860,60330,58,67321
CREATE PROCEDURE [dbo].[Insert_DoanhSoXuatHoaDonCore_PhatSinhTrongKy]
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietREF INT,
	@DmMaHopDongREF INT,
	@ThongTinHoaDonID INT
AS
BEGIN
	DECLARE @IsHopDongNoiBo INT --1: HD Noi Bo, 0: HopDong KHONG la Noi Bo
	SET @IsHopDongNoiBo = 0
	SET @IsHopDongNoiBo = [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](@DmMaHopDongREF, @NgayThucHien)
	--DELETE FROM DoanhSoXuatHoaDonCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietREF AND ThongTinHoaDonREF = @ThongTinHoaDonID
	--1. TINH DU LIEU PHAT SINH CHO HOP DONG KHONG PHAI LA NOI BO
	IF(@IsHopDongNoiBo = 0)
	BEGIN
		INSERT INTO DoanhSoXuatHoaDonCore
		SELECT * FROM 
		(
			SELECT @NgayThucHien NgayThucHien
			, hd.HopDongID
			, hd.SoHopDong
			, hd.NgayDanhSoHopDong
			, hd.NgayKyHopDong
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
				END	)SoLuongPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE hdct.SoLuong 
					END) SoLuongPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE  hdct.SoLuong
			  END	)SoLuongPhatSinhCuoiKy
			--SoLuongKM
			, 0 SoLuongKMPhatSinhDauKy
			, 0 SoLuongKMPhatSinhTrongKy
			, 0 SoLuongKMPhatSinhCuoiKy
			--SoLuongNB
			, 0 SoLuongNoiBoPhatSinhDauKy
			, 0 SoLuongNoiBoPhatSinhTrongKy
			, 0 SoLuongNoiBoPhatSinhCuoiKy
			, hdct.DonViTinhREF
			, isnull(hdct.DonViTinh,'') AS DonViTinh
			, hdct.DonGia
			, hdct.ChietKhau
			--ThanhTienThucThu
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE 0 	
				END		)ThucThuPhatSinhDauKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE [dbo].[fn_GetThanhTienByNgay_DoanhSoXuatHoaDonCore] 
					(
						@NgayThucHien,
						hd.HopDongID,
						tthd.ThongTinHoaDonID,
						hdct.ThanhTien
					)
					
				END) ThucThuPhatSinhTrongKy
			, (
				CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE [dbo].[fn_GetThanhTienByNgay_DoanhSoXuatHoaDonCore] 
					(
						@NgayThucHien,
						hd.HopDongID,
						tthd.ThongTinHoaDonID,
						hdct.ThanhTien
					) 
				END	)ThucThuPhatSinhCuoiKy
			--ThanhTienKM
			, 0 KhuyenMaiPhatSinhDauKy
			, 0 KhuyenMaiPhatSinhTrongKy
			, 0 KhuyenMaiPhatSinhCuoiKy
			--ThanhTienNoiBo
			, 0 NoiBoPhatSinhDauKy
			, 0 NoiBoPhatSinhTrongKy
			, 0 NoiBoPhatSinhCuoiKy
			, hd.TrangThaiHopDong as	TrangThaiHD
			, N'Chay du lieu phat sinh ' DienGiai
			, 'ASD' CreatedBy
			, GETDATE() CreatedAt
			, 'ASD' LastModifiedBy
			, GETDATE() LastModifiedAt
			, 0 RecordStatus
			, 0 DeletedStatus
			, 0 PrintStatus
			, 1 TypeRecordStatus -- 0 La chay du lieu qua khu
			,tthd.SoHoaDon AS SoHoaDon
			,tthd.LastModifiedAt AS NgayXuatHoaDon
			,tthd.ThongTinHoaDonID AS ThongTinHoaDonID
			,@DmMaHopDongREF AS mahd
			
			FROM HopDong hd
			INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
			INNER JOIN ThongTinHoaDon tthd ON tthd.HopDongREF = hd.HopDongID
			WHERE hd.HopDongID = @HopDongID
			AND hdct.HopDongChiTietID = @HopDongChiTietREF
			AND tthd.ThongTinHoaDonID = @ThongTinHoaDonID
			AND Hd.TrangThaiHopDong <>3
			AND hdct.DeletedStatus =0
			AND tthd.DeletedStatus =0
			AND (SELECT SUM(ThanhTien) FROM HopDongChiTiet hdct2 WHERE hdct2.HopDongFK = hd.HopDongID) > 0
			AND hd.GiaTriHopDong > 0
			AND hdct.ChietKhau <> 100
		)A
		WHERE (A.SoLuongPhatSinhTrongKy <> 0 
		OR A.ThucThuPhatSinhTrongKy<> 0 ) 	
	END
	--1. TINH DU LIEU PHAT SINH CHO HOP DONG NOI BO
	ELSE
		BEGIN
			INSERT INTO DoanhSoXuatHoaDonCore
			SELECT * FROM
			(
				SELECT @NgayThucHien NgayThucHien
				, hd.HopDongID
				, hd.SoHopDong
				, hd.NgayDanhSoHopDong
				, hd.NgayKyHopDong
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
				, 0 SoLuongKMPhatSinhDauKy
				, 0 SoLuongKMPhatSinhTrongKy
				, 0 SoLuongKMPhatSinhCuoiKy
						
				--SoLuongNB
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE [dbo].[fn_GetSoLuongDauKy_DoanhSoXuatHoaDonCore]
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
													ISNULL(hdct.DonViTinh,''),tthd.SoHoaDon) 	
					END	
				) SoLuongNoiBoPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE hdct.SoLuong - [dbo].[fn_GetSoLuongDauKy_DoanhSoXuatHoaDonCore]
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
													ISNULL(hdct.DonViTinh,''),tthd.SoHoaDon) 	
						END
				) SoLuongNoiBoPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE  hdct.SoLuong
				  END	
				) SoLuongNoiBoPhatSinhCuoiKy
				, hdct.DonViTinhREF
				, isnull(hdct.DonViTinh,'') AS DonViTinh
				, hdct.DonGia
				, hdct.ChietKhau
				--ThanhTienThucThu
				, 0 ThucThuPhatSinhDauKy
				, 0 ThucThuPhatSinhTrongKy
				, 0 ThucThuPhatSinhCuoiKy
				--ThanhTienKM
				, 0 KhuyenMaiPhatSinhDauKy
				, 0 KhuyenMaiPhatSinhTrongKy
				, 0 KhuyenMaiPhatSinhCuoiKy
				--ThanhTienNoiBo
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE [dbo].[fn_GetDoanhSoDauKy_DoanhSoXuatHoaDonCore](3,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
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
														ISNULL(hdct.DonViTinh,''),tthd.SoHoaDon) 	
					END		) NoiBoPhatSinhDauKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
					ELSE [dbo].[fn_GetThanhTienByNgay_DoanhSoXuatHoaDonCore] 
					(
						@NgayThucHien,
						hd.HopDongID,
						tthd.ThongTinHoaDonID,
						hdct.ThanhTien
					) -[dbo].[fn_GetDoanhSoDauKy_DoanhSoXuatHoaDonCore](3,--1 ThucThu, 2 KhuyenMai, 3 NoiBo
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
														ISNULL(hdct.DonViTinh,''),tthd.SoHoaDon)
					END) NoiBoPhatSinhTrongKy
				, (
					CASE WHEN hdct.ChietKhau = 100 THEN 0
						ELSE [dbo].[fn_GetThanhTienByNgay_DoanhSoXuatHoaDonCore] 
					(
						@NgayThucHien,
						hd.HopDongID,
						tthd.ThongTinHoaDonID,
						hdct.ThanhTien
					)  
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
				,tthd.SoHoaDon AS SoHoaDon
			    ,tthd.LastModifiedAt AS NgayXuatHoaDon
			    ,tthd.ThongTinHoaDonID AS ThongTinHoaDonID
			    ,@DmMaHopDongREF AS mahd
				FROM HopDong hd
				INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
				INNER JOIN ThongTinHoaDon tthd ON tthd.HopDongREF = hd.HopDongID
				WHERE hd.HopDongID = @HopDongID
				AND hdct.HopDongFK = @HopDongChiTietREF
				AND tthd.ThongTinHoaDonID = @ThongTinHoaDonID
				AND Hd.TrangThaiHopDong <>3
				AND hdct.DeletedStatus =0
				AND tthd.DeletedStatus =0
				AND (SELECT SUM(ThanhTien) FROM HopDongChiTiet hdct2 WHERE hdct2.HopDongFK = hd.HopDongID) > 0
					AND hd.GiaTriHopDong > 0
					AND hdct.ChietKhau <> 100
			)A
			WHERE (A.SoLuongKMPhatSinhTrongKy <> 0 OR A.SoLuongNoiBoPhatSinhTrongKy <> 0
			OR A.KhuyenMaiPhatSinhTrongKy <> 0 OR A.NoiBoPhatSinhTrongKy <>0)	
		END
		
END

```
