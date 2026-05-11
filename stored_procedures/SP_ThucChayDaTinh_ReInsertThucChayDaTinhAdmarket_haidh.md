# Stored Procedure: `ThucChayDaTinh_ReInsertThucChayDaTinhAdmarket_haidh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:03.687000
- **Ngày sửa cuối**: 2015-06-10 16:07:03.687000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@UserName` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-09
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.ThucChayDaTinh_ReInsertThucChayDaTinhAdmarket 
		'2015-01-06', 
		144, 
		'djbuonvn', 
		'CLICK',
		'Admarket_Chay_Lai_Du_Lieu',
		'1',
		''
	
*/
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_ReInsertThucChayDaTinhAdmarket_haidh] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME,
	@DmSanPhamREF	INT,
	@UserName		NVARCHAR(50),
	@DonViTinh		NVARCHAR(50),
	@GhiChu			NVARCHAR(255),
	@DmViTriREF		INT,
	@TenViTri		NVARCHAR(50)
AS
BEGIN
	DECLARE @PhanBoId			INT = 0,
			@DonViTinhPhanBo	NVARCHAR(20),
			@ChietKhauPhanBo	INT,
			@DonGiaPhanBo		INT,
			@DonGiaPhanBoSauCK	INT,
			@TypeInsert			INT
	
	DECLARE @SoLuongThucChaySanPham		INT,
			@SoLuongThucChayKMSanPham	INT,
			@TongViewThucChay			INT,
			@TongClickThucChay			INT,
			@ThanhTienThucChaySanPham	FLOAT,
			@ThanhTienThucChayKMSanPham	FLOAT,
			@DonGiaSanPham				INT,
			@DonViTinhSanPham			NVARCHAR(50),
			@IsNoiBo					INT = 0
						
	DECLARE @SoLuongThucChayPhanBo		INT,
			@ThanhTienThucChayPhanBo	FLOAT,
			@SoLuongPhanBo				INT,
			@ThanhTienPhanBo			FLOAT,
			@SoLuongKMPhanBo			INT,
			@ThanhTienKMPhanBo			FLOAT,
			@TenSanPham					NVARCHAR(50),
			@TenWebsite					NVARCHAR(50),
			@HopDongID					INT,
			@SoHopDong					NVARCHAR(50),
			@IsHopDongNoiBo				INT			
	
	DECLARE @SoLuongThucChay			INT,
			@ThanhTienThucChay			FLOAT,
			@ThanhTienThucChayTruocCK	FLOAT,
			@SoLuongThucChayKM			INT,
			@ThanhTienThucChayKM		FLOAT,
			@SoLuongLechTreoHa			INT,
			@ThanhTienLechTreoHa		FLOAT,
			@SoLuongThucChayKMPhanBo	INT,
			@ThanhTienThucChayKMPhanBo	FLOAT;
			
	DECLARE @ThanhTienHopDong			FLOAT = 0,
			@ThanhTienThucChayHopDong	FLOAT = 0,
			@ThanhTienThucChayHopDongNew	FLOAT = 0

	DECLARE @TotalViewOnline			INT = 0,
			@TotalClickOnline			INT = 0,
			@SoLuongThucChayOnline		INT = 0,
			@ThanhTienThucChayOnline	FLOAT = 0,
			@ThanhTienKMOnline			FLOAT = 0
			
	DECLARE @NgayGioiHanTinh			DATETIME = '2013-01-01',
			@UserBalance			FLOAT = 0,
			@IsMultileSale				INT = 0,
			@MaxValue					FLOAT,
			@SoNgayToiHanCanhBao		INT = 0,
			@SoNgayChayTruocTienVe		INT = 0,
			@IsTinhThucChay				INT = 0
			
	SELECT 
		@SoLuongThucChay = 0,
		@SoLuongThucChayKM = 0,
		@SoLuongLechTreoHa = 0,
		@ThanhTienThucChay = 0,
		@ThanhTienThucChayKM = 0,
		@ThanhTienLechTreoHa = 0									
		
	SET @DonViTinhSanPham = @DonViTinh;

	IF @DmSanPhamREF = 585
	BEGIN
		SET @IsNoiBo = (
			SELECT IsNoiBo
			FROM ThucChayAdXForUsers
			WHERE username = @UserName
				AND DmSanPhamREF = @DmSanPhamREF
				AND NgayThucHien = @NgayThucHien
				AND DmViTriREF = @DmViTriREF
		)
	END
	
	ELSE IF @DmSanPhamREF = 628
	BEGIN
		SET @IsNoiBo = (
			SELECT IsNoiBo
			FROM ThucChayViewPlusForUsers
			WHERE username = @UserName
				AND DmSanPhamREF = @DmSanPhamREF
				AND NgayThucHien = @NgayThucHien				
		)
	END
	ELSE
		SET @IsNoiBo = (
			SELECT IsNoiBo
			FROM ThucChayAdmarketUsers
			WHERE username = @UserName
				AND DmSanPhamREF = @DmSanPhamREF
				AND NgayThucHien = @NgayThucHien				
		)
	
	SET @IsNoiBo = ISNULL(@IsNoiBo,0);
		
	SELECT DISTINCT
		@SoHopDong = hd.SoHopDong
	FROM HopDongChiTiet AS hdct
		INNER JOIN HopDong AS hd ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN ThucChaySelfServingUsers AS tcau ON hdct.TK_AdMarket = tcau.username
	WHERE 
		tcau.NgayThucHien = @NgayThucHien
		AND hd.NgayDanhSoHopDong <= @NgayThucHien
		AND tcau.username = @UserName
		AND hd.TrangThaiHopDong <> 3
		AND hdct.DeletedStatus = 0
		AND hdct.DmSanPhamREF = @DmSanPhamREF
		
	IF (CHARINDEX('NB',@SoHopDong) > 0 OR CHARINDEX('SH',@SoHopDong) > 0)
		SET @IsHopDongNoiBo = 1
	ELSE
		SET @IsHopDongNoiBo = 0
	
	-- select so luong, thanh tien thuc chay tu du lieu cua san pham
	SET @SoLuongThucChaySanPham = (
		SELECT CASE A.DonViTinh
					WHEN 'VIEW' THEN SUM(A.ttv)
					ELSE SUM(A.ttc)
		       END
		FROM ThucChaySelfServingUsers A
		WHERE A.NgayThucHien	= @NgayThucHien
			AND A.DmSanPhamREF	= @DmSanPhamREF
			AND A.username		= @UserName	
			AND A.DonViTinh		= @DonViTinh
			AND A.DmViTriREF	= @DmViTriREF
		GROUP BY A.DmSanPhamREF, A.DonViTinh	   	
	);
	
	SELECT	@TongViewThucChay = SUM(A.ttv),
			@TongClickThucChay = SUM(A.ttc)
	FROM ThucChaySelfServingUsers A
	WHERE A.NgayThucHien	= @NgayThucHien
		AND A.DmSanPhamREF	= @DmSanPhamREF
		AND A.username		= @UserName
		AND A.DonViTinh		= @DonViTinh
		AND A.DmViTriREF	= @DmViTriREF;
	
	-- Thanh tien thuc chay truoc vat
	SELECT 
		@ThanhTienThucChaySanPham = SUM(ThanhTien),
		@ThanhTienThucChayKMSanPham = SUM(T.pro)
	FROM
	(
		SELECT 
			CASE A.IsNoiBo 
				WHEN 0 THEN (A.[money]/1.1)
				ELSE ((A.[money]/1.1) + (A.pro/1.1))
			END AS ThanhTien,
			CASE A.IsNoiBo
				WHEN 0 THEN (A.pro/1.1)
				ELSE 0
			END pro								  
		FROM ThucChaySelfServingUsers A
		WHERE A.NgayThucHien	= @NgayThucHien
			AND A.DmSanPhamREF	= @DmSanPhamREF
			AND A.username		= @UserName
			AND A.DonViTinh		= @DonViTinh
			AND A.DmViTriREF	= @DmViTriREF
	)T
	
	PRINT 'username: ' + CONVERT(NVARCHAR(50), @UserName);
	PRINT 'DonViTinh: ' + CONVERT(NVARCHAR(50), @DonViTinh);
	PRINT '@DmViTriREF: ' + CONVERT(NVARCHAR(50), @DmViTriREF);
	PRINT '@SoLuongThucChaySanPham: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySanPham);
	PRINT '@ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
	PRINT '@ThanhTienThucChayKMSanPham: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayKMSanPham);
	
	DECLARE tc_cursor CURSOR FOR
	
	SELECT DISTINCT
		hdct.HopDongFK, hd.SoHopDong, hdct.HopDongChiTietID, hdct.TenSanPham, hdct.SoLuong, hdct.DonViTinh, hdct.ThanhTien
	FROM HopDongChiTiet AS hdct
		INNER JOIN HopDong AS hd ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN ThucChaySelfServingUsers AS tcau ON hdct.TK_AdMarket = tcau.username
	WHERE 
		tcau.NgayThucHien					= @NgayThucHien
		--AND hd.NgayDanhSoHopDong	<= @NgayThucHien
		AND CONVERT(DATE, hdct.CreatedAt)	<= @NgayThucHien
		AND hdct.CreatedAt					>= @NgayGioiHanTinh
		AND tcau.username					= @UserName
		AND tcau.DonViTinh					= @DonViTinh
		AND hd.TrangThaiHopDong				<> 3
		AND hdct.DeletedStatus				= 0
		AND hdct.DmSanPhamREF				= @DmSanPhamREF
		AND hdct.IsKhuyenMai				<> 1
	ORDER BY
		hdct.HopDongChiTietID
	
	OPEN tc_cursor
	
	FETCH NEXT FROM tc_cursor INTO @HopDongID, @SoHopDong, @PhanBoId, @TenSanPham, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienPhanBo
	WHILE @@FETCH_STATUS = 0
	BEGIN
		--SELECT @HopDongID, @PhanBoId, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienPhanBo	
		PRINT '@ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
		
		PRINT '@IsHopDongNoiBo: ' + CONVERT(NVARCHAR(50), @IsHopDongNoiBo);
		PRINT '@PhanBoId: ' + CONVERT(NVARCHAR(50), @PhanBoId);
		
		--PRINT '@SoLuongPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBo);
		--PRINT '@ThanhTienPhanBo: ' + CONVERT(NVARCHAR(50), @ThanhTienPhanBo);
		
		SET @UserBalance = dbo.ThucChayAdmarket_GetAdmarketBalanceUserDaily_UserBalance(@UserName,@NgayThucHien, @DmSanPhamREF)
		PRINT '@UserBalance: ' + CONVERT(NVARCHAR(50), @UserBalance);
		
		IF ((@UserBalance <> 0) AND (@UserBalance >= @ThanhTienThucChaySanPham))
		BEGIN
			IF @ThanhTienThucChaySanPham > @ThanhTienPhanBo
				SET @MaxValue = @ThanhTienPhanBo; --CHO NAY CAN PHAI XEM LAI???
			ELSE
				SET @MaxValue = @ThanhTienThucChaySanPham;
			SET @IsTinhThucChay = 1;
				
			PRINT '@@MaxValue: ' + CONVERT(NVARCHAR(50), @MaxValue);
		END
		ELSE
		BEGIN
			-- Check xem du lieu canh bao da toi han chua
			SET @SoNgayToiHanCanhBao = dbo.fn_GetSoNgayDuocPhepChayThauChi()
			
			SELECT 
				@SoNgayChayTruocTienVe = ISNULL((DATEDIFF(d,MIN(NgayThucHien), MAX(NgayThucHien)) + 1), 0)
			FROM HopDongAdmarketCanhBao
			WHERE 1 = 1
				AND HopDongID = @HopDongID
				AND HopDongChiTietID = @PhanBoId
				AND RecordStatus = 0
				AND NgayThucHien <= @NgayThucHien				
				
			IF @SoNgayChayTruocTienVe < @SoNgayToiHanCanhBao
			BEGIN
				SET @IsTinhThucChay = 1;
				
				IF NOT EXISTS(SELECT HopDongID FROM HopDongAdmarketCanhBao AS hdacb 
				              WHERE hdacb.HopDongID = @HopDongID
								AND hdacb.HopDongChiTietID = @PhanBoId
								AND hdacb.NgayThucHien = @NgayThucHien)
				BEGIN
					PRINT 'account: ' + @UserName
					INSERT INTO HopDongAdmarketCanhBao(
						HopDongAdmarketCanhBaoID, HopDongID, SoHopDong, HopDongChiTietID, DmSanPhamREF, TenSanPham,
						TK_Admarket, DmViTriREF, TenViTri,
						SaleID, UserNameSale, TenSale,
						NgayThucHien, CreatedAt, CreatedBy, LastModifiedAt, LastModifiedBy, RecordStatus)
					VALUES(
						NEWID(), @HopDongID, @SoHopDong, @PhanBoId, @DmSanPhamREF, @TenSanPham, @UserName, @DmViTriREF, @TenViTri,
						(SELECT hd.SysNhanVienREF FROM HopDong AS hd WHERE hd.HopDongID = @HopDongID),
						(SELECT hd.TenDangNhap FROM HopDong AS hd WHERE hd.HopDongID = @HopDongID),
						(SELECT hd.TenNhanVien FROM HopDong AS hd WHERE hd.HopDongID = @HopDongID),
						@NgayThucHien, GETDATE(), 'asd', GETDATE(), 'asd', 0)
				END
			END	
			ELSE
			BEGIN
				SET @IsTinhThucChay = 0;
			END
			
		END
		
		IF (@IsTinhThucChay = 1 AND (@ThanhTienThucChaySanPham > 0 OR @SoLuongThucChaySanPham > 0))
		BEGIN	
			-- Select thanh tien thuc chay theo hop dong
			SELECT 
				@ThanhTienThucChayHopDong = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
			FROM ThucChayDaTinhAdmarket AS tcdta
			WHERE 1=1
				AND tcdta.HopDongID			= @HopDongID
				AND tcdta.DmSanPhamREF		= @DmSanPhamREF
				AND tcdta.NgayThucHien		<= @NgayThucHien
				AND tcdta.TrangThaiHopDong	<> 3
			
			-- Select gia tri hop dong theo san pham	
			SELECT @ThanhTienHopDong = SUM(ThanhTien)
			FROM HopDongChiTiet AS hdct
			WHERE 1=1
				AND hdct.HopDongFK		= @HopDongID
				AND hdct.DeletedStatus	= 0
				AND hdct.DmSanPhamREF	= @DmSanPhamREF
				AND hdct.IsKhuyenMai	<> 1
				
			PRINT '@@ThanhTienThucChayHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayHopDong);
			PRINT '@@ThanhTienHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienHopDong);
			
			-- Check thanh tien thuc chay tich luy so voi thanh tien phan bo
			SET @SoLuongThucChayPhanBo = 0;
			SET @ThanhTienThucChayPhanBo = 0;
			
			IF EXISTS(SELECT HopDongChiTietREF 
			          FROM ThucChayDaTinhAdmarket AS tcdt 
			          WHERE tcdt.HopDongChiTietREF = @PhanBoId
							AND tcdt.NgayThucHien <= @NgayThucHien)
			BEGIN
				-- select soluong, thanh tien thuc chay tich luy theo phan bo
				SELECT 
					@SoLuongThucChayPhanBo = SUM(A.SoLuongThucChay),
					@ThanhTienThucChayPhanBo = SUM(A.ThanhTienSauTrietKhauThucChay + A.GiaTriThayDoi)
				FROM ThucChayDaTinhAdmarket A
				WHERE
					A.HopDongChiTietREF	= @PhanBoId
					AND A.DmSanPhamREF	= @DmSanPhamREF
					AND A.HopDongID		= @HopDongID
					AND A.NgayThucHien	<= @NgayThucHien
			END
			
			PRINT '@SoLuongThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayPhanBo);
			PRINT '@ThanhTienThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayPhanBo);
			
			PRINT '@SoLuongPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBo);
			PRINT '@ThanhTienPhanBo: ' + CONVERT(NVARCHAR(50), @ThanhTienPhanBo);
			PRINT '@@MaxValue: ' + CONVERT(NVARCHAR(50), @MaxValue);
			
			-- Check neu Thanh tien thuc chay theo phan bo so voi Thanh tien tren phan bo hop dong	
			-- Neu thanh tien thuc chay theo phan bo chua vuot gia tri phan bo
			IF @ThanhTienThucChayPhanBo < @ThanhTienPhanBo
			BEGIN
				-- Neu thanh tien thuc chay theo phan bo chua vuot gia tri phan bo
				IF @ThanhTienThucChayPhanBo + @ThanhTienThucChaySanPham > @MaxValue
				BEGIN
					SET @ThanhTienThucChay = (@MaxValue - @ThanhTienThucChayPhanBo);
				END
				ELSE
				BEGIN
					SET @ThanhTienThucChay = @ThanhTienThucChaySanPham;
				END
			END	
			ELSE
				SET @ThanhTienThucChay = 0;	
			
			-- Thanh tien thuc chay theo hop dong sau khi duoc tinh thuc chay
			SET @ThanhTienThucChayHopDongNew = (@ThanhTienThucChayHopDong + @ThanhTienThucChay)
			
			PRINT '@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay);
			PRINT '@@ThanhTienThucChayHopDongNew: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayHopDongNew);
			
			-- Neu thanh tien thuc chay vuot gia tri hop dong (Xy ly cho truong hop hop dong duoc up date gia tri thuc chay 1 lan phuc vu kiem toan nam 2013)
			IF (@ThanhTienThucChayHopDongNew > @ThanhTienHopDong)
			BEGIN
				SET @ThanhTienThucChay = (@ThanhTienHopDong - @ThanhTienThucChayHopDong)
			END
			
			------------------------------
			IF ROUND(@ThanhTienThucChay,0) >= 1
			BEGIN
				SET @ThanhTienThucChay = @ThanhTienThucChay
			END
			ELSE
			BEGIN
				SET @ThanhTienThucChay = 0;
			END
			
			IF ROUND(@ThanhTienThucChay,0) >= 1
			BEGIN
				PRINT '@DonViTinhPhanBo: ' + CONVERT(NVARCHAR(50), @DonViTinhPhanBo);
				IF @DonViTinhPhanBo = 'CPM'
					SET @SoLuongPhanBo = @SoLuongPhanBo*1000; -- 1CPM = 1000 View
				
				-- Chi thuc hien viec chan so luong thuc chay khi don vi tinh la CPC hoac CPM
				IF (@DonViTinhPhanBo = 'CPC' OR @DonViTinhPhanBo = 'CPM')
				BEGIN
					IF @SoLuongThucChayPhanBo < @SoLuongPhanBo
					BEGIN	
						IF @SoLuongThucChayPhanBo + @SoLuongThucChaySanPham > @SoLuongPhanBo
						BEGIN
							SET @SoLuongThucChay = (@SoLuongPhanBo - @SoLuongThucChayPhanBo);
						END
						ELSE
						BEGIN
							SET @SoLuongThucChay = @SoLuongThucChaySanPham;
						END						                                          									                                         	
					END	
					ELSE
					BEGIN
						SET @SoLuongThucChay = 0;
						--SET @SoLuongLechTreoHa = (@SoLuongThucChaySanPham - @SoLuongThucChay);
					END
				END	
				ELSE
				BEGIN
					SET @SoLuongThucChay = @SoLuongThucChaySanPham;
				END
			END
			ELSE
			BEGIN
				SET @SoLuongThucChay = 0
			END
			PRINT '@SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay);
			PRINT '@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay);
				
			-- insert gia tri thay doi
			IF (@SoLuongThucChay > 0 OR @ThanhTienThucChay > 0)
			EXEC dbo.ThucChayDaTinhAdmarket_InsertGiaTriThayDoiByPhanBoID
				@NgayThucHien
				,@SoHopDong
				,@PhanBoID
				,@DmSanPhamREF
				,@TenSanPham
				,0 --@DmWebsiteREF
				,'' --@TenWebsite
				,@TongViewThucChay
				,@TongClickThucChay
				,@SoLuongThucChay
				,@ThanhTienThucChay
				,@SoLuongThucChayKM
				,@ThanhTienThucChayKM
				,@SoLuongLechTreoHa
				,@ThanhTienLechTreoHa
				,@TypeInsert
				,@DonViTinhSanPham
				,@GhiChu
				,@DmViTriREF
				,@TenViTri

			/*
			* Update gia tri thay doi cho hop dong online
			*/	
			IF (@IsHopDongNoiBo =  0)
			BEGIN
			UPDATE ThucChayDaTinhAdmarket
				SET GiaTriThayDoi = (GiaTriThayDoi + (0 - @ThanhTienThucChay)),
				GhiChu = 'Bo_Sung_Du_Lieu_Cho_HD'
			WHERE HopDongID = 0
				AND DmMaHopDongREF = 0
				AND NgayThucHien = @NgayThucHien
				AND DmSanPhamREF = @DmSanPhamREF
				AND DmViTriREF	 = @DmViTriREF
			END
			ELSE
			BEGIN
				UPDATE ThucChayDaTinhAdmarket
				SET GiaTriThayDoi = (GiaTriThayDoi + (0 - @ThanhTienThucChay))
				WHERE HopDongID = 0
					AND DmMaHopDongREF = 310
					AND NgayThucHien = @NgayThucHien
					AND DmSanPhamREF = @DmSanPhamREF
					AND DmViTriREF	 = @DmViTriREF
			END

			/*
			* Insert Log gttd
			*/		
			DECLARE @NoiDungLog NVARCHAR(255) = N'Chạy bổ sung dữ liệu';	
			EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
				@HopDongID
				,@SoHopDong
				,@PhanBoId
				,@DmSanPhamREF
				,0
				,@NgayThucHien
				,0
				,0
				,0
				,0
				,0
				,@NoiDungLog
				,'HopDongChiTiet_Admarket_ChayLaiDuLieu'
				,''	
						
			SET @SoLuongThucChaySanPham = (@SoLuongThucChaySanPham - @SoLuongThucChay);
			SET @ThanhTienThucChaySanPham = (@ThanhTienThucChaySanPham - @ThanhTienThucChay);						
			
		END
			
		FETCH NEXT FROM tc_cursor INTO @HopDongID, @SoHopDong, @PhanBoId, @TenSanPham, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienPhanBo
	END
	
	CLOSE tc_cursor;
	DEALLOCATE tc_cursor;
	
	PRINT '@ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
	
	PRINT '=========== 111';
	-- check thanh tien con du thi se insert gia tri con lai vao thuc chay online
	IF (@ThanhTienThucChaySanPham > 0 OR @SoLuongThucChaySanPham > 0)
	BEGIN
		PRINT '@ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
		PRINT '@SoLuongThucChaySanPham: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySanPham);
		PRINT '@PhanBoId: ' + CONVERT(NVARCHAR(50), @PhanBoId);		
		
		SET	@SoLuongThucChayOnline		= @SoLuongThucChaySanPham;
		SET	@ThanhTienThucChayOnline	= @ThanhTienThucChaySanPham;
		SET	@TotalViewOnline		= @TongViewThucChay;
		SET	@TotalClickOnline		= @TongClickThucChay;
		
		PRINT 'Insert thuc chay online';		
		INSERT INTO [dbo].[ThucChayAdmarketOnline]
			   ([ThucChayAdmarketOnlineID]
			   ,[DmSanPhamREF]
			   ,[TenSanPham]
			   ,[TaiKhoan]
			   ,[TotalView]
			   ,[TotalClick]
			   ,[SoLuong]
			   ,[DonViTinh]
			   ,[TienThucChay]
			   ,[TienKhuyenMai]
			   ,[NgayThucHien]
			   ,[IsNoiBo]
			   ,[GhiChu]
			   ,[RecordStatus]
			   ,[CreatedAt]
			   ,[CreatedBy]
			   ,[LastModifiedAt]
			   ,[LastModifiedBy]
			   ,[DmViTriREF]
			   ,[TenViTri])
		 VALUES
			   (
				NEWID()
			   ,@DmSanPhamREF
			   ,@TenSanPham
			   ,@UserName
			   ,@TotalViewOnline
			   ,@TotalClickOnline
			   ,@SoLuongThucChayOnline
			   ,@DonViTinh
			   ,@ThanhTienThucChayOnline
			   ,0
			   ,@NgayThucHien
			   ,@IsNoiBo
			   ,'Tinh_Lai'
			   ,0 -- Tinh lai
			   ,GETDATE()
			   ,'asd'
			   ,GETDATE()
			   ,'asd'
			   ,@DmViTriREF
			   ,@TenViTri
			   )
		
		SET @SoLuongThucChaySanPham = (@SoLuongThucChaySanPham - @SoLuongThucChayOnline);
		SET @ThanhTienThucChaySanPham = (@ThanhTienThucChaySanPham - @ThanhTienThucChayOnline);
	END
	
	PRINT 'End Insert thuc chay online***';
	PRINT '@ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChaySanPham);
	PRINT '@SoLuongThucChaySanPham: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySanPham);
	
	-- Insert gia tri thuc chay cho phan bo khuyen mai
	IF @ThanhTienThucChayKMSanPham > 0
	BEGIN
		DECLARE km_cursor CURSOR FOR
		SELECT DISTINCT
			hdct.HopDongFK, hd.SoHopDong, hdct.HopDongChiTietID, hdct.TenSanPham, hdct.SoLuong, hdct.DonViTinh, (hdct.SoLuong*hdct.DonGia) ThanhTienKM
		FROM HopDongChiTiet AS hdct
			INNER JOIN HopDong AS hd ON hd.HopDongID = hdct.HopDongFK
			INNER JOIN ThucChaySelfServingUsers AS tcau ON hdct.TK_AdMarket = tcau.username
		WHERE 
			tcau.NgayThucHien					= @NgayThucHien
			--AND hd.NgayDanhSoHopDong	<= @NgayThucHien
			AND CONVERT(DATE, hdct.CreatedAt)	<= @NgayThucHien
			AND hdct.CreatedAt					>= @NgayGioiHanTinh
			AND tcau.username					= @UserName
			AND tcau.DonViTinh					= @DonViTinh
			AND hd.TrangThaiHopDong				<> 3
			AND hdct.DeletedStatus				= 0
			AND hdct.DmSanPhamREF				= @DmSanPhamREF
			AND hdct.IsKhuyenMai				= 1
		
		OPEN km_cursor
	
		FETCH NEXT FROM km_cursor INTO @HopDongID, @SoHopDong, @PhanBoId, @TenSanPham, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienKMPhanBo
	
		WHILE @@FETCH_STATUS = 0
		BEGIN
			SET @SoLuongThucChayKMPhanBo = 0;
			SET @ThanhTienThucChayKMPhanBo = 0;
			SET @SoLuongThucChayKM = 0;
			SET @SoLuongLechTreoHa = 0;
			SET @SoLuongThucChay = 0;
			SET @ThanhTienThucChay = 0;
		
			IF EXISTS(SELECT HopDongChiTietREF 
			          FROM ThucChayDaTinhAdmarket AS tcdt 
			          WHERE HopDongChiTietREF = @PhanBoId
						AND NgayThucHien <= @NgayThucHien)
			BEGIN
				SELECT 
					@SoLuongThucChayKMPhanBo = SUM(A.SoLuongThucChayKM),
					@ThanhTienThucChayKMPhanBo = SUM(A.ThanhTienKM)
				FROM ThucChayDaTinhAdmarket A
				WHERE A.HopDongChiTietREF = @PhanBoId
					AND A.NgayThucHien <= @NgayThucHien;
			END
		
			IF @ThanhTienThucChayKMPhanBo < @ThanhTienKMPhanBo
			BEGIN
				IF @ThanhTienThucChayKMPhanBo + @ThanhTienThucChayKMSanPham > @ThanhTienKMPhanBo
				BEGIN
					SET @ThanhTienThucChayKM = (@ThanhTienKMPhanBo - @ThanhTienThucChayKMPhanBo);
				END 
				ELSE
				BEGIN
					SET @ThanhTienThucChayKM = @ThanhTienThucChayKMSanPham;
				END
			END
			
			IF @ThanhTienThucChayKM > 0
			BEGIN
				-- insert to ThucChayDaTinhAdmarket
				EXEC dbo.ThucChayDaTinhAdmarket_InsertGiaTriThayDoiByPhanBoID
					@NgayThucHien
					,@SoHopDong
					,@PhanBoID
					,@DmSanPhamREF
					,@TenSanPham
					,0 --@DmWebsiteREF
					,'' --@TenWebsite
					,@TongViewThucChay
					,@TongClickThucChay
					,@SoLuongThucChay
					,@ThanhTienThucChay
					,@SoLuongThucChayKM
					,@ThanhTienThucChayKM
					,@SoLuongLechTreoHa
					,@ThanhTienLechTreoHa
					,@TypeInsert
					,@DonViTinhSanPham
					,@GhiChu
					,@DmViTriREF
					,@TenViTri
					
				SET @ThanhTienThucChayKMSanPham = @ThanhTienThucChayKMSanPham - @ThanhTienThucChayKM;
			END
		
			FETCH NEXT FROM km_cursor INTO @HopDongID, @SoHopDong, @PhanBoId, @TenSanPham, @SoLuongPhanBo, @DonViTinhPhanBo, @ThanhTienKMPhanBo
		END
	
		CLOSE km_cursor;
		DEALLOCATE km_cursor;
		
		IF @ThanhTienThucChayKMSanPham > 0
		BEGIN			
			SET	@SoLuongThucChayOnline		= 0;
			SET @ThanhTienThucChayOnline = 0;
			SET	@ThanhTienKMOnline	= @ThanhTienThucChayKMSanPham;
		
			PRINT 'Insert thuc chay online';
			
			-- Insert Thuc chay Online		
			INSERT INTO [dbo].[ThucChayAdmarketOnline]
				   ([ThucChayAdmarketOnlineID]
				   ,[DmSanPhamREF]
				   ,[TenSanPham]
				   ,[TaiKhoan]
				   ,[TotalView]
				   ,[TotalClick]
				   ,[SoLuong]
				   ,[DonViTinh]
				   ,[TienThucChay]
				   ,[TienKhuyenMai]
				   ,[NgayThucHien]
				   ,[IsNoiBo]
				   ,[GhiChu]
				   ,[RecordStatus]
				   ,[CreatedAt]
				   ,[CreatedBy]
				   ,[LastModifiedAt]
				   ,[LastModifiedBy]
				   ,[DmViTriREF]
				   ,[TenViTri])
			 VALUES
				   (
					NEWID()
				   ,@DmSanPhamREF
				   ,@TenSanPham
				   ,@UserName
				   ,@TotalViewOnline
				   ,@TotalClickOnline
				   ,@SoLuongThucChayOnline
				   ,@DonViTinh
				   ,@ThanhTienThucChayOnline
				   ,@ThanhTienKMOnline
				   ,@NgayThucHien
				   ,@IsNoiBo
				   ,'Tinh_Lai'
				   ,0 -- Tinh lai
				   ,GETDATE()
				   ,'asd'
				   ,GETDATE()
				   ,'asd'
				   ,@DmViTriREF
				   ,@TenViTri
				   )
				
			SET @SoLuongThucChaySanPham = 0;
			SET @ThanhTienThucChayKMSanPham = 0;
		END
	END
END

```
