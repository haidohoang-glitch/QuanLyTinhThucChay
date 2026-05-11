# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTietThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-09 15:34:23.653000
- **Ngày sửa cuối**: 2017-07-13 16:58:17.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietThayDoiID` | `int(4)` | No |
| `@HopDongChiTietREF` | `bigint(8)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@HopDongThayDoiREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(400)` | No |
| `@DmNhomNganhREF` | `bigint(8)` | No |
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
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(400)` | No |
| `@ThoiGian` | `nvarchar(400)` | No |
| `@SoLuong` | `nvarchar(400)` | No |
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
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTietThayDoi] 	
@HopDongChiTietThayDoiID int ,	
@HopDongChiTietREF bigint ,	
@HopDongFK int ,	
@HopDongThayDoiREF int ,	
@NhanHang nvarchar (200) ,	
@DmNhomNganhREF bigint ,	
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
@DmViTriREF int ,	
@TenViTri nvarchar (200) ,	
@ThoiGian nvarchar (200) ,	
@SoLuong nvarchar (200) ,	
@DonViTinh nvarchar (200) ,	
@DonGia float ,	
@ChietKhau int ,	
@GiamGia float ,	
@TiLeTuVan int ,	
@KhuyenMai nvarchar (200) ,	
@IsKhuyenMai int ,	
@ChiPhiTuVan float ,	
@ThanhTien float ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [HopDongChiTietThayDoi] where [HopDongChiTietThayDoiID] = @HopDongChiTietThayDoiID))	
UPDATE [dbo].[HopDongChiTietThayDoi] SET 	
[HopDongChiTietREF] = @HopDongChiTietREF,	
[HopDongFK] = @HopDongFK,	
[HopDongThayDoiREF] = @HopDongThayDoiREF,	
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
[DmViTriREF] = @DmViTriREF,	
[TenViTri] = @TenViTri,	
[ThoiGian] = @ThoiGian,	
[SoLuong] = @SoLuong,	
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
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [HopDongChiTietThayDoiID] = @HopDongChiTietThayDoiID	
else 	
INSERT INTO [dbo].[HopDongChiTietThayDoi] (	
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
[RecordStatus])	
Values 	
(	
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
@RecordStatus)

```
