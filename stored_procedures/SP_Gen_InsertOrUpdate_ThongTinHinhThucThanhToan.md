# Stored Procedure: `Gen_InsertOrUpdate_ThongTinHinhThucThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-05-11 16:53:50.363000
- **Ngày sửa cuối**: 2016-05-11 16:53:50.363000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinHinhThucThanhToanID` | `bigint(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@LoaiHinhThucThanhToan` | `int(4)` | No |
| `@TenLoaiHinhThucThanhToan` | `nvarchar(400)` | No |
| `@SoLanThanhToan` | `int(4)` | No |
| `@NgayXuatHoaDonLanDau` | `datetime(8)` | No |
| `@SoNgayPhaiThanhToanSauXHD` | `int(4)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@DeletedStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinHinhThucThanhToan] 	
@ThongTinHinhThucThanhToanID bigint ,	
@HopDongREF int ,	
@SoHopDong nvarchar (200) ,	
@LoaiHinhThucThanhToan int ,	
@TenLoaiHinhThucThanhToan nvarchar (200) ,	
@SoLanThanhToan int ,	
@NgayXuatHoaDonLanDau datetime ,	
@SoNgayPhaiThanhToanSauXHD int ,	
@CreatedAt datetime ,	
@CreatedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@DeletedStatus int 	
As 	
if(exists(select * from [ThongTinHinhThucThanhToan] where [ThongTinHinhThucThanhToanID] = @ThongTinHinhThucThanhToanID))	
UPDATE [dbo].[ThongTinHinhThucThanhToan] SET 	
[HopDongREF] = @HopDongREF,	
[SoHopDong] = @SoHopDong,	
[LoaiHinhThucThanhToan] = @LoaiHinhThucThanhToan,	
[TenLoaiHinhThucThanhToan] = @TenLoaiHinhThucThanhToan,	
[SoLanThanhToan] = @SoLanThanhToan,	
[NgayXuatHoaDonLanDau] = @NgayXuatHoaDonLanDau,	
[SoNgayPhaiThanhToanSauXHD] = @SoNgayPhaiThanhToanSauXHD,	
[CreatedAt] = @CreatedAt,	
[CreatedBy] = @CreatedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[DeletedStatus] = @DeletedStatus where [ThongTinHinhThucThanhToanID] = @ThongTinHinhThucThanhToanID	
else 	
INSERT INTO [dbo].[ThongTinHinhThucThanhToan] (	
[ThongTinHinhThucThanhToanID],	
[HopDongREF],	
[SoHopDong],	
[LoaiHinhThucThanhToan],	
[TenLoaiHinhThucThanhToan],	
[SoLanThanhToan],	
[NgayXuatHoaDonLanDau],	
[SoNgayPhaiThanhToanSauXHD],	
[CreatedAt],	
[CreatedBy],	
[LastModifiedAt],	
[LastModifiedBy],	
[DeletedStatus])	
Values 	
(	
@ThongTinHinhThucThanhToanID,	
@HopDongREF,	
@SoHopDong,	
@LoaiHinhThucThanhToan,	
@TenLoaiHinhThucThanhToan,	
@SoLanThanhToan,	
@NgayXuatHoaDonLanDau,	
@SoNgayPhaiThanhToanSauXHD,	
@CreatedAt,	
@CreatedBy,	
@LastModifiedAt,	
@LastModifiedBy,	
@DeletedStatus)
```
