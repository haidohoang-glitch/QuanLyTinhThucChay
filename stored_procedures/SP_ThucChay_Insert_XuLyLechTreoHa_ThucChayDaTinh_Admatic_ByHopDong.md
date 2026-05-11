# Stored Procedure: `ThucChay_Insert_XuLyLechTreoHa_ThucChayDaTinh_Admatic_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-07 11:27:02.790000
- **Ngày sửa cuối**: 2018-08-16 14:49:02.983000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebiste` | `nvarchar(1000)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@ThanhTienHDCT` | `bigint(8)` | No |
| `@GhiChu` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_Insert_GTTD_XuLyLechTreoHa_ThucChayDaTinh_Admatic_ByHopDong] 
	@NgayThucHien = '2018-06-01 00:00:00.000',
	@HopDongID  = 1002190, 
	@DmBannerREF  = 543664,
	@HopDongChiTietID  = 525154,
	@DmWebsiteREF = 13, 
	@TenWebiste = 'afamily.vn',
	@TypeProduct = 5, 
	@DmSanPhamREF = 339,
	@ThanhTienHDCT = 40034150,
	@GhiChu = N'Tinh lai gia tri thuc chay hopdong admatic:QC1150418'
*/
CREATE  PROCEDURE [dbo].[ThucChay_Insert_XuLyLechTreoHa_ThucChayDaTinh_Admatic_ByHopDong] 
	@NgayThucHien DATETIME,
	@HopDongID INT, 
	@DmBannerREF INT,
	@HopDongChiTietID INT,
	@DmWebsiteREF INT, 
	@TenWebiste NVARCHAR(500),
	@TypeProduct INT, 
	@DmSanPhamREF INT,
	@ThanhTienHDCT BIGINT,
	@GhiChu NVARCHAR(2000)
AS
BEGIN
	DECLARE @Note NVARCHAR(500) = N'ADMATIC_THANHTIEN_TD_GTTD xử lý giá trị lệch treo hạ'
	DECLARE @ThanhTienTCDT BIGINT, @ThucChayDaTinhID NVARCHAR(200), @HopDongChiTietID_TiepTheo INT, @DonViTinh NVARCHAR(100)
	, @SoLuongLechTreoHa BIGINT, @ThanhTienLechTreoHa BIGINT
	DECLARE @ThanhTienThucChayXuLy BIGINT, @SoLuongThucChayXuLy BIGINT, @ThanhTienHDCTBf BIGINT, @DonGiaTheoDVT FLOAT, @ChietKhau FLOAT

	--XAC DINH NGAY PHAT SINH GIA TRI LECH TREO HA
	SELECT TOP (1) @ThucChayDaTinhID = ThucChayDaTinhID, @DonGiaTheoDVT = DonGiaTheoDonVi, @ChietKhau = ChietKhau, @DonViTinh = DonViTinh 
	, @SoLuongLechTreoHa = SoLuongThucChayLechTreoHa, @ThanhTienLechTreoHa = ThanhTienLechTreoHa
	FROM dbo.ThucChayDaTinh
	WHERE HopDongChiTietREF = @HopDongChiTietID
	AND HopDongID = @HopDongID
	AND SoLuongThucChayLechTreoHa <> 0
	AND NgayThucHien = @NgayThucHien
	AND GhiChu = @GhiChu
	ORDER BY CreatedAt ASC
	--XAC DINH HOPDONGCHITIET TIEP THEO CAN XU LY
	--Neu tren thuc treo cua Admatic co thong tin hopdongchitiet thi
	SET @GhiChu  = @Note
		SET @HopDongChiTietID_TiepTheo =
		ISNULL((
			SELECT TOP (1) HopDongChiTietREF FROM dbo.ThucChayHopDongChiTietAndBanner_Admatic
			WHERE DmBannerID = CONVERT(NVARCHAR(50),@DmBannerREF)
			AND HopDongREF = @HopDongID
			AND DmSanPhamID = @DmSanPhamREF
			AND DmSanPhamID <> 733
			AND ISNULL(HopDongChiTietREF,0) NOT IN (0,-1)
			ORDER BY HopDongChiTietREF
		),0)
		IF(@HopDongChiTietID_TiepTheo = 0 OR @HopDongChiTietID_TiepTheo = -1)
			BEGIN
				PRINT 'Xac dinh hop dong chi tiet can tinh thuc chay voi dong gia'
				PRINT 'VAO DAY 2'
				SET @HopDongChiTietID_TiepTheo =
				ISNULL((
					SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
					AND att.DmSanPhamREF = tt.DmSanPhamID
					WHERE att.HopDongFK = @HopDongID
					AND att.trangthaithucchay <> 3
					AND att.DmSanPhamREF = @DmSanPhamREF
					AND ABS(att.DonGia - tt.DonGia_Banner) <1 --cho nay xem lai co anh huong den performance
					AND att.DmSanPhamREF <> 733 --khong phai la san pham "Nhieu san pham"
					AND att.DonViTinhREF <> 10 --KHONG PHAI LA GOI
					AND att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
					AND tt.DmBannerID = @DmBannerREF
					ORDER BY att.SoThuTuChay
				),0)
				--PRINT 'hdct: ' + CONVERT(NVARCHAR(100), @HopDongChiTietID)
				IF(@HopDongChiTietID_TiepTheo = 0 OR @HopDongChiTietID_TiepTheo = -1)
				BEGIN
					--PRINT 'VAO DAY 3'
					SET @HopDongChiTietID_TiepTheo =
					ISNULL((
					SELECT TOP (1) HopdongchitietID FROM dbo.AdmaticThuTuChayHopDongChiTiet
					WHERE HopDongFK = @HopDongID
					AND trangthaithucchay <> 3
					AND DmSanPhamREF = 733
					ORDER BY SoThuTuChay
					),0)

					IF(@HopDongChiTietID_TiepTheo = 0 OR @HopDongChiTietID_TiepTheo = -1)
					BEGIN
						--PRINT 'VAO DAY 4'
						SET @HopDongChiTietID_TiepTheo =
						ISNULL((
							SELECT TOP (1) HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet
							WHERE HopDongFK = @HopDongID
							AND (DmSanPhamREF = 733 OR DmSanPhamREF = @DmSanPhamREF)
							AND TrangthaiThucChay <> 3
							ORDER BY SoThuTuChay
						),0)
						IF (@HopDongChiTietID_TiepTheo = 0 OR @HopDongChiTietID_TiepTheo = -1)
						BEGIN
							--PRINT 'VAO DAY 5'
							SET @HopDongChiTietID_TiepTheo =
							ISNULL((
								SELECT TOP (1) HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet
								WHERE HopDongFK = @HopDongID
								AND (DmSanPhamREF = 733 OR DmSanPhamREF = @DmSanPhamREF)
								--AND TrangthaiThucChay <> 3
								ORDER BY SoThuTuChay
							),0)
							--PRINT @HopDongChiTietID
						END
					END
				END
			END

	IF(@ThanhTienLechTreoHa <> 0 AND (@HopDongChiTietID_TiepTheo <> @HopDongChiTietID))
	BEGIN
			PRINT @ThanhTienLechTreoHa
			PRINT @HopDongChiTietID_TiepTheo
			SELECT HopDongChiTietID, SoThuTuChay, ThanhtienThucChay, TrangthaiThucChay, ThucChayDenNgay FROM dbo.AdmaticThuTuChayHopDongChiTiet
			WHERE HopDongChiTietID = @HopDongChiTietID_TiepTheo

			PRINT 'ThucChayDaTinhID thuctinh =' + @ThucChayDaTinhID
			INSERT INTO dbo.ThucChayDaTinh
			(
				ThucChayDaTinhID,
				HopDongID,
				SoHopDong,
				DmMaHopDongREF,
				TenMaHopDong,
				NgayDanhSoHopDong,
				NgayKyHopDong,
				NhanHopDong,
				NgayNhanBanFax,
				NgayNhanHopDongBanCung,
				NgayChuyenHopDongChoKeToan,
				So,
				Thang,
				Nam,
				GiaTriHopDong,
				CongNo,
				HopDongChiTietREF,
				DangSuDung,
				IsGiayPhep,
				TrangThaiHopDong,
				IsBanCung,
				DmPhongBanREF,
				TenPhongBan,
				DmBoPhanREF,
				TenBoPhan,
				DmNhomLamViecREF,
				TenNhomLamViec,
				DmDiaDiemLamViecREF,
				TenDiaDiemLamViec,
				SysNhanVienREF,
				TenDangNhap,
				TenNhanVien,
				TenKhachHang,
				NhanHang,
				DmNhomNganhREF,
				TenNhomNganh,
				DmHinhThucQuangCao,
				TenHinhThucQuangCao,
				DmSanPhamREF,
				TenSanPham,
				DmNhomWebsiteREF,
				TenNhomWebsite,
				DmChuyenMucREF,
				TenChuyenMuc,
				DmLoaiBannerREF,
				TenLoaiBanner,
				DmViTriREF,
				TenViTri,
				DotChayHopDong,
				SoLuongDotChayHD,
				DotChayBooking,
				SoLuongDotChayBooking,
				SoLuong,
				DonViTinh,
				DonGia,
				DonGiaTheoDonVi,
				ChietKhau,
				GiamGia,
				ThanhTien,
				TiLeTuVan,
				ChiPhiTuVan,
				IsKhuyenMai,
				KhuyenMai,
				DmBannerREF,
				DmChienDichREF,
				DmWebsiteREF,
				TenWebsite,
				TongViewThucChay,
				TongClickThucChay,
				TongSoBaiViet,
				SoLuongThucChay,
				NgayThucHien,
				GiaTriThayDoi,
				ThanhTienThucChayTruocTrietKhau,
				GiaTriTrietKhauThucChay,
				ThanhTienSauTrietKhauThucChay,
				GiaTriHoaHongThucChay,
				ThanhTienThucThu,
				ThanhTienKM,
				SoLuongThucChayKM,
				SoLuongThucChayLechTreoHa,
				ThanhTienLechTreoHa,
				CreatedAt,
				LastModifiedAt,
				IsPheDuyet,
				PheDuyetBy,
				PheDuyetAt,
				SoLuongThayDoi,
				SoLuongKMThayDoi,
				GiaTriKMThayDoi,
				GhiChu
			)
	
			SELECT TD.ThucChayDaTinhID, 
			-----------------
			TD.HopDongID,	TD.SoHopDong, 	TD.DmMaHopDongREF, 	TD.TenMaHopDong, 	TD.NgayDanhSoHopDong, TD.NgayKyHopDong, 
			TD.NhanHopDong, TD.NgayNhanBanFax, TD.NgayNhanHopDongBanCung, TD.NgayChuyenHopDongChoKeToan, 
			TD.So, TD.Thang, TD.Nam,	TD.GiaTriHopDong, TD.CongNo,	TD.HopDongChiTietREF,	TD.DangSuDung, TD.IsGiayPhep, 
			TD.TrangThaiHopDong, TD.IsBanCung, 	TD.DmPhongBanREF, 	TD.TenPhongBan, 	TD.DmBoPhanREF, 	TD.TenBoPhan, 	TD.DmNhomLamViecREF, 	
			TD.TenNhom, 	TD.DmDiaDiemLamViecREF, 	TD.TenDiaDiemLamViec, 	TD.SysNhanVienREF, 	
			TD.TenDangNhap,  	TD.TenNhanVien, 	TD.TenKhachHang, 	TD.NhanHang,	TD.DmNhomNganhREF, 	TD.TenNhomNganh, 
			TD.DmHinhThucQuangCao, TD.TenHinhThucQuangCao,	TD.DmSanPhamREF,	TD.TenSanPham,  
			TD.DmNhomWebsiteREF, 	TD.TenNhomWebsite, 	TD.DmChuyenMucREF, 	TD.TenChuyenMuc, 
			TD.DmLoaiBannerREF, 	TD.TenLoaiBanner, 	TD.DmViTriREF, 	TD.TenViTri, 
			TD.DotChayHopDong,	TD.SoLuongDotChayHD, TD.DotChayBooking, TD.SoLuongDotChayBooking, 
			TD.SoLuong,TD.DonViTinh, 
			TD.DonGia,TD.DonGiaTheoDonViTinh,
			TD.ChietKhau, TD.GiamGia, TD.ThanhTien,
			TD.TiLeTuVan,  TD.ChiPhiTuVan,
			TD.IsKhuyenMai,  
			TD.KhuyenMai,
			TD.DmBannerREF,--A.DmBannerREF,
			TD.DmChienDichREF,--A.DmChienDichREF,
			TD.DmWebsiteREF,
			TD.TenWebsite,
			TD.TongViewThucChay,
			TD.TongClickThucChay,
			TD.TongTrueViewThucChay, --Don Vi tinh True View
			TD.SoLuongThucChay,
			TD.NgayThucHien,
			TD.GiaTriThayDoi,
			TD.ThanhTienThucChayTruocTrietKhau,

			TD.GiaTriTrietKhauThucChay,
			TD.ThanhTienSauTrietKhauThucChay,
			TD.GiaTriHoaHongThucChay,
			TD.ThanhTienThucThu,
			TD.ThanhTienKM,
			TD.SoLuongThucChayKM,
			(CASE	WHEN (TD.DonViTinh = 'VIEW') AND (TD.ChietKhau <> 100) then (TD.TongViewThucChay - TD.SoLuongThucChay)
					WHEN  (TD.DonViTinh = 'CLICK') AND (TD.ChietKhau <> 100) then (TD.TongClickThucChay - TD.SoLuongThucChay)
					WHEN  (TD.DonViTinh = 'TRUE VIEW') AND (TD.ChietKhau <> 100) then (TD.TongTrueViewThucChay- TD.SoLuongThucChay)
					--KM
					WHEN (TD.DonViTinh = 'VIEW') AND (TD.ChietKhau = 100) then (TD.TongViewThucChay - TD.SoLuongThucChayKM)
					WHEN  (TD.DonViTinh = 'CLICK') AND (TD.ChietKhau = 100) then (TD.TongClickThucChay - TD.SoLuongThucChayKM)
					WHEN  (TD.DonViTinh = 'TRUE VIEW') AND (TD.ChietKhau = 100) then (TD.TongTrueViewThucChay- TD.SoLuongThucChayKM)
				else 0
				END
			)AS SoLuongLechTreoHa,
			(CASE	WHEN (TD.DonViTinh = 'VIEW')  AND (TD.ChietKhau <> 100)  THEN  (TD.TongViewThucChay - TD.SoLuongThucChay)*TD.DonGiaTheoDonViTinh
					WHEN  (TD.DonViTinh = 'CLICK')  AND (TD.ChietKhau <> 100)  THEN (TD.TongClickThucChay - TD.SoLuongThucChay)*TD.DonGiaTheoDonViTinh
					WHEN  (TD.DonViTinh = 'TRUE VIEW')  AND (TD.ChietKhau <> 100)  THEN (TD.TongTrueViewThucChay - TD.SoLuongThucChay)*TD.DonGiaTheoDonViTinh
					--KM
					WHEN (TD.DonViTinh = 'VIEW')  AND (TD.ChietKhau = 100)  THEN  (TD.TongViewThucChay - TD.SoLuongThucChayKM)*TD.DonGiaTheoDonViTinh
					WHEN  (TD.DonViTinh = 'CLICK')  AND (TD.ChietKhau = 100)   THEN (TD.TongClickThucChay - TD.SoLuongThucChayKM)*TD.DonGiaTheoDonViTinh
					WHEN  (TD.DonViTinh = 'TRUE VIEW')   AND (TD.ChietKhau = 100)  THEN (TD.TongTrueViewThucChay - TD.SoLuongThucChayKM)*TD.DonGiaTheoDonViTinh
				else 0
				END
			)AS ThanhTienLechTreoHa,
			GETDATE() AS CreatedAt,
			GETDATE() AS LastModifiedAt,
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			0 AS SoLuongThayDoi,
			0 AS SoLuongKMThayDoi,
			0 AS GiaTriKMThayDoi,
			@GhiChu GhiChu
			FROM
			(
					SELECT  NEWID() ThucChayDaTinhID, TD.*, 
					ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
					ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
					ISNULL((((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
					ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
					(CASE when TD.IsKhuyenMai=1 then TD.ThanhTienThucChayTruocTrietKhau
						else 0
					  END
					) as ThanhTienKM,
					(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) AND (TD.DonGiaTheoDonViTinh <> 0)) then TD.ThanhTienThucChayTruocTrietKhau/TD.DonGiaTheoDonViTinh
						else 0
					  END
					) as SoLuongThucChayKM
			
					FROM 
					(
					SELECT 

					--ID Hop Dong
					D.HopDongID,
					--Thong tin ve ma so 
					D.SoHopDong, 
					D.DmMaHopDongREF, 
					D.TenMaHopDong, 
					--Thong tin ve thoi gian
					D.NgayDanhSoHopDong, D.NgayKyHopDong, 
					D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
					D.So, D.Thang, D.Nam, 
					--Thong tin ve gia tri
					D.GiaTriHopDong, D.CongNo,
					--Thong tin chi tiet phan bo
					A.HopDongChiTietREF,
					--Thong tin ve trang thai
					D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
					--Thong tin ve Nhan vien kinh doanh
					D.DmPhongBanREF, 
					ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
					D.DmBoPhanREF, 
					ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
					D.DmNhomLamViecREF, 
					ISNULL(D.TenNhom, '') AS TenNhom, 
					D.DmDiaDiemLamViecREF, 
					D.TenDiaDiemLamViec, 
					D.SysNhanVienREF, 
					ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
					D.TenNhanVien, 
					--Thong tin ve khach hang
					--D.DmKhachHangREF, 
					D.TenKhachHang, 
					--C.NhanHang, 
					C.DanhSachNhanHangREF NhanHang,
					C.DmNhomNganhREF, 
					C.TenNhomNganh, 
					--Thong tin hinh thuc quang cao
					C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
					--Thong tin San pham
					dbo.GetProductIDByTypeProduct(A.TypeProduct) as DmSanPhamREF,
					dbo.GetProductNameByTypeProduct(A.TypeProduct) as TenSanPham,  
					C.DmNhomWebsiteREF, 
					C.TenNhomWebsite, 
					C.DmChuyenMucREF, 
					C.TenChuyenMuc, 
					C.DmLoaiBannerREF, 
					C.TenLoaiBanner, 
					C.DmBannerREF DmViTriREF, 
					C.TenViTri, 
					'' AS DotChayHopDong,
					0 AS SoLuongDotChayHD,
					'Xu ly lech treo ha thucchaydatinhid =' + @ThucChayDaTinhID AS  DotChayBooking,
					0 AS SoLuongDotChayBooking, 
					C.SoLuong AS SoLuong,
					(CASE WHEN A.DonViTinh = 'CPM' THEN 'VIEW'
						WHEN A.DonViTinh = 'TRUE VIEW' THEN 'TRUE VIEW'
						ELSE 'CLICK'
						--HAIDH COMMENT: them thong tin don vi tinh voi True View
						END
					 ) DonViTinh, 
					dbo.ThucChay_GetDonGiaByNgayThucHien(A.NgayThucHien,A.HopDongChiTietREF,C.DonGia) as DonGia,
					(CASE when (A.DonViTinh = 'CPM') then CONVERT(FLOAT,A.DonGia_Banner)/1000
						  else  A.DonGia_Banner --DUNG CHO CA CPC VA TRUE VIEW
					  END
					) AS DonGiaTheoDonViTinh,
					C.ChietKhau, C.GiamGia, C.ThanhTien,
					C.TiLeTuVan,  C.ChiPhiTuVan,
					C.IsKhuyenMai,  
					C.KhuyenMai,
					--Thuc chay
					@DmBannerREF DmBannerREF,--A.DmBannerREF,
					0 DmChienDichREF,--A.DmChienDichREF,
					A.DmWebsiteREF,
					A.TenWebsite,
					A.TongViewThucChay,
					A.TongClickThucChay,
					A.TongTrueViewThucChay, --Don Vi tinh True View
					--****haidh chinh sua	
					(CASE WHEN ((C.IsKhuyenMai=0) AND (A.DonViTinh = 'CPM')) 
						  THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (A.TongViewThucChay,A.TongClickThucChay,A.TongTrueViewThucChay,A.DonGia_Banner ,A.DonViTinh,A.NgayThucHien, A.HopDongChiTietREF,C.SoLuong, C.DonGia, C.ThanhTien, C.ChietKhau ),0)
						  WHEN ((C.IsKhuyenMai=0) AND (A.DonViTinh = 'CPC')) 
						  THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (A.TongViewThucChay,A.TongClickThucChay,A.TongTrueViewThucChay,A.DonGia_Banner ,A.DonViTinh,A.NgayThucHien, A.HopDongChiTietREF,C.SoLuong, C.DonGia, C.ThanhTien, C.ChietKhau ),0)
						  --HAIDH COMMENT: them thong tin don vi tinh voi True View
						   WHEN ((C.IsKhuyenMai=0) AND (A.DonViTinh = 'TRUE VIEW')) 
						  THEN ISNULL([dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (A.TongViewThucChay,A.TongClickThucChay,A.TongTrueViewThucChay ,A.DonGia_Banner ,A.DonViTinh,A.NgayThucHien, A.HopDongChiTietREF,C.SoLuong, C.DonGia, C.ThanhTien, C.ChietKhau ),0)
						  ELSE 0
					  END
					) as SoLuongThucChay,
					--Thanhuc Tien Thuc Chay
					A.NgayThucHien,
					0 as GiaTriThayDoi,
					--HAIDH COMMENT: them thong tin don vi tinh voi True View
					ISNULL(dbo.[ThucChay_GetThanhTienChuanThucChay_Admatic](C.SoLuong, C.DonGia, C.ThanhTien, C.ChietKhau,A.DonViTinh,A.DonGia_Banner,D.NgayKyHopDong,A.TongViewThucChay,A.TongClickThucChay,A.TongTrueViewThucChay,A.NgayThucHien,	A.HopDongChiTietREF),0) as ThanhTienThucChayTruocTrietKhau
					from (	
						select 
						@NgayThucHien AS NgayThucHien,
						(CASE WHEN @DonViTinh = 'VIEW' THEN @SoLuongLechTreoHa
						ELSE 0
						END) AS TongViewThucChay,
						(CASE WHEN @DonViTinh = 'CLICK' THEN @SoLuongLechTreoHa
						ELSE 0
						END) AS TongClickThucChay,
						(CASE WHEN @DonViTinh = 'TRUE VIEW' THEN @SoLuongLechTreoHa
						ELSE 0
						END) AS TongTrueViewThucChay,--Don Vi Tinh True View
						@HopDongChiTietID_TiepTheo AS HopDongChiTietREF,
						@DmBannerREF AS DmBannerREF,
						(CASE when (@DonViTinh = 'VIEW') then @DonGiaTheoDVT*1000
						  ELSE  @DonGiaTheoDVT --DUNG CHO CA CPC VA TRUE VIEW
						  END
						)  AS DonGia_Banner,
						(CASE WHEN @DonViTinh = 'VIEW' THEN 'CPM'
							WHEN @DonViTinh = 'CLICK' THEN 'CPC'
							WHEN @DonViTinh = 'TRUE VIEW' THEN 'TRUE VIEW' 
							ELSE ''
						END) AS DonViTinh,
						@TypeProduct AS TypeProduct,
						@DmSanPhamREF AS DmSanPhamref,
						@DmWebsiteREF AS DmWebsiteREF,
						@TenWebiste AS TenWebsite

					 )A
					 INNER JOIN (SELECT * FROM dbo.HopDongChiTiet C WHERE C.HopDongChiTietID = @HopDongChiTietID_TiepTheo) C on C.HopDongChiTietID = A.HopDongChiTietREF
					 INNER JOIN  (SELECT * FROM dbo.HopDong D WHERE D.HopDongID = @HopDongID)D on D.HopDongID = C.HopDongFK
					 WHERE D.TrangThaiHopDong <> 3
					 AND C.DeletedStatus = 0
					 AND C.HopDongChiTietID = @HopDongChiTietID_TiepTheo
					 AND D.HopDongID = @HopDongID
					 AND C.DmLoaiREF = 42 --Admatic
					 AND C.DmSanPhamREF IN  (231,238,339,240,370,598,613,733,342)
					 AND C.DmLoaiBannerREF NOT IN (17,18)--Khong tinh cho cac loai banner ChiPhi va Mua ngoai
					 AND C.DonViTinhREF IN (1,10,2,32) --Chi tinh cho Goi, CPM, CPC, TRUE VIEW
					 ) TD
			)TD

			----CAP NHAT THONG TIN LECH TREO HA
			UPDATE dbo.ThucChayDaTinh
			SET SoLuongThucChayLechTreoHa = 0
			, ThanhTienLechTreoHa = 0
			, DotChayHopDong = N'ThucChayDaTinhID =' + @ThucChayDaTinhID
			WHERE ThucChayDaTinhID = @ThucChayDaTinhID
			AND HopDongID = @HopDongID
			AND HopDongChiTietREF = @HopDongChiTietID
			AND DmHinhThucQuangCao = 42

			--Update lai thu tu tinh thuc chay cho hopdongchitiet
			EXEC [ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] @NgayThucHien,@HopDongChiTietID_TiepTheo
	END
	
END



```
