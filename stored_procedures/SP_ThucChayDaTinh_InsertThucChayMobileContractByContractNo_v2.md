# Stored Procedure: `ThucChayDaTinh_InsertThucChayMobileContractByContractNo_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-21 11:34:40.560000
- **Ngày sửa cuối**: 2014-11-19 12:24:59.603000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ContractNo` | `nvarchar(100)` | No |
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
-- EXEC dbo.ThucChayDaTinh_InsertThucChayMobileContractByContractNo_v2 '2014-05-27','QC260413','dantri.com.vn','VIEW', 3
CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChayMobileContractByContractNo_v2]
	@NgayThucHien	DATETIME,
	@ContractNo		NVARCHAR(50),
	@SiteName		NVARCHAR(50),
	@DonViTinh		NVARCHAR(50),
	@BannerType		INT
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
		DECLARE hd_cursor CURSOR FOR
			SELECT hdct.HopDongChiTietID
			FROM HopDong AS hd 
				INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
			WHERE
				hd.SoHopDong			= @ContractNo 
				AND hdct.DmSanPhamREF	= 342 
				AND hdct.DmLoaiREF		<> 13 
				AND hdct.IsKhuyenMai	= 0
			ORDER BY hdct.HopDongChiTietID
			
		OPEN hd_cursor
		FETCH NEXT FROM hd_cursor INTO @PhanBoId
		WHILE @@FETCH_STATUS = 0 
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
			
			-- Select so luong thuc chay cua phan bo, thanh tien thuc chay cua phan bo
			SELECT	@SoLuongThucChayPhanBo = ISNULL(SoLuongThucChay,0), 
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
			FETCH NEXT FROM hd_cursor INTO @PhanBoId
		END
		
		CLOSE hd_cursor;
		DEALLOCATE hd_cursor;
		
		-- Neu so luong thuc chay con lai van > 0 sau khi tinh cho cac phan bo trong hop dong
		IF @SoLuongThucChaySP > 0 
		BEGIN
			DECLARE @SoLuongKhuyenMaiPhanBo		INT = 0,
					@SoLuongThucChayKMPhanBo	INT = 0
					
			SET @TypeInsert = 2		
			PRINT 'TypeInsert: ' + CONVERT(NVARCHAR(50),@TypeInsert);
			
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
				
				SELECT 
					@SoLuongThucChayKMPhanBo	= ISNULL(SoLuongThucChayKM,0), 
					@ThanhTienThucChayPhanBoKM	= ISNULL(ThanhTienKM,0)
				FROM ThucChayDaTinh AS tcdt
				WHERE tcdt.HopDongChiTietREF = @PhanBoId AND tcdt.NgayThucHien <= @NgayThucHien
				
				IF (@DonViTinhPhanBo = 'CPM' OR @DonViTinhPhanBo = 'CPC')
				BEGIN
					PRINT 'SoLuongKhuyenMaiPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongKhuyenMaiPhanBo);
					PRINT 'SoLuongThucChayKMPhanBo: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKMPhanBo);
					
					IF @SoLuongKhuyenMaiPhanBo > @SoLuongThucChayKMPhanBo
					BEGIN
						PRINT 'Insert ThucChayKhuyenMai';
						
						SET @SoLuongThucChayKM = ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh(@SoLuongThucChaySP,@SoLuongKhuyenMaiPhanBo,@DonViTinhHD, @NgayThucHien, @PhanBoId),0)
					
						PRINT 'SoLuongThucChayKM: ' + CONVERT(NVARCHAR(50), @SoLuongThucChayKM);
						
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
							
						SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChayKM;
					END
				END
				ELSE
				BEGIN
					PRINT 'ThanhTienKhuyenMaiPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienKhuyenMaiPhanBo);
					PRINT 'ThanhTienThucChayKMPhanBo: ' + CONVERT(NVARCHAR(50),@ThanhTienThucChayPhanBoKM);
					
					IF @ThanhTienThucChayPhanBoKM < @ThanhTienKhuyenMaiPhanBo 
					BEGIN
						IF @ThanhTienThucChayPhanBoKM + @ThanhTienThucChaySanPham > @ThanhTienKhuyenMaiPhanBo
							SET @ThanhTienThucChayKM = @ThanhTienThucChayPhanBo - @ThanhTienThucChaySanPham
						ELSE	
							SET @ThanhTienThucChayKM = @ThanhTienThucChaySanPham
					
						SET @SoLuongThucChayKM = @ThanhTienThucChayKM/@DonGiaSanPham;
						
						IF @ThanhTienThucChayKM > 0
						BEGIN
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
								
							SET @ThanhTienThucChaySanPham = @ThanhTienThucChaySanPham - @ThanhTienThucChayKM;
							SET @SoLuongThucChaySP = @SoLuongThucChaySP - @SoLuongThucChayKM
						END
					END
				END
				
				FETCH NEXT FROM km_cursor INTO @PhanBoId
			END
			CLOSE km_cursor;
			DEALLOCATE km_cursor;
		END
		
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
									AND hdct.DmLoaiREF		<> 13 
									AND hdct.IsKhuyenMai	= 0
								ORDER BY hdct.HopDongChiTietID DESC
							)   
							
			SET @SoLuongLechTreoHa = @SoLuongThucChaySP
			
			PRINT 'Insert ThucChayLechTreoHa';
							
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
	END
END

```
