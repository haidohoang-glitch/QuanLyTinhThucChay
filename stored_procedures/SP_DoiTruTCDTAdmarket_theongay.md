# Stored Procedure: `DoiTruTCDTAdmarket_theongay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-12-31 10:51:09.283000
- **Ngày sửa cuối**: 2025-12-31 11:39:42.290000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |
| `@NgayGhiNhan` | `date(3)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[DoiTruTCDTAdmarket_theongay]
    @NgayThucHien      DATE,          -- ngày phát sinh gốc
    @NgayGhiNhan       DATE,          -- ngày ghi nhận bản ghi đối trừ
    @HopDongID         INT,
    @HopDongChiTietID  NVARCHAR(50),
    @DmSanPhamREF      INT,
    @GhiChu            NVARCHAR(200)
AS
BEGIN
    SET NOCOUNT ON;
	/*
        DoiTruTCDTAdmarket_theongay
        Tác giả: Nhung
        Mục đích: Đối trừ 1-1 theo ngày phát sinh, ghi nhận vào ngày khác
        Ngày tạo: 2025-12-31
        Ghi chú: Mỗi bản ghi nguồn -> tạo 1 bản ghi đối trừ (đảo âm các số liệu)
    */

    ;WITH Src AS (
        SELECT *
        FROM dbo.ThucChayDaTinhAdmarket
        WHERE HopDongID = @HopDongID
          AND HopDongChiTietREF = @HopDongChiTietID
          AND DmSanPhamREF = @DmSanPhamREF
          AND CONVERT(date, NgayThucHien) = @NgayThucHien
    )
    INSERT INTO dbo.ThucChayDaTinhAdmarket
    (
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
        ThanhTienLechTreoHa,
        CreatedAt, LastModifiedAt,
        IsPheDuyet, PheDuyetBy, PheDuyetAt,
        SoLuongThayDoi, SoLuongKMThayDoi, GiaTriKMThayDoi,
        GhiChu
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
        -ISNULL(SoLuongThucChay, 0),

        -- 🔴 ngày ghi nhận mới
        @NgayGhiNhan,

        -- 🔴 đảo âm
        -ISNULL(GiaTriThayDoi, 0),
        -ISNULL(ThanhTienThucChayTruocTrietKhau, 0),
        -ISNULL(GiaTriTrietKhauThucChay, 0),
        -ISNULL(ThanhTienSauTrietKhauThucChay, 0),
        -ISNULL(GiaTriHoaHongThucChay, 0),
        -ISNULL(ThanhTienThucThu, 0),
        -ISNULL(ThanhTienKM, 0),
        -ISNULL(SoLuongThucChayKM, 0),
        -ISNULL(SoLuongThucChayLechTreoHa, 0),
        -ISNULL(ThanhTienLechTreoHa, 0),

        GETDATE(), GETDATE(),
        0, 0, 0,

        -ISNULL(SoLuongThayDoi, 0),
        -ISNULL(SoLuongKMThayDoi, 0),
        -ISNULL(GiaTriKMThayDoi, 0),

        @GhiChu
    FROM Src;

    -- 👀 nhìn thấy ngay có insert hay không
    SELECT @@ROWCOUNT AS SoDongDaInsert;
END

```
