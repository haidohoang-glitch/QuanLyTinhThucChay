# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-09 15:34:25.287000
- **Ngày sửa cuối**: 2017-03-11 10:44:00.980000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
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
| `@TenViTri` | `nvarchar(400)` | No |
| `@ThoiGian` | `nvarchar(400)` | No |
| `@SoLuong` | `bigint(8)` | No |
| `@DonViTinhREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(400)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@GiamGia` | `float(8)` | No |
| `@TiLeTuVan` | `float(8)` | No |
| `@KhuyenMai` | `nvarchar(400)` | No |
| `@IsKhuyenMai` | `int(4)` | No |
| `@ChiPhiTuVan` | `float(8)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@DmSanphamREF_old` | `bigint(8)` | No |
| `@TK_AdMarket` | `nvarchar(400)` | No |
| `@TK_AdMarketID` | `nvarchar(400)` | No |
| `@SoLuongThucChay` | `float(8)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@TrangThaiThucChay` | `int(4)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@ThucChayDenNgay` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@DmLoaiNenTangREF` | `int(4)` | No |
| `@TenLoaiNenTang` | `nvarchar(400)` | No |
| `@DonViTinhThucChayMuaNgoaiREF` | `int(4)` | No |
| `@DonViTinhThucChayMuaNgoai` | `nvarchar(400)` | No |
| `@ThanhTienThucChayMuaNgoaiTruocCK` | `float(8)` | No |
| `@ChietKhauMuaNgoai` | `int(4)` | No |
| `@IsVuotKhung` | `int(4)` | No |
| `@SoHopDongHT` | `nvarchar(400)` | No |
| `@SuKienREF` | `int(4)` | No |
| `@TenSuKien` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTiet] 	
@HopDongChiTietID int ,	
@HopDongFK int ,	
@DanhSachNhanHangREF nvarchar (200) ,	
@NhanHang nvarchar (200) ,	
@DmNhomNganhREF nvarchar (200) ,	
@TenNhomNganh nvarchar (200) ,	
@DmLoaiREF bigint ,	
@TenLoai nvarchar (200) ,	
@DmNhomWebsiteREF nvarchar (200) ,	
@TenNhomWebsite nvarchar (200) ,	
@DmWebsiteREF int ,	
@TenWebsite nvarchar (200) ,	
@DmSanPhamREF int ,	
@TenSanPham nvarchar (200) ,	
@DmLoaiBannerREF int ,	
@TenLoaiBanner nvarchar (200) ,	
@DmChuyenMucREF int ,	
@TenChuyenMuc nvarchar (200) ,	
@DmBannerREF int ,	
@TenBanner nvarchar (200) ,	
@TenViTri nvarchar (200) ,	
@ThoiGian nvarchar (200) ,	
@SoLuong bigint ,	
@DonViTinhREF int ,	
@DonViTinh nvarchar (200) ,	
@DonGia float ,	
@ChietKhau FLOAT ,	
@GiamGia float ,	
@TiLeTuVan float ,	
@KhuyenMai nvarchar (200) ,	
@IsKhuyenMai int ,	
@ChiPhiTuVan float ,	
@ThanhTien float ,	
@GhiChu nvarchar (200) ,	
@DmSanphamREF_old bigint ,	
@TK_AdMarket nvarchar (200) ,	
@TK_AdMarketID nvarchar (200) ,	
@SoLuongThucChay float ,	
@ThanhTienThucChay float ,	
@TrangThaiThucChay int ,	
@ThoiGianBatDau datetime ,	
@ThoiGianKetThuc datetime ,	
@ThucChayDenNgay datetime ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int ,	
@DmLoaiNenTangREF int ,	
@TenLoaiNenTang nvarchar (200) ,	
@DonViTinhThucChayMuaNgoaiREF int ,	
@DonViTinhThucChayMuaNgoai nvarchar (200) ,	
@ThanhTienThucChayMuaNgoaiTruocCK float ,	
@ChietKhauMuaNgoai int ,	
@IsVuotKhung int ,	
@SoHopDongHT nvarchar (200) ,	
@SuKienREF int ,	
@TenSuKien nvarchar (200) 	
As 	
BEGIN
	SET @NhanHang = [dbo].[ReplaceNhanHangDoubleNhay](@NhanHang)
	if(exists(select * from [HopDongChiTiet] where [HopDongChiTietID] = @HopDongChiTietID))	
	UPDATE [dbo].[HopDongChiTiet] SET 	
	[HopDongFK] = @HopDongFK,	
	[DanhSachNhanHangREF] = @DanhSachNhanHangREF,	
	[NhanHang] = @NhanHang,	
	[DmNhomNganhREF] = @DmNhomNganhREF,	
	[TenNhomNganh] = @TenNhomNganh,	
	[DmLoaiREF] = @DmLoaiREF,	
	[TenLoai] = @TenLoai,	
	[DmNhomWebsiteREF] = @DmNhomWebsiteREF,	
	[TenNhomWebsite] = @TenNhomWebsite,	
	[DmWebsiteREF] = @DmWebsiteREF,	
	[TenWebsite] = @TenWebsite,	
	[DmSanPhamREF] = @DmSanPhamREF,	
	[TenSanPham] = @TenSanPham,	
	[DmLoaiBannerREF] = @DmLoaiBannerREF,	
	[TenLoaiBanner] = @TenLoaiBanner,	
	[DmChuyenMucREF] = @DmChuyenMucREF,	
	[TenChuyenMuc] = @TenChuyenMuc,	
	[DmBannerREF] = @DmBannerREF,	
	[TenBanner] = @TenBanner,	
	[TenViTri] = @TenViTri,	
	[ThoiGian] = @ThoiGian,	
	[SoLuong] = @SoLuong,	
	[DonViTinhREF] = @DonViTinhREF,	
	[DonViTinh] = @DonViTinh,	
	[DonGia] = @DonGia,	
	[ChietKhau] = @ChietKhau,	
	[GiamGia] = @GiamGia,	
	[TiLeTuVan] = @TiLeTuVan,	
	[KhuyenMai] = @KhuyenMai,	
	[IsKhuyenMai] = @IsKhuyenMai,	
	[ChiPhiTuVan] = @ChiPhiTuVan,	
	[ThanhTien] = @ThanhTien,	
	[GhiChu] = @GhiChu,	
	[DmSanphamREF_old] = @DmSanphamREF_old,	
	[TK_AdMarket] = @TK_AdMarket,	
	[TK_AdMarketID] = @TK_AdMarketID,	
	[SoLuongThucChay] = @SoLuongThucChay,	
	[ThanhTienThucChay] = @ThanhTienThucChay,	
	[TrangThaiThucChay] = @TrangThaiThucChay,	
	[ThoiGianBatDau] = @ThoiGianBatDau,	
	[ThoiGianKetThuc] = @ThoiGianKetThuc,	
	[ThucChayDenNgay] = @ThucChayDenNgay,	
	[CreatedBy] = @CreatedBy,	
	[CreatedAt] = @CreatedAt,	
	[LastModifiedBy] = @LastModifiedBy,	
	[LastModifiedAt] = @LastModifiedAt,	
	[DeletedStatus] = @DeletedStatus,	
	[PrintStatus] = @PrintStatus,	
	[RecordStatus] = @RecordStatus,	
	[DmLoaiNenTangREF] = @DmLoaiNenTangREF,	
	[TenLoaiNenTang] = @TenLoaiNenTang,	
	[DonViTinhThucChayMuaNgoaiREF] = @DonViTinhThucChayMuaNgoaiREF,	
	[DonViTinhThucChayMuaNgoai] = @DonViTinhThucChayMuaNgoai,	
	[ThanhTienThucChayMuaNgoaiTruocCK] = @ThanhTienThucChayMuaNgoaiTruocCK,	
	[ChietKhauMuaNgoai] = @ChietKhauMuaNgoai,	
	[IsVuotKhung] = @IsVuotKhung,	
	[SoHopDongHT] = @SoHopDongHT,	
	[SuKienREF] = @SuKienREF,	
	[TenSuKien] = @TenSuKien where [HopDongChiTietID] = @HopDongChiTietID	
	else 	
	INSERT INTO [dbo].[HopDongChiTiet] (	
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
	[DmBannerREF],	
	[TenBanner],	
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
	[DmSanphamREF_old],	
	[TK_AdMarket],	
	[TK_AdMarketID],	
	[SoLuongThucChay],	
	[ThanhTienThucChay],	
	[TrangThaiThucChay],	
	[ThoiGianBatDau],	
	[ThoiGianKetThuc],	
	[ThucChayDenNgay],	
	[CreatedBy],	
	[CreatedAt],	
	[LastModifiedBy],	
	[LastModifiedAt],	
	[DeletedStatus],	
	[PrintStatus],	
	[RecordStatus],	
	[DmLoaiNenTangREF],	
	[TenLoaiNenTang],	
	[DonViTinhThucChayMuaNgoaiREF],	
	[DonViTinhThucChayMuaNgoai],	
	[ThanhTienThucChayMuaNgoaiTruocCK],	
	[ChietKhauMuaNgoai],	
	[IsVuotKhung],	
	[SoHopDongHT],	
	[SuKienREF],	
	[TenSuKien])	
	Values 	
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
	@TenNhomWebsite,	
	@DmWebsiteREF,	
	@TenWebsite,	
	@DmSanPhamREF,	
	@TenSanPham,	
	@DmLoaiBannerREF,	
	@TenLoaiBanner,	
	@DmChuyenMucREF,	
	@TenChuyenMuc,	
	@DmBannerREF,	
	@TenBanner,	
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
	@DmSanphamREF_old,	
	@TK_AdMarket,	
	@TK_AdMarketID,	
	@SoLuongThucChay,	
	@ThanhTienThucChay,	
	@TrangThaiThucChay,	
	@ThoiGianBatDau,	
	@ThoiGianKetThuc,	
	@ThucChayDenNgay,	
	@CreatedBy,	
	@CreatedAt,	
	@LastModifiedBy,	
	@LastModifiedAt,	
	@DeletedStatus,	
	@PrintStatus,	
	@RecordStatus,	
	@DmLoaiNenTangREF,	
	@TenLoaiNenTang,	
	@DonViTinhThucChayMuaNgoaiREF,	
	@DonViTinhThucChayMuaNgoai,	
	@ThanhTienThucChayMuaNgoaiTruocCK,	
	@ChietKhauMuaNgoai,	
	@IsVuotKhung,	
	@SoHopDongHT,	
	@SuKienREF,	
	@TenSuKien)
END
```
