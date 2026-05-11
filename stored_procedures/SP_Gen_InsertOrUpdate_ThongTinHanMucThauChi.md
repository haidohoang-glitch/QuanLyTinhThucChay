# Stored Procedure: `Gen_InsertOrUpdate_ThongTinHanMucThauChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-14 18:20:15.370000
- **Ngày sửa cuối**: 2016-03-14 18:20:15.370000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanVienREF` | `int(4)` | No |
| `@TenNhanVien` | `nvarchar(400)` | No |
| `@TenPhongBan` | `nvarchar(400)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@TenBoPhan` | `nvarchar(400)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@TenNhom` | `nvarchar(400)` | No |
| `@DmNhomREF` | `int(4)` | No |
| `@HanMucThauChi` | `float(8)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinHanMucThauChi] 	
@DmNhanVienREF int ,	
@TenNhanVien nvarchar (200) ,	
@TenPhongBan nvarchar (200) ,	
@DmPhongBanREF int ,	
@TenBoPhan nvarchar (200) ,	
@DmBoPhanREF int ,	
@TenNhom nvarchar (200) ,	
@DmNhomREF int ,	
@HanMucThauChi float ,	
@CreatedAt datetime ,	
@CreatedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@DeletedStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [ThongTinHanMucThauChi] where [DmNhanVienREF] = @DmNhanVienREF))	
UPDATE [dbo].[ThongTinHanMucThauChi] SET 	
[TenNhanVien] = @TenNhanVien,	
[TenPhongBan] = @TenPhongBan,	
[DmPhongBanREF] = @DmPhongBanREF,	
[TenBoPhan] = @TenBoPhan,	
[DmBoPhanREF] = @DmBoPhanREF,	
[TenNhom] = @TenNhom,	
[DmNhomREF] = @DmNhomREF,	
[HanMucThauChi] = @HanMucThauChi,	
[CreatedAt] = @CreatedAt,	
[CreatedBy] = @CreatedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[DeletedStatus] = @DeletedStatus,	
[RecordStatus] = @RecordStatus where [DmNhanVienREF] = @DmNhanVienREF	
else 	
INSERT INTO [dbo].[ThongTinHanMucThauChi] (	
[DmNhanVienREF],	
[TenNhanVien],	
[TenPhongBan],	
[DmPhongBanREF],	
[TenBoPhan],	
[DmBoPhanREF],	
[TenNhom],	
[DmNhomREF],	
[HanMucThauChi],	
[CreatedAt],	
[CreatedBy],	
[LastModifiedAt],	
[LastModifiedBy],	
[DeletedStatus],	
[RecordStatus])	
Values 	
(	
@DmNhanVienREF,	
@TenNhanVien,	
@TenPhongBan,	
@DmPhongBanREF,	
@TenBoPhan,	
@DmBoPhanREF,	
@TenNhom,	
@DmNhomREF,	
@HanMucThauChi,	
@CreatedAt,	
@CreatedBy,	
@LastModifiedAt,	
@LastModifiedBy,	
@DeletedStatus,	
@RecordStatus)
```
