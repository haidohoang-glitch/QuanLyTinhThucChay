# Stored Procedure: `prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong_PhanBo_BK_20240529`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-05-29 15:14:06.637000
- **Ngày sửa cuối**: 2024-05-29 15:14:06.637000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@PhanBoID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@SoLuongThucChayKM` | `int(4)` | No |
| `@ThanhTienThucChayKM` | `float(8)` | No |
| `@SoLuongLechTreoHa` | `int(4)` | No |
| `@ThanhTienLechTreoHa` | `float(8)` | No |
| `@TypeInsert` | `int(4)` | No |
| `@DonViTinhSanPham` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |
| `@DmNhanHangREF` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: 2017
-- Description:	Insert Thuc chay da tinh Boxapp SSV theo website, san pham
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong_PhanBo_BK_20240529]
	-- Add the parameters for the stored procedure here
	@NgayThucHien			DATETIME,
	@SoHopDong				NVARCHAR(50),
	@PhanBoID				INT,
	@DmSanPhamREF			INT,
	@TenSanPham				NVARCHAR(50),
	@DmWebsiteREF			INT,
	@TenWebsite				NVARCHAR(50),
	@TongViewThucChay		INT,
	@TongClickThucChay		INT,
	@SoLuongThucChay		INT,
	@ThanhTienThucChay		FLOAT,
	@SoLuongThucChayKM		INT,
	@ThanhTienThucChayKM	FLOAT,
	@SoLuongLechTreoHa		INT,
	@ThanhTienLechTreoHa	FLOAT,
	@TypeInsert				INT, -- 1: ThucChay; 2: KhuyenMai; 3 LechTreoHa
	@DonViTinhSanPham		NVARCHAR(50),
	@GhiChu					NVARCHAR(255),
	@DmViTriREF				INT,
	@TenViTri				NVARCHAR(50),
	@DmNhanHangREF			NVARCHAR(200) 
AS
BEGIN
	DECLARE @TypeDonViTinh		INT = 0 -- 1: CPC/CPM; 0: Goi
	--PRINT 'PhanBoID: ' + CONVERT(NVARCHAR(50),@PhanBoID);
	if @DmSanPhamREF = 585 and @DmViTriREF = 0  set   @DmViTriREF = 1
	-----------------------------------------------------
	IF @DmViTriREF = 1  set @TenViTri = 'AdX'
	IF @DmViTriREF = 2  set @TenViTri = 'AdX Mobile'
	IF @DmViTriREF = 3  set @TenViTri = 'AdX Ecommerce'
	IF @DmViTriREF = 4  set @TenViTri = 'ADX Leadform'

	-----------------------------------------------------
	if isnull(@TongViewThucChay	,0) = 0 	set @TongViewThucChay = 1
	if isnull(@TongClickThucChay	,0) = 0 	set @TongClickThucChay = 1
	if isnull(@SoLuongThucChay	,0) = 0 	set @SoLuongThucChay = 1
	-----------------------------------------------------
	-- lấy tai khoan tu phan bo
	declare @TK_AdMarket nvarchar(100),@User_id nvarchar(50)
	select @TK_AdMarket = TK_AdMarket ,@User_id =TK_AdMarketID from HopDongChiTiet where HopDongChiTietID = @PhanBoID
	-----------------------------------------------------
	IF @DmSanPhamREF <> 585
	INSERT INTO ThucChayDaTinhAdmarket                      
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
		CONVERT(NVARCHAR(100),@DmNhanHangREF), 
		D.NgayNhanBanFax, 
		D.NgayNhanHopDongBanCung, 
		D.NgayChuyenHopDongChoKeToan, 
		D.So, 
		D.Thang, 
		D.Nam, 
		--Thong tin ve gia tri
		D.GiaTriHopDong, D.CongNo,
		--Thong tin chi tiet phan bo
		C.HopDongChiTietID AS HopDongChiTietREF,
		--Thong tin ve trang thai
		CASE @DmSanPhamREF
			WHEN 144 THEN 5001
			WHEN 299 THEN 5002
			WHEN 337 THEN 5003
			ELSE 0 -- AdX
		END AS DangSuDung, 
		D.IsGiayPhep, 
		D.TrangThaiHopDong,
		D.IsBanCung, 
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
		@DmNhanHangREF NhanHang, 
		'' DmNhomNganhREF, 
		'' TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, 
		C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		@DmSanPhamREF as DmSanPhamREF,
		@TenSanPham as TenSanPham,  
		C.DmNhomWebsiteREF DmNhomWebsiteREF, 
		C.TenNhomWebsite TenNhomWebsite, 
		--C.DmWebsiteREF, 
		--C.TenWebsite, 
		C.DmChuyenMucREF DmChuyenMucREF, 
		C.TenChuyenMuc TenChuyenMuc, 
		C.DmLoaiBannerREF DmLoaiBannerREF, 
		C.TenLoaiBanner TenLoaiBanner, 
		@DmViTriREF DmViTriREF, 
		@TenViTri TenViTri, 
		--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
		@GhiChu DotChayHopDong,
		C.SoLuong AS SoLuongDotChayHD,
		ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
		dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
		--****haidh chinh sua
		@DonViTinhSanPham DonViTinh, 
		--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
		dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,@PhanBoId,C.DonGia) AS DonGia,
		--****haidh chinh sua 
		ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, C.HopDongChiTietID),0),
		C.ChietKhau, C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		@DmWebsiteREF DmWebsiteREF,
		@TenWebsite AS TenWebsite,
		@TongViewThucChay TongViewThucChay,
		@TongClickThucChay TongClickThucChay,
		0 TongSoBaiViet,
		@SoLuongThucChay as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgayThucHien NgayThucHien,
		@ThanhTienThucChay as GiaTriThayDoi,
		0 as ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		0 ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		@ThanhTienThucChay AS ThanhTienThucThu,
		@ThanhTienThucChayKM as ThanhTienKM,
		@SoLuongThucChayKM as SoLuongThucChayKM,
		@SoLuongLechTreoHa AS SoLuongLechTreoHa,
		@ThanhTienLechTreoHa AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 as SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		@GhiChu as GhiChu
	FROM
		HopDong AS D 
			INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
	WHERE D.TrangThaiHopDong <> 3
		AND C.HopDongChiTietID = @PhanBoID
		AND D.SoHopDong = @SoHopDong
	ELSE
	BEGIN
		declare @i int  =1 , @giatrivitri1 money, @giatrivitri2 money
		, @giatrivitri3 money, @giatrivitri4 money,
		@giatri1 money ,@giatri2 money 
		, @giatri3 money, @giatri4 money
		
		
		select @giatrivitri1 = SUM(convert(money,domain_money)) 
			from [dbo].ThucChayAdmarket_HopDong_online 
			where contract_number = @SoHopDong 
			and trangthai = 0 
			and DmSanPhamREF = 585
			and user_id = @User_id
			and DmViTriREF = 1

		select @giatrivitri2 = SUM(convert(money,domain_money)) 
			from [dbo].ThucChayAdmarket_HopDong_online 
			where contract_number = @SoHopDong 
			and trangthai = 0 
			and DmSanPhamREF = 585
			and user_id = @User_id
			and DmViTriREF = 2
		select @giatrivitri3 = SUM(convert(money,domain_money)) 
			from [dbo].ThucChayAdmarket_HopDong_online 
			where contract_number = @SoHopDong 
			and trangthai = 0 
			and DmSanPhamREF = 585
			and user_id = @User_id
			and DmViTriREF = 3

		select @giatrivitri4 = SUM(convert(money,domain_money)) 
			from [dbo].ThucChayAdmarket_HopDong_online 
			where contract_number = @SoHopDong 
			and trangthai = 0 
			and DmSanPhamREF = 585
			and user_id = @User_id
			and DmViTriREF = 4

		-- 
		
		set @giatrivitri1 = isnull(@giatrivitri1,0)
		set @giatrivitri2 = isnull(@giatrivitri2,0)
		set @giatrivitri3 = isnull(@giatrivitri3,0)
		set @giatrivitri4 = isnull(@giatrivitri4,0)

		-- tính tỷ lệ theo giá trị tăng

		if @giatrivitri1 <> 0 set @giatri1 = @giatrivitri1/(@giatrivitri1 + @giatrivitri2 + @giatrivitri3 + @giatrivitri4) * @ThanhTienThucChay
		if @giatrivitri2 <> 0 set @giatri2 = @giatrivitri2/(@giatrivitri1 + @giatrivitri2 + @giatrivitri3 + @giatrivitri4) * @ThanhTienThucChay
		if @giatrivitri3 <> 0 set @giatri3 = @giatrivitri3/(@giatrivitri1 + @giatrivitri2 + @giatrivitri3 + @giatrivitri4) * @ThanhTienThucChay
		if @giatrivitri4 <> 0 set @giatri4 = @ThanhTienThucChay - @giatri1 - @giatri2 - @giatri3
		
		if @giatrivitri1 <> 0  and abs(@ThanhTienThucChay - @giatri1 - @giatri2 - @giatri3 - @giatri4) >0  
			set @giatri1 = @giatri1 - (@ThanhTienThucChay -@giatri1 - @giatri2 - @giatri3 - @giatri4)
		else if @giatrivitri2 <> 0  and abs(@ThanhTienThucChay -@giatri1 - @giatri2 - @giatri3 - @giatri4) >0  
			set @giatri2 = @giatri2 - (@ThanhTienThucChay -@giatri1 - @giatri2 - @giatri3 - - @giatri4)
		else if @giatrivitri3 <> 0  and abs(@ThanhTienThucChay -@giatri1 - @giatri2 - @giatri3 - @giatri4) >0  
			set @giatri3 = @giatri3 - (@ThanhTienThucChay -@giatri1 - @giatri2 - @giatri3 - @giatri4)
		else if @giatrivitri4 <> 0  and abs(@ThanhTienThucChay -@giatri1 - @giatri2 - @giatri3 - @giatri4) >0  
			set @giatri4 = @giatri4 - (@ThanhTienThucChay -@giatri1 - @giatri2 - @giatri3 - @giatri4)
		

	WHILE @i <=4
	BEGIN
			declare @giatrithaydoi money 
			if @i = 1 set @giatrithaydoi = @giatri1
			if @i = 2 set @giatrithaydoi = @giatri2
			if @i = 3 set @giatrithaydoi = @giatri3
			if @i = 4 set @giatrithaydoi = @giatri4

    IF abs(@giatrithaydoi) > 0
	BEGIN
		INSERT INTO ThucChayDaTinhAdmarket                      
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
			CONVERT(NVARCHAR(100),@DmNhanHangREF), 
			D.NgayNhanBanFax, 
			D.NgayNhanHopDongBanCung, 
			D.NgayChuyenHopDongChoKeToan, 
			D.So, 
			D.Thang, 
			D.Nam, 
			--Thong tin ve gia tri
			D.GiaTriHopDong, D.CongNo,
			--Thong tin chi tiet phan bo
			C.HopDongChiTietID AS HopDongChiTietREF,
			--Thong tin ve trang thai
			CASE @DmSanPhamREF
				WHEN 144 THEN 5001
				WHEN 299 THEN 5002
				WHEN 337 THEN 5003
				ELSE 0 -- AdX
			END AS DangSuDung, 
			D.IsGiayPhep, 
			D.TrangThaiHopDong,
			D.IsBanCung, 
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
			@DmNhanHangREF NhanHang, 
			'' DmNhomNganhREF, 
			'' TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, 
			C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			@DmSanPhamREF as DmSanPhamREF,
			@TenSanPham as TenSanPham,  
			C.DmNhomWebsiteREF DmNhomWebsiteREF, 
			C.TenNhomWebsite TenNhomWebsite, 
			--C.DmWebsiteREF, 
			--C.TenWebsite, 
			C.DmChuyenMucREF DmChuyenMucREF, 
			C.TenChuyenMuc TenChuyenMuc, 
			C.DmLoaiBannerREF DmLoaiBannerREF, 
			C.TenLoaiBanner TenLoaiBanner, 
			case when @i = 1 then 1 when @i= 2 then 2  when @i= 3 then 3 else 4 end DmViTriREF, 
			case when  @i = 1  then 'AdX'
				 when  @i= 2   then 'AdX Mobile'
				 when  @i = 3   then 'AdX Ecommerce'
				 when  @i = 4   then 'ADX Leadform' end TenViTri, 
			--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
			@GhiChu DotChayHopDong,
			C.SoLuong AS SoLuongDotChayHD,
			N'' DotChayBooking,
			0 SoLuongDotChayBooking, 
			--Thong tin ve Tien
			--****haidh chinh sua
			C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
			--****haidh chinh sua
			@DonViTinhSanPham DonViTinh, 
			--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,@PhanBoId,C.DonGia) AS DonGia,
			--****haidh chinh sua 
			ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, C.HopDongChiTietID),0),
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
			@DmWebsiteREF DmWebsiteREF,
			@TenWebsite AS TenWebsite,
			@TongViewThucChay TongViewThucChay,
			@TongClickThucChay TongClickThucChay,
			0 TongSoBaiViet,
			@SoLuongThucChay as SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien NgayThucHien,
			@giatrithaydoi,
			0 as ThanhTienThucChayTruocTrietKhau,
			0 GiaTriTrietKhauThucChay,
			0 ThanhTienSauTrietKhauThucChay,
			0 AS GiaTriHoaHongThucChay,
			@ThanhTienThucChay AS ThanhTienThucThu,
			@ThanhTienThucChayKM as ThanhTienKM,
			@SoLuongThucChayKM as SoLuongThucChayKM,
			@SoLuongLechTreoHa AS SoLuongLechTreoHa,
			@ThanhTienLechTreoHa AS ThanhTienLechTreoHa,
			GETDATE(),
			GETDATE(),
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			0 as SoLuongThayDoi,
			0 as SoLuongKMThayDoi,
			0 as GiaTriKMThayDoi,
			@GhiChu as GhiChu
		FROM
			HopDong AS D 
				INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
		WHERE D.TrangThaiHopDong <> 3
			AND C.HopDongChiTietID = @PhanBoID
			AND D.SoHopDong = @SoHopDong
		IF @i = 1  set @TenViTri = 'AdX'
		IF @i = 2  set @TenViTri = 'AdX Mobile'
		IF @i = 3  set @TenViTri = 'AdX Ecommerce'
		IF @i = 4  set @TenViTri = 'ADX Leadform'
		declare @j nvarchar(10) set @j = CONVERT(nvarchar(10),@i)
		declare @giatriam nvarchar(50) 
		IF @i = 1  set @giatriam = convert(nvarchar(500), - @giatri1)
		IF @i = 2  set @giatriam = convert(nvarchar(500), - @giatri2)
		IF @i = 3 set @giatriam = convert(nvarchar(500), - @giatri3)
		IF @i = 4 set @giatriam = convert(nvarchar(500), - @giatri4)
		
			
	END
		set @i +=1;
	END
	--update [dbo].ThucChayAdmarket_HopDong_online set trangthai = 1 where contract_number = @SoHopDong and user_id = @User_id
	END
END

/****** Object:  StoredProcedure [dbo].[ThucChayDaTinhAdmarket_InsertNoContractByProduct]    Script Date: 9/9/2014 4:23:12 PM ******/
SET ANSI_NULLS ON

```
