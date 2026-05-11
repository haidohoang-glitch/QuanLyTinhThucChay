# Stored Procedure: `ThucChayDaTinh_InsertThucChayMobileContractByContractNo_Banner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-24 17:50:59.987000
- **Ngày sửa cuối**: 2016-02-02 12:13:26.537000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ContractNo` | `nvarchar(100)` | No |
| `@SiteName` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@BannerType` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- EXEC dbo.[ThucChayDaTinh_InsertThucChayMobileContractByContractNo_Banner] '2015-01-21','QC3291214','afamily.vn','CLICK', 4,70731

CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChayMobileContractByContractNo_Banner]
	@NgayThucHien	DATETIME,
	@ContractNo		NVARCHAR(50),
	@SiteName		NVARCHAR(50),
	@DonViTinh		NVARCHAR(50),
	@BannerType		INT,
	@HopDongChiTietID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	
	DECLARE @PhanBoId		INT, 
			@IsKhuyenMai	INT,
			@TypeInsert		INT
			
	DECLARE @SoLuongThucChaySP		INT = 0, 
			@SoLuongDaChay			INT = 0, 
			@SoLuongThucChay		INT = 0, 
			@DonViTinhHD			 NVARCHAR(50),
			@DonViTinhPhanBo		NVARCHAR(50),
			@DonGiaPhanBo			INT,
			@NgayKyHopDong			DATETIME,
			@ExistPhuongPhapSP		INT,
			@GiaTriChietKhauPhanBo	FLOAT,
			@ChietKhauPhanBo		INT,
			@DonGiaSauCK			FLOAT,
			@DonViTinhFinal NVARCHAR(50)
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
			@ThanhTienLechTreoHa		FLOAT = 0,
			@ThanhTienHopDong			FLOAT,
			@ThanhTienThucChayHopDong	FLOAT,
			@ThanhTienThucChayTruocCK	FLOAT
			
	DECLARE @TongViewThucChay		INT = 0,
			@TongClickThucChay		INT = 0,
			@DonGiaSanPham			INT = 0,
			@DonGiaTheoDonViTinhSP	INT = 0,
			@UnitID INT =1

	SET @SoLuongPhanBoHopDong = 0;
	SET @ThanhTienPhanBoHopDong = 0;
							
	PRINT 'ContractNo: ' + CONVERT(NVARCHAR(50), @ContractNo)
	PRINT 'HopDongChiTietID: ' + CONVERT(NVARCHAR(50), @HopDongChiTietID)
	
	IF @DonViTinh = 'CLICK' SET @DonViTinhHD = 'CPC'
	ELSE --IF @DonViTinh = 'VIEW' 
	SET @DonViTinhHD = 'CPM'
		
	SET @SoLuongThucChaySP = 0;
	SET @SoLuongThucChaySP = (
		SELECT	CASE WHEN @DonViTinh = 'VIEW' THEN sum(tcm.TotalView)
					 ELSE sum(tcm.TotalClick)
				END AS SoLuongThucChay
		FROM ThucChayMobileTemp AS tcm
		WHERE tcm.dt = @NgayThucHien 
			AND tcm.[Contract] = @ContractNo 
			AND tcm.SiteName = @SiteName 
			--AND tcm.UnitName = @DonViTinh 	
			AND tcm.BannerType = @BannerType
			AND tcm.HopDongChiTietRER IN(SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	)
	
	PRINT 'SoLuongSP: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySP)
	
	SET @TongViewThucChay = 0;
	SET @TongViewThucChay = (SELECT isnull(sum(tcmt.TotalView),0)
	                          FROM ThucChayMobileTemp AS tcmt	                        
	                          WHERE tcmt.dt = @NgayThucHien
								AND tcmt.[Contract] = @ContractNo
								AND tcmt.SiteName = @SiteName
								AND BannerType	= @BannerType
								AND tcmt.HopDongChiTietRER IN(SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	
								--AND tcmt.UnitName = @DonViTinh							 
	)
	
	SET @TongClickThucChay = 0;
	SET @TongClickThucChay = (SELECT isnull(sum(tcmt.TotalClick),0)
	                          FROM ThucChayMobileTemp AS tcmt	                        
	                          WHERE tcmt.dt = @NgayThucHien
								AND tcmt.[Contract] = @ContractNo
								AND tcmt.SiteName = @SiteName
								AND BannerType	= @BannerType
								AND tcmt.HopDongChiTietRER IN(SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	
								--AND tcmt.UnitName = @DonViTinh							 
	)
	SELECT @DonViTinhHD
	SET @DonGiaSanPham = 0;

	SET @DonGiaSanPham = (
							SELECT TOP 1 dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 342,@BannerType, @DonViTinhHD)																
							--FROM ThucChayMobileTemp AS tcmt	                        
							--WHERE tcmt.dt = @NgayThucHien
							--	AND tcmt.[Contract] = @ContractNo
							--	AND tcmt.SiteName = @SiteName
							--	AND BannerType	= @BannerType
							--	AND tcmt.HopDongChiTietRER IN(SELECT HopDongChiTietID
	      --                                   FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	
							--	AND tcmt.UnitName = @DonViTinh	
	)
	--SELECT tcmt.BannerType, tcmt.UnitName																
	--						FROM ThucChayMobileTemp AS tcmt	                        
	--						WHERE tcmt.dt = @NgayThucHien
	--							AND tcmt.[Contract] = @ContractNo
	--							AND tcmt.SiteName = @SiteName
	--							AND BannerType	= @BannerType
	--							AND tcmt.HopDongChiTietRER IN(SELECT HopDongChiTietID
	--                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	
	--							AND tcmt.UnitName = @DonViTinh	
	SET @DonGiaSanPham = ISNULL(@DonGiaSanPham,0);	
		
	PRINT 'DonGiaSanPham: ' + CONVERT(NVARCHAR(50),@DonGiaSanPham);
	
	SET @NgayKyHopDong = (SELECT hd.NgayKyHopDong
	                       FROM HopDong AS hd WHERE hd.SoHopDong = @ContractNo
	                       )
	
	IF @SoLuongThucChaySP > 0
	BEGIN	
		DECLARE hd_cursor CURSOR FOR
			SELECT hdct.HopDongChiTietID
			FROM HopDong AS hd 
				INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
			WHERE
				hd.SoHopDong			= @ContractNo 
				AND hdct.DmSanPhamREF	= 342 
				AND hdct.DmLoaiREF		<> 13 
				AND hdct.IsKhuyenMai	= 0
				AND hdct.DeletedStatus <> 1
				AND hdct.HopDongChiTietID IN(SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
			ORDER BY hdct.HopDongChiTietID
		--	SET @DonViTinhFinal = (SELECT CASE WHEN @DonViTinh = 'CLICK' THEN 'CPC' ELSE 'CPM' END)
		OPEN hd_cursor
		FETCH NEXT FROM hd_cursor INTO @PhanBoId
		WHILE @@FETCH_STATUS = 0 
		BEGIN		
			
			SELECT  @DonViTinhPhanBo	= DonViTinh,--@DonViTinhFinal,
					@ChietKhauPhanBo	= ChietKhau,
					@SoLuongPhanBoHopDong = ISNULL(SoLuong,0), 
					@ThanhTienPhanBoHopDong = ISNULL(ThanhTien,0),
					@DonGiaPhanBo	= ISNULL(hdct.DonGia,0)
			FROM HopDongChiTiet AS hdct
			WHERE hdct.HopDongChiTietID = @PhanBoId				
			
			PRINT '---- @DonViTinhPhanBo: ' + CONVERT(NVARCHAR(50), @DonViTinhPhanBo)									
			PRINT '---- @ChietKhauPhanBo: ' + CONVERT(NVARCHAR(50), @ChietKhauPhanBo)	
			PRINT '---- @DonGiaPhanBo: ' + CONVERT(NVARCHAR(50), @DonGiaPhanBo)					                          	                          
						                          									
			-- Uu tien tinh so luong thuc chay truoc.
			SET @TypeInsert = 1
		 
			-- Neu don vi tinh phan bo la CPC hoac CPM
			IF(@DonViTinhPhanBo = 'CPC' OR @DonViTinhPhanBo = 'CPM')
			BEGIN
				SET @DonGiaSauCK = @DonGiaPhanBo - @DonGiaPhanBo*@ChietKhauPhanBo/100
			
				IF @DonViTinhPhanBo = 'CPM'
				SET @DonGiaSauCK = @DonGiaSauCK/1000
											
				IF @DonViTinhPhanBo = 'CPM' 
					SET @SoLuongPhanBoHopDong = @SoLuongPhanBoHopDong*1000  -- 1 CPM = 1000 View
			
				-- Select so luong thuc chay cua phan bo, thanh tien thuc chay cua phan bo
				SET @SoLuongThucChayPhanBo = 0;
				SET @ThanhTienThucChayPhanBo = 0;
				
				IF(EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinhMobile AS tcdt WHERE tcdt.HopDongChiTietREF = @PhanBoId))
					BEGIN
						SELECT	@SoLuongThucChayPhanBo = ISNULL(SUM(SoLuongThucChay),0), 
								@ThanhTienThucChayPhanBo = ISNULL(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi),0)
						FROM ThucChayDaTinhMobile AS tcdt
						WHERE tcdt.HopDongChiTietREF = @PhanBoId 
							AND tcdt.NgayThucHien <= @NgayThucHien
					END				
			
				PRINT 'SoLuongThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayPhanBo);
				
				PRINT 'SoHopDong :' + CONVERT(nvarchar(50),@ContractNo)
				PRINT 'PhanBoID :' + CONVERT(nvarchar(50),@PhanBoId)
				PRINT '@DonViTinhHD :' + CONVERT(nvarchar(50),@DonViTinhHD)
				PRINT 'SoLuongPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBoHopDong);
				PRINT 'WebsiteName :' + CONVERT(nvarchar(50),@SiteName)
			
				
				
				IF(EXISTS(SELECT tcdt.HopDongID FROM ThucChayDaTinhMobile AS tcdt WHERE tcdt.SoHopDong = @ContractNo AND tcdt.DmSanPhamREF = 342 AND tcdt.HopDongChiTietREF = 0))
					SET @ExistPhuongPhapSP = 1
				ELSE
					SET @ExistPhuongPhapSP = 0
					
				PRINT 'ExistPhuongPhapSP: ' + CONVERT(NVARCHAR(50),@ExistPhuongPhapSP)				
				PRINT '@SoLuongPhanBoHopDong: ' + CONVERT(NVARCHAR(50),@SoLuongPhanBoHopDong)
				PRINT '@SoLuongPhanBoHopDong: ' + CONVERT(NVARCHAR(50),@SoLuongThucChayPhanBo)

				IF(@SoLuongPhanBoHopDong > 0 AND @SoLuongThucChayPhanBo < @SoLuongPhanBoHopDong)
				BEGIN
					IF @ExistPhuongPhapSP = 0
					BEGIN
						SET @SoLuongThucChay = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_Mobile(@SoLuongThucChaySP,@SoLuongPhanBoHopDong,@DonViTinhHD, @NgayThucHien, @PhanBoId),0)
						PRINT '@NgayThucHien: ' + CONVERT(NVARCHAR(50),@NgayThucHien)				                    
						PRINT '---- SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)
						
						--SET @ThanhTienThucChay = dbo.ThucChay_GetThanhTienChuanThucChay(@SoLuongPhanBoHopDong,@DonViTinhPhanBo,@DonGiaPhanBo,@NgayKyHopDong,@SoLuongThucChay,@SoLuongThucChay,0,@NgayThucHien,@PhanBoId)
						SET @ThanhTienThucChayTruocCK = dbo.ThucChay_GetThanhTienChuanThucChay_Mobile(@SoLuongPhanBoHopDong,@DonViTinhPhanBo,@DonGiaPhanBo,@NgayKyHopDong,@SoLuongThucChay,@SoLuongThucChay,@BannerType,@NgayThucHien,@PhanBoId)
						SET @ThanhTienThucChay = @ThanhTienThucChayTruocCK - (@ThanhTienThucChayTruocCK*@ChietKhauPhanBo/100)												
						
						PRINT '---- @ThanhTienThucChayTruocCK: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayTruocCK)
						PRINT '---- ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay)
						PRINT '---- @ThanhTienThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayPhanBo)
						PRINT '---- @ThanhTienPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienPhanBoHopDong)
						PRINT '---- @DonGiaSauCK: ' + CONVERT(NVARCHAR(50), @DonGiaSauCK)

						IF (@ThanhTienThucChayPhanBo < @ThanhTienPhanBoHopDong )
						BEGIN
							IF @ThanhTienThucChayPhanBo + @ThanhTienThucChay > @ThanhTienPhanBoHopDong
							BEGIN
								SET @ThanhTienThucChay = @ThanhTienPhanBoHopDong - @ThanhTienThucChayPhanBo
								PRINT '111'
								IF @DonGiaSauCK <> 0
								SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK
								PRINT '---- SoLuongThucChay11: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)
							END	
							ELSE
								BEGIN
									SET @ThanhTienThucChay = @ThanhTienThucChay
									PRINT '222'
								END
							IF @DonGiaSauCK <> 0
							SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK
							PRINT '---- @ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay)
							PRINT '---- @DonGiaPhanBo: ' + CONVERT(NVARCHAR(50), @DonGiaPhanBo)
							PRINT '---- SoLuongThucChay22: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)		
						END
						ELSE
							BEGIN
								SET @SoLuongThucChay = 0
								PRINT '---- SoLuongThucChay33: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)
							END
							
					END
					ELSE
					BEGIN
						SET @ThanhTienThucChayHopDong = 0;
						SET @ThanhTienHopDong = 0;
						
						SET @ThanhTienThucChayTruocCK = dbo.ThucChay_GetThanhTienChuanThucChay(@SoLuongPhanBoHopDong,@DonViTinhPhanBo,@DonGiaPhanBo,@NgayKyHopDong,@SoLuongThucChaySP,@SoLuongThucChaySP,0,@NgayThucHien,@PhanBoId)
						SET @ThanhTienThucChay = @ThanhTienThucChayTruocCK - (@ThanhTienThucChayTruocCK*@ChietKhauPhanBo/100)					
						
						PRINT '---- @ThanhTienThucChayTruocCK: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayTruocCK)
						PRINT '---- ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay)
						PRINT '---- @ThanhTienThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayPhanBo)
						PRINT '---- @ThanhTienPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienPhanBoHopDong)
						
						-- SELECT THANH TIEN HOP DONG
						SELECT @ThanhTienHopDong = SUM(ThanhTien)
						FROM HopDong AS hd INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
						WHERE hd.SoHopDong = @ContractNo AND hdct.DmSanPhamREF = 342 AND hdct.IsKhuyenMai = 0
						
						-- SELECT THANH TIEN THUC CHAY THEO HOP DONG
						SELECT @ThanhTienThucChayHopDong = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
						FROM ThucChayDaTinhMobile AS tcdt
						WHERE tcdt.SoHopDong = @ContractNo AND tcdt.DmSanPhamREF = 342 AND tcdt.NgayThucHien <= @NgayThucHien
						
						PRINT '---- @ThanhTienThucChayHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChayHopDong)
						PRINT '---- @ThanhTienHopDong: ' + CONVERT(NVARCHAR(50), @ThanhTienHopDong)
						
						IF @ThanhTienThucChayHopDong < @ThanhTienHopDong 
						BEGIN
							IF @ThanhTienThucChayHopDong + @ThanhTienThucChay > @ThanhTienHopDong
							BEGIN
								SET @ThanhTienThucChay = @ThanhTienHopDong - @ThanhTienThucChayHopDong;
								PRINT '111'
							END							
							ELSE
								BEGIN
									SET @ThanhTienThucChay = @ThanhTienThucChay
									PRINT '222'
								END
							IF @DonGiaSauCK <> 0
							SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK
						END
						
						PRINT '---- @ThanhTienThucChay: ' + CONVERT(NVARCHAR(50), @ThanhTienThucChay)
						PRINT '---- @DonGiaPhanBo: ' + CONVERT(NVARCHAR(50), @DonGiaPhanBo)
						PRINT '---- SoLuongThucChay22: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)
					END
					IF @SoLuongThucChay > 0
					BEGIN
						
						PRINT 'Insert ThucChay';
						PRINT 'DonViTinhPhanBo: ' + CONVERT(NVARCHAR(50), @DonViTinhPhanBo);
					
						EXEC dbo.ThucChayDaTinh_InsertThucChayMobileByContractWebsiteUnitName
							@NgayThucHien,
							@ContractNo,
							@PhanBoId,
							@SiteName,
							@DonViTinhPhanBo,
							@BannerType,
							@TongViewThucChay,
							@TongClickThucChay,
							@SoLuongThucChay,
							@DonGiaTheoDonViTinhSP,
							@ThanhTienThucChayTruocCK,
							@SoLuongThucChayKM,
							@ThanhTienThucChayKM,
							@SoLuongLechTreoHa,
							@ThanhTienLechTreoHa,
							@TypeInsert
					END
					SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChay;
					PRINT '@SoLuongThucChaySP: ' + CONVERT(NVARCHAR(50),@SoLuongThucChaySP)
				END
			END
			ELSE -- Nguoc lai don vi tinh phan bo la Goi hoac d/v
			BEGIN
				PRINT 'Nguoc lai don vi tinh phan bo la Goi hoac d/v'
				PRINT '@SoLuongThucChaySP: ' + CONVERT(NVARCHAR(50),@SoLuongThucChaySP);
				PRINT '@BannerType: ' + CONVERT(NVARCHAR(50),@BannerType);
				PRINT '@DonGiaSanPham: ' + CONVERT(NVARCHAR(50),@DonGiaSanPham);
				
				SET @DonGiaSauCK = @DonGiaSanPham - @DonGiaSanPham*@ChietKhauPhanBo/100
				SET @ThanhTienThucChayTruocCK = @SoLuongThucChaySP*@DonGiaSanPham
				SET @DonGiaTheoDonViTinhSP = @DonGiaSanPham
				SET @DonViTinhPhanBo = @DonViTinh
				SET @ThanhTienThucChayPhanBo = 0
				SET @ThanhTienThucChaySanPham = @ThanhTienThucChayTruocCK -(@ThanhTienThucChayTruocCK*@ChietKhauPhanBo/100)
				IF(EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinhMobile AS tcdt WHERE tcdt.HopDongChiTietREF = @PhanBoId))
				BEGIN
					SELECT	@SoLuongThucChayPhanBo = ISNULL(SUM(SoLuongThucChay),0), 
							@ThanhTienThucChayPhanBo = ISNULL(SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0)
					FROM ThucChayDaTinhMobile AS tcdt
					WHERE tcdt.HopDongChiTietREF = @PhanBoId 
						AND tcdt.NgayThucHien <= @NgayThucHien
				END		
				PRINT 'ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChaySanPham);
				PRINT 'ThanhTienPhanBoHopDong: ' + CONVERT(NVARCHAR(50),@ThanhTienPhanBoHopDong);
				PRINT 'ThanhTienThucChayPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChayPhanBo)
				
				IF @ThanhTienThucChayPhanBo < @ThanhTienPhanBoHopDong
				BEGIN
					PRINT 'check'
					IF @ThanhTienThucChayPhanBo + @ThanhTienThucChaySanPham > @ThanhTienPhanBoHopDong
						SET @ThanhTienThucChay = @ThanhTienPhanBoHopDong - @ThanhTienThucChayPhanBo
					ELSE	
						SET @ThanhTienThucChay = @ThanhTienThucChaySanPham;
						PRINT 'ThanhTienThucChay: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChay);
					PRINT '@@ThanhTienThucChay: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChay);
					PRINT '@@@DonGiaSauCK: ' + CONVERT(NVARCHAR(50),@DonGiaSauCK);
					
					IF @DonGiaSauCK <> 0
					SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK;
					
						
					IF @ThanhTienThucChay > 0 
					BEGIN
						PRINT 'Insert ThucChay goi' 
							
						EXEC dbo.ThucChayDaTinh_InsertThucChayMobileByContractWebsiteUnitName
							@NgayThucHien,
							@ContractNo,
							@PhanBoId,
							@SiteName,
							@DonViTinhPhanBo,
							@BannerType,
							@TongViewThucChay,
							@TongClickThucChay,
							@SoLuongThucChay,
							@DonGiaTheoDonViTinhSP,
							@ThanhTienThucChayTruocCK,
							@SoLuongThucChayKM,
							@ThanhTienThucChayKM,
							@SoLuongLechTreoHa,
							@ThanhTienLechTreoHa,
							@TypeInsert
							
						--SET @ThanhTienThucChaySanPham	= @ThanhTienThucChaySanPham - @ThanhTienThucChay;
						SET @ThanhTienThucChayTruocCK = @ThanhTienThucChayTruocCK - (@ThanhTienThucChay*100/(100-@ChietKhauPhanBo))
						SET @SoLuongThucChaySP		= @SoLuongThucChaySP - @SoLuongThucChay;
					END
				END
			END
			FETCH NEXT FROM hd_cursor INTO @PhanBoId
		END
		
		PRINT '---- SoLuongThucChay - con lai: ' + CONVERT(NVARCHAR(50), @SoLuongThucChaySP)
		CLOSE hd_cursor;
		DEALLOCATE hd_cursor;
		
		-- Neu so luong thuc chay con lai van > 0 sau khi tinh cho cac phan bo trong hop dong
		IF @SoLuongThucChaySP > 0 
		BEGIN
			DECLARE @SoLuongKhuyenMaiPhanBo		INT = 0,
					@SoLuongThucChayKMPhanBo	INT = 0
					
			SET @TypeInsert = 2		
			SET @SoLuongThucChay = 0;
			SET @ThanhTienThucChay = 0;
			SET @SoLuongLechTreoHa = 0;
			SET @ThanhTienLechTreoHa = 0;
						
			DECLARE km_cursor CURSOR FOR
			SELECT hdct.HopDongChiTietID
			FROM HopDong AS hd 
				INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
			WHERE
				hd.SoHopDong			= @ContractNo 
				AND hdct.DmSanPhamREF	= 342 
				AND hdct.IsKhuyenMai	= 1
			ORDER BY hdct.HopDongChiTietID 
			
			OPEN km_cursor 
			FETCH NEXT FROM km_cursor INTO @PhanBoId
			WHILE @@FETCH_STATUS = 0
			BEGIN				
				SET @DonViTinhPhanBo = (
											SELECT DonViTinh 
											FROM HopDongChiTiet AS hdct 
											WHERE hdct.HopDongChiTietID = @PhanBoId
										)
				
				SELECT 
					@SoLuongKhuyenMaiPhanBo		= ISNULL(SoLuong,0), 
					@ThanhTienKhuyenMaiPhanBo	= ISNULL(hdct.SoLuong*hdct.DonGia,0)
				FROM HopDongChiTiet AS hdct
				WHERE hdct.HopDongChiTietID = @PhanBoId
				
				IF @DonViTinhPhanBo = 'CPM'
					SET @SoLuongKhuyenMaiPhanBo = @SoLuongKhuyenMaiPhanBo*1000 -- 1 CPM = 1000 View
				
				IF(EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinhMobile AS tcdt WHERE tcdt.HopDongChiTietREF = @PhanBoId))
				BEGIN
					SELECT 
						@SoLuongThucChayKMPhanBo	= SUM(ISNULL(SoLuongThucChayKM,0)), 
						@ThanhTienThucChayPhanBoKM	= SUM(ISNULL(ThanhTienKM,0))
					FROM ThucChayDaTinhMobile AS tcdt
					WHERE tcdt.HopDongChiTietREF = @PhanBoId AND tcdt.NgayThucHien <= @NgayThucHien
				END
				
				IF (@DonViTinhPhanBo = 'CPM' OR @DonViTinhPhanBo = 'CPC')
				BEGIN
					PRINT 'SoLuongKhuyenMaiPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongKhuyenMaiPhanBo);
					PRINT 'SoLuongThucChayKMPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKMPhanBo);
					
					IF @SoLuongKhuyenMaiPhanBo > @SoLuongThucChayKMPhanBo
					BEGIN
						SET @SoLuongThucChayKM = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh(@SoLuongThucChaySP,@SoLuongKhuyenMaiPhanBo,@DonViTinhHD, @NgayThucHien, @PhanBoId),0)
						
						PRINT '**** Insert ThucChayKhuyenMai';
						PRINT 'SoLuongThucChayKM: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKM);
						PRINT 'TypeInsert: ' + CONVERT(NVARCHAR(50),@TypeInsert);
						
						EXEC dbo.ThucChayDaTinh_InsertThucChayMobileByContractWebsiteUnitName
							@NgayThucHien,
							@ContractNo,
							@PhanBoId,
							@SiteName,
							@DonViTinhPhanBo,
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
							
						SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChayKM;
					END
					ELSE
						SET @SoLuongThucChayKM = 0
				END
				ELSE
				BEGIN
					PRINT 'ThanhTienKhuyenMaiPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienKhuyenMaiPhanBo);
					PRINT 'ThanhTienThucChayKMPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChayPhanBoKM);
					PRINT 'TypeInsert: ' + CONVERT(NVARCHAR(50),@TypeInsert);
					IF @ThanhTienThucChayPhanBoKM < @ThanhTienKhuyenMaiPhanBo 
					BEGIN
						IF @ThanhTienThucChayPhanBoKM + @ThanhTienThucChaySanPham > @ThanhTienKhuyenMaiPhanBo
							SET @ThanhTienThucChayKM = @ThanhTienThucChayPhanBo - @ThanhTienThucChaySanPham
						ELSE	
							SET @ThanhTienThucChayKM = @ThanhTienThucChaySanPham
						IF @DonGiaSanPham <> 0
						SET @SoLuongThucChayKM = @ThanhTienThucChayKM/@DonGiaSanPham;
						
						IF @ThanhTienThucChayKM > 0
						BEGIN
							PRINT '***** Insert ThucChayKhuyenMai';
							EXEC dbo.ThucChayDaTinh_InsertThucChayMobileByContractWebsiteUnitName
								@NgayThucHien,
								@ContractNo,
								@PhanBoId,
								@SiteName,
								@DonViTinhPhanBo,
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
								
							SET @ThanhTienThucChaySanPham = @ThanhTienThucChaySanPham - @ThanhTienThucChayKM;
							SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChayKM
						END
						ELSE 
							SET @SoLuongThucChayKM = 0
					END
				END
				
				FETCH NEXT FROM km_cursor INTO @PhanBoId
			END
			CLOSE km_cursor;
			DEALLOCATE km_cursor;
		END
		
		PRINT '@SoLuongThucChaySP: ' + CONVERT(NVARCHAR(50),@SoLuongThucChaySP);
		-- Neu so luong thuc chay con lai van > 0 sau khi tinh cho cac phan bo trong hop dong thi se insert vao gia tri lech treo ha
		IF @SoLuongThucChaySP > 0 
		BEGIN
			SET @TypeInsert = 3
			SET @PhanBoId = (SELECT TOP 1 hdct.HopDongChiTietID
								FROM HopDong AS hd 
									INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
								WHERE
									hd.SoHopDong			= @ContractNo 
									AND hdct.DmSanPhamREF	= 342 
									AND NOT (hdct.DmLoaiREF		= 13 OR hdct.DmLoaiBannerREF IN (17,18)) 
									AND hdct.IsKhuyenMai	= 0
								ORDER BY hdct.HopDongChiTietID DESC
							)   
			
			SET @SoLuongThucChay = 0
			SET @SoLuongThucChayKM = 0				
			SET @SoLuongLechTreoHa = @SoLuongThucChaySP
			SET @ThanhTienLechTreoHa = @ThanhTienThucChaySanPham
			
			PRINT 'Insert ThucChayLechTreoHa';
			PRINT '@@SoLuongLechTreoHa: ' + CONVERT(NVARCHAR(50),@SoLuongLechTreoHa);
							
			EXEC dbo.ThucChayDaTinh_InsertThucChayMobileByContractWebsiteUnitName
				@NgayThucHien,
				@ContractNo,
				@PhanBoId,
				@SiteName,
				@DonViTinhPhanBo,
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
	END
END

```
