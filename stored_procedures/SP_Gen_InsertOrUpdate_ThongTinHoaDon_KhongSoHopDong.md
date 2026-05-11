# Stored Procedure: `Gen_InsertOrUpdate_ThongTinHoaDon_KhongSoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-09 10:18:35.283000
- **Ngày sửa cuối**: 2015-06-09 10:18:35.283000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinHoaDon_KhongSoHopDongID` | `bigint(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHoaDon` | `nvarchar(400)` | No |
| `@NgayXuatHoaDon` | `datetime(8)` | No |
| `@GiaTri` | `int(4)` | No |
| `@NgayTraHoaDon` | `datetime(8)` | No |
| `@SoBangThongKe` | `nvarchar(400)` | No |
| `@TaiKhoanKhachHang` | `nvarchar(400)` | No |
| `@IsDoanhThuKhac` | `int(4)` | No |
| `@IsHoaDonGiamTru` | `int(4)` | No |
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
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinHoaDon_KhongSoHopDong] 	
@ThongTinHoaDon_KhongSoHopDongID bigint ,	
@HopDongREF int ,	
@SoHoaDon nvarchar (200) ,	
@NgayXuatHoaDon datetime ,	
@GiaTri int ,	
@NgayTraHoaDon datetime ,	
@SoBangThongKe nvarchar (200) ,	
@TaiKhoanKhachHang nvarchar (200) ,	
@IsDoanhThuKhac int ,	
@IsHoaDonGiamTru int ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [ThongTinHoaDon_KhongSoHopDong] where [ThongTinHoaDon_KhongSoHopDongID] = @ThongTinHoaDon_KhongSoHopDongID))	
UPDATE [dbo].[ThongTinHoaDon_KhongSoHopDong] SET 	
[HopDongREF] = @HopDongREF,	
[SoHoaDon] = @SoHoaDon,	
[NgayXuatHoaDon] = @NgayXuatHoaDon,	
[GiaTri] = @GiaTri,	
[NgayTraHoaDon] = @NgayTraHoaDon,	
[SoBangThongKe] = @SoBangThongKe,	
[TaiKhoanKhachHang] = @TaiKhoanKhachHang,	
[IsDoanhThuKhac] = @IsDoanhThuKhac,	
[IsHoaDonGiamTru] = @IsHoaDonGiamTru,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [ThongTinHoaDon_KhongSoHopDongID] = @ThongTinHoaDon_KhongSoHopDongID	
else 	
INSERT INTO [dbo].[ThongTinHoaDon_KhongSoHopDong] (	
[ThongTinHoaDon_KhongSoHopDongID],	
[HopDongREF],	
[SoHoaDon],	
[NgayXuatHoaDon],	
[GiaTri],	
[NgayTraHoaDon],	
[SoBangThongKe],	
[TaiKhoanKhachHang],	
[IsDoanhThuKhac],	
[IsHoaDonGiamTru],	
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
@ThongTinHoaDon_KhongSoHopDongID,	
@HopDongREF,	
@SoHoaDon,	
@NgayXuatHoaDon,	
@GiaTri,	
@NgayTraHoaDon,	
@SoBangThongKe,	
@TaiKhoanKhachHang,	
@IsDoanhThuKhac,	
@IsHoaDonGiamTru,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)
```
