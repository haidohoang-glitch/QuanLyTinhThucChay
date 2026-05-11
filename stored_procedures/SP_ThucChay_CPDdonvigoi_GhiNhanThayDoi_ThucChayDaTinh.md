# Stored Procedure: `ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-15 15:16:14.637000
- **Ngày sửa cuối**: 2025-04-10 09:20:34.667000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhan` | `date(3)` | No |
| `@NgayCheckThayDoi` | `date(3)` | No |
| `@NgayDanhSo_GioiHan` | `date(3)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh] 
	@NgayGhiNhan DATE ,
	@NgayCheckThayDoi DATE = NULL,
	@NgayDanhSo_GioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN
BEGIN TRANSACTION

	CREATE TABLE #DmPhanbothaydoichitiet
	(      hopdongREF INT,
		   hopdongchitietID INT,
	       ngaythuchien DATETIME,
		   DotChayHopDong NVARCHAR(MAX),
		   SoLuongDotChayHD INT,
		   Nhanhang NVARCHAR(MAX),
		   Loaithaydoi NVARCHAR(100),
		   Pbxoa INT
	)	

	--================================================= 0. Xử lý TH chạy lại job =============================
	DELETE
	FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien) = @NgayGhiNhan
		AND DmSanPhamREF IN (140,228,564,549,5082) 
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 5 --Đơn vị gói của hình thức CPD 
		AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF IN (17,18))
		AND DotChayBooking = N'CPD_GOI'
		AND (GhiChu LIKE N'Tính lại%' OR GhiChu LIKE N'Đối trừ%')
		AND (@NgayDanhSo_GioiHan IS NULL OR NgayDanhSoHopDong >= @NgayDanhSo_GioiHan )
		AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
		AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)

	--================================================= 1. Xác định phân bổ có thay đổi thông tin ============
	INSERT INTO #DmPhanbothaydoichitiet
	(
	    hopdongREF,
	    hopdongchitietID,
	    ngaythuchien,
	    Loaithaydoi,
		Pbxoa 
	) 
	--TH1: thông tin đánh số
	SELECT DISTINCT tc.HopDongFK
	     , tc.HopDongChiTietID
		 , ngaythuchien = @NgayGhiNhan
		 , Loaithaydoi = IIF(@SoHopDong IS NULL, '', N'xử lý tay ') + IIF(TC.DeletedStatus = 1, N'phân bổ bị xóa', N'thay đổi thông tin hợp đồng')
		 , Pbxoa = IIF(TC.DeletedStatus = 1, 1, 0)
	FROM
		(
			SELECT hdct.HopDongChiTietID, hd.LastModifiedAt, hdct.ThanhTien, hdct.ChietKhau, hdct.DonGia, hdct.DeletedStatus, hdct.HopDongFK
			FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct
			INNER JOIN ABM_Data_ThucChay.dbo.HopDong hd on hdct.HopDongFk = hd.HopDongID
			WHERE 1=1
			AND  hdct.DmSanPhamREF in (140,228,564,549,5082)
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 5  
			AND hd.DeletedStatus = 0
			AND hdct.DmLoaiBannerREF NOT IN (17,18)
			AND hdct.DmLoaiREF <> 13  
			AND (CONVERT(DATE,hdct.LastModifiedAt)  = CONVERT(DATE,@NgayCheckThayDoi) OR CONVERT(DATE,hdct.LastModifiedAt)  = CONVERT(DATE,@NgayCheckThayDoi)) 
			AND (@NgayDanhSo_GioiHan IS NULL OR NgayDanhSoHopDong >= @NgayDanhSo_GioiHan )
			AND (@SoHopDong IS NULL OR hd.SoHopDong = @SoHopDong)
			AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)
		)TC
	OUTER APPLY
	   (SELECT  TOP 1 tcl.HopDongChiTietREF, tcl.ThanhTien, tcl.ChietKhau, tcl.DonGia
		FROM  ABM_Data_ThucChay.dbo.HopDongChiTietLog TCL WHERE TCL.HopDongChiTietREF = tc.HopDongChiTietID
		AND convert(date,TCL.LastModifiedAt) < convert(date,tc.LastModifiedAt)
		order by tcl.LastModifiedAt desc
		)TCL
	WHERE (((ISNULL(TC.ThanhTien,0) <> ISNULL(TCL.ThanhTien,0))) 
			OR ((ISNULL(TC.ChietKhau,0) <> ISNULL(TCL.ChietKhau,0)))
			OR ((ISNULL(TC.DonGia,0) <> ISNULL(TCL.DonGia,0)))
			OR ( tc.DeletedStatus = 1)
		)
		AND TCL.HopDongChiTietREF IS NOT NULL

	--DECLARE @Sophanbocantinh INT
	--SELECT @Sophanbocantinh = COUNT(DISTINCT hopdongchitietID)
	--FROM #DmPhanbothaydoichitiet
	--PRINT (N'So phan bo can tinh: ' + CONVERT(varchar(10),@Sophanbocantinh))

	--================================================= 2. tính thay đổi =====================================
	IF 1=1
	BEGIN
		-- 1. Thông tin đợt chạy đánh số
		--    GetDotChayBookingByHopDongChiTiet(HopDongChiTietID,'Y')
		UPDATE dm
		SET dm.DotChayHopDong = ISNULL(ttdc.thongtindotchaydanhso, 'N/A')
		FROM #DmPhanbothaydoichitiet dm
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
		WHERE Pbxoa = 0

		-- 2. Tổng số lượng đánh số của phân bổ 
		--    dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(hdct.SoLuong,hdct.DonViTinh,HopDongChiTietID)
		UPDATE dm
		SET dm.SoLuongDotChayHD = hdct.SoLuong
		FROM #DmPhanbothaydoichitiet dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.HopDongChiTietID
		WHERE Pbxoa = 0

		-- 3. Nhãn hàng
		----   TH 1 ngày phân bổ có thể chạy cho nhiều nhãn hàng
		--   [dbo].[f_ReturnListConcatNhanHangREF_v2](HopDongChiTietID, @NgayThucHien)
		--;WITH Temp AS (  SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.DmNhanHangREF
		--				FROM ThucChayHopDongChiTiet tchdct
		--				INNER JOIN #DmPhanbothaydoichitiet dm ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		--				WHERE tchdct.DeletedStatus = 0 AND
		--					  CONVERT(DATE, tchdct.ThoiGianBatDau)  <= CONVERT(DATE, dm.NgayThucHien) AND
		--					  CONVERT(DATE, tchdct.ThoiGianKetThuc) >= CONVERT(DATE, dm.NgayThucHien))
		--UPDATE dm
		--SET   dm.Nhanhang = tchdct.nhanhang
		--FROM #DmPhanbothaydoichitiet dm
		--INNER JOIN (
		--			SELECT t1.HopDongChiTietREF, 
		--				   STUFF((
		--					   SELECT DISTINCT ',' + CAST(t2.DmNhanHangREF AS VARCHAR(MAX))
		--					   FROM Temp AS t2
		--					   WHERE t2.HopDongChiTietREF = t1.HopDongChiTietREF
		--					   FOR XML PATH(''), TYPE
		--				   ).value('.', 'NVARCHAR(MAX)'), 1, 1, '') AS nhanhang
		--			FROM Temp  t1
		--			GROUP BY t1.HopDongChiTietREF ) tchdct ON tchdct.HopDongChiTietREF = dm.HopdongchitietID
		--WHERE Pbxoa = 0;

		--WITH Temp2 AS (  SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.DmNhanHangREF
		--				FROM ThucChayHopDongChiTiet tchdct
		--				INNER JOIN #DmPhanbothaydoichitiet dm ON dm.HopdongchitietID = tchdct.HopDongChiTietREF AND dm.Nhanhang IS NULL
		--				WHERE tchdct.DeletedStatus = 0)
		--UPDATE dm
		--SET   dm.Nhanhang = tchdct.nhanhang
		--FROM #DmPhanbothaydoichitiet dm
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
		--WHERE dm.Nhanhang IS NULL AND
		--      Pbxoa = 0
		-- TH phân bổ 1 ngày chỉ chạy cho 1 nhãn hàng 
		UPDATE dm
		SET dm.Nhanhang = tchdct.DmNhanHangREF 
		FROM #DmPhanbothaydoichitiet dm
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0 AND
			  CONVERT(DATE, tchdct.ThoiGianBatDau)  <= CONVERT(DATE, dm.NgayThucHien) AND
			  CONVERT(DATE, tchdct.ThoiGianKetThuc) >= CONVERT(DATE, dm.NgayThucHien) AND
			  CAST(tchdct.DmNhanHangREF AS INT) >0  AND
			  dm.Pbxoa = 0

		UPDATE dm
		SET dm.Nhanhang = tchdct.DmNhanHangREF 
		FROM #DmPhanbothaydoichitiet dm
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0 AND
			  dm.Nhanhang IS NULL AND
			  dm.Pbxoa = 0
	END

	--================================================= 3. thực hiện đối trừ =================================
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
		SELECT tcdt.*, 
			   N'Đối trừ: SP tối ưu [dbo].[ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh] đối trừ do ' + dmcheck.Loaithaydoi
		FROM (
				SELECT NEWID() AS [ThucChayDaTinhID]
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
				  ,[DotChayBooking] = N'CPD_GOI'
				  ,[SoLuongDotChayBooking]
				  ,[SoLuong]
				  ,tcdt.[DonViTinh]
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
				  ,0 AS [SoLuongThucChay]
				  ,@NgayGhiNhan AS [Ngaythuchien]
				  ,-SUM([ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) AS [GiaTriThayDoi]
				  ,0 AS [ThanhTienThucChayTruocTrietKhau]
				  ,0 AS [GiaTriTrietKhauThucChay]
				  ,0 AS [ThanhTienSauTrietKhauThucChay]
				  ,0 AS [GiaTriHoaHongThucChay]
				  ,0 AS [ThanhTienThucThu]
				  ,0 AS [ThanhTienKM]
				  ,0 AS [SoLuongThucChayKM]
				  ,0 AS [SoLuongThucChayLechTreoHa]
				  ,0 AS [ThanhTienLechTreoHa]
				  ,GETDATE() AS [CreatedAt]
				  ,GETDATE() AS [LastModifiedAt]
				  ,0 AS [IsPheDuyet]
				  ,'' AS [PheDuyetBy]
				  ,'' AS [PheDuyetAt]
				  ,-SUM(tcdt.[SoLuongThucChay] + tcdt.[SoLuongThayDoi]) AS [SoLuongThayDoi]
				  ,-SUM([SoLuongThucChayKM] + tcdt.[SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
				  ,-SUM([ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) AS [GiaTriKMThayDoi]
				 FROM ABM_Data_ThucChay.dbo.[ThucChayDaTinh] tcdt
				 WHERE  EXISTS (SELECT  hopdongchitietID 
								FROM #DmPhanbothaydoichitiet dmcheck 
								WHERE dmcheck.hopdongchitietID = tcdt.HopDongChiTietREF)
						AND tcdt.NgayThucHien <= @NgayGhiNhan
				 GROUP BY
				   [HopDongID]
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
				  ,[SoLuongDotChayBooking]
				  ,[SoLuong]
				  ,tcdt.[DonViTinh]
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
				  HAVING SUM([ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) <> 0
				  OR SUM([ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) <> 0
			) tcdt
		INNER JOIN #DmPhanbothaydoichitiet dmcheck ON dmcheck.hopdongchitietID = tcdt.HopDongChiTietREF


		UPDATE tc
		SET tc.RecordStatus = 0
		FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tc
		INNER JOIN #DmPhanbothaydoichitiet kq ON tc.HopDongChiTietREF = kq.HopDongChiTietID

		--================================================= 4. tính lại ==========================================
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
		SELECT  TCDT.ThucChayDaTinhID
				,TCDT.HopDongID, TCDT.SoHopDong, 
				TCDT.DmMaHopDongREF,TCDT.TenMaHopDong, 
				TCDT.NgayDanhSoHopDong, TCDT.NgayKyHopDong, 
				TCDT.NhanHopDong, TCDT.NgayNhanBanFax, TCDT.NgayNhanHopDongBanCung, TCDT.NgayChuyenHopDongChoKeToan, 
				TCDT.So, TCDT.Thang, TCDT.Nam, 
				TCDT.GiaTriHopDong, TCDT.CongNo,
				TCDT.HopDongChiTietID,
				--Thong tin ve trang thai
				TCDT.DangSuDung, TCDT.IsGiayPhep, TCDT.TrangThaiHopDong,TCDT.IsBanCung, 
				--Thong tin ve Nhan vien kinh doanh
				TCDT.DmPhongBanREF, TCDT.TenPhongBan, 
				TCDT.DmBoPhanREF, TCDT.TenBoPhan, 
				TCDT.DmNhomLamViecREF,	TCDT.TenNhom, 
				TCDT.DmDiaDiemLamViecREF,	TCDT.TenDiaDiemLamViec, 
				TCDT.SysNhanVienREF, TCDT.TenDangNhap,  
				TCDT.TenNhanVien, 
				TCDT.TenKhachHang, 
				TCDT.NhanHang,
				TCDT.DmNhomNganhREF,TCDT.TenNhomNganh, 
				--Thong tin hinh thuc quang cao
				TCDT.DmHinhThucQuangCao, TCDT.TenHinhThucQuangCao, 
				--Thong tin San pham
				TCDT.DmSanPhamREF as DmSanPhamREF,	TCDT.TenSanPham,  
				TCDT.DmNhomWebsiteREF, TCDT.TenNhomWebsite, 
				TCDT.DmChuyenMucREF, TCDT.TenChuyenMuc,
				TCDT.DmLoaiBannerREF, TCDT.TenLoaiBanner, 
				TCDT.DmViTriREF, TCDT.TenViTri, 
				--Thong tin ve Tien
				TCDT.DotChayHopDong,
				TCDT.SoLuongDotChayHD,
				--Thong tin dot chay cua thuc treo ( vi tinh thuc chay theo dot chay va thuc treo hd)	
				TCDT.DotChayBooking,
				TCDT.SoLuongDotChayBooking,
				TCDT.SoLuong, 
				TCDT.DonViTinh,
				TCDT.DonGia, 
				TCDT.DonGiaTheoDonViTinh,
				TCDT.ChietKhau, TCDT.GiamGia, TCDT.ThanhTien,
				TCDT.TiLeTuVan,  TCDT.ChiPhiTuVan,
				TCDT.IsKhuyenMai,  
				TCDT.KhuyenMai,
				--Thuc chay
				TCDT.DmBannerREF,--A.DmBannerREF,
				TCDT.DmChienDichREF,--A.DmChienDichREF,
				TCDT.DmWebsiteREF,
				TCDT.TenWebsite,
				TCDT.TongViewThucChay,
				TCDT.TongClickThucChay,
				TCDT.TongSoBaiViet,
				0 SoLuongThucChay,
				--Thanh Tien Thuc Chay
				TCDT.NgayThucHien,
				TCDT.ThanhTienSauTrietKhauThucChay GiaTriThayDoi,
				ThanhTienThucChayTruocTrietKhau,
				ThanhTienThucChayTruocTrietKhau - ThanhTienThucChayTruocTrietKhau*TCDT.ChietKhau/100 as GiaTriTrietKhauThucChay,
				0 ThanhTienSauTrietKhauThucChay,
				0 GiaTriHoaHongThucChay,
				0 ThanhTienThucThu,
				0 ThanhTienKM,
				0 SoLuongThucChayKM,
				0 SoLuongThucChayLechTreoHa,
				0 ThanhTienLechTreoHa,
				TCDT.CreatedAt,
				TCDT.LastModifiedAt,
				TCDT.IsPheDuyet,
				TCDT.PheDuyetBy,
				TCDT.PheDuyetAt,
				TCDT.SoLuongThucChay AS SoLuongThayDoi,
				TCDT.SoLuongThucChayKM AS SoLuongKMThayDoi,
				TCDT.ThanhTienKM AS GiaTriKMThayDoi,
				TCDT.GhiChu	
		FROM (
				SELECT  NEWID() ThucChayDaTinhID, TD.*, 
						ROUND(ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0), 2) AS GiaTriTrietKhauThucChay,
						ROUND(ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0), 2) AS ThanhTienSauTrietKhauThucChay,
						ROUND(ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0), 2) AS GiaTriHoaHongThucChay,
						ROUND(ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0), 2) AS ThanhTienThucThu,
						(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then ROUND(TD.ThanhTienThucChayTruocTrietKhau, 2)
							else 0
							END
						) as ThanhTienKM,
						(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then ISNULL(TD.SoLuong,0)
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
						0 GiaTriKMThayDoi
				FROM (
						SELECT  --ID Hop Dong
								D.HopDongID, D.SoHopDong, 
								D.DmMaHopDongREF,D.TenMaHopDong, 
								--Thong tin ve thoi gian
								D.NgayDanhSoHopDong, D.NgayKyHopDong, 
								D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
								D.So, D.Thang, D.Nam, 
								--Thong tin ve gia tri
								D.GiaTriHopDong, D.CongNo,
								--Thong tin chi tiet phan bo
								C.HopDongChiTietID,
								--Thong tin ve trang thai
								D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
								--Thong tin ve Nhan vien kinh doanh
								D.DmPhongBanREF, ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
								D.DmBoPhanREF, ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
								D.DmNhomLamViecREF,	ISNULL(D.TenNhom, '') AS TenNhom, 
								D.DmDiaDiemLamViecREF,	D.TenDiaDiemLamViec, 
								D.SysNhanVienREF, ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
								D.TenNhanVien, 
								D.TenKhachHang, 
								--C.NhanHang, 
								C.Nhanhangtreo NhanHang,
								C.DmNhomNganhREF,C.TenNhomNganh, 
								--Thong tin hinh thuc quang cao
								C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
								--Thong tin San pham
								c.DmSanPhamREF as DmSanPhamREF,	C.TenSanPham,  
								C.DmNhomWebsiteREF, C.TenNhomWebsite, 
								C.DmChuyenMucREF, C.TenChuyenMuc,
								C.DmLoaiBannerREF, C.TenLoaiBanner, 
								C.DmViTriREF, C.TenViTri, 
								--Thong tin ve Tien
								CAST(C.DotChayHopDong AS VARCHAR(1000)) DotChayHopDong,
								C.SoLuongDotChayHD AS SoLuongDotChayHD,
								--Thong tin dot chay cua thuc treo ( vi tinh thuc chay theo dot chay va thuc treo hd)	
								N'CPD_GOI' DotChayBooking,
								0 SoLuongDotChayBooking,
								C.SoLuong AS SoLuong, 
								dbo.FormatDonViTinh(C.DonViTinh) DonViTinh,
								C.DonGia as DonGia, 
								C.DonGia AS DonGiaTheoDonViTinh,
								C.ChietKhau, C.GiamGia, C.ThanhTien,
								C.TiLeTuVan,  C.ChiPhiTuVan,
								C.IsKhuyenMai,  
								C.KhuyenMai,
								--Thuc chay
								0 DmBannerREF,--A.DmBannerREF,
								0 DmChienDichREF,--A.DmChienDichREF,
								dbo.[GetDmWebsiteReportingdbIDByDmWebsiteID_CPD](C.DmWebsiteREF) DmWebsiteREF,
								dbo.[GetWebsiteLinkByDmWebsiteID_CPD](C.DmWebsiteREF,C.TenWebsite) TenWebsite,
								0 TongViewThucChay,
								0 TongClickThucChay,
								0 TongSoBaiViet,
								(CASE when (C.ChietKhau = 100) then 0
									else ISNULL(C.SoLuong,0)
									END
								) as SoLuongThucChay,
								--Thanh Tien Thuc Chay
								@NgayGhiNhan AS NgayThucHien,
								0 as GiaTriThayDoi,
								ROUND(C.SoLuong*C.DonGia, 2) as ThanhTienThucChayTruocTrietKhau,
								C.lydo AS Ghichu
						FROM (  SELECT DISTINCT  hdct.* , lydo = N'Tính lại: SP tối ưu [dbo].[ThucChay_CPDdonvigoi_GhiNhanThayDoi_ThucChayDaTinh] tính lại do ' + dmcheck.Loaithaydoi, 
												 dmcheck.DotChayHopDong, dmcheck.SoLuongDotChayHD, dmcheck.Nhanhang AS Nhanhangtreo
								FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
								INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tc ON hdct.HopDongChiTietID = tc.HopDongChiTietREF
								INNER JOIN #DmPhanbothaydoichitiet dmcheck ON hdct.HopDongChiTietID = dmcheck.hopdongchitietID
								WHERE hdct.DmSanPhamREF in (140,228,564,549,5082)
									AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 5 --Đơn vị gói của hình thức CPD 
									AND hdct.DeletedStatus = 0
									AND tc.DeletedStatus = 0
									AND hdct.DmLoaiBannerREF NOT IN (17,18)
									AND hdct.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
									AND tc.RecordStatus = 0
									AND dmcheck.Pbxoa = 0
							) C  
						INNER JOIN  ( 
								SELECT * FROM ABM_Data_ThucChay.dbo.HopDong hd  WHERE hd.TrangThaiHopDong <> 3
									) D on D.HopDongID = C.HopDongFK
					) TD
			) TCDT
		WHERE TCDT.SoLuongThucChay >0 OR TCDT.SoLuongThucChayKM >0 

		UPDATE tc
		SET tc.RecordStatus = 1
		FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tc
		INNER JOIN #DmPhanbothaydoichitiet kq ON tc.HopDongChiTietREF = kq.HopDongChiTietID
	END

	DROP TABLE #DmPhanbothaydoichitiet

COMMIT TRANSACTION;

END

```
