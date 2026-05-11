# Stored Procedure: `Gen_InsertOrUpdate_PhanQuyenNguoiDungBooking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-21 13:50:52.090000
- **Ngày sửa cuối**: 2014-11-21 13:50:52.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NhanSuQuyenNguoiDungID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichREF` | `int(4)` | No |
| `@DmNhomNguoiDungREF` | `bigint(8)` | No |
| `@UserName` | `nvarchar(400)` | No |
| `@OxUserREF` | `bigint(8)` | No |
| `@LastLogInTime` | `datetime(8)` | No |
| `@KhoaDangNhapNguoiDung` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_PhanQuyenNguoiDungBooking] 	
@NhanSuQuyenNguoiDungID int ,	
@NhanSuSoYeuLyLichREF int ,	
@DmNhomNguoiDungREF bigint ,	
@UserName nvarchar (200) ,	
@OxUserREF bigint ,	
@LastLogInTime datetime ,	
@KhoaDangNhapNguoiDung int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime ,	
@LastModifiedBy nvarchar (200) ,	
@LastModifiedAt datetime ,	
@DeletedStatus int ,	
@PrintStatus int ,	
@RecordStatus int 	
As 	
if(exists(select * from [PhanQuyenNguoiDungBooking] where [NhanSuQuyenNguoiDungID] = @NhanSuQuyenNguoiDungID))	
UPDATE [dbo].[PhanQuyenNguoiDungBooking] SET 	
[NhanSuSoYeuLyLichREF] = @NhanSuSoYeuLyLichREF,	
[DmNhomNguoiDungREF] = @DmNhomNguoiDungREF,	
[UserName] = @UserName,	
[OxUserREF] = @OxUserREF,	
[LastLogInTime] = @LastLogInTime,	
[KhoaDangNhapNguoiDung] = @KhoaDangNhapNguoiDung,	
[CreatedBy] = @CreatedBy,	
[CreatedAt] = @CreatedAt,	
[LastModifiedBy] = @LastModifiedBy,	
[LastModifiedAt] = @LastModifiedAt,	
[DeletedStatus] = @DeletedStatus,	
[PrintStatus] = @PrintStatus,	
[RecordStatus] = @RecordStatus where [NhanSuQuyenNguoiDungID] = @NhanSuQuyenNguoiDungID	
else 	
INSERT INTO [dbo].[PhanQuyenNguoiDungBooking] (	
[NhanSuQuyenNguoiDungID],	
[NhanSuSoYeuLyLichREF],	
[DmNhomNguoiDungREF],	
[UserName],	
[OxUserREF],	
[LastLogInTime],	
[KhoaDangNhapNguoiDung],	
[CreatedBy],	
[CreatedAt],	
[LastModifiedBy],	
[LastModifiedAt],	
[DeletedStatus],	
[PrintStatus],	
[RecordStatus])	
Values 	
(	
@NhanSuQuyenNguoiDungID,	
@NhanSuSoYeuLyLichREF,	
@DmNhomNguoiDungREF,	
@UserName,	
@OxUserREF,	
@LastLogInTime,	
@KhoaDangNhapNguoiDung,	
@CreatedBy,	
@CreatedAt,	
@LastModifiedBy,	
@LastModifiedAt,	
@DeletedStatus,	
@PrintStatus,	
@RecordStatus)
```
