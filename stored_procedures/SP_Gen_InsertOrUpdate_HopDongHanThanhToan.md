# Stored Procedure: `Gen_InsertOrUpdate_HopDongHanThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:42:24.240000
- **Ngày sửa cuối**: 2016-09-14 15:29:55.163000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongHanThanhToanID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@LanThanhToan` | `nvarchar(400)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@SoTien` | `float(8)` | No |
| `@NgayDuDinhThanhToan` | `datetime(8)` | No |
| `@NgayDuKienXuatHoaDon` | `datetime(8)` | No |
| `@GiaTriDaThanhToan` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Active` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@HinhThucThanhToan` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongHanThanhToan] 	
@HopDongHanThanhToanID int ,	
@HopDongREF int ,	
@LanThanhToan nvarchar (200) ,	
@NgayThanhToan datetime ,	
@SoTien float ,	
@NgayDuDinhThanhToan datetime ,	
@NgayDuKienXuatHoaDon datetime ,	
@GiaTriDaThanhToan int ,	
@GhiChu nvarchar (200) ,	
@Active nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int ,
@HinhThucThanhToan INT
As 	
if(exists(select * from [HopDongHanThanhToan] where [HopDongHanThanhToanID] = @HopDongHanThanhToanID))	
UPDATE [dbo].[HopDongHanThanhToan] SET 	
[HopDongREF] = @HopDongREF,	
[LanThanhToan] = @LanThanhToan,	
[NgayThanhToan] = @NgayThanhToan,	
[SoTien] = @SoTien,	
[NgayDuDinhThanhToan] = @NgayDuDinhThanhToan,	
[NgayDuKienXuatHoaDon] = @NgayDuKienXuatHoaDon,	
[GiaTriDaThanhToan] = @GiaTriDaThanhToan,	
[GhiChu] = @GhiChu,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus,
[HinhThucThanhToan] = @HinhThucThanhToan 
WHERE [HopDongHanThanhToanID] = @HopDongHanThanhToanID	
else 	
INSERT INTO [dbo].[HopDongHanThanhToan] (	
[HopDongHanThanhToanID],	
[HopDongREF],	
[LanThanhToan],	
[NgayThanhToan],	
[SoTien],	
[NgayDuDinhThanhToan],	
[NgayDuKienXuatHoaDon],	
[GiaTriDaThanhToan],	
[GhiChu],	
[Active],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus],
[HinhThucThanhToan])	
Values 	
(	
@HopDongHanThanhToanID,	
@HopDongREF,	
@LanThanhToan,	
@NgayThanhToan,	
@SoTien,	
@NgayDuDinhThanhToan,	
@NgayDuKienXuatHoaDon,	
@GiaTriDaThanhToan,	
@GhiChu,	
@Active,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus,
@HinhThucThanhToan)
```
