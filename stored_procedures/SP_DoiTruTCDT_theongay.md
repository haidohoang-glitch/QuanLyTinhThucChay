# Stored Procedure: `DoiTruTCDT_theongay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-12-31 10:16:42.180000
- **Ngày sửa cuối**: 2025-12-31 10:30:28.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |
| `@NgayGhiNhan` | `date(3)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
CREATE  PROC [dbo].[DoiTruTCDT_theongay]
    @NgayThucHien  DATE,           -- ngày cần đối trừ (lọc dữ liệu)
    @NgayGhiNhan   DATE,           -- ngày ghi nhận bản ghi mới
    @HopDongID INT,
    @HopDongChiTietID INT,
    @DmSanPhamREF INT,
    @GhiChu NVARCHAR(500)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH Src AS (
        SELECT *
        FROM dbo.ThucChayDaTinh
        WHERE HopDongID = @HopDongID
          AND HopDongChiTietREF = CONVERT(varchar(50), @HopDongChiTietID)
          AND DmSanPhamREF = @DmSanPhamREF
          AND CONVERT(date, NgayThucHien) = @NgayThucHien
          -- chặn đối trừ trùng
          --AND (GhiChu IS NULL OR GhiChu NOT LIKE N'%Đối trừ%')
    )
    INSERT INTO dbo.ThucChayDaTinh (
        ThucChayDaTinhID,
        HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, NgayKyHopDong,
        NhanHopDong, NgayNhanBanFax, NgayNhanHopDongBanCung, NgayChuyenHopDongChoKeToan,
        So, Thang, Nam, GiaTriHopDong, CongNo, HopDongChiTietREF, DangSuDung, IsGiayPhep, TrangThaiHopDong,
        IsBanCung, DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomLamViecREF, TenNhomLamViec,
        DmDiaDiemLamViecREF, TenDiaDiemLamViec, SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang,
        DmNhomNganhREF, TenNhomNganh, DmHinhThucQuangCao, TenHinhThucQuangCao, DmSanPhamREF, TenSanPham,
        DmNhomWebsiteREF, TenNhomWebsite, DmChuyenMucREF, TenChuyenMuc, DmLoaiBannerREF, TenLoaiBanner,
        DmViTriREF, TenViTri, DotChayHopDong, SoLuongDotChayHD, DotChayBooking, SoLuongDotChayBooking,
        SoLuong, DonViTinh, DonGia, DonGiaTheoDonVi, ChietKhau, GiamGia, ThanhTien, TiLeTuVan, ChiPhiTuVan,
        IsKhuyenMai, KhuyenMai, DmBannerREF, DmChienDichREF, DmWebsiteREF, TenWebsite,
        TongViewThucChay, TongClickThucChay, TongSoBaiViet, SoLuongThucChay,
        NgayThucHien,
        GiaTriThayDoi, ThanhTienThucChayTruocTrietKhau, GiaTriTrietKhauThucChay,
        ThanhTienSauTrietKhauThucChay, GiaTriHoaHongThucChay, ThanhTienThucThu,
        ThanhTienKM, SoLuongThucChayKM, SoLuongThucChayLechTreoHa,
        ThanhTienLechTreoHa, CreatedAt, LastModifiedAt,
        IsPheDuyet, PheDuyetBy, PheDuyetAt,
        SoLuongThayDoi, SoLuongKMThayDoi, GiaTriKMThayDoi, GhiChu
    )
    SELECT
        NEWID(),
        HopDongID, SoHopDong, DmMaHopDongREF, TenMaHopDong, NgayDanhSoHopDong, NgayKyHopDong,
        NhanHopDong, NgayNhanBanFax, NgayNhanHopDongBanCung, NgayChuyenHopDongChoKeToan,
        So, Thang, Nam, GiaTriHopDong, CongNo, HopDongChiTietREF, DangSuDung, IsGiayPhep, TrangThaiHopDong,
        IsBanCung, DmPhongBanREF, TenPhongBan, DmBoPhanREF, TenBoPhan, DmNhomLamViecREF, TenNhomLamViec,
        DmDiaDiemLamViecREF, TenDiaDiemLamViec, SysNhanVienREF, TenDangNhap, TenNhanVien, TenKhachHang, NhanHang,
        DmNhomNganhREF, TenNhomNganh, DmHinhThucQuangCao, TenHinhThucQuangCao, DmSanPhamREF, TenSanPham,
        DmNhomWebsiteREF, TenNhomWebsite, DmChuyenMucREF, TenChuyenMuc, DmLoaiBannerREF, TenLoaiBanner,
        DmViTriREF, TenViTri, DotChayHopDong, SoLuongDotChayHD, DotChayBooking, SoLuongDotChayBooking,
        SoLuong, DonViTinh, DonGia, DonGiaTheoDonVi, ChietKhau, GiamGia, ThanhTien, TiLeTuVan, ChiPhiTuVan,
        IsKhuyenMai, KhuyenMai, DmBannerREF, DmChienDichREF, DmWebsiteREF, TenWebsite,

        0, 0, 0,
        -ISNULL(SoLuongThucChay,0),

        -- 🔴 NGÀY GHI NHẬN MỚI
        @NgayGhiNhan,

        -ISNULL(GiaTriThayDoi,0),
        -ISNULL(ThanhTienThucChayTruocTrietKhau,0),
        -ISNULL(GiaTriTrietKhauThucChay,0),
        -ISNULL(ThanhTienSauTrietKhauThucChay,0),
        -ISNULL(GiaTriHoaHongThucChay,0),
        -ISNULL(ThanhTienThucThu,0),
        -ISNULL(ThanhTienKM,0),
        -ISNULL(SoLuongThucChayKM,0),
        -ISNULL(SoLuongThucChayLechTreoHa,0),
        -ISNULL(ThanhTienLechTreoHa,0),

        GETDATE(), GETDATE(),
        0, 0, 0,

        -ISNULL(SoLuongThayDoi,0),
        -ISNULL(SoLuongKMThayDoi,0),
        -ISNULL(GiaTriKMThayDoi,0),

        @GhiChu
    FROM Src;
END

```
