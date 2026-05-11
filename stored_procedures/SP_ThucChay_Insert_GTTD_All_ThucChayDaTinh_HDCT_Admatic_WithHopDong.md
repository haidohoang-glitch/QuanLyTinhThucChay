# Stored Procedure: `ThucChay_Insert_GTTD_All_ThucChayDaTinh_HDCT_Admatic_WithHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-02-20 09:36:06.337000
- **Ngày sửa cuối**: 2019-02-20 09:36:06.337000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_HDCT_Admatic_WithHopDong] 
	@FromDate DATETIME,
	@ToDate DATETIME,
	@NgayGhiNhanThucChay DATETIME,
	@HopDongID INT, 
	@HopDongChiTietID INT,
	@GhiChu NVARCHAR(1000)
AS
BEGIN
	DECLARE @Note NVARCHAR(500) = @GhiChu

	--CHI THUC HIEN DOI TRU HOP DONG CHI TIET BI HUY
	INSERT INTO dbo.ThucChayDaTinh
	        ( ThucChayDaTinhID ,
	          HopDongID ,
	          SoHopDong ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          NgayDanhSoHopDong ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          NgayNhanBanFax ,
	          NgayNhanHopDongBanCung ,
	          NgayChuyenHopDongChoKeToan ,
	          So ,
	          Thang ,
	          Nam ,
	          GiaTriHopDong ,
	          CongNo ,
	          HopDongChiTietREF ,
	          DangSuDung ,
	          IsGiayPhep ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhomLamViec ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          TenKhachHang ,
	          NhanHang ,
	          DmNhomNganhREF ,
	          TenNhomNganh ,
	          DmHinhThucQuangCao ,
	          TenHinhThucQuangCao ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          DmNhomWebsiteREF ,
	          TenNhomWebsite ,
	          DmChuyenMucREF ,
	          TenChuyenMuc ,
	          DmLoaiBannerREF ,
	          TenLoaiBanner ,
	          DmViTriREF ,
	          TenViTri ,
	          DotChayHopDong ,
	          SoLuongDotChayHD ,
	          DotChayBooking ,
	          SoLuongDotChayBooking ,
	          SoLuong ,
	          DonViTinh ,
	          DonGia ,
	          DonGiaTheoDonVi ,
	          ChietKhau ,
	          GiamGia ,
	          ThanhTien ,
	          TiLeTuVan ,
	          ChiPhiTuVan ,
	          IsKhuyenMai ,
	          KhuyenMai ,
	          DmBannerREF ,
	          DmChienDichREF ,
	          DmWebsiteREF ,
	          TenWebsite ,
	          TongViewThucChay ,
	          TongClickThucChay ,
	          TongSoBaiViet ,
	          SoLuongThucChay ,
	          NgayThucHien ,
	          GiaTriThayDoi ,
	          ThanhTienThucChayTruocTrietKhau ,
	          GiaTriTrietKhauThucChay ,
	          ThanhTienSauTrietKhauThucChay ,
	          GiaTriHoaHongThucChay ,
	          ThanhTienThucThu ,
	          ThanhTienKM ,
	          SoLuongThucChayKM ,
	          SoLuongThucChayLechTreoHa ,
	          ThanhTienLechTreoHa ,
	          CreatedAt ,
	          LastModifiedAt ,
	          IsPheDuyet ,
	          PheDuyetBy ,
	          PheDuyetAt ,
	          SoLuongThayDoi ,
	          SoLuongKMThayDoi ,
	          GiaTriKMThayDoi ,
	          GhiChu
	        )
	SELECT  NEWID() ThucChayDaTinhID ,
	          HopDongID ,
	          SoHopDong ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          NgayDanhSoHopDong ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          NgayNhanBanFax ,
	          NgayNhanHopDongBanCung ,
	          NgayChuyenHopDongChoKeToan ,
	          So ,
	          Thang ,
	          Nam ,
	          GiaTriHopDong ,
	          CongNo ,
	          HopDongChiTietREF ,
	          DangSuDung ,
	          IsGiayPhep ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhomLamViec ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          TenKhachHang ,
	          NhanHang ,
	          DmNhomNganhREF ,
	          TenNhomNganh ,
	          DmHinhThucQuangCao ,
	          TenHinhThucQuangCao ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          DmNhomWebsiteREF ,
	          TenNhomWebsite ,
	          DmChuyenMucREF ,
	          TenChuyenMuc ,
	          DmLoaiBannerREF ,
	          TenLoaiBanner ,
	          DmViTriREF ,
	          TenViTri ,
	          '' AS DotChayHopDong ,
	          0 AS SoLuongDotChayHD ,
	          '' AS DotChayBooking ,
	          0 AS SoLuongDotChayBooking ,
	          SoLuong ,
	          DonViTinh ,
	          DonGia ,
	          DonGiaTheoDonVi ,
	          ChietKhau ,
	          GiamGia ,
	          ThanhTien ,
	          TiLeTuVan ,
	          ChiPhiTuVan ,
	          IsKhuyenMai ,
	          KhuyenMai ,
	          DmBannerREF ,
	          DmChienDichREF ,
	          DmWebsiteREF ,
	          TenWebsite ,
	          - SUM(TongViewThucChay) TongViewThucChay,
	          - SUM(TongClickThucChay) TongClickThucChay ,
	          0 TongSoBaiViet ,
	          0 SoLuongThucChay ,
	          NgayThucHien ,
	          -SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) GiaTriThayDoi ,
	          0 ThanhTienThucChayTruocTrietKhau ,
	          0 GiaTriTrietKhauThucChay ,
	          0 ThanhTienSauTrietKhauThucChay ,
	          0 GiaTriHoaHongThucChay ,
	          0 ThanhTienThucThu ,
	          0 ThanhTienKM ,
	          0 SoLuongThucChayKM ,
	          - SUM(tcdt.SoLuongThucChayLechTreoHa) SoLuongThucChayLechTreoHa ,
	          - SUM(tcdt.ThanhTienLechTreoHa) ThanhTienLechTreoHa ,
	          GETDATE() CreatedAt ,
	          GETDATE() LastModifiedAt ,
	          0 IsPheDuyet ,
	          '' PheDuyetBy ,
	          NULL PheDuyetAt ,
	          - SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) SoLuongThayDoi ,
	          - SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) SoLuongKMThayDoi ,
	          - SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) GiaTriKMThayDoi ,
	          @Note GhiChu
	        FROM dbo.ThucChayDaTinh tcdt
			WHERE 1=1
			AND tcdt.HopDongID = @HopDongID
			AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND DmHinhThucQuangCao = 42 --Admatic
			AND tcdt.NgayThucHien BETWEEN @FromDate AND @ToDate
			AND DmSanPhamREF NOT IN  (736,817) -- chi phí công nghệ, chi phi marketing fee
			GROUP BY  HopDongID ,
	          SoHopDong ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          NgayDanhSoHopDong ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          NgayNhanBanFax ,
	          NgayNhanHopDongBanCung ,
	          NgayChuyenHopDongChoKeToan ,
	          So ,
	          Thang ,
	          Nam ,
	          GiaTriHopDong ,
	          CongNo ,
	          HopDongChiTietREF ,
	          DangSuDung ,
	          IsGiayPhep ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhomLamViec ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          TenKhachHang ,
	          NhanHang ,
	          DmNhomNganhREF ,
	          TenNhomNganh ,
	          DmHinhThucQuangCao ,
	          TenHinhThucQuangCao ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          DmNhomWebsiteREF ,
	          TenNhomWebsite ,
	          DmChuyenMucREF ,
	          TenChuyenMuc ,
	          DmLoaiBannerREF ,
	          TenLoaiBanner ,
	          DmViTriREF ,
	          TenViTri ,
	          SoLuong ,
	          DonViTinh ,
	          DonGia ,
	          DonGiaTheoDonVi ,
	          ChietKhau ,
	          GiamGia ,
	          ThanhTien ,
	          TiLeTuVan ,
	          ChiPhiTuVan ,
	          IsKhuyenMai ,
	          KhuyenMai ,
	          DmBannerREF ,
	          DmChienDichREF ,
	          DmWebsiteREF ,
	          TenWebsite ,
	          NgayThucHien 

	--THUC HIEN DOI TRU VOI TRUONG HOP LA SAN PHAM ADX
	INSERT INTO dbo.ThucChayDaTinhAdmarket
	(
	    ThucChayDaTinhID,
	    HopDongID,
	    SoHopDong,
	    DmMaHopDongREF,
	    TenMaHopDong,
	    NgayDanhSoHopDong,
	    NgayKyHopDong,
	    NhanHopDong,
	    NgayNhanBanFax,
	    NgayNhanHopDongBanCung,
	    NgayChuyenHopDongChoKeToan,
	    So,
	    Thang,
	    Nam,
	    GiaTriHopDong,
	    CongNo,
	    HopDongChiTietREF,
	    DangSuDung,
	    IsGiayPhep,
	    TrangThaiHopDong,
	    IsBanCung,
	    DmPhongBanREF,
	    TenPhongBan,
	    DmBoPhanREF,
	    TenBoPhan,
	    DmNhomLamViecREF,
	    TenNhomLamViec,
	    DmDiaDiemLamViecREF,
	    TenDiaDiemLamViec,
	    SysNhanVienREF,
	    TenDangNhap,
	    TenNhanVien,
	    TenKhachHang,
	    NhanHang,
	    DmNhomNganhREF,
	    TenNhomNganh,
	    DmHinhThucQuangCao,
	    TenHinhThucQuangCao,
	    DmSanPhamREF,
	    TenSanPham,
	    DmNhomWebsiteREF,
	    TenNhomWebsite,
	    DmChuyenMucREF,
	    TenChuyenMuc,
	    DmLoaiBannerREF,
	    TenLoaiBanner,
	    DmViTriREF,
	    TenViTri,
	    DotChayHopDong,
	    SoLuongDotChayHD,
	    DotChayBooking,
	    SoLuongDotChayBooking,
	    SoLuong,
	    DonViTinh,
	    DonGia,
	    DonGiaTheoDonVi,
	    ChietKhau,
	    GiamGia,
	    ThanhTien,
	    TiLeTuVan,
	    ChiPhiTuVan,
	    IsKhuyenMai,
	    KhuyenMai,
	    DmBannerREF,
	    DmChienDichREF,
	    DmWebsiteREF,
	    TenWebsite,
	    TongViewThucChay,
	    TongClickThucChay,
	    TongSoBaiViet,
	    SoLuongThucChay,
	    NgayThucHien,
	    GiaTriThayDoi,
	    ThanhTienThucChayTruocTrietKhau,
	    GiaTriTrietKhauThucChay,
	    ThanhTienSauTrietKhauThucChay,
	    GiaTriHoaHongThucChay,
	    ThanhTienThucThu,
	    ThanhTienKM,
	    SoLuongThucChayKM,
	    SoLuongThucChayLechTreoHa,
	    ThanhTienLechTreoHa,
	    CreatedAt,
	    LastModifiedAt,
	    IsPheDuyet,
	    PheDuyetBy,
	    PheDuyetAt,
	    SoLuongThayDoi,
	    SoLuongKMThayDoi,
	    GiaTriKMThayDoi,
	    GhiChu
	)
	
	SELECT  NEWID() ThucChayDaTinhID ,
	          HopDongID ,
	          SoHopDong ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          NgayDanhSoHopDong ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          NgayNhanBanFax ,
	          NgayNhanHopDongBanCung ,
	          NgayChuyenHopDongChoKeToan ,
	          So ,
	          Thang ,
	          Nam ,
	          GiaTriHopDong ,
	          CongNo ,
	          HopDongChiTietREF ,
	          DangSuDung ,
	          IsGiayPhep ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhomLamViec ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          TenKhachHang ,
	          NhanHang ,
	          DmNhomNganhREF ,
	          TenNhomNganh ,
	          DmHinhThucQuangCao ,
	          TenHinhThucQuangCao ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          DmNhomWebsiteREF ,
	          TenNhomWebsite ,
	          DmChuyenMucREF ,
	          TenChuyenMuc ,
	          DmLoaiBannerREF ,
	          TenLoaiBanner ,
	          DmViTriREF ,
	          TenViTri ,
	          '' AS DotChayHopDong ,
	          0 AS SoLuongDotChayHD ,
	          '' AS DotChayBooking ,
	          0 AS SoLuongDotChayBooking ,
	          SoLuong ,
	          DonViTinh ,
	          DonGia ,
	          DonGiaTheoDonVi ,
	          ChietKhau ,
	          GiamGia ,
	          ThanhTien ,
	          TiLeTuVan ,
	          ChiPhiTuVan ,
	          IsKhuyenMai ,
	          KhuyenMai ,
	          DmBannerREF ,
	          DmChienDichREF ,
	          DmWebsiteREF ,
	          TenWebsite ,
	          0 TongViewThucChay ,
	          0 TongClickThucChay ,
	          0 TongSoBaiViet ,
	          0 SoLuongThucChay ,
	          NgayThucHien ,
	          -SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) GiaTriThayDoi ,
	          0 ThanhTienThucChayTruocTrietKhau ,
	          0 GiaTriTrietKhauThucChay ,
	          0 ThanhTienSauTrietKhauThucChay ,
	          0 GiaTriHoaHongThucChay ,
	          0 ThanhTienThucThu ,
	          0 ThanhTienKM ,
	          0 SoLuongThucChayKM ,
	          - SUM(tcdt.SoLuongThucChayLechTreoHa) SoLuongThucChayLechTreoHa ,
	          - SUM(tcdt.ThanhTienLechTreoHa) ThanhTienLechTreoHa ,
	          GETDATE() CreatedAt ,
	          GETDATE() LastModifiedAt ,
	          0 IsPheDuyet ,
	          '' PheDuyetBy ,
	          NULL PheDuyetAt ,
	          - SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) SoLuongThayDoi ,
	          - SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) SoLuongKMThayDoi ,
	          - SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) GiaTriKMThayDoi ,
	          @Note GhiChu
	        FROM dbo.ThucChayDaTinhAdmarket tcdt
			WHERE 1=1
			AND tcdt.HopDongID = @HopDongID
			AND tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND tcdt.DmHinhThucQuangCao = 42
			AND tcdt.NgayThucHien BETWEEN @FromDate AND @ToDate
			AND tcdt.DmSanPhamREF = 585
			GROUP BY 
			  HopDongID,
			  SoHopDong ,
	          DmMaHopDongREF ,
	          TenMaHopDong ,
	          NgayDanhSoHopDong ,
	          NgayKyHopDong ,
	          NhanHopDong ,
	          NgayNhanBanFax ,
	          NgayNhanHopDongBanCung ,
	          NgayChuyenHopDongChoKeToan ,
	          So ,
	          Thang ,
	          Nam ,
	          GiaTriHopDong ,
	          CongNo ,
	          HopDongChiTietREF ,
	          DangSuDung ,
	          IsGiayPhep ,
	          TrangThaiHopDong ,
	          IsBanCung ,
	          DmPhongBanREF ,
	          TenPhongBan ,
	          DmBoPhanREF ,
	          TenBoPhan ,
	          DmNhomLamViecREF ,
	          TenNhomLamViec ,
	          DmDiaDiemLamViecREF ,
	          TenDiaDiemLamViec ,
	          SysNhanVienREF ,
	          TenDangNhap ,
	          TenNhanVien ,
	          TenKhachHang ,
	          NhanHang ,
	          DmNhomNganhREF ,
	          TenNhomNganh ,
	          DmHinhThucQuangCao ,
	          TenHinhThucQuangCao ,
	          DmSanPhamREF ,
	          TenSanPham ,
	          DmNhomWebsiteREF ,
	          TenNhomWebsite ,
	          DmChuyenMucREF ,
	          TenChuyenMuc ,
	          DmLoaiBannerREF ,
	          TenLoaiBanner ,
	          DmViTriREF ,
	          TenViTri ,
	          SoLuong ,
	          DonViTinh ,
	          DonGia ,
	          DonGiaTheoDonVi ,
	          ChietKhau ,
	          GiamGia ,
	          ThanhTien ,
	          TiLeTuVan ,
	          ChiPhiTuVan ,
	          IsKhuyenMai ,
	          KhuyenMai ,
	          DmBannerREF ,
	          DmChienDichREF ,
	          DmWebsiteREF ,
	          TenWebsite ,
	          NgayThucHien 
END



```
