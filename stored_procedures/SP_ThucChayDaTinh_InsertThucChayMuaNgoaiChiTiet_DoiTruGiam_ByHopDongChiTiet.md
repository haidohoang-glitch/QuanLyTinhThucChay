# Stored Procedure: `ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_DoiTruGiam_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-05-17 11:40:29.467000
- **Ngày sửa cuối**: 2020-01-14 10:17:13.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@ghiChu` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMW
-- Create date: 2015-01-12
-- Description:	Insert Thuc chay da tinh mua ngoai by phanBoId
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_InsertThucChayMuaNgoaiChiTiet_DoiTruGiam_ByHopDongChiTiet]
	@NgayThucHien						DATETIME,
	@HopDongChiTietREF					INT,
	@ghiChu								NVARCHAR(512)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @MaxNgayThucHien DATETIME
	SET @MaxNgayThucHien = ISNULL((SELECT MAX(NgayThucHien) AS NgayThucHien
		FROM dbo.ThucChayDaTinh
		WHERE  1=1 		
		AND  HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien  < @NgayThucHien
	),'1900-01-01')
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
   
     SELECT NEWID() ,
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
        0 AS TongViewThucChay,
        0 AS TongClickThucChay,
        0 AS TongSoBaiViet,
        0 AS SoLuongThucChay,
        @NgayThucHien AS NgayThucHien,
        -(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi,
        0 AS ThanhTienThucChayTruocTrietKhau,
        0 AS GiaTriTrietKhauThucChay,
        0 AS ThanhTienSauTrietKhauThucChay,
        0 AS GiaTriHoaHongThucChay,
        -(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienThucThu,
        0 AS ThanhTienKM,
        0 AS SoLuongThucChayKM,
        0 AS SoLuongThucChayLechTreoHa,
        0 AS ThanhTienLechTreoHa,
        GETDATE() AS CreatedAt,
        GETDATE() AS LastModifiedAt,
        0 AS IsPheDuyet,
        PheDuyetBy,
        PheDuyetAt,
        -(SoLuongThucChay +SoLuongThayDoi) AS SoLuongThayDoi,
        -(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi,
        -(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi,
        @ghiChu AS GhiChu FROM dbo.ThucChayDaTinh
		WHERE  1=1 		
		AND  HopDongChiTietREF = @HopDongChiTietREF
		AND NgayThucHien  < @NgayThucHien
		AND ((ThanhTienKM + GiaTriKMThayDoi) <> 0 OR (ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) <> 0)
	
	
END

```
