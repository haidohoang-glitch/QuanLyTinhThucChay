# Stored Procedure: `Gen_InsertOrUpdate_ThucTreoVungMien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:27:15.170000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucTreoVungMienID` | `int(4)` | No |
| `@VungMienID` | `int(4)` | No |
| `@BookingREF` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinhREF` | `int(4)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucTreoVungMien] 	
@ThucTreoVungMienID int ,	
@VungMienID int ,	
@BookingREF int ,	
@SoLuong int ,	
@DonViTinhREF int ,	
@ThoiGianBatDau datetime ,	
@ThoiGianKetThuc datetime ,	
@DmBannerREF int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [ThucTreoVungMien] where [ThucTreoVungMienID] = @ThucTreoVungMienID))	
UPDATE [dbo].[ThucTreoVungMien] SET 	
[VungMienID] = @VungMienID,	
[BookingREF] = @BookingREF,	
[SoLuong] = @SoLuong,	
[DonViTinhREF] = @DonViTinhREF,	
[ThoiGianBatDau] = @ThoiGianBatDau,	
[ThoiGianKetThuc] = @ThoiGianKetThuc,	
[DmBannerREF] = @DmBannerREF,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [ThucTreoVungMienID] = @ThucTreoVungMienID	
else 	
INSERT INTO [dbo].[ThucTreoVungMien] (	
[ThucTreoVungMienID],	
[VungMienID],	
[BookingREF],	
[SoLuong],	
[DonViTinhREF],	
[ThoiGianBatDau],	
[ThoiGianKetThuc],	
[DmBannerREF],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@ThucTreoVungMienID,	
@VungMienID,	
@BookingREF,	
@SoLuong,	
@DonViTinhREF,	
@ThoiGianBatDau,	
@ThoiGianKetThuc,	
@DmBannerREF,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
