# Stored Procedure: `ThucChay_CheckHopDongCoPhatSinhGiaTri_CPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-09-14 14:36:23.423000
- **Ngày sửa cuối**: 2016-10-31 14:39:54.140000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DonGia` | `int(4)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@ThanhTien` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_CheckHopDongCoPhatSinhGiaTri_CPR] 26325,370,59116,'2014-06-12',10500,10,2000000000

CREATE  PROCEDURE [dbo].[ThucChay_CheckHopDongCoPhatSinhGiaTri_CPR] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@DmSanPhamREF INT,
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@DonGia INT,
	@ChietKhau FLOAT,
	@ThanhTien INT
	
AS
BEGIN
	-- Declare the return variable here
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500), @CONTENT_DETAIL_LOG NVARCHAR(MAX)
	DECLARE @count_HDCT INT, @ThanhTienThucChay BIGINT, @UVThucChay BIGINT, @UVHopDong INT, @TongViewGoi BIGINT
	DECLARE @MinDate DATETIME
	DECLARE @SoLuongThucChay BIGINT,
	        @TTChenhLechDuocTinh FLOAT
	DECLARE @TTThucChaySauChietKhau  FLOAT,
	        @GiaTriThayDoi           FLOAT,
	        @IsHDFinish				INT,
	        @TongTienThucChay		BIGINT,
	        @DonViTinhREF			INT
	
	SET @CONTENT_DETAIL_LOG = ''
	SET @IsHDFinish = 0
	SET @count_HDCT = 0
	SET @SoLuongThucChay = 0
	SET @TTThucChaySauChietKhau = 0
	SET @GiaTriThayDoi = 0
	SET @TTChenhLechDuocTinh = 0
	SET @UVThucChay = 0
	SET @UVHopDong = 0
	SET @TongViewGoi = 0
	SET @TongTienThucChay = 0
	SET @DonViTinhREF =0
	
	--NOI DUNG LOG
	SET @CONTENT_LOG = @CONTENT_LOG + N'(HĐ Thay đổi nội dung:'
	SET @NGUON_LOG = @NGUON_LOG + 'Table:HopDongChiTietThayDoi:'
	SET @MinDate = (
				SELECT MIN(tcdt.NgayThucHien)
				FROM   ThucChayDaTinh tcdt
				WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
					   AND tcdt.DmSanPhamREF = @DmSanPhamREF
					   AND tcdt.HopDongID = @HopDongREF
			)
	    
	SET @MinDate = ISNULL(@MinDate, GETDATE())
	IF (CONVERT(date, @MinDate) < CONVERT(date, @NgayThucHien))
	BEGIN
		--Xac dinh TongViewThucChay
		--Xac dinh UVThucChay
		SELECT @SoLuongThucChay  = SUM(tcdt.SoLuongThucChay)
				, @UVThucChay = SUM(tcdt.SoLuongDotChayBooking)
		FROM   ThucChayDaTinh tcdt
		WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
			   AND tcdt.DmSanPhamREF = @DmSanPhamREF
			   AND tcdt.HopDongID = @HopDongREF
			   AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
		
		SET @SoLuongThucChay = ISNULL(@SoLuongThucChay, 0)
		SET @UVThucChay = ISNULL(@UVThucChay,0)
		
		SET @DonViTinhREF = IsNULL(
			(
			SELECT hdct.DonViTinhREF FROM HopDongChiTiet hdct
			WHERE hdct.HopDongChiTietID = @HopDongChiTietID
			AND hdct.DeletedStatus = 0
		),0)
		IF(@DonViTinhREF = 10)--Goi
		BEGIN
			--Xac dinh TongViewGoi
			--Xac dinh UVHopDong
			SELECT @TongViewGoi =  dgc.UV*dgc.view_user
			, @UVHopDong = dgc.UV 
			FROM HopDongChiTiet hdct
			INNER JOIN DonGiaCPR dgc ON hdct.DmLoaiBannerREF = dgc.DmLoaiBannerREF
			WHERE hdct.HopDongChiTietID = @HopDongChiTietID
			
			--Tinh ThanhtienThucChaySauChietKhau cua hop dong
			set @ThanhTienThucChay = (@SoLuongThucChay/@TongViewGoi)*(@UVThucChay/@UVHopDong)*(@DonGia*@ChietKhau)/100	
		END
		ELSE
			IF(@DonViTinhREF = 30)
			BEGIN
				SET @ThanhTienThucChay = @UVThucChay*(@DonGia*@ChietKhau)/100
			END
        
		--Xac dinh gia tri ThanhTienThucChaySauChietKhau da thuc hien tinh tren ThucChayDaTinh
		--Xac dinh GiaTriThayDoi da thuc hien tinh tren ThucChayDaTinh
		SELECT @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay),
			   @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi)
		FROM   ThucChayDaTinh tcdt
		WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
			   AND tcdt.DmSanPhamREF = @DmSanPhamREF
			   AND tcdt.HopDongID = @HopDongREF
			   AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien	
        
		SET @TTThucChaySauChietKhau = ISNULL(@TTThucChaySauChietKhau, 0)
		SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi, 0)
        
        SET @TTChenhLechDuocTinh = @ThanhTienThucChay - (@TTThucChaySauChietKhau + @GiaTriThayDoi)
		
		IF (@ThanhTienThucChay > @ThanhTien)
		BEGIN
			SET @isHDFinish = 1
			SET @TTChenhLechDuocTinh  =  @ThanhTien  -(@TTThucChaySauChietKhau + @GiaTriThayDoi)
			SET @IsHDFinish = 1
		END

		IF(@TTThucChaySauChietKhau + @GiaTriThayDoi = 0)
			SET @TongTienThucChay = @TTChenhLechDuocTinh
		ELSE
			SET @TongTienThucChay = @TTThucChaySauChietKhau + @GiaTriThayDoi
		IF(@TongTienThucChay = 0)
			SET @TongTienThucChay = 1
			
		PRINT 'Thanh tien chenh lech :' + CONVERT(NVARCHAR(50), @TTChenhLechDuocTinh)    
		PRINT @HopDongChiTietID	        
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
							  [dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID, @NgayThucHien) NhanHang,
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
							  'CPR_TTR' DotChayHopDong,
							  0 AS SoLuongDotChayHD,
							  'PS THUC TREO CPR' DotChayBooking,
							  0 SoLuongDotChayBooking,
							  C.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS 
							  SoLuong,
							  --dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS 
							  'VIEW' DonViTinh,
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
							  C.DmBannerREF DmBannerREF,	--A.DmBannerREF,
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
								  WHERE  TCDT.HopDongChiTietREF = @HopDongChiTietID
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
					   WHERE  1=1
							  AND D.TrangThaiHopDong != 3
							  AND C.DeletedStatus = 0
							  AND C.DmSanPhamREF = @DmSanPhamREF
				   ) TD
            
				--HD Finish   
				IF(@IsHDFinish = 1)
				BEGIN
					PRINT 'HD finish'
					SELECT @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay),
						   @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi)
					FROM   ThucChayDaTinh tcdt
					WHERE  tcdt.HopDongChiTietREF = @HopDongChiTietID
						   AND tcdt.DmSanPhamREF = @DmSanPhamREF
						   AND tcdt.HopDongID = @HopDongREF
						   AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
					PRINT @ThanhTien - (@TTThucChaySauChietKhau + @GiaTriThayDoi)	
					
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
									  C.NhanHang,
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
									  C.DmBannerREF DmBannerREF,	--A.DmBannerREF,
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
												 (@ThanhTien - (@TTThucChaySauChietKhau + @GiaTriThayDoi)) GiaTriThayDoi
										  FROM   ThucChayDaTinh tcdt
										  WHERE  TCDT.HopDongChiTietREF = @HopDongChiTietID
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
							   WHERE  1=1
									  AND D.TrangThaiHopDong != 3
									  AND C.DeletedStatus = 0
									  AND C.DmSanPhamREF = @DmSanPhamREF
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
							  N'Thay doi noi dung hop dong',
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
								  WHERE  TCDT.HopDongChiTietREF = @HopDongChiTietID
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
					   WHERE  D.TrangThaiHopDong != 3
							  AND C.DeletedStatus = 0
							  AND C.DmSanPhamREF = @DmSanPhamREF
		END
	END

	SELECT 2


END

```
