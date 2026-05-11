# Stored Procedure: `ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-15 15:18:46.113000
- **Ngày sửa cuối**: 2025-04-11 09:55:00.323000

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
-- Created by:	DWH\haidh
-- Optimized date: 20-09-2024 by DWH\trangtth
-- Description:	tính thay đổi thực chạy sản phẩm CPD không đợt chạy
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh] 
	@NgayGhiNhan DATE,
	@NgayCheckThayDoi DATE = NULL ,
	@NgayDanhSo_GioiHan DATE = NULL,
	@SoHopDong NVARCHAR(50) = NULL,
	@HopDongChiTietID INT = NULL
AS
BEGIN
BEGIN TRANSACTION

	CREATE TABLE #DmPhanbothaydoi
	(      hopdongREF INT,
		   hopdongchitietID INT,
	       ngaythuchien DATETIME,
		   Loaithaydoi NVARCHAR(50),
		   Mathaydoi INT
		   --1: thay đổi thông tin  đánh số
		   --2: thay đổi thông tin treo
		   --3: phân bổ bị xóa
	)

	CREATE TABLE #DmPhanbothaydoichitiet
	(      hopdongREF INT,
		   hopdongchitietID INT,
	       ngaythuchien DATETIME,
		   dongiatheodonvitinh FLOAT,  -- đơn giá chuẩn theo đơn vị tính
		   soluongHT INT,  -- số lượng đánh số chuẩn theo đơn vị tính
		   SoLuongDotChayBooking INT, --số lượng thực treo của phân bổ
		   SoLuongThucChayHT FLOAT,  -- số lượng thực chạy tính đến hiện tại
		   SoLuongThucChay FLOAT, -- số lượng thực chạy đã tính
		   TongGiaTriThucChayDaTinhHT FLOAT,
		   TongGiaTriThucChayDaTinh FLOAT,
		   GiatriKMHT FLOAT,
		   GiatriKMDatinh FLOAT,
		   SoluongKMHT FLOAT,
		   SoluongKMDatinh FLOAT,
		   Giatrithaydoi FLOAT,
		   GiatriKMthaydoi FLOAT,
		   Soluongthaydoi FLOAT,
		   SoluongKMthaydoi FLOAT,
		   Loaithaydoi NVARCHAR(100) ,
		   pbxoa INT,
		   nhanhang NVARCHAR(MAX), 
		   DotChayBooking NVARCHAR(MAX),
		   DonGia FLOAT
	)

	--================================================= 0. Xử lý TH chạy lại job =============================
	DELETE FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien) = @NgayGhiNhan
	AND DotChayHopDong = 'CPD_KhongDotChay'
	AND (GhiChu LIKE N'Tính lại%' OR GhiChu LIKE N'Đối trừ%')
	AND (@SoHopDong IS NULL OR SoHopDong = @SoHopDong)
	AND (@HopDongChiTietID IS NULL OR HopDongChiTietREF = @HopDongChiTietID)


	--================================================= 1. Xác định phân bổ có thay đổi thông tin ============
	BEGIN
		INSERT INTO #DmPhanbothaydoi
		(
			hopdongREF,
			hopdongchitietID,
			ngaythuchien,
			Loaithaydoi,
			Mathaydoi
		)
		--TH1: thông tin đánh số
		SELECT DISTINCT
			   hd.HopDongID, 
			   hdct.HopDongChiTietID, 
			   ngaythuchien = @NgayGhiNhan,
			   Loaithaydoi = N'thông tin hợp đồng', 
			   Mathaydoi = 1
		FROM ABM_Data_ThucChay.dbo.HopDong hd
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE	hd.TrangThaiHopDong <> 3
				AND hdct.DmLoaiREF <> 13 
				AND hdct.DmSanPhamREF IN (140,228,564,549)
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1	  
				--AND [dbo].[ThucChay_CheckSanPhamCPDKhongDotChay](hdct.HopDongChiTietID, @NgayCheckThayDoi) = 1
				AND (@NgayDanhSo_GioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan)
				AND (Convert(date,hd.LastModifiedAt) = @NgayCheckThayDoi OR Convert(date,hdct.LastModifiedAt) = @NgayCheckThayDoi)
				AND @SoHopDong IS NULL
	
		--TH2: thực treo thay đổi
		UNION
		SELECT DISTINCT A.HopDongREF, 
						A.HopDongChiTietREF, 
						ngaythuchien = @NgayGhiNhan,
						Loaithaydoi = N'thông tin thực treo', 
						Mathaydoi = 2
		FROM(
				   SELECT tchdctp.HopDongREF,
						  hd.SoHopDong,
						  tchdctp.HopDongChiTietREF,
						  hdct.SoLuong,
						  hdct.ThanhTien,
						  tchdctp.ThoiGianBatDau,
						  tchdctp.ThoiGianKetThuc,
						  (   CASE 
								   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN tchdctp.CreatedAt
								   ELSE tchdctp.LastModifiedAt
							  END
						  ) NgayThucHien
				   FROM ABM_Data_ThucChay.dbo.HopDong hd INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
				   INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdctp ON hdct.HopDongChiTietID = tchdctp.HopDongChiTietREF
				   WHERE  tchdctp.ThoiGianBatDau IS NOT NULL
						  AND (   CASE 
									   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
									   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
								  END
							  ) = @NgayCheckThayDoi
						  AND hdct.DmSanPhamREF IN (140,228,564,549)
						  AND hdct.DeletedStatus = 0
						  AND hd.DeletedStatus = 0
						  AND tchdctp.DeletedStatus = 0
						  AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1	 --Đơn vị của hình thức CPD 
						  --AND [dbo].[ThucChay_CheckSanPhamCPDKhongDotChay](hdct.HopDongChiTietID, @NgayCheckThayDoi) = 1
						  AND (@NgayDanhSo_GioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan)
						  AND @SoHopDong IS NULL
				)A

		--TH4: xử lý tay
		UNION
		SELECT DISTINCT
			   hd.HopDongID, 
			   hdct.HopDongChiTietID, 
			   ngaythuchien = @NgayGhiNhan,
			   Loaithaydoi = N'xử lý tay hợp đồng/ phân bổ', 
			   Mathaydoi = 1
		FROM ABM_Data_ThucChay.dbo.HopDong hd
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE	hd.TrangThaiHopDong <> 3
				AND hdct.DmLoaiREF <> 13 
				AND hdct.DmSanPhamREF IN (140,228,564,549)
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1	  
				--AND [dbo].[ThucChay_CheckSanPhamCPDKhongDotChay](hdct.HopDongChiTietID, @NgayGhiNhan) = 1
				AND (@NgayDanhSo_GioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan)
				AND hd.SoHopDong = @SoHopDong
				AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)

		--TH3: phân bổ bị xóa
		UPDATE dmcheck
		SET dmcheck.Loaithaydoi = N'phân bổ bị xóa',
			mathaydoi = 3
		FROM #DmPhanbothaydoi dmcheck
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dmcheck.hopdongchitietID AND ISNULL(hdct.DeletedStatus , 0) = 1

		DELETE 
		FROM #DmPhanbothaydoi
		WHERE [dbo].[ThucChay_CheckSanPhamCPDKhongDotChay](HopDongChiTietID, @NgayGhiNhan) <> 1

		--DECLARE @Sophanbothaydoi INT
		--SELECT @Sophanbothaydoi = COUNT(DISTINCT hopdongchitietID)
		--FROM #DmPhanbothaydoi
		--PRINT (N'So phan bo thay doi: ' + CONVERT(varchar(10),@Sophanbothaydoi))

		INSERT INTO #DmPhanbothaydoichitiet
		(
			hopdongREF,
			hopdongchitietID,
			ngaythuchien,
			Loaithaydoi,
			pbxoa
		)
		SELECT   hopdongREF,
				 hopdongchitietID,
				 ngaythuchien,
				 N'thay đổi ' +
				 STUFF((
						SELECT ' - ' + CAST(Loaithaydoi AS NVARCHAR(100))
						FROM #DmPhanbothaydoi t2
						WHERE t2.hopdongchitietID = t1.hopdongchitietID 
						FOR XML PATH(''), TYPE
					   ).value('.', 'NVARCHAR(MAX)'), 1, 3, '') AS Loaithaydoi,
				pbxoa = 0
		FROM #DmPhanbothaydoi t1
		WHERE t1.Mathaydoi <> 3
		GROUP BY hopdongREF,
				 ngaythuchien, 
				 hopdongchitietID
		UNION
		SELECT DISTINCT
			   hopdongREF,
			   hopdongchitietID, 
			   ngaythuchien, 
			   Loaithaydoi ,
			   pbxoa = 1
		FROM  #DmPhanbothaydoi 
		WHERE Mathaydoi = 3
	END

	--================================================= 2. tính thay đổi =====================================
	BEGIN
		--1. Xác định thông tin đánh số, đơn giá, số lượng chuẩn theo đơn vị tính ở hiện tại
		--   [GetSoLuongDotChayThucTreoByHopDongChiTiet](hopdongchitietID)
		UPDATE dm 
		SET dm.SoLuongDotChayBooking = ISNULL(tchdct.songaytreo, 0)
		FROM #DmPhanbothaydoichitiet dm
		LEFT JOIN (SELECT HopDongChiTietREF, ISNULL(SUM(DATEDIFF(day, ThoiGianBatDau, ThoiGianKetThuc) + 1),0) AS songaytreo
					FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet
					WHERE  DeletedStatus = 0
					GROUP BY HopDongChiTietREF) tchdct ON tchdct.HopDongChiTietREF = dm.HopDongChiTietID

		--   dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_CPDKhongDotChay(hdct.SoLuong,hdct.DonViTinh,hdct.DonGia,hd.ngaykyhopdong,@ngaythuchien,hopdongchitietID)
		UPDATE dm
		SET dm.dongiatheodonvitinh = IIF(dm.SoLuongDotChayBooking = 0, 0, (hdct.SoLuong*hdct.DonGia)/dm.SoLuongDotChayBooking)
		FROM #DmPhanbothaydoichitiet dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.hopdongchitietID
		WHERE dm.pbxoa = 0

		--2. Xác định số lượng, giá trị thực chạy tính đến hiện tại
		--   ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay(hdct.soluong, hdct.donvitinh, hopdongchitietID, @ngaythuchien)
		UPDATE dmcheck
		SET dmcheck.SoLuongThucChayHT = soluong.Soluong
		FROM #DmPhanbothaydoichitiet dmcheck
		INNER JOIN (SELECT HopDongChiTietREF, ISNULL(sum(DATEDIFF(day, 
																  ThoiGianBatDau, 
																  IIF(convert(date,ThoiGianKetThuc) > @NgayGhiNhan, 
																	  @NgayGhiNhan, 
																	  ThoiGianKetThuc) + 1)),0) AS Soluong
					FROM (SELECT DISTINCT HopDongChiTietREF, BookingREF, ThoiGianBatDau, ThoiGianKetThuc 
						  FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet 
						  WHERE  DeletedStatus = 0 AND 
								 CONVERT(date,ThoiGianBatDau) <= @NgayGhiNhan) tchdct
					GROUP BY HopDongChiTietREF
					) soluong ON soluong.HopDongChiTietREF = dmcheck.hopdongchitietID
		WHERE dmcheck.pbxoa = 0

		UPDATE dmcheck
		SET dmcheck.TongGiaTriThucChayDaTinhHT = SoLuongThucChayHT*((dongiatheodonvitinh*(100-hdct.ChietKhau))/100),
			dmcheck.SoluongKMHT = IIF(hdct.ChietKhau = 100, SoLuongThucChayHT, 0),
			dmcheck.GiatriKMHT = IIF(hdct.ChietKhau = 100, SoLuongThucChayHT*dongiatheodonvitinh, 0),
			dmcheck.SoLuongThucChayHT = IIF(hdct.ChietKhau = 100, 0, SoLuongThucChayHT)
		FROM #DmPhanbothaydoichitiet dmcheck
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dmcheck.hopdongchitietID
		WHERE dmcheck.pbxoa = 0

		--3. Xác định số lượng, giá trị thực chạy đã tính
		UPDATE dmcheck
		SET dmcheck.SoLuongThucChay = tcdt.SoLuongThucChay,
			dmcheck.TongGiaTriThucChayDaTinh = tcdt.TongGiaTriThucChayDaTinh,
			dmcheck.SoluongKMDatinh = tcdt.SoluongKMDatinh,
			dmcheck.GiatriKMDatinh = tcdt.GiatriKMDatinh
		FROM #DmPhanbothaydoichitiet dmcheck
		OUTER APPLY
				   ( SELECT   SoLuongThucChay = SUM(ISNULL(tcdt.SoLuongThucChay,0)) + SUM(ISNULL(tcdt.SoLuongThayDoi,0))
							, TongGiaTriThucChayDaTinh =  SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)) +	SUM(ISNULL(tcdt.GiaTriThayDoi,0))
							, SoluongKMDatinh = SUM(ISNULL(tcdt.SoLuongThucChayKM,0)) + SUM(ISNULL(tcdt.SoLuongKMThayDoi,0))
							, GiatriKMDatinh = SUM(ISNULL(tcdt.ThanhTienKM,0)) +	SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))
					 FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh tcdt 
					 WHERE tcdt.HopDongChiTietREF = dmcheck.hopdongchitietID AND
						   tcdt.NgayThucHien <= dmcheck.ngaythuchien
					) tcdt

		--4. Xác định số lượng, giá trị thay đổi
		UPDATE dmcheck
		SET GiaTriThayDoi = ISNULL(TongGiaTriThucChayDaTinhHT, 0) - ISNULL(TongGiaTriThucChayDaTinh, 0),
			GiatriKMThaydoi =  ISNULL(GiatriKMHT, 0) - ISNULL(GiatriKMDatinh, 0),
			Soluongthaydoi = ISNULL(SoLuongThucChayHT, 0) - ISNULL(SoLuongThucChay, 0),
			SoluongKMThaydoi = ISNULL(SoluongKMHT, 0) - ISNULL(SoluongKMDatinh, 0)
		FROM  #DmPhanbothaydoichitiet dmcheck

		DELETE
		FROM #DmPhanbothaydoichitiet
		WHERE ROUND(GiaTriThayDoi, 0) = 0 AND 
			  ROUND(GiaTriKMThayDoi, 0) = 0 AND 
			  Soluongthaydoi = 0 AND 
			  SoluongKMthaydoi = 0 

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
		--WHERE dm.pbxoa = 0;

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
		--WHERE dm.Nhanhang IS NULL AND dm.pbxoa = 0

		-- TH phân bổ 1 ngày chỉ chạy cho 1 nhãn hàng 
		UPDATE dm
		SET dm.Nhanhang = CAST(tchdct.DmNhanHangREF AS INT)
		FROM #DmPhanbothaydoichitiet dm
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0 AND
			  CONVERT(DATE, tchdct.ThoiGianBatDau)  <= CONVERT(DATE, dm.NgayThucHien) AND
			  CONVERT(DATE, tchdct.ThoiGianKetThuc) >= CONVERT(DATE, dm.NgayThucHien) AND
			  CAST(tchdct.DmNhanHangREF AS INT) >0 AND
			  dm.pbxoa = 0

		UPDATE dm
		SET dm.Nhanhang = CAST(tchdct.DmNhanHangREF AS INT)
		FROM #DmPhanbothaydoichitiet dm
		INNER JOIN ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct ON dm.HopdongchitietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0 AND
			  dm.Nhanhang IS NULL AND
			  dm.pbxoa = 0

		-- 4. Thông tin đợt chạy thực treo của phân bổ
		--    dbo.GetDotChayThucTreoByHopDongChiTiet(HopDongChiTietID,'Y')
		UPDATE dm
		SET dm.DotChayBooking = ISNULL(ttdc.thongtindotchaydanhso, 'N/A')
		FROM #DmPhanbothaydoichitiet dm
		LEFT JOIN (	SELECT	hdct.HopDongChiTietID,
							STUFF((	SELECT (Convert(NVARCHAR(50),tchdct.BookingREF) + ' : ' 
												+ convert(NVARCHAR(10),tchdct.ThoiGianBatDau,101) + ' - ' 
												+ Convert(NVARCHAR(10), tchdct.ThoiGianKetThuc,101)) + CAST(';' AS VARCHAR(max)) 
									FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct 
									WHERE tchdct.DeletedStatus = 0
									ORDER BY tchdct.BookingREF
									FOR XML PATH('')
								),1,0,'') AS thongtindotchaydanhso
					FROM ABM_Data_ThucChay.dbo.hopdongchitiet hdct  
					WHERE hdct.DeletedStatus = 0 
					GROUP BY hdct.HopDongChiTietID
										) ttdc ON dm.HopDongChiTietID = ttdc.HopDongChiTietID 
		WHERE pbxoa = 0

		--5. Thông tin đơn giá đánh số của phân bổ
		--   [dbo].[ThucChay_GetDonGiaByNgayThucHien](@Ngaythuchien, HopdongchitietID, hdct.dongia)
		UPDATE dm
		SET dm.DonGia = hdct.DonGia
		FROM #DmPhanbothaydoichitiet dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.hopdongchitietID
		WHERE pbxoa = 0

		--DECLARE @Sophanbocantinh INT
		--SELECT @Sophanbocantinh = COUNT(DISTINCT hopdongchitietID)
		--FROM #DmPhanbothaydoichitiet
		--PRINT (N'So phan bo can tinh: ' + CONVERT(varchar(10),@Sophanbocantinh))
	END

	--==================================================3. Đối trừ ================================================
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
           ,[GhiChu]
           ,[NgayThucHien])
	SELECT tcdt.*, 
		   N'Đối trừ: SP tối ưu [dbo].[ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh] đối trừ do ' + dmcheck.Loaithaydoi, 
		   @NgayGhiNhan
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
				  ,[DotChayHopDong] = 'CPD_KhongDotChay'
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
				  ,0 AS [SoLuongThucChay]
				  ,-SUM([ThanhTienSauTrietKhauThucChay] + [GiaTriThayDoi]) AS [GiaTriThayDoi]
				  ,-SUM([ThanhTienThucChayTruocTrietKhau]) AS [ThanhTienThucChayTruocTrietKhau]
				  ,-SUM([GiaTriTrietKhauThucChay]) AS [GiaTriTrietKhauThucChay]
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
			  HAVING SUM([ThanhTienSauTrietKhauThucChay] + [GiaTriThayDoi]) <> 0
			  OR SUM([ThanhTienKM] + [GiaTriKMThayDoi]) <> 0 
		) tcdt
	INNER JOIN #DmPhanbothaydoichitiet dmcheck ON dmcheck.hopdongchitietID = tcdt.HopDongChiTietREF


	--========================================================4. Tính lại==================================
	INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
	SELECT  NEWID(), TD.* 
	FROM 
	(	SELECT 
			--ID Hop Dong
			D.HopDongID,
			--Thong tin ve ma so 
			D.SoHopDong, 
			D.DmMaHopDongREF, 
			D.TenMaHopDong, 
			--Thong tin ve thoi gian
			D.NgayDanhSoHopDong, D.NgayKyHopDong, 
			ISNULL(D.NhanHopDong,'') AS NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
			D.So, D.Thang, D.Nam, 
			--Thong tin ve gia tri
			D.GiaTriHopDong, D.CongNo,
			--Thong tin chi tiet phan bo
			C.HopDongChiTietID,
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
			dmcheck.nhanhang NhanHang,
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			c.DmSanPhamREF as DmSanPhamREF,
			E.TenSanPham,  
			C.DmNhomWebsiteREF, 
			C.TenNhomWebsite, 
			--C.DmWebsiteREF, 
			--C.TenWebsite, 
			C.DmChuyenMucREF, 
			C.TenChuyenMuc,
			C.DmLoaiBannerREF, 
			C.TenLoaiBanner, 
			C.DmViTriREF, 
			C.TenViTri, 
			'CPD_KhongDotChay' DotChayHopDong,
			0 AS SoLuongDotChayHD,
			CAST(dmcheck.DotChayBooking AS VARCHAR(1000)) DotChayBooking,
			dmcheck.SoLuongDotChayBooking SoLuongDotChayBooking,
			--Thong tin ve Tien
			C.SoLuong AS SoLuong, 
			dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
			ROUND(dmcheck.DonGia, 2) as DonGia, 
			ROUND(dmcheck.dongiatheodonvitinh, 2) AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			--dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
			dbo.[GetDmWebsiteReportingdbIDByDmWebsiteID_CPD](C.DmWebsiteREF) DmWebsiteREF,
			--dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			dbo.[GetWebsiteLinkByDmWebsiteID_CPD](C.DmWebsiteREF,C.TenWebsite) TenWebsite,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			0 SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			dmcheck.NgayThucHien AS NgayThucHien,
			ROUND(dmcheck.TongGiaTriThucChayDaTinhHT, 2) as GiaTriThayDoi,
			Case when C.ChietKhau = 100 
					then ROUND(dmcheck.GiatriKMHT, 2)
					when isnull(C.ChietKhau, 0) <> 100 
					then ROUND(dmcheck.TongGiaTriThucChayDaTinhHT/(1-isnull(C.ChietKhau, 0)/100), 2)
			end as ThanhTienThucChayTruocTrietKhau,
			Case when C.ChietKhau = 100 
					then ROUND(dmcheck.GiatriKMHT - dmcheck.GiatriKMHT*C.ChietKhau/100, 2)
					when isnull(C.ChietKhau, 0) <> 100 
					then ROUND((dmcheck.TongGiaTriThucChayDaTinhHT/(1-isnull(C.ChietKhau, 0)/100))*(1-C.ChietKhau/100), 2)
			end as GiaTriTrietKhauThucChay,
			0 AS ThanhTienSauTrietKhauThucChay,
			0 AS GiaTriHoaHongThucChay,
			0 AS ThanhTienThucThu,
			0 as ThanhTienKM,
			0 as SoLuongThucChayKM,
			0 SoLuongLechTreoHa,
			0 ThanhTienLechTreoHa,
			GETDATE() AS [CreatedAt],
			GETDATE() AS [LastModifiedAt],
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			dmcheck.SoLuongThucChayHT  SoLuongThayDoi,
			dmcheck.SoluongKMHT	 SoLuongKMThayDoi,
			ROUND(dmcheck.GiatriKMHT, 0)  GiaTriKMThayDoi,
			N'Tính lại: SP tối ưu [dbo].[ThucChay_CPDkhongdotchay_GhiNhanThayDoi_ThucChayDaTinh] tính lại do ' + dmcheck.Loaithaydoi AS GhiChu 
		FROM #DmPhanbothaydoichitiet dmcheck
		INNER JOIN 
		(
			SELECT * FROM ABM_Data_ThucChay.dbo.HopDongChiTiet 
			WHERE DmSanPhamREF in (140,228,564,549)
						AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 1 --Đơn vị của hình thức CPD 
		) C  ON C.HopDongChiTietID = dmcheck.hopdongchitietID 
		INNER JOIN  
			( 
	 		SELECT * FROM ABM_Data_ThucChay.dbo.HopDong hd 
			WHERE hd.TrangThaiHopDong != 3
			) D on D.HopDongID = C.HopDongFK
		INNER JOIN ABM_Data_ThucChay.dbo.DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
		WHERE dmcheck.pbxoa = 0
	) TD

	DROP TABLE #DmPhanbothaydoichitiet
	DROP TABLE #DmPhanbothaydoi

COMMIT TRANSACTION;

END



```
