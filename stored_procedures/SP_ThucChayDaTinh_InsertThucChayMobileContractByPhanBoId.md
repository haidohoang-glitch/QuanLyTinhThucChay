# Stored Procedure: `ThucChayDaTinh_InsertThucChayMobileContractByPhanBoId`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-29 08:34:54.417000
- **Ngày sửa cuối**: 2014-11-19 12:25:01.997000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ContractNo` | `nvarchar(100)` | No |
| `@PhanBoId` | `int(4)` | No |
| `@SiteName` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@BannerType` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC dbo.ThucChayDaTinh_InsertThucChayMobileContractByPhanBoId '2014-05-27','QC260413','dantri.com.vn','VIEW', 3
CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChayMobileContractByPhanBoId]
	@NgayThucHien	DATETIME,
	@ContractNo		NVARCHAR(50),
	@PhanBoId		INT,
	@SiteName		NVARCHAR(50),
	@DonViTinh		NVARCHAR(50),
	@BannerType		INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	
	DECLARE 
			@IsKhuyenMai	INT,
			@TypeInsert		INT
			
	DECLARE @SoLuongThucChaySP		INT = 0, 
			@SoLuongDaChay			INT = 0, 
			@SoLuongThucChay		INT = 0, 
			@DonViTinhHD			 NVARCHAR(50),
			@DonViTinhPhanBo		NVARCHAR(50)
			
	DECLARE @SoLuongThucChayPhanBo	INT, 
			@SoLuongPhanBoHopDong	INT
			
	DECLARE @ThanhTienThucChaySanPham FLOAT = 0,
			@ThanhTienPhanBoHopDong		FLOAT = 0,
			@ThanhTienThucChayPhanBo	FLOAT = 0,
			@ThanhTienThucChay			FLOAT = 0,
			@ThanhTienKhuyenMaiPhanBo	FLOAT = 0,
			@ThanhTienThucChayPhanBoKM	FLOAT = 0,
			@ThanhTienThucChayKM		FLOAT = 0,
			@SoLuongThucChayKM			INT = 0,
			@SoLuongLechTreoHa			INT = 0,
			@ThanhTienLechTreoHa		FLOAT = 0
			
	DECLARE @TongViewThucChay		INT = 0,
			@TongClickThucChay		INT = 0,
			@DonGiaSanPham			INT = 0,
			@DonGiaTheoDonViTinhSP	INT = 0
	
	IF @DonViTinh = 'CLICK' SET @DonViTinhHD = 'CPC'
		ELSE SET @DonViTinhHD = 'CPM'
	
	SET @SoLuongThucChaySP = (
		SELECT	CASE WHEN @DonViTinh = 'VIEW' THEN (tcm.TotalView)
					 ELSE (tcm.TotalClick)
				END AS SoLuongThucChay
		FROM ThucChayMobileTemp AS tcm
		WHERE tcm.dt = @NgayThucHien 
			AND tcm.[Contract] = @ContractNo 
			AND tcm.SiteName = @SiteName 
			AND tcm.UnitName = @DonViTinh 	
			AND tcm.BannerType = @BannerType
	)
	
	PRINT 'SoLuongSP: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySP)
	
	SET @TongViewThucChay = (SELECT tcmt.TotalView
	                          FROM ThucChayMobileTemp AS tcmt	                        
	                          WHERE tcmt.dt = @NgayThucHien
								AND tcmt.[Contract] = @ContractNo
								AND tcmt.SiteName = @SiteName
								AND BannerType	= @BannerType
								AND tcmt.UnitName = @DonViTinh							 
	)
	SET @TongClickThucChay = (SELECT tcmt.TotalClick
	                          FROM ThucChayMobileTemp AS tcmt	                        
	                          WHERE tcmt.dt = @NgayThucHien
								AND tcmt.[Contract] = @ContractNo
								AND tcmt.SiteName = @SiteName
								AND BannerType	= @BannerType
								AND tcmt.UnitName = @DonViTinh							 
	)
	
	SET @DonGiaSanPham = (
							SELECT 
								CASE WHEN tcmt.BannerType = 2 THEN 3000
									 WHEN tcmt.BannerType = 3 AND tcmt.UnitName = 'CLICK' THEN 3000
									 WHEN tcmt.BannerType = 3 AND tcmt.UnitName = 'VIEW' THEN 65000/1000
									 WHEN tcmt.BannerType = 4 AND tcmt.UnitName = 'CLICK' THEN 3000
									 WHEN tcmt.BannerType = 4 AND tcmt.UnitName = 'VIEW' THEN 35000/1000
									 WHEN tcmt.BannerType = 5 THEN 3000
									 WHEN tcmt.BannerType = 10 AND tcmt.UnitName = 'CLICK' THEN 3000
									 WHEN tcmt.BannerType = 10 AND tcmt.UnitName = 'VIEW' THEN 35000/1000
									 WHEN tcmt.BannerType = 14 AND tcmt.UnitName = 'CLICK' THEN 3000
									 WHEN tcmt.BannerType = 14 AND tcmt.UnitName = 'VIEW' THEN 45000/1000
								END
							FROM ThucChayMobileTemp AS tcmt	                        
							WHERE tcmt.dt = @NgayThucHien
								AND tcmt.[Contract] = @ContractNo
								AND tcmt.SiteName = @SiteName
								AND BannerType	= @BannerType
								AND tcmt.UnitName = @DonViTinh	
	)
	SET @DonGiaSanPham = ISNULL(@DonGiaSanPham,0);
	
	SET @DonGiaTheoDonViTinhSP = (
							SELECT 
								CASE WHEN tcmt.BannerType = 2 THEN 3000
									 WHEN tcmt.BannerType = 5 THEN 3000
									 WHEN tcmt.BannerType = 3 THEN 65000/1000
									 WHEN tcmt.BannerType = 4 THEN 35000/1000
									 WHEN tcmt.BannerType = 10 THEN 35000/1000
									 WHEN tcmt.BannerType = 14 THEN 45000/1000
									 ELSE 0
								END
							FROM ThucChayMobileTemp AS tcmt	                        
							WHERE tcmt.dt = @NgayThucHien
								AND tcmt.[Contract] = @ContractNo
								AND tcmt.SiteName = @SiteName
								AND BannerType	= @BannerType
								AND tcmt.UnitName = @DonViTinh	
	)
	SET @DonGiaTheoDonViTinhSP = ISNULL(@DonGiaTheoDonViTinhSP,0);
	
	PRINT 'DonGiaSanPham: ' + CONVERT(NVARCHAR(50),@DonGiaSanPham);
	
	IF @SoLuongThucChaySP > 0
	BEGIN	
		SET @DonViTinhPhanBo = (
										SELECT DonViTinh FROM HopDongChiTiet AS hdct WHERE hdct.HopDongChiTietID = @PhanBoId
									)	
			-- Select so luong cua phan bo, thanh tien cua phan bo
			SELECT	@SoLuongPhanBoHopDong = ISNULL(SoLuong,0), 
					@ThanhTienPhanBoHopDong = ISNULL(ThanhTien,0)
			FROM HopDongChiTiet AS hdct
			WHERE hdct.HopDongChiTietID = @PhanBoId;
			
			IF @DonViTinhPhanBo = 'CPM' 
				SET @SoLuongPhanBoHopDong = @SoLuongPhanBoHopDong*1000  -- 1 CPM = 1000 View
			
			SET @SoLuongThucChayPhanBo = 0;
			SET @ThanhTienThucChayPhanBo = 0;
			
			-- Select so luong thuc chay cua phan bo, thanh tien thuc chay cua phan bo
			SELECT	@SoLuongThucChayPhanBo = SoLuongThucChay, 
					@ThanhTienThucChayPhanBo = (ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
			FROM ThucChayDaTinh AS tcdt
			WHERE tcdt.HopDongChiTietREF = @PhanBoId 
				AND tcdt.NgayThucHien <= @NgayThucHien
				
			PRINT 'SoLuongPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBoHopDong);
			PRINT 'SoHopDong :' + CONVERT(nvarchar(50),@ContractNo)
			PRINT 'PhanBoID :' + CONVERT(nvarchar(50),@PhanBoId)
			PRINT 'WebsiteName :' + CONVERT(nvarchar(50),@SiteName)
			
			-- Uu tien tinh so luong thuc chay truoc.
			SET @TypeInsert = 1
			PRINT '@TypeInsert: ' + CONVERT(NVARCHAR(50), @TypeInsert);
			
			PRINT '@DonViTinhPhanBo: ' + @DonViTinhPhanBo 
				
			-- Neu don vi tinh phan bo la CPC hoac CPM
			IF(@DonViTinhPhanBo = 'CPC' OR @DonViTinhPhanBo = 'CPM')
			BEGIN
				PRINT 'SoLuongThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayPhanBo);
				PRINT 'SoLuongThucChayHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBoHopDong);
				
				IF(@SoLuongThucChayPhanBo < @SoLuongPhanBoHopDong)
				BEGIN
					SET @SoLuongThucChay = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh(@SoLuongThucChaySP,@SoLuongPhanBoHopDong,@DonViTinhHD, @NgayThucHien, @PhanBoId),0)
					PRINT '@NgayThucHien: ' + CONVERT(NVARCHAR(50),@NgayThucHien)				                    
					PRINT '---- SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)
					
					IF @SoLuongThucChay > 0
					BEGIN
						
						PRINT 'Insert ThucChay';
						PRINT 'DonViTinhPhanBo: ' + CONVERT(NVARCHAR(50), @DonViTinhPhanBo);
					
						EXEC dbo.ThucChayDaTinh_InsertThucChayMobileByContractWebsiteUnitName
							@NgayThucHien,
							@ContractNo,
							@PhanBoId,
							@SiteName,
							@DonViTinhHD,
							@BannerType,
							@TongViewThucChay,
							@TongClickThucChay,
							@SoLuongThucChay,
							@DonGiaTheoDonViTinhSP,
							@ThanhTienThucChay,
							@SoLuongThucChayKM,
							@ThanhTienThucChayKM,
							@SoLuongLechTreoHa,
							@ThanhTienLechTreoHa,
							@TypeInsert
					END
					SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChay;
				END
			END
			ELSE -- Nguoc lai don vi tinh phan bo la Goi hoac d/v
			BEGIN
				SET @ThanhTienThucChaySanPham = @SoLuongThucChaySP*@DonGiaSanPham
				
				PRINT 'ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChaySanPham);
				PRINT 'ThanhTienPhanBoHopDong: ' + CONVERT(NVARCHAR(50),@ThanhTienPhanBoHopDong);
				PRINT 'ThanhTienThucChayPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChayPhanBo)
				
				IF @ThanhTienThucChayPhanBo < @ThanhTienPhanBoHopDong
				BEGIN
					IF @ThanhTienThucChayPhanBo + @ThanhTienThucChaySanPham > @ThanhTienPhanBoHopDong
						SET @ThanhTienThucChay = @ThanhTienPhanBoHopDong - @ThanhTienThucChayPhanBo
					ELSE	
						SET @ThanhTienThucChay = @ThanhTienThucChaySanPham;
				
					SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSanPham;

					PRINT 'ThanhTienThucChay: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChay);
						
					IF @ThanhTienThucChay > 0 
					BEGIN
						PRINT 'Insert ThucChay goi' 
							
						EXEC dbo.ThucChayDaTinh_InsertThucChayMobileByContractWebsiteUnitName
							@NgayThucHien,
							@ContractNo,
							@PhanBoId,
							@SiteName,
							@DonViTinhHD,
							@BannerType,
							@TongViewThucChay,
							@TongClickThucChay,
							@SoLuongThucChay,
							@DonGiaTheoDonViTinhSP,
							@ThanhTienThucChay,
							@SoLuongThucChayKM,
							@ThanhTienThucChayKM,
							@SoLuongLechTreoHa,
							@ThanhTienLechTreoHa,
							@TypeInsert
							
						SET @ThanhTienThucChaySanPham	= @ThanhTienThucChaySanPham - @ThanhTienThucChay;
						SET @SoLuongThucChaySP		= @SoLuongThucChaySP - @SoLuongThucChay;
					END
				END
			END
	END
END

```
