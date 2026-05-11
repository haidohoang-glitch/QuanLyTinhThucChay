# Stored Procedure: `prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:01:56.053000
- **Ngày sửa cuối**: 2024-06-29 11:22:21.347000

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
CREATE PROCEDURE [dbo].[prc_asd_ThucChayDaTinhAdmarket_InsertByPhanBoID_ThayDoiHopDong_PhanBo]
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

	DECLARE @OutputTbl TABLE (ThucChayDaTinhID NVARCHAR(100),HopDongChiTietREF int )

	INSERT INTO ThucChayDaTinhAdmarket   
	OUTPUT INSERTED.ThucChayDaTinhID,INSERTED.HopDongChiTietREF INTO @OutputTbl(ThucChayDaTinhID,HopDongChiTietREF)                   
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

	--CHECK NEU THUC HIEN INSERT THANH CONG THI THUC HIEN DOI TRU
	IF(EXISTS(SELECT top 1 ThucChayDaTinhID FROM @OutputTbl where hopdongchitietref = @PhanBoID ))
	BEGIN
		DECLARE @DmMaHopDongREF INT = 0, @TenMaHopDong NVARCHAR(50) = N'', @NhanHang NVARCHAR(100), @v_ThucChayDaTinhID nvarchar(100) = ''
		, @v_GiaTriThayDoi FLOAT = 0, @v_SoLuongThucChay BIGINT = 0

		SELECT top 1 @DmMaHopDongREF = hd.DmMaHopDongREF, @TenMaHopDong = hd.TenMaHopDong FROM dbo.HopDong hd
		WHERE hd.SoHopDong = @SoHopDong

		SELECT top 1 @v_ThucChayDaTinhID = ThucChayDaTinhID FROM @OutputTbl where hopdongchitietref = @PhanBoID

		SET @DmMaHopDongREF = ISNULL(@DmMaHopDongREF,0)
		SET @TenMaHopDong = ISNULL(@TenMaHopDong,'')
		SET @NhanHang = CONVERT(NVARCHAR(50),@DmNhanHangREF)
		SET @v_ThucChayDaTinhID = ISNULL(@v_ThucChayDaTinhID,'')
		SET @v_GiaTriThayDoi = -@ThanhTienThucChay
		SET @v_SoLuongThucChay = -@SoLuongThucChay

		SET @GhiChu = N'Đối trừ vào online cho bản ghi vừa ghi nhận hdct:' + Convert(nvarchar(100),@PhanBoID) + ', ThucChayDaTinhID = ' + @v_ThucChayDaTinhID

		--THUC HIEN DOI TRU ONLINE CHO CAN VIEC TANG GIA TRI THEO PHAN BO
		EXEC [dbo].[ThucChayDaTinhAdmarket_InsertNoContractByProduct_PhanBo]
		-- Add the parameters for the stored procedure here	
		@DmSanPhamREF			= @DmSanPhamREF,
		@TenSanPham				= @TenSanPham,
		@DonViTinh				= @DonViTinhSanPham,
		@DmWebsiteREF			= @DmWebsiteREF,
		@TenWebsite				= @TenWebsite,
		@NgayThucHien			= @NgayThucHien,
		@SoLuongThucChay		= 0,
		@SoLuongThhucChayKM		= 0,
		@ThanhTienThucChay		= 0,
		@ThanhTienThucChayKM	= 0,
		@DmMaHopDongREF			= @DmMaHopDongREF,
		@TenMaHopDong			= @TenMaHopDong,
		@GhiChu					= @GhiChu,
		@GiaTriThayDoi			= @v_GiaTriThayDoi,
		@SoLuongThayDoi			= @v_SoLuongThucChay,
		@DmViTriREF				= @DmViTriREF,
		@TenViTri				= @TenViTri,
		@NhanHang				= @NhanHang,
		@HopDongChiTietREF		= @PhanBoID,
		@Data_Type				= 0
	END
END



```
