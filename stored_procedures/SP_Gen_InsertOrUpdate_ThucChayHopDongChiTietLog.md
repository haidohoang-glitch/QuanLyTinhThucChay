# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTietLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:11:19.833000
- **Ngày sửa cuối**: 2017-11-08 10:20:29.243000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietID` | `bigint(8)` | No |
| `@HopDongREF` | `bigint(8)` | No |
| `@HopDongChiTietREF` | `bigint(8)` | No |
| `@DmBannerREF` | `nvarchar(400)` | No |
| `@TenBanner` | `nvarchar(400)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@ViTri` | `nvarchar(400)` | No |
| `@DmNhanHangREF` | `nvarchar(400)` | No |
| `@NhanHang` | `nvarchar(400)` | No |
| `@BookingREF` | `bigint(8)` | No |
| `@ThoiGianBatDau` | `date(3)` | No |
| `@ThoiGianKetThuc` | `date(3)` | No |
| `@SoLuongThucTreo` | `float(8)` | No |
| `@SoLuongThucChay` | `float(8)` | No |
| `@DmDonViTinhREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(400)` | No |
| `@TypeThucChay` | `int(4)` | No |
| `@Link` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@TenHinhThucQuangCao` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@InputType` | `int(4)` | No |
| `@IsReadBooking` | `int(4)` | No |
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
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTietLog]
	@ThucChayHopDongChiTietID BIGINT ,
	@HopDongREF BIGINT ,
	@HopDongChiTietREF BIGINT ,
	@DmBannerREF NVARCHAR(200) ,
	@TenBanner NVARCHAR(200) ,
	@DmViTriREF INT ,
	@ViTri NVARCHAR(200) ,
	@DmNhanHangREF NVARCHAR(200) ,
	@NhanHang NVARCHAR(200) ,
	@BookingREF BIGINT ,
	@ThoiGianBatDau date ,
	@ThoiGianKetThuc date ,
	@SoLuongThucTreo FLOAT ,
	@SoLuongThucChay FLOAT ,
	@DmDonViTinhREF INT ,
	@DonViTinh NVARCHAR(200) ,
	@TypeThucChay INT ,
	@Link NVARCHAR(200) ,
	@GhiChu NVARCHAR(200) ,
	@DmHinhThucQuangCaoREF INT ,
	@TenHinhThucQuangCao NVARCHAR(200) ,
	@DmSanPhamREF INT ,
	@TenSanPham NVARCHAR(200) ,
	@InputType INT ,
	@IsReadBooking INT ,
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
	
	SET @NhanHang = ISNULL(@NhanHang,'')
	SET @NhanHang = REPLACE(@NhanHang, '''''','''')

	DECLARE @IsExist INT
	SET @IsExist = (
	        SELECT COUNT(tchdctl.ThucChayHopDongChiTietID)
	        FROM   ThucChayHopDongChiTietLog tchdctl
	        WHERE  tchdctl.ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
	               AND tchdctl.ThoiGianLog = @ThoiGianLog
	               AND tchdctl.LoaiLog = @LoaiLog
	    )
	
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [ThucChayHopDongChiTietLog]
	           WHERE  1 > 2
	       )
	   )
	    UPDATE [dbo].[ThucChayHopDongChiTietLog]
	    SET    [ThucChayHopDongChiTietID]  = @ThucChayHopDongChiTietID,
	           [HopDongREF]                = @HopDongREF,
	           [HopDongChiTietREF]         = @HopDongChiTietREF,
	           [DmBannerREF]               = @DmBannerREF,
	           [TenBanner]                 = @TenBanner,
	           [DmViTriREF]                = @DmViTriREF,
	           [ViTri]                     = @ViTri,
	           [DmNhanHangREF]             = @DmNhanHangREF,
	           [NhanHang]                  = @NhanHang,
	           [BookingREF]                = @BookingREF,
	           [ThoiGianBatDau]            = @ThoiGianBatDau,
	           [ThoiGianKetThuc]           = @ThoiGianKetThuc,
	           [SoLuongThucTreo]           = @SoLuongThucTreo,
	           [SoLuongThucChay]           = @SoLuongThucChay,
	           [DmDonViTinhREF]            = @DmDonViTinhREF,
	           [DonViTinh]                 = @DonViTinh,
	           [TypeThucChay]              = @TypeThucChay,
	           [Link]                      = @Link,
	           [GhiChu]                    = @GhiChu,
	           [DmHinhThucQuangCaoREF]     = @DmHinhThucQuangCaoREF,
	           [TenHinhThucQuangCao]       = @TenHinhThucQuangCao,
	           [DmSanPhamREF]              = @DmSanPhamREF,
	           [TenSanPham]                = @TenSanPham,
	           [InputType]                 = @InputType,
	           [IsReadBooking]             = @IsReadBooking,
	           [ThoiGianLog]               = @ThoiGianLog,
	           [NguoiLog]                  = @NguoiLog,
	           [LoaiLog]                   = @LoaiLog,
	           [CreatedBy]                 = @CreatedBy,
	           [CreatedAt]                 = @CreatedAt,
	           [LastModifiedBy]            = @LastModifiedBy,
	           [LastModifiedAt]            = @LastModifiedAt,
	           [DeletedStatus]             = @DeletedStatus,
	           [PrintStatus]               = @PrintStatus,
	           [RecordStatus]              = @RecordStatus
	    WHERE  1 > 2
	ELSE
	IF (@IsExist = 0)
	BEGIN
	    INSERT INTO [dbo].[ThucChayHopDongChiTietLog]
	      (
	        [ThucChayHopDongChiTietID],
	        [HopDongREF],
	        [HopDongChiTietREF],
	        [DmBannerREF],
	        [TenBanner],
	        [DmViTriREF],
	        [ViTri],
	        [DmNhanHangREF],
	        [NhanHang],
	        [BookingREF],
	        [ThoiGianBatDau],
	        [ThoiGianKetThuc],
	        [SoLuongThucTreo],
	        [SoLuongThucChay],
	        [DmDonViTinhREF],
	        [DonViTinh],
	        [TypeThucChay],
	        [Link],
	        [GhiChu],
	        [DmHinhThucQuangCaoREF],
	        [TenHinhThucQuangCao],
	        [DmSanPhamREF],
	        [TenSanPham],
	        [InputType],
	        [IsReadBooking],
	        [ThoiGianLog],
	        [NguoiLog],
	        [LoaiLog],
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
	        @ThucChayHopDongChiTietID,
	        @HopDongREF,
	        @HopDongChiTietREF,
	        @DmBannerREF,
	        @TenBanner,
	        @DmViTriREF,
	        @ViTri,
	        @DmNhanHangREF,
	        @NhanHang,
	        @BookingREF,
	        @ThoiGianBatDau,
	        @ThoiGianKetThuc,
	        @SoLuongThucTreo,
	        @SoLuongThucChay,
	        @DmDonViTinhREF,
	        @DonViTinh,
	        @TypeThucChay,
	        @Link,
	        @GhiChu,
	        @DmHinhThucQuangCaoREF,
	        @TenHinhThucQuangCao,
	        @DmSanPhamREF,
	        @TenSanPham,
	        @InputType,
	        @IsReadBooking,
	        @ThoiGianLog,
	        @NguoiLog,
	        @LoaiLog,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )
	END
	
	IF (@LoaiLog = 3)
	BEGIN
	    UPDATE ThucChayHopDongChiTiet
	    SET    LastModifiedBy            = @LastModifiedBy,
	           LastModifiedAt            = @ThoiGianLog,
	           DeletedStatus             = 1
	    WHERE  ThucChayHopDongChiTietID  = @ThucChayHopDongChiTietID
	END
END

```
