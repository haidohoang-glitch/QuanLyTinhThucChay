# Stored Procedure: `Gen_InsertOrUpdate_ThucChay_bk`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:50.963000
- **Ngày sửa cuối**: 2017-09-11 15:02:50.987000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayID` | `nvarchar(400)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@DanhsachDmBookingREF` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@DmNhomWebsiteREF` | `int(4)` | No |
| `@TenNhomWebsite` | `nvarchar(400)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@DmChienDichREF` | `int(4)` | No |
| `@TenChienDich` | `nvarchar(400)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@TenBanner` | `nvarchar(400)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@TongSoBaiViet` | `int(4)` | No |
| `@SoThuTuTheoNgay` | `bigint(8)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@bannertype` | `int(4)` | No |
| `@username` | `nvarchar(400)` | No |
| `@salename` | `nvarchar(400)` | No |
| `@email` | `nvarchar(400)` | No |
| `@LastTimeCalc` | `datetime(8)` | No |
| `@sys_date` | `datetime(8)` | No |
| `@IsReady` | `int(4)` | No |
| `@ProductUnitID` | `int(4)` | No |
| `@ProductUnitName` | `nvarchar(400)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@BannerTypeName` | `nvarchar(400)` | No |
| `@CampainStatus` | `nvarchar(400)` | No |
| `@BannerStatus` | `nvarchar(400)` | No |
| `@IsNoiBo` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChay_bk] 	
@ThucChayID nvarchar (200) ,	
@SoHopDong nvarchar (200) ,	
@DanhsachDmBookingREF nvarchar (200) ,	
@DmSanPhamREF int ,	
@TenSanPham nvarchar (200) ,	
@DmNhomWebsiteREF int ,	
@TenNhomWebsite nvarchar (200) ,	
@DmWebsiteREF int ,	
@TenWebsite nvarchar (200) ,	
@DmChienDichREF int ,	
@TenChienDich nvarchar (200) ,	
@DmBannerREF int ,	
@TenBanner nvarchar (200) ,	
@NgayThucHien datetime ,	
@TongViewThucChay int ,	
@TongClickThucChay int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int ,	
@TongSoBaiViet int ,	
@SoThuTuTheoNgay bigint ,	
@TypeProduct int ,	
@bannertype int ,	
@username nvarchar (200) ,	
@salename nvarchar (200) ,	
@email nvarchar (200) ,	
@LastTimeCalc datetime ,	
@sys_date datetime ,	
@IsReady int ,	
@ProductUnitID int ,	
@ProductUnitName nvarchar (200) ,	
@HopDongChiTietREF int ,	
@BannerTypeName nvarchar (200) ,	
@CampainStatus nvarchar (200) ,	
@BannerStatus nvarchar (200) ,	
@IsNoiBo int 	
As 	
INSERT INTO [dbo].[ThucChay] (	
[ThucChayID],	
[SoHopDong],	
[DanhsachDmBookingREF],	
[DmSanPhamREF],	
[TenSanPham],	
[DmNhomWebsiteREF],	
[TenNhomWebsite],	
[DmWebsiteREF],	
[TenWebsite],	
[DmChienDichREF],	
[TenChienDich],	
[DmBannerREF],	
[TenBanner],	
[NgayThucHien],	
[TongViewThucChay],	
[TongClickThucChay],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus],	
[TongSoBaiViet],	
[SoThuTuTheoNgay],	
[TypeProduct],	
[bannertype],	
[username],	
[salename],	
[email],	
[LastTimeCalc],	
[sys_date],	
[IsReady],	
[ProductUnitID],	
[ProductUnitName],	
[HopDongChiTietREF],	
[BannerTypeName],	
[CampainStatus],	
[BannerStatus],	
[IsNoiBo])	
Values 	
(	
@ThucChayID,	
@SoHopDong,	
@DanhsachDmBookingREF,	
@DmSanPhamREF,	
@TenSanPham,	
@DmNhomWebsiteREF,	
@TenNhomWebsite,	
@DmWebsiteREF,	
@TenWebsite,	
@DmChienDichREF,	
@TenChienDich,	
@DmBannerREF,	
@TenBanner,	
@NgayThucHien,	
@TongViewThucChay,	
@TongClickThucChay,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus,	
@TongSoBaiViet,	
@SoThuTuTheoNgay,	
@TypeProduct,	
@bannertype,	
@username,	
@salename,	
@email,	
@LastTimeCalc,	
@sys_date,	
@IsReady,	
@ProductUnitID,	
@ProductUnitName,	
@HopDongChiTietREF,	
@BannerTypeName,	
@CampainStatus,	
@BannerStatus,	
@IsNoiBo)

```
