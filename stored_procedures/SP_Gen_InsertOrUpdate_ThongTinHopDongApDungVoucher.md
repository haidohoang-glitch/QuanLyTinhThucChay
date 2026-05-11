# Stored Procedure: `Gen_InsertOrUpdate_ThongTinHopDongApDungVoucher`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-01-08 10:40:01.827000
- **Ngày sửa cuối**: 2016-01-08 10:40:01.827000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinHopDongApDungVoucherID` | `bigint(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@VoucherREF` | `nvarchar(400)` | No |
| `@MaVoucher` | `nvarchar(400)` | No |
| `@GiaTriVoucherTamTinh` | `float(8)` | No |
| `@GiaTriVouCherHieuLuc` | `float(8)` | No |
| `@NgayHieuLucVoucher` | `datetime(8)` | No |
| `@NgayHetHanVoucher` | `datetime(8)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@LastMofiedBy` | `nvarchar(400)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinHopDongApDungVoucher] 	
@ThongTinHopDongApDungVoucherID bigint ,	
@HopDongREF int ,	
@SoHopDong nvarchar (200) ,	
@VoucherREF nvarchar (200) ,	
@MaVoucher nvarchar (200) ,	
@GiaTriVoucherTamTinh float ,	
@GiaTriVouCherHieuLuc float ,	
@NgayHieuLucVoucher datetime ,	
@NgayHetHanVoucher datetime ,	
@CreatedAt datetime ,	
@CreatedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@LastMofiedBy nvarchar (200) ,	
@DeletedStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [ThongTinHopDongApDungVoucher] where [ThongTinHopDongApDungVoucherID] = @ThongTinHopDongApDungVoucherID))	
UPDATE [dbo].[ThongTinHopDongApDungVoucher] SET 	
[HopDongREF] = @HopDongREF,	
[SoHopDong] = @SoHopDong,	
[VoucherREF] = @VoucherREF,	
[MaVoucher] = @MaVoucher,	
[GiaTriVoucherTamTinh] = @GiaTriVoucherTamTinh,	
[GiaTriVouCherHieuLuc] = @GiaTriVouCherHieuLuc,	
[NgayHieuLucVoucher] = @NgayHieuLucVoucher,	
[NgayHetHanVoucher] = @NgayHetHanVoucher,	
[CreatedAt] = @CreatedAt,	
[CreatedBy] = @CreatedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[LastMofiedBy] = @LastMofiedBy,	
[DeletedStatus] = @DeletedStatus,	
[RecordStatus] = @RecordStatus where [ThongTinHopDongApDungVoucherID] = @ThongTinHopDongApDungVoucherID	
else 	
INSERT INTO [dbo].[ThongTinHopDongApDungVoucher] (	
[ThongTinHopDongApDungVoucherID],	
[HopDongREF],	
[SoHopDong],	
[VoucherREF],	
[MaVoucher],	
[GiaTriVoucherTamTinh],	
[GiaTriVouCherHieuLuc],	
[NgayHieuLucVoucher],	
[NgayHetHanVoucher],	
[CreatedAt],	
[CreatedBy],	
[LastModifiedAt],	
[LastMofiedBy],	
[DeletedStatus],	
[RecordStatus])	
Values 	
(	
@ThongTinHopDongApDungVoucherID,	
@HopDongREF,	
@SoHopDong,	
@VoucherREF,	
@MaVoucher,	
@GiaTriVoucherTamTinh,	
@GiaTriVouCherHieuLuc,	
@NgayHieuLucVoucher,	
@NgayHetHanVoucher,	
@CreatedAt,	
@CreatedBy,	
@LastModifiedAt,	
@LastMofiedBy,	
@DeletedStatus,	
@RecordStatus)
```
