# Stored Procedure: `ThucChayDaTinh_InsertThucChayDaTinhAdmarketByPhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-10 15:04:31.967000
- **Ngày sửa cuối**: 2015-03-03 13:55:02.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@PhanBoId` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@SiteName` | `nvarchar(100)` | No |
| `@DonViTinhSanPham` | `nvarchar(100)` | No |
| `@DonViTinhPhanBo` | `nvarchar(100)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@DonGiaTheoDonViTinh` | `int(4)` | No |
| `@ThanhTienThucChayTruocCK` | `float(8)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@SoLuongThucChayKM` | `int(4)` | No |
| `@ThanhTienThucChayKM` | `float(8)` | No |
| `@SoLuongLechTreoHa` | `int(4)` | No |
| `@ThanhTienLechTreoHa` | `float(8)` | No |
| `@TypeInsert` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-10
-- Description:	Insert Thuc chay da tinh Admarket theo phan bo
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChayDaTinhAdmarketByPhanBo]
	-- Add the parameters for the stored procedure here
	@NgayThucHien			DATETIME,
	--@ContractNo				NVARCHAR(50),
	@PhanBoId				INT,
	@DmSanPhamREF			INT,
	@TenSanPham				NVARCHAR(50),
	@SiteName				NVARCHAR(50),
	@DonViTinhSanPham		NVARCHAR(50),
	@DonViTinhPhanBo		NVARCHAR(50),
	@TongViewThucChay		INT,
	@TongClickThucChay		INT,
	@SoLuongThucChay		INT,
	@DonGiaTheoDonViTinh	INT,
	@ThanhTienThucChayTruocCK FLOAT,
	@ThanhTienThucChay		FLOAT,
	@SoLuongThucChayKM		INT,
	@ThanhTienThucChayKM	FLOAT,
	@SoLuongLechTreoHa		INT,
	@ThanhTienLechTreoHa	FLOAT,
	@TypeInsert				INT -- 1: ThucChay; 2: KhuyenMai; 3 LechTreoHa
AS
BEGIN
	DECLARE @TypeDonViTinh		INT = 0 -- 1: CPC/CPM; 0: Goi
	
	IF (@DonViTinhPhanBo = 'CPC' OR @DonViTinhPhanBo = 'CPM')
		SET @TypeDonViTinh = 1
	
	--INSERT INTO ThucChayDaTinhAdmarket	
	SELECT  NEWID(), TD.*, 
		ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
		--CASE WHEN ((ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) + @GiaTriThucChay) > @GiaTriHopDong) THEN	
		--			@GiaTriHopDong - @GiaTriThucChay
		--	 ELSE
		--	 	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) 
		--END AS ThanhTienSauTrietKhauThucChay,
		--ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
		@ThanhTienThucChay AS ThanhTienSauTrietKhauThucChay,
		ISNULL((((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
		ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
		CASE WHEN @TypeInsert = 2 THEN TD.ThanhTienThucChayTruocTrietKhau
			ELSE 0
		END as ThanhTienKM,
		@SoLuongThucChayKM as SoLuongThucChayKM,
		@SoLuongLechTreoHa AS SoLuongLechTreoHa,
		CASE WHEN @TypeInsert = 3 THEN 
				@SoLuongLechTreoHa*TD.DonGiaTheoDonViTinh
			 --WHEN (@TypeInsert = 1 AND ((ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) + @GiaTriThucChay) > @GiaTriHopDong)) THEN
			 --	@GiaTriThucChay + ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) - @GiaTriHopDong
			 ELSE 0
		END AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt	
	FROM
	(			                       
		SELECT distinct
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
			@DmSanPhamREF as DmSanPhamREF,
			@TenSanPham as TenSanPham,  
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
				 ELSE @DonViTinhSanPham
			END as DonViTinh, 
			--'VIEW' DonViTinh, 
			--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
			dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,@PhanBoId,C.DonGia) AS DonGia,
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
			0 DmBannerREF,--A.DmBannerREF,
			0 DmChienDichREF,--A.DmChienDichREF,
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
					--ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,@SoLuongThucChay,@SoLuongThucChay,0,@NgayThucHien,	C.HopDongChiTietID),0)
					@ThanhTienThucChayTruocCK					
				 WHEN @TypeInsert = 1 AND @TypeDonViTinh <> 1 THEN
				 	@ThanhTienThucChayTruocCK
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
			AND C.DmSanPhamREF = @DmSanPhamREF
			AND C.DeletedStatus = 0
	)TD
END

```
