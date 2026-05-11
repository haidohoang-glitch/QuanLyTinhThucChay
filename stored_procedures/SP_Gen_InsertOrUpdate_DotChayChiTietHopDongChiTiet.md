# Stored Procedure: `Gen_InsertOrUpdate_DotChayChiTietHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:40:33.987000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.030000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayChiTietHopDongChiTietID` | `int(4)` | No |
| `@DotChayHopDongChitietREF` | `int(4)` | No |
| `@BookingREF` | `int(4)` | No |
| `@SoLuong` | `float(8)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@VungMienID` | `int(4)` | No |
| `@TenVungMien` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_DotChayChiTietHopDongChiTiet] 	
@DotChayChiTietHopDongChiTietID int ,	
@DotChayHopDongChitietREF int ,	
@BookingREF int ,	
@SoLuong float ,	
@ThoiGianBatDau datetime ,	
@ThoiGianKetThuc datetime ,	
@VungMienID int ,	
@TenVungMien nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [DotChayChiTietHopDongChiTiet] where [DotChayChiTietHopDongChiTietID] = @DotChayChiTietHopDongChiTietID))	
UPDATE [dbo].[DotChayChiTietHopDongChiTiet] SET 	
[DotChayHopDongChitietREF] = @DotChayHopDongChitietREF,	
[BookingREF] = @BookingREF,	
[SoLuong] = @SoLuong,	
[ThoiGianBatDau] = @ThoiGianBatDau,	
[ThoiGianKetThuc] = @ThoiGianKetThuc,	
[VungMienID] = @VungMienID,	
[TenVungMien] = @TenVungMien,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [DotChayChiTietHopDongChiTietID] = @DotChayChiTietHopDongChiTietID	
else 	
INSERT INTO [dbo].[DotChayChiTietHopDongChiTiet] (	
[DotChayChiTietHopDongChiTietID],	
[DotChayHopDongChitietREF],	
[BookingREF],	
[SoLuong],	
[ThoiGianBatDau],	
[ThoiGianKetThuc],	
[VungMienID],	
[TenVungMien],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@DotChayChiTietHopDongChiTietID,	
@DotChayHopDongChitietREF,	
@BookingREF,	
@SoLuong,	
@ThoiGianBatDau,	
@ThoiGianKetThuc,	
@VungMienID,	
@TenVungMien,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
