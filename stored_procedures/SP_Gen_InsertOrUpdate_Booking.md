# Stored Procedure: `Gen_InsertOrUpdate_Booking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-03 10:00:42.167000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.437000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@BookingID` | `int(4)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@status` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@SoLuongTheoDV` | `int(4)` | No |
| `@DonViTinh` | `int(4)` | No |
| `@soluong` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@HinhThucSP` | `int(4)` | No |
| `@TenHinhSanPham` | `nvarchar(400)` | No |
| `@MaSanPham` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@createdby` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_Booking] 	
@BookingID int ,	
@NgayBatDau datetime ,	
@NgayKetThuc datetime ,	
@status int ,	
@SoHopDong nvarchar (200) ,	
@SoLuongTheoDV int ,	
@DonViTinh int ,	
@soluong int ,	
@TenWebsite nvarchar (200) ,	
@DmWebsiteREF int ,	
@HinhThucSP int ,	
@TenHinhSanPham nvarchar (200) ,	
@MaSanPham int ,	
@TenSanPham nvarchar (200) ,	
@createdby nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [Booking] where [BookingID] = @BookingID and [HinhThucSP] = @HinhThucSP and [MaSanPham] = @MaSanPham))	
UPDATE [dbo].[Booking] SET 	
[NgayBatDau] = @NgayBatDau,	
[NgayKetThuc] = @NgayKetThuc,	
[status] = @status,	
[SoHopDong] = @SoHopDong,	
[SoLuongTheoDV] = @SoLuongTheoDV,	
[DonViTinh] = @DonViTinh,	
[soluong] = @soluong,	
[TenWebsite] = @TenWebsite,	
[DmWebsiteREF] = @DmWebsiteREF,	
[TenHinhSanPham] = @TenHinhSanPham,	
[TenSanPham] = @TenSanPham,	
[createdby] = @createdby,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [BookingID] = @BookingID and [HinhThucSP] = @HinhThucSP and [MaSanPham] = @MaSanPham	
else 	
INSERT INTO [dbo].[Booking] (	
[BookingID],	
[NgayBatDau],	
[NgayKetThuc],	
[status],	
[SoHopDong],	
[SoLuongTheoDV],	
[DonViTinh],	
[soluong],	
[TenWebsite],	
[DmWebsiteREF],	
[HinhThucSP],	
[TenHinhSanPham],	
[MaSanPham],	
[TenSanPham],	
[createdby],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@BookingID,	
@NgayBatDau,	
@NgayKetThuc,	
@status,	
@SoHopDong,	
@SoLuongTheoDV,	
@DonViTinh,	
@soluong,	
@TenWebsite,	
@DmWebsiteREF,	
@HinhThucSP,	
@TenHinhSanPham,	
@MaSanPham,	
@TenSanPham,	
@createdby,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
