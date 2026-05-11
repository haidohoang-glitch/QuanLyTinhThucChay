# Stored Procedure: `Gen_InsertOrUpdate_HopDongAttachFileBanCung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 17:26:56.240000
- **Ngày sửa cuối**: 2016-09-14 14:06:04.620000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongAttachFileBanCungID` | `int(4)` | No |
| `@HopDongAttachFileREF` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@NgayNhanBanCung` | `datetime(8)` | No |
| `@NgayNhanBanFax` | `datetime(8)` | No |
| `@NgayChuyenChoKeToan` | `datetime(8)` | No |
| `@KhongTheNhapBanCung` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@CanLayBangKeThucChayYN` | `smallint(2)` | No |
| `@NgayHenTraBanCung` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongAttachFileBanCung] 	
@HopDongAttachFileBanCungID int ,	
@HopDongAttachFileREF int ,	
@HopDongREF int ,	
@NgayNhanBanCung datetime ,	
@NgayNhanBanFax datetime ,	
@NgayChuyenChoKeToan datetime ,	
@KhongTheNhapBanCung int ,	
@GhiChu nvarchar (200) ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus INT,
@CanLayBangKeThucChayYN SMALLINT,
@NgayHenTraBanCung DATETIME
As 	
if(exists(select * from [HopDongAttachFileBanCung] where [HopDongAttachFileBanCungID] = @HopDongAttachFileBanCungID))	
UPDATE [dbo].[HopDongAttachFileBanCung] SET 	
[HopDongAttachFileREF] = @HopDongAttachFileREF,	
[HopDongREF] = @HopDongREF,	
[NgayNhanBanCung] = @NgayNhanBanCung,	
[NgayNhanBanFax] = @NgayNhanBanFax,	
[NgayChuyenChoKeToan] = @NgayChuyenChoKeToan,	
[KhongTheNhapBanCung] = @KhongTheNhapBanCung,	
[GhiChu] = @GhiChu,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus,
[CanLayBangKeThucChayYN] = @CanLayBangKeThucChayYN,
[NgayHenTraBanCung] = @NgayHenTraBanCung
WHERE [HopDongAttachFileBanCungID] = @HopDongAttachFileBanCungID	
else 	
INSERT INTO [dbo].[HopDongAttachFileBanCung] (	
[HopDongAttachFileBanCungID],	
[HopDongAttachFileREF],	
[HopDongREF],	
[NgayNhanBanCung],	
[NgayNhanBanFax],	
[NgayChuyenChoKeToan],	
[KhongTheNhapBanCung],	
[GhiChu],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus],
[CanLayBangKeThucChayYN],
[NgayHenTraBanCung])	
Values 	
(	
@HopDongAttachFileBanCungID,	
@HopDongAttachFileREF,	
@HopDongREF,	
@NgayNhanBanCung,	
@NgayNhanBanFax,	
@NgayChuyenChoKeToan,	
@KhongTheNhapBanCung,	
@GhiChu,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus,
@CanLayBangKeThucChayYN,
@NgayHenTraBanCung)
```
