# Stored Procedure: `ThucChay_Exec_GTTD_ThucChayDaTinh_Admatic_Adx_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-08-01 10:30:14.370000
- **Ngày sửa cuối**: 2018-11-07 16:48:00.093000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
/*
EXEC  [dbo].[ThucChay_ExecInsertThucChayDaTinh_Admatic_Adx_BySoHopDong_dev] 1003848,'2018-06-30'
*/
CREATE  PROCEDURE [dbo].[ThucChay_Exec_GTTD_ThucChayDaTinh_Admatic_Adx_BySoHopDong] 
	@HopDongID INT,
	@NgayThucHien DATETIME,
	@GhiChu NVARCHAR(2000)
AS
BEGIN
	DECLARE @username NVARCHAR(500), @contract_number NVARCHAR(100), @domain_name NVARCHAR(500), @domain_id INT
	, @domain_tt_money FLOAT, @domain_tt_promotion FLOAT, @ClickBalance INT, @ClickPromotion INT
	, @ViewBalance INT, @ViewPromotion INT, @banner_id INT, @campaign_id INT, @DmViTriREF INT, @TenViTri NVARCHAR(100), @NhanHangID NVARCHAR(100)
	DECLARE @SoHopDong NVARCHAR(100), @HopDongChiTietID INT, @DmSanPhamREF int, @ThanhTien_HDCT FLOAT, @ThanhTienThucChay FLOAT, @SoLuongThucChay BIGINT
	, @ThanhTienThucChayKM FLOAT, @SoLuongThucChayKM BIGINT, @DonViTinh NVARCHAR(100), @GiaTriLechTreoHa FLOAT = 0
	, @SoLuongLechTreoha BIGINT = 0, @SoLuong INT = 0, @DonViTinh_HDCT NVARCHAR(100) = '', @DonGiaTheoDVT FLOAT = 0, @ThanhTienThucChayDaTinh FLOAT = 0
	, @SoLuongThucChayDaTinh BIGINT = 0
	, @COUNT INT = 0
	SET @DmSanPhamREF = 585

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
	--XAC DINH SO HOP DONG
	SET @SoHopDong = ISNULL((SELECT TOP (1) SoHopDong FROM dbo.HopDong WHERE HopDongID = @HopDongID ORDER BY HopDongID),'')
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
	    CONVERT(FLOAT,ISNULL(tc.domain_tt_money,0))/1.1 AS domain_tt_money,
	    CONVERT(FLOAT,ISNULL(tc.domain_tt_promotion,0))/1.1 AS domain_tt_promotion,
	    CONVERT(INT,ISNULL(tc.ClickBalance,0)) AS ClickBalance,
	    CONVERT(INT,ISNULL(tc.ClickPromotion,0)) AS ClickPromotion,
	    CONVERT(INT,ISNULL(tc.ViewBalance,0)) AS ViewBalance,
	    CONVERT(INT,ISNULL(tc.ViewPromotion,0)) AS ViewPromotion,
	    CONVERT(INT,ISNULL(tc.banner_id,0)) AS banner_id,
	    CONVERT(INT,ISNULL(tc.campaign_id,0)) AS campaign_id,
	    CONVERT(INT,ISNULL(tc.DmSanPhamREF,0)) AS DmSanPhamREF,
	    tc.TenSanPham,
	    CONVERT(INT,tc.DmViTriREF) AS DmViTriREF,
	    tc.TenViTri,
	    tc.NhanHang,
	    tc.NhanHangID,
	    tc.NgayThucHien
	FROM dbo.DataThucChay_Adx tc
	WHERE tc.NgayThucHien = @NgayThucHien
	AND tc.contract_number = @SoHopDong
	
	DECLARE Cursor_AdmaticAdx CURSOR FOR
		--1. Xac dinh thuc chay hop dong Admatic Adx
	SELECT DISTINCT tc.username, tc.contract_number, tc.domain_name, tc.domain_id, tc.domain_tt_money
	, tc.domain_tt_promotion, tc.ClickBalance, tc.ClickPromotion
	, tc.ViewBalance, tc.ViewPromotion, tc.banner_id, tc.campaign_id, tc.DmViTriREF, tc.TenViTri, tc.NhanHangID 
	FROM @DataThucChay_Adx tc
	ORDER BY tc.contract_number, tc.domain_name

	OPEN Cursor_AdmaticAdx
	FETCH NEXT FROM Cursor_AdmaticAdx INTO @username , @contract_number , @domain_name , @domain_id 
	, @domain_tt_money , @domain_tt_promotion , @ClickBalance , @ClickPromotion 
	, @ViewBalance , @ViewPromotion , @banner_id, @campaign_id , @DmViTriREF , @TenViTri , @NhanHangID 
	WHILE @@FETCH_STATUS =0
	BEGIN
		--SET @COUNT = @COUNT +1
		--PRINT @COUNT
		----******CHECK CÓ TỒN TẠI HOPDONGCHITIET CẦN TÍNH THỰC CHẠY*********---------
		IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
				WHERE HopDongFK = @HopDongID 
				AND DmSanPhamREF IN (585,733) 
				AND DmLoaiREF = 42 
				AND DeletedStatus = 0
				AND DmLoaiBannerREF <> 18)
		)
		BEGIN
			--XAC DINH DONGIATHEODONVITINH
			--PRINT 'VAO DAY 1'
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
			----------******1. XAC DINH HOPDONGCHITIET TINH THUC CHAY*****-------------

			SET @HopDongChiTietID =
			ISNULL((
				SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
				INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
				AND att.DmSanPhamREF = tt.DmSanPhamID
				WHERE tt.DmBannerID = CONVERT(NVARCHAR(50),@banner_id)
				AND tt.HopDongREF = @HopDongID
				AND tt.DmSanPhamID = @DmSanPhamREF
				AND tt.DmSanPhamID <> 733
				AND ISNULL(tt.HopDongChiTietREF,0) NOT IN (0,-1)
				AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
					AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
					))
				OR (att.DonViTinhREF = 10))
				ORDER BY tt.HopDongChiTietREF
			),0)
			IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
			BEGIN
				--PRINT 'Xac dinh hop dong chi tiet can tinh thuc chay voi dong gia'
				--PRINT 'VAO DAY 2'
				SET @HopDongChiTietID =
				ISNULL((
					SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
					AND att.DmSanPhamREF = tt.DmSanPhamID
					WHERE att.HopDongFK = @HopDongID
					AND att.trangthaithucchay <> 3
					AND att.DmSanPhamREF = @DmSanPhamREF
					AND ABS(att.DonGia - tt.DonGia_Banner) <1 --cho nay xem lai co anh huong den performance
					AND att.DmSanPhamREF <> 733 --khong phai la san pham "Nhieu san pham"
					AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
						AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
						))
					OR (att.DonViTinhREF = 10))
					AND tt.DmBannerID = CONVERT(NVARCHAR(50),@banner_id)
					ORDER BY att.SoThuTuChay
				),0)
				--PRINT 'hdct: ' + CONVERT(NVARCHAR(100), @HopDongChiTietID)
				IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
				BEGIN
					--PRINT 'VAO DAY 3'
					SET @HopDongChiTietID =
					ISNULL((
					SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
					INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
					WHERE att.HopDongFK = @HopDongID
					AND att.trangthaithucchay <> 3
					AND att.DmSanPhamREF = 733
					AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
						AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
						))
					OR (att.DonViTinhREF = 10))
					AND tt.DmBannerID = CONVERT(NVARCHAR(50),@banner_id)
					ORDER BY att.SoThuTuChay
					),0)

					IF(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
					BEGIN
						--PRINT 'VAO DAY 4'
						SET @HopDongChiTietID =
						ISNULL((
							SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
							INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
							WHERE att.HopDongFK = @HopDongID
							AND (att.DmSanPhamREF = 733 OR att.DmSanPhamREF = @DmSanPhamREF)
							AND att.TrangthaiThucChay <> 3
							AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
								AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
								))
							OR (att.DonViTinhREF = 10))
							AND tt.DmBannerID = CONVERT(NVARCHAR(50),@banner_id)
							ORDER BY att.SoThuTuChay
						),0)
						IF (@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
						BEGIN
							--PRINT 'VAO DAY 5'
							SET @HopDongChiTietID =
							ISNULL((
								SELECT TOP (1) att.HopDongChiTietID FROM dbo.AdmaticThuTuChayHopDongChiTiet att
								INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic tt ON att.HopDongFK = tt.HopDongREF
								WHERE att.HopDongFK = @HopDongID
								AND (att.DmSanPhamREF = 733 OR att.DmSanPhamREF = @DmSanPhamREF)
								AND (((att.DonViTinhREF <> 10) --KHONG PHAI LA GOI
									AND (att.DonViTinh = tt.DonViTinh--CUNG DON VI TINH
									))
								OR (att.DonViTinhREF = 10))
								AND tt.DmBannerID = CONVERT(NVARCHAR(50),@banner_id)
								ORDER BY att.SoThuTuChay
							),0)
							--PRINT @HopDongChiTietID
						END
					END
				END
			END
			----------*************END 1.XAC DINH HOP DONG CHI TIET CAN TINH THUC CHAY
			--PRINT @HopDongChiTietID
			---NEU CO HOP DONG CHI TIET CAN TINH THUC CHAY

			IF NOT(@HopDongChiTietID = 0 OR @HopDongChiTietID = -1)
			BEGIN
			    SET @ThanhTien_HDCT = (SELECT TOP(1) ThanhTien FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
				SET @SoLuong = (SELECT TOP(1) SoLuong FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
				--PRINT @domain_name
				--PRINT @domain_tt_money
				--1.1 NEU HOPDONGCHITIET KHONG LA KHUYEN MAI
				IF(EXISTS(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID AND ChietKhau <> 100))
				BEGIN
					--PRINT 'HOPDONGCHITIET KHONG KHUYEN MAI'
					SET @ThanhTienThucChayKM = 0
					SET @SoLuongThucChayKM = 0
					--THUC HIEN DO TOAN BO SO TIEN DOMAIN_TT_MONEY
					IF(EXISTS(SELECT * FROM dbo.AdmaticThuTuChayHopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID 
						AND (ThanhTien - ThanhtienThucChay) >= ROUND(@domain_tt_money,2)))
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

						EXEC [dbo].[ThucChay_Insert__GTTD_ThucChayDaTinh_Admatic_Adx]
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
								, @GhiChu = @GhiChu
						--UPDATE LAI THANH TIEN THUC CHAY VA THU TU 
						EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
							@NgayThucHien = @NgayThucHien,
							@HopDongChiTietID = @HopDongChiTietID

									
					END
					--GAN DU THANH TIEN
					ELSE
					BEGIN
						--PRINT 'GAN DU THANH TIEN'
					
						SET @ThanhTienThucChayDaTinh = ISNULL((SELECT TOP (1) ThanhtienThucChay FROM dbo.AdmaticThuTuChayHopDongChiTiet 
						WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID) ,0)

						SET @SoLuongThucChayDaTinh = ISNULL((SELECT SUM(SoLuongThucChay) FROM dbo.ThucChayDaTinh 
						WHERE HopDongChiTietREF = @HopDongChiTietID) ,0)

						SET @ThanhTienThucChay = @domain_tt_money
						SET @ThanhTienThucChay = (@ThanhTien_HDCT - @ThanhTienThucChayDaTinh)
						--DONVITINH
						SET @DonViTinh = (SELECT TOP (1) [dbo].[FormatDonViTinh](DonViTinh) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID ORDER BY HopDongChiTietID)
						--SOLUONG THUC CHAY
						IF(@DonViTinh = N'CLICK') SET @SoLuongThucChay = @SoLuong - @SoLuongThucChayDaTinh
						ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongThucChay = @SoLuong*1000 - @SoLuongThucChayDaTinh
						ELSE SET @SoLuongThucChay = @SoLuong - @SoLuongThucChayDaTinh

								
						--NEU CHI CO 01 HOPDONGCHITIET CAN TINH THUC CHAY
						IF(@ThanhTienThucChay = 0 OR @ThanhTienThucChay < @domain_tt_money)
						BEGIN
							SET @GiaTriLechTreoHa = @domain_tt_money - @ThanhTienThucChay
							IF(@DonViTinh = N'CLICK') SET @SoLuongLechTreoha = @ClickBalance - @SoLuongThucChay
							ELSE IF(@DonViTinh = N'VIEW') SET @SoLuongLechTreoha = @ViewBalance  - @SoLuongThucChay
							ELSE SET @SoLuongLechTreoha = @ViewBalance - @SoLuongThucChay
									
						END
						ELSE
						BEGIN
							SET @GiaTriLechTreoHa = 0
							SET @SoLuongLechTreoha = 0
							SET @domain_tt_money = @domain_tt_money - @ThanhTien_HDCT
							IF(@DonViTinh = N'CLICK') SET @ClickBalance = @ClickBalance - @SoLuongThucChay
							ELSE IF(@DonViTinh = N'VIEW') SET @ViewBalance = @ViewBalance  - @SoLuongThucChay
							ELSE SET @ViewBalance = @ViewBalance - @SoLuongThucChay
									
						END
								
						EXEC [dbo].[ThucChay_Insert__GTTD_ThucChayDaTinh_Admatic_Adx]
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
								, @GhiChu = @GhiChu
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
					EXEC [dbo].[ThucChay_Insert__GTTD_ThucChayDaTinh_Admatic_Adx]
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
							, @GhiChu = @GhiChu
					--UPDATE LAI THANH TIEN THUC CHAY VA THU TU 
					EXEC [dbo].[ThucChay_UpdateThucChay_AdmaticHopDongChiTiet] 
						@NgayThucHien = @NgayThucHien,
						@HopDongChiTietID = @HopDongChiTietID
					--THOAT KHOI DANH SACH HOP DONG CHI TIET
							
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
