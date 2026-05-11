# Stored Procedure: `ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-08 10:56:38.093000
- **Ngày sửa cuối**: 2021-07-08 12:27:13.370000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChayMuaNgoaiChiTietID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@ThanhTienThucChayBanSauCK` | `float(8)` | No |
| `@DonViTinhThucChay` | `nvarchar(100)` | No |
| `@ghiChu` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMW
-- Create date: 2015-01-12
-- Description:	Insert Thuc chay da tinh mua ngoai by phanBoId
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_dev]
	@NgayThucHien						DATETIME,
	@ThucChayMuaNgoaiChiTietID			INT,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@SoLuongThucChay					INT,
	@ThanhTienThucChayBanSauCK			FLOAT,
	@DonViTinhThucChay					NVARCHAR(50),
	@ghiChu								NVARCHAR(512)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	SET @ThanhTienThucChayBanSauCK = ISNULL(@ThanhTienThucChayBanSauCK,0)

    --INSERT INTO dbo.ThucChayDaTinh
    --(
    --    ThucChayDaTinhID,
    --    HopDongID,
    --    SoHopDong,
    --    DmMaHopDongREF,
    --    TenMaHopDong,
    --    NgayDanhSoHopDong,
    --    NgayKyHopDong,
    --    NhanHopDong,
    --    NgayNhanBanFax,
    --    NgayNhanHopDongBanCung,
    --    NgayChuyenHopDongChoKeToan,
    --    So,
    --    Thang,
    --    Nam,
    --    GiaTriHopDong,
    --    CongNo,
    --    HopDongChiTietREF,
    --    DangSuDung,
    --    IsGiayPhep,
    --    TrangThaiHopDong,
    --    IsBanCung,
    --    DmPhongBanREF,
    --    TenPhongBan,
    --    DmBoPhanREF,
    --    TenBoPhan,
    --    DmNhomLamViecREF,
    --    TenNhomLamViec,
    --    DmDiaDiemLamViecREF,
    --    TenDiaDiemLamViec,
    --    SysNhanVienREF,
    --    TenDangNhap,
    --    TenNhanVien,
    --    TenKhachHang,
    --    NhanHang,
    --    DmNhomNganhREF,
    --    TenNhomNganh,
    --    DmHinhThucQuangCao,
    --    TenHinhThucQuangCao,
    --    DmSanPhamREF,
    --    TenSanPham,
    --    DmNhomWebsiteREF,
    --    TenNhomWebsite,
    --    DmChuyenMucREF,
    --    TenChuyenMuc,
    --    DmLoaiBannerREF,
    --    TenLoaiBanner,
    --    DmViTriREF,
    --    TenViTri,
    --    DotChayHopDong,
    --    SoLuongDotChayHD,
    --    DotChayBooking,
    --    SoLuongDotChayBooking,
    --    SoLuong,
    --    DonViTinh,
    --    DonGia,
    --    DonGiaTheoDonVi,
    --    ChietKhau,
    --    GiamGia,
    --    ThanhTien,
    --    TiLeTuVan,
    --    ChiPhiTuVan,
    --    IsKhuyenMai,
    --    KhuyenMai,
    --    DmBannerREF,
    --    DmChienDichREF,
    --    DmWebsiteREF,
    --    TenWebsite,
    --    TongViewThucChay,
    --    TongClickThucChay,
    --    TongSoBaiViet,
    --    SoLuongThucChay,
    --    NgayThucHien,
    --    GiaTriThayDoi,
    --    ThanhTienThucChayTruocTrietKhau,
    --    GiaTriTrietKhauThucChay,
    --    ThanhTienSauTrietKhauThucChay,
    --    GiaTriHoaHongThucChay,
    --    ThanhTienThucThu,
    --    ThanhTienKM,
    --    SoLuongThucChayKM,
    --    SoLuongThucChayLechTreoHa,
    --    ThanhTienLechTreoHa,
    --    CreatedAt,
    --    LastModifiedAt,
    --    IsPheDuyet,
    --    PheDuyetBy,
    --    PheDuyetAt,
    --    SoLuongThayDoi,
    --    SoLuongKMThayDoi,
    --    GiaTriKMThayDoi,
    --    GhiChu
    --)
     SELECT DISTINCT
		NEWID() ThucChayDaTinhID,
		D.HopDongID, D.SoHopDong,D.DmMaHopDongREF,D.TenMaHopDong,D.NgayDanhSoHopDong, D.NgayKyHopDong, 
		D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
		D.So, D.Thang, D.Nam,D.GiaTriHopDong, D.CongNo,
		@HopDongChiTietREF AS HopDongChiTietREF,
		D.DangSuDung, D.IsGiayPhep, 
		2 AS TrangThaiHopDong,
		D.IsBanCung,D.DmPhongBanREF,ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
		D.DmBoPhanREF,ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
		D.DmNhomLamViecREF,ISNULL(D.TenNhom, '') AS TenNhom, 
		D.DmDiaDiemLamViecREF,D.TenDiaDiemLamViec, 
		D.SysNhanVienREF,ISNULL(D.TenDangNhap, '') AS TenDangNhap,D.TenNhanVien, 
		D.TenKhachHang, 
		C.DanhSachNhanHangREF NhanHang, 
		'' DmNhomNganhREF, 
		'' TenNhomNganh, 
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		C.DmSanPhamREF,C.TenSanPham,0 DmNhomWebsiteREF,'' TenNhomWebsite, 
		C.DmChuyenMucREF AS DmChuyenMucREF, 
		C.TenChuyenMuc AS TenChuyenMuc, 
		C.DmLoaiBannerREF AS DmLoaiBannerREF, 
		C.TenLoaiBanner AS TenLoaiBanner, 
		C.DmViTriREF AS DmViTriREF, 
		C.TenViTri AS TenViTri, 
		@GhiChu AS DotChayHopDong,
		0 AS SoLuongDotChayHD,
		@ThucChayMuaNgoaiChiTietID DotChayBooking,
		@ThucChayMuaNgoaiChiTietID SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		ISNULL(dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh(C.SoLuong,C.DonViTinh),0) AS SoLuong,
		--****haidh chinh sua
		@donViTinhThucChay AS DonViTinh, 
		dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,		
		--****haidh chinh sua
		dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh,
		C.ChietKhau ChietKhau, C.GiamGia GiamGia, C.ThanhTien ThanhTien,
		C.TiLeTuVan TiLeTuVan,  C.ChiPhiTuVan ChiPhiTuVan,
		C.IsKhuyenMai IsKhuyenMai,  
		C.KhuyenMai KhuyenMai,
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
		dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		(CASE WHEN C.ChietKhau <> 100 THEN @SoLuongThucChay
			ELSE 0
		END) as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@ngayThucHien NgayThucHien,
		0 as GiaTriThayDoi,
		--@chietKhauMuaNgoai as ChietKhauMuaNgoai,
		(CASE WHEN C.ChietKhau = 100 THEN @ThanhTienThucChayBanSauCK
			ELSE (@ThanhTienThucChayBanSauCK*100)/(100-C.ChietKhau)
		END) AS ThanhTienThucChayTruocTrietKhau,
		(CASE WHEN C.ChietKhau = 100 THEN @ThanhTienThucChayBanSauCK
			ELSE (@ThanhTienThucChayBanSauCK*C.ChietKhau)/100
		END) AS GiaTriTrietKhauThucChay,
		(CASE WHEN C.ChietKhau = 100 THEN 0
			ELSE @ThanhTienThucChayBanSauCK
		END)  ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		(CASE WHEN C.ChietKhau = 100 THEN 0
			ELSE @ThanhTienThucChayBanSauCK
		END) AS ThanhTienThucThu,
		(CASE WHEN C.ChietKhau = 100 THEN @ThanhTienThucChayBanSauCK
			ELSE 0
		END) as ThanhTienKM,
		(CASE WHEN C.ChietKhau = 100 THEN @SoLuongThucChay
			ELSE 0
		END) AS SoLuongThucChayKM,
		0 AS SoLuongLechTreoHa,
		0 AS ThanhTienLechTreoHa,
		GETDATE() AS CreatedAt,
		GETDATE() AS LastModifiedAt,
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 AS SoLuongThayDoi,
		0 AS SoLuongKMThayDoi,
		0 AS GiaTriKMThayDoi,
		@GhiChu AS GhiChu
	FROM (SELECT * FROM dbo.HopDong WHERE HopDongID = @HopDongREF)AS D 
	INNER JOIN 
	(SELECT * FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietREF)C ON C.HopDongFK = D.HopDongID
	
END

```
