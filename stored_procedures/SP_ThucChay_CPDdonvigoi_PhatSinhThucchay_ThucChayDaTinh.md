# Stored Procedure: `ThucChay_CPDdonvigoi_PhatSinhThucchay_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-15 15:16:43.340000
- **Ngày sửa cuối**: 2026-02-28 09:54:50.850000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |
| `@NgayDanhSo_GioiHan` | `date(3)` | No |
| `@SohopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Created by:	DWH\haidh
-- Optimized date: 20-09-2024 by DWH\trangtth
-- Description:	tính mới thực chạy sản phẩm CPD gói
-- =============================================
CREATE  PROCEDURE [dbo].[ThucChay_CPDdonvigoi_PhatSinhThucchay_ThucChayDaTinh] 
	@NgayThucHien DATE,
	@NgayDanhSo_GioiHan DATE = NULL,
	@SohopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN
BEGIN TRANSACTION
	DECLARE @Count INT

	CREATE TABLE #DmPhanbo  
	(		HopDongChiTietID INT,
			Ngaythuchien DATETIME,
			DotChayHopDong NVARCHAR(MAX),
			SoLuongDotChayHD INT,
			NhanHang NVARCHAR(MAX)
	)

	--======================================== 0.Xử lý TH chạy lại job ========================
	INSERT INTO #DmPhanbo ( HopDongChiTietID )
	SELECT HopDongChiTietREF
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien) = @NgayThucHien
		AND DmSanPhamREF IN (140,228,564,549,5082) 
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 5 --Đơn vị gói của hình thức CPD 
		AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF IN (17,18))
		AND DotChayBooking = N'CPD_GOI'
		AND GhiChu LIKE N'Tính mới%'
		AND (@NgayDanhSo_GioiHan IS NULL OR NgayDanhSoHopDong >= @NgayDanhSo_GioiHan )
		AND (@SohopDong IS NULL OR SoHopDong = @SohopDong)
		AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)

	SELECT @Count = COUNT(1)
	FROM #DmPhanbo

	IF ISNULL(@Count, 0) >0 
	BEGIN
		DELETE
		FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
		WHERE convert(date,NgayThucHien) = @NgayThucHien
			  AND EXISTS (SELECT HopDongChiTietREF 
						  FROM #DmPhanbo dm 
						  WHERE dm.HopDongChiTietID = hopdongchitietRef)
			  AND GhiChu LIKE N'Tính mới%'
			  AND DotChayBooking = N'CPD_GOI'

		UPDATE tc
		SET tc.RecordStatus = 0
		FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tc 
		WHERE EXISTS (SELECT HopDongChiTietREF 
					  FROM #DmPhanbo dm 
					  WHERE dm.HopDongChiTietID = hopdongchitietRef)

		DELETE
		FROM #DmPhanbo
	END

	--========================================= 1. Xác định danh mục các phân bổ cần tính mới tại ngaythuchien ==============
	INSERT INTO #DmPhanbo (HopDongChiTietID, Ngaythuchien )
	SELECT DISTINCT  hdct.HopDongChiTietID, @NgayThucHien
	FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
	INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tc ON hdct.HopDongChiTietID = tc.HopDongChiTietREF
	INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
	WHERE hdct.DmSanPhamREF in (140,228,564,549,5082)
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 5 --Đơn vị gói của hình thức CPD 
		AND hdct.DeletedStatus = 0
		AND tc.DeletedStatus = 0
		AND hdct.DmLoaiBannerREF NOT IN (17,18)
		AND hdct.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
		AND CONVERT(DATE,tc.LastModifiedAt)  = CONVERT(DATE,@NgayThucHien)
		AND tc.RecordStatus = 0 --thuc treo chua tinh thuc chay
		AND (@NgayDanhSo_GioiHan IS NULL OR NgayDanhSoHopDong >= @NgayDanhSo_GioiHan )
		AND (@SohopDong IS NULL OR SoHopDong = @SohopDong)
		AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)


	--========================================= 2. Tính toán thông số liên quan =============================================
	BEGIN
		-- 1. Thông tin đợt chạy hợp đồng của phân bổ
		--    GetDotChayBookingByHopDongChiTiet(HopDongChiTietID,'Y')
		UPDATE dm
		SET DotChayHopDong = ISNULL(ttdc.thongtindotchaydanhso, 'N/A')
		FROM #Dmphanbo dm
		LEFT JOIN (SELECT hdct.HopDongChiTietID,
												STUFF((	SELECT (Convert(NVARCHAR(50),dchdct.BookingREF) + ' : ' 
																	+ convert(NVARCHAR(10),dchdct.ThoiGianBatDau,101) + ' - ' 
																	+ Convert(NVARCHAR(10), dchdct.ThoiGianKetThuc,101)) + CAST(';' AS VARCHAR(max)) 
														FROM ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet dchdct
														WHERE dchdct.HopDongChiTietREF = hdct.HopDongChiTietID
																AND dchdct.DeletedStatus = 0
														ORDER BY dchdct.BookingREF
														FOR XML PATH('')
													),1,0,'') AS thongtindotchaydanhso
										FROM ABM_Data_ThucChay.dbo.hopdongchitiet hdct  
										WHERE hdct.DeletedStatus = 0 
										GROUP BY hdct.HopDongChiTietID
										) ttdc ON dm.HopDongChiTietID = ttdc.HopDongChiTietID 

		-- 2. Tổng số lượng đánh số của phân bổ 
		--    dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(hdct.SoLuong,hdct.DonViTinh,HopDongChiTietID)
		UPDATE dm
		SET dm.SoLuongDotChayHD = hdct.SoLuong
		FROM #DmPhanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID

		-- 3. Nhãn hàng
		----   TH 1 ngày phân bổ có thể chạy cho nhiều nhãn hàng
		--   [dbo].[f_ReturnListConcatNhanHangREF_v2](HopDongChiTietID, @NgayThucHien)
		--;WITH Temp AS (  SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.DmNhanHangREF
		--				FROM ThucChayHopDongChiTiet tchdct
		--				INNER JOIN #Dmphanbo dm ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		--				WHERE tchdct.DeletedStatus = 0 AND
		--					  CONVERT(DATE, tchdct.ThoiGianBatDau)  <= CONVERT(DATE, dm.NgayThucHien) AND
		--					  CONVERT(DATE, tchdct.ThoiGianKetThuc) >= CONVERT(DATE, dm.NgayThucHien))
		--UPDATE dm
		--SET   dm.Nhanhang = tchdct.nhanhang
		--FROM #Dmphanbo dm
		--INNER JOIN (
		--			SELECT t1.HopDongChiTietREF, 
		--				   STUFF((
		--					   SELECT DISTINCT ',' + CAST(t2.DmNhanHangREF AS VARCHAR(MAX))
		--					   FROM Temp AS t2
		--					   WHERE t2.HopDongChiTietREF = t1.HopDongChiTietREF
		--					   FOR XML PATH(''), TYPE
		--				   ).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS nhanhang
		--			FROM Temp  t1
		--			GROUP BY t1.HopDongChiTietREF ) tchdct ON tchdct.HopDongChiTietREF = dm.HopdongchitietID ;

		--WITH Temp2 AS (  SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.DmNhanHangREF
		--				FROM ThucChayHopDongChiTiet tchdct
		--				INNER JOIN #Dmphanbo dm ON dm.HopdongchitietID = tchdct.HopDongChiTietREF AND dm.Nhanhang IS NULL
		--				WHERE tchdct.DeletedStatus = 0)
		--UPDATE dm
		--SET   dm.Nhanhang = tchdct.nhanhang
		--FROM #Dmphanbo dm
		--INNER JOIN (
		--			SELECT t1.HopDongChiTietREF, 
		--				   STUFF((
		--					   SELECT DISTINCT ',' + CAST(t2.DmNhanHangREF AS VARCHAR(MAX))
		--					   FROM Temp2 AS t2
		--					   WHERE t2.HopDongChiTietREF = t1.HopDongChiTietREF
		--					   FOR XML PATH(''), TYPE
		--				   ).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS nhanhang
		--			FROM Temp2  t1
		--			GROUP BY t1.HopDongChiTietREF ) tchdct ON tchdct.HopDongChiTietREF = dm.HopdongchitietID
		--WHERE dm.Nhanhang IS NULL

		-- TH phân bổ 1 ngày chỉ chạy cho 1 nhãn hàng 
		UPDATE dm
		SET dm.Nhanhang = tchdct.DmNhanHangREF 
		FROM #DmPhanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0 AND
			  CONVERT(DATE, tchdct.ThoiGianBatDau)  <= CONVERT(DATE, dm.NgayThucHien) AND
			  CONVERT(DATE, tchdct.ThoiGianKetThuc) >= CONVERT(DATE, dm.NgayThucHien) AND
			  CAST(tchdct.DmNhanHangREF AS INT) >0 

		UPDATE dm
		SET dm.Nhanhang = tchdct.DmNhanHangREF 
		FROM #DmPhanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0 AND
			  dm.Nhanhang IS NULL 

	END


	--========================================= 3. Chốt thực chạy==============================================================
	BEGIN
		INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
				   ([ThucChayDaTinhID]
				   ,[HopDongID]
				   ,[SoHopDong]
				   ,[DmMaHopDongREF]
				   ,[TenMaHopDong]
				   ,[NgayDanhSoHopDong]
				   ,[NgayKyHopDong]
				   ,[NhanHopDong]
				   ,[NgayNhanBanFax]
				   ,[NgayNhanHopDongBanCung]
				   ,[NgayChuyenHopDongChoKeToan]
				   ,[So]
				   ,[Thang]
				   ,[Nam]
				   ,[GiaTriHopDong]
				   ,[CongNo]
				   ,[HopDongChiTietREF]
				   ,[DangSuDung]
				   ,[IsGiayPhep]
				   ,[TrangThaiHopDong]
				   ,[IsBanCung]
				   ,[DmPhongBanREF]
				   ,[TenPhongBan]
				   ,[DmBoPhanREF]
				   ,[TenBoPhan]
				   ,[DmNhomLamViecREF]
				   ,[TenNhomLamViec]
				   ,[DmDiaDiemLamViecREF]
				   ,[TenDiaDiemLamViec]
				   ,[SysNhanVienREF]
				   ,[TenDangNhap]
				   ,[TenNhanVien]
				   ,[TenKhachHang]
				   ,[NhanHang]
				   ,[DmNhomNganhREF]
				   ,[TenNhomNganh]
				   ,[DmHinhThucQuangCao]
				   ,[TenHinhThucQuangCao]
				   ,[DmSanPhamREF]
				   ,[TenSanPham]
				   ,[DmNhomWebsiteREF]
				   ,[TenNhomWebsite]
				   ,[DmChuyenMucREF]
				   ,[TenChuyenMuc]
				   ,[DmLoaiBannerREF]
				   ,[TenLoaiBanner]
				   ,[DmViTriREF]
				   ,[TenViTri]
				   ,[DotChayHopDong]
				   ,[SoLuongDotChayHD]
				   ,[DotChayBooking]
				   ,[SoLuongDotChayBooking]
				   ,[SoLuong]
				   ,[DonViTinh]
				   ,[DonGia]
				   ,[DonGiaTheoDonVi]
				   ,[ChietKhau]
				   ,[GiamGia]
				   ,[ThanhTien]
				   ,[TiLeTuVan]
				   ,[ChiPhiTuVan]
				   ,[IsKhuyenMai]
				   ,[KhuyenMai]
				   ,[DmBannerREF]
				   ,[DmChienDichREF]
				   ,[DmWebsiteREF]
				   ,[TenWebsite]
				   ,[TongViewThucChay]
				   ,[TongClickThucChay]
				   ,[TongSoBaiViet]
				   ,[SoLuongThucChay]
				   ,[NgayThucHien]
				   ,[GiaTriThayDoi]
				   ,[ThanhTienThucChayTruocTrietKhau]
				   ,[GiaTriTrietKhauThucChay]
				   ,[ThanhTienSauTrietKhauThucChay]
				   ,[GiaTriHoaHongThucChay]
				   ,[ThanhTienThucThu]
				   ,[ThanhTienKM]
				   ,[SoLuongThucChayKM]
				   ,[SoLuongThucChayLechTreoHa]
				   ,[ThanhTienLechTreoHa]
				   ,[CreatedAt]
				   ,[LastModifiedAt]
				   ,[IsPheDuyet]
				   ,[PheDuyetBy]
				   ,[PheDuyetAt]
				   ,[SoLuongThayDoi]
				   ,[SoLuongKMThayDoi]
				   ,[GiaTriKMThayDoi]
				   ,[GhiChu])
		SELECT  NEWID() ThucChayDaTinhID,	
				hd.HopDongID, hd.SoHopDong, 
				hd.DmMaHopDongREF,hd.TenMaHopDong, 
				--Thong tin ve thoi gian
				hd.NgayDanhSoHopDong, hd.NgayKyHopDong, 
				hd.NhanHopDong, hd.NgayNhanBanFax, hd.NgayNhanHopDongBanCung, hd.NgayChuyenHopDongChoKeToan, 
				hd.So, hd.Thang, hd.Nam, 
				--Thong tin ve gia tri
				hd.GiaTriHopDong, hd.CongNo,
				--Thong tin chi tiet phan bo
				dm.HopDongChiTietID,
				--Thong tin ve trang thai
				hd.DangSuDung, hd.IsGiayPhep, hd.TrangThaiHopDong,hd.IsBanCung, 
				--Thong tin ve Nhan vien kinh doanh
				hd.DmPhongBanREF, ISNULL(hd.TenPhongBan, '') AS TenPhongBan, 
				hd.DmBoPhanREF, ISNULL(hd.TenBoPhan,'') AS TenBoPhan, 
				hd.DmNhomLamViecREF,	ISNULL(hd.TenNhom, '') AS TenNhom, 
				hd.DmDiaDiemLamViecREF,	hd.TenDiaDiemLamViec, 
				hd.SysNhanVienREF, ISNULL(hd.TenDangNhap, '') AS TenDangNhap,  
				hd.TenNhanVien, 
				hd.TenKhachHang, 
				--C.NhanHang, 
				dm.NhanHang NhanHang,
				hdct.DmNhomNganhREF,hdct.TenNhomNganh, 
				--Thong tin hinh thuc quang cao
				hdct.DmLoaiREF AS DmHinhThucQuangCao, hdct.TenLoai AS TenHinhThucQuangCao, 
				--Thong tin San pham
				hdct.DmSanPhamREF as DmSanPhamREF,	hdct.TenSanPham,  
				hdct.DmNhomWebsiteREF, hdct.TenNhomWebsite, 
				hdct.DmChuyenMucREF, hdct.TenChuyenMuc,
				hdct.DmLoaiBannerREF, hdct.TenLoaiBanner, 
				hdct.DmViTriREF, hdct.TenViTri, 
				--Thong tin ve Tien
				CAST(dm.DotChayHopDong AS VARCHAR(1000)) DotChayHopDong,
				dm.SoLuongDotChayHD AS SoLuongDotChayHD,
				--Thong tin dot chay cua thuc treo ( vi tinh thuc chay theo dot chay va thuc treo hd)	
				N'CPD_GOI' DotChayBooking,
				0 SoLuongDotChayBooking,
				hdct.SoLuong AS SoLuong, 
				dbo.FormatDonViTinh(hdct.DonViTinh) DonViTinh,
				hdct.DonGia as DonGia, 
				hdct.DonGia AS DonGiaTheoDonViTinh,
				hdct.ChietKhau, hdct.GiamGia, hdct.ThanhTien,
				hdct.TiLeTuVan,  hdct.ChiPhiTuVan,
				hdct.IsKhuyenMai,  
				hdct.KhuyenMai,
				--Thuc chay
				0 DmBannerREF,--A.DmBannerREF,
				0 DmChienDichREF,--A.DmChienDichREF,
				dbo.[GetDmWebsiteReportingdbIDByDmWebsiteID_CPD](hdct.DmWebsiteREF) DmWebsiteREF,
				dbo.[GetWebsiteLinkByDmWebsiteID_CPD](hdct.DmWebsiteREF,hdct.TenWebsite) TenWebsite,
				0 TongViewThucChay,
				0 TongClickThucChay,
				0 TongSoBaiViet,
				hdct.SoLuong as SoLuongThucChay,
				--Thanh Tien Thuc Chay
				@NgayThucHien AS NgayThucHien,
				0 as GiaTriThayDoi,
				ROUND(hdct.SoLuong*hdct.DonGia, 2) as ThanhTienThucChayTruocTrietKhau,
				ROUND(ISNULL((hdct.SoLuong*hdct.DonGia * hdct.ChietKhau)/100,0), 2) AS GiaTriTrietKhauThucChay,
				ROUND(ISNULL((hdct.SoLuong*hdct.DonGia - (hdct.SoLuong*hdct.DonGia * hdct.ChietKhau)/100),0), 2) AS ThanhTienSauTrietKhauThucChay,
				ROUND(ISNULL(((hdct.SoLuong*hdct.DonGia - (hdct.SoLuong*hdct.DonGia * hdct.ChietKhau)/100) * hdct.TiLeTuVan)/100,0), 2) AS GiaTriHoaHongThucChay,
				ROUND(ISNULL((hdct.SoLuong*hdct.DonGia - (hdct.SoLuong*hdct.DonGia * hdct.ChietKhau)/100 - ((hdct.SoLuong*hdct.DonGia - (hdct.SoLuong*hdct.DonGia * hdct.ChietKhau)/100) * hdct.TiLeTuVan)/100),0), 2) AS ThanhTienThucThu,
				(CASE when ((hdct.IsKhuyenMai=1) OR (hdct.ChietKhau = 100)) then ROUND(hdct.SoLuong*hdct.DonGia,2)
					else 0
					END
				) as ThanhTienKM,
				(CASE when ((hdct.IsKhuyenMai=1) OR (hdct.ChietKhau = 100)) then ISNULL(dm.SoLuongDotChayHD,0)
					else 0
					END
				) as SoLuongThucChayKM,
				0 SoLuongThucChayLechTreoHa,
				0 ThanhTienLechTreoHa,
				GETDATE() CreatedAt,
				GETDATE() LastModifiedAt,
				0 IsPheDuyet,
				'' PheDuyetBy,
				'' PheDuyetAt,
				0 SoLuongThayDoi,
				0 SoLuongKMThayDoi,
				0 GiaTriKMThayDoi,
				GhiChu = IIF(@SohopDong IS NULL ,
							 N'Tính mới: SP tối ưu [dbo].[ThucChay_CPDdonvigoi_PhatSinhThucchay_ThucChayDaTinh]' ,
							 N'Tính mới: SP tối ưu xử lý tay [dbo].[ThucChay_CPDdonvigoi_PhatSinhThucchay_ThucChayDaTinh]' )
		FROM #DmPhanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
		INNER JOIN  
			(   SELECT * 
				FROM ABM_Data_ThucChay.dbo.HopDong hd  
				WHERE hd.TrangThaiHopDong <> 3
			) hd on hd.HopDongID = hdct.HopDongFK
		WHERE  hdct.SoLuong >0 

		--========================================= 4. Update trang thai thuc treo CPD DonViGoi===================================
		UPDATE tc
		SET tc.RecordStatus = 1 --Da Tinh Thuc Chay CPD DonViGoi
		FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tc
		INNER JOIN #DmPhanbo kq ON tc.HopDongChiTietREF = kq.HopDongChiTietID
	END

COMMIT TRANSACTION;
END

```
