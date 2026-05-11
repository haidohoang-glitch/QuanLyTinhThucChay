# Stored Procedure: `ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-10 09:59:47.723000
- **Ngày sửa cuối**: 2016-10-10 15:52:04.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(200)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@DmNhanHangThayDoiREF` | `int(4)` | No |
| `@ThanhTienThucChay` | `bigint(8)` | No |
| `@SoLuongThucChay` | `bigint(8)` | No |
| `@CONTENT_LOG` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_InsertGiaTriThayDoiThucChayDaTinhAdmarket_xulynhan] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@DmSanPhamREF INT,
	@HopDongChiTietREF INT,
	@DonViTinh NVARCHAR(100),
	@DmNhanHangREF INT,
	@DmNhanHangThayDoiREF INT,
	@ThanhTienThucChay BIGINT,
	@SoLuongThucChay BIGINT,
	@CONTENT_LOG NVARCHAR(MAX)
AS
BEGIN
	DECLARE @MinDate DATETIME
	DECLARE @GhiChu NVARCHAR(200) ='NH_TREO_TD_xuly: '
	DECLARE @count_HDCT              INT,
	        @DonGiaTheoDonViTinh     FLOAT,
	        @TongTienHopDong		 BIGINT,
	        @IsHDFinish				 INT,
			@SoLuongHopDong			 BIGINT
	
	
	SET @IsHDFinish = 0
	SET @count_HDCT = 0
	SET @SoLuongHopDong = 0
	SET @DonGiaTheoDonViTinh = 0
	PRINT 'NhanHang: ' + CONVERT(nvarchar(100),@DmNhanHangREF)
	IF (@count_HDCT = 0)--T/c tinh theo phuong phap thuc treo
	BEGIN
	  
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
	                       AND hdct.DmSanPhamREF = @DmSanPhamREF
	                       AND hdct.DeletedStatus = 0
	            )
	        
	        SET @DonGiaTheoDonViTinh = ISNULL(@DonGiaTheoDonViTinh, 0)
	        
	    
	        --   
			IF (@SoLuongThucChay >= @SoLuongHopDong)
			BEGIN
				SET @isHDFinish = 1
				SET @TongTienHopDong =
				(
					SELECT sum(hdct.ThanhTien)
					FROM   HopDongChiTiet hdct
					WHERE  hdct.HopDongFK = @HopDongID
						   AND hdct.HopDongChiTietID = @HopDongChiTietREF
						   AND hdct.DmSanPhamREF = @DmSanPhamREF
						   AND hdct.DeletedStatus = 0
				)
	        PRINT 'Thanh tien chenh lech :' + CONVERT(NVARCHAR(50), @ThanhTienThucChay)    
			PRINT @HopDongChiTietREF	
			END
			        
	        IF (@ThanhTienThucChay != 0)
	        BEGIN
			--DOI TRU AM VOI NHAN HANG BI CHUAN HOA
	            --INSERT INTO ThucChayDaTinhAdmarket
				INSERT INTO ThucChayDaTinhAdmarket_xulynhan
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
						(@GhiChu + 'Update nhan hang chuan hoa giam') GhiChu	
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
	                              @HopDongChiTietREF HopDongChiTiet,
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
	                              @DmNhanHangREF NhanHang,
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
	                              'ADMARKET_TTR' DotChayHopDong,
	                              C.SoLuong AS SoLuongDotChayHD,
	                              'PS THUC TREO ADMARKET' DotChayBooking,
	                              0 SoLuongDotChayBooking,
	                              C.SoLuong * dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS 
	                              SoLuong,
	                              --dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS 
	                              --DonViTinh,
								  @DonViTinh DonViTinh,
	                              dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien, @HopDongChiTietREF, C.DonGia) AS 
	                              DonGia,
	                              ISNULL(
	                                  dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(
	                                      C.SoLuong,
	                                      C.DonViTinh,
	                                      C.DonGia,
	                                      D.NgayKyHopDong,
	                                      @NgayThucHien,
	                                      @HopDongChiTietREF
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
	                              0 DmWebsiteREF,
	                              '' TenWebsite,
	                              0 TongViewThucChay,
	                              0 TongClickThucChay,
	                              0 TongSoBaiViet,
	                              0 AS SoLuongThucChay,
	                              @NgayThucHien NgayThucHien,
	                              - @ThanhTienThucChay AS GiaTriThayDoi,
	                              0 AS ThanhTienThucChayTruocTrietKhau
	                       FROM  HopDongChiTiet C
	                              INNER JOIN HopDong D
	                                   ON  D.HopDongID = C.HopDongFK
	                       WHERE  1=1
	                              --AND D.TrangThaiHopDong != 3
	                              AND C.DeletedStatus = 0
	                              AND C.DmSanPhamREF  IN (144,299,337,585,628)
								  AND C.HopDongChiTietID = @HopDongChiTietREF
								  AND C.HopDongFK= @HopDongID
	                   ) TD
	            
				--DOI TRU DUONG VOI NHAN HANG DUOC NHAN CHUAN HOA TU NHAN KHAC
				--INSERT INTO ThucChayDaTinhAdmarket
				INSERT INTO ThucChayDaTinhAdmarket_xulynhan
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
						(@GhiChu + 'Update nhan hang chuan hoa tang') GhiChu	
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
	                              @HopDongChiTietREF HopDongChiTiet,
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
	                              @DmNhanHangThayDoiREF NhanHang,
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
	                              --dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) AS 
	                              --DonViTinh,
								  @DonViTinh DonViTinh,
	                              dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien, @HopDongChiTietREF, C.DonGia) AS 
	                              DonGia,
	                              ISNULL(
	                                  dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(
	                                      C.SoLuong,
	                                      C.DonViTinh,
	                                      C.DonGia,
	                                      D.NgayKyHopDong,
	                                      @NgayThucHien,
	                                      @HopDongChiTietREF
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
	                              0 DmWebsiteREF,
	                              '' TenWebsite,
	                              0 TongViewThucChay,
	                              0 TongClickThucChay,
	                              0 TongSoBaiViet,
	                              0 AS SoLuongThucChay,
	                              @NgayThucHien NgayThucHien,
	                              @ThanhTienThucChay AS GiaTriThayDoi,
	                              0 AS ThanhTienThucChayTruocTrietKhau
	                       FROM  HopDongChiTiet C
	                              INNER JOIN HopDong D
	                                   ON  D.HopDongID = C.HopDongFK
	                       WHERE  1=1
	                             -- AND D.TrangThaiHopDong != 3
	                              AND C.DeletedStatus = 0
	                              AND C.DmSanPhamREF  IN (144,299,337,585,628) --144,299,337,585,628
								  AND C.HopDongChiTietID = @HopDongChiTietREF
								  AND C.HopDongFK = @HopDongID
	                   ) TD
	            
	            
					--Insert log
	               INSERT INTO [dbo].[ThucChay_LogNNTinhGiaTriThayDoi]
					  SELECT  NEWID(), D.HopDongID,
	                              --Thong tin ve ma so 
	                              D.SoHopDong,
	                              @HopDongChiTietREF HopDongChiTietREF,
	                              C.DmSanPhamREF AS DmSanPhamREF,
							      0 DmWebsiteREF,
								  @NgayThucHien NgayThucHien,
								  @ThanhTienThucChay GiaTriThayDoi,
	                              0 AS GiaSauCK1,
	                              0 Soluong1,
	                              0 AS GiaSauCK2,
	                              0 Soluong2,
	                              @CONTENT_LOG,
	                              N'Chuẩn hóa nhãn hàng ',
	                              'CPM',	'ThucChay',	GETDATE(),
								  'ThucChay',GETDATE(),0,
	                              0,0
					  FROM    HopDongChiTiet C
	                              INNER JOIN HopDong D
	                                   ON  D.HopDongID = C.HopDongFK
	                       WHERE  D.TrangThaiHopDong != 3
	                              AND C.DeletedStatus = 0
	                              AND C.DmSanPhamREF IN (144,299,337,585,628)
								  AND C.HopDongChiTietID = @HopDongChiTietREF
	                             
	        END
	END
	
	SELECT 2
END



```
