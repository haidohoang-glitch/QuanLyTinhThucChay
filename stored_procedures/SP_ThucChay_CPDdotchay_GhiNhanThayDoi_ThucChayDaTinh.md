# Stored Procedure: `ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-15 15:18:15.903000
- **Ngày sửa cuối**: 2025-09-18 10:18:52.773000

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
-- Description:	tính thay đổi thực chạy sản phẩm CPD đợt chạy
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh] 
	@NgayGhiNhan DATE,
	@NgayCheckThayDoi DATE = NULL,
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
		   --1: thay đổi thông tin thành tiền đánh số
		   --2: thay đổi thông tin đợt chạy đánh số
		   --3: thay đổi thông tin treo
		   --4: phân bổ bị xóa
	)

	CREATE TABLE #DmPhanbothaydoichitiet
	(      hopdongREF INT,
		   hopdongchitietID INT,
	       ngaythuchien DATETIME,
		   dongiatheodonvitinh FLOAT,  -- đơn giá chuẩn theo đơn vị tính
		   SoLuongDotChayHD INT,  -- số lượng đánh số chuẩn theo đơn vị tính
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
		   Loaithaydoi NVARCHAR(100),
		   pbxoa INT,
		   Nhanhang NVARCHAR(MAX),
		   DotChayHopDong NVARCHAR(MAX),
		   DotChayBooking NVARCHAR(MAX),
		   dongia FLOAT
	)

	--================================================= 0. Xử lý TH chạy lại job =============================
	DELETE FROM ABM_Data_ThucChay.dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien) = @NgayGhiNhan
	AND DmSanPhamREF IN (140,228,564,549,5082) 
	AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1 --Đơn vị của hình thức CPD 
	AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF IN (17,18))
	AND (DotChayBooking <> N'CPD_GOI' or DotChayHopDong <> 'CPD_KhongDotChay')
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
		--TH1. thông tin đánh số
		SELECT DISTINCT hd.HopDongID, hdct.HopDongChiTietID, ngaythuchien = @NgayGhiNhan, Loaithaydoi = N'thông tin hợp đồng', Mathaydoi = 1
		FROM ABM_Data_ThucChay.dbo.HopDong hd
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.TrangThaiHopDong <> 3
			  AND hdct.DmSanPhamREF IN (140,228,241,564,549,5082)
			  AND hdct.DmLoaiREF <> 13 
		      AND  Upper((RTrim(LTrim(hdct.DonViTinh)))) IN (N'NGÀY' , N'TUẦN' , N'THÁNG' , N'NĂM' )
			  AND exists (select top 1 dc.HopDongChiTietREF from ABM_Data_ThucChay.dbo.DotChayHopDongchitiet dc WHERE dc.HopDongChiTietREF = hdct.HopDongChiTietID)--check co dot chay 02/12/2022

			  AND (@NgayDanhSo_GioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan)
			  AND (Convert(date,hd.LastModifiedAt) = @NgayCheckThayDoi OR Convert(date,hdct.LastModifiedAt) = @NgayCheckThayDoi)

			  AND @SoHopDong IS NULL

		UNION
		--TH2. thay đổi thông tin đợt chạy đánh số
		SELECT DISTINCT hd.HopDongID, dchdct.HopDongChiTietREF, ngaythuchien = @NgayGhiNhan, Loaithaydoi = N'thông tin đợt chạy đánh số', Mathaydoi = 2
		FROM ABM_Data_ThucChay.dbo.HopDong hd
		INNER JOIN (SELECT * FROM ABM_Data_ThucChay.dbo.HopDongChiTiet hdct 
					WHERE  hdct.DmSanPhamREF IN (140,228,564,549,5082)
						   AND hdct.DeletedStatus = 0
						   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 1
					)hdct ON hdct.HopDongFK = hd.HopDongID
		INNER JOIN ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet dchdct ON hdct.HopDongChiTietID = dchdct.HopDongChiTietREF
		WHERE 1=1 AND 
			  (@NgayDanhSo_GioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan) AND 
			  CAST(dchdct.LastModifiedAt AS DATE) = @NgayCheckThayDoi

			  AND @SoHopDong IS NULL


		UNION
		--TH3. thay đổi thông tin treo
		SELECT DISTINCT hdct.HopDongFK , tchdct.HopDongChiTietREF, ngaythuchien = @NgayGhiNhan, Loaithaydoi = N'thông tin treo', Mathaydoi = 3
		FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet tchdct
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		INNER JOIN ABM_Data_ThucChay.dbo.hopdong hd ON hd.HopDongID = hdct.HopDongFK
		WHERE	1 = 1
				AND hdct.DeletedStatus = 0
				AND hd.TrangThaiHopDong <> 3
				AND hdct.DmLoaiREF <> 13 
				AND hdct.DmSanPhamREF IN (140,228,564,549,5082) 
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1 
				AND EXISTS (SELECT TOP (1) dc.HopDongChiTietREF from ABM_Data_ThucChay.dbo.DotChayHopDongchitiet dc WHERE dc.HopDongChiTietREF = hdct.HopDongChiTietID)--Check CPD dotchay 02/12/2022
	
				AND convert(date,tchdct.LastModifiedAt) = @NgayCheckThayDoi
				AND (@NgayDanhSo_GioiHan IS NULL OR hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan)

				AND @SoHopDong IS NULL

		--TH5. xử lý tay phân bổ
		UNION 
		SELECT DISTINCT hd.HopDongID, hdct.HopDongChiTietID, ngaythuchien = @NgayGhiNhan, Loaithaydoi = N'xử lý tay hợp đồng/phân bổ', Mathaydoi = 1
		FROM ABM_Data_ThucChay.dbo.HopDong hd
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hd.TrangThaiHopDong <> 3
			  AND hdct.DmSanPhamREF IN (140,228,241,564,549,5082)
			  AND hdct.DmLoaiREF <> 13 
		      AND  Upper((RTrim(LTrim(hdct.DonViTinh)))) IN (N'NGÀY' , N'TUẦN' , N'THÁNG' , N'NĂM' )
			  AND exists (select top 1 dc.HopDongChiTietREF from ABM_Data_ThucChay.dbo.DotChayHopDongchitiet dc WHERE dc.HopDongChiTietREF = hdct.HopDongChiTietID)--check co dot chay 02/12/2022

			  AND hd.SoHopDong = @SoHopDong
			  AND (@HopDongChiTietID IS NULL OR hdct.HopDongChiTietID = @HopDongChiTietID)

		--TH4. Phân bổ bị xóa
		UPDATE dmcheck
		SET dmcheck.Loaithaydoi = N'phân bổ bị xóa',
			mathaydoi = 4
		FROM #DmPhanbothaydoi dmcheck
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dmcheck.hopdongchitietID AND ISNULL(hdct.DeletedStatus , 0) = 1

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
		WHERE t1.Mathaydoi <> 4
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
		WHERE Mathaydoi = 4
	END

	--================================================= 2. tính thay đổi =====================================
	BEGIN
		--1. Xác định thông tin đánh số, đơn giá, số lượng chuẩn theo đơn vị tính ở hiện tại
		--   [ThucChay_GetSoLuongChuanTheoDonViTinh](hdct.SoLuong ,hdct.DonViTinh ,hdct.HopDongChiTietID)
		UPDATE dmcheck
		SET dmcheck.SoLuongDotChayHD = IIF(hdct.DmLoaiBannerREF = 5,
									ISNULL(dbo.ThucChay_GetSoLuong_DonViTinh(hdct.SoLuong,hdct.DonViTinh), 0),
									dc.songay)
		FROM #DmPhanbothaydoichitiet dmcheck
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dmcheck.hopdongchitietID
		INNER JOIN (SELECT dchdct.HopDongChiTietREF , 
						   songay = ISNULL(sum(DATEDIFF(day, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1),0)
					FROM ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet dchdct 
					WHERE dchdct.RecordStatus = 0
						  AND dchdct.DeletedStatus = 0
					GROUP BY HopDongChiTietREF  
					) dc ON dc.HopDongChiTietREF = dmcheck.hopdongchitietID
		WHERE dmcheck.pbxoa = 0

		--  dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(hdct.SoLuong,hdct.DonViTinh,NULL,@NgayThucHien, NULL, HopDongChiTietID)
		UPDATE dmcheck
		SET dmcheck.dongiatheodonvitinh = IIF(dmcheck.SoLuongDotChayHD = 0, 0, hdct.SoLuong*hdct.DonGia/dmcheck.SoLuongDotChayHD )
		FROM #DmPhanbothaydoichitiet dmcheck
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dmcheck.hopdongchitietID
		WHERE dmcheck.pbxoa = 0

		--2. Xác định số lượng, giá tị thực chạy tính đến hiện tại
		--   ThucChay_GetSoLuongThucChayBooking_CPDDotChay(SoLuongDotChayHD ,hdct.DonViTinh ,HopDongChiTietID ,@NgayThucHien )
		UPDATE dmcheck
		SET dmcheck.SoLuongThucChayHT = soluong.Soluong
		FROM #DmPhanbothaydoichitiet dmcheck
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dmcheck.hopdongchitietID
		INNER JOIN (SELECT HopDongChiTietREF, ISNULL(sum(DATEDIFF(day, 
																  ThoiGianBatDau, 
																  IIF(convert(date,ThoiGianKetThuc) > @NgayGhiNhan, 
																	  @NgayGhiNhan, 
																	  ThoiGianKetThuc) + 1)),0) AS Soluong
					FROM (SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.BookingREF, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc 
						  FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct
						  INNER JOIN ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet dchdct 
										ON tchdct.HopDongChiTietREF = dchdct.HopDongChiTietREF	
										   AND dchdct.BookingREF = tchdct.BookingREF
						  WHERE  tchdct.DeletedStatus = 0 AND 
								 CONVERT(date,tchdct.ThoiGianBatDau) <= @NgayGhiNhan AND
								 dchdct.DeletedStatus = 0 AND
								 dchdct.RecordStatus = 0) tchdct
					GROUP BY HopDongChiTietREF
					) soluong ON soluong.HopDongChiTietREF = dmcheck.hopdongchitietID
		WHERE dmcheck.pbxoa = 0 AND ISNULL(hdct.DmLoaiBannerREF, 0) <> 5

		UPDATE dmcheck
		SET dmcheck.SoLuongThucChayHT = soluong.Soluong
		FROM #DmPhanbothaydoichitiet dmcheck
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dmcheck.hopdongchitietID
		INNER JOIN (SELECT HopDongChiTietREF, ISNULL(sum(DATEDIFF(day, 
																  ThoiGianBatDau, 
																  IIF(convert(date,ThoiGianKetThuc) > @NgayGhiNhan, 
																	  @NgayGhiNhan, 
																	  ThoiGianKetThuc) + 1)),0) AS Soluong
					FROM (SELECT DISTINCT tchdct.HopDongChiTietREF, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc 
						  FROM ABM_Data_ThucChay.dbo.ThucChayHopDongChiTiet  tchdct
						  INNER JOIN ABM_Data_ThucChay.dbo.DotChayHopDongChiTiet dchdct 
										ON tchdct.HopDongChiTietREF = dchdct.HopDongChiTietREF	
										   AND dchdct.BookingREF = tchdct.BookingREF
						  WHERE  tchdct.DeletedStatus = 0 AND 
								 CONVERT(date,tchdct.ThoiGianBatDau) <= @NgayGhiNhan AND
								 dchdct.DeletedStatus = 0 AND
								 dchdct.RecordStatus = 0) tchdct
					GROUP BY HopDongChiTietREF
					) soluong ON soluong.HopDongChiTietREF = dmcheck.hopdongchitietID
		WHERE dmcheck.pbxoa = 0 AND ISNULL(hdct.DmLoaiBannerREF, 0) = 5

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
		WHERE ROUND(GiaTriThayDoi, 0) = 0   AND 
			  ROUND(GiaTriKMThayDoi, 0) = 0 AND 
			  Soluongthaydoi = 0            AND 
			  SoluongKMthaydoi = 0 

		--5. Thông tin nhãn hàng
		----   TH 1 ngày phân bổ có thể chạy cho nhiều nhãn hàng
		----   [dbo].[f_ReturnListConcatNhanHangREF_v2](HopDongChiTietID, @NgayThucHien)
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
		--WHERE pbxoa = 0;
		
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
		--      pbxoa = 0;


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

		--6. Thông tin đợt chạy hợp đồng của phân bổ
		--   dbo.GetDotChayBookingByHopDongChiTiet(HopDongChiTietID,'Y') 
		UPDATE dm
		SET DotChayHopDong = ISNULL(ttdc.thongtindotchaydanhso, 'N/A')
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
		WHERE pbxoa = 0

		--7. Thông tin đợt chạy thực treo của phân bổ
		--   GetDotChayBookingByHopDongChiTiet(HopDongChiTietID,'N')
		UPDATE dm
		SET dm.DotChayBooking = ISNULL(ttdc.thongtindotchaydanhso, 'N/A')
		FROM #DmPhanbothaydoichitiet dm
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
		WHERE dm.pbxoa = 0

		-- 8. Thông tin đơn giá đánh số của phân bổ
		--    ThucChay_GetDonGiaByNgayThucHien (@NgayThucHien, HopDongChiTietID, hdct.dongia)
		UPDATE dm
		SET dm.dongia = hdct.DonGia
		FROM #DmPhanbothaydoichitiet dm
		INNER JOIN ABM_Data_ThucChay.dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = dm.hopdongchitietID
		WHERE pbxoa = 0

		--DECLARE @Sophanbocantinh INT
		--SELECT @Sophanbocantinh = COUNT(DISTINCT hopdongchitietID)
		--FROM #DmPhanbothaydoichitiet
		--PRINT (N'So phan bo can tinh: ' + CONVERT(varchar(10),@Sophanbocantinh))
	END

	--================================================= 3. thực hiện đối trừ =================================
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
		   N'Đối trừ: SP tối ưu [dbo].[ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh] đối trừ do ' + dmcheck.Loaithaydoi, 
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
				  ,[DotChayHopDong]
				  ,[SoLuongDotChayHD]
				  ,[DotChayBooking]
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
				  ,-SUM([ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) AS [GiaTriThayDoi]
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
				  ,-SUM(tcdt.[SoLuongThucChayKM] + tcdt.[SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
				  ,-SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) AS [GiaTriKMThayDoi]
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
				  ,[DotChayBooking]
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
			  HAVING SUM(tcdt.[ThanhTienSauTrietKhauThucChay] + tcdt.[GiaTriThayDoi]) <> 0
			  OR SUM(tcdt.[ThanhTienKM] + tcdt.[GiaTriKMThayDoi]) <> 0
			  ) tcdt
	  INNER JOIN #DmPhanbothaydoichitiet dmcheck ON dmcheck.hopdongchitietID = tcdt.HopDongChiTietREF



	  --=============================================== 4. thực hiện tính lại ================================
	INSERT INTO ABM_Data_ThucChay.dbo.ThucChayDaTinh
	SELECT  NEWID(), TD.*
	FROM 
	(SELECT  --ID Hop Dong
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
			dmcheck.Nhanhang NhanHang,
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
			CAST(dmcheck.DotChayHopDong AS NVARCHAR(1000)) DotChayHopDong,  
			dmcheck.SoLuongDotChayHD AS SoLuongDotChayHD,
			CAST(dmcheck.DotChayBooking AS NVARCHAR(1000)) DotChayBooking,
			0 AS SoLuongDotChayBooking, 
			--Thong tin ve Tien
			C.SoLuong AS SoLuong, 
			dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
			ROUND(dmcheck.dongia, 2) as DonGia, 
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
			@NgayGhiNhan AS NgayThucHien,
			ROUND(ISNULL(dmcheck.TongGiaTriThucChayDaTinhHT, 0), 2) as GiaTriThayDoi,
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
			ISNULL(dmcheck.SoLuongThucChayHT, 0)  SoLuongThayDoi,
			ISNULL(dmcheck.SoluongKMHT, 0)	 SoLuongKMThayDoi,
			ROUND(ISNULL(dmcheck.GiatriKMHT, 0), 2)  GiaTriKMThayDoi,
			N'Tính lại: SP tối ưu [dbo].[ThucChay_CPDdotchay_GhiNhanThayDoi_ThucChayDaTinh] tính lại do ' + dmcheck.Loaithaydoi AS GhiChu
		FROM #DmPhanbothaydoichitiet dmcheck
		INNER JOIN 
		(   SELECT * FROM ABM_Data_ThucChay.dbo.HopDongChiTiet 
			WHERE DmSanPhamREF in (140,228,241,564,549,5082)
				    AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 1 --Đơn vị của hình thức CPD 
		) C ON C.HopDongChiTietID = dmcheck.hopdongchitietID 
		INNER JOIN  
		( 
	 		SELECT * FROM ABM_Data_ThucChay.dbo.HopDong hd 
			WHERE hd.TrangThaiHopDong <> 3
		) D on D.HopDongID = dmcheck.hopdongREF
		INNER JOIN ABM_Data_ThucChay.dbo.DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
		WHERE dmcheck.pbxoa = 0
	) TD
	where ROUND(TD.GiaTriThayDoi,0) <> 0 OR ROUND(TD.GiaTriKMThayDoi,0) <> 0
		
	DROP TABLE #DmPhanbothaydoichitiet
	DROP TABLE #DmPhanbothaydoi

COMMIT TRANSACTION;

END

```
