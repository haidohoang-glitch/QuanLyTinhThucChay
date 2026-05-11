# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTietLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-09 15:34:24.080000
- **Ngày sửa cuối**: 2017-04-05 14:27:55.227000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietLogID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@DanhSachNhanHangREF` | `nvarchar(400)` | No |
| `@NhanHang` | `nvarchar(400)` | No |
| `@DmNhomNganhREF` | `nvarchar(400)` | No |
| `@TenNhomNganh` | `nvarchar(400)` | No |
| `@DmLoaiREF` | `bigint(8)` | No |
| `@TenLoai` | `nvarchar(400)` | No |
| `@DmNhomWebsiteREF` | `nvarchar(400)` | No |
| `@TenNhomWebsite` | `nvarchar(400)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@DmLoaiBannerREF` | `int(4)` | No |
| `@TenLoaiBanner` | `nvarchar(400)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@TenChuyenMuc` | `nvarchar(400)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@TenBanner` | `nvarchar(400)` | No |
| `@ThoiGian` | `nvarchar(400)` | No |
| `@SoLuong` | `bigint(8)` | No |
| `@DonViTinhREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(400)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `int(4)` | No |
| `@GiamGia` | `float(8)` | No |
| `@TiLeTuVan` | `int(4)` | No |
| `@KhuyenMai` | `nvarchar(400)` | No |
| `@IsKhuyenMai` | `int(4)` | No |
| `@ChiPhiTuVan` | `float(8)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@DmSanphamREF_old` | `bigint(8)` | No |
| `@TK_AdMarket` | `nvarchar(400)` | No |
| `@TK_AdMarketID` | `int(4)` | No |
| `@SoLuongThucChay` | `float(8)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@TrangThaiThucChay` | `int(4)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@ThucChayDenNgay` | `datetime(8)` | No |
| `@ThoiGianLog` | `datetime(8)` | No |
| `@NguoiLog` | `nvarchar(400)` | No |
| `@LoaiLog` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTietLog]
	@HopDongChiTietLogID INT ,
	@HopDongChiTietREF INT ,
	@HopDongFK INT ,
	@DanhSachNhanHangREF NVARCHAR(200) ,
	@NhanHang NVARCHAR(200) ,
	@DmNhomNganhREF NVARCHAR(200) ,
	@TenNhomNganh NVARCHAR(200) ,
	@DmLoaiREF BIGINT ,
	@TenLoai NVARCHAR(200) ,
	@DmNhomWebsiteREF NVARCHAR(200) ,
	@TenNhomWebsite NVARCHAR(200) ,
	@DmWebsiteREF INT ,
	@TenWebsite NVARCHAR(200) ,
	@DmSanPhamREF INT ,
	@TenSanPham NVARCHAR(200) ,
	@DmLoaiBannerREF INT ,
	@TenLoaiBanner NVARCHAR(200) ,
	@DmChuyenMucREF INT ,
	@TenChuyenMuc NVARCHAR(200) ,
	@DmBannerREF INT ,
	@TenBanner NVARCHAR(200) ,
	@ThoiGian NVARCHAR(200) ,
	@SoLuong BIGINT ,
	@DonViTinhREF INT ,
	@DonViTinh NVARCHAR(200) ,
	@DonGia FLOAT ,
	@ChietKhau INT ,
	@GiamGia FLOAT ,
	@TiLeTuVan INT ,
	@KhuyenMai NVARCHAR(200) ,
	@IsKhuyenMai INT ,
	@ChiPhiTuVan FLOAT ,
	@ThanhTien FLOAT ,
	@GhiChu NVARCHAR(200) ,
	@DmSanphamREF_old BIGINT ,
	@TK_AdMarket NVARCHAR(200) ,
	@TK_AdMarketID INT ,
	@SoLuongThucChay FLOAT ,
	@ThanhTienThucChay FLOAT ,
	@TrangThaiThucChay INT ,
	@ThoiGianBatDau DATETIME ,
	@ThoiGianKetThuc DATETIME ,
	@ThucChayDenNgay DATETIME ,
	@ThoiGianLog DATETIME ,
	@NguoiLog NVARCHAR(200) ,
	@LoaiLog INT ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT
