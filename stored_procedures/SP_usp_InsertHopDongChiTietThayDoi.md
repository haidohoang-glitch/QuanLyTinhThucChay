# Stored Procedure: `usp_InsertHopDongChiTietThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:31:22
- **Ngày sửa cuối**: 2014-11-19 12:16:45.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietThayDoiID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@HopDongThayDoiREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(510)` | No |
| `@DmNhomNganhREF` | `int(4)` | No |
| `@TenNhomNganh` | `nvarchar(100)` | No |
| `@DmLoaiREF` | `int(4)` | No |
| `@TenLoai` | `nvarchar(100)` | No |
| `@DmNhomWebsiteREF` | `int(4)` | No |
| `@TenNhomWebsite` | `nvarchar(200)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@DmLoaiBannerREF` | `int(4)` | No |
| `@TenLoaiBanner` | `nvarchar(100)` | No |
| `@DmChuyenMucREF` | `int(4)` | No |
| `@TenChuyenMuc` | `nvarchar(200)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |
| `@ThoiGian` | `nvarchar(100)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@GiamGia` | `float(8)` | No |
| `@TiLeTuVan` | `float(8)` | No |
| `@KhuyenMai` | `nvarchar(100)` | No |
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

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertHopDongChiTietThayDoi]
	@HopDongChiTietThayDoiID INT,
	@HopDongChiTietREF INT,
	@HopDongFK INT,
	@HopDongThayDoiREF INT,
	@NhanHang NVARCHAR(255),
	@DmNhomNganhREF INT,
	@TenNhomNganh NVARCHAR(50),
	@DmLoaiREF INT,
	@TenLoai NVARCHAR(50),
	@DmNhomWebsiteREF INT,
	@TenNhomWebsite NVARCHAR(100),
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(100),
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(100),
	@DmLoaiBannerREF INT,
	@TenLoaiBanner NVARCHAR(50),
	@DmChuyenMucREF INT,
	@TenChuyenMuc NVARCHAR(100),
	@DmViTriREF INT,
	@TenViTri NVARCHAR(50),
	@ThoiGian NVARCHAR(50),
	@SoLuong INT,
	@DonViTinh NVARCHAR(50),
	@DonGia FLOAT,
	@ChietKhau FLOAT,
	@GiamGia FLOAT,
	@TiLeTuVan FLOAT,
	@KhuyenMai NVARCHAR(50),
	@IsKhuyenMai INT,
	@ChiPhiTuVan FLOAT,
	@ThanhTien FLOAT,
	@GhiChu NVARCHAR(255),
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModifiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT
AS
	SET NOCOUNT ON
	IF (
	       EXISTS(
	           SELECT [HopDongFK]
	           FROM   [HopDongChiTietThayDoi]
	           WHERE  [HopDongChiTietThayDoiID] = @HopDongChiTietThayDoiID
	       )
	   )
	    UPDATE [dbo].[HopDongChiTietThayDoi]
	    SET    [HopDongChiTietREF]        = @HopDongChiTietREF,
	           [HopDongFK]                = @HopDongFK,
	           [HopDongThayDoiREF]        = @HopDongThayDoiREF,
	           [NhanHang]                 = @NhanHang,
	           [DmNhomNganhREF]           = @DmNhomNganhREF,
	           [TenNhomNganh]             = @TenNhomNganh,
	           [DmLoaiREF]                = @DmLoaiREF,
	           [TenLoai]                  = @TenLoai,
	           [DmNhomWebsiteREF]         = @DmNhomWebsiteREF,
	           [TenNhomWebsite]           = @TenNhomWebsite,
	           [DmWebsiteREF]             = @DmWebsiteREF,
	           [TenWebsite]               = @TenWebsite,
	           [DmSanPhamREF]             = @DmSanPhamREF,
	           [TenSanPham]               = @TenSanPham,
	           [DmLoaiBannerREF]          = @DmLoaiBannerREF,
	           [TenLoaiBanner]            = @TenLoaiBanner,
	           [DmChuyenMucREF]           = @DmChuyenMucREF,
	           [TenChuyenMuc]             = @TenChuyenMuc,
	           [DmViTriREF]               = @DmViTriREF,
	           [TenViTri]                 = @TenViTri,
	           [ThoiGian]                 = @ThoiGian,
	           [SoLuong]                  = @SoLuong,
	           [DonViTinh]                = @DonViTinh,
	           [DonGia]                   = @DonGia,
	           [ChietKhau]                = @ChietKhau,
	           [GiamGia]                  = @GiamGia,
	           [TiLeTuVan]                = @TiLeTuVan,
	           [KhuyenMai]                = @KhuyenMai,
	           [IsKhuyenMai]              = @IsKhuyenMai,
	           [ChiPhiTuVan]              = @ChiPhiTuVan,
	           [ThanhTien]                = @ThanhTien,
	           [GhiChu]                   = @GhiChu,
	           [LastModifiedBy]           = @LastModifiedBy,
	           [LastModifiedAt]           = @LastModifiedAt,
	           [DeletedStatus]            = @DeletedStatus,
	           [PrintStatus]              = @PrintStatus,
	           [RecordStatus]             = @RecordStatus
	    WHERE  [HopDongChiTietThayDoiID]  = @HopDongChiTietThayDoiID
	ELSE
	    INSERT INTO [dbo].[HopDongChiTietThayDoi]
	      (
	        [HopDongChiTietThayDoiID],
	        [HopDongChiTietREF],
	        [HopDongFK],
	        [HopDongThayDoiREF],
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
	        [RecordStatus]
	      )
	    VALUES
	      (
	        @HopDongChiTietThayDoiID,
	        @HopDongChiTietREF,
	        @HopDongFK,
	        @HopDongThayDoiREF,
	        @NhanHang,
	        @DmNhomNganhREF,
	        @TenNhomNganh,
	        @DmLoaiREF,
	        @TenLoai,
	        @DmNhomWebsiteREF,
	        @TenNhomWebsite,
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
	        @RecordStatus
	      )

```
