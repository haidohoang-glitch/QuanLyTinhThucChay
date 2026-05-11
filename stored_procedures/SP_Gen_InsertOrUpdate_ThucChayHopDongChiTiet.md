# Stored Procedure: `Gen_InsertOrUpdate_ThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-28 14:08:36.653000
- **Ngày sửa cuối**: 2017-07-05 08:25:39.607000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietID` | `bigint(8)` | No |
| `@HopDongREF` | `bigint(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmBannerREF` | `nvarchar(400)` | No |
| `@TenBanner` | `nvarchar(400)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@ViTri` | `nvarchar(400)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(400)` | No |
| `@BookingREF` | `bigint(8)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@SoLuongThucTreo` | `int(4)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
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
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@KichThuoc` | `nvarchar(400)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@ThanhTien` | `float(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayHopDongChiTiet] 	
@ThucChayHopDongChiTietID bigint ,	
@HopDongREF bigint ,	
@HopDongChiTietREF int ,	
@DmBannerREF nvarchar (200) ,	
@TenBanner nvarchar (200) ,	
@DmViTriREF int ,	
@ViTri nvarchar (200) ,	
@DmNhanHangREF int ,	
@NhanHang nvarchar (200) ,	
@BookingREF bigint ,	
@ThoiGianBatDau datetime ,	
@ThoiGianKetThuc datetime ,	
@SoLuongThucTreo int ,	
@SoLuongThucChay int ,	
@DmDonViTinhREF int ,	
@DonViTinh nvarchar (200) ,	
@TypeThucChay int ,	
@Link nvarchar (200) ,	
@GhiChu nvarchar (200) ,	
@DmHinhThucQuangCaoREF int ,	
@TenHinhThucQuangCao nvarchar (200) ,	
@DmSanPhamREF int ,	
@TenSanPham nvarchar (200) ,	
@InputType int ,	
@IsReadBooking int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int ,	
@KichThuoc nvarchar (200) ,
@DonGia FLOAT,
@ChietKhau FLOAT, 
@ThanhTien FLOAT
As 	
BEGIN
	SET @NhanHang = [dbo].[ReplaceNhanHangDoubleNhay](@NhanHang)

	if(exists(select * from [ThucChayHopDongChiTiet] where [ThucChayHopDongChiTietID] = @ThucChayHopDongChiTietID))	
	UPDATE [dbo].[ThucChayHopDongChiTiet] SET 	
	[HopDongREF] = @HopDongREF,	
	[HopDongChiTietREF] = @HopDongChiTietREF,	
	[DmBannerREF] = @DmBannerREF,	
	[TenBanner] = @TenBanner,	
	[DmViTriREF] = @DmViTriREF,	
	[ViTri] = @ViTri,	
	[DmNhanHangREF] = @DmNhanHangREF,	
	[NhanHang] = @NhanHang,	
	[BookingREF] = @BookingREF,	
	[ThoiGianBatDau] = @ThoiGianBatDau,	
	[ThoiGianKetThuc] = @ThoiGianKetThuc,	
	[SoLuongThucTreo] = @SoLuongThucTreo,	
	[SoLuongThucChay] = @SoLuongThucChay,	
	[DmDonViTinhREF] = @DmDonViTinhREF,	
	[DonViTinh] = @DonViTinh,	
	[TypeThucChay] = @TypeThucChay,	
	[Link] = @Link,	
	[GhiChu] = @GhiChu,	
	[DmHinhThucQuangCaoREF] = @DmHinhThucQuangCaoREF,	
	[TenHinhThucQuangCao] = @TenHinhThucQuangCao,	
	[DmSanPhamREF] = @DmSanPhamREF,	
	[TenSanPham] = @TenSanPham,	
	[InputType] = @InputType,	
	[IsReadBooking] = @IsReadBooking,	
	[CreatedBy] = @CreatedBy,	
	[CreatedAt] = @CreatedAt,	
	[LastModifiedBy] = @LastModifiedBy,	
	[LastModifiedAt] = @LastModifiedAt,	
	[KichThuoc] = @KichThuoc ,
	[DonGia] = @DonGia,
	[ChietKhau] = @ChietKhau, 
	[ThanhTien] = @ThanhTien WHERE [ThucChayHopDongChiTietID] = @ThucChayHopDongChiTietID	
	else 	
	INSERT INTO [dbo].[ThucChayHopDongChiTiet] (	
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
	[CreatedBy],	
	[CreatedAt],	
	[LastModifiedBy],	
	[LastModifiedAt],	
	[DeletedStatus],	
	[PrintStatus],	
	[RecordStatus],	
	[KichThuoc],
	[DonGia] ,
	[ChietKhau] , 
	[ThanhTien] )	
	Values 	
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
	@CreatedBy,	
	@CreatedAt,	
	@LastModifiedBy,	
	@LastModifiedAt,	
	@DeletedStatus,	
	@PrintStatus,	
	@RecordStatus,	
	@KichThuoc,
	@DonGia,
	@ChietKhau, 
	@ThanhTien)
END
```
