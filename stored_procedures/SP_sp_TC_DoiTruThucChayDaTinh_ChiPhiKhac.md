# Stored Procedure: `sp_TC_DoiTruThucChayDaTinh_ChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-30 09:37:00.843000
- **Ngày sửa cuối**: 2019-05-31 15:28:38.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


/*
EXEC [dbo].[sp_TC_DoiTruThucChayDaTinh_ChiPhiKhac]
    @HopDongID INT,
	@HopDongChiTietID INT ,
    @NgaythucHien DATETIME ,
	@GhiChu NVARCHAR(500)
*/

CREATE PROCEDURE [dbo].[sp_TC_DoiTruThucChayDaTinh_ChiPhiKhac]
    @HopDongID INT,
	@HopDongChiTietID INT ,
    @NgaythucHien DATETIME ,
	@GhiChu NVARCHAR(500)
AS
BEGIN
	INSERT INTO dbo.ThucChayDaTinh
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
	
	SELECT NEWID() ThucChayDaTinhID,
           tcdt.HopDongID,
           tcdt.SoHopDong,
           tcdt.DmMaHopDongREF,
           tcdt.TenMaHopDong,
           tcdt.NgayDanhSoHopDong,
           tcdt.NgayKyHopDong,
           tcdt.NhanHopDong,
           tcdt.NgayNhanBanFax,
           tcdt.NgayNhanHopDongBanCung,
           tcdt.NgayChuyenHopDongChoKeToan,
           tcdt.So,
           tcdt.Thang,
           tcdt.Nam,
           tcdt.GiaTriHopDong,
           tcdt.CongNo,
           tcdt.HopDongChiTietREF,
           tcdt.DangSuDung,
           tcdt.IsGiayPhep,
           tcdt.TrangThaiHopDong,
           tcdt.IsBanCung,
           tcdt.DmPhongBanREF,
           tcdt.TenPhongBan,
           tcdt.DmBoPhanREF,
           tcdt.TenBoPhan,
           tcdt.DmNhomLamViecREF,
           tcdt.TenNhomLamViec,
           tcdt.DmDiaDiemLamViecREF,
           tcdt.TenDiaDiemLamViec,
           tcdt.SysNhanVienREF,
           tcdt.TenDangNhap,
           tcdt.TenNhanVien,
           tcdt.TenKhachHang,
           tcdt.NhanHang,
           tcdt.DmNhomNganhREF,
           tcdt.TenNhomNganh,
           tcdt.DmHinhThucQuangCao,
           tcdt.TenHinhThucQuangCao,
           tcdt.DmSanPhamREF,
           tcdt.TenSanPham,
           tcdt.DmNhomWebsiteREF,
           tcdt.TenNhomWebsite,
           tcdt.DmChuyenMucREF,
           tcdt.TenChuyenMuc,
           tcdt.DmLoaiBannerREF,
           tcdt.TenLoaiBanner,
           tcdt.DmViTriREF,
           tcdt.TenViTri,
           'DOI TRU TOAN BO CUA THUC TREO :' + tcdt.DotChayBooking AS DotChayHopDong,
           tcdt.SoLuongDotChayHD,
           tcdt.DotChayBooking,
           tcdt.SoLuongDotChayBooking,
           tcdt.SoLuong,
           tcdt.DonViTinh,
           tcdt.DonGia,
           tcdt.DonGiaTheoDonVi,
           tcdt.ChietKhau,
           tcdt.GiamGia,
           tcdt.ThanhTien,
           tcdt.TiLeTuVan,
           tcdt.ChiPhiTuVan,
           tcdt.IsKhuyenMai,
           tcdt.KhuyenMai,
           tcdt.DmBannerREF,
           tcdt.DmChienDichREF,
           tcdt.DmWebsiteREF,
           tcdt.TenWebsite,
           tcdt.TongViewThucChay,
           tcdt.TongClickThucChay,
           tcdt.TongSoBaiViet,
           0 AS SoLuongThucChay,
           @NgaythucHien AS NgayThucHien,
           -(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS GiaTriThayDoi,
           0 AS ThanhTienThucChayTruocTrietKhau,
           0 AS GiaTriTrietKhauThucChay,
           0 AS ThanhTienSauTrietKhauThucChay,
           0 AS GiaTriHoaHongThucChay,
           -(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhTienThucThu,
           0 AS ThanhTienKM,
           0 AS SoLuongThucChayKM,
           0 AS SoLuongThucChayLechTreoHa,
           0 AS ThanhTienLechTreoHa,
           GETDATE() AS CreatedAt,
           GETDATE() AS LastModifiedAt,
           0 AS IsPheDuyet,
           '' AS PheDuyetBy,
           GETDATE() AS PheDuyetAt,
           -(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuongThayDoi,
           -(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS SoLuongKMThayDoi,
           -(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS GiaTriKMThayDoi,
           @GhiChu AS ghiChu 
		   FROM dbo.ThucChayDaTinh tcdt
		   WHERE tcdt.HopDongID = @HopDongID
		   AND tcdt.HopDongChiTietREF = @HopDongChiTietID
END
       



```
