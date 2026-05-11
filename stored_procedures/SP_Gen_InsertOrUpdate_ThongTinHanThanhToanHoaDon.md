# Stored Procedure: `Gen_InsertOrUpdate_ThongTinHanThanhToanHoaDon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:23:46.527000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.837000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@HopDongHanThanhToanREF` | `int(4)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@LanThanhToan` | `nvarchar(400)` | No |
| `@NgayDuKienXuatHoaDon` | `datetime(8)` | No |
| `@SoTien` | `float(8)` | No |
| `@ThongTinHoaDonREF` | `int(4)` | No |
| `@GiaTriHoaDon` | `int(4)` | No |
| `@NgayXuatHoaDon` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinHanThanhToanHoaDon] 	
@HopDongREF int ,	
@HopDongHanThanhToanREF int ,	
@NgayThanhToan datetime ,	
@LanThanhToan nvarchar (200) ,	
@NgayDuKienXuatHoaDon datetime ,	
@SoTien float ,	
@ThongTinHoaDonREF int ,	
@GiaTriHoaDon int ,	
@NgayXuatHoaDon datetime ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
INSERT INTO [dbo].[ThongTinHanThanhToanHoaDon] (	
[HopDongREF],	
[HopDongHanThanhToanREF],	
[NgayThanhToan],	
[LanThanhToan],	
[NgayDuKienXuatHoaDon],	
[SoTien],	
[ThongTinHoaDonREF],	
[GiaTriHoaDon],	
[NgayXuatHoaDon],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@HopDongREF,	
@HopDongHanThanhToanREF,	
@NgayThanhToan,	
@LanThanhToan,	
@NgayDuKienXuatHoaDon,	
@SoTien,	
@ThongTinHoaDonREF,	
@GiaTriHoaDon,	
@NgayXuatHoaDon,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