AS
BEGIN
	PRINT 'KHONG SU DUNG LAY DU LIEU TU HDCN'
	--IF (
	--       EXISTS(
	--           SELECT *
	--           FROM   [HopDongChiTietLog]
	--           WHERE  [HopDongChiTietLogID] = @HopDongChiTietLogID
	--       )
	--   )
	--    UPDATE [dbo].[HopDongChiTietLog]
	--    SET    [HopDongChiTietREF]    = @HopDongChiTietREF,
	--           [HopDongFK]            = @HopDongFK,
	--           [DanhSachNhanHangREF]  = @DanhSachNhanHangREF,
	--           [NhanHang]             = @NhanHang,
	--           [DmNhomNganhREF]       = @DmNhomNganhREF,
	--           [TenNhomNganh]         = @TenNhomNganh,
	--           [DmLoaiREF]            = @DmLoaiREF,
	--           [TenLoai]              = @TenLoai,
	--           [DmNhomWebsiteREF]     = @DmNhomWebsiteREF,
	--           [TenNhomWebsite]       = @TenNhomWebsite,
	--           [DmWebsiteREF]         = @DmWebsiteREF,
	--           [TenWebsite]           = @TenWebsite,
	--           [DmSanPhamREF]         = @DmSanPhamREF,
	--           [TenSanPham]           = @TenSanPham,
	--           [DmLoaiBannerREF]      = @DmLoaiBannerREF,
	--           [TenLoaiBanner]        = @TenLoaiBanner,
	--           [DmChuyenMucREF]       = @DmChuyenMucREF,
	--           [TenChuyenMuc]         = @TenChuyenMuc,
	--           [DmBannerREF]          = @DmBannerREF,
	--           [TenBanner]            = @TenBanner,
	--           [ThoiGian]             = @ThoiGian,
	--           [SoLuong]              = @SoLuong,
	--           [DonViTinhREF]         = @DonViTinhREF,
	--           [DonViTinh]            = @DonViTinh,
	--           [DonGia]               = @DonGia,
	--           [ChietKhau]            = @ChietKhau,
	--           [GiamGia]              = @GiamGia,
	--           [TiLeTuVan]            = @TiLeTuVan,
	--           [KhuyenMai]            = @KhuyenMai,
	--           [IsKhuyenMai]          = @IsKhuyenMai,
	--           [ChiPhiTuVan]          = @ChiPhiTuVan,
	--           [ThanhTien]            = @ThanhTien,
	--           [GhiChu]               = @GhiChu,
	--           [DmSanphamREF_old]     = @DmSanphamREF_old,
	--           [TK_AdMarket]          = @TK_AdMarket,
	--           [TK_AdMarketID]        = @TK_AdMarketID,
	--           [SoLuongThucChay]      = @SoLuongThucChay,
	--           [ThanhTienThucChay]    = @ThanhTienThucChay,
	--           [TrangThaiThucChay]    = @TrangThaiThucChay,
	--           [ThoiGianBatDau]       = @ThoiGianBatDau,
	--           [ThoiGianKetThuc]      = @ThoiGianKetThuc,
	--           [ThucChayDenNgay]      = @ThucChayDenNgay,
	--           [ThoiGianLog]          = @ThoiGianLog,
	--           [NguoiLog]             = @NguoiLog,
	--           [LoaiLog]              = @LoaiLog,
	--           [CreatedBy]            = @CreatedBy,
	--           [CreatedAt]            = @CreatedAt,
	--           [LastModifiedBy]       = @LastModifiedBy,
	--           [LastModifiedAt]       = @LastModifiedAt,
	--           [DeletedStatus]        = @DeletedStatus,
	--           [PrintStatus]          = @PrintStatus,
	--           [RecordStatus]         = @RecordStatus
	--    WHERE  [HopDongChiTietLogID]  = @HopDongChiTietLogID
	--ELSE
	--    INSERT INTO [dbo].[HopDongChiTietLog]
	--      (
	--        [HopDongChiTietLogID],
	--        [HopDongChiTietREF],
	--        [HopDongFK],
	--        [DanhSachNhanHangREF],
	--        [NhanHang],
	--        [DmNhomNganhREF],
	--        [TenNhomNganh],
	--        [DmLoaiREF],
	--        [TenLoai],
	--        [DmNhomWebsiteREF],
	--        [TenNhomWebsite],
	--        [DmWebsiteREF],
	--        [TenWebsite],
	--        [DmSanPhamREF],
	--        [TenSanPham],
	--        [DmLoaiBannerREF],
	--        [TenLoaiBanner],
	--        [DmChuyenMucREF],
	--        [TenChuyenMuc],
	--        [DmBannerREF],
	--        [TenBanner],
	--        [ThoiGian],
	--        [SoLuong],
	--        [DonViTinhREF],
	--        [DonViTinh],
	--        [DonGia],
	--        [ChietKhau],
	--        [GiamGia],
	--        [TiLeTuVan],
	--        [KhuyenMai],
	--        [IsKhuyenMai],
	--        [ChiPhiTuVan],
	--        [ThanhTien],
	--        [GhiChu],
	--        [DmSanphamREF_old],
	--        [TK_AdMarket],
	--        [TK_AdMarketID],
	--        [SoLuongThucChay],
	--        [ThanhTienThucChay],
	--        [TrangThaiThucChay],
	--        [ThoiGianBatDau],
	--        [ThoiGianKetThuc],
	--        [ThucChayDenNgay],
	--        [ThoiGianLog],
	--        [NguoiLog],
	--        [LoaiLog],
	--        [CreatedBy],
	--        [CreatedAt],
	--        [LastModifiedBy],
	--        [LastModifiedAt],
	--        [DeletedStatus],
	--        [PrintStatus],
	--        [RecordStatus]
	--      )
	--    VALUES
	--      (
	--        @HopDongChiTietLogID,
	--        @HopDongChiTietREF,
	--        @HopDongFK,
	--        @DanhSachNhanHangREF,
	--        @NhanHang,
	--        @DmNhomNganhREF,
	--        @TenNhomNganh,
	--        @DmLoaiREF,
	--        @TenLoai,
	--        @DmNhomWebsiteREF,
	--        @TenNhomWebsite,
	--        @DmWebsiteREF,
	--        @TenWebsite,
	--        @DmSanPhamREF,
	--        @TenSanPham,
	--        @DmLoaiBannerREF,
	--        @TenLoaiBanner,
	--        @DmChuyenMucREF,
	--        @TenChuyenMuc,
	--        @DmBannerREF,
	--        @TenBanner,
	--        @ThoiGian,
	--        @SoLuong,
	--        @DonViTinhREF,
	--        @DonViTinh,
	--        @DonGia,
	--        @ChietKhau,
	--        @GiamGia,
	--        @TiLeTuVan,
	--        @KhuyenMai,
	--        @IsKhuyenMai,
	--        @ChiPhiTuVan,
	--        @ThanhTien,
	--        @GhiChu,
	--        @DmSanphamREF_old,
	--        @TK_AdMarket,
	--        @TK_AdMarketID,
	--        @SoLuongThucChay,
	--        @ThanhTienThucChay,
	--        @TrangThaiThucChay,
	--        @ThoiGianBatDau,
	--        @ThoiGianKetThuc,
	--        @ThucChayDenNgay,
	--        @ThoiGianLog,
	--        @NguoiLog,
	--        @LoaiLog,
	--        @CreatedBy,
	--        @CreatedAt,
	--        @LastModifiedBy,
	--        @LastModifiedAt,
	--        @DeletedStatus,
	--        @PrintStatus,
	--        @RecordStatus
	--      )
END

```
