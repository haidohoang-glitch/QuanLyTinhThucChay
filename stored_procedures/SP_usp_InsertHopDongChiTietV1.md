# Stored Procedure: `usp_InsertHopDongChiTietV1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-04 17:26:21.780000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.213000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@DanhSachNhanHangREF` | `nvarchar(500)` | No |
| `@NhanHang` | `nvarchar(510)` | No |
| `@DmNhomNganhREF` | `nvarchar(500)` | No |
| `@TenNhomNganh` | `nvarchar(1000)` | No |
| `@DmLoaiREF` | `int(4)` | No |
| `@TenLoai` | `nvarchar(500)` | No |
| `@DmNhomWebsiteREF` | `int(4)` | No |
| `@TenNhomWebsite` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(1000)` | No |
| `@DmLoaiBannerREF` | `int(4)` | No |
| `@TenLoaiBanner` | `nvarchar(500)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@TenChuyenMuc` | `nvarchar(1000)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(1000)` | No |
| `@ThoiGian` | `nvarchar(100)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinhREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@GiamGia` | `float(8)` | No |
| `@TiLeTuVan` | `float(8)` | No |
| `@KhuyenMai` | `nvarchar(500)` | No |
| `@IsKhuyenMai` | `int(4)` | No |
| `@ChiPhiTuVan` | `float(8)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@DmSanphamREF_old` | `int(4)` | No |
| `@TK_AdMarket` | `nvarchar(200)` | No |
| `@TK_AdMarketID` | `int(4)` | No |
| `@SoluongThucChay` | `float(8)` | No |
| `@ThanhtienThucChay` | `float(8)` | No |
| `@TrangthaiThucChay` | `int(4)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@ThucChayDenNgay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertHopDongChiTietV1](
    @HopDongChiTietID     INT,
    @HopDongFK            INT,
    @DanhSachNhanHangREF  NVARCHAR(250),
    @NhanHang             NVARCHAR(255),
    @DmNhomNganhREF       NVARCHAR(250),
    @TenNhomNganh         NVARCHAR(500),
    @DmLoaiREF            INT,
    @TenLoai              NVARCHAR(250),
    @DmNhomWebsiteREF     INT,
    @TenNhomWebsite       NVARCHAR(100),
    @DmWebsiteREF         INT,
    @TenWebsite           NVARCHAR(100),
    @DmSanPhamREF         INT,
    @TenSanPham           NVARCHAR(500),
    @DmLoaiBannerREF      INT,
    @TenLoaiBanner        NVARCHAR(250),
    @DmChuyenMucREF       INT,
    @TenChuyenMuc         NVARCHAR(500),
    @DmViTriREF           INT,
    @TenViTri             NVARCHAR(500),
    @ThoiGian             NVARCHAR(50),
    @SoLuong              INT,
    @DonViTinhREF         INT,
    @DonViTinh            NVARCHAR(50),
    @DonGia               FLOAT,
    @ChietKhau            FLOAT,
    @GiamGia              FLOAT,
    @TiLeTuVan            FLOAT,
    @KhuyenMai            NVARCHAR(250),
    @IsKhuyenMai          INT,
    @ChiPhiTuVan          FLOAT,
    @ThanhTien            FLOAT,
    @GhiChu               NVARCHAR(255),
    @CreatedBy            NVARCHAR(50),
    @CreatedAt            DATETIME,
    @LastModifiedBy       NVARCHAR(50),
    @LastModifiedAt       DATETIME,
    @DeletedStatus        INT,
    @PrintStatus          INT,
    @RecordStatus         INT,
    @DmSanphamREF_old     INT,
    @TK_AdMarket          NVARCHAR(100),
    @TK_AdMarketID        INT,
    @SoluongThucChay      FLOAT,
    @ThanhtienThucChay    FLOAT,
    @TrangthaiThucChay    INT,
    @ThoiGianBatDau       DATETIME,
    @ThoiGianKetThuc      DATETIME,
    @ThucChayDenNgay      DATETIME
)
AS
BEGIN
	DECLARE @TenNhomWebsiteTemp NVARCHAR(100)
	SET @TenNhomWebsiteTemp = @TenNhomWebsite
	SET NOCOUNT ON
	
	IF (@DmSanPhamREF IN (240, 370, 339))
	BEGIN
	    SELECT @TenNhomWebsiteTemp = [NhomWebsiteName]
	    FROM   [dbo].[DmNhomWebsite]
	    WHERE  [DmNhomWebsiteId] = @DmNhomWebsiteREF
	END
	
	IF (
	       EXISTS(
	           SELECT HopDongFK
	           FROM   [HopDongChiTiet]
	           WHERE  [HopDongChiTietID] = @HopDongChiTietID
	       )
	   )
	    UPDATE [dbo].[HopDongChiTiet]
	    SET    [HopDongFK]            = @HopDongFK,
	           [DanhSachNhanHangREF]  = @DanhSachNhanHangREF,
	           [NhanHang]             = @NhanHang,
	           [DmNhomNganhREF]       = @DmNhomNganhREF,
	           [TenNhomNganh]         = @TenNhomNganh,
	           [DmLoaiREF]            = @DmLoaiREF,
	           [TenLoai]              = @TenLoai,
	           [DmNhomWebsiteREF]     = @DmNhomWebsiteREF,
	           [TenNhomWebsite]       = @TenNhomWebsiteTemp,
	           [DmWebsiteREF]         = @DmWebsiteREF,
	           [TenWebsite]           = @TenWebsite,
	           [DmSanPhamREF]         = @DmSanPhamREF,
	           [TenSanPham]           = @TenSanPham,
	           [DmLoaiBannerREF]      = @DmLoaiBannerREF,
	           [TenLoaiBanner]        = @TenLoaiBanner,
	           [DmChuyenMucREF]       = @DmChuyenMucREF,
	           [TenChuyenMuc]         = @TenChuyenMuc,
	           [DmViTriREF]           = @DmViTriREF,
	           [TenViTri]             = @TenViTri,
	           [ThoiGian]             = @ThoiGian,
	           [SoLuong]              = @SoLuong,
	           [DonViTinhREF]         = @DonViTinhREF,
	           [DonViTinh]            = @DonViTinh,
	           [DonGia]               = @DonGia,
	           [ChietKhau]            = @ChietKhau,
	           [GiamGia]              = @GiamGia,
	           [TiLeTuVan]            = @TiLeTuVan,
	           [KhuyenMai]            = @KhuyenMai,
	           [IsKhuyenMai]          = @IsKhuyenMai,
	           [ChiPhiTuVan]          = @ChiPhiTuVan,
	           [ThanhTien]            = @ThanhTien,
	           [GhiChu]               = @GhiChu,
	           [LastModifiedBy]       = @LastModifiedBy,
	           [LastModifiedAt]       = @LastModifiedAt,
	           [DeletedStatus]        = @DeletedStatus,
	           [PrintStatus]          = @PrintStatus,
	           [RecordStatus]         = @RecordStatus,
	           DmSanphamREF_old       = @DmSanphamREF_old,
	           TK_AdMarket            = @TK_AdMarket,
	           TK_AdMarketID          = @TK_AdMarketID,
	           SoluongThucChay        = @SoluongThucChay,
	           ThanhtienThucChay      = @ThanhtienThucChay,
	           TrangthaiThucChay      = @TrangthaiThucChay,
	           ThoiGianBatDau         = @ThoiGianBatDau,
	           ThoiGianKetThuc        = @ThoiGianKetThuc,
	           ThucChayDenNgay        = @ThucChayDenNgay
	    WHERE  [HopDongChiTietID]     = @HopDongChiTietID
	ELSE
	    INSERT INTO [dbo].[HopDongChiTiet]
	      (
	        [HopDongChiTietID],
	        [HopDongFK],
	        [DanhSachNhanHangREF],
	        [NhanHang],
	        [DmNhomNganhREF],
	        [TenNhomNganh],
	        [DmLoaiREF],
	        [TenLoai],
	        [DmNhomWebsiteREF],
	        [TenNhomWebsite],
	        [DmWebsiteREF],
	        [TenWebsite],
	        [DmSanPhamREF],
	        [TenSanPham],
	        [DmLoaiBannerREF],
	        [TenLoaiBanner],
	        [DmChuyenMucREF],
	        [TenChuyenMuc],
	        [DmViTriREF],
	        [TenViTri],
	        [ThoiGian],
	        [SoLuong],
	        [DonViTinhREF],
	        [DonViTinh],
	        [DonGia],
	        [ChietKhau],
	        [GiamGia],
	        [TiLeTuVan],
	        [KhuyenMai],
	        [IsKhuyenMai],
	        [ChiPhiTuVan],
	        [ThanhTien],
	        [GhiChu],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
	        DmSanphamREF_old,
	        TK_AdMarket,
	        TK_AdMarketID,
	        SoluongThucChay,
	        ThanhtienThucChay,
	        TrangthaiThucChay,
	        ThoiGianBatDau,
	        ThoiGianKetThuc,
	        ThucChayDenNgay
	      )
	    VALUES
	      (
	        @HopDongChiTietID,
	        @HopDongFK,
	        @DanhSachNhanHangREF,
	        @NhanHang,
	        @DmNhomNganhREF,
	        @TenNhomNganh,
	        @DmLoaiREF,
	        @TenLoai,
	        @DmNhomWebsiteREF,
	        @TenNhomWebsiteTemp,
	        @DmWebsiteREF,
	        @TenWebsite,
	        @DmSanPhamREF,
	        @TenSanPham,
	        @DmLoaiBannerREF,
	        @TenLoaiBanner,
	        @DmChuyenMucREF,
	        @TenChuyenMuc,
	        @DmViTriREF,
	        @TenViTri,
	        @ThoiGian,
	        @SoLuong,
	        @DonViTinhREF,
	        @DonViTinh,
	        @DonGia,
	        @ChietKhau,
	        @GiamGia,
	        @TiLeTuVan,
	        @KhuyenMai,
	        @IsKhuyenMai,
	        @ChiPhiTuVan,
	        @ThanhTien,
	        @GhiChu,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus,
	        @DmSanphamREF_old,
	        @TK_AdMarket,
	        @TK_AdMarketID,
	        @SoluongThucChay,
	        @ThanhtienThucChay,
	        @TrangthaiThucChay,
	        @ThoiGianBatDau,
	        @ThoiGianKetThuc,
	        @ThucChayDenNgay
	      )
END

```
