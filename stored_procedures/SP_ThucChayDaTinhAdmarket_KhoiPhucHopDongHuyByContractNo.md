# Stored Procedure: `ThucChayDaTinhAdmarket_KhoiPhucHopDongHuyByContractNo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-05 15:34:52.973000
- **Ngày sửa cuối**: 2014-12-12 14:18:11.130000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ContractNo` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-09-05
-- Description:	Khoi phuc hop dong huy bang tay
-- =============================================
-- 
-- EXEC dbo.ThucChayDaTinhAdmarket_KhoiPhucHopDongHuyByContractNo '2014-08-18', 'CPC450414'
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_KhoiPhucHopDongHuyByContractNo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien		DATETIME,
	@ContractNo			NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE	@HopDongREF INT,
			@SoHopDong NVARCHAR(50),
			@HopDongChiTietID INT,
			@DonViTinh			NVARCHAR(50),
			@account		NVARCHAR(50)
			
	DECLARE @SoLuongDotChayHD INT,
			@ThanhTienHDCT FLOAT, 
			@DmSanPhamREF	INT,
			@TenSanPham		NVARCHAR(50)
			
	DECLARE  
			@count_HDCT INT, 
			@SoLuongThucChayBF INT
			
	DECLARE @SoLuongCurrent	INT,
			@DonGiaCurrent	INT,
			@ChietKhauCurrent	INT,
			@ThanhTienCurrent	FLOAT,
			@DeltaValue			FLOAT,
			@GiaTriThayDoiByWebsite	FLOAT
			
	DECLARE @SoLuongOld	INT,
			@DonGiaOld	INT,
			@ChietKhauOld	INT,
			@ThanhTienOld	FLOAT	
	
	DECLARE @NgayThayDoiMax	DATETIME,
			@HopDongThayDoiREFMax INT	
	
	DECLARE @Count INT,
			@ThucChayTheoSite FLOAT,
			@Tyle				FLOAT,
			@TongTienThucChay	FLOAT
		
	DECLARE @NoiDungLog			NVARCHAR(MAX),
			@GhiChu				NVARCHAR(MAX)
			
	DECLARE @GiaTriHopDong		FLOAT,
			@GiaTriThucChay	FLOAT

	BEGIN
		-- Check xem co hop dong huy hay khong
		DECLARE @HopDongHuyId				INT,
				@SoHopDongHuy				NVARCHAR(50),
				@PhanBoHuyId				INT,
				@SanPhamHuyId				INT,
				@TenSanPhamHuy				NVARCHAR(50),
				@SoLuongThayDoiThucChay		BIGINT,
				@ThanhTienThayDoiThucChay	FLOAT,
				@DonViTinhHuy				NVARCHAR(50),
				@MaHopDongHuyId				INT,
				@TenMaHopDongHuy			NVARCHAR(50)
		
		DECLARE hd_cursor CURSOR FOR
		
		SELECT hd.HopDongID, hd.SoHopDong, hdct.HopDongChiTietID, hdct.DmSanPhamREF, TenSanPham,
			CASE hd.DmMaHopDongREF
				WHEN 310 THEN 310
				WHEN 533 THEN 310
				ELSE 0
			END AS DmMaHopDongREF,
			CASE hd.DmMaHopDongREF
				WHEN 310 THEN 'NB'
				WHEN 533 THEN 'NB'
				ELSE ''
			END AS TenMaHopDong
		FROM HopDong AS hd 
			INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
		WHERE hd.TrangThaiHopDong <> 3
			AND hd.SoHopDong = @ContractNo
			AND hdct.DmSanPhamREF IN (144,299,337,585) 
		
		OPEN hd_cursor
		FETCH NEXT FROM hd_cursor INTO @HopDongHuyId, @SoHopDongHuy, @PhanBoHuyId, @SanPhamHuyId, @TenSanPhamHuy, @MaHopDongHuyId, @TenMaHopDongHuy
		
		WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT '2: Update gia tri thay doi by hop dong huy';
			
			-- Tinh tien thuc chay theo tung phan bo id
			DECLARE pb_cursor CURSOR FOR
			SELECT
				DonViTinh, 
				SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0)) 
			FROM ThucChayDaTinhAdmarket A
			WHERE A.HopDongID = @HopDongHuyID
				and A.HopDongChiTietREF = @PhanBoHuyId
				AND A.NgayThucHien <= @NgayThucHien
				AND A.DotChayHopDong = 'HDHUY'
			GROUP BY
				A.DonViTinh
				
			OPEN pb_cursor
				
			FETCH NEXT FROM pb_cursor INTO @DonViTinhHuy, @ThanhTienThayDoiThucChay
			WHILE @@FETCH_STATUS = 0
			BEGIN
				PRINT 'DonViTinhHuy: ' + @DonViTinhHuy
				PRINT '@ThanhTienThayDoiThucChay: ' + cast(@ThanhTienThayDoiThucChay as nvarchar(50))
				
				IF @ThanhTienThayDoiThucChay <> 0
				BEGIN
					SELECT @account = TK_Admarket
					FROM HopDongChiTiet AS hdct
					WHERE hdct.HopDongChiTietID = @PhanBoHuyId
					
					SET @ThanhTienThayDoiThucChay = (0 - @ThanhTienThayDoiThucChay);
					
					PRINT '@ThanhTienThayDoiThucChay: ' + cast(@ThanhTienThayDoiThucChay as nvarchar(50))
					
					-- Insert gia tri thay doi
					EXEC dbo.ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi
						@NgayThucHien				= @NgayThucHien
						,@HopDongId					= @HopDongHuyId
						,@SoHopDong					= @SoHopDongHuy
						,@PhanBoId					= @PhanBoHuyId
						,@SanPhamId					= @SanPhamHuyId
						,@TenSanPham				= @TenSanPhamHuy
						,@DonViTinh					= @DonViTinhHuy
						,@SoLuongThayDoiThucChay	= 0
						,@ThanhTienThayDoiThucChay	= @ThanhTienThayDoiThucChay
						,@SoLuongThayDoiKhuyenMai	= 0
						,@ThanhTienThayDoiKhuyenMai	= 0
						,@GhiChu					= 'HDHUY_KHOIPHUC'
						
					-- Insert Log gia tri thay doi
					PRINT 'Log: ' + @NoiDungLog;
					EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
						@HopDongHuyId
						,@SoHopDongHuy
						,@PhanBoHuyId
						,@DmSanPhamREF
						,0
						,@NgayThucHien
						,@ThanhTienThayDoiThucChay
						,0
						,0
						,0
						,0
						,'Update Gia tri thay doi cho khoi phuc hop dong Huy'
						,'HopDongChiTiet_Admarket_HopDongHuy'
						,''						
						
					SET @ThanhTienThayDoiThucChay = @ThanhTienThayDoiThucChay*(-1);
					PRINT '@ThanhTienThayDoiThucChay1: ' + cast(@ThanhTienThayDoiThucChay as nvarchar(50))
					SET @GhiChu = 'HDHUY_KHOIPHUC_' + @SoHopDong
					-- Insert bu gia tri cho doi tuong khong co so hop dong
					EXEC dbo.ThucChayDaTinhAdmarket_InsertNoContractByProduct
						@DmSanPhamREF			= @SanPhamHuyId
						,@TenSanPham			= @TenSanPhamHuy
						,@DonViTinh				= @DonViTinhHuy
						,@DmWebsiteREF			= 0
						,@TenWebsite			= ''
						,@NgayThucHien			= @NgayThucHien
						,@SoLuongThucChay		= 0
						,@SoLuongThhucChayKM	= 0
						,@ThanhTienThucChay		= @ThanhTienThayDoiThucChay
						,@ThanhTienThucChayKM	= 0
						,@DmMaHopDongREF		= @MaHopDongHuyId
						,@TenMaHopDong			= @TenMaHopDongHuy
						,@GhiChu				= @GhiChu
						,@GiaTriThayDoi			= @ThanhTienThayDoiThucChay
						,@SoLuongThayDoi		= 0
						
					-- Insert gia tri online
					INSERT INTO ThucChayAdmarketOnline
					SELECT 
						NEWID()
						,@DmSanPhamREF
						,@TenSanPham -- AdX  CPC Admarket
						,@account
						,0 -- TotalViewOnline
						,0 -- TotalClickOnline
						,0 -- SoLuongThucChayOnline
						,@DonViTinh
						,@ThanhTienThayDoiThucChay -- Tien online
						,0	-- KM online
						,@NgayThucHien
						,0 --IsNoiBo
						,@GhiChu
						,0
						,GETDATE()
						,'asd'
						,GETDATE()
						,'asd'
						
				END
					
				FETCH NEXT FROM pb_cursor INTO @DonViTinhHuy, @ThanhTienThayDoiThucChay
			END
			
			CLOSE pb_cursor;
			DEALLOCATE pb_cursor;
						
			FETCH NEXT FROM hd_cursor INTO @HopDongHuyId, @SoHopDongHuy, @PhanBoHuyId, @SanPhamHuyId, @TenSanPhamHuy, @MaHopDongHuyId, @TenMaHopDongHuy
		END
		
		CLOSE hd_cursor;
		DEALLOCATE hd_cursor; 
		
	END
	SELECT 2
END

```
