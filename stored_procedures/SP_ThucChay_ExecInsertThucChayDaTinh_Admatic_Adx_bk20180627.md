# Stored Procedure: `ThucChay_ExecInsertThucChayDaTinh_Admatic_Adx_bk20180627`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-06-27 15:34:40.317000
- **Ngày sửa cuối**: 2018-06-27 15:34:40.317000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_Adx] '2017-09-12'
CREATE  PROCEDURE [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_Adx_bk20180627] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @username NVARCHAR(500), @contract_number NVARCHAR(100), @domain_name NVARCHAR(500), @domain_id INT
	, @domain_tt_money FLOAT, @domain_tt_promotion FLOAT, @ClickBalance INT, @ClickPromotion INT
	, @ViewBalance INT, @ViewPromotion INT, @banner_id INT, @campaign_id INT, @DmViTriREF INT, @TenViTri NVARCHAR(100), @NhanHangID NVARCHAR(100)
	DECLARE @HopDongID INT, @HopDongChiTietID INT, @DmSanPhamREF int, @ThanhTien_HDCT FLOAT, @ThanhTienThucChay FLOAT, @SoLuongThucChay BIGINT
	, @ThanhTienThucChayKM FLOAT, @SoLuongThucChayKM BIGINT, @DonViTinh NVARCHAR(100), @GiaTriLechTreoHa FLOAT = 0
	, @SoLuongLechTreoha BIGINT = 0, @SoLuong INT = 0, @DonViTinh_HDCT NVARCHAR(100) = '', @DonGiaTheoDVT FLOAT = 0

	SET @DmSanPhamREF = 585 --AdX
	DECLARE @DataThucChay_Adx TABLE(
	[username] [NVARCHAR](500) NULL,
	[isnoibo] SMALLINT NULL,
	[contract_number] [NVARCHAR](500) NULL,
	[domain_name] [NVARCHAR](500) NULL,
	[domain_id] INT NULL,
	[domain_tt_money] FLOAT NULL,
	[domain_tt_promotion] FLOAT NULL,
	[ClickBalance] INT NULL,
	[ClickPromotion] INT NULL,
	[ViewBalance] INT NULL,
	[ViewPromotion] INT NULL,
	[banner_id] INT  NULL,
	[campaign_id] INT NULL,
	[DmSanPhamREF] INT NULL,
	[TenSanPham] [NVARCHAR](500) NULL,
	[DmViTriREF] INT NULL,
	[TenViTri] [NVARCHAR](500) NULL,
	[NhanHang] [NVARCHAR](500) NULL,
	[NhanHangID] [NVARCHAR](500) NULL,
	[NgayThucHien] [DATETIME] NULL	
	) 
	--Lay thong tin thuc chay san pham admatic adx

	INSERT INTO @DataThucChay_Adx
	(
	    username,
	    isnoibo,
	    contract_number,
	    domain_name,
	    domain_id,
	    domain_tt_money,
	    domain_tt_promotion,
	    ClickBalance,
	    ClickPromotion,
	    ViewBalance,
	    ViewPromotion,
	    banner_id,
	    campaign_id,
	    DmSanPhamREF,
	    TenSanPham,
	    DmViTriREF,
	    TenViTri,
	    NhanHang,
	    NhanHangID,
	    NgayThucHien
	)
	
	SELECT tc.username,
	    CONVERT(SMALLINT,tc.isnoibo) AS isnoibo,
	    tc.contract_number,
	    tc.domain_name,
	    0 AS domain_id,
	    CONVERT(FLOAT,tc.domain_tt_money)/1.1 AS domain_tt_money,
	    CONVERT(FLOAT,tc.domain_tt_promotion)/1.1 AS domain_tt_promotion,
	    CONVERT(INT,tc.ClickBalance) AS ClickBalance,
	    CONVERT(INT,tc.ClickPromotion) AS ClickPromotion,
	    CONVERT(INT,tc.ViewBalance) AS ViewBalance,
	    CONVERT(INT,tc.ViewPromotion) AS ViewPromotion,
	    CONVERT(INT,tc.banner_id) AS banner_id,
	    CONVERT(INT,tc.campaign_id) AS campaign_id,
	    CONVERT(INT,tc.DmSanPhamREF) AS DmSanPhamREF,
	    tc.TenSanPham,
	    CONVERT(INT,tc.DmViTriREF) AS DmViTriREF,
	    tc.TenViTri,
	    tc.NhanHang,
	    tc.NhanHangID,
	    tc.NgayThucHien
	FROM dbo.DataThucChay_Adx tc
	WHERE tc.NgayThucHien = @NgayThucHien
	
	
	DECLARE Cursor_AdmaticAdx CURSOR FOR
		--1. Xac dinh thuc chay hop dong Admatic Adx
	SELECT DISTINCT tc.username, tc.contract_number, tc.domain_name, tc.domain_id, tc.domain_tt_money
	, tc.domain_tt_promotion, tc.ClickBalance, tc.ClickPromotion
	, tc.ViewBalance, tc.ViewPromotion, tc.banner_id, tc.campaign_id, tc.DmViTriREF, tc.TenViTri, tc.NhanHangID 
	FROM @DataThucChay_Adx tc
	ORDER BY tc.contract_number

	OPEN Cursor_AdmaticAdx
	FETCH NEXT FROM Cursor_AdmaticAdx INTO @username , @contract_number , @domain_name , @domain_id 
	, @domain_tt_money , @domain_tt_promotion , @ClickBalance , @ClickPromotion 
	, @ViewBalance , @ViewPromotion , @banner_id, @campaign_id , @DmViTriREF , @TenViTri , @NhanHangID 
	WHILE @@FETCH_STATUS =0
	BEGIN
		SET @HopDongID = ISNULL((SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @contract_number ORDER BY HopDongID),0)
		--PRINT N'CHECK CÓ TỒN TẠI HOPDONGCHITIET CẦN TÍNH THỰC CHẠY'
		IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
				WHERE HopDongFK = @HopDongID 
				AND DmSanPhamREF IN (585,733) 
				AND DmLoaiREF = 42 
				AND DeletedStatus = 0
				AND DmLoaiBannerREF <> 18)
		)
		BEGIN
			--PRINT N'CHECK TỒN TẠI NHIỀU HOPDONGCHITIET CẦN TÍNH THỰC CHẠY ADMATIC'
			IF(EXISTS(SELECT HopDongFK, COUNT(HopDongChiTietID)sl FROM dbo.HopDongChiTiet 
				WHERE HopDongFK = @HopDongID 
				AND DmSanPhamREF IN (585,733) 
				AND DmLoaiREF = 42 
				AND DeletedStatus = 0
				AND DmLoaiBannerREF <> 18 GROUP BY HopDongFK HAVING COUNT(HopDongChiTietID) >1)
			)
			BEGIN
				--XAC DINH DONGIATHEODONVITINH
				SET @DonGiaTheoDVT = 
				ISNULL((SELECT 
					(CASE when (A.DonViTinh = 'CPM') THEN CONVERT(FLOAT,A.DonGia_Banner)/1000
						ELSE  A.DonGia_Banner --DUNG CHO CA CPC VA TRUE VIEW
						END
					) AS DonGiaBanner 
					FROM dbo.ThucChayHopDongChiTietAndBanner_Admatic A 
					WHERE A.HopDongREF = @HopDongID 
					AND A.DmSanPhamID = @DmSanPhamREF 
					AND A.DmBannerID = @banner_id
				),0)
				----------******XAC DINH HOPDONGCHITIET TINH THUC CHAY*****-------------
				DECLARE Cursor_hdct_AdmaticAdx CURSOR FOR
						SELECT HopDongChiTietID, DmSanPhamREF, ThanhTien, SoLuong, DonViTinh FROM dbo.HopDongChiTiet
						WHERE HopDongFK = @HopDongID 
						AND DmSanPhamREF IN (585,733) 
						AND DmLoaiREF = 42 
						AND DeletedStatus = 0
						AND DmLoaiBannerREF <> 18
						ORDER BY  DmSanPhamREF , HopDongChiTietID

				OPEN Cursor_hdct_AdmaticAdx
				FETCH NEXT FROM Cursor_hdct_AdmaticAdx INTO @HopDongChiTietID, @DmSanPhamREF, @ThanhTien_HDCT, @SoLuong, @DonViTinh_HDCT
			
				WHILE @@FETCH_STATUS =0
				BEGIN
					/*****BEGIN*********/
					--PRINT N'XÁC ĐỊNH HỢP ĐỒNG CHI TIẾT CẦN TÍNH THỰC CHẠY'
					--XAC DINH HOP DONG CO SAN PHAM ADMATIC - ADX VA CO THE DAY THEM TIEN THUC CHAY KHONG?
					--PRINT CONVERT(NVARCHAR(50), @HopDongChiTietID)
					IF(EXISTS(SELECT HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet
					WHERE HopDongChiTietID = @HopDongChiTietID
					AND TrangthaiThucChay <> 3))
					BEGIN
						--NEU KHONG PHAI LA PHAN BO KHUYEN MAI
						IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID AND ChietKhau <> 100))
						BEGIN
						    --PRINT 'HOPDONGCHITIET KHONG KHUYEN MAI'
							SET @ThanhTienThucChayKM = 0
							SET @SoLuongThucChayKM = 0
							--THUC HIEN DO TOAN BO SO TIEN DOMAIN_TT_MONEY
							IF(EXISTS(SELECT * FROM dbo.AdmaticThuTuChayHopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID 
								AND (ThanhTien - ThanhtienThucChay) >= @domain_tt_money))
							BEGIN
								--PRINT 'CHUA DU THANH TIEN'
								SET @ThanhTienThucChay = @domain_tt_money
								--DONVITINH
								SET @DonViTinh = (SELECT TOP (1) [dbo].[FormatDonViTinh](DonViTinh) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
								--SOLUONG THUC CHAY
								IF(@DonViTinh = N'CLICK') SET @SoLuongThucChay = @ClickBalance
								ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongThucChay = @ViewBalance
								ELSE SET @SoLuongThucChay = @ViewBalance

								SET @GiaTriLechTreoHa = 0
								SET @SoLuongLechTreoha = 0

								EXEC [dbo].[ThucChay_Insert_ThucChayDaTinh_Admatic_Adx]
										@NgayThucHien = @NgayThucHien
									  , @HopDongID = @HopDongID
									  , @pHopDongChiTiet = @HopDongChiTietID
									  , @DmBannerREF = @banner_id
									  , @DmCampaign = @campaign_id
									  , @GiaTriThucChay = @ThanhTienThucChay
									  , @GiaTriThucChayKM = 0
									  , @GiaTriLechTreoHa = @GiaTriLechTreoHa
									  , @TongViewThucChay = @ViewBalance
									  , @TongClickThucChay = @ClickBalance
									  , @DmViTriREF = @DmViTriREF
									  , @TenViTri = @TenViTri
									  , @TenWebsite = @domain_name
									  , @DmWebsiteREF = @domain_id
									  , @SoLuongThucChay = @SoLuongThucChay
									  , @SoLuongThucChayKM = @SoLuongThucChayKM
									  , @SoLuongLechTreoha = @SoLuongLechTreoha
									  , @DonViTinh = @DonViTinh
									  , @DonGiaTheoDVT = @DonGiaTheoDVT
								--UPDATE LAI THANH TIEN THUC CHAY VA THU TU 
								EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
									@NgayThucHien = @NgayThucHien,
									@HopDongChiTietID = @HopDongChiTietID

									BREAK;
							END
							--GAN DU THANH TIEN
							ELSE
							BEGIN
							    --THUC HIEN CHI DO PHAN TIEN DU THANHTIEN
								--PRINT 'GAN DU THANH TIEN'
								--GIA TRI THUC CHAY
								SET @ThanhTienThucChay = (@ThanhTien_HDCT - @ThanhtienThucChay)
								--DONVITINH
								SET @DonViTinh = (SELECT TOP (1) [dbo].[FormatDonViTinh](DonViTinh) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
								--SOLUONG THUC CHAY
								IF(@DonViTinh = N'CLICK') SET @SoLuongThucChay = @SoLuong - @ClickBalance
								ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongThucChay = @SoLuong*1000 - @ViewBalance
								ELSE SET @SoLuongThucChay = @SoLuong - @ClickBalance

								
								--NEU CHI CO 01 HOPDONGCHITIET CAN TINH THUC CHAY
								IF(EXISTS(SELECT HopDongFK, COUNT(HopDongChiTietID)sl FROM dbo.AdmaticThuTuChayHopDongChiTiet
									WHERE HopDongFK = @HopDongID 
									AND DmSanPhamREF IN (585,733) 
									AND DmLoaiREF = 42 
									AND DeletedStatus = 0
									AND TrangthaiThucChay <> 3 --Chua chay xong
									AND DmLoaiBannerREF <> 18 GROUP BY HopDongFK HAVING COUNT(HopDongChiTietID) <=1)
								)
								BEGIN
								    SET @GiaTriLechTreoHa = @domain_tt_money - @ThanhTienThucChay
									IF(@DonViTinh = N'CLICK') SET @SoLuongLechTreoha = @ClickBalance - @SoLuongThucChay
									ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongLechTreoha = @ViewBalance  - @SoLuongThucChay
									ELSE SET @SoLuongLechTreoha = @ClickBalance - @SoLuongThucChay
									BREAK;
								END
								ELSE
                                BEGIN
                                    SET @GiaTriLechTreoHa = 0
									SET @SoLuongLechTreoha = 0
									SET @domain_tt_money = @domain_tt_money - @ThanhTien_HDCT
									IF(@DonViTinh = N'CLICK') SET @ClickBalance = @ClickBalance - @SoLuongThucChay
									ELSE IF(@DonViTinh = N'VIEW') SET @ViewBalance = @ViewBalance  - @SoLuongThucChay
									ELSE SET @ClickBalance = @ClickBalance - @SoLuongThucChay
									BREAK;
                                END
								
								EXEC [dbo].[ThucChay_Insert_ThucChayDaTinh_Admatic_Adx]
										@NgayThucHien = @NgayThucHien
									  , @HopDongID = @HopDongID
									  , @pHopDongChiTiet = @HopDongChiTietID
									  , @DmBannerREF = @banner_id
									  , @DmCampaign = @campaign_id
									  , @GiaTriThucChay = @ThanhTienThucChay
									  , @GiaTriThucChayKM = 0
									  , @GiaTriLechTreoHa = @GiaTriLechTreoHa
									  , @TongViewThucChay = @ViewBalance
									  , @TongClickThucChay = @ClickBalance
									  , @DmViTriREF = @DmViTriREF
									  , @TenViTri = @TenViTri
									  , @TenWebsite = @domain_name
									  , @DmWebsiteREF = @domain_id
									  , @SoLuongThucChay = @SoLuongThucChay
									  , @SoLuongThucChayKM = @SoLuongThucChayKM
									  , @SoLuongLechTreoha = @SoLuongLechTreoha
									  , @DonViTinh = @DonViTinh
									  , @DonGiaTheoDVT = @DonGiaTheoDVT
								--UPDATE LAI THANH TIEN THUC CHAY VA THU TU 
								EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
									@NgayThucHien = @NgayThucHien,
									@HopDongChiTietID = @HopDongChiTietID
							END
						END
						ELSE
						BEGIN
						    --PRINT N'HOPDONGCHITIET KHUYEN MAI'
							--GIA TRI THUC CHAY
							SET @SoLuongThucChay = 0
							SET @ThanhTienThucChay = 0

							SET  @ThanhTienThucChayKM = @domain_tt_promotion
							--DONVITINH
							SET @DonViTinh = (SELECT TOP (1) [dbo].[FormatDonViTinh](DonViTinh) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
							--SOLUONG THUC CHAY
							IF(@DonViTinh = N'CLICK') SET @SoLuongThucChayKM = @ClickPromotion
							ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongThucChayKM = @ViewPromotion
							ELSE SET @SoLuongThucChayKM = @ViewPromotion

							SET @ThanhTienThucChay = 0
							SET @SoLuongThucChay = 0
							SET @GiaTriLechTreoHa = 0
							SET @SoLuongLechTreoha = 0
							EXEC [dbo].[ThucChay_Insert_ThucChayDaTinh_Admatic_Adx]
									@NgayThucHien = @NgayThucHien
									, @HopDongID = @HopDongID
									, @pHopDongChiTiet = @HopDongChiTietID
									, @DmBannerREF = @banner_id
									, @DmCampaign = @campaign_id
									, @GiaTriThucChay = @ThanhTienThucChay
									, @GiaTriThucChayKM = 0
									, @GiaTriLechTreoHa = @GiaTriLechTreoHa
									, @TongViewThucChay = @ViewBalance
									, @TongClickThucChay = @ClickBalance
									, @DmViTriREF = @DmViTriREF
									, @TenViTri = @TenViTri
									, @TenWebsite = @domain_name
									, @DmWebsiteREF = @domain_id
									, @SoLuongThucChay = @SoLuongThucChay
									, @SoLuongThucChayKM = @SoLuongThucChayKM
									, @SoLuongLechTreoha = @SoLuongLechTreoha
									, @DonViTinh = @DonViTinh
									, @DonGiaTheoDVT = @DonGiaTheoDVT
							--UPDATE LAI THANH TIEN THUC CHAY VA THU TU 
							EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
								@NgayThucHien = @NgayThucHien,
								@HopDongChiTietID = @HopDongChiTietID
							--THOAT KHOI DANH SACH HOP DONG CHI TIET
							BREAK;
						END
					   
					END
					/*****END*********/
				FETCH NEXT FROM Cursor_hdct_AdmaticAdx INTO @HopDongChiTietID, @DmSanPhamREF, @ThanhTien_HDCT, @SoLuong, @DonViTinh_HDCT			
				END
				CLOSE Cursor_hdct_AdmaticAdx;
				DEALLOCATE Cursor_hdct_AdmaticAdx;
				-------------*******************************************----------------
			END
			ELSE
			BEGIN
			    --PRINT N'CÓ 01 HOPDONGCHITIET CẦN XÁC ĐỊNH'
				--NEU KHONG PHAI LA PHAN BO KHUYEN MAI
				--XAC DINH THONG TIN HOPDONGCHITIET CAN TINH THUC CHAY
				SELECT TOP (1) @HopDongChiTietID = HopDongChiTietID, @DmSanPhamREF = DmSanPhamREF, @ThanhTien_HDCT = ThanhTien
				,@SoLuong = SoLuong, @DonViTinh = DonViTinh 
				FROM dbo.HopDongChiTiet
				WHERE HopDongFK = @HopDongID 
				AND DmSanPhamREF IN (585,733) 
				AND DmLoaiREF = 42 
				AND DeletedStatus = 0
				AND DmLoaiBannerREF <> 18
				ORDER BY  DmSanPhamREF , HopDongChiTietID

				SET @SoLuongThucChayKM = 0
				SET @ThanhTienThucChayKM = 0

				IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID AND ChietKhau <> 100))
				BEGIN
					--PRINT 'HOPDONGCHITIET KHONG KHUYEN MAI'
					--THUC HIEN DO TOAN BO SO TIEN DOMAIN_TT_MONEY
					IF(EXISTS(SELECT * FROM dbo.AdmaticThuTuChayHopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID 
						AND (ThanhTien - ThanhtienThucChay) >= @domain_tt_money))
					BEGIN
						--PRINT 'CHUA DU THANH TIEN'
						--GIA TRI THUC CHAY
						SET @ThanhTienThucChay = @domain_tt_money
						--DONVITINH
						SET @DonViTinh = (SELECT TOP (1) [dbo].[FormatDonViTinh](DonViTinh) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
						--SOLUONG THUC CHAY
						IF(@DonViTinh = N'CLICK') SET @SoLuongThucChay = @ClickBalance
						ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongThucChay = @ViewBalance
						ELSE SET @SoLuongThucChay = @ViewBalance

						SET @GiaTriLechTreoHa = 0
						SET @SoLuongLechTreoha = 0
						EXEC [dbo].[ThucChay_Insert_ThucChayDaTinh_Admatic_Adx]
								@NgayThucHien = @NgayThucHien
								, @HopDongID = @HopDongID
								, @pHopDongChiTiet = @HopDongChiTietID
								, @DmBannerREF = @banner_id
								, @DmCampaign = @campaign_id
								, @GiaTriThucChay = @ThanhTienThucChay
								, @GiaTriThucChayKM = 0
								, @GiaTriLechTreoHa = @GiaTriLechTreoHa
								, @TongViewThucChay = @ViewBalance
								, @TongClickThucChay = @ClickBalance
								, @DmViTriREF = @DmViTriREF
								, @TenViTri = @TenViTri
								, @TenWebsite = @domain_name
								, @DmWebsiteREF = @domain_id
								, @SoLuongThucChay = @SoLuongThucChay
								, @SoLuongThucChayKM = @SoLuongThucChayKM
								, @SoLuongLechTreoha = @SoLuongLechTreoha
								, @DonViTinh = @DonViTinh
								, @DonGiaTheoDVT = @DonGiaTheoDVT
						--UPDATE LAI THANH TIEN THUC CHAY VA THU TU 
						EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
							@NgayThucHien = @NgayThucHien,
							@HopDongChiTietID = @HopDongChiTietID
					END
					--GAN DU THANH TIEN
					ELSE
					BEGIN
						--THUC HIEN CHI DO PHAN TIEN DU THANHTIEN
						--PRINT 'GAN DU THANH TIEN'
						--GIA TRI THUC CHAY
						SET @ThanhTienThucChay = (@ThanhTien_HDCT - @ThanhtienThucChay)
						--DONVITINH
						SET @DonViTinh = (SELECT TOP (1) [dbo].[FormatDonViTinh](DonViTinh) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
						--SOLUONG THUC CHAY
						IF(@DonViTinh = N'CLICK') SET @SoLuongThucChay = @SoLuong - @ClickBalance
						ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongThucChay = @SoLuong*1000 - @ViewBalance
						ELSE SET @SoLuongThucChay = @SoLuong - @ClickBalance

						SET @GiaTriLechTreoHa = 0
						SET @SoLuongLechTreoha = 0
						--NEU CHI CO 01 HOPDONGCHITIET CAN TINH THUC CHAY
						IF(EXISTS(SELECT HopDongFK, COUNT(HopDongChiTietID)sl FROM dbo.AdmaticThuTuChayHopDongChiTiet
							WHERE HopDongFK = @HopDongID 
							AND DmSanPhamREF IN (585,733) 
							AND DmLoaiREF = 42 
							AND DeletedStatus = 0
							AND TrangthaiThucChay <> 3 --Chua chay xong
							AND DmLoaiBannerREF <> 18 GROUP BY HopDongFK HAVING COUNT(HopDongChiTietID) <=1)
						)
						BEGIN
							SET @GiaTriLechTreoHa = @domain_tt_money - @ThanhTienThucChay
							IF(@DonViTinh = N'CLICK') SET @SoLuongLechTreoha = @ClickBalance - @SoLuongThucChay
							ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongLechTreoha = @ViewBalance  - @SoLuongThucChay
							ELSE SET @SoLuongLechTreoha = @ClickBalance - @SoLuongThucChay
						END
								
						EXEC [dbo].[ThucChay_Insert_ThucChayDaTinh_Admatic_Adx]
								@NgayThucHien = @NgayThucHien
								, @HopDongID = @HopDongID
								, @pHopDongChiTiet = @HopDongChiTietID
								, @DmBannerREF = @banner_id
								, @DmCampaign = @campaign_id
								, @GiaTriThucChay = @ThanhTienThucChay
								, @GiaTriThucChayKM = 0
								, @GiaTriLechTreoHa = @GiaTriLechTreoHa
								, @TongViewThucChay = @ViewBalance
								, @TongClickThucChay = @ClickBalance
								, @DmViTriREF = @DmViTriREF
								, @TenViTri = @TenViTri
								, @TenWebsite = @domain_name
								, @DmWebsiteREF = @domain_id
								, @SoLuongThucChay = @SoLuongThucChay
								, @SoLuongThucChayKM = @SoLuongThucChayKM
								, @SoLuongLechTreoha = @SoLuongLechTreoha
								, @DonViTinh = @DonViTinh
								, @DonGiaTheoDVT = @DonGiaTheoDVT
						--UPDATE LAI THANH TIEN THUC CHAY VA THU TU 
						EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
							@NgayThucHien = @NgayThucHien,
							@HopDongChiTietID = @HopDongChiTietID
					END
				END
				ELSE
				BEGIN
					--PRINT N'HOPDONGCHITIET KHUYEN MAI'
					--GIA TRI THUC CHAY
					SET  @ThanhTienThucChayKM = @domain_tt_promotion
					--DONVITINH
					SET @DonViTinh = (SELECT TOP (1) [dbo].[FormatDonViTinh](DonViTinh) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
					--SOLUONG THUC CHAY
					IF(@DonViTinh = N'CLICK') SET @SoLuongThucChayKM = @ClickPromotion
					ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongThucChayKM = @ViewPromotion
					ELSE SET @SoLuongThucChayKM = @ViewPromotion

					SET @ThanhTienThucChay = 0
					SET @SoLuongThucChay = 0
					SET @GiaTriLechTreoHa = 0
					SET @SoLuongLechTreoha = 0
					EXEC [dbo].[ThucChay_Insert_ThucChayDaTinh_Admatic_Adx]
							@NgayThucHien = @NgayThucHien
							, @HopDongID = @HopDongID
							, @pHopDongChiTiet = @HopDongChiTietID
							, @DmBannerREF = @banner_id
							, @DmCampaign = @campaign_id
							, @GiaTriThucChay = @ThanhTienThucChay
							, @GiaTriThucChayKM = 0
							, @GiaTriLechTreoHa = @GiaTriLechTreoHa
							, @TongViewThucChay = @ViewBalance
							, @TongClickThucChay = @ClickBalance
							, @DmViTriREF = @DmViTriREF
							, @TenViTri = @TenViTri
							, @TenWebsite = @domain_name
							, @DmWebsiteREF = @domain_id
							, @SoLuongThucChay = @SoLuongThucChay
							, @SoLuongThucChayKM = @SoLuongThucChayKM
							, @SoLuongLechTreoha = @SoLuongLechTreoha
							, @DonViTinh = @DonViTinh
							, @DonGiaTheoDVT = @DonGiaTheoDVT
					--UPDATE LAI THANH TIEN THUC CHAY VA THU TU 
					EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
						@NgayThucHien = @NgayThucHien,
						@HopDongChiTietID = @HopDongChiTietID
				END
			END
		END
	FETCH NEXT FROM Cursor_AdmaticAdx INTO @username , @contract_number , @domain_name , @domain_id 
	, @domain_tt_money , @domain_tt_promotion , @ClickBalance , @ClickPromotion 
	, @ViewBalance , @ViewPromotion , @banner_id, @campaign_id , @DmViTriREF , @TenViTri , @NhanHangID 
	END
	CLOSE Cursor_AdmaticAdx;
	DEALLOCATE Cursor_AdmaticAdx;
	
	--SELECT 1;
END

```
