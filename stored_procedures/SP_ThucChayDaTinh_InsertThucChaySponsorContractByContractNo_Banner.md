# Stored Procedure: `ThucChayDaTinh_InsertThucChaySponsorContractByContractNo_Banner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-01 15:49:15.573000
- **Ngày sửa cuối**: 2015-04-10 10:26:32.880000

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
-- EXEC dbo.ThucChayDaTinh_InsertThucChaySponsorContractByContractNo_v3 '2014-04-28','QC2170314','cafebiz.vn','VIEW', 4

CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChaySponsorContractByContractNo_Banner]
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
			@DonGiaSauCK			FLOAT
			
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
			@UnitID NVARCHAR(50)
	
	IF @DonViTinh = 'CLICK' SET @DonViTinhHD = 'CPC'
		ELSE SET @DonViTinhHD = 'CPM'
	
	SET @SoLuongThucChaySP = 0;
	SET @SoLuongThucChaySP = (
		SELECT	CASE WHEN @DonViTinh = 'VIEW' THEN sum(tcm.TotalView)
					 ELSE sum(tcm.TotalClick)
				END AS SoLuongThucChay
		FROM ThucChaySponsorTemp AS tcm
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
	                          FROM ThucChaySponsorTemp AS tcmt	                        
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
	                          FROM ThucChaySponsorTemp AS tcmt	                        
	                          WHERE tcmt.dt = @NgayThucHien
								AND tcmt.[Contract] = @ContractNo
								AND tcmt.SiteName = @SiteName
								AND BannerType	= @BannerType
								AND tcmt.HopDongChiTietRER IN(SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	
								--AND tcmt.UnitName = @DonViTinh							 
	)
	
	SET @DonGiaSanPham = 0;
	SET @DonGiaSanPham = (
							SELECT TOP 1 dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, tcmt.BannerType, tcmt.UnitID)																
							FROM ThucChaySponsorTemp AS tcmt	                        
							WHERE tcmt.dt = @NgayThucHien
								AND tcmt.[Contract] = @ContractNo
								AND tcmt.SiteName = @SiteName
								AND BannerType	= @BannerType
								AND tcmt.HopDongChiTietRER IN(SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
	
								--AND tcmt.UnitName = @DonViTinh	
	)
	SET @DonGiaSanPham = ISNULL(@DonGiaSanPham,0);
	
	IF @DonViTinh = 'CLICK' SET @UnitID = 'CPC'
	ELSE IF @DonViTinh = 'VIEW' SET @UnitID = 'CPM'
	
	SET @DonGiaTheoDonViTinhSP = 0;
	SET @DonGiaTheoDonViTinhSP = (
							SELECT distinct
								CASE WHEN @BannerType = 2 THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)
									 WHEN @BannerType = 3 AND @DonViTinh = 'CLICK' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)
									 WHEN @BannerType = 3 AND @DonViTinh = 'VIEW' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)/1000
									 WHEN @BannerType = 4 AND @DonViTinh = 'CLICK' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)
									 WHEN @BannerType = 4 AND @DonViTinh = 'VIEW' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)/1000
									 WHEN @BannerType = 5 THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)
									 WHEN @BannerType = 10 AND @DonViTinh = 'CLICK' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)
									 WHEN @BannerType = 10 AND @DonViTinh = 'VIEW' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)/1000
									 WHEN @BannerType = 14 AND @DonViTinh = 'CLICK' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)
									 WHEN @BannerType = 14 AND @DonViTinh = 'VIEW' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(@NgayThucHien, 381, @BannerType, @UnitID)/1000
									 ELSE 0
								END
							--FROM ThucChaySponsorTemp AS tcmt	                        
							--WHERE tcmt.dt = @NgayThucHien
							--	AND tcmt.[Contract] = @ContractNo
							--	AND tcmt.SiteName = @SiteName
							--	AND BannerType	= @BannerType
							--	AND tcmt.UnitName = @DonViTinh	
	)
	SET @DonGiaTheoDonViTinhSP = ISNULL(@DonGiaTheoDonViTinhSP,0);
	
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
				AND hdct.DmSanPhamREF	= 381 
				AND hdct.DmLoaiREF		<> 13 
				AND hdct.IsKhuyenMai	= 0
				AND hdct.DeletedStatus <> 1
				AND hdct.HopDongChiTietID IN(SELECT HopDongChiTietID
	                                         FROM   dbo.ThucChay_GetHopDongChiTietChungBanner(@HopDongChiTietID))
			ORDER BY hdct.HopDongChiTietID
			
		OPEN hd_cursor
		FETCH NEXT FROM hd_cursor INTO @PhanBoId
		WHILE @@FETCH_STATUS = 0 
		BEGIN		
			
			SELECT	@DonViTinhPhanBo	= DonViTinh,
					@DonGiaPhanBo		= DonGia,
					@ChietKhauPhanBo	= ChietKhau
			FROM HopDongChiTiet AS hdct
			WHERE hdct.HopDongChiTietID = @PhanBoId	
			
			PRINT '---- @DonViTinhPhanBo: ' + CONVERT(NVARCHAR(50), @DonViTinhPhanBo)									
			PRINT '---- @ChietKhauPhanBo: ' + CONVERT(NVARCHAR(50), @ChietKhauPhanBo)	
			PRINT '---- @DonGiaPhanBo: ' + CONVERT(NVARCHAR(50), @DonGiaPhanBo)					                          
						                          
			SET @DonGiaSauCK = @DonGiaPhanBo- @DonGiaPhanBo*@ChietKhauPhanBo/100
			
			IF @DonViTinhPhanBo = 'CPM'
				SET @DonGiaSauCK = @DonGiaSauCK/1000

			PRINT '---- @DonGiaSauCK: ' + CONVERT(NVARCHAR(50), @DonGiaSauCK)				                          
						                          									
			-- Uu tien tinh so luong thuc chay truoc.
			SET @TypeInsert = 1
			
			-- Neu don vi tinh phan bo la CPC hoac CPM
			IF(@DonViTinhPhanBo = 'CPC' OR @DonViTinhPhanBo = 'CPM')
			BEGIN

				-- Select so luong cua phan bo, thanh tien cua phan bo
				SET @SoLuongPhanBoHopDong = 0;
				SET @ThanhTienPhanBoHopDong = 0;
				
				SELECT	@SoLuongPhanBoHopDong = ISNULL(SoLuong,0), 
						@ThanhTienPhanBoHopDong = ISNULL(ThanhTien,0),
						@DonGiaPhanBo	= ISNULL(hdct.DonGia,0)
				FROM HopDongChiTiet AS hdct
				WHERE hdct.HopDongChiTietID = @PhanBoId
					AND hdct.DonViTinh = @DonViTinhHD;
			
				IF @DonViTinhPhanBo = 'CPM' 
					SET @SoLuongPhanBoHopDong = @SoLuongPhanBoHopDong*1000  -- 1 CPM = 1000 View
			
				-- Select so luong thuc chay cua phan bo, thanh tien thuc chay cua phan bo
				SET @SoLuongThucChayPhanBo = 0;
				SET @ThanhTienThucChayPhanBo = 0;
				
				IF(EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinhSponsorBanner AS tcdt WHERE tcdt.HopDongChiTietREF = @PhanBoId))
				BEGIN
					SELECT	@SoLuongThucChayPhanBo = SUM(ISNULL(SoLuongThucChay,0)), 
							@ThanhTienThucChayPhanBo = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
					FROM ThucChayDaTinhSponsorBanner AS tcdt
					WHERE tcdt.HopDongChiTietREF = @PhanBoId 
						AND tcdt.NgayThucHien <= @NgayThucHien
				END				
					
				PRINT 'SoLuongThucChayPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayPhanBo);
				
				PRINT 'SoHopDong :' + CONVERT(nvarchar(50),@ContractNo)
				PRINT 'PhanBoID :' + CONVERT(nvarchar(50),@PhanBoId)
				PRINT '@DonViTinhHD :' + CONVERT(nvarchar(50),@DonViTinhHD)
				PRINT 'SoLuongPhanBoHopDong: ' + CONVERT(NVARCHAR(50), @SoLuongPhanBoHopDong);
				PRINT 'WebsiteName :' + CONVERT(nvarchar(50),@SiteName)
			
				
				
				IF(EXISTS(SELECT tcdt.HopDongID FROM ThucChayDaTinhSponsorBanner AS tcdt WHERE tcdt.SoHopDong = @ContractNo AND tcdt.DmSanPhamREF = 381 AND tcdt.HopDongChiTietREF = 0))
					SET @ExistPhuongPhapSP = 1
				ELSE
					SET @ExistPhuongPhapSP = 0
					
				PRINT 'ExistPhuongPhapSP: ' + CONVERT(NVARCHAR(50),@ExistPhuongPhapSP)				
					
				IF(@SoLuongPhanBoHopDong > 0 AND @SoLuongThucChayPhanBo < @SoLuongPhanBoHopDong)
				BEGIN
					IF @ExistPhuongPhapSP = 0
					BEGIN
						PRINT '@SoLuongThucChaySP ' + CONVERT(NVARCHAR(50),@SoLuongThucChaySP)
						SET @SoLuongThucChay = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_Sponsor(@SoLuongThucChaySP,@SoLuongPhanBoHopDong,@DonViTinhHD, @NgayThucHien, @PhanBoId),0)
						PRINT '@NgayThucHien: ' + CONVERT(NVARCHAR(50),@NgayThucHien)				                    
						PRINT '---- SoLuongThucChay: ' + CONVERT(NVARCHAR(50), @SoLuongThucChay)
						
						--SET @ThanhTienThucChay = dbo.ThucChay_GetThanhTienChuanThucChay_(@SoLuongPhanBoHopDong,@DonViTinhPhanBo,@DonGiaPhanBo,@NgayKyHopDong,@SoLuongThucChay,@SoLuongThucChay,0,@NgayThucHien,@PhanBoId)
						SET @ThanhTienThucChayTruocCK = dbo.ThucChay_GetThanhTienChuanThucChay_Sponsor(@SoLuongPhanBoHopDong,@DonViTinhPhanBo,@DonGiaPhanBo,@NgayKyHopDong,@SoLuongThucChay,@SoLuongThucChay,0,@NgayThucHien,@PhanBoId)
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
						WHERE hd.SoHopDong = @ContractNo AND hdct.DmSanPhamREF = 381 AND hdct.IsKhuyenMai = 0
						
						-- SELECT THANH TIEN THUC CHAY THEO HOP DONG
						SELECT @ThanhTienThucChayHopDong = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
						FROM ThucChayDaTinhSponsorBanner AS tcdt
						WHERE tcdt.SoHopDong = @ContractNo AND tcdt.DmSanPhamREF = 381 AND tcdt.NgayThucHien <= @NgayThucHien
						
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
					
						EXEC dbo.ThucChayDaTinh_InsertThucChaySponsorByContractWebsiteUnitName
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
				--SET @ThanhTienThucChaySanPham = @SoLuongThucChaySP*@DonGiaSanPham
				SET @ThanhTienThucChayTruocCK = @SoLuongThucChaySP*@DonGiaSanPham
				
				SET @ThanhTienThucChaySanPham = @ThanhTienThucChayTruocCK -(@ThanhTienThucChayTruocCK*@ChietKhauPhanBo/100)
				
				PRINT 'ThanhTienThucChaySanPham: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChaySanPham);
				PRINT 'ThanhTienPhanBoHopDong: ' + CONVERT(NVARCHAR(50),@ThanhTienPhanBoHopDong);
				PRINT 'ThanhTienThucChayPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChayPhanBo)
				
				IF @ThanhTienThucChayPhanBo < @ThanhTienPhanBoHopDong
				BEGIN
					IF @ThanhTienThucChayPhanBo + @ThanhTienThucChaySanPham > @ThanhTienPhanBoHopDong
						SET @ThanhTienThucChay = @ThanhTienPhanBoHopDong - @ThanhTienThucChayPhanBo
					ELSE	
						SET @ThanhTienThucChay = @ThanhTienThucChaySanPham;
					IF @DonGiaSauCK <> 0
					SET @SoLuongThucChay = @ThanhTienThucChay/@DonGiaSauCK;

					PRINT 'ThanhTienThucChay: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChay);
						
					IF @ThanhTienThucChay > 0 
					BEGIN
						PRINT 'Insert ThucChay goi' 
							
						EXEC dbo.ThucChayDaTinh_InsertThucChaySponsorByContractWebsiteUnitName
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
				AND hdct.DmSanPhamREF	= 381 
				AND hdct.DmLoaiREF		<> 13 
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
				
				IF(EXISTS(SELECT HopDongChiTietREF FROM ThucChayDaTinhSponsorBanner AS tcdt WHERE tcdt.HopDongChiTietREF = @PhanBoId))
				BEGIN
					SELECT 
						@SoLuongThucChayKMPhanBo	= SUM(ISNULL(SoLuongThucChayKM,0)), 
						@ThanhTienThucChayPhanBoKM	= SUM(ISNULL(ThanhTienKM,0))
					FROM ThucChayDaTinhSponsorBanner AS tcdt
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
						
						EXEC dbo.ThucChayDaTinh_InsertThucChaySponsorByContractWebsiteUnitName
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
							EXEC dbo.ThucChayDaTinh_InsertThucChaySponsorByContractWebsiteUnitName
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
									AND hdct.DmSanPhamREF	= 381 
									AND hdct.DmLoaiREF		<> 13 
									AND hdct.IsKhuyenMai	= 0
								ORDER BY hdct.HopDongChiTietID DESC
							)   
			
			SET @SoLuongThucChay = 0
			SET @SoLuongThucChayKM = 0				
			SET @SoLuongLechTreoHa = @SoLuongThucChaySP
			SET @ThanhTienLechTreoHa = @ThanhTienThucChaySanPham
			
			PRINT 'Insert ThucChayLechTreoHa';
			PRINT '@@SoLuongLechTreoHa: ' + CONVERT(NVARCHAR(50),@SoLuongLechTreoHa);
							
			EXEC dbo.ThucChayDaTinh_InsertThucChaySponsorByContractWebsiteUnitName
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
