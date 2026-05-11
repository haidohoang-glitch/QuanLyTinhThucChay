# Stored Procedure: `ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_ORDER_ThanhTien_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-10-08 15:58:46.773000
- **Ngày sửa cuối**: 2022-06-03 15:56:00.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@Operating_Order_Id` | `int(4)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
[dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_ORDER_ThanhTien_GGFB] 
	@NgayGhiNhanThucChay DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT,
	@Operating_Order_Id INT,
	@DmSanPhamREF INT,
	@GhiChu NVARCHAR(1000)
*/


CREATE  PROCEDURE [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_By_ORDER_ThanhTien_GGFB] 
	@NgayGhiNhanThucChay DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT,
	@Operating_Order_Id INT,
	@GhiChu NVARCHAR(1000)
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
		SELECT NEWID() AS ThucChayDaTinhID,
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
		    0 SoLuongDotChayHD,
		    DotChayBooking ,
		    SoLuongDotChayBooking ,
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
		    0 TongViewThucChay,
		    0 TongClickThucChay,
		    0 TongSoBaiViet,
		    0 AS SoLuongThucChay,
		    @NgayGhiNhanThucChay AS NgayThucHien,
		    -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi,
		    0 AS ThanhTienThucChayTruocTrietKhau,
		    0 AS GiaTriTrietKhauThucChay,
		    0 AS ThanhTienSauTrietKhauThucChay,
		    0 AS GiaTriHoaHongThucChay,
		    0 AS ThanhTienThucThu,
		    0 AS ThanhTienKM,
		    0 AS SoLuongThucChayKM,
		    -SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa,
		    -SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa,
		    GETDATE() CreatedAt,
		    GETDATE() LastModifiedAt,
		    0 IsPheDuyet,
		    '' PheDuyetBy,
		    '' PheDuyetAt,
		    -SUM(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi,
		    -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi,
		    -SUM(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi,
		    @GhiChu GhiChu 
			FROM dbo.ThucChayDaTinh
			WHERE HopDongID = @HopDongID
			AND HopDongChiTietREF = @HopDongChiTietID
			AND not (DmHinhThucQuangCao IN(13) OR DmLoaiBannerREF IN (18))
			AND (DmSanPhamREF in (306,423,5160,5188,772)  OR DmViTriREF in (100093,100478,100774))
			AND DmSanPhamREF <> 585 --khac san pham Adx
			AND DmChienDichREF = @Operating_Order_Id --DOI TRU CUA GGFB TINH THEO SOLUONG THUC TE VA THEO SAN LUONG CHOT
			AND NgayThucHien <= @NgayGhiNhanThucChay
			GROUP BY
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
			DotChayBooking ,
		    SoLuongDotChayBooking ,
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
		    TenWebsite
			HAVING (SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) <> 0 
					OR SUM(ThanhTienKM + GiaTriKMThayDoi) <> 0
					OR SUM(ThanhTienLechTreoHa) <> 0)
	
END

```
