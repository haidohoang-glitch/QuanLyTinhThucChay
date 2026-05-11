# Stored Procedure: `ThucChayDaTinhAdmarket_UpdateHopDongHuy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-28 10:06:17.993000
- **Ngày sửa cuối**: 2016-10-10 13:51:42.677000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
	EXEC dbo.ThucChayDaTinhAdmarket_UpdateHopDongHuy '2015-03-26'
*/
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_UpdateHopDongHuy]
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE	@HopDongREF INT,
			@SoHopDong NVARCHAR(50),
			@HopDongChiTietID INT,
			@DonViTinh			NVARCHAR(50),
			@account			NVARCHAR(50),
			@DmViTriREF			INT,
			@TenViTri			NVARCHAR(50)
			
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
			@GiaTriThayDoiByWebsite	FLOAT,
			@GiaTriThayDoi		FLOAT = 0,
			@GiaTriThayDoiByViTri	FLOAT = 0			
			
	DECLARE @SoLuongOld	INT,
			@DonGiaOld	INT,
			@ChietKhauOld	INT,
			@ThanhTienOld	FLOAT	
	
	DECLARE @NgayThayDoiMax	DATETIME,
			@HopDongThayDoiREFMax INT	
	
	DECLARE @Count INT,
			@ThucChayTheoSite FLOAT,
			@Tyle				FLOAT,
			@TongTienThucChay	FLOAT,
			@ThanhTienThucChayByViTri	FLOAT = 0,
			@TyLeByViTri			FLOAT = 0,
			@ThucChayAdXMobile	FLOAT = 0,
			@ThucChayAdxEcommerce FLOAT = 0,
			@ThucChayAdx		FLOAT = 0
		
	DECLARE @NoiDungLog			NVARCHAR(MAX),
			@GhiChu				NVARCHAR(MAX)
			
	DECLARE @GiaTriHopDong		FLOAT,
			@GiaTriThucChay	FLOAT
		
	DECLARE @MaHopDongId				INT,
			@TenMaHopDong			NVARCHAR(50)
			
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
		INNER JOIN HopDongThayDoi as hdtd ON hdtd.HopDongFK = hd.HopDongID
	WHERE 1 = 1
		--AND hd.TrangThaiHopDong = 3			
		--AND CONVERT(date,hd.LastModifiedAt) = @NgayThucHien
		AND hdtd.LoaiThayDoi = 0
		AND CONVERT(date,hdtd.NgayThayDoi) = @NgayThucHien
		AND hdct.DmSanPhamREF IN (144,299,337,585) 
	
	OPEN hd_cursor
	FETCH NEXT FROM hd_cursor INTO @HopDongHuyId, @SoHopDongHuy, @PhanBoHuyId, @SanPhamHuyId, @TenSanPhamHuy, @MaHopDongHuyId, @TenMaHopDongHuy
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT '2: Update gia tri thay doi by hop dong huy';
		PRINT 'SoHopDongHuy: ' + @SoHopDongHuy
		-- Tinh tien thuc chay theo tung phan bo id
		DECLARE pb_cursor CURSOR FOR
		SELECT
			DonViTinh, 
			SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0)) 
		FROM ThucChayDaTinhAdmarket A
		WHERE A.HopDongID = @HopDongHuyID
			and A.HopDongChiTietREF = @PhanBoHuyId
		GROUP BY
			A.DonViTinh
			
		OPEN pb_cursor
			
		FETCH NEXT FROM pb_cursor INTO @DonViTinhHuy, @ThanhTienThayDoiThucChay
		WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT 'DonViTinhHuy: ' + @DonViTinhHuy
			PRINT '@@PhanBoHuyId: ' + cast(@PhanBoHuyId as nvarchar(50))
			PRINT '@SanPhamHuyId: ' + cast(@SanPhamHuyId as nvarchar(50))
			PRINT '@ThanhTienThayDoiThucChay: ' + cast(@ThanhTienThayDoiThucChay as nvarchar(50))
			
			IF @ThanhTienThayDoiThucChay > 0
			BEGIN
				SELECT @account = TK_Admarket
				FROM HopDongChiTiet AS hdct
				WHERE hdct.HopDongChiTietID = @PhanBoHuyId
			
				SET @ThanhTienThayDoiThucChay = (0 - @ThanhTienThayDoiThucChay);
				
				PRINT '@ThanhTienThayDoiThucChay: ' + cast(@ThanhTienThayDoiThucChay as nvarchar(50))
				
				DECLARE vitri_cursor_huy CURSOR FOR
				SELECT DmViTriREF, TenViTri, SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
				FROM ThucChayDaTinhAdmarket tcdt
				WHERE HopDongChiTietREF = @PhanBoHuyId
					AND tcdt.DmSanPhamREF = @SanPhamHuyId
					AND tcdt.NgayThucHien BETWEEN '2013-01-01' AND @NgayThucHien 
				GROUP BY
					DmViTriREF, TenViTri
				
				OPEN vitri_cursor_huy
				
				FETCH NEXT FROM vitri_cursor_huy INTO @DmViTriREF, @TenViTri, @ThanhTienThucChayByViTri
				WHILE @@FETCH_STATUS = 0
				BEGIN
					PRINT '@@@ThanhTienThucChayByViTri: ' + cast(@ThanhTienThucChayByViTri as nvarchar(50))
					
					SET @GiaTriThayDoiByViTri = (-1)*@ThanhTienThucChayByViTri
					
					PRINT '@@GiaTriThayDoiByViTri: ' + cast(@GiaTriThayDoiByViTri as nvarchar(50))
					
					IF @GiaTriThayDoiByViTri <> 0
					BEGIN
						-- Insert gia tri thay doi
						--EXEC dbo.ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi
						EXEC [dbo].[ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi_HDHuy]
							@NgayThucHien				= @NgayThucHien
							,@HopDongId					= @HopDongHuyId
							,@SoHopDong					= @SoHopDongHuy
							,@PhanBoId					= @PhanBoHuyId
							,@SanPhamId					= @SanPhamHuyId
							,@TenSanPham				= @TenSanPhamHuy
							,@DonViTinh					= @DonViTinhHuy
							,@SoLuongThayDoiThucChay	= 0
							,@ThanhTienThayDoiThucChay	= @GiaTriThayDoiByViTri
							,@SoLuongThayDoiKhuyenMai	= 0
							,@ThanhTienThayDoiKhuyenMai	= 0
							,@GhiChu					= 'HDHUY'
							,@DmViTriREF				= @DmViTriREF
							,@TenViTri					= @TenViTri
							
						-- Insert Log gia tri thay doi
						PRINT 'Log: ' + @NoiDungLog;
						EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
							@HopDongHuyId
							,@SoHopDongHuy
							,@PhanBoHuyId
							,@SanPhamHuyId
							,0
							,@NgayThucHien
							,@ThanhTienThayDoiThucChay
							,0
							,0
							,0
							,0
							,'Update Gia tri thay doi cho hop dong Huy'
							,'HopDongChiTiet_Admarket_HopDongHuy'
							,''						
							
						SET @GiaTriThayDoiByViTri = @GiaTriThayDoiByViTri*(-1);
						PRINT '@@GiaTriThayDoiByViTri: ' + cast(@GiaTriThayDoiByViTri as nvarchar(50))
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
							,@ThanhTienThucChay		= 0
							,@ThanhTienThucChayKM	= 0
							,@DmMaHopDongREF		= @MaHopDongHuyId
							,@TenMaHopDong			= @TenMaHopDongHuy
							,@GhiChu				= 'HDHUY'
							,@GiaTriThayDoi			= @GiaTriThayDoiByViTri
							,@SoLuongThayDoi		= 0
							,@DmViTriREF			= @DmViTriREF
							,@TenViTri				= @TenViTri
							
						-- Insert thuc chay online
						
						INSERT INTO ThucChayAdmarketOnline
						SELECT 
							NEWID()
							,@SanPhamHuyId
							,@TenSanPhamHuy -- AdX  CPC Admarket
							,@account
							,0 -- TotalViewOnline
							,0 -- TotalClickOnline
							,0 -- SoLuongThucChayOnline
							,@DonViTinhHuy
							,@GiaTriThayDoiByViTri -- Tien online
							,0	-- KM online
							,@NgayThucHien
							,0 --IsNoiBo
							,'Hop_Dong_Thay_Doi_Huy'
							,0
							,GETDATE()
							,'asd'
							,GETDATE()
							,'asd'
							,@DmViTriREF
							,@TenViTri
					END	
				
					FETCH NEXT FROM vitri_cursor_huy INTO @DmViTriREF, @TenViTri, @ThanhTienThucChayByViTri
				END
				
				CLOSE vitri_cursor_huy
				DEALLOCATE vitri_cursor_huy	
					
				SET @ThanhTienThayDoiThucChay = 0
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

```
