# Stored Procedure: `ThucChayDaTinh_CanculateThucChayGG_FB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-12 17:20:55.783000
- **Ngày sửa cuối**: 2015-05-25 11:34:55.127000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |
| `@phanBoId` | `int(4)` | No |
| `@TaiKhoan` | `nvarchar(400)` | No |
| `@sanPhamId` | `int(4)` | No |
| `@tenSanPham` | `nvarchar(100)` | No |
| `@websiteId` | `int(4)` | No |
| `@tenWebsite` | `nvarchar(100)` | No |
| `@isKhuyenMai` | `int(4)` | No |
| `@donViTinhPhanBo` | `nvarchar(100)` | No |
| `@soLuongPhanBo` | `int(4)` | No |
| `@thanhTienPhanBo` | `float(8)` | No |
| `@chietKhauPhanBo` | `int(4)` | No |
| `@hopDongID` | `int(4)` | No |
| `@soHopDong` | `nvarchar(100)` | No |
| `@donGiaPhanBo` | `int(4)` | No |
| `@totalClick` | `int(4)` | No |
| `@totalDay` | `int(4)` | No |
| `@cost` | `float(8)` | No |
| `@type` | `nvarchar(100)` | No |
| `@outTotalClick` | `int(4)` | Yes |
| `@outTotalDay` | `int(4)` | Yes |
| `@outCost` | `float(8)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-11-18
-- Description:	Calculate data thuc chay
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_CanculateThucChayGG_FB] 
	-- Add the parameters for the stored procedure here
	@ngayThucHien		DATETIME,
	@phanBoId	INT,
	@TaiKhoan NVARCHAR(200), 
	@sanPhamId	INT,
	@tenSanPham	NVARCHAR(50), 
	@websiteId	INT, 
	@tenWebsite	NVARCHAR(50), 
	@isKhuyenMai INT, 
	@donViTinhPhanBo	NVARCHAR(50),
	@soLuongPhanBo	INT, 
	@thanhTienPhanBo	FLOAT, 
	@chietKhauPhanBo	INT, 
	@hopDongID			INT, 
	@soHopDong			NVARCHAR(50), 
	@donGiaPhanBo		INT,
	@totalClick			INT,
	@totalDay			INT,
	@cost				FLOAT,
	@type				NVARCHAR(50),
	@outTotalClick		INT OUTPUT,
	@outTotalDay		INT OUTPUT,
	@outCost			FLOAT OUTPUT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @thanhTienPhanBoChiPhi	FLOAT
			,@websiteIdThucChay	INT
			,@tenWebsiteThucChay	NVARCHAR(50)
			,@tenWebsiteHopDong		NVARCHAR(50)
			,@soLuongPhanBoQuyDoi	INT
	
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
			@donViTinhChiPhi	NVARCHAR(50),
			@totalDaysContract	INT
			
	DECLARE @soluong INT = 0,
			@deltaValue	FLOAT = 0,
			@deltaSoLuong	INT = 0,
			@ghiChu	NVARCHAR(512) = 'GG_FB',
			@thanhTienPhanBoChiPhiTichLuy	FLOAT = 0,
			@thanhTienThucChayChiPhi		FLOAT = 0
			
	DECLARE @prePhanBoId INT = 0,
			@prePhanBoChiPhiId INT = 0,
			@preThanhTienPhanBoChiPhi FLOAT = 0,
			@preTienThucChayPhanBoChiPhiTichLuy FLOAT = 0
			
	DECLARE @ThanhTienThucChayPhanBoTamTinh FLOAT = 0,
			@delta FLOAT = 0;
				
	SELECT @soLuongThucChayPhanBoTichLuy	= 0,
			@tienThucChayPhanBoTichLuy		= 0,
			@soLuongPhanBoKMTichLuy			= 0,
			@tienPhanBoKMTichLuy			= 0,
			@thanhTienPhanBoChiPhi			= 0
			
			
	IF @sanPhamId = 423
	BEGIN
		SET @websiteId = 285;
		SET @websiteIdThucChay = 466;	
		SET @tenWebsiteThucChay = 'google.com.vn';
		SET @tenWebsiteHopDong = 'Google';
	END
	ELSE
	BEGIN
		SET @websiteId = 307;
		SET @websiteIdThucChay = 426;	
		SET @tenWebsiteThucChay = 'facebook.com';
		SET @tenWebsiteHopDong = 'Facebook';
	END
	
	IF EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinh WHERE HopDongChiTietREF = @phanBoId)
		SET @tienThucChayPhanBoTichLuy = (SELECT SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
											FROM ThucChayDaTinh
											WHERE HopDongChiTietREF = @phanBoId
												AND TrangThaiHopDong <> 3
												AND NgayThucHien <= @ngayThucHien)
	ELSE
		SET @tienThucChayPhanBoTichLuy = 0;

    -- Check loai doi tuong
	-- Check loai doi tuong
	IF (@type = N'phi_quan_ly')
	BEGIN
		PRINT 'Hop dong chi phi khac';
		PRINT '@phanBoId: ' + CONVERT(NVARCHAR(50), @phanBoId)
			
		PRINT '@thanhTienPhanBo: ' + CONVERT(NVARCHAR(50), @thanhTienPhanBo)
		PRINT '@tienThucChayPhanBoTichLuy: ' + CONVERT(NVARCHAR(50), @tienThucChayPhanBoTichLuy)
		PRINT '@cost: ' + CONVERT(NVARCHAR(50), @cost)
		
		-- Check xem phan bo chi phi cua hop dong truoc da duoc tinh du chua
		-- Neu chua tinh du thi tinh not cho phan bo chi phi truoc khi tinh cho phan bo chinh moi
		DECLARE chiphi_cursor CURSOR FOR
		SELECT hdct.HopDongChiTietID, hdct.DmSanPhamREF, hdct.TenSanPham, 
			hdct.ThanhTien, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
		FROM HopDongChiTiet AS hdct
			INNER JOIN ThucChayDaTinh AS tcdt ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
		WHERE 1=1
			AND hdct.DmSanPhamREF = 535
			AND hdct.IsKhuyenMai = 0
			AND hdct.HopDongChiTietID < @phanBoId
			AND hdct.TenWebsite = @tenWebsiteHopDong
			AND hdct.TK_AdMarket LIKE '%' + @TaiKhoan + '%'
			AND tcdt.TrangThaiHopDong <> 3
			AND tcdt.NgayThucHien <= @ngayThucHien
		GROUP BY hdct.HopDongChiTietID, hdct.ThanhTien, hdct.DmSanPhamREF, hdct.TenSanPham
			
		OPEN chiphi_cursor
		
		FETCH NEXT FROM chiphi_cursor INTO @prePhanBoChiPhiId, @sanPhamChiPhiId, @tenSanPhamChiPhi, @preThanhTienPhanBoChiPhi, @preTienThucChayPhanBoChiPhiTichLuy		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT '@cost1: ' + CONVERT(NVARCHAR(50),@cost);
			IF (@cost > 0 AND (ROUND(@preTienThucChayPhanBoChiPhiTichLuy,0) < ROUND(@preThanhTienPhanBoChiPhi,0)))
			BEGIN
				PRINT '@cost11: ' + CONVERT(NVARCHAR(50),@cost);
				IF(@preTienThucChayPhanBoChiPhiTichLuy + @cost) < @preThanhTienPhanBoChiPhi
					SET @thanhTienThucChay = @cost;
				ELSE
					SET @thanhTienThucChay = ROUND((@preThanhTienPhanBoChiPhi - @preTienThucChayPhanBoChiPhiTichLuy), 0);
			END
			ELSE
				SET @thanhTienThucChay = 0;
				
			PRINT '@thanhTienThucChay: ' + CONVERT(NVARCHAR(50),@thanhTienThucChay);
				
			IF @thanhTienThucChay > 0
			BEGIN
				EXEC dbo.ThucChayDaTinhGoogleFacebook_InsertByPhanBoId 
					@NgayThucHien			= @ngayThucHien,
					@SoHopDong				= @soHopDong,
					@PhanBoID				= @prePhanBoChiPhiId,
					@DmSanPhamREF			= @sanPhamChiPhiId,
					@TenSanPham				= @tenSanPhamChiPhi,
					@DmWebsiteREF			= @websiteIdThucChay,
					@TenWebsite				= @tenWebsiteThucChay,
					@SoLuongThucChay		= 1,
					@ThanhTienThucChay		= @thanhTienThucChay,
					@SoLuongThucChayKM		= 0,
					@ThanhTienThucChayKM	= 0,
					@DonViTinhSanPham		= @donViTinhPhanBo,
					@GhiChu					= @ghiChu,
					@Type					= @type
					
				SET @cost = (@cost - @thanhTienThucChay);
				PRINT '@costSauKhiTinh: ' + CONVERT(NVARCHAR(50),@cost);
			END
			
			FETCH NEXT FROM chiphi_cursor INTO @prePhanBoChiPhiId, @sanPhamChiPhiId, @tenSanPhamChiPhi, @preThanhTienPhanBoChiPhi, @preTienThucChayPhanBoChiPhiTichLuy	
		END
		
		CLOSE chiphi_cursor
		DEALLOCATE chiphi_cursor;
		
		-- Tinh cho phan bo chinh hien tai
		IF (@cost > 0 AND (@tienThucChayPhanBoTichLuy < @thanhTienPhanBo))
		BEGIN
			
			IF (@tienThucChayPhanBoTichLuy + @cost) < @thanhTienPhanBo
			BEGIN
				PRINT '111'
				SET @thanhTienThucChay = @cost;							
			END
			ELSE
			BEGIN
				PRINT '222'
				SET @thanhTienThucChay = ROUND((@thanhTienPhanBo - @tienThucChayPhanBoTichLuy),0);
				
				PRINT '@thanhTienThucChay: ' + CONVERT(NVARCHAR(50), @thanhTienThucChay)				
			END
			-- Insert thuc chay GG,FB
			IF ROUND(@thanhTienThucChay,0) > 0
			BEGIN
				EXEC dbo.ThucChayDaTinhGoogleFacebook_InsertByPhanBoId 
					@NgayThucHien			= @ngayThucHien,
					@SoHopDong				= @soHopDong,
					@PhanBoID				= @phanBoId,
					@DmSanPhamREF			= @sanPhamId,
					@TenSanPham				= @tenSanPham,
					@DmWebsiteREF			= @websiteIdThucChay,
					@TenWebsite				= @tenWebsiteThucChay,
					@SoLuongThucChay		= 1,
					@ThanhTienThucChay		= @thanhTienThucChay,
					@SoLuongThucChayKM		= 0,
					@ThanhTienThucChayKM	= 0,
					@DonViTinhSanPham		= @donViTinhPhanBo,
					@GhiChu					= @ghiChu,
					@Type					= @type
					
				SET @cost = (@cost - @thanhTienThucChay);
				
				PRINT '@Cost du: ';
				PRINT '@@cost: ' + CONVERT(NVARCHAR(50), @cost)																
			END
			
			IF @cost > 0
			BEGIN
				PRINT 'Tiep tuc tinh cho phan bo chi phi'
				-- thuc chay chi phi 
				SELECT TOP 1 @phanBoChiPhiId = hdct.HopDongChiTietID
				FROM HopDongChiTiet AS hdct
				WHERE 1=1
					AND hdct.HopDongFK = @hopDongId
					AND hdct.DeletedStatus = 0
					AND hdct.DmWebsiteREF = @websiteID
					AND (hdct.DmLoaiREF = 14 OR hdct.DmSanPhamREF = 535 OR hdct.DmSanPhamREF = 251)
					
				SELECT 
					@sanPhamChiPhiId = hdct.DmSanPhamREF,
					@tenSanPhamChiPhi = hdct.TenSanPham,
					@donViTinhChiPhi = hdct.DonViTinh,
					@thanhTienPhanBoChiPhi = ThanhTien
				FROM HopDongChiTiet AS hdct
				WHERE hdct.HopDongChiTietID = @phanBoChiPhiId
				
				IF @phanBoChiPhiId > 0
				BEGIN
					SELECT @thanhTienPhanBoChiPhiTichLuy = ISNULL(SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdt.GiaTriThayDoi,0)),0)
					FROM ThucChayDaTinh AS tcdt
					WHERE tcdt.HopDongChiTietREF = @phanBoChiPhiId
						AND tcdt.TrangThaiHopDong <> 3
						AND tcdt.NgayThucHien >= '2014-01-01'
						AND tcdt.NgayThucHien <= @ngayThucHien
				END
				ELSE
				BEGIN
					SET @thanhTienPhanBoChiPhiTichLuy = 0;
				END
				
				PRINT '@phanBoChiPhiId: ' + CONVERT(NVARCHAR(50), @phanBoChiPhiId)
				PRINT '@@thanhTienPhanBoChiPhi: ' + CONVERT(NVARCHAR(50), @thanhTienPhanBoChiPhi)
				PRINT '@@thanhTienPhanBoChiPhiTichLuy: ' + CONVERT(NVARCHAR(50), @thanhTienPhanBoChiPhiTichLuy)
				
				IF @thanhTienPhanBoChiPhiTichLuy < @thanhTienPhanBoChiPhi
				BEGIN
					IF ((@thanhTienPhanBoChiPhiTichLuy + @cost) > @thanhTienPhanBoChiPhi)
						SET @thanhTienThucChayChiPhi = (@thanhTienPhanBoChiPhi - @thanhTienPhanBoChiPhiTichLuy)
					ELSE
					BEGIN
						IF @cost > @thanhTienPhanBoChiPhi
							SET @thanhTienThucChayChiPhi = @thanhTienPhanBoChiPhi
						ELSE
							SET @thanhTienThucChayChiPhi = @cost;
					END
				END
				ELSE
				BEGIN
					SET @thanhTienThucChayChiPhi = 0;
				END								
				
				-- Insert phan bo chi phi
				IF (@thanhTienThucChayChiPhi > 0)
				BEGIN
					EXEC dbo.ThucChayDaTinhGoogleFacebook_InsertByPhanBoId 
						@NgayThucHien			= @ngayThucHien,
						@SoHopDong				= @soHopDong,
						@PhanBoID				= @phanBoChiPhiId,
						@DmSanPhamREF			= @sanPhamChiPhiId,
						@TenSanPham				= @tenSanPhamChiPhi,
						@DmWebsiteREF			= @websiteIdThucChay,
						@TenWebsite				= @tenWebsiteThucChay,
						@SoLuongThucChay		= 1,
						@ThanhTienThucChay		= @thanhTienThucChayChiPhi,
						@SoLuongThucChayKM		= 0,
						@ThanhTienThucChayKM	= 0,
						@DonViTinhSanPham		= @donViTinhChiPhi,
						@GhiChu					= @ghiChu,
						@Type					= @type
				END
				
				SET @cost = (@cost - @thanhTienThucChayChiPhi);
				PRINT '@cost: ' + CONVERT(NVARCHAR(50), @cost)
				
			END
									
		END
	END
	ELSE IF (@type = 'click' OR @type = 'page_like')
	BEGIN		
		PRINT 'Hop dong cam ket theo click'; 
		PRINT '@phanBoId: ' + CONVERT(NVARCHAR(50), @phanBoId)
		PRINT '@thanhTienPhanBo: ' + CONVERT(NVARCHAR(50), @thanhTienPhanBo)
		PRINT '@tienThucChayPhanBoTichLuy: ' + CONVERT(NVARCHAR(50), @tienThucChayPhanBoTichLuy)
		PRINT '@totalClick: ' + CONVERT(NVARCHAR(50), @totalClick)
		
		IF EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinh WHERE HopDongChiTietREF = @phanBoId)
			SELECT @soLuongThucChayPhanBoTichLuy = SUM(ISNULL(SoLuongThucChay,0) + ISNULL(SoLuongThayDoi,0))
			FROM ThucChayDaTinh
			WHERE HopDongChiTietREF = @phanBoId
				AND TrangThaiHopDong <> 3
				AND NgayThucHien <= @ngayThucHien
		ELSE
			SET @soLuongThucChayPhanBoTichLuy = 0
		
		PRINT '@soLuongThucChayPhanBoTichLuy: ' + CONVERT(NVARCHAR(50), @soLuongThucChayPhanBoTichLuy)
		PRINT '@soLuongPhanBo: ' + CONVERT(NVARCHAR(50), @soLuongPhanBo)		
		
		IF (ROUND(@tienThucChayPhanBoTichLuy,0) < @thanhTienPhanBo)
		BEGIN
			SET @deltaValue = (@thanhTienPhanBo - @tienThucChayPhanBoTichLuy);
			PRINT '@@deltaValue: ' + CONVERT(NVARCHAR(50), @deltaValue)	
			IF(@donViTinhPhanBo = N'Gói')
			BEGIN
				SET @donGiaSauCK =
				(
					SELECT A.DonGia
					FROM ThucChayGoogleFacebook	A
					WHERE 1=1
						AND A.NgayThucHien = (             
												SELECT MAX(tcgf.NgayThucHien) NgayThucHien
												FROM ThucChayGoogleFacebook tcgf
												WHERE 1=1 
													AND tcgf.TaiKhoan = @TaiKhoan
													AND tcgf.RecordStatus = 1	    
													AND tcgf.NgayThucHien <= @ngayThucHien    
						)
						AND A.TaiKhoan = @TaiKhoan
						AND A.[Type] = @type
				)
				
				SET @donGiaSauCK = @donGiaSauCK *(100-@chietKhauPhanBo)/100
			END
			ELSE
				BEGIN
					SET @donGiaSauCK = CONVERT(FLOAT, @thanhTienPhanBo)/CONVERT(FLOAT, @soLuongPhanBo);		
				END
			IF(	@donGiaSauCK <> 0)
			BEGIN
				SET @soluong = (@tienThucChayPhanBoTichLuy/@donGiaSauCK);
				SET @deltaSoLuong = (@deltaValue/@donGiaSauCK);	
			END
			ELSE
				BEGIN
					SET @soluong = 0;
					SET @deltaSoLuong = 0;	
				END
				
			PRINT '@donGiaSauCK: ' + CONVERT(NVARCHAR(50), @donGiaSauCK)
			PRINT '@soluong: ' + CONVERT(NVARCHAR(50), @soluong)	
			PRINT '@deltaSoLuong: ' + CONVERT(NVARCHAR(50), @deltaSoLuong)
			IF(@donViTinhPhanBo = N'Gói')
			BEGIN
				IF @totalClick < @deltaSoLuong
					BEGIN
						SET @soLuongThucChay = @totalClick;
					END
					ELSE
					BEGIN
						SET @soLuongThucChay = @deltaSoLuong;
					END
				
			END
			ELSE
				BEGIN
					IF @totalClick < @deltaSoLuong
					BEGIN
						SET @soLuongThucChay = @totalClick;
					END
					ELSE
					BEGIN
						SET @soLuongThucChay = @deltaSoLuong;
					END
				END
			SET @thanhTienThucChay = (@soLuongThucChay*@donGiaSauCK);
			
			SET @ThanhTienThucChayPhanBoTamTinh = (@thanhTienThucChay + @tienThucChayPhanBoTichLuy)
			SET @delta = (@ThanhTienThucChayPhanBoTamTinh - @thanhTienPhanBo)
			
			IF @delta > 0
				SET @thanhTienThucChay = (@thanhTienThucChay - @delta);
			ELSE IF @delta < 0
			BEGIN
				IF((@totalClick - @soLuongThucChay) >= 1)
				BEGIN
					SET @soLuongThucChay = (@soLuongThucChay + 1);
					SET @thanhTienThucChay = (@thanhTienPhanBo - @tienThucChayPhanBoTichLuy);
				END
					
			END
				
			--SET @totalClick = (@totalClick - @soLuongThucChay)
		END	
		ELSE
			SELECT @soLuongThucChay = 0, @thanhTienThucChay = 0;
		
		PRINT '@soLuongThucChay: ' + CONVERT(NVARCHAR(50), @soLuongThucChay)
		PRINT '@thanhTienThucChay: ' + CONVERT(NVARCHAR(50), @thanhTienThucChay)
		
		-- insert thuc chay GG,FB
		IF (@soLuongThucChay > 0 OR ROUND(@thanhTienThucChay,0) > 0)
		BEGIN
		EXEC dbo.ThucChayDaTinhGoogleFacebook_InsertByPhanBoId 
				@NgayThucHien			= @ngayThucHien,
				@SoHopDong				= @soHopDong,
				@PhanBoID				= @phanBoId,
				@DmSanPhamREF			= @sanPhamId,
				@TenSanPham				= @tenSanPham,
				@DmWebsiteREF			= @websiteIdThucChay,
				@TenWebsite				= @tenWebsiteThucChay,
				@SoLuongThucChay		= @soLuongThucChay,
				@ThanhTienThucChay		= @thanhTienThucChay,
				@SoLuongThucChayKM		= 0,
				@ThanhTienThucChayKM	= 0,
				@DonViTinhSanPham		= @donViTinhPhanBo,
				@GhiChu					= @ghiChu,
				@Type					= @type
		END
		
		PRINT '@totalClick1: ' + CONVERT(NVARCHAR(50), @totalClick)		
		SET @totalClick = (@totalClick - @soLuongThucChay);
		PRINT '@totalClick2: ' + CONVERT(NVARCHAR(50), @totalClick)	
		
	END
	ELSE IF (@type = N'thoi_gian')
	BEGIN
		PRINT 'Hop dong cam ket theo thoi gian chay';
		PRINT '@phanBoId: ' + CONVERT(NVARCHAR(50), @phanBoId)
		PRINT '@thanhTienPhanBo: ' + CONVERT(NVARCHAR(50), @thanhTienPhanBo)
		PRINT '@tienThucChayPhanBoTichLuy: ' + CONVERT(NVARCHAR(50), @tienThucChayPhanBoTichLuy)
		PRINT '@totalDay: ' + CONVERT(NVARCHAR(50), @totalDay)
		
		SET @donViTinhThucChay = N'Ngày';
		SET @donViTinhThucChay = dbo.ThucChay_GetUnitThucChay(@sanPhamId,@donViTinhPhanBo);
		SET @soLuongPhanBoQuyDoi = dbo.ThucChay_GG_FB_GetSoLuongByDotChay(@phanBoId);
		IF @soLuongPhanBoQuyDoi > 0
			SET @donGiaSauCK = CONVERT(FLOAT,@thanhTienPhanBo)/CONVERT(FLOAT,@soLuongPhanBoQuyDoi)
		ELSE
			SET @donGiaSauCK = 0;
		
		PRINT '@soLuongPhanBoQuyDoi: ' + CONVERT(NVARCHAR(50), @soLuongPhanBoQuyDoi)
		PRINT '@donGiaSauCK: ' + CONVERT(NVARCHAR(50), @donGiaSauCK)
		
		IF (ROUND(@tienThucChayPhanBoTichLuy,0) < @thanhTienPhanBo)
		BEGIN
			SET @deltaValue = (@thanhTienPhanBo - @tienThucChayPhanBoTichLuy);
			SET @soluong = (@tienThucChayPhanBoTichLuy/@donGiaSauCK);
			SET @deltaSoLuong = (@deltaValue/@donGiaSauCK);
			
			PRINT '@donGiaSauCK: ' + CONVERT(NVARCHAR(50), @donGiaSauCK)
			PRINT '@soluong: ' + CONVERT(NVARCHAR(50), @soluong)	
			PRINT '@deltaSoLuong: ' + CONVERT(NVARCHAR(50), @deltaSoLuong)
			
			IF @totalDay < @deltaSoLuong
			BEGIN
				SET @soLuongThucChay = @totalDay;
			END
			ELSE
			BEGIN
				SET @soLuongThucChay = @deltaSoLuong;
			END
			
			SET @thanhTienThucChay = (@soLuongThucChay*@donGiaSauCK);
			--SET @totalDay = (@totalDay - @soLuongThucChay)
		END
		ELSE
			SELECT @soLuongThucChay = 0, @thanhTienThucChay = 0;
			
		PRINT '@soLuongThucChay: ' + CONVERT(NVARCHAR(50), @soLuongThucChay)
		PRINT '@thanhTienThucChay: ' + CONVERT(NVARCHAR(50), @thanhTienThucChay)				
		
		IF (ROUND(@thanhTienThucChay,0) > 0 OR @soLuongThucChay > 0)
		BEGIN
			EXEC dbo.ThucChayDaTinhGoogleFacebook_InsertByPhanBoId 
				@NgayThucHien			= @ngayThucHien,
				@SoHopDong				= @soHopDong,
				@PhanBoID				= @phanBoId,
				@DmSanPhamREF			= @sanPhamId,
				@TenSanPham				= @tenSanPham,
				@DmWebsiteREF			= @websiteIdThucChay,
				@TenWebsite				= @tenWebsiteThucChay,
				@SoLuongThucChay		= @soLuongThucChay,
				@ThanhTienThucChay		= @thanhTienThucChay,
				@SoLuongThucChayKM		= 0,
				@ThanhTienThucChayKM	= 0,
				@DonViTinhSanPham		= @donViTinhThucChay,
				@GhiChu					= @ghiChu,
				@Type					= @type
		END
		
		SET @totalDay = (@totalDay - @soLuongThucChay);				
	END
	
	PRINT '@cost: ' + CONVERT(NVARCHAR(50), @cost)
	SELECT @outTotalClick = @totalClick,
			@outTotalDay = @totalDay,
			@outCost = @cost
	
	--SELECT @outTotalClick = 1,
	--		@outTotalDay = 2,
	--		@outCost = 3
END

```
