# Stored Procedure: `ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_XulyConfirmTcHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-21 10:23:56.610000
- **Ngày sửa cuối**: 2018-07-23 14:13:42.827000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TaiKhoanAdmarket` | `nvarchar(400)` | No |
| `@SoTienConfirm_VAT` | `float(8)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_XulyConfirmTcHopDong] 
	 @NgayThucHien = '2018-07-20',
	 @SoHopDong = 'QC5120718', 
	 @DmSanPhamREF = 585, 
	 @TaiKhoanAdmarket = 'kiengiang1410', 
	 @SoTienConfirm_VAT =  2000400 , 
	 @FromDate  = '1900-01-01', 
    @ToDate  = '1900-01-01'
*/
CREATE PROCEDURE [dbo].[ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_XulyConfirmTcHopDong] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(100), 
	@DmSanPhamREF INT, 
	@TaiKhoanAdmarket NVARCHAR(200), 
	@SoTienConfirm_VAT FLOAT, 
	@FromDate DATETIME = '1900-01-01', 
    @ToDate DATETIME = '1900-01-01'
AS
BEGIN
	/*
	cấu trúc cho vào ghi chú: TenSP_TaiKhoan_Bosung/Giamgiatri
	cho vao dotchaybooking: Bo sung cho thoi gian nao (ngay-thang-nam)
	*/
	DECLARE @SoTienDieuChinh FLOAT, @ThanhTienThucChayDatinhHDCT FLOAT, @SoTienConfirm FLOAT
	, @HopDongID INT, @HopDongChiTietID INT, @TongThanhTienSanPhamHopDong FLOAT, @ThanhTienHDCT FLOAT
	DECLARE @ThanhTienThucChayOnline FLOAT, @ThanhTienThucChayTK FLOAT, @ThanhTienThucChayTKHopDong FLOAT
	DECLARE @ghichu NVARCHAR(MAX) =''
	, @DoLechChoPhepTinh INT = 2

	SET @HopDongID = ISNULL((SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID),0)
	SET @SoTienConfirm = ROUND((@SoTienConfirm_VAT/1.1),0)

	SET @TongThanhTienSanPhamHopDong = 
	(SELECT SUM(ThanhTien)
		FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 
		AND HopDongFK = @HopDongID 
		AND DmSanPhamREF = @DmSanPhamREF 
		AND TK_AdMarket = @TaiKhoanAdmarket)
	
	--XAC DINH TONG TIEN ONLINE CUA TAI KHOAN
	----THUC HIEN CHECK VA XAC DINH SO TIEN DIEU CHINH THUC CHAY CHO HOP DONG
	--San pham Adx
	IF(@DmSanPhamREF = 585)
	BEGIN
	    SET @ThanhTienThucChayTK = ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdXforUsers 
									WHERE 1=1 AND NgayThucHien <'2017-09-11' AND  username = @TaiKhoanAdmarket),0)

									 + ISNULL(( SELECT SUM(CONVERT(FLOAT,domain_tt_money))/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
									 WHERE 1=1 AND NgayThucHien >='2017-09-11' AND NgayThucHien <= @NgayThucHien AND username = @TaiKhoanAdmarket AND DmSanPhamREF = @DmSanPhamREF),0)
		--ThanhtienthucchayTkHopDong
		SET @ThanhTienThucChayTKHopDong = ISNULL((SELECT SUM(tcdt.ThanhTienThucChay)ThanhTienThucChay FROM
											(
													SELECT HopDongID, HopDongChiTietREF
													, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
													FROM dbo.ThucChayDaTinhAdmarket
													WHERE TrangThaiHopDong <> 3 
													AND DmSanPhamREF = @DmSanPhamREF
													AND NgayThucHien <= @NgayThucHien
													GROUP BY HopDongID, HopDongChiTietREF
												)tcdt 
												INNER JOIN 
												(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
															WHERE DeletedStatus = 0 
															AND TK_AdMarket = @TaiKhoanAdmarket 
															AND DmSanPhamREF = @DmSanPhamREF
												)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
											),0)
		SET @ThanhTienThucChayOnline = @ThanhTienThucChayTK - @ThanhTienThucChayTKHopDong
	END
	--San pham CPC Admarket
	ELSE IF(@DmSanPhamREF = 144)
	BEGIN
	      SET @ThanhTienThucChayTK = ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdmarketUsers 
									WHERE 1=1 AND NgayThucHien <'2017-09-11' AND  username = @TaiKhoanAdmarket),0)

									 + ISNULL(( SELECT SUM(CONVERT(FLOAT,domain_tt_money))/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdmarket_ADX_CPC_HopDong 
									 WHERE 1=1 AND NgayThucHien >='2017-09-11' AND NgayThucHien <= @NgayThucHien AND username = @TaiKhoanAdmarket AND DmSanPhamREF = @DmSanPhamREF),0)
		--ThanhtienthucchayTkHopDong
		SET @ThanhTienThucChayTKHopDong = ISNULL((SELECT SUM(tcdt.ThanhTienThucChay)ThanhTienThucChay FROM
											(
													SELECT HopDongID, HopDongChiTietREF
													, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
													FROM dbo.ThucChayDaTinhAdmarket
													WHERE TrangThaiHopDong <> 3 
													AND DmSanPhamREF = @DmSanPhamREF
													AND NgayThucHien <= @NgayThucHien
													GROUP BY HopDongID, HopDongChiTietREF
												)tcdt 
												INNER JOIN 
												(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
															WHERE DeletedStatus = 0 
															AND TK_AdMarket = @TaiKhoanAdmarket 
															AND DmSanPhamREF = @DmSanPhamREF
												)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
											),0)
		SET @ThanhTienThucChayOnline = @ThanhTienThucChayTK - @ThanhTienThucChayTKHopDong
	END
	--San pham ViewPlus
	ELSE 
	BEGIN
	         SET @ThanhTienThucChayTK = ISNULL((SELECT SUM(money)/1.1 AS ThanhTienThucChay FROM dbo.ThucChayViewPlusForUsers 
									WHERE 1=1 AND NgayThucHien <'2017-09-11' AND  username = @TaiKhoanAdmarket),0)

									 + ISNULL(( SELECT SUM(CONVERT(FLOAT,domain_money))/1.1 AS ThanhTienThucChay FROM dbo.ThucChayAdmarket_Viewplus_HopDong 
									 WHERE 1=1 AND NgayThucHien >='2017-09-11' AND NgayThucHien <= @NgayThucHien AND username = @TaiKhoanAdmarket AND DmSanPhamREF = @DmSanPhamREF),0)
			--ThanhtienthucchayTkHopDong
			SET @ThanhTienThucChayTKHopDong = ISNULL((SELECT SUM(tcdt.ThanhTienThucChay)ThanhTienThucChay FROM
												(
														SELECT HopDongID, HopDongChiTietREF
														, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
														FROM dbo.ThucChayDaTinhAdmarket
														WHERE TrangThaiHopDong <> 3 
														AND DmSanPhamREF = @DmSanPhamREF
														AND NgayThucHien <= @NgayThucHien
														GROUP BY HopDongID, HopDongChiTietREF
													)tcdt 
													INNER JOIN 
													(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
																WHERE DeletedStatus = 0 
																AND TK_AdMarket = @TaiKhoanAdmarket 
																AND DmSanPhamREF = @DmSanPhamREF
													)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
												),0)
			SET @ThanhTienThucChayOnline = @ThanhTienThucChayTK - @ThanhTienThucChayTKHopDong
	END
	--TH0. NEU GIA TRI CONFIRM = 0 THI GHI NHAN TOAN BO GIA TRI THUCCHAY THEO TAI KHOAN HOPDONG VE = 0
	IF(@SoTienConfirm = 0)
	BEGIN
	    PRINT N'Thực hiện đối trừ toàn bộ tiền thực chạy của hợp đồng và chuyển sang online'
		EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_DoiTruGiam_HopDong]
			@NgayThucHien = @NgayThucHien, 
			@HopDongID = @HopDongID,
			@DmSanPhamREF = @DmSanPhamREF, 
			@Tk_Admarket = @TaiKhoanAdmarket
	END
	ELSE
    IF(@SoTienConfirm >0)
	BEGIN
		--SO TIEN CONFIRM <= TONG THANH TIEN HOPDONG
	    IF((@SoTienConfirm - @DoLechChoPhepTinh)<= @TongThanhTienSanPhamHopDong )
		BEGIN
			--TH1: SO TIEN CONFIRM > THANH TIEN THUC CHAY THEO TAI KHOAN CUA HOPDONG
		    IF(@SoTienConfirm > @ThanhTienThucChayTKHopDong) 
			BEGIN
			    IF((@SoTienConfirm - @ThanhTienThucChayTKHopDong) <= @ThanhTienThucChayOnline)
				BEGIN
					IF(EXISTS(SELECT HopDongFK, COUNT(HopDongChiTietID)sl 
					FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 
					AND HopDongFK = @HopDongID 
					AND DmSanPhamREF = @DmSanPhamREF 
					AND TK_AdMarket = @TaiKhoanAdmarket
					GROUP BY HopDongFK HAVING COUNT(HopDongChiTietID) >1))
					BEGIN
							PRINT 'TH Co nhieu hop dong chi tiet'
							DECLARE pb_admarket_cursor CURSOR FOR
	
							SELECT HopDongChiTietID, ThanhTien
							FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 
							AND HopDongFK = @HopDongID 
							AND DmSanPhamREF = @DmSanPhamREF 
							AND TK_AdMarket = @TaiKhoanAdmarket
							ORDER BY HopDongChiTietID ASC 

							OPEN pb_admarket_cursor
	
							FETCH NEXT FROM pb_admarket_cursor INTO @HopDongChiTietID, @ThanhTienHDCT
							WHILE @@FETCH_STATUS = 0
							BEGIN
								PRINT CONVERT(NVARCHAR(100),@HopDongChiTietID)
								SET @SoTienDieuChinh = 0
								--NEU SO TIEN CONFIRM >0
								IF(@SoTienConfirm >0)
								BEGIN
								    --TINH KHONG PHAN BIET THOI GIAN
									IF(@FromDate = '1900-01-01' AND @ToDate = '1900-01-01')
									BEGIN
										--XAC DINH SO TIEN TCDT CUA HOPDONGCHITIET
										SET @ThanhTienThucChayDatinhHDCT = (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																				FROM dbo.ThucChayDaTinhAdmarket
																				WHERE HopDongID = @HopDongID
																				AND DmSanPhamREF = @DmSanPhamREF
																				AND HopDongChiTietREF = @HopDongChiTietID 
																				AND NgayThucHien <= @NgayThucHien) 
										IF(@SoTienConfirm <=@ThanhTienHDCT)
											BEGIN
											 SET @SoTienDieuChinh = @SoTienConfirm - @ThanhTienThucChayDatinhHDCT
							 
												--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
												IF(@SoTienDieuChinh <> 0)
													EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
											 END
										ELSE
										BEGIN
											IF(@SoTienConfirm > @ThanhTienThucChayDatinhHDCT)
											BEGIN
												SET @SoTienDieuChinh = @ThanhTienHDCT - @ThanhTienThucChayDatinhHDCT
												SET @SoTienConfirm = @SoTienConfirm - @ThanhTienHDCT
												--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
												IF(@SoTienDieuChinh <> 0)
													EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
											END
										END
									END
									--TINH PHAN BIET THOI GIAN
									ELSE
									BEGIN
										PRINT 'TINH PHAN BIET THOI GIAN'
										--XAC DINH SO TIEN TCDT CUA HOPDONGCHITIET
										SET @ThanhTienThucChayDatinhHDCT = (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																				FROM dbo.ThucChayDaTinhAdmarket
																				WHERE HopDongID = @HopDongID
																				AND DmSanPhamREF = @DmSanPhamREF
																				AND HopDongChiTietREF = @HopDongChiTietID AND NgayThucHien BETWEEN @FromDate AND @ToDate) 
										--PHan ghi chu
										SET @ThanhTienThucChayDatinhHDCT =  (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																				FROM dbo.ThucChayDaTinhAdmarket
																				WHERE HopDongID = @HopDongID
																				AND DmSanPhamREF = @DmSanPhamREF
																				AND HopDongChiTietREF = @HopDongChiTietID AND SoLuongDotChayBooking BETWEEN MONTH(@FromDate) AND MONTH(@ToDate)
																			) 
										IF(@SoTienConfirm <=@ThanhTienHDCT)
										BEGIN
											 SET @SoTienDieuChinh = @SoTienConfirm - @ThanhTienThucChayDatinhHDCT
											--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
											EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
											BREAK;
										END
										ELSE
										BEGIN
											IF(@SoTienConfirm > @ThanhTienThucChayDatinhHDCT)
											BEGIN
												IF(@ThanhTienHDCT>= @ThanhTienThucChayDatinhHDCT)
												BEGIN
													SET @SoTienDieuChinh = @ThanhTienHDCT - @ThanhTienThucChayDatinhHDCT
													SET @SoTienConfirm = @SoTienConfirm - @ThanhTienHDCT
													--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
													EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
												END
											END
										END
									END
								END
							

								FETCH NEXT FROM pb_admarket_cursor INTO @HopDongChiTietID, @ThanhTienHDCT
							END
	
							CLOSE pb_admarket_cursor
							DEALLOCATE pb_admarket_cursor
					END
					ELSE
					BEGIN
						PRINT'TH chi co 01 hop dong chi tiet fff'
						--TINH KHONG PHAN BIET THOI GIAN
						SET @HopDongChiTietID = ISNULL((SELECT  TOP (1) HopDongChiTietID
						FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 
						AND HopDongFK = @HopDongID 
						AND DmSanPhamREF = @DmSanPhamREF 
						AND TK_AdMarket = @TaiKhoanAdmarket 
						ORDER BY HopDongChiTietID),0)

						SET @ThanhTienHDCT = ISNULL((SELECT TOP (1) ThanhTien FROM dbo.HopDongChiTiet
						WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID),0)
						PRINT 'khong chay'
						IF(@FromDate = '1900-01-01' AND @ToDate = '1900-01-01')
						BEGIN
							--XAC DINH SO TIEN TCDT CUA HOPDONGCHITIET
							PRINT 'vao day'
							SET @ThanhTienThucChayDatinhHDCT = (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																	FROM dbo.ThucChayDaTinhAdmarket
																	WHERE HopDongID = @HopDongID
																	AND DmSanPhamREF = @DmSanPhamREF
																	AND HopDongChiTietREF = @HopDongChiTietID
																	AND NgayThucHien <= @NgayThucHien) 
							IF(@SoTienConfirm <=@ThanhTienHDCT)
								BEGIN
									SET @SoTienDieuChinh = @SoTienConfirm - @ThanhTienThucChayDatinhHDCT
									PRINT 'ghinhan'
									SET @ThanhTienThucChayOnline = ISNULL(@ThanhTienThucChayOnline,0)

									PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@SoTienDieuChinh))
									PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienHDCT))
									PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@HopDongChiTietID))
									PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienThucChayOnline))

									--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
									EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
									@NgayThucHien		= @NgayThucHien, 
									@HopDongID			= @HopDongID,
									@HopDongChiTietID	= @HopDongChiTietID, 
									@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
									@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
									@GiaTriThayDoi		= @SoTienDieuChinh, 
									@DmSanPhamREF		= @DmSanPhamREF, 
									@GhiChu				= @ghichu ,
									@Tk					= @TaiKhoanAdmarket
									END
							ELSE
							BEGIN
								IF(@SoTienConfirm > @ThanhTienThucChayDatinhHDCT)
								BEGIN
									IF(@ThanhTienHDCT>= @ThanhTienThucChayDatinhHDCT)
									BEGIN
										SET @SoTienDieuChinh = @ThanhTienHDCT - @ThanhTienThucChayDatinhHDCT
										SET @SoTienConfirm = @SoTienConfirm - @ThanhTienHDCT
										--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
										EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
										@NgayThucHien		= @NgayThucHien, 
										@HopDongID			= @HopDongID,
										@HopDongChiTietID	= @HopDongChiTietID, 
										@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
										@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
										@GiaTriThayDoi		= @SoTienDieuChinh, 
										@DmSanPhamREF		= @DmSanPhamREF, 
										@GhiChu				= @ghichu ,
										@Tk					= @TaiKhoanAdmarket
									END
								END
							END
						END
						--TINH PHAN BIET THOI GIAN
						ELSE
						BEGIN
							PRINT 'TINH PHAN BIET THOI GIAN'
							--XAC DINH SO TIEN TCDT CUA HOPDONGCHITIET
							SET @ThanhTienThucChayDatinhHDCT = (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																	FROM dbo.ThucChayDaTinhAdmarket
																	WHERE HopDongID = @HopDongID
																	AND DmSanPhamREF = @DmSanPhamREF
																	AND HopDongChiTietREF = @HopDongChiTietID AND NgayThucHien BETWEEN @FromDate AND @ToDate) 
							--PHan ghi chu
							SET @ThanhTienThucChayDatinhHDCT =  (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																	FROM dbo.ThucChayDaTinhAdmarket
																	WHERE HopDongID = @HopDongID
																	AND DmSanPhamREF = @DmSanPhamREF
																	AND HopDongChiTietREF = @HopDongChiTietID AND SoLuongDotChayBooking BETWEEN MONTH(@FromDate) AND MONTH(@ToDate)
																) 
							IF(@SoTienConfirm <=@ThanhTienHDCT)
							BEGIN
									SET @SoTienDieuChinh = @SoTienConfirm - @ThanhTienThucChayDatinhHDCT
								--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
								EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
								@NgayThucHien		= @NgayThucHien, 
								@HopDongID			= @HopDongID,
								@HopDongChiTietID	= @HopDongChiTietID, 
								@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
								@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
								@GiaTriThayDoi		= @SoTienDieuChinh, 
								@DmSanPhamREF		= @DmSanPhamREF, 
								@GhiChu				= @ghichu ,
								@Tk					= @TaiKhoanAdmarket
							END
							ELSE
							BEGIN
								IF(@SoTienConfirm > @ThanhTienThucChayDatinhHDCT)
								BEGIN
									IF(@ThanhTienHDCT>= @ThanhTienThucChayDatinhHDCT)
									BEGIN
										SET @SoTienDieuChinh = @ThanhTienHDCT - @ThanhTienThucChayDatinhHDCT
										SET @SoTienConfirm = @SoTienConfirm - @ThanhTienHDCT
										--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
										EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong]
										@NgayThucHien		= @NgayThucHien, 
										@HopDongID			= @HopDongID,
										@HopDongChiTietID	= @HopDongChiTietID, 
										@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
										@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
										@GiaTriThayDoi		= @SoTienDieuChinh, 
										@DmSanPhamREF		= @DmSanPhamREF, 
										@GhiChu				= @ghichu ,
										@Tk					= @TaiKhoanAdmarket
									END
								END
							END
						END
					END
				END
				--CHI CO 01 HOPDONGCHITIET
				ELSE
				BEGIN
					PRINT N'Số tiên confirm lớn hơn thanhtien của hopdong hoặc số tiền confirm lớn hơn ThanhTienThucChayOnline'
					PRINT N'Số tiền confirm: ' + CONVERT(NVARCHAR(100),dbo.FormatNumber(@SoTienConfirm))
					PRINT N'Số Tổng thành tiền:' + CONVERT(NVARCHAR(100),dbo.FormatNumber(@TongThanhTienSanPhamHopDong))
					PRINT N'Số tiền online:' + CONVERT(NVARCHAR(100),dbo.FormatNumber(@ThanhTienThucChayOnline))
					PRINT N'Số tiền thực chạy tài khoản: ' + CONVERT(NVARCHAR(100),dbo.FormatNumber(@ThanhTienThucChayTK))

					SELECT tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienThucChay)ThanhTienThucChay 
					   FROM
							(
									SELECT HopDongID,SoHopDong, HopDongChiTietREF
									, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
									FROM dbo.ThucChayDaTinhAdmarket
									WHERE TrangThaiHopDong <> 3 
									AND DmSanPhamREF = @DmSanPhamREF
									AND NgayThucHien <= @NgayThucHien
									GROUP BY HopDongID, SoHopDong, HopDongChiTietREF
								)tcdt 
								INNER JOIN 
								(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
											WHERE DeletedStatus = 0 
											AND TK_AdMarket = @TaiKhoanAdmarket 
											AND DmSanPhamREF = @DmSanPhamREF
								)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
						GROUP BY tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF
				END
			END
			--TH2: SO TIEN CONFIRM < THANH TIEN THUC CHAY THEO TAI KHOAN CUA HOPDONG
			ELSE
            BEGIN
               PRINT N' SO TIEN CONFIRM < THANH TIEN THUC CHAY THEO TAI KHOAN CUA HOPDONG'
			   --**************THUC HIEN GIAM TIEN THUC CHAY THEO TAI KHOAN HOPDONG VA GHI TANG ONLINE*********************
			   IF(EXISTS(SELECT HopDongFK, COUNT(HopDongChiTietID)sl 
					FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 
					AND HopDongFK = @HopDongID 
					AND DmSanPhamREF = @DmSanPhamREF 
					AND TK_AdMarket = @TaiKhoanAdmarket
					GROUP BY HopDongFK HAVING COUNT(HopDongChiTietID) >1))
					BEGIN
							PRINT 'TH Co nhieu hop dong chi tiet'
							DECLARE pb_admarket_cursor CURSOR FOR
	
							SELECT HopDongChiTietID, ThanhTien
							FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 
							AND HopDongFK = @HopDongID 
							AND DmSanPhamREF = @DmSanPhamREF 
							AND TK_AdMarket = @TaiKhoanAdmarket
							ORDER BY HopDongChiTietID ASC 

							OPEN pb_admarket_cursor
	
							FETCH NEXT FROM pb_admarket_cursor INTO @HopDongChiTietID, @ThanhTienHDCT
							WHILE @@FETCH_STATUS = 0
							BEGIN
								PRINT CONVERT(NVARCHAR(100),@HopDongChiTietID)
								SET @SoTienDieuChinh = 0
								--NEU SO TIEN CONFIRM >0
								IF(@SoTienConfirm >0)
								BEGIN
								    --TINH KHONG PHAN BIET THOI GIAN
									IF(@FromDate = '1900-01-01' AND @ToDate = '1900-01-01')
									BEGIN
										--XAC DINH SO TIEN TCDT CUA HOPDONGCHITIET
										SET @ThanhTienThucChayDatinhHDCT = (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																				FROM dbo.ThucChayDaTinhAdmarket
																				WHERE HopDongID = @HopDongID
																				AND DmSanPhamREF = @DmSanPhamREF
																				AND HopDongChiTietREF = @HopDongChiTietID
																				AND NgayThucHien <= @NgayThucHien) 
										IF(@SoTienConfirm <=@ThanhTienHDCT)
											BEGIN
											 SET @SoTienDieuChinh = @SoTienConfirm - @ThanhTienThucChayDatinhHDCT
							 
												--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
												IF(@SoTienDieuChinh <> 0)
													EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
											 END
										ELSE
										BEGIN
											IF(@SoTienConfirm > @ThanhTienThucChayDatinhHDCT)
											BEGIN
												SET @SoTienDieuChinh = @ThanhTienHDCT - @ThanhTienThucChayDatinhHDCT
												SET @SoTienConfirm = @SoTienConfirm - @ThanhTienHDCT
												--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
												IF(@SoTienDieuChinh <> 0)
													EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
											END
										END
									END
									--TINH PHAN BIET THOI GIAN
									ELSE
									BEGIN
										PRINT 'TINH PHAN BIET THOI GIAN'
										--XAC DINH SO TIEN TCDT CUA HOPDONGCHITIET
										SET @ThanhTienThucChayDatinhHDCT = (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																				FROM dbo.ThucChayDaTinhAdmarket
																				WHERE HopDongID = @HopDongID
																				AND DmSanPhamREF = @DmSanPhamREF
																				AND HopDongChiTietREF = @HopDongChiTietID AND NgayThucHien BETWEEN @FromDate AND @ToDate) 
										--PHan ghi chu
										SET @ThanhTienThucChayDatinhHDCT =  (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																				FROM dbo.ThucChayDaTinhAdmarket
																				WHERE HopDongID = @HopDongID
																				AND DmSanPhamREF = @DmSanPhamREF
																				AND HopDongChiTietREF = @HopDongChiTietID AND SoLuongDotChayBooking BETWEEN MONTH(@FromDate) AND MONTH(@ToDate)
																			) 
										IF(@SoTienConfirm <=@ThanhTienHDCT)
										BEGIN
											 SET @SoTienDieuChinh = @SoTienConfirm - @ThanhTienThucChayDatinhHDCT
											--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
											EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
											BREAK;
										END
										ELSE
										BEGIN
											IF(@SoTienConfirm > @ThanhTienThucChayDatinhHDCT)
											BEGIN
												IF(@ThanhTienHDCT>= @ThanhTienThucChayDatinhHDCT)
												BEGIN
													SET @SoTienDieuChinh = @ThanhTienHDCT - @ThanhTienThucChayDatinhHDCT
													SET @SoTienConfirm = @SoTienConfirm - @ThanhTienHDCT
													--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
													EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
												END
											END
										END
									END
								END
							

								FETCH NEXT FROM pb_admarket_cursor INTO @HopDongChiTietID, @ThanhTienHDCT
							END
	
							CLOSE pb_admarket_cursor
							DEALLOCATE pb_admarket_cursor
					END
					ELSE
					BEGIN
						PRINT N'TH chi co 01 hop dong chi tiet ddd'

						SET @HopDongChiTietID = ISNULL((SELECT  TOP (1) HopDongChiTietID
						FROM dbo.HopDongChiTiet WHERE DeletedStatus = 0 
						AND HopDongFK = @HopDongID 
						AND DmSanPhamREF = @DmSanPhamREF 
						AND TK_AdMarket = @TaiKhoanAdmarket 
						ORDER BY HopDongChiTietID),0)

						SET @ThanhTienHDCT = ISNULL((SELECT TOP (1) ThanhTien FROM dbo.HopDongChiTiet
						WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID),0)
						--TINH KHONG PHAN BIET THOI GIAN
						PRINT 'khogn vao'
						IF(@FromDate = '1900-01-01' AND @ToDate = '1900-01-01')
						BEGIN
							--XAC DINH SO TIEN TCDT CUA HOPDONGCHITIET
							SET @ThanhTienThucChayDatinhHDCT = (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																	FROM dbo.ThucChayDaTinhAdmarket
																	WHERE HopDongID = @HopDongID
																	AND DmSanPhamREF = @DmSanPhamREF
																	AND HopDongChiTietREF = @HopDongChiTietID
																	AND NgayThucHien <= @NgayThucHien) 
							PRINT 'sotien hdct'
							PRINT @SoTienConfirm
							PRINT @HopDongID
							PRINT @DmSanPhamREF
							PRINT @TaiKhoanAdmarket
							PRINT @HopDongChiTietID
							PRINT @ThanhTienHDCT

							IF(@SoTienConfirm <=@ThanhTienHDCT)
								BEGIN
									SET @SoTienDieuChinh = @SoTienConfirm - @ThanhTienThucChayDatinhHDCT
									PRINT 'ghinhan'
									SET @ThanhTienThucChayOnline = ISNULL(@ThanhTienThucChayOnline,0)

									PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@SoTienDieuChinh))
									PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienHDCT))
									PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@HopDongChiTietID))
									PRINT CONVERT(nvarchar(100),dbo.FormatNumber(@ThanhTienThucChayOnline))

									--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
									EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
									END
							ELSE
							BEGIN
								IF(@SoTienConfirm > @ThanhTienThucChayDatinhHDCT)
								BEGIN
									IF(@ThanhTienHDCT>= @ThanhTienThucChayDatinhHDCT)
									BEGIN
										SET @SoTienDieuChinh = @ThanhTienHDCT - @ThanhTienThucChayDatinhHDCT
										SET @SoTienConfirm = @SoTienConfirm - @ThanhTienHDCT
										--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
										EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
									END
								END
							END
						END
						--TINH PHAN BIET THOI GIAN
						ELSE
						BEGIN
							PRINT 'TINH PHAN BIET THOI GIAN'
							--XAC DINH SO TIEN TCDT CUA HOPDONGCHITIET
							SET @ThanhTienThucChayDatinhHDCT = (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																	FROM dbo.ThucChayDaTinhAdmarket
																	WHERE HopDongID = @HopDongID
																	AND DmSanPhamREF = @DmSanPhamREF
																	AND HopDongChiTietREF = @HopDongChiTietID AND NgayThucHien BETWEEN @FromDate AND @ToDate) 
							--PHan ghi chu
							SET @ThanhTienThucChayDatinhHDCT =  (SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay
																	FROM dbo.ThucChayDaTinhAdmarket
																	WHERE HopDongID = @HopDongID
																	AND DmSanPhamREF = @DmSanPhamREF
																	AND HopDongChiTietREF = @HopDongChiTietID AND SoLuongDotChayBooking BETWEEN MONTH(@FromDate) AND MONTH(@ToDate)
																) 
							IF(@SoTienConfirm <=@ThanhTienHDCT)
							BEGIN
									SET @SoTienDieuChinh = @SoTienConfirm - @ThanhTienThucChayDatinhHDCT
									--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
									EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
														@NgayThucHien		= @NgayThucHien, 
														@HopDongID			= @HopDongID,
														@HopDongChiTietID	= @HopDongChiTietID, 
														@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
														@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
														@GiaTriThayDoi		= @SoTienDieuChinh, 
														@DmSanPhamREF		= @DmSanPhamREF, 
														@GhiChu				= @ghichu ,
														@Tk					= @TaiKhoanAdmarket
							END
							ELSE
							BEGIN
								IF(@SoTienConfirm > @ThanhTienThucChayDatinhHDCT)
								BEGIN
									IF(@ThanhTienHDCT>= @ThanhTienThucChayDatinhHDCT)
									BEGIN
										SET @SoTienDieuChinh = @ThanhTienHDCT - @ThanhTienThucChayDatinhHDCT
										SET @SoTienConfirm = @SoTienConfirm - @ThanhTienHDCT
										--THUC HIEN CAP NHAT TIEN CHO HOPDONGCHITIET VOI @SoTienDieuChinh
										EXEC [dbo].[ThucChay_InsertGTTDThucChayDaTinhAdmarket_XulyConfirmTcHopDong_GiamGT]
													@NgayThucHien		= @NgayThucHien, 
													@HopDongID			= @HopDongID,
													@HopDongChiTietID	= @HopDongChiTietID, 
													@ThanhTienThucChayOnline = @ThanhTienThucChayOnline,
													@ThanhTienThucChayHopDongChiTiet = @ThanhTienThucChayDatinhHDCT,
													@GiaTriThayDoi		= @SoTienDieuChinh, 
													@DmSanPhamREF		= @DmSanPhamREF, 
													@GhiChu				= @ghichu ,
													@Tk					= @TaiKhoanAdmarket
									END
								END
							END
						END
					END
            END
		END
		ELSE
		BEGIN
			PRINT N'Số tiên confirm lớn hơn thanhtien của hopdong hoặc số tiền confirm lớn hơn ThanhTienThucChayOnline'
			PRINT N'Số tiền confirm: ' + CONVERT(NVARCHAR(100),dbo.FormatNumber(@SoTienConfirm))
			PRINT N'Số Tổng thành tiền:' + CONVERT(NVARCHAR(100),dbo.FormatNumber(@TongThanhTienSanPhamHopDong))
			PRINT N'Số tiền online:' + CONVERT(NVARCHAR(100),dbo.FormatNumber(@ThanhTienThucChayOnline))
			PRINT N'Số tiền thực chạy tài khoản: ' + CONVERT(NVARCHAR(100),dbo.FormatNumber(@ThanhTienThucChayTK))

			SELECT tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienThucChay)ThanhTienThucChay 
			   FROM
					(
							SELECT HopDongID,SoHopDong, HopDongChiTietREF
							, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)ThanhTienThucChay 
							FROM dbo.ThucChayDaTinhAdmarket
							WHERE TrangThaiHopDong <> 3 
							AND DmSanPhamREF = @DmSanPhamREF
							GROUP BY HopDongID, SoHopDong, HopDongChiTietREF
						)tcdt 
						INNER JOIN 
						(	SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
									WHERE DeletedStatus = 0 
									AND TK_AdMarket = @TaiKhoanAdmarket 
									AND DmSanPhamREF = @DmSanPhamREF
						)hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
				GROUP BY tcdt.HopDongID, tcdt.SoHopDong, tcdt.HopDongChiTietREF
		END
	END
	---------
	SELECT 1; 
END



```
