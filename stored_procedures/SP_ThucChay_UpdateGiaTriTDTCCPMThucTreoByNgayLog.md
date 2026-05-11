# Stored Procedure: `ThucChay_UpdateGiaTriTDTCCPMThucTreoByNgayLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:21.750000
- **Ngày sửa cuối**: 2017-06-07 09:59:59.930000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@CONTENT_LOG` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriTDTCCPMThucTreoByNgayLog] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongREF INT,
	@DmSanPhamID INT,
	@HopDongChiTietREF INT,
	@CONTENT_LOG NVARCHAR(500)
AS
BEGIN
	DECLARE @MinDate DATETIME,
	        @SoLuongLechTreoHa BIGINT,
	        @SoLuongThucChayDuocTinh BIGINT
	
	DECLARE @SoLuongThucChay BIGINT,
	        @SoLuongHopDong BIGINT,
	        @TTChenhLechDuocTinh FLOAT
	
	DECLARE @count_HDCT              INT,
	        @DonGiaTheoDonViTinh     FLOAT,
	        @TTThucChaySauChietKhau  FLOAT,
	        @GiaTriThayDoi           FLOAT,
	        @TongTienThucChay		 FLOAT,
	        @TongTienHopDong		BIGINT,
	        @IsHDFinish				INT
	
	SET @TongTienHopDong = 0
	SET @IsHDFinish = 0
	SET @count_HDCT = 0
	SET @SoLuongLechTreoHa = 0
	SET @SoLuongThucChayDuocTinh = 0
	SET @SoLuongThucChay = 0
	SET @SoLuongHopDong = 0
	SET @DonGiaTheoDonViTinh = 0
	SET @TTThucChaySauChietKhau = 0
	SET @GiaTriThayDoi = 0
	SET @TTChenhLechDuocTinh = 0
	SET @TongTienThucChay = 0
	
	IF (@count_HDCT = 0)--T/c tinh theo phuong phap thuc treo
	BEGIN
	    SET @MinDate = (
	            SELECT MIN(tcdt.NgayThucHien)
	            FROM   ThucChayDaTinh tcdt
	            WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
	                   AND tcdt.DmSanPhamREF = @DmSanPhamID
	                   AND tcdt.HopDongID = @HopDongREF
	        )
	    
	    SET @MinDate = ISNULL(@MinDate, GETDATE())
	    IF (CONVERT(date, @MinDate) < CONVERT(date, @NgayThucHien))
	    BEGIN
	        --Tinh s/l thuc chay 
	        SET @SoLuongThucChay = (
	                SELECT SUM(tcdt.SoLuongThucChay)
	                FROM   ThucChayDaTinh tcdt
	                WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
	                       AND tcdt.DmSanPhamREF = @DmSanPhamID
	                       AND tcdt.HopDongID = @HopDongREF
	                       AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
	            )
	        
	        SET @SoLuongThucChay = ISNULL(@SoLuongThucChay, 0)
	        --Tinh s/l HopDong
	        SET @SoLuongHopDong = (
	                SELECT hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                FROM   HopDongChiTiet hdct
	                WHERE  hdct.HopDongChiTietID = @HopDongChiTietREF
	                       AND hdct.DeletedStatus = 0
	            )
	        --Tinh DonGiaTheoDonViTinh sau chiet khau
	        SET @DonGiaTheoDonViTinh = (
	                SELECT (
	                           hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                       ) * (100 -hdct.ChietKhau) / 100
	                FROM   HopDongChiTiet hdct
	                WHERE  hdct.HopDongChiTietID = @HopDongChiTietREF
	                       AND hdct.DmSanPhamREF = @DmSanPhamID
	                       AND hdct.DeletedStatus = 0
	            )
	        
	        SET @DonGiaTheoDonViTinh = ISNULL(@DonGiaTheoDonViTinh, 0)
	        
	        --Tinh Tong tien t/c sau chiet khau, Gia tri thay doi
	        SELECT @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay),
	               @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi)
	        FROM   ThucChayDaTinh tcdt
	        WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
	               AND tcdt.DmSanPhamREF = @DmSanPhamID
	               AND tcdt.HopDongID = @HopDongREF
	               AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien	
	        
	        SET @TTThucChaySauChietKhau = ISNULL(@TTThucChaySauChietKhau, 0)
	        SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi, 0)
	        
	        --CHECK TINH S./L THUCCHAY DUOC TINH
	        IF (
	               @SoLuongThucChay > 0
	               AND @SoLuongThucChay < @SoLuongHopDong
	           )
	        BEGIN
	            --Tinh s/l LechTreoHa
	            SET @SoLuongLechTreoHa = (
	                    SELECT SUM(tcdt.SoLuongThucChayLechTreoHa)
	                    FROM   ThucChayDaTinh tcdt
	                    WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
	                           AND tcdt.DmSanPhamREF = @DmSanPhamID
	                           AND tcdt.HopDongID = @HopDongREF
	                           AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
	                )
	            
	            SET @SoLuongLechTreoHa = ISNULL(@SoLuongLechTreoHa, 0)
	            IF (
	                   (@SoLuongLechTreoHa > 0)
	                   AND (@SoLuongThucChay + @SoLuongLechTreoHa <= @SoLuongHopDong)
	               )
	            BEGIN
	                SET @SoLuongThucChayDuocTinh = @SoLuongThucChay + @SoLuongLechTreoHa
	            END
	            ELSE 
	            IF (
	                   (@SoLuongLechTreoHa > 0)
	                   AND (@SoLuongThucChay + @SoLuongLechTreoHa > @SoLuongHopDong)
	               )
	            BEGIN
	                SET @SoLuongThucChayDuocTinh = (@SoLuongThucChay + @SoLuongLechTreoHa) 
	                    -((@SoLuongThucChay + @SoLuongLechTreoHa) - @SoLuongHopDong)
	            END
	            ELSE 
	            IF (@SoLuongLechTreoHa <= 0)
	            BEGIN
	                SET @SoLuongThucChayDuocTinh = @SoLuongThucChay
	            END
	            SET @TTChenhLechDuocTinh = (@SoLuongThucChayDuocTinh * @DonGiaTheoDonViTinh)
	            -(@TTThucChaySauChietKhau + @GiaTriThayDoi)
	        END
	        --
	        --   
			IF (@SoLuongThucChay >= @SoLuongHopDong)
			BEGIN
				SET @isHDFinish = 1
				SET @TongTienHopDong =
				(
					SELECT sum(hdct.ThanhTien)
					FROM   HopDongChiTiet hdct
					WHERE  hdct.HopDongFK = @HopDongREF
						   AND hdct.HopDongChiTietID = @HopDongChiTietREF
						   AND hdct.DmSanPhamREF = @DmSanPhamID
						   AND hdct.DeletedStatus = 0
						   AND hdct.ChietKhau <> 100
				)           
				SET @TTChenhLechDuocTinh  =  @TongTienHopDong  -(@TTThucChaySauChietKhau + @GiaTriThayDoi)
				SET @IsHDFinish = 1
			END

	        IF(@TTThucChaySauChietKhau + @GiaTriThayDoi = 0)
				SET @TongTienThucChay = @TTChenhLechDuocTinh
			ELSE
				SET @TongTienThucChay = @TTThucChaySauChietKhau + @GiaTriThayDoi
	        IF(@TongTienThucChay = 0)
				SET @TongTienThucChay = 1
				
	        PRINT 'Thanh tien chenh lech :' + CONVERT(NVARCHAR(50), @TTChenhLechDuocTinh)    
			PRINT @HopDongChiTietREF	        
	        IF (@TTChenhLechDuocTinh != 0)
	        BEGIN
	            INSERT INTO ThucChayDaTinh
	            SELECT NEWID(),
	                   TD.*,
	                   0 AS GiaTriTrietKhauThucChay,
	                   0 AS ThanhTienSauTrietKhauThucChay,
	                   0 AS GiaTriHoaHongThucChay,
	                   0 AS ThanhTienThucThu,
	                   0 AS ThanhTienKM,
	                   0 AS SoLuongThucChayKM,
	                   0 AS SoLuongLechTreoHa,
	                   0 AS ThanhTienLechTreoHa,
	                   GETDATE(),
	                   GETDATE(),
	                   0 IsPheDuyet,
	                   '' PheDuyetBy,
	                   '' PheDuyetAt,
						0 SoLuongThayDoi,
						0 SoLuongKMThayDoi,
						0 GiaTriKMThayDoi,
						'' GhiChu	
	            FROM   (
	                       SELECT --ID Hop Dong
	                              D.HopDongID,
	                              --Thong tin ve ma so 
	                              D.SoHopDong,
	                              D.DmMaHopDongREF,
	                              D.TenMaHopDong,
	                              --Thong tin ve thoi gian
	                              D.NgayDanhSoHopDong,
	                              D.NgayKyHopDong,
	                              D.NhanHopDong,
	                              D.NgayNhanBanFax,
	                              D.NgayNhanHopDongBanCung,
	                              D.NgayChuyenHopDongChoKeToan,
	                              D.So,
	                              D.Thang,
	                              D.Nam,
	                              --Thong tin ve gia tri
	                              D.GiaTriHopDong,
	                              D.CongNo,
	                              --Thong tin chi tiet phan bo
	                              A.HopDongChiTietREF,
	                              --Thong tin ve trang thai
	                              D.DangSuDung,
	                              D.IsGiayPhep,
	                              D.TrangThaiHopDong,
	                              D.IsBanCung,
	                              --Thong tin ve Nhan vien kinh doanh
	                              D.DmPhongBanREF,
	                              ISNULL(D.TenPhongBan, '') AS TenPhongBan,
	                              D.DmBoPhanREF,
	                              ISNULL(D.TenBoPhan, '') AS TenBoPhan,
	                              D.DmNhomLamViecREF,
	                              ISNULL(D.TenNhom, '') AS TenNhom,
	                              D.DmDiaDiemLamViecREF,
	                              D.TenDiaDiemLamViec,
	                              D.SysNhanVienREF,
	                              ISNULL(D.TenDangNhap, '') AS TenDangNhap,
	                              D.TenNhanVien,
	                              --Thong tin ve khach hang
	                              --D.DmKhachHangREF, 
	                              D.TenKhachHang,
	                              A.NhanHang,
	                              C.DmNhomNganhREF,
	                              C.TenNhomNganh,
	                              --Thong tin hinh thuc quang cao
	                              C.DmLoaiREF AS DmHinhThucQuangCao,
	                              C.TenLoai AS TenHinhThucQuangCao,
	                              --Thong tin San pham
	                              C.DmSanPhamREF AS DmSanPhamREF,
	                              C.TenSanPham AS TenSanPham,
	                              C.DmNhomWebsiteREF,
	                              C.TenNhomWebsite,
	                              --C.DmWebsiteREF,
	                              --C.TenWebsite, 
	                              C.DmChuyenMucREF,
	                              C.TenChuyenMuc,
	                              C.DmLoaiBannerREF,
	                              C.TenLoaiBanner,
	                              C.DmViTriREF,
	                              C.TenViTri,
	                              'CPM_TTR' DotChayHopDong,
	                              C.SoLuong AS SoLuongDotChayHD,
	                              'PS THUC TREO CPM' DotChayBooking,
	                              0 SoLuongDotChayBooking,
	                              C.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS 
	                              SoLuong,
	                              dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS 
	                              DonViTinh,
	                              dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien, A.HopDongChiTietREF, C.DonGia) AS 
	                              DonGia,
	                              ISNULL(
	                                  dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(
	                                      C.SoLuong,
	                                      C.DonViTinh,
	                                      C.DonGia,
	                                      D.NgayKyHopDong,
	                                      @NgayThucHien,
	                                      A.HopDongChiTietREF
	                                  ),
	                                  0
	                              ) AS DonGiaTheoDonViTinh,
	                              C.ChietKhau,
	                              C.GiamGia,
	                              C.ThanhTien,
	                              C.TiLeTuVan,
	                              C.ChiPhiTuVan,
	                              C.IsKhuyenMai,
	                              C.KhuyenMai,
	                              0 DmBannerREF,	--A.DmBannerREF,
	                              0 DmChienDichREF,	--A.DmChienDichREF,
	                              A.DmWebsiteREF,
	                              A.TenWebsite,
	                              0 TongViewThucChay,
	                              0 TongClickThucChay,
	                              0 TongSoBaiViet,
	                              0 AS SoLuongThucChay,
	                              @NgayThucHien NgayThucHien,
	                              A.GiaTriThayDoi AS GiaTriThayDoi,
	                              0 AS ThanhTienThucChayTruocTrietKhau
	                       FROM   (
	                                  SELECT tcdt.HopDongChiTietREF,
	                                         tcdt.DmWebsiteREF,
	                                         tcdt.TenWebsite,
	                                         tcdt.NhanHang,
	                                         ROUND(
	                                             (
	                                                 (
	                                                     SUM(tcdt.ThanhTienSauTrietKhauThucChay) 
	                                                     + SUM(tcdt.GiaTriThayDoi)
	                                                 ) / @TongTienThucChay
	                                             ) * @TTChenhLechDuocTinh,
	                                             0
	                                         ) GiaTriThayDoi
	                                  FROM   ThucChayDaTinh tcdt
	                                  WHERE  TCDT.HopDongChiTietREF = @HopDongChiTietREF
	                                         AND (
	                                                 tcdt.GiaTriThayDoi != 0
	                                                 OR tcdt.ThanhTienSauTrietKhauThucChay 
	                                                    != 0
	                                             )
	                                  GROUP BY
	                                         tcdt.HopDongChiTietREF,
	                                         tcdt.DmWebsiteREF,
	                                         tcdt.TenWebsite,
	                                         tcdt.NhanHang
	                              )A
	                              INNER JOIN HopDongChiTiet C
	                                   ON  C.HopDongChiTietID = A.HopDongChiTietREF
	                              INNER JOIN HopDong D
	                                   ON  D.HopDongID = C.HopDongFK
	                              INNER JOIN DmWebsite E
	                                   ON  E.DmWebsiteID = C.DmWebsiteREF
	                       WHERE  (
	                                  (UPPER(C.DonViTinh) = 'CPM')
	                                  OR (UPPER(C.DonViTinh) = 'CPC')
									  OR (UPPER(C.DonViTinh) = 'TRUE REACH')
	                              )
	                              AND D.TrangThaiHopDong != 3
	                              AND C.DeletedStatus = 0
	                              AND C.DmSanPhamREF IN (231, 238, 339, 240, 370,598,613,732,735)
	                   ) TD
	            
					--HD Finish   
					IF(@IsHDFinish = 1)
					BEGIN
						PRINT 'HD finish'
						SELECT @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay),
							   @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi)
						FROM   ThucChayDaTinh tcdt
						WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietREF
							   AND tcdt.DmSanPhamREF = @DmSanPhamID
							   AND tcdt.HopDongID = @HopDongREF
							   AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
						PRINT @TongTienHopDong- (@TTThucChaySauChietKhau + @GiaTriThayDoi)	
						
						INSERT INTO ThucChayDaTinh
							SELECT NEWID(),
							   TD.*,
							   0 AS GiaTriTrietKhauThucChay,
							   0 AS ThanhTienSauTrietKhauThucChay,
							   0 AS GiaTriHoaHongThucChay,
							   0 AS ThanhTienThucThu,
							   0 AS ThanhTienKM,
							   0 AS SoLuongThucChayKM,
							   0 AS SoLuongLechTreoHa,
							   0 AS ThanhTienLechTreoHa,
							   GETDATE(),
							   GETDATE(),
							   0 IsPheDuyet,
							   '' PheDuyetBy,
							   '' PheDuyetAt,
								0 SoLuongThayDoi,
								0 SoLuongKMThayDoi,
								0 GiaTriKMThayDoi,
								'' GhiChu	
						FROM   (
								   SELECT --ID Hop Dong
										  D.HopDongID,
										  --Thong tin ve ma so 
										  D.SoHopDong,
										  D.DmMaHopDongREF,
										  D.TenMaHopDong,
										  --Thong tin ve thoi gian
										  D.NgayDanhSoHopDong,
										  D.NgayKyHopDong,
										  D.NhanHopDong,
										  D.NgayNhanBanFax,
										  D.NgayNhanHopDongBanCung,
										  D.NgayChuyenHopDongChoKeToan,
										  D.So,
										  D.Thang,
										  D.Nam,
										  --Thong tin ve gia tri
										  D.GiaTriHopDong,
										  D.CongNo,
										  --Thong tin chi tiet phan bo
										  A.HopDongChiTietREF,
										  --Thong tin ve trang thai
										  D.DangSuDung,
										  D.IsGiayPhep,
										  D.TrangThaiHopDong,
										  D.IsBanCung,
										  --Thong tin ve Nhan vien kinh doanh
										  D.DmPhongBanREF,
										  ISNULL(D.TenPhongBan, '') AS TenPhongBan,
										  D.DmBoPhanREF,
										  ISNULL(D.TenBoPhan, '') AS TenBoPhan,
										  D.DmNhomLamViecREF,
										  ISNULL(D.TenNhom, '') AS TenNhom,
										  D.DmDiaDiemLamViecREF,
										  D.TenDiaDiemLamViec,
										  D.SysNhanVienREF,
										  ISNULL(D.TenDangNhap, '') AS TenDangNhap,
										  D.TenNhanVien,
										  --Thong tin ve khach hang
										  --D.DmKhachHangREF, 
										  D.TenKhachHang,
										  A.NhanHang,
										  C.DmNhomNganhREF,
										  C.TenNhomNganh,
										  --Thong tin hinh thuc quang cao
										  C.DmLoaiREF AS DmHinhThucQuangCao,
										  C.TenLoai AS TenHinhThucQuangCao,
										  --Thong tin San pham
										  C.DmSanPhamREF AS DmSanPhamREF,
										  C.TenSanPham AS TenSanPham,
										  C.DmNhomWebsiteREF,
										  C.TenNhomWebsite,
										  --C.DmWebsiteREF,
										  --C.TenWebsite, 
										  C.DmChuyenMucREF,
										  C.TenChuyenMuc,
										  C.DmLoaiBannerREF,
										  C.TenLoaiBanner,
										  C.DmViTriREF,
										  C.TenViTri,
										  'CPM_TTR' DotChayHopDong,
										  C.SoLuong AS SoLuongDotChayHD,
										  'PS THUC TREO CPM' DotChayBooking,
										  0 SoLuongDotChayBooking,
										  C.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS 
										  SoLuong,
										  dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS 
										  DonViTinh,
										  dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien, A.HopDongChiTietREF, C.DonGia) AS 
										  DonGia,
										  ISNULL(
											  dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(
												  C.SoLuong,
												  C.DonViTinh,
												  C.DonGia,
												  D.NgayKyHopDong,
												  @NgayThucHien,
												  A.HopDongChiTietREF
											  ),
											  0
										  ) AS DonGiaTheoDonViTinh,
										  C.ChietKhau,
										  C.GiamGia,
										  C.ThanhTien,
										  C.TiLeTuVan,
										  C.ChiPhiTuVan,
										  C.IsKhuyenMai,
										  C.KhuyenMai,
										  0 DmBannerREF,	--A.DmBannerREF,
										  0 DmChienDichREF,	--A.DmChienDichREF,
										  A.DmWebsiteREF,
										  A.TenWebsite,
										  0 TongViewThucChay,
										  0 TongClickThucChay,
										  0 TongSoBaiViet,
										  0 AS SoLuongThucChay,
										  @NgayThucHien NgayThucHien,
										  A.GiaTriThayDoi AS GiaTriThayDoi,
										  0 AS ThanhTienThucChayTruocTrietKhau
								   FROM   (
											  SELECT  top 1 tcdt.HopDongChiTietREF,
													 tcdt.DmWebsiteREF,
													 tcdt.TenWebsite,
													 tcdt.NhanHang,
													 (@TongTienHopDong- (@TTThucChaySauChietKhau + @GiaTriThayDoi)) GiaTriThayDoi
											  FROM   ThucChayDaTinh tcdt
											  WHERE  TCDT.HopDongChiTietREF = @HopDongChiTietREF
													 AND (
															 tcdt.GiaTriThayDoi != 0
															 OR tcdt.ThanhTienSauTrietKhauThucChay 
																!= 0
														 )
											  GROUP BY
													 tcdt.HopDongChiTietREF,
													 tcdt.DmWebsiteREF,
													 tcdt.TenWebsite,
													 tcdt.NhanHang
										  )A
										  INNER JOIN HopDongChiTiet C
											   ON  C.HopDongChiTietID = A.HopDongChiTietREF
										  INNER JOIN HopDong D
											   ON  D.HopDongID = C.HopDongFK
										  INNER JOIN DmWebsite E
											   ON  E.DmWebsiteID = C.DmWebsiteREF
								   WHERE  (
											  (UPPER(C.DonViTinh) = 'CPM')
											  OR (UPPER(C.DonViTinh) = 'CPC')
											  OR (UPPER(C.DonViTinh) = 'TRUE REACH')
										  )
										  AND D.TrangThaiHopDong != 3
										  AND C.DeletedStatus = 0
										  AND C.DmSanPhamREF IN (231, 238, 339, 342, 337, 240, 370,598,613,732,735)
							   ) TD
					END
	            
					--Insert log
	               INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
					  SELECT  NEWID(), D.HopDongID,
	                              --Thong tin ve ma so 
	                              D.SoHopDong,
	                              A.HopDongChiTietREF,
	                              C.DmSanPhamREF AS DmSanPhamREF,
							      A.DmWebsiteREF,
								  @NgayThucHien NgayThucHien,
								  isnull(A.GiaTriThayDoi,0) AS GiaTriThayDoi,
	                              
	                              0 AS GiaSauCK1,
	                              0 Soluong1,
	                              0 AS GiaSauCK2,
	                              0 Soluong2,
	                              @CONTENT_LOG,
	                              N'Thay đổi hợp đồng',
	                              'CPM',	'ThucChay',	GETDATE(),
								  'ThucChay',GETDATE(),0,
	                              0,0
					  FROM   (
	                                  SELECT tcdt.HopDongChiTietREF,
	                                         tcdt.DmWebsiteREF,
	                                         tcdt.TenWebsite,
	                                         ROUND(
	                                             (
	                                                 (
	                                                     SUM(tcdt.ThanhTienSauTrietKhauThucChay) 
	                                                     + SUM(tcdt.GiaTriThayDoi)
	                                                 ) / @TongTienThucChay
	                                             ) * @TTChenhLechDuocTinh,
	                                             0
	                                         ) GiaTriThayDoi
	                                  FROM   ThucChayDaTinh tcdt
	                                  WHERE  TCDT.HopDongChiTietREF = @HopDongChiTietREF
	                                         AND (
	                                                 tcdt.GiaTriThayDoi != 0
	                                                 OR tcdt.ThanhTienSauTrietKhauThucChay 
	                                                    != 0
	                                             )
	                                  GROUP BY
	                                         tcdt.HopDongChiTietREF,
	                                         tcdt.DmWebsiteREF,
	                                         tcdt.TenWebsite
	                              )A
	                              INNER JOIN HopDongChiTiet C
	                                   ON  C.HopDongChiTietID = A.HopDongChiTietREF
	                              INNER JOIN HopDong D
	                                   ON  D.HopDongID = C.HopDongFK
	                              INNER JOIN DmWebsite E
	                                   ON  E.DmWebsiteID = C.DmWebsiteREF
	                       WHERE  D.TrangThaiHopDong != 3
	                              AND C.DeletedStatus = 0
	                              AND C.DmSanPhamREF IN (231, 238, 339, 240, 370,598,613,732,735)
	                              AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](C.DonViTinhREF, C.DonViTinh) = 3      
	        END
	    END
	END
	
	SELECT 2
END

--EXEC [ThucChay_UpdateGiaTriTDTCCPMThucTreoByNgay] '2013-09-20', 'QC124555', 123454, 339

```
