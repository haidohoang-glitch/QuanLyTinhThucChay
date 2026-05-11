# Stored Procedure: `Gen_InsertOrUpdate_KhachHangNguoiLienHe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-09-19 14:35:09.280000
- **Ngày sửa cuối**: 2014-11-19 12:16:52.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangNguoiLienHeID` | `int(4)` | No |
| `@KhachHangThongTinChungFK` | `int(4)` | No |
| `@TenNguoiLienHe` | `nvarchar(400)` | No |
| `@AccountNguoiLienHe` | `nvarchar(400)` | No |
| `@ChucVu` | `nvarchar(400)` | No |
| `@Email` | `nvarchar(400)` | No |
| `@Email2` | `nvarchar(400)` | No |
| `@Mobile` | `nvarchar(400)` | No |
| `@Mobile2` | `nvarchar(400)` | No |
| `@SoDienThoai` | `nvarchar(400)` | No |
| `@SoFax` | `nvarchar(400)` | No |
| `@DiaChiLienHe` | `nvarchar(400)` | No |
| `@NgaySinh` | `datetime(8)` | No |
| `@GioiTinh` | `nvarchar(400)` | No |
| `@ThongTinKhac` | `nvarchar(400)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_KhachHangNguoiLienHe] 	
@KhachHangNguoiLienHeID int ,	
@KhachHangThongTinChungFK int ,	
@TenNguoiLienHe nvarchar (200) ,	
@AccountNguoiLienHe nvarchar (200) ,	
@ChucVu nvarchar (200) ,	
@Email nvarchar (200) ,	
@Email2 nvarchar (200) ,	
@Mobile nvarchar (200) ,	
@Mobile2 nvarchar (200) ,	
@SoDienThoai nvarchar (200) ,	
@SoFax nvarchar (200) ,	
@DiaChiLienHe nvarchar (200) ,	
@NgaySinh datetime ,	
@GioiTinh nvarchar (200) ,	
@ThongTinKhac nvarchar (200) ,	
@Active int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [KhachHangNguoiLienHe] where [KhachHangNguoiLienHeID] = @KhachHangNguoiLienHeID))	
UPDATE [dbo].[KhachHangNguoiLienHe] SET 	
[KhachHangThongTinChungFK] = @KhachHangThongTinChungFK,	
[TenNguoiLienHe] = @TenNguoiLienHe,	
[AccountNguoiLienHe] = @AccountNguoiLienHe,	
[ChucVu] = @ChucVu,	
[Email] = @Email,	
[Email2] = @Email2,	
[Mobile] = @Mobile,	
[Mobile2] = @Mobile2,	
[SoDienThoai] = @SoDienThoai,	
[SoFax] = @SoFax,	
[DiaChiLienHe] = @DiaChiLienHe,	
[NgaySinh] = @NgaySinh,	
[GioiTinh] = @GioiTinh,	
[ThongTinKhac] = @ThongTinKhac,	
[Active] = @Active,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [KhachHangNguoiLienHeID] = @KhachHangNguoiLienHeID	
else 	
INSERT INTO [dbo].[KhachHangNguoiLienHe] (	
[KhachHangNguoiLienHeID],	
[KhachHangThongTinChungFK],	
[TenNguoiLienHe],	
[AccountNguoiLienHe],	
[ChucVu],	
[Email],	
[Email2],	
[Mobile],	
[Mobile2],	
[SoDienThoai],	
[SoFax],	
[DiaChiLienHe],	
[NgaySinh],	
[GioiTinh],	
[ThongTinKhac],	
[Active],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@KhachHangNguoiLienHeID,	
@KhachHangThongTinChungFK,	
@TenNguoiLienHe,	
@AccountNguoiLienHe,	
@ChucVu,	
@Email,	
@Email2,	
@Mobile,	
@Mobile2,	
@SoDienThoai,	
@SoFax,	
@DiaChiLienHe,	
@NgaySinh,	
@GioiTinh,	
@ThongTinKhac,	
@Active,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)

```
