# Stored Procedure: `Gen_InsertOrUpdate_ThucTreoHopDongChiTietAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-08 15:27:13.577000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.097000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucTreoHopDongChiTietAdmarketID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@CampaignID` | `int(4)` | No |
| `@CampaignName` | `nvarchar(400)` | No |
| `@TK_AdmarketID` | `int(4)` | No |
| `@TK_Admarket` | `nvarchar(400)` | No |
| `@NgayNhanVienYeuCau` | `datetime(8)` | No |
| `@RetryCount` | `int(4)` | No |
| `@ThoiGianCapNhat` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecodStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucTreoHopDongChiTietAdmarket] 	
@ThucTreoHopDongChiTietAdmarketID int ,	
@HopDongChiTietREF int ,	
@HopDongREF int ,	
@SoHopDong nvarchar (200) ,	
@DmSanPhamREF int ,	
@CampaignID int ,	
@CampaignName nvarchar (200) ,	
@TK_AdmarketID int ,	
@TK_Admarket nvarchar (200) ,	
@NgayNhanVienYeuCau datetime ,	
@RetryCount int ,	
@ThoiGianCapNhat datetime ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecodStatus int 	
As 	
if(exists(select * from [ThucTreoHopDongChiTietAdmarket] where [ThucTreoHopDongChiTietAdmarketID] = @ThucTreoHopDongChiTietAdmarketID))	
UPDATE [dbo].[ThucTreoHopDongChiTietAdmarket] SET 	
[HopDongChiTietREF] = @HopDongChiTietREF,	
[HopDongREF] = @HopDongREF,	
[SoHopDong] = @SoHopDong,	
[DmSanPhamREF] = @DmSanPhamREF,	
[CampaignID] = @CampaignID,	
[CampaignName] = @CampaignName,	
[TK_AdmarketID] = @TK_AdmarketID,	
[TK_Admarket] = @TK_Admarket,	
[NgayNhanVienYeuCau] = @NgayNhanVienYeuCau,	
[RetryCount] = @RetryCount,	
[ThoiGianCapNhat] = @ThoiGianCapNhat,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecodStatus] = @RecodStatus where [ThucTreoHopDongChiTietAdmarketID] = @ThucTreoHopDongChiTietAdmarketID	
else 	
INSERT INTO [dbo].[ThucTreoHopDongChiTietAdmarket] (	
[ThucTreoHopDongChiTietAdmarketID],	
[HopDongChiTietREF],	
[HopDongREF],	
[SoHopDong],	
[DmSanPhamREF],	
[CampaignID],	
[CampaignName],	
[TK_AdmarketID],	
[TK_Admarket],	
[NgayNhanVienYeuCau],	
[RetryCount],	
[ThoiGianCapNhat],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecodStatus])	
Values 	
(	
@ThucTreoHopDongChiTietAdmarketID,	
@HopDongChiTietREF,	
@HopDongREF,	
@SoHopDong,	
@DmSanPhamREF,	
@CampaignID,	
@CampaignName,	
@TK_AdmarketID,	
@TK_Admarket,	
@NgayNhanVienYeuCau,	
@RetryCount,	
@ThoiGianCapNhat,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecodStatus)

```
