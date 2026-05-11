# Stored Procedure: `ThucChayDaTinh_CanculateThucChayGG_FB_KM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-16 17:11:57.117000
- **Ngày sửa cuối**: 2015-01-29 10:02:56.853000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |
| `@phanBoId` | `int(4)` | No |
| `@sanPhamId` | `int(4)` | No |
| `@tenSanPham` | `nvarchar(100)` | No |
| `@websiteId` | `int(4)` | No |
| `@tenWebsite` | `nvarchar(100)` | No |
| `@isKhuyenMai` | `int(4)` | No |
| `@donViTinhPhanBo` | `nvarchar(100)` | No |
| `@soLuongPhanBoKM` | `int(4)` | No |
| `@thanhTienPhanBoKM` | `float(8)` | No |
| `@chietKhauPhanBoKM` | `int(4)` | No |
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
CREATE PROCEDURE [dbo].[ThucChayDaTinh_CanculateThucChayGG_FB_KM] 
	-- Add the parameters for the stored procedure here
	@ngayThucHien		DATETIME,
	@phanBoId	INT, 
	@sanPhamId	INT,
	@tenSanPham	NVARCHAR(50), 
	@websiteId	INT, 
	@tenWebsite	NVARCHAR(50), 
	@isKhuyenMai INT, 
	@donViTinhPhanBo	NVARCHAR(50),
	@soLuongPhanBoKM	INT, 
	@thanhTienPhanBoKM	FLOAT, 
	@chietKhauPhanBoKM	INT, 
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
			,@soLuongPhanBoQuyDoi	INT
	
	DECLARE @soLuongThucChayPhanBoKMTichLuy	INT,
			@tienThucChayPhanBoKMTichLuy	FLOAT,
			@soLuongPhanBoKMTichLuy		INT,
			@tienPhanBoKMTichLuy		FLOAT,
			@soLuongThucChayKM			INT = 0,
			@thanhTienThucChayKM			FLOAT = 0,
			@donGiaSauCK				FLOAT = 0,
			@thanhTienTamTinh			FLOAT = 0,
			@donViTinhThucChay			NVARCHAR(50)
			
	DECLARE @next	INT = 0,
			@online	INT	= 0,
			@phanBoChiPhiId	INT = 0,
			@sanPhamChiPhiId	INT,
			@tenSanPhamChiPhi	NVARCHAR(50),
			@donViTinhChiPhi	NVARCHAR(50)
			
	SELECT @soLuongThucChayPhanBoKMTichLuy	= 0,
			@tienThucChayPhanBoKMTichLuy		= 0,
			@soLuongPhanBoKMTichLuy			= 0,
			@tienPhanBoKMTichLuy			= 0,
			@thanhTienPhanBoChiPhi			= 0
			
			
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

    -- Check loai doi tuong
	-- Check loai doi tuong
	IF (@donViTinhPhanBo = N'Gói')
	BEGIN
		PRINT 'Hop dong chi phi khac';

		IF (@tienThucChayPhanBoKMTichLuy < @thanhTienPhanBoKM)
		BEGIN
			IF (@tienThucChayPhanBoKMTichLuy + @cost) < @thanhTienPhanBoKM
			BEGIN
				SET @thanhTienThucChayKM = @cost;							
			END
			ELSE
			BEGIN
				SET @thanhTienThucChayKM = ROUND((@thanhTienPhanBoKM - @tienThucChayPhanBoKMTichLuy),0);				
				
				PRINT '@thanhTienThucChayKM: ' + CONVERT(NVARCHAR(50), @thanhTienThucChayKM)
				-- Insert thuc chay GG,FB
				IF ROUND(@thanhTienThucChayKM,0) > 0
				BEGIN
					EXEC dbo.ThucChayDaTinhGoogleFacebook_InsertByPhanBoId 
						@NgayThucHien			= @ngayThucHien,
						@SoHopDong				= @soHopDong,
						@PhanBoID				= @phanBoId,
						@DmSanPhamREF			= @sanPhamId,
						@TenSanPham				= @tenSanPham,
						@DmWebsiteREF			= @websiteIdThucChay,
						@TenWebsite				= @tenWebsiteThucChay,
						@SoLuongThucChay		= 0,
						@ThanhTienThucChay		= 0,
						@SoLuongThucChayKM		= @soLuongThucChayKM,
						@ThanhTienThucChayKM	= @thanhTienThucChayKM,
						@DonViTinhSanPham		= @donViTinhPhanBo,
						@GhiChu					= ''																	
				END				
				
				SET @cost = (@cost - @thanhTienThucChayKM);
			END						
		END
	END
	ELSE IF (@donViTinhPhanBo = 'CPC' OR @donViTinhPhanBo = 'LIKE')
	BEGIN
		PRINT 'Hop dong cam ket theo click'; 
		
		IF (@soLuongThucChayPhanBoKMTichLuy < @soLuongPhanBoKM)
		BEGIN
			IF (@soLuongThucChayPhanBoKMTichLuy + @totalClick) > @soLuongPhanBoKM
			BEGIN
				SET @soLuongThucChayKM = (@soLuongPhanBoKM - @soLuongThucChayPhanBoKMTichLuy);
			END
			ELSE
			BEGIN
				SET @soLuongThucChayKM = @totalClick;
			END
		END
		ELSE
			SET @soLuongThucChayKM = 0;
		
		IF (@tienThucChayPhanBoKMTichLuy < @thanhTienPhanBoKM)
		BEGIN	
			SET @donGiaSauCK = CONVERT(FLOAT, @thanhTienPhanBoKM)/CONVERT(FLOAT, @soLuongPhanBoKM);
		
			SET @thanhTienTamTinh = (@soLuongThucChayKM * @donGiaSauCK);
			
			PRINT '@phanBoId: ' + CONVERT(NVARCHAR(50), @phanBoId)
			PRINT '@donGiaSauCK: ' + CONVERT(NVARCHAR(50), @donGiaSauCK)
			PRINT '@soLuongThucChay: ' + CONVERT(NVARCHAR(50), @soLuongThucChayKM)
			PRINT '@thanhTienTamTinh: ' + CONVERT(NVARCHAR(50), @thanhTienTamTinh)
			PRINT '@$tienThucChayPhanBoTichLuy: ' + CONVERT(NVARCHAR(50), @tienThucChayPhanBoKMTichLuy)
			PRINT '================================='
			
			IF (@tienThucChayPhanBoKMTichLuy + @thanhTienTamTinh) > @thanhTienPhanBoKM
			BEGIN
				SET @thanhTienThucChayKM = (@thanhTienPhanBoKM - @tienThucChayPhanBoKMTichLuy)
			END
			ELSE
			BEGIN
				SET @thanhTienThucChayKM = @thanhTienTamTinh;
			END
						
			PRINT '@thanhTienThucChay: ' + CONVERT(NVARCHAR(50), @thanhTienThucChayKM)
		END
		
		-- insert thuc chay GG,FB
		IF (@soLuongThucChayKM > 0 OR ROUND(@thanhTienThucChayKM,0) > 0)
		BEGIN
		EXEC dbo.ThucChayDaTinhGoogleFacebook_InsertByPhanBoId 
				@NgayThucHien			= @ngayThucHien,
				@SoHopDong				= @soHopDong,
				@PhanBoID				= @phanBoId,
				@DmSanPhamREF			= @sanPhamId,
				@TenSanPham				= @tenSanPham,
				@DmWebsiteREF			= @websiteIdThucChay,
				@TenWebsite				= @tenWebsiteThucChay,
				@SoLuongThucChay		= 0,
				@ThanhTienThucChay		= 0,
				@SoLuongThucChayKM		= @soLuongThucChayKM,
				@ThanhTienThucChayKM	= @thanhTienThucChayKM,
				@DonViTinhSanPham		= @donViTinhPhanBo,
				@GhiChu					= ''
		END
				
		SET @totalClick = (@totalClick - @soLuongThucChayKM);
		
	END
	ELSE IF (@donViTinhPhanBo = N'Tuần' OR @donViTinhPhanBo = N'Tháng' OR @donViTinhPhanBo = N'Ngày')
	BEGIN
		PRINT 'Hop dong cam ket theo thoi gian chay';
		SET @donViTinhThucChay = N'Ngày';
		SET @donViTinhThucChay = dbo.ThucChay_GetUnitThucChay(@sanPhamId,@donViTinhPhanBo);
		SET @soLuongPhanBoQuyDoi = @soLuongPhanBoKM*dbo.ThucChay_GetQuantityThucChay(@sanPhamId,@soLuongPhanBoKM,@donViTinhPhanBo);
		SET @donGiaSauCK = CONVERT(FLOAT,@thanhTienPhanBoKM)/CONVERT(FLOAT,@soLuongPhanBoQuyDoi)
		
		PRINT '@soLuongPhanBoQuyDoi: ' + CONVERT(NVARCHAR(50), @soLuongPhanBoQuyDoi)
		PRINT '@donGiaSauCK: ' + CONVERT(NVARCHAR(50), @donGiaSauCK)
		
		IF @soLuongThucChayPhanBoKMTichLuy < @soLuongPhanBoQuyDoi
		BEGIN
			IF (@soLuongThucChayPhanBoKMTichLuy + @totalDay) > @soLuongPhanBoQuyDoi
			BEGIN
				SET @soLuongThucChayKM = (@soLuongPhanBoQuyDoi - @soLuongThucChayPhanBoKMTichLuy);
			END
			ELSE
			BEGIN
				SET @soLuongThucChayKM = @totalDay;
			END
		END
		
		IF @tienThucChayPhanBoKMTichLuy < @thanhTienPhanBoKM
		BEGIN
			SET @thanhTienTamTinh = @donGiaSauCK*@soLuongThucChayKM;
			
			IF (@tienThucChayPhanBoKMTichLuy + @thanhTienTamTinh) > @thanhTienPhanBoKM
			BEGIN
				SET @thanhTienThucChayKM = (@thanhTienPhanBoKM - @tienThucChayPhanBoKMTichLuy);
			END
			ELSE
			BEGIN
				SET @thanhTienThucChayKM = @thanhTienTamTinh;
			END
		END
		
		IF (ROUND(@thanhTienThucChayKM,0) > 0 OR @soLuongThucChayKM > 0)
		BEGIN
			EXEC dbo.ThucChayDaTinhGoogleFacebook_InsertByPhanBoId 
				@NgayThucHien			= @ngayThucHien,
				@SoHopDong				= @soHopDong,
				@PhanBoID				= @phanBoId,
				@DmSanPhamREF			= @sanPhamId,
				@TenSanPham				= @tenSanPham,
				@DmWebsiteREF			= @websiteIdThucChay,
				@TenWebsite				= @tenWebsiteThucChay,
				@SoLuongThucChay		= 0,
				@ThanhTienThucChay		= 0,
				@SoLuongThucChayKM		= @soLuongThucChayKM,
				@ThanhTienThucChayKM	= @thanhTienThucChayKM,
				@DonViTinhSanPham		= @donViTinhThucChay,
				@GhiChu					= ''
		END
		
		SET @totalDay = (@totalDay - @soLuongThucChayKM);				
	END
	
	SELECT @outTotalClick = @totalClick,
			@outTotalDay = @totalDay,
			@outCost = @cost
	
	--SELECT @outTotalClick = 1,
	--		@outTotalDay = 2,
	--		@outCost = 3
END

```
