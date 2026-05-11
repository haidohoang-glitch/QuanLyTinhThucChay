# Stored Procedure: `ThucChay_GoogleFacebookInsertGTTD_TinhLai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-10-07 09:34:26.737000
- **Ngày sửa cuối**: 2017-10-07 09:34:26.737000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `nvarchar(100)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DmLoaiBannerREF` | `int(4)` | No |
| `@NhanHopDong` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC  [dbo].[ThucChay_GoogleFacebookInsertGTTD_Doannv] '2015-10-23','GG020115','Google Ads',1402,2727272,'CPC'
CREATE PROCEDURE [dbo].[ThucChay_GoogleFacebookInsertGTTD_TinhLai]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF NVARCHAR(50),
	@SoLuongThucChay INT, 
	@ThanhTienThucChay FLOAT, 
	@DonViTinh NVARCHAR(50),
	@DmLoaiBannerREF INT,
	@NhanHopDong NVARCHAR(500) 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    DECLARE @HopDongID INT , @HopDongChiTietID INT, @SoLuongPhanBo INT, @ThanhTienPhanBo FLOAT
    DECLARE @SoLuongPhanBoThucChay INT, @ThanhTienPhanBoThucChay FLOAT
    DECLARE @SoLuongCheck INT, @ThanhTienCheck FLOAT
    DECLARE @SoLuongThucChayInsert INT , @ThanhTienThucChayInsert FLOAT
    DECLARE @SoLuongHopDong INT , @ThanhTienHopDong FLOAT
    
     DECLARE @SoLuongThucChayHopDong INT , @ThanhTienThucChayHopDong FLOAT
     
     DECLARE @DonViTinhThucChay NVARCHAR(50), @TrangThai INT SET @TrangThai =0
    -- Insert statements for procedure here
    	 --- Kiểm tra đơn vị tính
    IF @DmLoaiBannerREF <> 1 AND @DmLoaiBannerREF <> 16
		BEGIN
			SET @DonViTinhThucChay = (SELECT TenLoaiBanner FROM DmLoaiBanner dlb WHERE dlb.DmLoaiBannerID = @DmLoaiBannerREF)
			IF @DonViTinhThucChay = N'Chi phí' OR @DonViTinhThucChay = N'Chi phí quản lý'
			SET @DonViTinhThucChay =  N'Gói'
			IF @DonViTinhThucChay = N'Thời gian' 
			SET @DonViTinhThucChay =  N'Ngày'
		END
	ELSE
		BEGIN
			IF isnull(@DonViTinh,'') <> '' 
			BEGIN
			SET @DonViTinhThucChay = @DonViTinh
			IF @DonViTinhThucChay = N'Tuần' OR @DonViTinhThucChay = N'Tháng' OR @DonViTinhThucChay = N'Năm'
			SET @DonViTinhThucChay = N'Ngày'
			IF @DonViTinhThucChay ='CPC' SET @DonViTinhThucChay = 'Click'
			END
			ELSE  SET @DonViTinhThucChay = N'Gói'
		END
		IF(@DonViTinhThucChay =N'Gói') SET @TrangThai = 2
	    ELSE SET @TrangThai= 1 
	
	
	DECLARE db_cursorinsert CURSOR FOR  
	SELECT 
	hd.HopDongID,
	hdct.HopDongChiTietID,
	hdct.SoLuong,
	hdct.ThanhTien
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct
	ON hd.HopDongID = hdct.HopDongFK
	WHERE 1=1
			AND hdct.DeletedStatus =0
			AND hd.DeletedStatus =0
			AND hd.TrangThaiHopDong <> 3
			AND hd.SoHopDong = @SoHopDong
			AND hdct.TenSanPham = @DmSanPhamREF
			AND hdct.DonViTinh = @DonViTinh
			--AND hdct.DonViTinh = @DonViTinhThucChay
			AND hdct.DmLoaiBannerREF = @DmLoaiBannerREF
	ORDER BY hdct.HopDongChiTietID DESC
	
	OPEN db_cursorinsert   
	
	FETCH NEXT FROM db_cursorinsert INTO @HopDongID,@HopDongChiTietID,@SoLuongPhanBo,@ThanhTienPhanBo

	WHILE @@FETCH_STATUS = 0   
	BEGIN  
	
		  -- Thuc chay da tinh theo phan bo (hop dong chi tiet)
		  SET @SoLuongPhanBoThucChay = ISNULL((SELECT SUM(SoLuongThucChay + SoLuongThayDoi)
		                                 FROM ThucChayDaTinh WHERE HopDongChiTietREF = @HopDongChiTietID
										  AND TrangThaiHopDong <> 3),0)
		  SET @ThanhTienPhanBoThucChay = ISNULL((SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
		                                 FROM ThucChayDaTinh WHERE HopDongChiTietREF = @HopDongChiTietID
										  AND TrangThaiHopDong <> 3),0)
          -- tinh theo hop dong
		  --SET @SoLuongHopDong = ISNULL((SELECT SUM(SoLuong)
		  --                               FROM HopDongChiTiet WHERE HopDongFK = @HopDongID
				--						  AND TenSanPham = @DmSanPhamREF
				--						  AND DonViTinh = @DonViTinh),0)
		  --SET @ThanhTienHopDong = ISNULL((SELECT SUM(ThanhTien)
		  --                                FROM HopDongChiTiet WHERE HopDongFK = @HopDongID
				--						  AND TenSanPham = @DmSanPhamREF
				--						  AND DonViTinh = @DonViTinh),0)
		  -- thuc chay da tinh theo hop dong							  
		  SET @SoLuongThucChayHopDong = ISNULL((SELECT SUM(SoLuongThucChay + SoLuongThayDoi)
		                                 FROM ThucChayDaTinh WHERE HopDongID = @HopDongID
		                                 AND TenSanPham =  @DmSanPhamREF
		                                 AND DonViTinh = @DonViTinhThucChay
		                                 AND DmLoaiBannerREF = @DmLoaiBannerREF
										  AND TrangThaiHopDong <> 3),0)
		  SET @ThanhTienThucChayHopDong = ISNULL((SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
		                                 FROM ThucChayDaTinh WHERE HopDongID = @HopDongID
		                                 AND TenSanPham =  @DmSanPhamREF
		                                 AND DonViTinh = @DonViTinhThucChay
		                                    AND DmLoaiBannerREF = @DmLoaiBannerREF
										  AND TrangThaiHopDong <> 3),0)
		IF @DonViTinh = N'Tuần' SET @SoLuongPhanBo = @SoLuongPhanBo * 7
		IF @DonViTinh = N'Tháng' SET @SoLuongPhanBo = @SoLuongPhanBo * 30
		IF @DonViTinh = N'Năm' SET  @SoLuongPhanBo = @SoLuongPhanBo * 365
	-- Kiem tra xem da chay chua
	IF @SoLuongPhanBoThucChay > 0 OR @ThanhTienPhanBoThucChay >0
	-- kiem tra theo hop dong
	IF @SoLuongThucChay < @SoLuongThucChayHopDong OR  round(@ThanhTienThucChay,-1) < round(@ThanhTienThucChayHopDong,-1) 
	-- kiem tra theo phan bo 
	   
    --IF @SoLuongPhanBo > @SoLuongPhanBoThucChay OR round(@ThanhTienPhanBo,-1) > round(@ThanhTienPhanBoThucChay,-1)
    BEGIN
    	print(1)
    	SET @SoLuongCheck =  @SoLuongThucChayHopDong - @SoLuongThucChay
    	SET @ThanhTienCheck = @ThanhTienThucChayHopDong - @ThanhTienThucChay
    	
    	IF @ThanhTienCheck < @ThanhTienPhanBoThucChay
    	   SET @ThanhTienThucChayInsert = @ThanhTienCheck
    	ELSE  SET @ThanhTienThucChayInsert = @ThanhTienPhanBoThucChay
    	
    	IF @SoLuongCheck < @SoLuongPhanBoThucChay
    	   SET @SoLuongThucChayInsert = @SoLuongCheck
    	ELSE  SET @SoLuongThucChayInsert = @SoLuongPhanBoThucChay
  
    -- Insert dữ liệu
    INSERT INTO ThucChayDaTinh                      
	SELECT DISTINCT
		NEWID() ThucChayDaTinhID,
		--ID Hop Dong
		D.HopDongID,
		--Thong tin ve ma so 
		D.SoHopDong, 
		D.DmMaHopDongREF, 
		D.TenMaHopDong, 
		--Thong tin ve thoi gian
		D.NgayDanhSoHopDong, D.NgayKyHopDong, 
		@NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
		D.So, D.Thang, D.Nam, 
		--Thong tin ve gia tri
		D.GiaTriHopDong, D.CongNo,
		--Thong tin chi tiet phan bo
		C.HopDongChiTietID AS HopDongChiTietREF,
		--Thong tin ve trang thai
		D.DangSuDung AS DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		D.DmPhongBanREF, 
		ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
		D.DmBoPhanREF, 
		ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
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
		C.DanhSachNhanHangREF NhanHang, 
		C.DmNhomNganhREF DmNhomNganhREF, 
		C.TenNhomNganh TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, 
		C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		c.DmSanPhamREF as DmSanPhamREF,
		c.TenSanPham as TenSanPham,  
		C.DmNhomWebsiteREF DmNhomWebsiteREF, 
		C.TenNhomWebsite TenNhomWebsite, 
		--C.DmWebsiteREF, 
		--C.TenWebsite, 
		C.DmChuyenMucREF DmChuyenMucREF, 
		C.TenChuyenMuc TenChuyenMuc, 
		C.DmLoaiBannerREF DmLoaiBannerREF, 
		C.TenLoaiBanner TenLoaiBanner, 
		C.DmViTriREF DmViTriREF, 
		C.TenViTri TenViTri, 
		ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
		C.SoLuong AS SoLuongDotChayHD,
		ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
		dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		--dbo.ThucChay_GetQuantityThucChay(C.DmSanPhamREF,C.SoLuong, C.DonViTinh) AS SoLuong,
		@SoLuongPhanBo,
		--****haidh chinh sua
		@DonViTinhThucChay, 
		--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
		
		c.DonGia AS DonGia,
		--****haidh chinh sua 
		ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, C.HopDongChiTietID),0),
		C.ChietKhau, C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		CASE WHEN @DmSanPhamREF = N'Google Ads' OR c.DmWebsiteREF = 285
		THEN 466
		WHEN @DmSanPhamREF = N'Facebook Ads' OR c.DmWebsiteREF = 307
		THEN 426
	
		ELSE (SELECT TOP 1 DmWebsiteREF FROM ThucChayDaTinh tcdt WHERE tcdt.SoHopDong =@SoHopDong AND tcdt.TenSanPham = @DmSanPhamREF)
		END DmWebsiteREF,
		CASE WHEN @DmSanPhamREF = N'Google Ads' OR c.DmWebsiteREF = 285
		THEN 'google.com.vn'
		WHEN @DmSanPhamREF = N'Facebook Ads' OR c.DmWebsiteREF = 307
		THEN 'facebook.com'
		ELSE (SELECT TOP 1 tcdt.TenWebsite FROM ThucChayDaTinh tcdt WHERE tcdt.SoHopDong =@SoHopDong AND tcdt.TenSanPham = @DmSanPhamREF)
		END TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		0 as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgayThucHien NgayThucHien,
		-@ThanhTienThucChayinsert as GiaTriThayDoi,
		0 as ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		0 ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		0 AS ThanhTienThucThu,
		0 as ThanhTienKM,
		0 as SoLuongThucChayKM,
		0 AS SoLuongLechTreoHa,
		0 AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		CASE WHEN @TrangThai = 1 THEN -@SoLuongThucChayInsert
		ELSE -1
		end SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		'' as GhiChu
	FROM
		HopDong AS D 
			INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
	WHERE D.TrangThaiHopDong <> 3
		AND C.HopDongChiTietID = @HopDongChiTietID
		AND D.HopDongID = @HopDongID
    	   
    END
    
	FETCH NEXT FROM db_cursorinsert INTO @HopDongID,@HopDongChiTietID,@SoLuongPhanBo,@ThanhTienPhanBo
	END   

	CLOSE db_cursorinsert   
	DEALLOCATE db_cursorinsert
END

```
