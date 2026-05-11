# Stored Procedure: `ThucChay_CPDdotchay_PhatSinhThucchay_ThucChayDaTinh_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-18 10:17:35.940000
- **Ngày sửa cuối**: 2025-10-18 10:19:50.283000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |
| `@NgayDanhSo_GioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Created by:	DWH\haidh
-- Optimized date: 20-09-2024 by DWH\trangtth
-- Description:	tính mới thực chạy sản phẩm CPD đợt chạy
-- =============================================
/*
 EXEC [dbo].[ThucChay_CPDdotchay_PhatSinhThucchay_ThucChayDaTinh_dev] 
	@StartDate = '2025-10-17 00:00:00.000',
	@EndDate = '2025-10-17 00:00:00.000',
	--@NgayDanhSo_GioiHan DATE = NULL,
	@SoHopDong = N'QC0541025',
	@HopDongChiTietID  = 767731
*/
CREATE  PROCEDURE [dbo].[ThucChay_CPDdotchay_PhatSinhThucchay_ThucChayDaTinh_dev] 
	@StartDate DATE,
	@EndDate DATE,
	@NgayDanhSo_GioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN
BEGIN TRANSACTION
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @StartDate

	--DELETE FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
	--WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
	--AND DmSanPhamREF IN (140,228,564,549,5082) 
	--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1 --Đơn vị của hình thức CPD 
	--AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF IN (17,18))
	--AND (DotChayBooking <> N'CPD_GOI' or DotChayHopDong <> 'CPD_KhongDotChay')
	--AND GhiChu LIKE N'Tính mới%'
	--AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
	--AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)
	--AND (@NgayDanhSo_GioiHan IS NULL OR NgayDanhSoHopDong >= @NgayDanhSo_GioiHan)

	
	CREATE TABLE #Dmphanbo 
	(    HopdongchitietID INT,
		 Ngaythuchien DATETIME,
	     DotChayHopDong NVARCHAR(MAX),
		 DotChayBooking NVARCHAR(MAX),
		 SoLuongDotChayHD INT,
		 SoLuongDotChayBooking INT,
		 Nhanhang NVARCHAR(MAX),
		 dongia FLOAT,
		 dongiatheodonvitinh FLOAT,
		 soluongthucchay INT, 
		 soluongKM INT,
		 ThanhTienThucChayTruocTrietKhau FLOAT
	)
	--================================================= 1. Xác định phân bổ có thay đổi thông tin ============
	BEGIN
		WHILE(@NgayThucHien <= @EndDate)
		BEGIN
			INSERT INTO #Dmphanbo  (HopdongchitietID, Ngaythuchien, dongia)
			SELECT DISTINCT hdct.HopDongChiTietID, @Ngaythuchien, hdct.DonGia
			FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
			INNER JOIN ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet dchdct ON hdct.HopDongChiTietID = dchdct.HopDongChiTietREF
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK 
			WHERE DmSanPhamREF in (140,228,564,549,5082)
					AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 1 --Đơn vị của hình thức CPD 
					AND hdct.DeletedStatus = 0
					AND dchdct.DeletedStatus = 0
					AND hdct.DmLoaiBannerREF NOT IN (17,18)
					AND hdct.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
					AND CONVERT(DATE,dchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
					AND CONVERT(DATE,dchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien) 
					AND (@NgayDanhSo_GioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan )
					AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
					AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
			SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
		END
	END

	--================================================= 2. Tính toán các thông số liên quan ==================
	BEGIN
		--1. Thông tin đợt chạy hợp đồng của phân bổ
		--   dbo.GetDotChayBookingByHopDongChiTiet(HopDongChiTietID,'Y')
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


		--1. Thông tin đợt chạy thực treo của phân bổ
		--   GetDotChayBookingByHopDongChiTiet(HopDongChiTietID,'N')
		UPDATE dm
		SET dm.DotChayBooking = ISNULL(ttdc.thongtindotchaydanhso, 'N/A')
		FROM #Dmphanbo dm
		LEFT JOIN (SELECT hdct.HopDongChiTietID,
											   STUFF((	SELECT (Convert(NVARCHAR(50),dchdct.BookingREF) + ' : ' 
																	+ convert(NVARCHAR(10),dchdct.ThoiGianBatDau,101) + ' - ' 
																	+ Convert(NVARCHAR(10), dchdct.ThoiGianKetThuc,101)) + CAST(';' AS VARCHAR(max)) 
														FROM ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet dchdct
														INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct ON tchdct.HopDongChiTietREF = dchdct.HopDongChiTietREF 
																   AND tchdct.BookingREF = dchdct.BookingREF
														WHERE dchdct.HopDongChiTietREF = hdct.HopDongChiTietID
															  AND dchdct.DeletedStatus = 0
															  AND tchdct.DeletedStatus = 0
														ORDER BY dchdct.BookingREF
														FOR XML PATH('')
													),1,0,'') AS thongtindotchaydanhso
										FROM ABM_Data_ThucChay.dbo.hopdongchitiet hdct  
										WHERE hdct.DeletedStatus = 0 
										GROUP BY hdct.HopDongChiTietID
										) ttdc ON dm.HopDongChiTietID = ttdc.HopDongChiTietID 

		--2. Tổng số lượng đợt chạy đánh số của phân bổ
		--   dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(hdct.SoLuong,hdct.DonViTinh,HopDongChiTietID)
		UPDATE dm 
		SET dm.SoLuongDotChayHD =          IIF(hdct.DmLoaiBannerREF = 5, 
									  ISNULL(dbo.ThucChay_GetSoLuong_DonViTinh(hdct.SoLuong,hdct.DonViTinh), 0),
									  ISNULL(dchdct.songaydotchaydanhso, 0))
		FROM #Dmphanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopdongchitietID
		LEFT JOIN (SELECT HopDongChiTietREF, ISNULL(SUM(DATEDIFF(day, ThoiGianBatDau, ThoiGianKetThuc) + 1),0) AS songaydotchaydanhso
					FROM ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet
					WHERE RecordStatus = 0 AND DeletedStatus = 0
					GROUP BY HopDongChiTietREF) dchdct ON dchdct.HopDongChiTietREF = dm.HopDongChiTietID

		--3. Tổng số ngày treo của phân bổ 
		--   [GetSoLuongDotChayThucTreoByHopDongChiTiet] (hopdongchitietID)
		UPDATE dm 
		SET dm.SoLuongDotChayBooking = ISNULL(tchdct.songaytreo, 0)
		FROM #Dmphanbo dm
		LEFT JOIN (SELECT HopDongChiTietREF, ISNULL(SUM(DATEDIFF(day, ThoiGianBatDau, ThoiGianKetThuc) + 1),0) AS songaytreo
					FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet
					WHERE  DeletedStatus = 0
					GROUP BY HopDongChiTietREF) tchdct ON tchdct.HopDongChiTietREF = dm.HopDongChiTietID

		--4. Số lượng thực chạy tại ngày hiện tại
		--   ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPDDotChay(@NgayThucHien, HopDongChiTietID)
		UPDATE dm
		SET soluongthucchay = IIF (hdct.ChietKhau = 100 OR hdct.KhuyenMai = 1 ,
								   0,
								   IIF (hdct.DmLoaiBannerREF = 5, IIF(tchdct.soluong > 0, 1, 0),
								   ISNULL(tchdct.soluong, 0))
								  ),
			soluongKM =	   IIF (hdct.ChietKhau = 100 OR hdct.KhuyenMai = 1 ,
								IIF (hdct.DmLoaiBannerREF = 5, IIF(tchdct.soluong > 0, 1, 0),
								ISNULL(tchdct.soluong, 0)),
								0
								  )
		FROM  #Dmphanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopdongchitietID
		LEFT JOIN ( SELECT dm.HopdongchitietID, dm.NgayThucHien, COUNT(tchdct.BookingREF) AS soluong
					FROM #Dmphanbo dm 
					INNER JOIN (
								SELECT DISTINCT dchdct.HopDongChiTietREF, tchdct.BookingREF, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc
								FROM ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet dchdct
								INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct ON tchdct.HopDongChiTietREF = dchdct.HopDongChiTietREF 
																				AND dchdct.BookingREF = tchdct.BookingREF
								WHERE tchdct.DeletedStatus = 0
									  AND dchdct.DeletedStatus = 0
									  AND year(dchdct.ThoiGianKetThuc) >= 2013
								) tchdct 
							ON tchdct.HopDongChiTietREF = dm.HopdongchitietID AND
								CONVERT(DATE,tchdct.ThoiGianBatDau)  <= CONVERT(DATE, dm.NgayThucHien) AND
								CONVERT(DATE,tchdct.ThoiGianKetThuc) >= CONVERT(DATE, dm.NgayThucHien)
					GROUP BY dm.HopdongchitietID, dm.NgayThucHien ) tchdct ON dm.HopdongchitietID = tchdct.HopdongchitietID


		--5. Đơn giá chuẩn theo ngày
		--   ThucChay_GetDonGiaChuanTheoDonViTinh(hdct.SoLuong,hdct.DonViTinh,hdct.DonGia,hd.NgayKyHopDong, @NgayThucHien, HopDongChiTietID)
		UPDATE dm
		SET dm.dongiatheodonvitinh = IIF(dm.SoLuongDotChayHD = 0, 0, (hdct.SoLuong*hdct.DonGia)/dm.SoLuongDotChayHD)
		FROM #Dmphanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopdongchitietID ;
	
		--6. nhãn hàng
		----   TH 1 ngày phân bổ có thể chạy cho nhiều nhãn hàng
		--   [dbo].[f_ReturnListConcatNhanHangREF_v2](HopDongChiTietID, @NgayThucHien)
		--WITH Temp AS (  SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.DmNhanHangREF
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
		SET dm.Nhanhang = CAST(tchdct.DmNhanHangREF AS INT)
		FROM #DmPhanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0 AND
			  CONVERT(DATE, tchdct.ThoiGianBatDau)  <= CONVERT(DATE, dm.NgayThucHien) AND
			  CONVERT(DATE, tchdct.ThoiGianKetThuc) >= CONVERT(DATE, dm.NgayThucHien) AND
			  CAST(tchdct.DmNhanHangREF AS INT) >0 

		UPDATE dm
		SET dm.Nhanhang = CAST(tchdct.DmNhanHangREF AS INT)
		FROM #DmPhanbo dm
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0 AND
			  dm.Nhanhang IS NULL 


		--7. Thành tiền trước chiết khấu
		--   dbo.ThucChay_GetThanhTienChuanThucChay_CPD(hdct.SoLuong,hdct.DonViTinh,hdct.DonGia,hd.NgayKyHopDong,@NgayThucHien, HopDongChiTietID)
		UPDATE dm
		SET dm.ThanhTienThucChayTruocTrietKhau = dm.dongiatheodonvitinh * (dm.soluongthucchay+dm.soluongKM)
		FROM #Dmphanbo dm
	END

	--================================================= 3. chốt thực chạy ====================================
	--INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh

	SELECT  NEWID() ThucChayDaTinhID,
			--ID Hop Dong
			hd.HopDongID, hd.SoHopDong, 
			hd.DmMaHopDongREF,hd.TenMaHopDong, 
			--Thong tin ve thoi gian
			hd.NgayDanhSoHopDong, hd.NgayKyHopDong, 
			hd.NhanHopDong, hd.NgayNhanBanFax, hd.NgayNhanHopDongBanCung, hd.NgayChuyenHopDongChoKeToan, 
			hd.So, hd.Thang, hd.Nam, 
			--Thong tin ve gia tri
			hd.GiaTriHopDong, hd.CongNo,
			--Thong tin chi tiet phan bo
			hdct.HopDongChiTietID,
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
			dm.Nhanhang NhanHang,
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
			CAST(dm.DotChayBooking AS VARCHAR(1000)) DotChayBooking,
			dm.SoLuongDotChayBooking SoLuongDotChayBooking,
			--0 SoLuongDotChayBooking,
			hdct.SoLuong AS SoLuong, 
			dbo.FormatDonViTinh(hdct.DonViTinh) DonViTinh,
			ROUND(dm.dongia, 2) as DonGia, 
			ROUND(dm.dongiatheodonvitinh, 2) AS DonGiaTheoDonViTinh,
			hdct.ChietKhau, hdct.GiamGia, hdct.ThanhTien,
			hdct.TiLeTuVan,  hdct.ChiPhiTuVan,
			hdct.IsKhuyenMai,  
			hdct.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			--dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(hdct.DmWebsiteREF) DmWebsiteREF,
			dbo.[GetDmWebsiteReportingdbIDByDmWebsiteID_CPD](hdct.DmWebsiteREF) DmWebsiteREF,
			--dbo.GetWebsiteLinkByDmWebsiteID(hdct.DmWebsiteREF,hdct.TenWebsite) TenWebsite,
			dbo.[GetWebsiteLinkByDmWebsiteID_CPD](hdct.DmWebsiteREF,hdct.TenWebsite) TenWebsite,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			dm.soluongthucchay as SoLuongThucChay,
			--Thanh Tien Thuc Chay
			dm.Ngaythuchien AS NgayThucHien,
			0 as GiaTriThayDoi,
			ROUND(dm.ThanhTienThucChayTruocTrietKhau, 2) as ThanhTienThucChayTruocTrietKhau,
			ROUND(ISNULL((dm.ThanhTienThucChayTruocTrietKhau*hdct.ChietKhau)/100,0), 2) AS GiaTriTrietKhauThucChay,
			ROUND(ISNULL((dm.ThanhTienThucChayTruocTrietKhau - (dm.ThanhTienThucChayTruocTrietKhau*hdct.ChietKhau)/100),0), 2) AS ThanhTienSauTrietKhauThucChay,
			ROUND(ISNULL(((dm.ThanhTienThucChayTruocTrietKhau - (dm.ThanhTienThucChayTruocTrietKhau * hdct.ChietKhau)/100) * hdct.TiLeTuVan)/100,0), 2) AS GiaTriHoaHongThucChay,
			ROUND(ISNULL((dm.ThanhTienThucChayTruocTrietKhau - (dm.ThanhTienThucChayTruocTrietKhau * hdct.ChietKhau)/100 - ((dm.ThanhTienThucChayTruocTrietKhau - (dm.ThanhTienThucChayTruocTrietKhau * hdct.ChietKhau)/100) * hdct.TiLeTuVan)/100),0), 2) AS ThanhTienThucThu,
			(CASE when ((hdct.IsKhuyenMai=1) OR (hdct.ChietKhau = 100)) then ROUND(dm.ThanhTienThucChayTruocTrietKhau, 2)
				else 0
			  END
			) as ThanhTienKM,
			dm.soluongKM as SoLuongThucChayKM,
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
			GhiChu = IIF(@SoHopDong IS NULL, 
						 N'Tính mới: SP tối ưu [dbo].[ThucChay_CPDdotchay_PhatSinhThucchay_ThucChayDaTinh]',
						 N'Tính mới: SP tối ưu xử lý tay [dbo].[ThucChay_CPDdotchay_PhatSinhThucchay_ThucChayDaTinh]') 	
	FROM #Dmphanbo dm
	INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopdongchitietID
	INNER JOIN  
	( 
	 	SELECT * FROM ABM_Data_ThucChay.dbo.HopDong hd  WHERE hd.TrangThaiHopDong <> 3
		AND hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan
	) hd on hd.HopDongID = hdct.HopDongFK
	WHERE dm.soluongKM >0 OR dm.soluongthucchay > 0

COMMIT TRANSACTION;

END

```
