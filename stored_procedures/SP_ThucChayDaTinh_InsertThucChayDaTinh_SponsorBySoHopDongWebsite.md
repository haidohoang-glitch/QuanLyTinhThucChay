# Stored Procedure: `ThucChayDaTinh_InsertThucChayDaTinh_SponsorBySoHopDongWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-12 10:12:02.980000
- **Ngày sửa cuối**: 2014-11-19 12:25:00.943000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@PhanBoId` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@SiteName` | `nvarchar(100)` | No |
| `@DmChienDichREF` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@DonGiaTheoDonViTinh` | `int(4)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@SoLuongThucChayKM` | `int(4)` | No |
| `@ThanhTienThucChayKM` | `float(8)` | No |
| `@SoLuongLechTreoHa` | `int(4)` | No |
| `@ThanhTienLechTreoHa` | `float(8)` | No |
| `@TypeInsert` | `int(4)` | No |

## Definition (Source Code)

```sql
-- Stored Procedure

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

-- EXEC dbo.[ThucChayDaTinh_InsertThucChayDaTinh_SponsorBySoHopDongWebsite] '2014-05-10', 'CPC370613'
--

CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChayDaTinh_SponsorBySoHopDongWebsite]
	-- Add the parameters for the stored procedure here
	@NgayThucHien			DATETIME,
	@SoHopDong				NVARCHAR(50),
	@PhanBoId				INT,	
	@DonViTinh				NVARCHAR(50),	
	@DmWebsiteREF			INT,
	@SiteName				NVARCHAR(50),
	@DmChienDichREF			INT,	
	@DmBannerREF			INT,
	@TongViewThucChay		INT,
	@TongClickThucChay		INT,
	@SoLuongThucChay		INT,
	@DonGiaTheoDonViTinh	INT,
	@ThanhTienThucChay		FLOAT,
	@SoLuongThucChayKM		INT,
	@ThanhTienThucChayKM	FLOAT,
	@SoLuongLechTreoHa		INT,
	@ThanhTienLechTreoHa	FLOAT,
	@TypeInsert				INT -- 1: ThucChay; 2: KhuyenMai; 3 LechTreoHa
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

	DECLARE @TypeDonViTinh		INT = 0, -- 1: CPC/CPM; 0: Goi
			@DonViTinhPhanBo	NVARCHAR(50),
			@GiaTriHopDong		FLOAT = 0,
			@GiaTriThucChay		FLOAT = 0

	SET @DonViTinhPhanBo = (SELECT DonViTinh FROM HopDongChiTiet AS hdct WHERE hdct.HopDongChiTietID = @PhanBoId)
	IF (@DonViTinhPhanBo = 'CPC' OR @DonViTinhPhanBo = 'CPM')
		SET @TypeDonViTinh = 1

	SELECT @GiaTriHopDong = ISNULL(SUM(ThanhTien),0)
	FROM HopDong AS hd INNER JOIN HopDongChiTiet AS hdct ON hdct.HopDongFK = hd.HopDongID
	WHERE hd.SoHopDong = @SoHopDong 
		AND hdct.DmSanPhamREF = 381
		--AND hdct.HopDongChiTietID = @PhanBoId

	--PRINT 'GiaTriHopDong: ' + CONVERT(NVARCHAR(50),@GiaTriHopDong);

	SELECT @GiaTriThucChay = SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0) + ISNULL(GiaTriThayDoi,0))
	FROM ThucChayDaTinh AS tcdt
	WHERE tcdt.SoHopDong = @SoHopDong 
		AND tcdt.DmSanPhamREF = 381
		AND tcdt.NgayThucHien <= @NgayThucHien

	--PRINT 'GiaTriThucChay: ' + CONVERT(NVARCHAR(50),@GiaTriThucChay);

	IF @DonGiaTheoDonViTinh = 0 
		set @DonGiaTheoDonViTinh  = (select dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381))

	INSERT INTO ThucChayDaTinh
	SELECT  NEWID(), TD.*, 
		ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
		CASE WHEN ((ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) + @GiaTriThucChay) > @GiaTriHopDong) THEN	
					@GiaTriHopDong - @GiaTriThucChay
			 ELSE
			 	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) 
		END AS ThanhTienSauTrietKhauThucChay,		
		ISNULL((((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
		ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
		CASE WHEN @TypeInsert = 2 THEN TD.ThanhTienThucChayTruocTrietKhau
			ELSE 0
		END as ThanhTienKM,
		@SoLuongThucChayKM as SoLuongThucChayKM,
		@SoLuongLechTreoHa AS SoLuongLechTreoHa,
		CASE WHEN @TypeInsert = 3 THEN 
				round(@SoLuongLechTreoHa*TD.DonGiaTheoDonViTinh*(100-TD.ChietKhau)/100,0)
			 WHEN (@TypeInsert = 1 AND ((ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) + @GiaTriThucChay) > @GiaTriHopDong)) THEN
			 	@GiaTriThucChay + ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) - @GiaTriHopDong
			 ELSE 0
		END AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
 0 SoLuongKMThayDoi,
 0 GiaTriKMThayDoi,
 '' GhiChu
	FROM
	(			                       
		SELECT --distinct
			--ID Hop Dong
			D.HopDongID,
			--Thong tin ve ma so 
			D.SoHopDong, 
			D.DmMaHopDongREF, 
			D.TenMaHopDong, 
			--Thong tin ve thoi gian
			D.NgayDanhSoHopDong, D.NgayKyHopDong, 
			D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
			D.So, D.Thang, D.Nam, 
			--Thong tin ve gia tri
			D.GiaTriHopDong, D.CongNo,
			--Thong tin chi tiet phan bo
			C.HopDongChiTietID AS HopDongChiTietREF,
			--Thong tin ve trang thai
			D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
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
			C.NhanHang, 
			C.DmNhomNganhREF, 
			C.TenNhomNganh, 
			--Thong tin hinh thuc quang cao
			C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
			--Thong tin San pham
			381 as DmSanPhamREF,
			'Sponsor Post' AS TenSanPham,  
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
			ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
			C.SoLuong AS SoLuongDotChayHD,
			ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
			dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking, 
			--Thong tin ve Tien
			--****haidh chinh sua
			C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
			--****haidh chinh sua
			CASE WHEN @TypeDonViTinh = 1 THEN
					dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh)
				 ELSE @DonViTinh
			END as DonViTinh, 
			CASE WHEN @TypeDonViTinh = 1 THEN
				dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,@PhanBoId,C.DonGia) 
				ELSE dbo.ThucChayDaTinh_GetDonGiaBaoGiaSanPham(@NgayThucHien,381)	
			END AS DonGia,
			--****haidh chinh sua 
			CASE WHEN @TypeDonViTinh = 1 THEN
					ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, C.HopDongChiTietID),0) 
				 ELSE @DonGiaTheoDonViTinh
			END AS DonGiaTheoDonViTinh,
			C.ChietKhau, C.GiamGia, C.ThanhTien,
			C.TiLeTuVan,  C.ChiPhiTuVan,
			C.IsKhuyenMai,  
			C.KhuyenMai,
			--Thuc chay
			@DmBannerREF DmBannerREF,
			@DmChienDichREF DmChienDichREF,
			(SELECT TOP 1 DmWebsiteReportingdbID FROM DmWebsiteReportingdb WHERE DmWebsiteReportingdb.TenWebsite = @SiteName) DmWebsiteREF,
			@SiteName AS TenWebsite,
			@TongViewThucChay TongViewThucChay,
			@TongClickThucChay TongClickThucChay,
			0 TongSoBaiViet,
			@SoLuongThucChay as SoLuongThucChay,
			--Thanhuc Tien Thuc Chay
			@NgayThucHien NgayThucHien,
			0 as GiaTriThayDoi,
			CASE WHEN @TypeInsert = 1 AND @TypeDonViTinh = 1 THEN					
					@ThanhTienThucChay
				 WHEN @TypeInsert = 1 AND @TypeDonViTinh <> 1 THEN
				 	@SoLuongThucChay * @DonGiaTheoDonViTinh
				 WHEN @TypeInsert = 2 AND @TypeDonViTinh = 1 THEN 
					ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,@SoLuongThucChayKM,@SoLuongThucChayKM,0,@NgayThucHien,	C.HopDongChiTietID),0)
				 WHEN @TypeInsert = 2 AND @TypeDonViTinh <> 1 THEN
				 	@SoLuongThucChayKM * @DonGiaTheoDonViTinh	
				ELSE 0
			END as ThanhTienThucChayTruocTrietKhau 
		FROM
			HopDong AS D 
			INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
		WHERE D.TrangThaiHopDong <> 3
			AND C.HopDongChiTietID = @PhanBoId
			AND C.DmSanPhamREF = 381
			AND C.DeletedStatus = 0
	)TD
END

```
