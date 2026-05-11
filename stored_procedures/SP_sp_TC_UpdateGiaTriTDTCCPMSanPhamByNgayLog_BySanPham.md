# Stored Procedure: `sp_TC_UpdateGiaTriTDTCCPMSanPhamByNgayLog_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-18 16:18:37.303000
- **Ngày sửa cuối**: 2017-09-18 16:18:37.303000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@CONTENT_LOG` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriTDTCCPMSanPhamByNgay] '2013-09-20', 'QC124555', 123454, 339

CREATE PROCEDURE [dbo].[sp_TC_UpdateGiaTriTDTCCPMSanPhamByNgayLog_BySanPham] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongREF INT,
	@DmSanPhamID INT,
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
	        @TongTienThucChay		FLOAT,
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
	
	--T/c tinh theo phuong phap san pham
	SET @MinDate = (
	        SELECT MIN(tcdt.NgayThucHien)
	        FROM   ThucChayDaTinh tcdt
	        WHERE  tcdt.DmSanPhamREF = @DmSanPhamID
	               AND tcdt.HopDongID = @HopDongREF
	               AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3
	    )
	
	SET @MinDate = ISNULL(@MinDate, GETDATE())
	IF (CONVERT(date, @MinDate) < CONVERT(date, @NgayThucHien))
	BEGIN
	    --Tinh s/l thuc chay 
	    SET @SoLuongThucChay = (
	            SELECT SUM(tcdt.SoLuongThucChay)
	            FROM   ThucChayDaTinh tcdt
	            WHERE  tcdt.DmSanPhamREF = @DmSanPhamID
	                   AND tcdt.HopDongID = @HopDongREF
	                   AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
	                   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3
	        )
	    
	    SET @SoLuongThucChay = ISNULL(@SoLuongThucChay, 0)
	    --Tinh s/l HopDong
	    SET @SoLuongHopDong = (
	            SELECT SUM(
	                       hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                   )
	            FROM   HopDongChiTiet hdct
	            WHERE  hdct.HopDongFK = @HopDongREF
	                   AND hdct.DmSanPhamREF = @DmSanPhamID
	                   AND hdct.DeletedStatus = 0
	                   AND hdct.ChietKhau <> 100
	                   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh)  = 3
	        )
	    --Tinh DonGiaTheoDonViTinh sau chi?t kh?u
	    SET @DonGiaTheoDonViTinh = (
	            SELECT MAX(
	                       (
	                           hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                       ) * (100 -hdct.ChietKhau) / 100
	                   )
	            FROM   HopDongChiTiet hdct
	            WHERE  hdct.HopDongFK = @HopDongREF
	                   AND hdct.DmSanPhamREF = @DmSanPhamID
	                   AND hdct.DeletedStatus = 0
	                   AND hdct.ChietKhau <> 100
	                   AND hdct.DonGia <> 0
	                   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh)  = 3
	        )
	    
	    SET @DonGiaTheoDonViTinh = ISNULL(@DonGiaTheoDonViTinh, 0)
	    
	    --Tinh Tong tien t/c sau chiet khau, Gia tri thay doi
	    SELECT @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay),
	           @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi)
	    FROM   ThucChayDaTinh tcdt
	    WHERE  tcdt.DmSanPhamREF = @DmSanPhamID
	           AND tcdt.HopDongID = @HopDongREF
	           AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien	
	           AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3
	    
	    SET @TTThucChaySauChietKhau = ISNULL(@TTThucChaySauChietKhau, 0)
	    SET @GiaTriThayDoi = ISNULL(@GiaTriThayDoi, 0)
	   
	    --CHECK TINH S./L THUCCHAY DUOC TINH
	    --
	    IF (
	           @SoLuongThucChay > 0
	           AND @SoLuongThucChay < @SoLuongHopDong
	       )
	    BEGIN
	        --Tinh s/l LechTreoHa
	        SET @SoLuongLechTreoHa = (
	                SELECT SUM(tcdt.SoLuongThucChayLechTreoHa)
	                FROM   ThucChayDaTinh tcdt
	                WHERE  tcdt.DmSanPhamREF = @DmSanPhamID
	                       AND tcdt.HopDongID = @HopDongREF
	                       AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
	                       AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3
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
	    IF (@SoLuongThucChay >= @SoLuongHopDong)
	    BEGIN
			SET @TongTienHopDong =
			(
				SELECT sum(hdct.ThanhTien)
	            FROM   HopDongChiTiet hdct
	            WHERE  hdct.HopDongFK = @HopDongREF
	                   AND hdct.DmSanPhamREF = @DmSanPhamID
	                   AND hdct.DeletedStatus = 0
	                   AND hdct.ChietKhau <> 100
	                   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh)  = 3
	        )           
	        SET @TTChenhLechDuocTinh  =  @TongTienHopDong  -(@TTThucChaySauChietKhau + @GiaTriThayDoi)
	        SET @IsHDFinish = 1
	    END
	    IF(@TTThucChaySauChietKhau + @GiaTriThayDoi = 0)
			SET @TongTienThucChay = (@SoLuongThucChayDuocTinh * @DonGiaTheoDonViTinh)
		ELSE
			SET @TongTienThucChay = (@TTThucChaySauChietKhau + @GiaTriThayDoi)
		IF(@TongTienThucChay = 0)
			SET @TongTienThucChay = 1	
			
	    PRINT 'Thanh tien chenh lech:'  + convert(nvarchar(50),@TTChenhLechDuocTinh)
	    PRINT @GiaTriThayDoi
	    IF (@TTChenhLechDuocTinh != 0)
	    BEGIN
	        INSERT INTO ThucChayDaTinh
	        SELECT NEWID(),
	               TD.*,
	               0 AS ThanhTienThucChayTruocTrietKhau,
	               0 AS GiaTriTrietKhauThucChay,
	               0 AS ThanhTienThucChaySauTrietKhau,
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
	                          ISNULL(b.HopDongID, 0) HopDongID,
	                          --Thong tin ve ma so 
	                          b.SoHopDong,
	                          b.DmMaHopDongREF,
	                          b.TenMaHopDong,
	                          --Thong tin ve thoi gian
	                          b.NgayDanhSoHopDong,
	                          b.NgayKyHopDong,
	                          b.NhanHopDong,
	                          b.NgayNhanBanFax,
	                          b.NgayNhanHopDongBanCung,
	                          b.NgayChuyenHopDongChoKeToan,
	                          b.So,
	                          b.Thang,
	                          b.Nam,
	                          --Thong tin ve gia tri
	                          b.GiaTriHopDong,
	                          b.CongNo,
	                          --Thong tin chi tiet phan bo
	                          0 HopDongChiTietREF,
	                          --Thong tin ve trang thai
	                          b.DangSuDung,
	                          b.IsGiayPhep,
	                          b.TrangThaiHopDong,
	                          b.IsBanCung,
	                          --Thong tin ve Nhan vien kinh doanh
	                          b.DmPhongBanREF,
	                          ISNULL(b.TenPhongBan, '') AS TenPhongBan,
	                          b.DmBoPhanREF,
	                          ISNULL(b.TenBoPhan, '') AS TenBoPhan,
	                          b.DmNhomLamViecREF,
	                          ISNULL(b.TenNhom, '') AS TenNhom,
	                          b.DmDiaDiemLamViecREF,
	                          b.TenDiaDiemLamViec,
	                          b.SysNhanVienREF,
	                          ISNULL(b.TenDangNhap, '') AS TenDangNhap,
	                          b.TenNhanVien,
	                          --Thong tin ve khach hang
	                          --D.DmKhachHangREF, 
	                          b.TenKhachHang,
	                          --'' NhanHang,
	                          A.NhanHang,
	                          0 DmNhomNganhREF,
	                          '' TenNhomNganh,
	                          --Thong tin hinh thuc quang cao
	                          b.DmHinhThucSanPhamREF AS DmHinhThucQuangCao,
	                          b.TenHinhThucSanPham AS TenHinhThucQuangCao,
	                          --Thong tin San pham
	                          b.DmSanPhamREF AS DmSanPhamREF,
	                          b.TenSanPham AS TenSanPham,
	                          0 DmNhomWebsiteREF,
	                          '' TenNhomWebsite,
	                          0 DmChuyenMucREF,
	                          '' TenChuyenMuc,
	                          0 DmLoaiBannerREF,
	                          '' TenLoaiBanner,
	                          0 DmViTriREF,
	                          '' TenViTri,
	                          'CPM_TTR' DotChayHopDong,
	                          b.soluongdotchayHD AS SoLuongDotChayHD,
	                          'PS THUC TREO CPM' DotChayBooking,
	                          0 AS SoLuongDotChayBooking,
	                          --Thong tin ve Tien
	                          b.soluong,
	                          b.DonViTinh,
	                          b.DonGia AS DonGia,
	                          b.DonGiaSauCK AS DonGiaTheoDonViTinh,
	                          0 ChietKhau,
	                          0 GiamGia,
	                          ISNULL(b.ThanhTien, 0) ThanhTien,
	                          0 TiLeTuVan,
	                          0 ChiPhiTuVan,
	                          0 IsKhuyenMai,
	                          '' KhuyenMai,
	                          --Thuc chay
	                          A.DmBannerREF DmBannerREF,	--A.DmBannerREF,
	                          0 DmChienDichREF,	--A.DmChienDichREF,
	                          A.DmWebsiteREF DmWebsiteREF,
	                          A.TenWebsite TenWebsite,
	                          0 TongViewThucChay,
	                          0 TongClickThucChay,
	                          0 TongSoBaiViet,
	                          0 AS SoLuongThucChay,
	                          --Thanhuc Tien Thuc Chay
	                          @NgayThucHien AS NgayThucHien,
	                          A.GiaTriThayDoi AS GiaTriThayDoi
	                   FROM   (
	                              SELECT tcdt.SoHopDong,
	                                     tcdt.DmSanPhamREF,
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
	                                     , tcdt.DmBannerREF
	                              FROM   ThucChayDaTinh tcdt
	                              WHERE  TCDT.HopDongID = @HopDongREF
										 AND tcdt.DmSanPhamREF = @DmSanPhamID
	                                     AND (
	                                             tcdt.GiaTriThayDoi != 0
	                                             OR tcdt.ThanhTienSauTrietKhauThucChay 
	                                                != 0
	                                     )
	                                     AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3
	                              GROUP BY
	                                     tcdt.SoHopDong,
	                                     tcdt.DmSanPhamREF,
	                                     tcdt.DmWebsiteREF,
	                                     tcdt.TenWebsite,
	                                     tcdt.NhanHang,
										 tcdt.DmBannerREF
	                          )A
	                          LEFT JOIN (
	                                   SELECT hd.SoHopDong,
	                                          hd.HopDongID,
	                                          --Thong tin ve ma so 
	                                          hd.DmMaHopDongREF,
	                                          hd.TenMaHopDong,
	                                          --Thong tin ve thoi gian
	                                          hd.NgayDanhSoHopDong,
	                                          hd.NgayKyHopDong,
	                                          hd.NhanHopDong,
	                                          hd.NgayNhanBanFax,
	                                          hd.NgayNhanHopDongBanCung,
	                                          hd.NgayChuyenHopDongChoKeToan,
	                                          hd.So,
	                                          hd.Thang,
	                                          hd.Nam,
	                                          --Thong tin ve gia tri
	                                          hd.GiaTriHopDong,
	                                          hd.CongNo,
	                                          --Thong tin chi tiet phan bo
	                                          --Thong tin ve trang thai
	                                          hd.DangSuDung,
	                                          hd.IsGiayPhep,
	                                          hd.TrangThaiHopDong,
	                                          hd.IsBanCung,
	                                          --Thong tin ve Nhan vien kinh doanh
	                                          hd.DmPhongBanREF,
	                                          ISNULL(hd.TenPhongBan, '') AS 
	                                          TenPhongBan,
	                                          hd.DmBoPhanREF,
	                                          ISNULL(hd.TenBoPhan, '') AS 
	                                          TenBoPhan,
	                                          hd.DmNhomLamViecREF,
	                                          ISNULL(hd.TenNhom, '') AS TenNhom,
	                                          hd.DmDiaDiemLamViecREF,
	                                          hd.TenDiaDiemLamViec,
	                                          hd.SysNhanVienREF,
	                                          ISNULL(hd.TenDangNhap, '') AS 
	                                          TenDangNhap,
	                                          hd.TenNhanVien,
	                                          hd.TenKhachHang,
	                                          HDCT.DmSanPhamREF,
	                                          HDCT.TenSanPham,
	                                          MAX(hdct.DmLoaiREF) AS DmHinhThucSanPhamREF,
	                                          MAX(hdct.TenLoai) AS TenHinhThucSanPham,
	                                          SUM(hdct.SoLuong) soluongdotchayHD,
	                                          SUM(
	                                              hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                                          ) soluong,
	                                          SUM(hdct.ThanhTien) ThanhTien,
	                                          MAX(dbo.ThucChay_GetDonViTinhNotCPD(hdct.DonViTinh)) AS 
	                                          DonViTinh,
	                                          MAX(
	                                              hdct.ThanhTien / (
	                                                  hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                                              )
	                                          ) DonGiaSauCK,
	                                          MAX(
	                                              hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                                          ) DonGia
	                                   FROM   HopDong hd
	                                          INNER JOIN HopDongChiTiet hdct
	                                               ON  HD.HopDongID = HDCT.HopDongFK
	                                               AND HDCT.DmSanPhamREF = @DmSanPhamID
	                                               AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3
	                                               AND hdct.DeletedStatus = 0
	                                               AND hdct.SoLuong > 0
	                                   GROUP BY
	                                          HDCT.DmSanPhamREF,
	                                          HDCT.TenSanPham,
	                                          HD.SoHopDong,
	                                          hd.HopDongID,
	                                          --Thong tin ve ma so 
	                                          hd.DmMaHopDongREF,
	                                          hd.TenMaHopDong,
	                                          --Thong tin ve thoi gian
	                                          hd.NgayDanhSoHopDong,
	                                          hd.NgayKyHopDong,
	                                          hd.NhanHopDong,
	                                          hd.NgayNhanBanFax,
	                                          hd.NgayNhanHopDongBanCung,
	                                          hd.NgayChuyenHopDongChoKeToan,
	                                          hd.So,
	                                          hd.Thang,
	                                          hd.Nam,
	                                          --Thong tin ve gia tri
	                                          hd.GiaTriHopDong,
	                                          hd.CongNo,
	                                          --Thong tin chi tiet phan bo
	                                          --Thong tin ve trang thai
	                                          hd.DangSuDung,
	                                          hd.IsGiayPhep,
	                                          hd.TrangThaiHopDong,
	                                          hd.IsBanCung,
	                                          --Thong tin ve Nhan vien kinh doanh
	                                          hd.DmPhongBanREF,
	                                          hd.TenPhongBan,
	                                          hd.DmBoPhanREF,
	                                          hd.TenBoPhan,
	                                          hd.DmNhomLamViecREF,
	                                          hd.TenNhom,
	                                          hd.DmDiaDiemLamViecREF,
	                                          hd.TenDiaDiemLamViec,
	                                          hd.SysNhanVienREF,
	                                          hd.TenDangNhap,
	                                          hd.TenNhanVien,
	                                          hd.TenKhachHang
	                               )B
	                               ON  UPPER(LTRIM(RTRIM(A.SoHopDong))) = B.SoHopDong
	                               AND A.DmSanPhamREF = B.DmSanPhamREF 
	                                   --AND B.DonGiaSauCK > 0
	                                   --ORDER BY A.TenSanPham ,a.SoHopDong,a.TenWebsite
	               ) TD
	        WHERE  TD.SoHopDong IS NOT NULL
	        IF(@IsHDFinish = 1)
	        BEGIN
	        	PRINT 'HD finish'
	        	 --Tinh Tong tien t/c sau chiet khau, Gia tri thay doi
				SELECT @TTThucChaySauChietKhau = SUM(tcdt.ThanhTienSauTrietKhauThucChay),
					   @GiaTriThayDoi = SUM(tcdt.GiaTriThayDoi)
				FROM   ThucChayDaTinh tcdt
				WHERE  tcdt.DmSanPhamREF = @DmSanPhamID
					   AND tcdt.HopDongID = @HopDongREF
					   AND tcdt.NgayThucHien BETWEEN @MinDate AND @NgayThucHien
					   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3
					    
				PRINT @TongTienHopDong- (@TTThucChaySauChietKhau + @GiaTriThayDoi)	   
				IF((@TTThucChaySauChietKhau + @GiaTriThayDoi) <> @TongTienHopDong)
					INSERT INTO ThucChayDaTinh
					SELECT NEWID(),
						   TD.*,
						   0 AS ThanhTienThucChayTruocTrietKhau,
						   0 AS GiaTriTrietKhauThucChay,
						   0 AS ThanhTienThucChaySauTrietKhau,
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
									  ISNULL(b.HopDongID, 0) HopDongID,
									  --Thong tin ve ma so 
									  b.SoHopDong,
									  b.DmMaHopDongREF,
									  b.TenMaHopDong,
									  --Thong tin ve thoi gian
									  b.NgayDanhSoHopDong,
									  b.NgayKyHopDong,
									  b.NhanHopDong,
									  b.NgayNhanBanFax,
									  b.NgayNhanHopDongBanCung,
									  b.NgayChuyenHopDongChoKeToan,
									  b.So,
									  b.Thang,
									  b.Nam,
									  --Thong tin ve gia tri
									  b.GiaTriHopDong,
									  b.CongNo,
									  --Thong tin chi tiet phan bo
									  0 HopDongChiTietREF,
									  --Thong tin ve trang thai
									  b.DangSuDung,
									  b.IsGiayPhep,
									  b.TrangThaiHopDong,
									  b.IsBanCung,
									  --Thong tin ve Nhan vien kinh doanh
									  b.DmPhongBanREF,
									  ISNULL(b.TenPhongBan, '') AS TenPhongBan,
									  b.DmBoPhanREF,
									  ISNULL(b.TenBoPhan, '') AS TenBoPhan,
									  b.DmNhomLamViecREF,
									  ISNULL(b.TenNhom, '') AS TenNhom,
									  b.DmDiaDiemLamViecREF,
									  b.TenDiaDiemLamViec,
									  b.SysNhanVienREF,
									  ISNULL(b.TenDangNhap, '') AS TenDangNhap,
									  b.TenNhanVien,
									  --Thong tin ve khach hang
									  --D.DmKhachHangREF, 
									  b.TenKhachHang,
									  --'' NhanHang,
									  A.NhanHang,
									  0 DmNhomNganhREF,
									  '' TenNhomNganh,
									  --Thong tin hinh thuc quang cao
									  b.DmHinhThucSanPhamREF AS DmHinhThucQuangCao,
									  b.TenHinhThucSanPham AS TenHinhThucQuangCao,
									  --Thong tin San pham
									  b.DmSanPhamREF AS DmSanPhamREF,
									  b.TenSanPham AS TenSanPham,
									  0 DmNhomWebsiteREF,
									  '' TenNhomWebsite,
									  0 DmChuyenMucREF,
									  '' TenChuyenMuc,
									  0 DmLoaiBannerREF,
									  '' TenLoaiBanner,
									  0 DmViTriREF,
									  '' TenViTri,
									  'CPM_TTR' DotChayHopDong,
									  b.soluongdotchayHD AS SoLuongDotChayHD,
									  'PS THUC TREO CPM' DotChayBooking,
									  0 AS SoLuongDotChayBooking,
									  --Thong tin ve Tien
									  b.soluong,
									  b.DonViTinh,
									  b.DonGia AS DonGia,
									  b.DonGiaSauCK AS DonGiaTheoDonViTinh,
									  0 ChietKhau,
									  0 GiamGia,
									  ISNULL(b.ThanhTien, 0) ThanhTien,
									  0 TiLeTuVan,
									  0 ChiPhiTuVan,
									  0 IsKhuyenMai,
									  '' KhuyenMai,
									  --Thuc chay
									  A.DmBannerREF DmBannerREF,	--A.DmBannerREF,
									  0 DmChienDichREF,	--A.DmChienDichREF,
									  A.DmWebsiteREF DmWebsiteREF,
									  A.TenWebsite TenWebsite,
									  0 TongViewThucChay,
									  0 TongClickThucChay,
									  0 TongSoBaiViet,
									  0 AS SoLuongThucChay,
									  --Thanhuc Tien Thuc Chay
									  @NgayThucHien AS NgayThucHien,
									  A.GiaTriThayDoi AS GiaTriThayDoi
							   FROM   (
										  SELECT TOP 1 
										  tcdt.SoHopDong,
												 tcdt.DmSanPhamREF,
												 tcdt.DmWebsiteREF,
												 tcdt.TenWebsite,
												 tcdt.NhanHang,
												 (@TongTienHopDong -(@TTThucChaySauChietKhau + @GiaTriThayDoi))  GiaTriThayDoi,
			                                     tcdt.DmBannerREF
										  FROM   ThucChayDaTinh tcdt
										  WHERE  TCDT.HopDongID = @HopDongREF
												 AND tcdt.DmSanPhamREF = @DmSanPhamID
												 AND (
														 tcdt.GiaTriThayDoi != 0
														 OR tcdt.ThanhTienSauTrietKhauThucChay 
															!= 0
												 )
												 AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3
										  GROUP BY
												 tcdt.SoHopDong,
												 tcdt.DmSanPhamREF,
												 tcdt.DmWebsiteREF,
												 tcdt.TenWebsite,
												 tcdt.NhanHang,
												 tcdt.DmBannerREF
									  )A
									  LEFT JOIN (
											   SELECT hd.SoHopDong,
													  hd.HopDongID,
													  --Thong tin ve ma so 
													  hd.DmMaHopDongREF,
													  hd.TenMaHopDong,
													  --Thong tin ve thoi gian
													  hd.NgayDanhSoHopDong,
													  hd.NgayKyHopDong,
													  hd.NhanHopDong,
													  hd.NgayNhanBanFax,
													  hd.NgayNhanHopDongBanCung,
													  hd.NgayChuyenHopDongChoKeToan,
													  hd.So,
													  hd.Thang,
													  hd.Nam,
													  --Thong tin ve gia tri
													  hd.GiaTriHopDong,
													  hd.CongNo,
													  --Thong tin chi tiet phan bo
													  --Thong tin ve trang thai
													  hd.DangSuDung,
													  hd.IsGiayPhep,
													  hd.TrangThaiHopDong,
													  hd.IsBanCung,
													  --Thong tin ve Nhan vien kinh doanh
													  hd.DmPhongBanREF,
													  ISNULL(hd.TenPhongBan, '') AS 
													  TenPhongBan,
													  hd.DmBoPhanREF,
													  ISNULL(hd.TenBoPhan, '') AS 
													  TenBoPhan,
													  hd.DmNhomLamViecREF,
													  ISNULL(hd.TenNhom, '') AS TenNhom,
													  hd.DmDiaDiemLamViecREF,
													  hd.TenDiaDiemLamViec,
													  hd.SysNhanVienREF,
													  ISNULL(hd.TenDangNhap, '') AS 
													  TenDangNhap,
													  hd.TenNhanVien,
													  hd.TenKhachHang,
													  HDCT.DmSanPhamREF,
													  HDCT.TenSanPham,
													  MAX(hdct.DmLoaiREF) AS DmHinhThucSanPhamREF,
													  MAX(hdct.TenLoai) AS TenHinhThucSanPham,
													  SUM(hdct.SoLuong) soluongdotchayHD,
													  SUM(
														  hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
													  ) soluong,
													  SUM(hdct.ThanhTien) ThanhTien,
													  MAX(dbo.ThucChay_GetDonViTinhNotCPD(hdct.DonViTinh)) AS 
													  DonViTinh,
													  MAX(
														  hdct.ThanhTien / (
															  hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
														  )
													  ) DonGiaSauCK,
													  MAX(
														  hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
													  ) DonGia
											   FROM   HopDong hd
													  INNER JOIN HopDongChiTiet hdct
														   ON  HD.HopDongID = HDCT.HopDongFK
														   AND HDCT.DmSanPhamREF = @DmSanPhamID
														   AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3
														   AND hdct.DeletedStatus = 0
														   AND hdct.SoLuong > 0
											   GROUP BY
													  HDCT.DmSanPhamREF,
													  HDCT.TenSanPham,
													  HD.SoHopDong,
													  hd.HopDongID,
													  --Thong tin ve ma so 
													  hd.DmMaHopDongREF,
													  hd.TenMaHopDong,
													  --Thong tin ve thoi gian
													  hd.NgayDanhSoHopDong,
													  hd.NgayKyHopDong,
													  hd.NhanHopDong,
													  hd.NgayNhanBanFax,
													  hd.NgayNhanHopDongBanCung,
													  hd.NgayChuyenHopDongChoKeToan,
													  hd.So,
													  hd.Thang,
													  hd.Nam,
													  --Thong tin ve gia tri
													  hd.GiaTriHopDong,
													  hd.CongNo,
													  --Thong tin chi tiet phan bo
													  --Thong tin ve trang thai
													  hd.DangSuDung,
													  hd.IsGiayPhep,
													  hd.TrangThaiHopDong,
													  hd.IsBanCung,
													  --Thong tin ve Nhan vien kinh doanh
													  hd.DmPhongBanREF,
													  hd.TenPhongBan,
													  hd.DmBoPhanREF,
													  hd.TenBoPhan,
													  hd.DmNhomLamViecREF,
													  hd.TenNhom,
													  hd.DmDiaDiemLamViecREF,
													  hd.TenDiaDiemLamViec,
													  hd.SysNhanVienREF,
													  hd.TenDangNhap,
													  hd.TenNhanVien,
													  hd.TenKhachHang
										   )B
										   ON  UPPER(LTRIM(RTRIM(A.SoHopDong))) = B.SoHopDong
										   AND A.DmSanPhamREF = B.DmSanPhamREF 
											   --AND B.DonGiaSauCK > 0
											   --ORDER BY A.TenSanPham ,a.SoHopDong,a.TenWebsite
						   ) TD
					WHERE  TD.SoHopDong IS NOT NULL   	
	        END
	        --INSERT LOG
	        INSERT INTO ThucChay_LogNNTinhGiaTriThayDoi
	        SELECT NEWID(),
	                          ISNULL(b.HopDongID, 0) HopDongID,
	                          --Thong tin ve ma so 
	                          b.SoHopDong,
	                          0 HopDongChiTietREF,
	                          b.DmSanPhamREF AS DmSanPhamREF,
	                          A.DmWebsiteREF DmWebsiteREF,
	                          @NgayThucHien AS NgayThucHien,
	                          A.GiaTriThayDoi AS GiaTriThayDoi,
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
	                              SELECT tcdt.SoHopDong,
	                                     tcdt.DmSanPhamREF,
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
	                                     ) GiaTriThayDoi,
										 tcdt.DmBannerREF
	                              FROM   ThucChayDaTinh tcdt
	                              WHERE  TCDT.HopDongID = @HopDongREF
										 AND tcdt.DmSanPhamREF = @DmSanPhamID
	                                     AND (
	                                             tcdt.GiaTriThayDoi != 0
	                                             OR tcdt.ThanhTienSauTrietKhauThucChay 
	                                                != 0
	                                     )
	                                     AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh)  = 3
	                              GROUP BY
	                                     tcdt.SoHopDong,
	                                     tcdt.DmSanPhamREF,
	                                     tcdt.DmWebsiteREF,
	                                     tcdt.TenWebsite,
										 tcdt.DmBannerREF
	                          )A
	                          LEFT JOIN (
	                                   SELECT hd.SoHopDong,
	                                          hd.HopDongID,
	                                          HDCT.DmSanPhamREF,
	                                          HDCT.TenSanPham,
	                                          MAX(hdct.DmLoaiREF) AS DmHinhThucSanPhamREF,
	                                          MAX(hdct.TenLoai) AS TenHinhThucSanPham,
	                                          SUM(hdct.SoLuong) soluongdotchayHD,
	                                          SUM(
	                                              hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                                          ) soluong,
	                                          SUM(hdct.ThanhTien) ThanhTien,
	                                          MAX(dbo.ThucChay_GetDonViTinhNotCPD(hdct.DonViTinh)) AS 
	                                          DonViTinh,
	                                          MAX(
	                                              hdct.ThanhTien / (
	                                                  hdct.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                                              )
	                                          ) DonGiaSauCK,
	                                          MAX(
	                                              hdct.DonGia / dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)
	                                          ) DonGia
	                                   FROM   HopDong hd
	                                          INNER JOIN HopDongChiTiet hdct
	                                               ON  HD.HopDongID = HDCT.HopDongFK
	                                               AND HDCT.DmSanPhamREF = @DmSanPhamID
	                                               AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3
	                                               AND hdct.DeletedStatus = 0
	                                               AND hdct.SoLuong > 0
	                                   GROUP BY
	                                          HDCT.DmSanPhamREF,
	                                          HDCT.TenSanPham,
	                                          HD.SoHopDong,
	                                          hd.HopDongID,
	                                          --Thong tin ve ma so 
	                                          hd.DmMaHopDongREF,
	                                          hd.TenMaHopDong,
	                                          --Thong tin ve thoi gian
	                                          hd.NgayDanhSoHopDong,
	                                          hd.NgayKyHopDong,
	                                          hd.NhanHopDong,
	                                          hd.NgayNhanBanFax,
	                                          hd.NgayNhanHopDongBanCung,
	                                          hd.NgayChuyenHopDongChoKeToan,
	                                          hd.So,
	                                          hd.Thang,
	                                          hd.Nam,
	                                          --Thong tin ve gia tri
	                                          hd.GiaTriHopDong,
	                                          hd.CongNo,
	                                          --Thong tin chi tiet phan bo
	                                          --Thong tin ve trang thai
	                                          hd.DangSuDung,
	                                          hd.IsGiayPhep,
	                                          hd.TrangThaiHopDong,
	                                          hd.IsBanCung,
	                                          --Thong tin ve Nhan vien kinh doanh
	                                          hd.DmPhongBanREF,
	                                          hd.TenPhongBan,
	                                          hd.DmBoPhanREF,
	                                          hd.TenBoPhan,
	                                          hd.DmNhomLamViecREF,
	                                          hd.TenNhom,
	                                          hd.DmDiaDiemLamViecREF,
	                                          hd.TenDiaDiemLamViec,
	                                          hd.SysNhanVienREF,
	                                          hd.TenDangNhap,
	                                          hd.TenNhanVien,
	                                          hd.TenKhachHang
	                               )B
	                               ON  UPPER(LTRIM(RTRIM(A.SoHopDong))) = B.SoHopDong
	                               AND A.DmSanPhamREF = B.DmSanPhamREF 
	    END
	END
	
	SELECT 2
END

--EXEC [ThucChay_UpdateGiaTriTDTCCPMSanPhamByNgay] '2013-09-20', 'QC124555', 123454, 339

```
