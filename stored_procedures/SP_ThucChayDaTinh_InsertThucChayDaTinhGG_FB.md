# Stored Procedure: `ThucChayDaTinh_InsertThucChayDaTinhGG_FB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-04 12:07:50.943000
- **Ngày sửa cuối**: 2015-05-25 11:35:11.243000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |
| `@account` | `nvarchar(100)` | No |
| `@sanPhamId` | `int(4)` | No |
| `@type` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.ThucChayDaTinh_InsertThucChayDaTinhGG_FB 
		'2015-05-04', 
		'Vietjet_Dai Loan', 
		423, 
		'phi_quan_ly'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChayDaTinhGG_FB]
	-- Add the parameters for the stored procedure here
	@ngayThucHien	DATETIME,
	@account		NVARCHAR(50),
	@sanPhamId		INT,
	@type			NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    --SELECT @ngayThucHien, @account, @sanPhamId
    
    DECLARE @tenSanPham	NVARCHAR(50)
			,@websiteID	INT
			,@tenWebsite	NVARCHAR(50)
			,@totalClick	INT
			,@totalDay		INT
			,@cost			FLOAT
			,@totalClickMulti	INT
			,@totalDayMulti		INT
			,@totalCostMulti	FLOAT
			
	DECLARE @phanBoId		INT
			,@isKhuyenMai	INT
			,@donViTinhPhanBo	NVARCHAR(50)
			,@soLuongPhanBo		INT
			,@thanhTienPhanBo	FLOAT
			,@chietKhauPhanBo	int
			,@thanhTienPhanBoChiPhi	FLOAT
			,@websiteIdThucChay	INT
			,@tenWebsiteThucChay	NVARCHAR(50)
			,@hopDongId			INT
			,@soHopDong			NVARCHAR(50)
			,@donGiaPhanBo		INT
			,@soLuongPhanBoQuyDoi	INT
			,@accountPhanBo		NVARCHAR(512)
			
	DECLARE @soLuongThucChayPhanBoTichLuy	INT,
			@tienThucChayPhanBoTichLuy	FLOAT,
			@soLuongPhanBoKMTichLuy		INT,
			@tienPhanBoKMTichLuy		FLOAT,
			@soLuongThucChay			INT = 0,
			@thanhTienThucChay			FLOAT = 0,
			@donGiaSauCK				FLOAT = 0,
			@thanhTienTamTinh			FLOAT = 0,
			@donViTinhThucChay			NVARCHAR(50)
			
	DECLARE @next	INT = 0,
			@online	INT	= 0,
			@phanBoChiPhiId	INT = 0,
			@sanPhamChiPhiId	INT,
			@tenSanPhamChiPhi	NVARCHAR(50),
			@donViTinhChiPhi	NVARCHAR(50)
			
	DECLARE @outTotalClick		INT = 0,
			@outTotalDay		INT	= 0,
			@outCost			FLOAT = 0
			
	DECLARE @TongTienPhanBo		FLOAT = 0,
			@TongTienThucChay   FLOAT = 0;
			
	SELECT @soLuongThucChayPhanBoTichLuy	= 0,
			@tienThucChayPhanBoTichLuy		= 0,
			@soLuongPhanBoKMTichLuy			= 0,
			@tienPhanBoKMTichLuy			= 0,
			@thanhTienPhanBoChiPhi			= 0
			
	DECLARE @AccountTemp as TABLE (
		Account		NVARCHAR(50),
		TotalClick		INT,
		TotalDay		INT,
		Cost			FLOAT,
		PerClick		FLOAT,
		PerDay			FLOAT,
		PerCost			FLOAT,
		[Type]			NVARCHAR(50)
	)
	
		
	SELECT 
		@totalClick = SUM(A.Click),
		@totalDay = SUM(A.SoNgayChay),
		@cost = SUM(A.ThanhTien)
	FROM ThucChayGoogleFacebookByDay A
	WHERE 1=1
		AND A.DmSanPhamREF = @sanPhamId
		AND A.NgayThucHien = @ngayThucHien
		AND A.TaiKhoan = @account
		AND A.[Type] = @type
		
	PRINT 'totalClick: ' + CONVERT(NVARCHAR(50), @totalClick)
	PRINT 'totalDay: ' + CONVERT(NVARCHAR(50), @totalDay)
	PRINT 'cost: ' + CONVERT(NVARCHAR(50), @cost)
	
	/*
		check san pham tinh la Google hay Facebook
	*/
	IF @sanPhamId = 423
	BEGIN
		SET @websiteIdThucChay = 466;	
		SET @tenWebsiteThucChay = 'google.com.vn';
	END
	ELSE
	BEGIN
		SET @websiteIdThucChay = 426;	
		SET @tenWebsiteThucChay = 'facebook.com';
	END
				
	--PHAN BIET DANH SACH CAC PHAN BO CAN TINH THEO PHUONG PHAP NAO
	IF @type = 'thoi_gian'
	BEGIN
		PRINT 'thoi_gian'
		DECLARE pb_cursor CURSOR FOR
		SELECT DISTINCT
			T.HopDongChiTietID, T.TenSanPham, T.DmWebsiteREF, T.TenWebsite, T.IsKhuyenMai, T.DonViTinh, 
			T.SoLuong, T.ThanhTien, T.ChietKhau, T.HopDongFK, T.SoHopDong, T.DonGia, T.TK_AdMarket
		FROM
		(
			SELECT 
				A.HopDongChiTietID, A.TenSanPham, A.DmWebsiteREF, A.TenWebsite, A.IsKhuyenMai, A.DonViTinh, 
				A.SoLuong, A.ThanhTien, A.ChietKhau, A.HopDongFK, B.SoHopDong, A.DonGia, A.TK_AdMarket
				,dbo.ThucChay_GG_FB_GetSoLuongByDotChay(A.HopDongChiTietID) TotalDays
			FROM HopDongChiTiet A
				INNER JOIN HopDong B ON B.HopDongID = A.HopDongFK
			WHERE 1=1
				AND A.DeletedStatus = 0
				AND B.TrangThaiHopDong <> 3
				AND A.DmSanPhamREF = @sanPhamId
				AND A.TK_AdMarket = @account
				AND A.DmLoaiBannerREF <> 17 --CHI PHI CUA SAN PHAM CHINH
				AND A.CreatedAt >= '2014-01-01'
				AND CONVERT(DATE,A.CreatedAt) <= @ngayThucHien
				AND A.DonViTinh <> 'CPC'
				
			UNION
			SELECT 
				A.HopDongChiTietID, A.TenSanPham, A.DmWebsiteREF, A.TenWebsite, A.IsKhuyenMai, A.DonViTinh, 
				A.SoLuong, A.ThanhTien, A.ChietKhau, A.HopDongFK, B.SoHopDong, A.DonGia, A.TK_AdMarket
				,dbo.ThucChay_GG_FB_GetSoLuongByDotChay(A.HopDongChiTietID) TotalDays
			FROM HopDongChiTietGoogleFacebook A
				INNER JOIN HopDong B ON B.HopDongID = A.HopDongFK
			WHERE 1=1
				AND A.DeletedStatus = 0
				AND B.TrangThaiHopDong <> 3
				AND A.DmSanPhamREF = @sanPhamId
				AND A.TK_AdMarket = @account
				AND A.DmLoaiBannerREF <> 17 --CHI PHI CUA SAN PHAM CHINH
				AND A.CreatedAt >= '2014-01-01'
				AND CONVERT(DATE,A.CreatedAt) <= @ngayThucHien
				AND A.DonViTinh <> 'CPC'
		)T
		WHERE T.TotalDays > 0
		ORDER BY 
			T.HopDongChiTietID
		
	END
	ELSE
	BEGIN
		DECLARE pb_cursor CURSOR FOR
		SELECT *
		FROM
		(
			SELECT 
				A.HopDongChiTietID, A.TenSanPham, A.DmWebsiteREF, A.TenWebsite, A.IsKhuyenMai, A.DonViTinh, 
				A.SoLuong, A.ThanhTien, A.ChietKhau, A.HopDongFK, B.SoHopDong, A.DonGia, A.TK_AdMarket
			FROM HopDongChiTiet A
				INNER JOIN HopDong B ON B.HopDongID = A.HopDongFK
			WHERE 1=1
				AND A.DeletedStatus = 0
				AND B.TrangThaiHopDong <> 3
				AND A.DmSanPhamREF = @sanPhamId
				AND A.TK_AdMarket = @account
				AND A.DmLoaiBannerREF <> 17 --CHI PHI CUA SAN PHAM CHINH
				AND A.CreatedAt >= '2014-01-01'
				AND CONVERT(DATE,A.CreatedAt) <= @ngayThucHien
				AND A.DonViTinh = CASE  WHEN @type = 'phi_quan_ly' AND A.DonViTinh = N'Gói' THEN N'Gói'
											 WHEN @type = 'phi_quan_ly' AND A.DonViTinh = N'CPC' THEN N'CPC'
											 WHEN @type = 'click' AND A.DonViTinh = 'CPC'		THEN N'CPC'
											 WHEN @type = 'click' AND A.DonViTinh = 'CLICK'		THEN N'CLICK'
											 WHEN @type = 'click' AND A.DonViTinh = 'CPV'	THEN N'CPV'
											 WHEN @type = 'click' AND A.DonViTinh = N'Gói' THEN N'Gói'
											 WHEN @type = 'page_like'		THEN N'LIKE'
											 WHEN @type = 'page_like' AND A.DonViTinh = N'Gói' THEN N'Gói'
								  END
			--ORDER BY 
			--		A.HopDongChiTietID
			UNION
			SELECT 
				A.HopDongChiTietID, A.TenSanPham, A.DmWebsiteREF, A.TenWebsite, A.IsKhuyenMai, A.DonViTinh, 
				A.SoLuong, A.ThanhTien, A.ChietKhau, A.HopDongFK, B.SoHopDong, A.DonGia, A.TK_AdMarket
			FROM HopDongChiTietGoogleFacebook A
				INNER JOIN HopDong B ON B.HopDongID = A.HopDongFK
			WHERE 1=1
				AND A.DeletedStatus = 0
				AND B.TrangThaiHopDong <> 3
				AND A.DmSanPhamREF = @sanPhamId
				AND A.TK_AdMarket = @account
				AND A.DmLoaiBannerREF <> 17 --CHI PHI CUA SAN PHAM CHINH
				AND A.CreatedAt >= '2014-01-01'
				AND CONVERT(DATE,A.CreatedAt) <= @ngayThucHien
				AND A.DonViTinh = CASE  WHEN @type = 'phi_quan_ly' AND A.DonViTinh = N'Gói' THEN N'Gói'
											 WHEN @type = 'phi_quan_ly' AND A.DonViTinh = N'CPC' THEN N'CPC'
											 WHEN @type = 'click' AND A.DonViTinh = 'CPC'		THEN N'CPC'
											 WHEN @type = 'click' AND A.DonViTinh = 'CLICK'		THEN N'CLICK'
											 WHEN @type = 'click' AND A.DonViTinh = 'CPV'	THEN N'CPV'
											 WHEN @type = 'click' AND A.DonViTinh = N'Gói' THEN N'Gói'
											 WHEN @type = 'page_like'		THEN N'LIKE'
											 WHEN @type = 'page_like' AND A.DonViTinh = N'Gói' THEN N'Gói'
								  END
		)T
		ORDER BY 
				T.HopDongChiTietID
	END	
	
	OPEN pb_cursor
	
	FETCH NEXT FROM pb_cursor INTO @phanBoId, @tenSanPham, @websiteId, @tenWebsite, @isKhuyenMai, @donViTinhPhanBo,
					@soLuongPhanBo, @thanhTienPhanBo, @chietKhauPhanBo, @hopDongID, @soHopDong, @donGiaPhanBo, @accountPhanBo
	
	WHILE @@FETCH_STATUS = 0
	BEGIN		
		-- Check xem phan bo co chay multile tai khoan hay khong
		SELECT @accountPhanBo = TK_Admarket
		FROM HopDongChiTiet
		WHERE HopDongChiTietID = @phanBoId
		
		IF CHARINDEX(',', @accountPhanBo) > 0
		BEGIN
			-- hop dong chay nhieu tai khoan
			PRINT 'Multle account';
			PRINT '@accountPhanBo: ' + CONVERT(NVARCHAR(50), @accountPhanBo)
			
			SELECT @totalClickMulti = SUM(A.Click),
				@totalDayMulti = SUM(A.SoNgayChay),
				@totalCostMulti = SUM(A.ThanhTien)
			FROM ThucChayGoogleFacebookByDay A
				INNER JOIN (SELECT * FROM dbo.StringSplitter(@accountPhanBo,',')) B ON A.TaiKhoan = dbo.TRIM(B.Items)
			WHERE 1=1
				AND A.NgayThucHien = @ngayThucHien
				
			PRINT '@totalClickMulti: ' + CONVERT(NVARCHAR(50), @totalClickMulti)
			PRINT '@totalDayMulti: ' + CONVERT(NVARCHAR(50), @totalDayMulti)
			PRINT '@totalCostMulti: ' + CONVERT(NVARCHAR(50), @totalCostMulti)
			
			DELETE FROM @AccountTemp
			INSERT INTO @AccountTemp
			SELECT A.TaiKhoan,A.Click, A.SoNgayChay, A.ThanhTien,
				CASE WHEN @totalClickMulti > 0 THEN CONVERT(FLOAT,A.Click)/CONVERT(FLOAT,@totalClickMulti) ELSE 0
				END TotalClick, 
				CASE WHEN @totalDayMulti > 0 THEN CONVERT(FLOAT,A.SoNgayChay)/CONVERT(FLOAT,@totalDayMulti) ELSE 0
				END TotalDay,
				CASE WHEN @totalCostMulti > 0 THEN CONVERT(FLOAT,A.ThanhTien)/CONVERT(FLOAT,@totalCostMulti) ELSE 0
				END TotalCost,
				@type
			FROM ThucChayGoogleFacebookByDay A
				INNER JOIN (SELECT * FROM dbo.StringSplitter(@accountPhanBo,',')) B ON A.TaiKhoan = dbo.TRIM(B.Items)
			WHERE 1=1
				AND A.NgayThucHien = @ngayThucHien
				
			SELECT * FROM @AccountTemp
			PRINT '@phanBoId: ' + Convert(nvarchar(50),@phanBoId) 
			-- Check xem phan bo da duoc tinh trong ngay chua?
			SELECT @TongTienPhanBo = ThanhTien
			FROM HopDongChiTiet AS hdct
			WHERE 1=1
				AND hdct.HopDongChiTietID = @phanBoId;
				
			SELECT @TongTienThucChay = isnull(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0)
			FROM ThucChayDaTinh AS tcdt
			WHERE 1=1
				AND tcdt.HopDongChiTietREF = @phanBoId
				AND tcdt.TrangThaiHopDong <> 3
				AND tcdt.NgayThucHien <= @ngayThucHien
				
			PRINT 'TongTienPhanBo: ' + CONVERT(NVARCHAR(50), @TongTienPhanBo);
			PRINT 'TongTienThucChay: ' + CONVERT(NVARCHAR(50), @TongTienThucChay);		
				
			IF (NOT EXISTS(SELECT HopDongChiTietREF 
			              FROM HopDongChiTietGoogleFacebookByDay 
			              WHERE HopDongCHiTietREF = @phanBoId
			              AND Convert(date,NgayThucHien) = @ngayThucHien				
				) AND (@TongTienThucChay < @TongTienPhanBo)
			)
			BEGIN
				PRINT 'ThucChayDaTinh_CanculateThucChayGG_FB :' + Convert(nvarchar(50),@phanBoId) 
				PRINT 'Total cost: ' + CONVERT(NVARCHAR(50),@totalCostMulti);
				EXEC dbo.ThucChayDaTinh_CanculateThucChayGG_FB
					@ngayThucHien		= @ngayThucHien,
					@phanBoId			= @phanBoId,
					@TaiKhoan	        = @account ,
					@sanPhamId			= @sanPhamId,
					@tenSanPham			= @tenSanPham, 
					@websiteId			= @websiteIdThucChay, 
					@tenWebsite			= @tenWebsiteThucChay, 
					@isKhuyenMai		= @isKhuyenMai, 
					@donViTinhPhanBo	= @donViTinhPhanBo,
					@soLuongPhanBo		= @soLuongPhanBo,
					@thanhTienPhanBo	= @thanhTienPhanBo, 
					@chietKhauPhanBo	= @chietKhauPhanBo,	 
					@hopDongID			= @hopDongId,		 
					@soHopDong			= @soHopDong, 
					@donGiaPhanBo		= @donGiaPhanBo,		
					@totalClick			= @totalClickMulti,		
					@totalDay			= @totalDayMulti,			
					@cost				= @totalCostMulti,
					@type				= @type,
					@outTotalClick		= @outTotalClick OUTPUT,
					@outTotalDay		= @outTotalDay OUTPUT,
					@outCost			= @outCost OUTPUT;
					
				SELECT @outTotalClick, @outTotalDay, @outCost
				
				SELECT @account
				
				SELECT 
					Account, PerClick*@outTotalClick TotalClick,
					PerDay*@outTotalDay TotalDay,
					PerCost*@outCost Cost
					
				FROM @AccountTemp
				WHERE Account <> @account;
				
				-- Update trang thai phan bo da duoc tinh de khoi phai tinh lai khi quyet den tai khoan thu 2
				INSERT INTO HopDongChiTietGoogleFacebookByDay
				SELECT NEWID(),@phanBoId,@ngayThucHien,'' GhiChu

				-- Update cho tai khoan khac
				
				DECLARE @costDu FLOAT = 0
				
				SELECT 
					@costDu = PerCost*@outCost
				FROM ThucChayGoogleFacebookByDay A
					INNER JOIN @AccountTemp B ON B.Account = A.TaiKhoan
				WHERE 1=1
					AND A.Type = @type
					AND A.TaiKhoan IN (
						SELECT Account
						FROM @AccountTemp
						WHERE 1=1
							AND Account <> @account
							AND [Type] = @type
					)
				
				PRINT '--------'	
				PRINT '@costDu: ' + CONVERT(NVARCHAR(50), @costDu)
					
				UPDATE ThucChayGoogleFacebookByDay
				SET Click = PerClick*@outTotalClick,
					SoNgayChay = PerDay*@outTotalDay,
					ThanhTien = PerCost*@outCost
				FROM ThucChayGoogleFacebookByDay A
					INNER JOIN @AccountTemp B ON B.Account = A.TaiKhoan
				WHERE 1=1
					AND A.Type = @type
					AND A.TaiKhoan IN (
						SELECT Account
						FROM @AccountTemp
						WHERE 1=1
							--AND Account <> @account
							AND [Type] = @type
					)
					
				-- Set lai gia tri cho tai khoan dang tinh
				SELECT @totalClick = PerClick*@outTotalClick,
					@totalDay = PerDay*@outTotalDay,
					@cost = PerCost*@outCost
				FROM @AccountTemp
				WHERE Account = @account
				
				PRINT '========== Du sau khi tinh ================='
				PRINT '@@cost: ' + CONVERT(NVARCHAR(50), @cost)
			END
		END
		ELSE
		BEGIN
			-- Phan bo chi co 1 tai khoan 
			PRINT '1 account';
			PRINT '@@totalClick: ' + CONVERT(NVARCHAR(50), @totalClick)
			PRINT '@@totalDay: ' + CONVERT(NVARCHAR(50), @totalDay)
			PRINT '@@cost: ' + CONVERT(NVARCHAR(50), @cost)
			
			PRINT '@thanhTienPhanBo: ' + CONVERT(NVARCHAR(50), @thanhTienPhanBo)
			
			-- so sanh tien thuc chay so voi tien phan bo hop dong
			SELECT @TongTienPhanBo = ThanhTien
			FROM HopDongChiTiet AS hdct
			WHERE 1=1
				AND hdct.HopDongChiTietID = @phanBoId;
				
			SELECT @TongTienThucChay = isnull(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0)
			FROM ThucChayDaTinh AS tcdt
			WHERE 1=1
				AND tcdt.HopDongChiTietREF = @phanBoId
				AND tcdt.TrangThaiHopDong <> 3
				AND tcdt.NgayThucHien <= @ngayThucHien
							
			PRINT 'TongTienPhanBo: ' + CONVERT(NVARCHAR(50), @TongTienPhanBo);
			PRINT 'TongTienThucChay: ' + CONVERT(NVARCHAR(50), @TongTienThucChay);
			
			IF (@type = 'phi_quan_ly' AND @cost > 0 AND (ROUND(@TongTienThucChay,0) < ROUND(@TongTienPhanBo,0)))
			BEGIN
				SET @next = 1;
				PRINT '@cost:' + CONVERT(NVARCHAR(50), @cost)
			END
			ELSE IF (@type = 'click' AND @totalClick > 0)
			BEGIN
				SET @next = 1
				PRINT '@totalClick:' + CONVERT(NVARCHAR(50), @totalClick)
			END
			ELSE IF (@type = 'thoi_gian' AND @totalDay > 0)
			BEGIN
				SET @next = 1
				PRINT '@totalDay:' + CONVERT(NVARCHAR(50), @totalDay)
			END
			ELSE IF (@type = 'like' AND @totalClick > 0)
			BEGIn
				SET @next = 1
				PRINT '@totalClick:' + CONVERT(NVARCHAR(50), @totalClick)
			END					

			PRINT '@@next: ' + CONVERT(NVARCHAR(50), @next)
			IF @next = 1
			BEGIN
				EXEC dbo.ThucChayDaTinh_CanculateThucChayGG_FB
					@ngayThucHien		= @ngayThucHien,
					@phanBoId			= @phanBoId, 
					@TaiKhoan	        = @account ,
					@sanPhamId			= @sanPhamId,
					@tenSanPham			= @tenSanPham, 
					@websiteId			= @websiteIdThucChay, 
					@tenWebsite			= @tenWebsiteThucChay, 
					@isKhuyenMai		= @isKhuyenMai, 
					@donViTinhPhanBo	= @donViTinhPhanBo,
					@soLuongPhanBo		= @soLuongPhanBo,
					@thanhTienPhanBo	= @thanhTienPhanBo, 
					@chietKhauPhanBo	= @chietKhauPhanBo,	 
					@hopDongID			= @hopDongId,		 
					@soHopDong			= @soHopDong, 
					@donGiaPhanBo		= @donGiaPhanBo,		
					@totalClick			= @totalClick,		
					@totalDay			= @totalDay,			
					@cost				= @cost,
					@type				= @type,
					@outTotalClick		= @outTotalClick OUTPUT,
					@outTotalDay		= @outTotalDay OUTPUT,
					@outCost			= @outCost OUTPUT;
					
					SET @totalClick = @outTotalClick;
					SET @totalDay = @outTotalDay;
					SET @cost = @outCost;				
			END
		END
		
		FETCH NEXT FROM pb_cursor INTO @phanBoId, @tenSanPham, @websiteId, @tenWebsite, @isKhuyenMai, @donViTinhPhanBo,
					@soLuongPhanBo, @thanhTienPhanBo, @chietKhauPhanBo, @hopDongID, @soHopDong, @donGiaPhanBo, @accountPhanBo
	END
	
	CLOSE pb_cursor
	DEALLOCATE pb_cursor	
	
	IF (@type = 'phi_quan_ly' AND @cost > 0)
		SET @online = 1;
	ELSE IF (@type = 'click' AND @totalClick > 0)
		SET @online = 1
	ELSE IF (@type = 'thoi_gian' AND @totalDay > 0)
		SET @online = 1
	ELSE IF (@type = 'like' AND @totalClick > 0)
		set @online = 1
		
	PRINT '@online: ' + CONVERT(NVARCHAR(50), @online)	
	
	IF @online = 1
	BEGIN
		INSERT INTO [dbo].[ThucChayGoogleFacebookOnline]
		SELECT
			   @sanPhamId
			   ,@tenSanPham
			   ,@account
			   ,@totalDay
			   ,@totalClick
			   ,@cost
			   ,@type
			   ,NEWID()
			   ,@ngayThucHien
			   ,GETDATE()
			   ,'asd'
			   ,GETDATE()
			   ,'asd'
			   ,0
			   ,0    
		
		SELECT @totalClick = 0,
				@totalDay = 0,
				@cost = 0
	END
	
	-- Update du lieu tai khoan vua tinh
	--UPDATE ThucChayGoogleFacebookByDay
	--SET Click = @totalClick,
	--	SoNgayChay = @totalDay,
	--	ThanhTien = @cost
	--WHERE 1=1
	--	AND TaiKhoan = @account
	--	AND NgayThucHien = @ngayThucHien
	--	AND [Type] = @type
			
	--PRINT '@totalDay: ' + CONVERT(NVARCHAR(50), @totalDay);
	--PRINT '@totalClick: ' + CONVERT(NVARCHAR(50), @totalClick)
	--PRINT '@cost: ' + CONVERT(NVARCHAR(50), @cost)
 --   UPDATE ThucChayGoogleFacebook 
 --   SET RecordStatus = 2,
	--	SoNgayChay = @totalDay,
	--	Click = @totalClick,
	--	ThanhTien = @cost
	--WHERE NgayThucHien = @ngayThucHien AND TaiKhoan = @account AND DmSanPhamREF = @sanPhamId AND RecordStatus = 1
		
END

```
