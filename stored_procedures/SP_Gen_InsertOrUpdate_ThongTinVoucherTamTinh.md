# Stored Procedure: `Gen_InsertOrUpdate_ThongTinVoucherTamTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-01-08 10:16:25.600000
- **Ngày sửa cuối**: 2016-01-08 10:41:37.300000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinVoucherTamTinhID` | `bigint(8)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@DmKhachHangREF` | `int(4)` | No |
| `@TenKhachHang` | `nvarchar(400)` | No |
| `@TenNguoiLienHe` | `nvarchar(400)` | No |
| `@EmailNguoiLienHe` | `nvarchar(400)` | No |
| `@ChucVuNguoiLienHe` | `nvarchar(400)` | No |
| `@SoDienThoaiNguoiLienHe` | `nvarchar(400)` | No |
| `@GiaTriVoucherTamTinh` | `float(8)` | No |
| `@DmKhachHangLienHeREF` | `int(4)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThongTinVoucherTamTinh] 	
@ThongTinVoucherTamTinhID bigint ,	
@HopDongREF int ,	
@SoHopDong nvarchar (200) ,	
@DmKhachHangREF int ,	
@TenKhachHang nvarchar (200) ,	
@TenNguoiLienHe nvarchar (200) ,	
@EmailNguoiLienHe nvarchar (200) ,	
@ChucVuNguoiLienHe nvarchar (200) ,	
@SoDienThoaiNguoiLienHe nvarchar (200) ,	
@GiaTriVoucherTamTinh float ,	
@DmKhachHangLienHeREF int ,	
@CreatedAt datetime ,	
@CreatedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@DeletedStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [ThongTinVoucherTamTinh] where [ThongTinVoucherTamTinhID] = @ThongTinVoucherTamTinhID))	
UPDATE [dbo].[ThongTinVoucherTamTinh] SET 	
[HopDongREF] = @HopDongREF,	
[SoHopDong] = @SoHopDong,	
[DmKhachHangREF] = @DmKhachHangREF,	
[TenKhachHang] = @TenKhachHang,	
[TenNguoiLienHe] = @TenNguoiLienHe,	
[EmailNguoiLienHe] = @EmailNguoiLienHe,	
[ChucVuNguoiLienHe] = @ChucVuNguoiLienHe,	
[SoDienThoaiNguoiLienHe] = @SoDienThoaiNguoiLienHe,	
[GiaTriVoucherTamTinh] = @GiaTriVoucherTamTinh,	
[DmKhachHangLienHeREF] = @DmKhachHangLienHeREF,	
[CreatedAt] = @CreatedAt,	
[CreatedBy] = @CreatedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[DeletedStatus] = @DeletedStatus,	
[RecordStatus] = @RecordStatus where [ThongTinVoucherTamTinhID] = @ThongTinVoucherTamTinhID	
else 	
INSERT INTO [dbo].[ThongTinVoucherTamTinh] (	
[ThongTinVoucherTamTinhID],	
[HopDongREF],	
[SoHopDong],	
[DmKhachHangREF],	
[TenKhachHang],	
[TenNguoiLienHe],	
[EmailNguoiLienHe],	
[ChucVuNguoiLienHe],	
[SoDienThoaiNguoiLienHe],	
[GiaTriVoucherTamTinh],	
[DmKhachHangLienHeREF],	
[CreatedAt],	
[CreatedBy],	
[LastModifiedAt],	
[LastModifiedBy],	
[DeletedStatus],	
[RecordStatus])	
Values 	
(	
@ThongTinVoucherTamTinhID,	
@HopDongREF,	
@SoHopDong,	
@DmKhachHangREF,	
@TenKhachHang,	
@TenNguoiLienHe,	
@EmailNguoiLienHe,	
@ChucVuNguoiLienHe,	
@SoDienThoaiNguoiLienHe,	
@GiaTriVoucherTamTinh,	
@DmKhachHangLienHeREF,	
@CreatedAt,	
@CreatedBy,	
@LastModifiedAt,	
@LastModifiedBy,	
@DeletedStatus,	
@RecordStatus)
```
